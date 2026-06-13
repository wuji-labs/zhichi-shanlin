# 平台适配 · Codex

在 Codex(含 app-server 长连接 / exec)中加载与调用 咫尺山林(zhichi-shanlin)。

## 安装

```bash
cp -r labs/skills/zhichi-shanlin ~/.codex/skills/
```

或在本仓库内通过 workspace 依赖 `@labs-skills/zhichi-shanlin` 直接引用。

## 调用

1. 在 Codex 的 prompt / AGENTS 上下文中，将本 skill 的 [SKILL.md](../SKILL.md) 作为「空间·境」任务的起手参考。
2. 强制起手为 SKILL.md「二、四底层原则」：
   - 原则1 三远(高远/深远/平远)——先立纵深
   - 原则2 可行可望可游可居——定境的等级
   - 原则3 经营位置，留白即境——虚实相生
   - 原则4 身即山川，外师造化——先看见再经营
3. 典源原文/概念取自弹药库 [reference/linquan-gaozhi.md](../reference/linquan-gaozhi.md)，引用注「书·篇」。

## 适配要点

- Codex 长连接(app-server)场景下，可把「四底层原则」摘要常驻系统提示，让空间相关任务默认带三远与四可视角。
- exec 一次性场景下，按需读 SKILL.md + reference 即可。

## 与其他 skill 协同

- 配 `labs/skills/tiangong`(美学骨法)、`subs/tingxiang`(沉浸空间)。

## 不做什么

- 不改动用户内容本意；只经营空间结构。
- 不杜撰典源原文。
