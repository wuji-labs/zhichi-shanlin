# 咫尺山林 ZhiChi ShanLin — Mountains Within an Inch

这是华夏道脉献给世界开源社区的十件礼物之一(叩兩端·无极樞纽)。
我们不立华夏本位,不主张华夏文明优于任何文明;我们只是先从自己最熟悉的道脉开始,
把它打磨成一件可用的工具,放到人类共同的开源工具架上。未来还会有希腊、那烂陀、
犹太、波斯诸文明的礼物依次到来,共同构成十二文明对标的开源能力矩阵。

EN: This is one of ten gifts the Chinese stream of wisdom offers to the world's
open-source community. We make no claim that any civilization is superior; we
simply begin with the lineage we know best, and place it on humanity's shared
toolshelf. Gifts from the Greek, Nalanda, Hebrew, and Persian streams will follow.

---

> **咫尺之内，便覺萬里為遙** — Within an inch, one feels ten thousand miles of distance.
> — 郭熙《林泉高致·山水訓》, Guo Xi, *Lin Quan Gao Zhi*

**Your AI fills the screen. It has never learned to open a distance inside it.**

Most AI spatial training is flat: a grid, a hero section, a feed. Everything sits on one plane, at one distance, with nowhere to go. Pixels are placed; space is never *composed*.

**咫尺山林** (ZhiChi ShanLin) teaches AI the thousand-year Chinese art of landscape space — how to put a whole mountain range inside one inch, how to make empty space hold the depth, and how to build a place a person actually wants to walk into and stay.

## The Problem

```
You: "Design this scene / page / space."
AI without 咫尺山林: Perfect grid. Everything visible. Everything flat.
                    Usable, looks fine... but no depth, no path, no reason to stay.
AI with 咫尺山林:    A near rock, a winding path, a far peak dissolving into mist.
                    Empty space that makes the mountain feel high.
                    A place you can walk through (可游) and dwell in (可居).
```

## What It Teaches AI

### 🏔️ The Three Distances (三遠法, 11th century)

From Guo Xi's *Lin Quan Gao Zhi* — how a single frame holds real depth:

| Distance | Chinese | Vantage | Feeling | UI / Scene use |
|----------|---------|---------|---------|----------------|
| High Distance | 高遠 | Looking up from the foot of the mountain | Towering, abrupt | Hero impact, vertical authority |
| Deep Distance | 深遠 | Peering from the front to behind the mountain | Layered, hidden | Progressive disclosure, somewhere to go |
| Level Distance | 平遠 | Gazing from a near peak to a far one | Vast, drifting, calm | Far horizon, quiet resolution |

### 🚶 The Four Grades of Space (可行可望可游可居)

> 山水有可行者，有可望者，有可游者，有可居者……但可行可望不如可游可居之為得。
> A landscape may be walkable, viewable, wanderable, dwellable — but the walkable and viewable do not measure up to the wanderable and dwellable.

| Grade | Chinese | Means | The bar it sets |
|-------|---------|-------|-----------------|
| Walkable | 可行 | A path exists | Flow works, nothing dead-ends |
| Viewable | 可望 | Something to see | Focus, worth a pause |
| **Wanderable** | 可遊 | Worth roaming | Exploration rewards you |
| **Dwellable** | 可居 | Worth staying | You want to come back |

> "Usable and pretty" is merely passing. The goal is **wanderable and dwellable**.

### 🌫️ Empty Space Is the Mountain's Height (虛實相生)

> 山欲高，盡出之則不高，煙霞鎖其腰則高矣。
> If you would have a mountain seem high, show all of it and it will not — let mist gird its waist, and it rises.
> — Guo Xi, *Lin Quan Gao Zhi · Shan Shui Xun*

Empty space is not "the part not yet filled." It is the mist, the cloud, the breath that lets the mountain stand tall. Fill everything and the depth dies.

### 👁️ See It Before You Compose It (身即山川 · 外師造化)

> 身即山川而取之 — Make your body the mountains and rivers, and take from them.

