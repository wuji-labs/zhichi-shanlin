# 咫尺山林 Benchmark Suite — 评测设计

> **状态:本文件为评测设计(scenarios + 对照条件 + 评分 rubric + 复现步骤)。结果待真实运行,本仓未跑出任何数字。**
> 下文凡涉及指标/统计,均为**方法说明**;任何 p 值、百分比、效应量、胜率在真实跑出前**一律不得填入本仓**(research-integrity 铁律)。

---

## 一、评测目的

衡量一个核心命题:在「空间 / 界面 / 场景 / 路径 / 意境」类任务上,加载 **咫尺山林 skill** 是否让 AI 产出**更有纵深、更可游可居**的方案,而非停留在「平、满、可用就好」的平面默认。

具体问:启用 skill 后,agent 是否更可能——
1. 主动诊断**纵深缺失**(三远),而非只调样式;
2. 把目标从「可行可望」(能用好看)推进到「可游可居」(想久留想回来);
3. 用**留白/虚实**而非「继续加组件」解决「太满」;
4. **精准触发**——在纯逻辑任务(场景 7)上**不**误用空间话术。

---

## 二、对照条件设计(baseline vs skill)

| 条件 | system 注入 | 说明 |
|------|------------|------|
| **baseline** | 无 skill,仅通用「请帮我改进这个设计/场景」 | 香草 agent,代表平面默认 |
| **skill** | 完整 `SKILL.md`(四底层原则 + 弹药库指针) | 加载咫尺山林 |

> 两条件用**同一题库、同一 task prompt、同一模型与采样参数**,唯一差异是 system 是否注入 SKILL.md。
> 可选第三条件 `skill+ref`:额外预载 `reference/linquan-gaozhi.md`,测「渐进式披露」对引用准确性的增益。本设计默认两条件,第三条件为加分扩展。

---

## 三、题库

`scenarios.json` 含 7 个真实场景,覆盖:

| id | category | 测什么 | 难度 |
|----|----------|--------|------|
| 1 | spatial-depth | 平面落地页 → 立三远 | medium |
| 2 | retention-depth | 引导流不回访 → 可游可居 | medium |
| 3 | negative-space | 塞满 dashboard → 留白虚实(不删内容) | hard |
| 4 | scene-narrative | 静态山水图 → 可走入的境 | medium |
| 5 | multi-step-path | 每步雷同的 wizard → 步步移面面看 | medium |
| 6 | immersive-space | 香席沉浸空间(耦合 tingxiang)→ 四时/可居 | hard |
| 7 | **anti-trigger** | 纯逻辑 bug → **不应**触发本 skill | easy |

每条含:`description`(ground-truth,不给 agent)、`task`(给 agent 的 prompt)、`expected_actions`(理想 agent 应做的动作清单,用于命中率评分)、`difficulty`。

场景 7 是**反触发对照**:用来检验 skill 的 description 是否精准——启用 skill 后在纯逻辑任务上**不应**冒出三远/可游可居话术(over-trigger 是失败,不是成功)。

---

## 四、评分 rubric

每个场景的每次运行,按两类打分。

### 4.1 expected_actions 命中率(客观,可自动/半自动)

对照该场景 `expected_actions` 列表,逐项判该次输出是否命中(命中=1,未命中=0)。
- 命中率 = 命中项 / 该场景 expected_actions 总数。
- 反触发场景 7:`expected_actions` 已写成「**不**调用空间话术、直接修 bug」——命中即「没误用」。

### 4.2 维度评分(主观,人评或 LLM-judge,每维 1–5)

| 维度 | 看什么 |
|------|--------|
| **纵深诊断(depth-diagnosis)** | 是否识别「全在一个平面 / 缺远」并对症,而非只调样式 |
| **等级跃迁(grade-lift)** | 是否把目标从可行可望推到可游可居,且给出**具体**改法 |
| **虚实运用(negative-space)** | 「太满」是否用留白/分层解,而非继续堆组件 |
| **典源准确(citation-fidelity)** | 引《林泉高致》是否注书·篇、是否伪托原文(伪托=判低) |
| **落地度(actionability)** | 处方是否「改前→改后」具体可做,而非空泛口号 |
| **触发精度(trigger-precision)** | 该触发时触发、不该触发时(场景7)不误用 |

> LLM-judge 须**盲评**:评审不知该样本来自 baseline 还是 skill,且打乱顺序,避免顺序/来源偏差。

---

## 五、统计方法(待数据)

> 以下为**方法约定**,非结果。真实跑出 ≥5 runs/场景/条件后方可计算并填表。

