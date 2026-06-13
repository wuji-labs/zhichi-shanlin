#!/usr/bin/env python3
"""咫尺山林 Benchmark Analyzer — 统计分析(仅在有真实评分时出数).

读取 run_benchmark.py 落盘的 results/*.json,对 baseline vs skill 做非参检验
(Wilcoxon / Mann-Whitney)与效应量(Cohen's d)。

铁律:本脚本**只统计已由盲评填入的真实分数**(dimension_scores 中的非 None 值、
expected_actions_hit 列表)。若某记录评分仍为 None,则视为「未评分」并跳过,
**绝不**用占位/默认/编造值参与计算。无有效评分时,明确打印「无可分析的真实评分」并退出,
不输出任何捏造的 p 值或效应量。

依赖:
    pip install numpy scipy

用法:
    python analyze_results.py --input-dir results/
    python analyze_results.py --input-dir results/ --dimension grade_lift
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

DIMENSION_KEYS = [
    "depth_diagnosis", "grade_lift", "negative_space",
    "citation_fidelity", "actionability", "trigger_precision",
]


def load_records(input_dir: Path) -> list:
    records = []
    for path in sorted(input_dir.glob("*.json")):
        with path.open(encoding="utf-8") as fh:
            data = json.load(fh)
        if isinstance(data, list):
            records.extend(data)
    return records


def hit_rate(rec: dict):
    """expected_actions 命中率;未评分(None)返回 None。"""
    hit = rec.get("expected_actions_hit")
    total = rec.get("expected_actions_total") or 0
    if hit is None or total == 0:
        return None
    return len(hit) / total


def metric_value(rec: dict, metric: str):
    if metric == "hit_rate":
        return hit_rate(rec)
    return rec.get("dimension_scores", {}).get(metric)


def cohens_d(a, b):
    import numpy as np
    a, b = np.asarray(a, float), np.asarray(b, float)
    na, nb = len(a), len(b)
    if na < 2 or nb < 2:
        return None
    pooled = ((na - 1) * a.var(ddof=1) + (nb - 1) * b.var(ddof=1)) / (na + nb - 2)
    if pooled == 0:
        return 0.0
    return float((a.mean() - b.mean()) / (pooled ** 0.5))


def compare(metric: str, records: list) -> None:
    from scipy import stats

    by_cond = defaultdict(list)
    for rec in records:
        val = metric_value(rec, metric)
        if val is not None:  # 只纳入真实已评分项
            by_cond[rec["condition"]].append(val)

    base = by_cond.get("baseline", [])
    skill = by_cond.get("skill", [])
    if len(base) < 2 or len(skill) < 2:
        print(f"[{metric}] 真实评分不足(baseline={len(base)}, skill={len(skill)}),跳过。")
        return

    import numpy as np
    print(f"\n[{metric}]")
    print(f"  baseline: n={len(base)} mean={np.mean(base):.3f}")
    print(f"  skill   : n={len(skill)} mean={np.mean(skill):.3f}")

    # 非配对 Mann-Whitney(配对需对齐 scenario×run,见 README;此处给保守非参)
    try:
        u, p = stats.mannwhitneyu(skill, base, alternative="two-sided")
        print(f"  Mann-Whitney U={u:.1f}  p={p:.4g}")
    except ValueError as exc:
        print(f"  Mann-Whitney 无法计算: {exc}")
    d = cohens_d(skill, base)
    if d is not None:
        print(f"  Cohen's d={d:.3f}")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="咫尺山林 评测统计分析")
    parser.add_argument("--input-dir", required=True, help="results JSON 目录")
    parser.add_argument("--dimension", default=None,
                        help="只分析某一维度;省略则全部 + hit_rate")
    args = parser.parse_args(argv)

    input_dir = Path(args.input_dir)
    if not input_dir.exists():
        print(f"目录不存在: {input_dir}", file=sys.stderr)
        return 1

    records = load_records(input_dir)
    if not records:
        print("无结果文件。先运行 run_benchmark.py。", file=sys.stderr)
        return 1

    metrics = [args.dimension] if args.dimension else (["hit_rate"] + DIMENSION_KEYS)

    scored = any(
        metric_value(rec, m) is not None for rec in records for m in metrics
    )
    if not scored:
        print("无可分析的真实评分(所有 dimension_scores / hit 仍为 None)。")
        print("请先完成盲评填分,再运行本脚本。绝不输出编造数字。")
        return 0

    for metric in metrics:
        compare(metric, records)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
