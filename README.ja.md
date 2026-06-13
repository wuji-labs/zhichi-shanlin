# 咫尺山林 ZhiChi ShanLin — 寸の内に山林を（Mountains Within an Inch）

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/zhichi-shanlin"><img src="https://www.skills.sh/b/wuji-labs/zhichi-shanlin" alt="skills.sh"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

**[🇨🇳 中文](README.zh-CN.md)** | **[🇺🇸 English](README.md)** | **🇯🇵 日本語** | **[🇰🇷 한국어](README.ko.md)** | **[🇪🇸 Español](README.es.md)** | **[🇧🇷 Português](README.pt.md)** | **[🇫🇷 Français](README.fr.md)**

これは華夏の道脈が世界のオープンソース・コミュニティに捧げる十の贈り物のひとつです（叩兩端・無極樞紐）。
私たちは華夏本位を立てず、華夏文明が他のいかなる文明よりも優れているとも主張しません。ただ、自分たちが最もよく知る道脈からまず始め、
それを使える道具へと磨き上げ、人類共通のオープンソースの道具棚に置くだけです。やがてギリシャ、ナーランダ、
ユダヤ、ペルシャといった諸文明の贈り物も順に届き、十二文明に対標するオープンソース能力の体系を共に成していきます。

EN: This is one of ten gifts the Chinese stream of wisdom offers to the world's
open-source community. We make no claim that any civilization is superior; we
simply begin with the lineage we know best, and place it on humanity's shared
toolshelf. Gifts from the Greek, Nalanda, Hebrew, and Persian streams will follow.

---

> **咫尺之內，便覺萬里為遙** — 寸の内にして、なお万里の遥かさを覚える。
> — 郭熙《林泉高致·山水訓》, Guo Xi, *Linquan Gaozhi*（『林泉高致』「山水を望むの心得」）

**あなたのAIは画面を埋め尽くす。だが、その内に一段の奥行きを開くことを学んだことがない。**

AIの空間学習はたいてい平面的です。グリッド、ヒーローセクション、フィード——すべてがひとつの面に、ひとつの距離に置かれ、どこへも行けません。ピクセルは配置されるが、空間が*経営*されることはない。

**咫尺山林**（ZhiChi ShanLin）は、千年にわたる華夏の山水空間の術をAIに教えます——いかにして一寸の内に山脈まるごとを収めるか、いかにして余白に奥行きを湛えさせるか、そして、人が本当に歩み入り、留まりたくなる場をいかにして築くか。

## 課題

```
あなた：「このシーン / ページ / 空間をデザインして。」
咫尺山林なしのAI： 完璧なグリッド。すべてが見える。すべてが平ら。
                    使えるし、見栄えも悪くない……だが奥行きがなく、道がなく、留まる理由がない。
咫尺山林ありのAI： 近くの岩、曲がりくねる小道、霞へと溶けゆく遠峰。
                    山を高く感じさせる余白。
                    歩み抜け（可遊）、そこに住める（可居）場。
```

## AIに何を教えるか

### 🏔️ 三遠法（Three Distances：三遠法、11世紀）

郭熙『林泉高致』より——いかにして一枚の画面が真の奥行きを宿すか：

| 距離 | 漢語 | 視点 | 感じ | UI / シーンでの用法 |
|------|------|------|------|------------------|
| High Distance（高遠） | 高遠 | 山の麓から仰ぎ見る | 聳え立ち、切り立つ | ヒーローの衝撃、垂直の威厳 |
| Deep Distance（深遠） | 深遠 | 山の手前から背後を覗き込む | 重なり、隠れる | 段階的開示、行く先がある |
| Level Distance（平遠） | 平遠 | 近い峰から遠い峰を眺めわたす | 広やか、漂い、静か | 遠い地平、静かな収束 |

### 🚶 空間の四つの段階（可行可望可游可居）

> 山水有可行者，有可望者，有可游者，有可居者……但可行可望不如可游可居之為得。
> 山水には行くべきものあり、望むべきものあり、遊ぶべきものあり、住むべきものあり……されど行き望むは、遊び住むには及ばぬものなり。

| 段階 | 漢語 | 意味 | 立てる基準 |
|------|------|------|-----------|
| Walkable（可行） | 可行 | 道がある | 流れが通り、行き止まりがない |
| Viewable（可望） | 可望 | 見るべきものがある | 焦点があり、立ち止まる価値がある |
| **Wanderable（可遊）** | 可遊 | 巡り歩く価値がある | 探索が報われる |
| **Dwellable（可居）** | 可居 | 留まる価値がある | また訪れたくなる |

> 「使えて、きれい」は単なる及第点にすぎません。目指すのは**可遊・可居**です。

### 🌫️ 余白こそ山の高さ（虛實相生：空と実が互いに生み合う）

> 山欲高，盡出之則不高，煙霞鎖其腰則高矣。
> 山を高く見せたければ、その全てを描き出してはかえって高くならぬ——霞にその腰を巻かせよ、さすれば聳える。
> — Guo Xi, *Linquan Gaozhi · Shanshui Xun*（郭熙『林泉高致』「山水訓」）