- **配对非参检验**:同场景 × 同 run 在 baseline vs skill 间配对 → **Wilcoxon signed-rank**。
- **非配对回退**:不可配对时 → **Mann-Whitney U**。
- **效应量**:**Cohen's d**(|d|<0.2 可忽略,0.2–0.5 小,0.5–0.8 中,>0.8 大)+ Mann-Whitney 的 rank-biserial r。
- **显著性标记**:`*` p<0.05,`**` p<0.01,`***` p<0.001,`n.s.` 不显著。
- **多场景校正**:跨 7 场景比较时用 Holm-Bonferroni 控制族错误率。

---

## 六、CLI 用法(执行器为加分项,见 `run_benchmark.py` 若存在)

> 若仓内提供 `run_benchmark.py` / `analyze_results.py`,约定接口如下;否则可手工按上述条件跑并人工评分。

```bash
# 全量:两条件 × 7 场景 × 5 runs
python run_benchmark.py --model claude-sonnet-4 --condition all --runs 5

# 单条件
python run_benchmark.py --model gpt-4o --condition skill --runs 5

# 单场景(调试)
python run_benchmark.py --model gemini-2.5-pro --scenario 3 --condition baseline --runs 1

# 干跑:只打印计划不执行
python run_benchmark.py --model claude-sonnet-4 --condition all --dry-run
```

| Flag | 含义 | 默认 |
|------|------|------|
| `--model` | claude-sonnet-4 / gpt-4o / gemini-2.5-pro | 必填 |
| `--condition` | baseline / skill / all | all |
| `--runs` | 每场景每条件运行次数 | 5 |
| `--scenario` | 指定场景 id(1–7)或全部 | 全部 |
| `--output-dir` | 结果落盘目录 | results/ |
| `--dry-run` | 只打印计划 | off |

---

## 七、输出结构

```
benchmark/
├── scenarios.json            # 7 个评测场景(本设计核心)
├── README_BENCHMARK.md       # 本文件(评测设计)
├── run_benchmark.py          # 执行器(加分,不预置任何结果数据)
├── analyze_results.py        # 统计分析(加分,仅在有真实 results 时出数)
├── test-project/             # 被测现场:场景指向的真实样本(加分)
├── results/                  # 原始结果(真实运行后生成,当前应为空)
└── analysis/                 # 分析产物(真实运行后生成,当前应为空)
```

### 单条结果记录约定(真实运行后生成)

```json
{
  "scenario_id": 1,
  "scenario_name": "Flat SaaS Landing Page",
  "condition": "skill",
  "model": "claude-sonnet-4",
  "run_number": 1,
  "timestamp": "<ISO8601>",
  "expected_actions_hit": ["...", "..."],
  "expected_actions_total": 5,
  "dimension_scores": {
    "depth_diagnosis": null,
    "grade_lift": null,
    "negative_space": null,
    "citation_fidelity": null,
    "actionability": null,
    "trigger_precision": null
  },
  "raw_response": "...",
  "error": ""
}
```

> `dimension_scores` 初始为 `null`,由盲评后填入 1–5;**禁止**预置任何非 null 占位分。

---

## 八、成本估算(量级,非承诺)

每全量(2 条件 × 7 场景 × 5 runs = 70 次主调用 + 评分调用):

| 模型 | 量级 |
|------|------|
| Claude Sonnet 4 | 几美元量级,随响应长度浮动 |
| GPT-4o | 同量级 |
| Gemini 2.5 Pro | 同量级 |

> 仅供规划,非精确报价。

---

## 九、复现步骤

1. 装依赖:`pip install anthropic openai google-generativeai numpy scipy`(+ 评分若用 LLM-judge)。
2. 设对应模型的 API key 环境变量。
3. 准备被测现场:`test-project/` 含各场景引用的真实样本(落地页结构、wizard 截图描述、香席脚本等)。
4. 跑 baseline 与 skill 两条件(同模型、同参数、同题库)。
5. **盲评**:打乱来源后按 §4 rubric 打分。
6. 按 §5 统计,填表、出图。
7. 报告须含:模型版本、日期、runs 数、采样参数、题库 commit hash。

---

## 十、加场景

编辑 `scenarios.json` 追加一条,字段同上(`id/category/name/description/task/expected_actions/difficulty`),并确保 `test-project/` 有对应的真实被测样本——**场景不得凭空,须指向可复现的现场**。

---

> 再次强调:**本仓当前无任何评测结果数字。** 任何 README/对外材料引用本 benchmark 的「效果」时,在真实跑出并落盘前,只能描述**设计**,不得给出 before/after 数字。
