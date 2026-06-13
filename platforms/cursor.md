# 平台适配 · Cursor

在 Cursor 中加载与调用 咫尺山林(zhichi-shanlin)。

## 安装

Cursor 通过 `.cursor/rules/` 加载规则。把本 skill 摘要为一条 rule：

1. 在项目 `.cursor/rules/` 下新建 `zhichi-shanlin.mdc`。
2. 规则正文引用本 skill 的四底层原则(见下「规则模板」)，并指向仓库内 [SKILL.md](../SKILL.md) 与弹药库 [reference/linquan-gaozhi.md](../reference/linquan-gaozhi.md) 作为完整出处。

## 规则模板(可粘进 .mdc)

```md
---
description: 空间·境——为界面/场景注入山水空间法(三远·四可)
globs:
alwaysApply: false
---

# 咫尺山林 · 空间经营规则

做任何「空间/场景/界面/路径/意境」编排时，依次自检：

1. 三远：这个画面立了高远/深远/平远中的哪一种?至少一种,最好近-中-远各有交代。
2. 四可:做到可行可望(能用好看)只是合格;有没有可游可居(想久留、想回来)?
3. 留白:空白是让主体显高显远的"烟霞",不是没填;满则塞,塞则无境。
4. 先看见:先看够对象与上下文,再经营;不照搬模板套壳。

典源:郭熙《林泉高致·山水训》。引用原文须注书·篇,勿杜撰。
```

## 触发判据

当改动涉及布局纵深、引导流、空间叙事、画面"太平/太满/没去处"时套用本规则。

## 与其他 skill 协同

- 配 `tiangong`(美学)、`tingxiang`(沉浸空间)的 Cursor rule 并用。

## 不做什么

- 不改动内容本意;只经营空间结构。
- 不杜撰典源原文;reference 之外按概念框架处理。