留白（余白）とは「まだ埋めていない部分」ではありません。それは霞であり、雲であり、山を高く立たせる呼吸そのものです。すべてを埋めれば、奥行きは死にます。

### 👁️ 経営する前に、まず観よ（身即山川 · 外師造化）

> 身即山川而取之 — 身をもって山川となり、そこから取れ。

いかなる空間を経営する前にも、それを*まことに観る*こと——その文脈、その事物を、観るに飽き足りるまで（饱游饫看）。空間は観照から育つものであって、テンプレートから捺印されるものではありません。これは**NoPUA**と同根です——不安に駆られて積み上げるのではなく、理解によって駆動せよ。

## インストール

### A. ワンクリック（Claude Code プラグイン）

```bash
# このスキルのマーケットプレイスを追加し、プラグインをインストール
/plugin marketplace add wuji-labs/zhichi-shanlin
/plugin install zhichi-shanlin
```

### B. 裸クローン（任意の agent / プラットフォーム）

```bash
git clone https://github.com/wuji-labs/zhichi-shanlin
cp -r zhichi-shanlin ~/.claude/skills/        # Claude Code
# Codex / Cursor：下記のプラットフォーム別入口を参照
```

### プラットフォーム別の入口

| プラットフォーム | 入口 | ワンクリック |
|----------------|------|------------|
| Claude Code | [platforms/claude-code.md](platforms/claude-code.md) | `/plugin install zhichi-shanlin` |
| Codex | [platforms/codex.md](platforms/codex.md) | 裸クローン |
| Cursor | [platforms/cursor.md](platforms/cursor.md) | 裸クローン |

### 呼び出し方

- **自動** — 空間 / UI / シーン / 経路 / 意境にかかわる作業をしていて、
  *「このページは平板すぎる」「詰め込みすぎ」「ユーザーが戻ってこない」「歩み入れる感じにしたい」* といったことを言うと、
  スキルが自ら起動します（[SKILL.md](SKILL.md) の `description` トリガーを参照）。
- **手動** — `/zhichi-shanlin [あなたの空間]` を実行すると、固定のステータス行 + 三部構成の処方フォーマットで明示的に審校します
  （[commands/zhichi-shanlin.md](commands/zhichi-shanlin.md) を参照）。

### Before / After

| 課題 | 咫尺山林なし | 咫尺山林あり |
|------|-------------|-------------|
| 「このランディングページをデザインして」 | 平らなグリッド、すべてが一つの面 | 霞に腰を覆われたスクリーンショットの上に高遠のヒーロー、深遠の段階的開示、平遠の遠景 |
| 「誰も戻ってこないオンボーディング」 | 手順は滑らかに、だが行き止まりは同じ | 可行可望で止まっている → 可遊（分岐）+ 可居（あなた自身の場所）を加える |
| 「ダッシュボードが詰め込みすぎ」 | カードを縮小 / 削除する | 虚実相生：いくつかを近景に引き立て、残りを霞に隠し、呼吸する烟霞を残す |

入力→出力の実例：[examples/](examples/) ·
再現可能な評価設計（実走による数値は未取得）：[benchmark/README_BENCHMARK.md](benchmark/README_BENCHMARK.md)。

中文版 README：[README.zh-CN.md](README.zh-CN.md)

## 東西の出会い

咫尺山林はフラットデザインの規律を置き換えるものではありません。その**内に奥行きを開く**ものです。

| 平面のデフォルト | + 咫尺山林 | = 完成形 |
|----------------|-----------|---------|
| グリッド：すべてが一つの面 | 三遠：近・深・遠 | 真の奥行きをもつレイアウト |
| ヒーローセクション：一声叫ぶ | 高遠：仰ぎ見る | 聳え立つ衝撃 |
| フィード：果てしないスクロール | 可遊可居：巡り、住む | 留まる価値のある場 |
| 余白：ただのpadding | 留白：峰を持ち上げる霞 | 物を言う空 |

> **可行可望不如可游可居之為得。**
> 行き望むは、遊び住むには及ばぬものなり。
> — Guo Xi, *Linquan Gaozhi*（郭熙『林泉高致』）

## 同じ流れより

- [**天工 TianGong**](https://github.com/wuji-labs/tiangong) — 華夏美学のデザインフレームワーク。自然に対をなします：天工は*美しいか*を問い、咫尺山林は*歩み入れるか*を問います。
- [**NoPUA**](https://github.com/wuji-labs/nopua) — 恐怖ではなく知恵でAIを駆動する。

## 基本情報

| 項目 | 値 |
|------|----|
| 帰属 | WUJI Labs |
| ディレクトリ | `labs/skills/zhichi-shanlin/` |
| ライセンス | MIT |
| 上流 | github.com/wuji-labs/zhichi-shanlin |
| 典源 | 郭熙《林泉高致》Guo Xi, *Linquan Gaozhi* |
| バージョン | v1.0 · 2026-06-02 |

---

*咫尺山林 ZhiChi ShanLin — by [WUJI](https://github.com/wuji-labs)*
*咫尺之內，便覺萬里為遙。寸の内に万里を開く。*