Before composing any space, *truly see* it — its context, its objects, until you have seen your fill (饱游饫看). Space is grown from observation, not stamped from a template. This is the same root as **NoPUA**: drive by understanding, not by anxious piling-on.

## Installation

### A. One-click (Claude Code plugin)

```bash
# add this skill's marketplace, then install the plugin
/plugin marketplace add wuji-labs/zhichi-shanlin
/plugin install zhichi-shanlin
```

### B. Bare clone (any agent / platform)

```bash
git clone https://github.com/wuji-labs/zhichi-shanlin
cp -r zhichi-shanlin ~/.claude/skills/        # Claude Code
# Codex / Cursor: see the per-platform entry points below
```

### Per-platform entry points

| Platform | Entry | One-click |
|----------|-------|-----------|
| Claude Code | [platforms/claude-code.md](platforms/claude-code.md) | `/plugin install zhichi-shanlin` |
| Codex | [platforms/codex.md](platforms/codex.md) | bare clone |
| Cursor | [platforms/cursor.md](platforms/cursor.md) | bare clone |

### How it's invoked

- **Automatic** — when you work on a space/UI/scene/path/意境 task and say things like
  *"this page is too flat" / "too crowded" / "users don't come back" / "make it feel walkable"*,
  the skill self-activates (see the `description` triggers in [SKILL.md](SKILL.md)).
- **Manual** — run `/zhichi-shanlin [your space]` for an explicit audit with a fixed
  status-line + three-part prescription format (see [commands/zhichi-shanlin.md](commands/zhichi-shanlin.md)).

### Before / After

| Task | Without 咫尺山林 | With 咫尺山林 |
|------|-----------------|--------------|
| "Design this landing page" | Flat grid, everything on one plane | 高遠 hero over a mist-veiled screenshot, 深遠 progressive reveal, 平遠 far-ground |
| "Onboarding nobody returns to" | Smoother steps, same dead-end | Stops at 可行可望 → adds 可游 (a branch) + 可居 (a place that's yours) |
| "Dashboard is too crowded" | Shrink/delete cards | 虚实相生: promote a few to near-ground, veil the rest, keep the breathing 烟霞 |

Worked input→output examples: [examples/](examples/) ·
Reproducible evaluation design (results pending real runs): [benchmark/README_BENCHMARK.md](benchmark/README_BENCHMARK.md).

中文版 README: [README.zh-CN.md](README.zh-CN.md)

## East Meets West

咫尺山林 doesn't replace flat-design discipline. It **opens a depth inside it**.

| Flat default | + 咫尺山林 | = Complete |
|--------------|-----------|------------|
| Grid: everything on one plane | 三遠: near, deep, far | Layout with real depth |
| Hero section: shout once | 高遠: looking up | Impact that towers |
| Feed: endless scroll | 可遊可居: roam and dwell | A place worth staying |
| Whitespace: padding | 留白: mist that lifts the peak | Emptiness that speaks |

> **可行可望不如可游可居之為得。**
> Walkable and viewable do not measure up to wanderable and dwellable.
> — Guo Xi, *Lin Quan Gao Zhi*

## From the Same Stream

- [**TianGong 天工**](https://github.com/wuji-labs/tiangong) — Chinese aesthetic design framework. Pairs naturally: TianGong asks *is it beautiful*; 咫尺山林 asks *can you walk into it*.
- [**NoPUA**](https://github.com/wuji-labs/nopua) — Drive AI with wisdom instead of fear.

## 基本信息

| 项 | 值 |
|----|----|
| 归属 | WUJI Labs |
| 目录 | `labs/skills/zhichi-shanlin/` |
| 许可证 | MIT |
| 上游 | github.com/wuji-labs/zhichi-shanlin |
| 典源 | 郭熙《林泉高致》Guo Xi, *Lin Quan Gao Zhi* |
| 版本 | v1.0 · 2026-06-02 |

---

*咫尺山林 ZhiChi ShanLin — by [WUJI](https://github.com/wuji-labs)*
*咫尺之內，便覺萬里為遙。Open a thousand miles inside an inch.*
