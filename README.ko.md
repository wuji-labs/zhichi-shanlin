# 咫尺山林 ZhiChi ShanLin — 한 치 안의 산림(Mountains Within an Inch)

<p align="center">
  <a href="https://www.skills.sh/wuji-labs/zhichi-shanlin"><img src="https://www.skills.sh/b/wuji-labs/zhichi-shanlin" alt="skills.sh"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/wuji-labs/huaxia-skills"><img src="https://img.shields.io/badge/%E5%8D%8E%E5%A4%8F%E5%8D%81%E5%A4%A7-HuaXia%20Skills-c1272d" alt="HuaXia Skills"></a>
</p>

**[🇨🇳 中文](README.zh-CN.md)** | **[🇺🇸 English](README.md)** | **[🇯🇵 日本語](README.ja.md)** | **🇰🇷 한국어** | **[🇪🇸 Español](README.es.md)** | **[🇧🇷 Português](README.pt.md)** | **[🇫🇷 Français](README.fr.md)**

이것은 화하(華夏)의 도맥(道脈)이 세계 오픈소스 커뮤니티에 바치는 열 가지 선물 중 하나입니다(고양단·무극추뉴, 叩兩端·無極樞紐).
우리는 화하 본위를 내세우지 않으며, 화하 문명이 그 어떤 문명보다 우월하다고 주장하지도 않습니다. 다만 우리가 가장 잘 아는 도맥에서 먼저 시작하여,
그것을 쓸 만한 도구로 다듬어, 인류 공동의 오픈소스 도구 선반에 올려둘 뿐입니다. 앞으로 그리스, 날란다,
유대, 페르시아 등 여러 문명의 선물이 차례로 도착하여, 열두 문명에 대표(對標)하는 오픈소스 능력의 행렬을 함께 이룰 것입니다.

EN: This is one of ten gifts the Chinese stream of wisdom offers to the world's
open-source community. We make no claim that any civilization is superior; we
simply begin with the lineage we know best, and place it on humanity's shared
toolshelf. Gifts from the Greek, Nalanda, Hebrew, and Persian streams will follow.

---

> **咫尺之內，便覺萬里為遙** — 한 치 안에서, 만 리의 아득함을 느낀다.
> — 郭熙《林泉高致·山水訓》, Guo Xi, *Linquan Gaozhi*(『임천고치(林泉高致)』 「산수를 그리는 가르침」)

**당신의 AI는 화면을 가득 채운다. 그러나 그 안에 한 겹의 깊이를 여는 법은 한 번도 배운 적이 없다.**

AI의 공간 학습은 대체로 평면적입니다. 그리드, 히어로 섹션, 피드 — 모든 것이 하나의 평면, 하나의 거리에 놓여, 어디로도 갈 수 없습니다. 픽셀은 배치되지만, 공간이 *경영*되는 일은 없습니다.

**咫尺山林**(ZhiChi ShanLin)은 천 년에 걸친 화하의 산수 공간의 예술을 AI에게 가르칩니다 — 어떻게 한 치 안에 산맥 전체를 담는지, 어떻게 여백이 깊이를 머금게 하는지, 그리고 사람이 진정으로 걸어 들어가 머물고 싶어 하는 장소를 어떻게 짓는지를.

## 문제

```
당신: "이 장면 / 페이지 / 공간을 디자인해 줘."
咫尺山林이 없는 AI: 완벽한 그리드. 모든 것이 보인다. 모든 것이 평평하다.
                    쓸 만하고, 보기에도 나쁘지 않지만… 깊이가 없고, 길이 없고, 머물 이유가 없다.
咫尺山林이 있는 AI: 가까운 바위, 굽이도는 오솔길, 안개 속으로 녹아드는 먼 봉우리.
                    산을 높아 보이게 하는 여백.
                    걸어서 누비고(可遊), 그 안에 머물 수 있는(可居) 장소.
```

## AI에게 무엇을 가르치는가

### 🏔️ 삼원법(Three Distances: 三遠法, 11세기)

곽희의 『임천고치』에서 — 어떻게 하나의 화면이 진정한 깊이를 품는가:

