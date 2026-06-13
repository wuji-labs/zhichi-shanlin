# test-project — 被测现场样本

> benchmark/scenarios.json 中各场景引用的真实样本上下文,保证场景非凭空、结果可复现。
> 这些不是「正确答案」,而是给 agent 评测时可附带的**真实输入物料**(供 baseline 与 skill 两条件同样接收)。

## 文件对照

| 场景 id | 样本文件 | 内容 |
|---------|---------|------|
| 1 | `landing-page.html` | 平面 SaaS 落地页的真实结构骨架(可在浏览器打开) |
| 3 | `dashboard-layout.json` | 18 卡监控 dashboard 的卡片清单与布局 |
| 5 | `import-wizard-steps.md` | 6 步雷同 wizard 的逐步描述 |
| 6 | `incense-ceremony-script.md` | 香席沉浸空间的现有 20 分钟脚本 |
| 7 | `billing.py` | 含整数除法取整 bug 的计税函数(反触发场景) |

场景 2、4 为纯文字描述型(task 内已自包含足够上下文),不需额外样本文件。

## 用法

评测时把对应样本随 task prompt 一并提供给 agent(两条件一致),再按 README_BENCHMARK.md 的 rubric 评分。
样本可按需扩充,但新增场景必须配真实样本——场景不得凭空。
