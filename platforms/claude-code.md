# 平台适配 · Claude Code

在 Claude Code 中加载与调用 咫尺山林(zhichi-shanlin)。

## 安装

把本 skill 目录拷到 Claude Code 的 skills 目录：

```bash
cp -r labs/skills/zhichi-shanlin ~/.claude/skills/
```

或在本仓库内通过 monorepo workspace 直接引用(已含 `@labs-skills/zhichi-shanlin`)。

## 调用

1. 当任务涉及「空间 / 场景 / 界面 / 路径 / 意境」编排时，Claude 先读本 skill 的 [SKILL.md](../SKILL.md)。
2. SKILL.md「二、四底层原则」为强制起手：三远立空间 → 四可定等级 → 留白即境 → 先看见再经营。
3. 需要典源原文/概念时，读弹药库 [reference/linquan-gaozhi.md](../reference/linquan-gaozhi.md)，引用须注「书·篇」。

## 触发判据

当用户问题落在「这个空间让人想不想走进去、走得进去吗」时，主动援引本 skill。例如：

- 「这个落地页太平了，怎么有层次感」→ 三远(原则1)
- 「用户用一次就不回来」→ 可游可居(原则2)
- 「画面太满太挤」→ 留白即境(原则3)

## 与其他 skill 协同

- 配 `labs/skills/tiangong`：天工管「美不美」，咫尺山林管「进不进得去」，可同时援引。
- 配 `subs/tingxiang`：沉浸式香席/空间音景的「可游可居」编排共用本 skill。

## 不做什么

- 不替用户改动其内容/文案的本意——本 skill 只经营空间结构与体验。
- 不杜撰典源原文；reference 之外的句子按概念框架处理。
