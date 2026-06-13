---
name: zhichi-shanlin
description: >-
  Composes any "space / interface / scene / path / mood" using the landscape
  spatial method of Guo Xi's Northern-Song 《林泉高致》(三远 the Three Distances ·
  可行可望可游可居 walkable/viewable/wanderable/dwellable · 虚实留白
  void-and-substance) — so AI builds not just laid-out pixels but a realm with
  depth, one you can roam and dwell in. Activates when: designing depth-bearing
  interfaces / landing pages / canvases, sequencing multi-screen multi-step
  experiences (onboarding, guided flows, narrative flows), crafting immersive
  scenes (exhibitions, incense/tea ceremony, meditation, spatial audio),
  arranging framing and a roam-route for 3D / maps / panorama / digital twins,
  reviewing AI-generated landscape scenes, or reworking spaces that feel "too
  flat / too crowded / nowhere to go / used once and never returned." One test:
  if the question is "does this space make you want to walk in, and can you," use
  this skill. Not for: backend logic / algorithms / numeric bugs, or pure
  color/font aesthetics (tiangong's job).
version: 1.0.0
date: 2026-06-02
authority: WUJI Labs
license: MIT
author: WUJI (wuji-labs)
homepage: https://github.com/wuji-labs/zhichi-shanlin
---

# WUJI Labs · 咫尺山林 ZhiChi ShanLin Skill

> 本 skill 教 AI 在一方屏幕、一段空间里经营山林——让 **咫尺之内，有万里之遥**。
> 弹药层典源为北宋郭熙《林泉高致》。AI 接手任何「空间 / 场景 / 界面 / 路径 / 意境」编排任务，读本 SKILL.md 即可导航。

---

## 一、调用场景

你正在做以下任何一件事，都应先读本 SKILL.md：

- 设计需要**空间纵深**的界面、页面、画布（不止是平铺的网格）
- 编排**多屏 / 多步 / 多场景**的体验路径（onboarding、引导流、叙事流）
- 处理**空间叙事**：让用户在有限画面里产生「身在其中」的感受
- 设计**沉浸式空间**（展陈、空间音频、香席、茶席、冥想场景）——与 `subs/tingxiang` 听香沉香空间耦合
- 为 3D / 地图 / 全景 / 数字孪生场景安排**取景与游观路线**
- 给 AI 生成的山水、园林、场景图做**空间结构审校**（有没有远近、有没有可游之路）
- 任何「画面太满 / 太平 / 没有呼吸 / 没有去处」的诊断与重构

一句判据：**当问题是「这个空间让人想不想走进去、走得进去吗」，就读本 skill。**

---

## 二、四底层原则

这四条是其他所有规则的出发点，违反任一即违反本 skill。

### 原则 1 · 三远立空间（高远 · 深远 · 平远）

来自《林泉高致·山水训》。一切空间先问：**纵深从哪来？**

| 远法 | 取景视点 | 空间感受 | 界面/场景类比 |
|------|---------|---------|--------------|
| **高远** | 自山下仰山巅 | 高峻、突兀、压强 | 英雄区 / 首屏冲击 / 仰视权威感 |
| **深远** | 自山前窥山后 | 重叠、幽深、藏隐 | 渐次揭示 / 层层下钻 / 路径有去处 |
| **平远** | 自近山望远山 | 冲融、缥缈、辽阔 | 留白远景 / 平静收束 / 视线放远 |

铁律：**一个空间至少立一种远，最好三远各司其职**。没有「远」的画面只是贴图，不是境。

### 原则 2 · 可行 · 可望 · 可游 · 可居（境的四个等级）

来自《林泉高致·山水训》：「山水有可行者，有可望者，有可游者，有可居者……但可行可望不如可游可居之为得。」

| 等级 | 含义 | 对界面/空间的要求 |
|------|------|------------------|
| 可行 | 有路可走 | 动线通、不堵死、能操作 |
| 可望 | 有景可看 | 有焦点、有看头、值得停留 |
| **可游** | 能在其中游历 | 探索有奖赏、路径有变化、值得逛 |
| **可居** | 能在其中安住 | 让人愿意长留、有归属、想回来 |

铁律：**做到「可行可望」只是合格，追求「可游可居」才算得**。AI 不能止步于「能用、好看」，要问「想不想久留」。

### 原则 3 · 经营位置，留白即境（虚实相生）

来自谢赫六法「经营位置」与郭熙「山欲高，尽出之则不高，烟霞锁其腰则高矣」。

- 空白不是「还没填的地方」，是**烟霞、是云水、是让山显高的那口气**。
- 满则塞，**塞则无境**。删到「再删就缺了」为止，留出的空白要让主体显得更大、更远、更深。
- 实景定骨，虚景生韵；先问「哪里该空」，再问「哪里该实」。

### 原则 4 · 身即山川，外师造化（先看见，再经营）

来自《林泉高致》「身即山川而取之」「饱游饫看」与张璪「外师造化，中得心源」。

- 经营任何空间前，先**真正看见**它的对象与上下文（看够、看透、看到「饱」）。
- 不照搬模板套壳；空间是从对真实场景的观照中**长出来**的，不是从网格里填出来的。
- 与 NoPUA「以道驭术 · 用信任替代恐惧」同源：**先观照、后经营，用理解驱动，而非用焦虑堆砌**。

---

## 三、弹药库导航

| 弹药 | 路径 | 装什么 |
|------|------|--------|
| 典源种子 | [reference/linquan-gaozhi.md](reference/linquan-gaozhi.md) | 《林泉高致》核心概念体系 · 三远法 · 四可 · 真引用（注书·篇） |

调用入口与样例：

| 用途 | 路径 | 装什么 |
|------|------|--------|
| 手动命令 | [commands/zhichi-shanlin.md](commands/zhichi-shanlin.md) | `/zhichi-shanlin` 显式入口 · 固定状态行 + 三段处方格式 |
| 工作样例 | [examples/01-flat-landing-page.md](examples/01-flat-landing-page.md) · [examples/02-onboarding-no-return.md](examples/02-onboarding-no-return.md) · [examples/03-overcrowded-dashboard.md](examples/03-overcrowded-dashboard.md) | input→output 对照 · 锁定输出风格 |
| 评测设计 | [benchmark/README_BENCHMARK.md](benchmark/README_BENCHMARK.md) | 7 场景 · baseline vs skill 对照 · 评分 rubric（结果待真实运行） |

平台适配入口：

| 平台 | 入口 |
|------|------|
| Claude Code | [platforms/claude-code.md](platforms/claude-code.md) |
| Codex | [platforms/codex.md](platforms/codex.md) |
| Cursor | [platforms/cursor.md](platforms/cursor.md) |

耦合 skill / 子项目：

| 相邻 | 关系 |
|------|------|
| `subs/tingxiang`（听香沉香空间） | 沉浸式香席 / 空间音景的「可游可居」编排共用本 skill 的三远与四可 |
| `labs/skills/tiangong`（天工美学） | 美学骨法（气韵 · 经营位置）与本 skill 的空间纵深互补：天工管「美不美」，咫尺山林管「进不进得去」 |

---

*WUJI Labs · 咫尺山林 ZhiChi ShanLin Skill · v1.0.0 · 2026-06-02 · MIT*