| 거리 | 한자 | 시점 | 느낌 | UI / 장면에서의 쓰임 |
|------|------|------|------|------------------|
| High Distance(고원) | 高遠 | 산기슭에서 우러러본다 | 우뚝 솟고, 가파르다 | 히어로의 충격, 수직의 위엄 |
| Deep Distance(심원) | 深遠 | 산 앞에서 그 뒤를 들여다본다 | 겹겹이 쌓이고, 감춰진다 | 점진적 공개, 갈 곳이 있다 |
| Level Distance(평원) | 平遠 | 가까운 봉우리에서 먼 봉우리를 바라본다 | 광활하고, 떠돌며, 고요하다 | 먼 지평, 고요한 마무리 |

### 🚶 공간의 네 등급(可行可望可游可居)

> 山水有可行者，有可望者，有可游者，有可居者……但可行可望不如可游可居之為得。
> 산수에는 다닐 만한 것이 있고, 바라볼 만한 것이 있고, 노닐 만한 것이 있고, 머물 만한 것이 있다…… 그러나 다니고 바라보는 것은 노닐고 머무는 것의 얻음만 못하다.

| 등급 | 한자 | 뜻 | 세우는 기준 |
|------|------|-----|-----------|
| Walkable(가행) | 可行 | 길이 있다 | 흐름이 통하고, 막다른 곳이 없다 |
| Viewable(가망) | 可望 | 볼 것이 있다 | 초점이 있고, 멈출 가치가 있다 |
| **Wanderable(가유)** | 可遊 | 거닐 가치가 있다 | 탐색이 보상을 준다 |
| **Dwellable(가거)** | 可居 | 머물 가치가 있다 | 다시 찾고 싶어진다 |

> "쓸 만하고 예쁘다"는 그저 합격점일 뿐입니다. 목표는 **가유·가거(可遊·可居)**입니다.

### 🌫️ 여백이 곧 산의 높이(虛實相生: 빔과 참이 서로를 낳는다)

> 山欲高，盡出之則不高，煙霞鎖其腰則高矣。
> 산을 높이고자 하면, 그 전부를 드러내서는 도리어 높아지지 않으니 — 안개로 그 허리를 두르게 하라, 그러면 솟아오른다.
> — Guo Xi, *Linquan Gaozhi · Shanshui Xun*(곽희 『임천고치』 「산수훈」)

유백(留白, 여백)은 "아직 채우지 못한 부분"이 아닙니다. 그것은 안개이고, 구름이며, 산을 높이 세우는 숨결 그 자체입니다. 모든 것을 채우면 깊이는 죽습니다.

### 👁️ 경영하기 전에, 먼저 보라(身即山川 · 外師造化)

> 身即山川而取之 — 몸으로 산천이 되어, 거기서 취하라.

어떤 공간을 경영하기에 앞서, 그것을 *참으로 보라* — 그 맥락과 그 사물을, 보는 데 흡족할 때까지(饱游饫看). 공간은 관조에서 자라나는 것이지, 템플릿에서 찍어내는 것이 아닙니다. 이것은 **NoPUA**와 같은 뿌리입니다 — 불안에 쫓겨 쌓아 올리지 말고, 이해로 이끌라.

## 설치

### A. 원클릭(Claude Code 플러그인)

```bash
# 이 스킬의 마켓플레이스를 추가한 뒤, 플러그인을 설치
/plugin marketplace add wuji-labs/zhichi-shanlin
/plugin install zhichi-shanlin
```

### B. 베어 클론(임의의 agent / 플랫폼)

```bash
git clone https://github.com/wuji-labs/zhichi-shanlin
cp -r zhichi-shanlin ~/.claude/skills/        # Claude Code
# Codex / Cursor: 아래의 플랫폼별 진입점을 참조
```

### 플랫폼별 진입점

| 플랫폼 | 진입점 | 원클릭 |
|--------|--------|--------|
| Claude Code | [platforms/claude-code.md](platforms/claude-code.md) | `/plugin install zhichi-shanlin` |
| Codex | [platforms/codex.md](platforms/codex.md) | 베어 클론 |
| Cursor | [platforms/cursor.md](platforms/cursor.md) | 베어 클론 |

