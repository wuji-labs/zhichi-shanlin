# 咫尺山林 ZhiChi ShanLin — 咫尺之内，有万里之遥

**[🇨🇳 简体中文](README.zh-CN.md)** · **[🇺🇸 English](README.md)** · **[🇯🇵 日本語](README.ja.md)** · **[🇰🇷 한국어](README.ko.md)** · **[🇪🇸 Español](README.es.md)** · **[🇧🇷 Português](README.pt.md)** · **[🇫🇷 Français](README.fr.md)**

> English: [README.md](README.md)

这是华夏道脉献给世界开源社区的十件礼物之一(叩兩端·无极樞纽)。
我们不立华夏本位,不主张华夏文明优于任何文明;只是先从自己最熟悉的道脉开始,
把它打磨成一件可用的工具,放到人类共同的开源工具架上。希腊、那烂陀、犹太、波斯
诸文明的礼物将依次到来,共同构成十二文明对标的开源能力矩阵。

> **咫尺之內，便覺萬里為遙。**
> — 郭熙《林泉高致·山水訓》

---

## 一句话

**AI 会把屏幕填满，却从没学会在其中打开一段纵深。**
咫尺山林把北宋郭熙《林泉高致》的山水空间法注入 AI：三远立纵深、四可定等级、留白即境、步步移面面看——让 AI 不止排布像素,而是经营一片**有纵深、可游可居**的境。

## 能力对照

| 平面默认 | + 咫尺山林 | = 完整 |
|---------|-----------|--------|
| 网格:全在一个平面 | 三远:近—深—远 | 有真纵深的布局 |
| 英雄区:喊一嗓子 | 高遠:自下仰巅 | 拔地而起的冲击 |
| 信息流:无限下滚 | 可游可居:逛与住 | 想久留的地方 |
| 留白:就是padding | 烟霞锁腰:让山显高的那口气 | 会说话的空 |

## 何时自动触发

- 设计需要**纵深**的界面/落地页/画布;
- 编排**多屏多步**体验(onboarding/引导流/wizard/叙事流);
- 做**空间叙事 / 沉浸式场景**(展陈/香席/茶席/冥想/空间音景,与 `subs/tingxiang` 耦合);
- 为 3D/地图/全景/数字孪生安排**取景与游观路线**;
- 审校 AI 生成的山水园林场景图;
- 诊断重构「太平 / 太满 / 没有呼吸 / 没去处 / 用一次不回来」的空间。

**反触发**:纯后端逻辑/算法/数值 bug、与空间纵深无关的代码、单纯配色字体的美学定夺(那是 `tiangong` 的活)。

> 一句判据:**当问题是「这个空间让人想不想走进去、走得进去吗」,就用本 skill。**

## 安装

### A. 一键(Claude Code 插件)

```bash
/plugin marketplace add wuji-labs/zhichi-shanlin
/plugin install zhichi-shanlin
```

### B. 裸 clone(任意 agent / 平台)

```bash
git clone https://github.com/wuji-labs/zhichi-shanlin
cp -r zhichi-shanlin ~/.claude/skills/        # Claude Code
# Codex / Cursor 见下方平台入口
```

### 平台一键矩阵

| 平台 | 入口 | 一键 |
|------|------|------|
| Claude Code | [platforms/claude-code.md](platforms/claude-code.md) | `/plugin install zhichi-shanlin` |
| Codex | [platforms/codex.md](platforms/codex.md) | 裸 clone |
| Cursor | [platforms/cursor.md](platforms/cursor.md) | 裸 clone |

## 调用方式

- **自动**:做空间/界面/场景/路径/意境任务,说「这页太平了 / 太满 / 用户不回来 / 想让它能走进去」时,skill 自激活(触发词见 [SKILL.md](SKILL.md) 的 description)。
- **手动**:`/zhichi-shanlin [你的空间]` 显式审校,固定状态行 + 三段处方格式(见 [commands/zhichi-shanlin.md](commands/zhichi-shanlin.md))。

## before / after

| 任务 | 无咫尺山林 | 有咫尺山林 |
|------|-----------|-----------|
| 「设计这个落地页」 | 平面网格,全在一个平面 | 高遠英雄区压在烟霞遮腰的截图上 · 深遠层层揭示 · 平遠远景收束 |
| 「引导流没人回访」 | 步骤更顺,死路依旧 | 止于可行可望 → 加可游(分岔)+ 可居(属于你的位置) |
| 「dashboard 太挤」 | 缩小/删卡片 | 虚实相生:近景留几张,余者隐入烟霞,留出呼吸 |

工作样例(input→output):[examples/](examples/)
评测设计(结果待真实运行,本仓未跑出数字):[benchmark/README_BENCHMARK.md](benchmark/README_BENCHMARK.md)

## 方法论背书

弹药库 [reference/linquan-gaozhi.md](reference/linquan-gaozhi.md) 中所有标「原文」的句子均注明**书·篇**(《林泉高致·山水训》),概念框架与原文分级标注,**绝不伪托郭熙原句**。与 NoPUA「以道驭术 · 用信任替代恐惧」同源:先观照、后经营。

## 同源之礼

- [**天工 TianGong**](https://github.com/wuji-labs/tiangong) — 华夏美学设计框架。天工问「美不美」,咫尺山林问「进不进得去」,天然成对。
- [**NoPUA**](https://github.com/wuji-labs/nopua) — 以智慧而非恐惧驱动 AI。

## 基本信息

| 项 | 值 |
|----|----|
| 归属 | WUJI Labs |
| 目录 | `labs/skills/zhichi-shanlin/` |
| 许可证 | MIT |
| 上游 | github.com/wuji-labs/zhichi-shanlin |
| 典源 | 郭熙《林泉高致》Guo Xi, *Lin Quan Gao Zhi* |
| 版本 | v1.0.0 · 2026-06-02 |

---

*咫尺山林 ZhiChi ShanLin — by [WUJI](https://github.com/wuji-labs)*
*咫尺之內，便覺萬里為遙。Open a thousand miles inside an inch.*
