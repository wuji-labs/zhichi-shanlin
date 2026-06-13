#!/usr/bin/env python3
"""咫尺山林 Benchmark Runner — baseline vs skill 对照评测执行器.

对每个场景在两个条件(baseline / skill)下调用一个 LLM,落盘原始响应。
本脚本**不预置、不编造任何评测结果数字**:dimension_scores 一律为 None,
留待后续盲评(人评或 LLM-judge)填入。expected_actions 命中率亦不在此自动判定,
仅落盘 raw response 供评分阶段对照(避免脚本自评偏差)。

依赖(显式列出,按需安装):
    pip install anthropic            # --provider anthropic
    pip install openai               # --provider openai
    pip install google-generativeai  # --provider google
仅 --dry-run 时不需要任何 provider SDK 与 API key。

用法:
    python run_benchmark.py --model claude-sonnet-4 --condition all --runs 5
    python run_benchmark.py --model gpt-4o --condition skill --scenario 3
    python run_benchmark.py --model claude-sonnet-4 --condition all --dry-run
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# --- 配置 ------------------------------------------------------------------

MODELS = {
    "claude-sonnet-4": {"provider": "anthropic", "model_id": "claude-sonnet-4-20250514"},
    "gpt-4o": {"provider": "openai", "model_id": "gpt-4o"},
    "gemini-2.5-pro": {"provider": "google", "model_id": "gemini-2.5-pro"},
}

CONDITIONS = ["baseline", "skill"]
DEFAULT_RUNS = 5
DEFAULT_OUTPUT_DIR = "results"

# 路径锚定到本脚本,正斜杠由 pathlib 处理,跨平台安全。
BENCH_DIR = Path(__file__).resolve().parent
SKILL_DIR = BENCH_DIR.parent
SKILL_MD_PATH = SKILL_DIR / "SKILL.md"
SCENARIOS_PATH = BENCH_DIR / "scenarios.json"

# baseline 条件的通用 system,不含任何咫尺山林内容。
BASELINE_SYSTEM = (
    "You are a senior product/experience designer. Help the user improve the "
    "design, scene, or flow they describe. Be concrete and actionable."
)

# 评分维度键(全部初始化为 None,禁止预置占位分)。
DIMENSION_KEYS = [
    "depth_diagnosis",
    "grade_lift",
    "negative_space",
    "citation_fidelity",
    "actionability",
    "trigger_precision",
]

MAX_OUTPUT_TOKENS = 2048


# --- 加载 ------------------------------------------------------------------

def load_scenarios() -> list:
    if not SCENARIOS_PATH.exists():
        raise FileNotFoundError(f"scenarios.json not found at {SCENARIOS_PATH}")
    with SCENARIOS_PATH.open(encoding="utf-8") as fh:
        return json.load(fh)


def load_skill_system() -> str:
    """skill 条件的 system = 完整 SKILL.md 正文。"""
    if not SKILL_MD_PATH.exists():
        raise FileNotFoundError(f"SKILL.md not found at {SKILL_MD_PATH}")
    return SKILL_MD_PATH.read_text(encoding="utf-8")


def system_for(condition: str, skill_text: str) -> str:
    if condition == "baseline":
        return BASELINE_SYSTEM
    if condition == "skill":
        return skill_text
    raise ValueError(f"unknown condition: {condition}")


# --- provider 调用 ----------------------------------------------------------

def call_anthropic(model_id: str, system: str, user: str) -> str:
    try:
        import anthropic
    except ImportError as exc:
        raise RuntimeError(
            "anthropic SDK 未安装。运行: pip install anthropic"
        ) from exc
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise RuntimeError("环境变量 ANTHROPIC_API_KEY 未设置。")
    client = anthropic.Anthropic(api_key=key)
    resp = client.messages.create(
        model=model_id,
        max_tokens=MAX_OUTPUT_TOKENS,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    return "".join(block.text for block in resp.content if block.type == "text")


def call_openai(model_id: str, system: str, user: str) -> str:
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError("openai SDK 未安装。运行: pip install openai") from exc
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("环境变量 OPENAI_API_KEY 未设置。")
    client = OpenAI(api_key=key)
    resp = client.chat.completions.create(
        model=model_id,
        max_tokens=MAX_OUTPUT_TOKENS,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return resp.choices[0].message.content or ""


def call_google(model_id: str, system: str, user: str) -> str:
    try:
        import google.generativeai as genai
    except ImportError as exc:
        raise RuntimeError(
            "google-generativeai 未安装。运行: pip install google-generativeai"
        ) from exc
    key = os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise RuntimeError("环境变量 GOOGLE_API_KEY 未设置。")
    genai.configure(api_key=key)
    model = genai.GenerativeModel(model_id, system_instruction=system)
    resp = model.generate_content(user)
    return resp.text or ""


PROVIDER_DISPATCH = {
    "anthropic": call_anthropic,
    "openai": call_openai,
    "google": call_google,
}


def call_model(provider: str, model_id: str, system: str, user: str) -> str:
    fn = PROVIDER_DISPATCH.get(provider)
    if fn is None:
        raise ValueError(f"unknown provider: {provider}")
    return fn(model_id, system, user)


# --- 单次运行 --------------------------------------------------------------

def run_one(scenario: dict, condition: str, model_key: str, model_cfg: dict,
            run_number: int, skill_text: str, dry_run: bool) -> dict:
    system = system_for(condition, skill_text)
    user = scenario["task"]
    record = {
        "scenario_id": scenario["id"],
        "scenario_name": scenario["name"],
        "condition": condition,
        "model": model_key,
        "run_number": run_number,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "expected_actions_total": len(scenario.get("expected_actions", [])),
        # 评分留空:严禁预置任何非 None 占位分。
        "expected_actions_hit": None,
        "dimension_scores": {key: None for key in DIMENSION_KEYS},
        "raw_response": None,
        "error": "",
    }
    if dry_run:
        record["raw_response"] = "[dry-run: 未实际调用模型]"
        return record
    try:
        record["raw_response"] = call_model(
            model_cfg["provider"], model_cfg["model_id"], system, user
        )
    except Exception as exc:  # 自处理:把失败落进记录,不甩回上层崩溃。
        record["error"] = f"{type(exc).__name__}: {exc}"
    return record


# --- 主流程 ----------------------------------------------------------------

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="咫尺山林 baseline vs skill 评测执行器")
    parser.add_argument("--model", required=True, choices=sorted(MODELS),
                        help="评测模型")
    parser.add_argument("--condition", default="all",
                        choices=["baseline", "skill", "all"],
                        help="评测条件")
    parser.add_argument("--runs", type=int, default=DEFAULT_RUNS,
                        help="每场景每条件运行次数")
    parser.add_argument("--scenario", type=int, default=None,
                        help="指定场景 id;省略则全部")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR,
                        help="结果落盘目录")
    parser.add_argument("--dry-run", action="store_true",
                        help="只打印计划并落盘占位记录,不调用模型")
    args = parser.parse_args(argv)

    scenarios = load_scenarios()
    if args.scenario is not None:
        scenarios = [s for s in scenarios if s["id"] == args.scenario]
        if not scenarios:
            print(f"无 id={args.scenario} 的场景", file=sys.stderr)
            return 1

    conditions = CONDITIONS if args.condition == "all" else [args.condition]
    model_cfg = MODELS[args.model]
    # dry-run 不读 SKILL.md 失败也无妨;非 dry-run 才硬依赖。
    skill_text = ""
    if "skill" in conditions:
        if args.dry_run and not SKILL_MD_PATH.exists():
            skill_text = "[dry-run: SKILL.md 未加载]"
        else:
            skill_text = load_skill_system()

    out_dir = (BENCH_DIR / args.output_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    plan = len(scenarios) * len(conditions) * args.runs
    print(f"计划: {len(scenarios)} 场景 × {len(conditions)} 条件 × {args.runs} runs "
          f"= {plan} 次调用 (model={args.model}, dry_run={args.dry_run})")

    for condition in conditions:
        records = []
        for scenario in scenarios:
            for run_number in range(1, args.runs + 1):
                rec = run_one(scenario, condition, args.model, model_cfg,
                              run_number, skill_text, args.dry_run)
                records.append(rec)
                tag = "DRY" if args.dry_run else ("ERR" if rec["error"] else "ok")
                print(f"  [{tag}] s{scenario['id']} {condition} run{run_number}")
        out_path = out_dir / f"{args.model}_{condition}.json"
        with out_path.open("w", encoding="utf-8") as fh:
            json.dump(records, fh, ensure_ascii=False, indent=2)
        print(f"  -> 写入 {out_path}")

    print("完成。dimension_scores 全为 None,待盲评填入(禁止编造)。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