### 호출 방식

- **자동** — 공간 / UI / 장면 / 경로 / 의경(意境)에 관한 작업을 하면서,
  *"이 페이지는 너무 밋밋해" / "너무 빽빽해" / "사용자가 돌아오지 않아" / "걸어 들어갈 수 있는 느낌으로"* 같은 말을 하면,
  스킬이 스스로 활성화됩니다([SKILL.md](SKILL.md)의 `description` 트리거 참조).
- **수동** — `/zhichi-shanlin [당신의 공간]`을 실행하면 고정된 상태 행 + 3부 구성의 처방 형식으로 명시적으로 감수합니다
  ([commands/zhichi-shanlin.md](commands/zhichi-shanlin.md) 참조).

### Before / After

| 과제 | 咫尺山林 없이 | 咫尺山林 있이 |
|------|--------------|--------------|
| "이 랜딩 페이지를 디자인해 줘" | 평평한 그리드, 모든 것이 한 평면 | 안개에 허리를 감춘 스크린샷 위에 고원의 히어로, 심원의 점진적 공개, 평원의 원경 |
| "아무도 돌아오지 않는 온보딩" | 단계는 더 매끄럽지만, 막다른 길은 그대로 | 가행·가망에서 멈춰 있음 → 가유(분기) + 가거(당신만의 자리)를 더한다 |
| "대시보드가 너무 빽빽해" | 카드를 축소 / 삭제한다 | 허실상생: 몇 개를 근경으로 끌어올리고, 나머지는 안개에 감추며, 숨 쉴 연하(烟霞)를 남긴다 |

입력→출력 실례: [examples/](examples/) ·
재현 가능한 평가 설계(실제 실행에 의한 수치는 미취득): [benchmark/README_BENCHMARK.md](benchmark/README_BENCHMARK.md).

중문판 README: [README.zh-CN.md](README.zh-CN.md)

## 동서의 만남

咫尺山林은 플랫 디자인의 규율을 대체하지 않습니다. 그 **안에 깊이를 엽니다.**

| 평면 기본값 | + 咫尺山林 | = 완성형 |
|------------|-----------|---------|
| 그리드: 모든 것이 한 평면 | 삼원: 근·심·원 | 진정한 깊이를 지닌 레이아웃 |
| 히어로 섹션: 한 번 외친다 | 고원: 우러러본다 | 우뚝 솟는 충격 |
| 피드: 끝없는 스크롤 | 가유·가거: 거닐고 머문다 | 머물 가치가 있는 장소 |
| 여백: 그저 padding | 유백: 봉우리를 들어 올리는 안개 | 말을 거는 빔 |

> **可行可望不如可游可居之為得。**
> 다니고 바라보는 것은 노닐고 머무는 것의 얻음만 못하다.
> — Guo Xi, *Linquan Gaozhi*(곽희 『임천고치』)

## 같은 흐름에서

- [**천공 TianGong**](https://github.com/wuji-labs/tiangong) — 화하 미학의 디자인 프레임워크. 자연스레 짝을 이룹니다: 천공은 *아름다운가*를 묻고, 咫尺山林은 *걸어 들어갈 수 있는가*를 묻습니다.
- [**NoPUA**](https://github.com/wuji-labs/nopua) — 두려움이 아니라 지혜로 AI를 이끈다.

## 기본 정보

| 항목 | 값 |
|------|----|
| 귀속 | WUJI Labs |
| 디렉터리 | `labs/skills/zhichi-shanlin/` |
| 라이선스 | MIT |
| 상류 | github.com/wuji-labs/zhichi-shanlin |
| 전거(典源) | 郭熙《林泉高致》Guo Xi, *Linquan Gaozhi* |
| 버전 | v1.0 · 2026-06-02 |

---

*咫尺山林 ZhiChi ShanLin — by [WUJI](https://github.com/wuji-labs)*
*咫尺之內，便覺萬里為遙。한 치 안에 만 리를 연다.*
