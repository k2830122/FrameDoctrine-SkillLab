# Confirmed Skill Names — MTG card-title adoption (v0.28)

**Decision date: 2026-10-29.** All 14 confirmed Skill Lab skills use
titles of actual *Magic: The Gathering* cards. The three Frame variants
share one card-title prefix, giving 12 distinct source card titles.

This document records the **currently approved display names**. They
are deliberately not rigid: a later skill may receive a better-fitting
name, in which case names can be reassigned together. Naming does not
imply that the MTG card's rules text is being adapted into the game.
The source-card effect notes below are concise Japanese paraphrases
for context only.

| Stable Skill ID | Previous name | Adopted display name (source MTG card) | Original MTG card effect (summary) |
| --- | --- | --- | --- |
| `frame-light` | Frame Combat Proficiency (Light) | **[Tempered Steel](https://scryfall.com/card/som/24/tempered-steel) (Light)** | 自軍のアーティファクト・クリーチャー全体に+2/+2。 |
| `frame-standard` | Frame Combat Proficiency (Standard) | **[Tempered Steel](https://scryfall.com/card/som/24/tempered-steel) (Standard)** | 同上。 |
| `frame-heavy` | Frame Combat Proficiency (Heavy) | **[Tempered Steel](https://scryfall.com/card/som/24/tempered-steel) (Heavy)** | 同上。 |
| `marksmanship` | Plant Your Feet | **[Last Word](https://scryfall.com/card/dst/23/last-word)** | 打ち消されない呪文で、対象の呪文を打ち消す。 |
| `mobile-evasion` | Keep Moving | **[Escape Velocity](https://scryfall.com/card/thb/132/escape-velocity)** | クリーチャーに+1/+0と速攻を付与。墓地からの再利用も可能。 |
| `momentum-melee` | On the Charge | **[Through the Breach](https://scryfall.com/card/chk/193/through-the-breach)** | 手札のクリーチャーを一時的に戦場へ出し、速攻を付与。終了時に生け贄。 |
| `guardian-reaction` | Got Your Six | **[No One Left Behind](https://scryfall.com/card/bro/109/no-one-left-behind)** | 墓地のクリーチャーを戦場に戻す。小型の対象ならコスト軽減。 |
| `brace-discipline` | Hunker Down | **[Built to Last](https://scryfall.com/card/kld/7/built-to-last)** | +2/+2。対象がアーティファクトなら破壊不能も付与。 |
| `conceal-discipline` | Go Dark | **[Moment of Silence](https://scryfall.com/card/mmq/28/moment-of-silence)** | 対象プレイヤーの次の戦闘フェイズを飛ばす。 |
| `fired-up` | Fired Up | **[Repercussion](https://scryfall.com/card/uds/95/repercussion)** | クリーチャーへのダメージを、そのコントローラーにも反映する。 |
| `observation-discipline` | Keep Watch | **[Standstill](https://scryfall.com/card/ody/102/standstill)** | 誰かが呪文を唱えると生け贄にし、そのプレイヤーの対戦相手が3枚ずつ引く。 |
| `scan-interpretation` | Sweep the Sector | **[See Beyond](https://scryfall.com/card/roe/86/see-beyond)** | 2枚引き、手札1枚を山札に戻して切り直す。 |
| `solo-operator` | On Your Own | **[Against All Odds](https://scryfall.com/card/one/1/against-all-odds)** | 自軍パーマネントを一時追放して戻す／墓地の軽量アーティファクトかクリーチャーを復活。 |
| `pick-your-ground` | Pick Your Ground | **[Dead of Winter](https://scryfall.com/card/mh1/85/dead-of-winter)** | 自軍の氷雪パーマネントの数だけ、氷雪でない全クリーチャーを一時的に弱体化。 |

## Scope of the rename

- **Changed:** Skill Lab card titles; in-page prose, sample text,
  formulas and option-study notes that name those current confirmed
  skills; the preview version label.
- **Unchanged:** all stable Skill IDs, levels, effects, activation
  conditions, skill group/category, status, source design decisions,
  saves/import/export format, and the separate main-game Core.
- **Historical README / design-note logs** retain their old wording
  because they document past decisions; the mapping above is current.
- The latest research-only [MTG candidate catalog and broader naming
  notes](https://github.com/k2830122/FrameDoctrine-SkillLab/tree/research/mtg-naming-20261029/research/mtg-names)
  are kept separate from approved skill definitions.

## Naming-review notes

- **Against All Odds** (now confirmed for `solo-operator`) is very
  similar to **Against the Odds** (separate, provisional
  `against-the-odds` CritPen-related skill with a previously settled
  name). We deliberately **did not rename that provisional skill** in
  this 14-skill-only change. This collision should be revisited when
  organizing the next batch of names.
- In spite of its snow setting, **Dead of Winter** is used for the
  terrain/position-defense skill solely as a creative title, not as an
  adaptation of its original mass-debuff effect.
- Card title and game mechanics are independently changeable. Name
  assignments should be evaluated as a **complete roster** rather than
  one-by-one translations of skills.
