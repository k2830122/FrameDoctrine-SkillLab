# FRAME DOCTRINE — PILOT SKILL LAB

**Current release: v0.40 (2026-10-30).** 32 active skills: **23 confirmed**, 9 provisional, with eleven archived retired skills. Names of confirmed skills use actual MTG card titles. Existing skill IDs and `fd-skill-lab-v1` save/import/export compatibility are maintained. This is still an acquisition/effects simulator, not a battle engine.

## v0.40 — Sight Beyond Sight, Iron Verdict, category cleanup (2026-10-30)

- New confirmed **Sight Beyond Sight** (`anti-air-recon`), [real MTG card](https://scryfall.com/card/dtk/75/sight-beyond-sight). When this pilot attempts to detect a **flying** enemy (ordinary sensors or ACTIVE SCAN), use TargetSignature **+1/+2/+3** at Lv1/2/3 for that detection calculation only. The enemy's actual Signature, pilot INSIGHT, Detection Power and other observers' calculations remain unchanged; legal Local Tracks are shared over normal Datalink. The existing flying-Unit negative-Signature convention represents 3D sensor geometry projected onto 2D Hexes, not necessarily physical stealth.
- New confirmed **Iron Verdict** (`heavy-rail-proficiency`), [real MTG card](https://scryfall.com/card/khm/17/iron-verdict): **effective SHOOTING +2/+4/+6** exclusively while using Heavy Rail on eligible shooting Attacks. Heavy Rail's 4-slot requirement, ammunition, movement modifier, CritPen and other weapon stats are unaltered. Valid conditional bonuses from **Seize Opportunity** and **Tempered Steel (Heavy)** can stack. **Historical naming caveat:** Iron Verdict was formerly the name of `marksmanship` before that skill was renamed Seize Opportunity in v0.37. The new Heavy Rail skill has its own ID; old `marksmanship` builds remain unchanged.
- Category cleanup: split `機体・武器固定` into **`機体固定`** (3 Frame class skills) and **`武器固定`** (Last Word, No Quarter, Iron Verdict); put **Shadow of Doubt** and **Fault Line** in **`敵弱体化`** instead of `攻撃・弾薬`; add **`索敵・情報`** for Sight Beyond Sight. These are organizational changes only.
- **32 active skills (23 confirmed, 9 provisional); 11 archived**. Stable saved skill IDs, `fd-skill-lab-v1`, `retiredSkillLevels`, retired-point refunds and old JSON import/export remain compatible. Both new skills are research-confirmed only: **the production Core and physical weapon definitions were not modified**.

## v0.39 — Retire Stillness in Motion; rebalance Confront the Unknown (2026-10-29)

- Archived **Stillness in Motion** (`observation-discipline`, formerly confirmed), preserving its original +4/+8/+12 effective INSIGHT levels and prior design description in `ARCHIVED_SKILLS` and the research history. Its lack of natural value in this game's advance-and-stop reconnaissance loop led to retirement: after no normal MOVE and completion of the Activation, a late extended scan generally cannot replace forward reconnaissance or immediate ACTIVE SCAN.
- Prior saved `skillLevels["observation-discipline"]` transfers into `retiredSkillLevels["observation-discipline"]` by the existing migration path, with **full point refund**. Existing stable ID is retained in the archive, not reused.
- **Confront the Unknown** (`scan-interpretation`) keeps ACTIVE SCAN-only effective INSIGHT +4/+8/+12 and standard scan +12 Detection Power. Its ACTIVE SCAN scanner Signature **total** is now **+3/+4/+5** at Lv1/2/3, up from standard scan +2, persisting to the next own Activation start under the existing scan rules. No extra command or additional Signature stacking category is introduced.
- The skill gives +1/+2/+3 Detection Budget over standard ACTIVE SCAN while increasing the owner's Signature by the same integer amount, but neither value guarantees a fixed number of Hexes of detection through varied terrain and blockers. The Main Action and exposure/INTERCEPT risk are retained.
- **30 active (21 confirmed, 9 provisional); 11 archived**. `fd-skill-lab-v1`, existing allocations and old JSON import/export remain compatible. The production Core and Option definitions were **not** changed.

## v0.38 — Final Fortune confirmed (2026-10-29)

- New confirmed **Final Fortune** (`final-fortune`), named after the [real MTG card](https://scryfall.com/card/mir/173/final-fortune). Each friendly Faction Phase start (including the first after mission start), independently roll 50% good / 50% bad for each owner.
- Good: effective SHOOTING and MELEE +4/+5/+6 (Lv1/2/3). Bad: effective REFLEX −6/−5/−4. State persists until the next friendly Faction Phase start, including enemy phases. Independent rolls allow repeated outcomes.
- Each rank 1P; 12P budget provisional. No new command, MP, cooldown, use counter or bad-luck protection. Skill Lab displays both states but does not run RNG or battle simulation. Core unchanged.
- Active 31 (22 confirmed, 9 provisional), archived 10. Existing IDs, `fd-skill-lab-v1`, import/export and retired-level compatibility retained.

## v0.37 — Confirm two weapon proficiencies and rename two skills (2026-10-29)

- **Seize Opportunity** replaces the display name **Iron Verdict** on existing ID `marksmanship`: normal Unit-target Direct FIRE **before own normal MOVE**, effective SHOOTING +2/+4/+6. Unrestricted firearm choice. Existing effects and stable ID unchanged.
- **Collision Course** replaces the display name **Through the Breach** on existing ID `momentum-melee`: successful normal MOVE entry of at least 3 Hex in the same Activation before eligible melee, effective MELEE +2/+4/+6. Any eligible melee weapon. Existing effects and stable ID unchanged.
- New confirmed **No Quarter** (`assault-lance-proficiency`): effective MELEE +2/+4/+6 only during Assault Lance melee Attack checks, with no additional MOVE requirement. Assault Lance remains CritPen NO, capacity 2.
- New confirmed **Last Word** (`sniper-rifle-proficiency`): effective SHOOTING +2/+4/+6 only during Sniper Rifle shooting Attack checks, with no additional MOVE requirement. Sniper Rifle remains CritPen YES and retains range 2–10 Hex, 4 shots, capacity 2 and the normal post-MOVE −20 accuracy modifier.
- Conditions are independent: No Quarter and Collision Course can stack, as can Last Word and Seize Opportunity, when both conditions apply. No new active command, cooldown or resource bar. Each rank costs 1P; the Lab's current 12P budget remains provisional.
- Active **30 (21 confirmed, 9 provisional)**; archived **10**. The old generic favorite-weapon skill `charlene-favorite-weapon` stays archived, with its historical levels preserved. New skills use independent IDs. Existing IDs, `fd-skill-lab-v1` storage key, previously saved builds, rank refund history and JSON import/export compatibility are preserved.
- Changes apply to **Skill Lab only**; the production game Core has not been updated.

## v0.36 — Retire generic favorite-weapon skill (2026-10-29)

- Archived provisional **Charlene / 愛用武器（仮）** (`charlene-favorite-weapon`) without changing its stable ID or historical level descriptions.
- **Reason:** Selecting any one weapon would let players take the buff with a general-purpose, low-capacity weapon such as the Assault Rifle; the intended equipment commitment would be weak. Instead, separately design dedicated proficiency skills for high-commitment **Assault Lance** and **Sniper Rifle** (both Armament Capacity 2). Names, final specifications, and registration of the new individual skills will follow the naming/design discussion; they are **not added in v0.36**.
- Active total **28** (19 confirmed / 9 provisional), archived total **10**. Old ranks migrate to `retiredSkillLevels` and their point costs are refunded; save key `fd-skill-lab-v1` and import/export schema remain unchanged.
- Core game remains unchanged.

## v0.35 — Retire Against the Odds (2026-10-29)

- Archived the **provisional** `against-the-odds` (**Against the Odds**, low-accuracy / CritPen chance boost), retaining its full old research specification under the same stable ID.
- **Reason:** Making low accuracy directly increase armor-critical effects may reward deliberately poor shooting conditions. Synergies with Shadow of Doubt and Fault Line further undermine the intended cost of low Hit chance. The name also closely resembled the confirmed **Against All Odds**.
- The confirmed **Against All Odds** (`lethal-endurance`) and all other 18 confirmed skills are unchanged.
- **29 active skills** (19 confirmed, 10 provisional) and **9 archived**. Existing skill IDs, `fd-skill-lab-v1`, and old-build import/export remain compatible. Saved ranks in the retired skill are preserved in `retiredSkillLevels` without consuming active points.
- No change to production Core.

## v0.34 — Brink of Disaster / Against All Odds confirmed; five more skills archived (2026-10-29)

**Two existing provisional skills are now design-confirmed**, with unchanged stable IDs:

- **Brink of Disaster** (`last-stand-ability`): at HP ≤50% of MaxHP (while alive), effective REFLEX increases by `1 + floor(deployment-base INSIGHT × Lv / 6)`, identical to Audacity's growth formula but improving REFLEX rather than SHOOTING. Lv1–3 with base INSIGHT10: +2/+4/+6; INSIGHT18: +4/+7/+10. Recompute after damage and repair; a newly crossed threshold takes effect for subsequent Hits within the same Attack, never retroactively. The base INSIGHT is fixed at deployment (including permanent training), not temporary buffs. No activation command, extra resources, or use limit.
- **Against All Odds** (`lethal-endurance`): guaranteed survival at **HP1** when an eligible incoming Attack would otherwise be fatal, checking the actor's HP **at Attack start**. Lv1: HP≥50% MaxHP and HP≥2; Lv2: HP≥25% MaxHP and HP≥2; Lv3: HP≥2 regardless of fraction. The entire one Attack is survivable, including all Hits of a multi-Hit Attack. The next distinct Attack checks its own starting HP and may kill the HP1 survivor. **No once-per-Mission limit**; repair can bring the unit back above threshold. This is not resurrection of an HP0/Destroyed unit.
- Archived five provisional entries: **First Watch** (`early-starter`), **Steady Nerves** (`burst-focus`), **Stay Frosty** (`certain-evasion`), **Right on Cue** (`reaction-shooter`), and **据置精密貫徹** (`stationary-penetration`). This removes passive, low-tradeoff WAIT buffs and redundant static-accuracy/penetration stacking from the active list.
- Active count **30 (19 confirmed, 11 provisional)**; archived count **8**. Existing archived rank handling saves retired IDs in `retiredSkillLevels` and refunds their spent points, preserving `fd-skill-lab-v1` storage and the v1 import/export schema.
- The provisional `against-the-odds` (CritPen skill) remains a separate existing ID and title, **not design-confirmed**. Its name is now close to the approved **Against All Odds**; rename it separately if that provisional skill is retained.
- The Skill Lab remains a **point-allocation and effect-description tool**, not an in-battle HP/damage simulation; **production Core has not been changed**. Updated approved MTG references, card art links and effects are in [MTG_SKILL_NAMES.md](MTG_SKILL_NAMES.md).

## v0.33 — Retire moving-fire penalty mitigation (2026-10-29)

- Archived provisional `moving-fire-discipline` (移動射撃術) without adopting it. Old rank/skill ID preserved in `ARCHIVED_SKILLS`, active list now 35 skills (17 confirmed, 18 provisional), archived list now 3 skills.
- Rationale: reducing or eliminating a weapon's negative post-MOVE accuracy modifier undermines the intended tradeoff between movement flexibility and static precision. The idea lacks sufficient new tactical choices to justify neutralizing a deliberately designed disadvantage.
- **WAIT assessment:** in this game, movement and end-of-movement detection are automatic and WAIT is the natural default when no enemy is located; it also enables eligible INTERCEPT/COVER/anti-missile reactions. Thus WAIT provides practical utility without a major opportunity cost in that situation. Right on Cue, Steady Nerves, Stay Frosty remain provisional, because extra unconditional WAIT rewards could make WAIT excessively dominant.
- Legacy saved ranks migrate to `retiredSkillLevels` and points are refunded for reallocation. Keep `fd-skill-lab-v1`, import/export structure, and main battle Core unchanged.

## v0.32 — Archive Lucky Seven (2026-10-29)

- Moved `range-lucky-star` (the former provisional ラッキースター / Lucky Seven) from active skills into `ARCHIVED_SKILLS`. Now 36 active skills: 17 confirmed, 19 provisional; 2 archived (including Quick Study).
- Rationale: indicating legal 7-Hex trigger positions is important to make the condition understandable, but then optimal play risks becoming just choosing a highlighted destination and firing. This was not found to create enough interesting positional decisions. CritPen +7/+14/+21 was only a provisional proposal.
- Existing `range-lucky-star` allocations migrate via `retiredSkillLevels`, preserving their history while refunding the points. The `fd-skill-lab-v1` key, active IDs, import/export format, and main game Core are unchanged.
- WAIT/Reaction candidates remain under review; simply rewarding WAIT can make it the default action without a new tradeoff. No WAIT skill was finalized or archived.

## v0.31 — Finalized suppression skill, renames and categories (2026-10-29)

- Reused existing `suppressive-fire` ID: renamed **Shadow of Doubt**, confirmed with Lv1/2/3 enemy REFLEX −2/−4/−6 only when **every Hit** of a normal enemy Unit Direct FIRE Attack misses. Applies after Attack resolution until the **attacker Faction Phase ends**, strongest effect only, not cumulative. Ineligible: any Hit lands, Reaction/INTERCEPT, missiles, Area/Hex attacks. Existing FIRE resource costs apply; no special action.
- Five other confirmed names updated: **Shielded Passage**, **Decisive Denial**, **Stillness in Motion**, **Audacity**, **Confront the Unknown**. **Repercussion stays unchanged**. No other skill effects changed.
- Grouped COVER/BRACE/CONCEAL/ACTIVE SCAN under **コマンド強化**; merged geographic/terrain skills under **位置・地形**; moved Repair Kit enhancement under **装備・消耗品**. WAIT-specific provisional skills remain in WAIT・Reaction.
- The updated approved roster, descriptions of each skill, and linked source MTG card images are in [MTG_SKILL_NAMES.md](MTG_SKILL_NAMES.md).
- Main game Core was not modified. The new effects are design-confirmed in Skill Lab only.


**Current release: v0.30 (2026-10-29).** 37 active Skills: **16 confirmed**, 21 provisional; 1 retired Skill archived separately. Confirmed Skill names are English-only even in the Japanese interface. The Pilot Ability formerly labeled AWARENESS is now **INSIGHT**; private Core's Pilot Detection and Frame Sensor have not been renamed. Historical notes below may still use former names.


## v0.30 — Fault Line and Survival Cache confirmed (2026-10-29)

**Two new confirmed pilot skills** were added to the point-allocation simulator:
37 active skills total, **16 design-confirmed**, 21 provisional.
One stable Skill ID per new entry; previous 35 IDs are untouched.

- **[Fault Line](https://scryfall.com/card/usg/185/fault-line)** (`fault-line`,
  attack/ammunition): on eligible enemy Unit **Critical Penetration success**
  during FIRE or MELEE, reduce the target's Armor by **−2/−4/−6**
  (Lv1/2/3). The successful CritPen Hit itself resolves as ordinary
  Armor-bypassing damage; **the reduction occurs immediately after that Hit's
  damage**, so remaining Hits in the same multi-Hit Attack already benefit.
  The best reduction applies, not cumulative stacks. Clamp Armor at zero;
  lasts until target destruction or Mission end. CritPen eligibility and
  once-per-Attack roll semantics are unchanged, including independent
  per-target Attacks for the Combat Knife's AreaMelee. No extra proc roll.
  Normal total Armor penetration *without CritPen* does not trigger it.
- **[Survival Cache](https://scryfall.com/card/roe/44/survival-cache)**
  (`survival-cache`, repair/support): while using an **equipped Repair Kit**,
  increase recovery from 8 HP to **12/16/20 HP** at Lv1/2/3
  (bonuses +4/+8/+12). The original **two Kit charges per Mission**,
  Main Action cost, self/adjacent friendly living Frame eligibility,
  Max HP cap, and inability to revive a destroyed Frame stay unchanged.

The adopted names are real *Magic: The Gathering* card titles;
source-card effects are described in
[MTG_SKILL_NAMES.md](MTG_SKILL_NAMES.md).
These titles are naming references; source MTG mechanics are **not** copied.

**Implementation boundary:** Skill Lab models acquisition, rank comparisons,
and textual formula examples only. It does **not** run battlefield CritPen,
Armor mutation, or REPAIR actions. No change to private production Core.
The `fd-skill-lab-v1` save key, previous skill IDs, existing allocations,
export and import remain compatible; new IDs default to level 0.

## v0.29 — Rename stationary-fire skill to Iron Verdict (2026-10-29)

The confirmed stationary-fire skill (stable ID `marksmanship`) has been
renamed **Iron Verdict** (a real MTG card from *Kaldheim*); previously,
the same Skill was named **Last Word**. **Last Word** is now unassigned,
and may later be used for a WAIT/Reaction Skill if that design is approved.
No other Skills were renamed. See [MTG_SKILL_NAMES.md](MTG_SKILL_NAMES.md).

All skill effects, activation conditions, levels, IDs, save compatibility,
confirmation status and production Core behavior are unchanged.

## v0.28 — Confirmed Skill names replaced with MTG card titles (2026-10-29)

**All 14 design-confirmed pilot skills now use actual Magic: The Gathering
card titles** (12 distinct card names because Light/Standard/Heavy share
the title `Tempered Steel`). Display names were selected for atmosphere
and cohesion, **not because source-card effects map to the pilot skills**.

See [MTG_SKILL_NAMES.md](MTG_SKILL_NAMES.md) for the authoritative
**old name → current name → stable Skill ID** table, source-card links
and short explanations of the source MTG card effects. Selected examples (as of v0.28):
`Tempered Steel`, `Last Word`, `Escape Velocity`, `No One Left Behind`,
`Moment of Silence`, `Repercussion`, and `Dead of Winter`.

**Names only:** skill mechanics, levels, activation conditions, status,
skill IDs, the `fd-skill-lab-v1` save key, existing saved builds,
and import/export compatibility remain unchanged. No canonical Core
implementation was changed. Prior version notes below are historical
records and deliberately keep the names used at the time.

A naming near-collision remains between the confirmed skill
`Against All Odds` and the separate research skill `Against the Odds`;
the latter was not renamed as part of the confirmed-14 naming pass.

## Historical decision log: Frame Proficiency Skills (2026-10-23)

**確定（仕様確定）:** 機体習熟 Light / Standard / Heavy

| Level | Effective SHOOTING | Effective MELEE |
|---|---:|---:|
| Lv1 | +1 | +1 |
| Lv2 | +2 | +2 |
| Lv3 | +3 | +3 |

Passive automatic Skill: applies while operating the matching Frame class. The changes are effective Ability modifiers used by all eligible SHOOTING/MELEE calculations, including applicable Missile Intercept or Critical Penetration checks. REFLEX and AWARENESS are unaffected. No Action, Reaction, MP, cooldown or use count. One Training Point per rank.

This decision replaces the earlier provisional +2/+3/+5% accuracy/evasion proposal. **Confirmed for Skill Lab game design, not yet implemented into private Core or canonical specifications.** All other skills were not approved at the time of that decision; see the later Opening Advantage confirmation below.


A standalone browser-based simulator for experimental pilot skill builds in FRAME DOCTRINE: LAST RESORT.

**Status:** Research prototype v0.30. The game project itself is separate and is not included in this public repository. None of the proposed skills or balance numbers are official game specifications.

## Features

- 37 active experimental pilot skills (sixteen confirmed, 21 provisional) and one retired Skill in the archive
- Ability development and Lv.1–3 skill purchases with a shared 1–12 point budget
- Undo, reset, filter and search
- Local browser auto-save and import/export of build JSON
- In-app classifications of 20 existing Options, for design study only

## Run

Open `index.html` directly in a modern browser or access the GitHub Pages site once Pages has been enabled.

## Publish with GitHub Pages

Repository **Settings → Pages → Build and deployment → Deploy from a branch → main → /(root) → Save**.

All files in this repository (and its published Pages site) are intentionally public. Do not commit private project source, documents, character art, secrets or other non-public assets here.

## Source separation

This repository was initialized independently of the private game's Git history. Only the standalone application and this public README were copied. This skill lab does not modify the game's core, option implementations or canonical specifications.

## Disclaimer

Experimental results and numbers are design hypotheses; the simulator models **point allocation**, not full combat outcomes.

## New concept candidates (2026-10-23)

The following candidates are only rough exploratory ideas, not accepted implementation requirements. The initial Lv.1–3 values and caps in the app are illustrative placeholders.

- **Kill Momentum Growth / 撃破成長:** Each enemy defeated grants a bonus to a player-chosen Ability. Important unresolved questions: choice timing, per-mission versus persistent growth, stacking cap, and kill credit.
- **Reflex Follow-Up Move / 反射機動:** After acting, gain a chance to move again proportional to *effective REFLEX*. Illustrative Lv.1 formula: 1% × REFLEX (REFLEX 10 → 10%); higher-level scaling is provisional. The legality and interaction with existing mobility features are unresolved.
- **Lethal Endurance / 不屈:** Survive an otherwise lethal hit at HP 1. The current per-level initial-HP thresholds and once-per-mission limit are illustrative only.
- **Low-HP Ability Surge / 背水の陣:** Gain an effective Ability bonus when current HP falls below a chosen threshold. Ability selection, threshold and level bonus are not approved.

### Cross-cutting idea: Ability-value-based Skills

Besides ordinary Ability-boosting Skills, investigate Skills whose *magnitude or activation probability is calculated from the Pilot's current effective Ability*, such as `REFLEX × 1%` for a conditional follow-up move. This gives ordinary Ability increases additional strategic value.

When a Skill says it grants an effective Ability bonus (SHOOTING, MELEE, AWARENESS or REFLEX), the intended *research direction* is to use the resulting effective Ability in all relevant calculations, rather than granting narrow +Hit% / +Evasion% substitutions. This still requires explicit combat-design review before any change to the private Core.

This app currently simulates **training-point allocation only**, not on-map kill events, HP reductions, Action outcomes, or chance rolls.

## Ability cap removal and limited guaranteed outcomes (2026-10-23)

**New accepted research direction (not yet canonical Core):**
- Remove the numeric ceiling on both *base* and *effective* Pilot Abilities (SHOOTING, MELEE, AWARENESS, REFLEX). A player may continue investing Training Points into a base Ability past 20, subject to their finite Training Point budget.
- Conditional Skill boosts stack into the effective Ability and use that full value consistently in all relevant Ability-dependent calculations.
- Extreme accuracy and evasion are allowed to become correspondingly strong. Probability quantities, however, are still bounded by 0–100%; removing an Ability ceiling is **not** removing probability bounds.
- Balance through finite growth points, real activation conditions, opportunity costs and build tradeoffs, not a universal ability ceiling. Do not silently migrate this rule into the private game Core or master specs.

**New speculative Skills (not approved effects):**
- **必中の一撃 / Decisive Shot:** a limited number of eligible attacks per Mission become guaranteed hits; draft ranks allow 1/2/3 uses. Prefer an understandable passive/conditional trigger over another active command. What counts as an eligible attack, how a use is spent and whether a 100% base hit consumes it remain unresolved.
- **完全回避 / Certain Evasion:** evade exactly one qualifying incoming attack after a preparation cost. Working non-active version is to use existing WAIT as its trigger, with 1/2/3 prepared guaranteed evades per Mission by rank. This is a proposal, not approval of specific timing or effect.
- In interactions between guaranteed hit and guaranteed dodge, the governing priority is **undecided**. Direct Fire vs Missile vs Area/multi-hit and interactions with critical penetration need explicit rules. Do not infer priorities from the labels alone.

The skill-list page models **purchase allocation**, not true combat resolution or activation charges. These new entries are deliberately labeled exploratory.

## 2026-10-23 — effective Ability rework of the original 19 skills

The Skill Lab now shows the research redesign on all 19 original candidates, retaining all 6 later rough ideas (28 total) and stable IDs for saved builds. **No Core changes are authorized.** Existing Option mechanics remain untouched.

**Research principle:** When a Skill grants conditional Ability +N or −N, use that *effective* Ability consistently in **all otherwise eligible formulas** that use SHOOTING, MELEE, AWARENESS, or REFLEX, instead of one-off Hit/Evasion percentage exceptions. Conditional skills do not mutate the underlying base value. Base and effective Ability caps are removed *in the research design*; probability outputs still use ordinary 0–100% rules.

New compare-only Lv1/2/3 values:

- Frame Proficiency L/S/H: SHOOTING and MELEE +1/+2/+3 (not REFLEX).
- Opening Vigilance (formerly Opening Advantage; confirmed): AWARENESS and REFLEX +1/+2/+3. Solo Operator (provisional): SHOOTING and REFLEX +1/+2/+3.
- Precision Shooting, Mobile Evasion, Momentum Melee: relevant SHOOTING/REFLEX/MELEE +2/+4/+6 respectively, with existing stationary or 3-Hex movement trigger.
- Ordinary INTERCEPT specialist: SHOOTING +2/+4/+6 only during qualifying ordinary INTERCEPT.
- Burst Focus: selected Ability +2/+4/+6 (activation economics unresolved).
- Night/Adverse Weather, Stationary Observation, Active Scan Interpretation: AWARENESS +4/+8/+12 under their respective conditions (strong provisional values; Active Scan Skill remains unapproved).
- Suppressive Fire: target effective REFLEX −1/−2/−3 for rest of firing Faction Phase; full applicable REFLEX semantics, not a special +Hit% buff.
- Guardian Reaction: REFLEX +1/+2/+3 when protecting an ally (Skill migration on hold).
- Stationary penetration, Lance charge penetration, BRACE Armor, CONCEAL Signature: remain special-effect skills; not all effects should be expressed as Ability gains.

The app is only a **point-allocation simulator**. Conditional skills are not automatically added to the base-Ability numbers in the pilot panel, because no battlefield conditions have been simulated; see each skill's trigger and effect instead. Unconfirmed numerical proposals are marked provisional; the approved Frame Proficiency and Opening Vigilance Skills have fixed Skill Lab specifications.
\n## Passive-first Skill design (2026-10-23)\n\n[SKILL_DESIGN_NOTES.md](SKILL_DESIGN_NOTES.md) has the current cost catalogue and new Skill concepts: REFLEX-based second-chance dodge, SHOOTING-based movement-disabling hit, and additional-ammo multi-attempt FIRE. The design direction favors passive Skills and existing tactical resources, with active Skills as exceptions only. All three are exploratory.\n
## 2026-10-23 — Range and movement-triggered skill drafts

Two further exploratory candidates were added (30 total): a condition-based “Lucky Star” slot (example: firing from 7 Hexes, effect TBD) and a REFLEX-dependent movement firing penalty mitigation skill. Refer to [SKILL_DESIGN_NOTES.md](SKILL_DESIGN_NOTES.md) for candidate formulas and Core distinctions. Their conditions and numbers are not approved final mechanics.

## v0.9 — Pilot AWARENESS and saved-build migration (2026-10-23)

- Pilot Ability label: **AWARENESS（状況把握）**, formerly displayed as SENSOR in Skill Lab. This remains the current private game's internal **`PilotStats.Detection`**. Physical **`Frame.Sensor`** is a distinct Frame statistic; private Core and canonical game specs remain unchanged.
- Legacy browser saves and imported JSON with `abilityBonus.SENSOR` automatically map to `abilityBonus.AWARENESS`, preserving allocated Training Points. New exports use AWARENESS.
- The 「確定スキルを見る」 button toggles on/off; the second click restores previously selected search/category/origin/status filters (Issue #1).
- **Historical exploration (superseded by the confirmed v0.10 design below):** Early Starter duration was proposed as `max(1, floor(base AWARENESS at deployment / 2))` global Turns. The formula and Lv bonuses have since been approved for Opening Advantage. The general integer-rounding policy is still under discussion and is not an approved global Core change.

## v0.10 — Historical: Opening Advantage / 初動掌握 (superseded by v0.11)

**Status: 確定 (Skill Lab design, not implemented in private Core).** Existing Skill ID `early-starter` is retained for saved build compatibility. Rename from アーリースターター / Early Starter to **初動掌握 / Opening Advantage**.

| Rank | Effective SHOOTING | Effective REFLEX | Training cost |
|---|---:|---:|---:|
| Lv1 | +1 | +1 | 1P total |
| Lv2 | +2 | +2 | 2P total |
| Lv3 | +3 | +3 | 3P total |

Trigger: passive and automatic from global Turn 1. Duration: global Turns `1..max(1, floor(base AWARENESS measured at sortie deployment / 2))`, inclusive. It applies in **every Faction Phase** of each eligible global Turn; expires from the start of the next global Turn. The base AWARENESS snapshot is not recomputed on conditional temporary changes during the battle. Examples: AWARENESS 10 → Turns 1–5; 16 → Turns 1–8; 20 → Turns 1–10.

The modifiers affect all eligible uses of effective SHOOTING/REFLEX while active, including direct-attack accuracy, defensive evasion, qualifying missile-intercept formula, and relevant CritPen. No Frame-class restriction or extra Action/Reaction/ammunition/resource consumption. Baseline Ability is unchanged. The confirmed-vs-draft count becomes **4 confirmed / 26 under consideration** in the Skill Lab; use the confirmed filter to inspect them.

Design rationale: a time-limited, Frame-agnostic alternative to permanent single-Ability training and Frame Proficiency. Particularly useful for high-AWARENESS reconnaissance pilots who need early evasion; mission lengths and contact-turn distributions should still be tested. This decision **does not change `docs/IDEAS.md`, `docs/CORE_SPEC.md`, or any implementation in the private game**.

## v0.11 — Confirmed Opening Vigilance / 初動警戒 (2026-10-23)

**Current approved design** (supersedes the previous Opening Advantage confirmation): The public Skill Lab card `early-starter` is renamed **初動警戒 / Opening Vigilance**. Its underlying Skill ID is kept unchanged, preserving existing saved builds. The earlier SHOOTING/REFLEX bonus and subsequently discussed MELEE addition are not adopted.

| Rank | Effective AWARENESS | Effective REFLEX | Cumulative Training Points |
|---|---:|---:|---:|
| Lv1 | +1 | +1 | 1 |
| Lv2 | +2 | +2 | 2 |
| Lv3 | +3 | +3 | 3 |

Automatically active in **every faction Phase** of global Turn 1 through `max(1, floor(base AWARENESS at deployment / 2))` (inclusive), then expires. The duration uses **base AWARENESS at sortie deployment**, including permanently trained base points but **excluding the Skill's own conditional AWARENESS increase** and any other temporary buff. Skill rank changes the benefit, not its duration. Base AWARENESS10 = 5 Turns, 16 = 8 Turns, 20 = 10 Turns. While active, the effective AWARENESS bonus contributes to eligible detection checks and REFLEX to eligible enemy attacks/evasion/reaction formulas. Base Ability never changes. No Frame-class limit or extra active command.

The three formerly named **Frame Proficiency** Skills (Light/Standard/Heavy) retained their effects and have been renamed **Frame Combat Proficiency** in v0.12: effective SHOOTING and MELEE each +1/+2/+3 within the specified Frame class. No extra six-pair card variants have been adopted. **4 confirmed and 26 exploratory Skills** remain.

Scope: Skill Lab research design, not private game's Core or canonical gameplay documents. This simulator allocates points; it does not currently simulate live battlefield buffs or Turn counts.

## v0.12 — Released Skill Lab skill-spec consolidation (2026-10-23)

**Current state: 32 cards; 6 confirmed; 26 exploratory.** Confirmed:
1. 機体戦闘習熟：Light / Frame Combat Proficiency: Light
2. 機体戦闘習熟：Standard / Frame Combat Proficiency: Standard
3. 機体戦闘習熟：Heavy / Frame Combat Proficiency: Heavy
4. 初動警戒 / Opening Vigilance
5. 臨戦集中 / Combat Focus
6. 戦況適応 / Tactical Adaptation

The three Frame Combat Proficiency cards retain the exact previous effects and Skill IDs `frame-light`, `frame-standard`, `frame-heavy`. A matching Frame class gives effective **SHOOTING +1/2/3 and MELEE +1/2/3** by rank. **AWARENESS/REFLEX, scouting, mobility and defensive ability are not strengthened.** Only the displayed Skill name changes.

**戦況適応 / Tactical Adaptation** is a new confirmed passive Skill, Lv1/2/3 effective SHOOTING and MELEE **+1/+2/+3**. Activates at global Turn `max(3, 20 - base AWARENESS at sortie)`, inclusive and continues to end of Mission; phase-wide and Frame-agnostic. Example base AWARENESS 10 → Turn10, 14 → Turn6, 15 → Turn5, 16 → Turn4, 17+ → Turn3. Re-evaluating activation time against temporary effective-AWARENESS boosts is not allowed. No additional command. It complements the early defense/scouting role of Opening Vigilance.

**臨戦集中 / Combat Focus**, previously `集中バースト` / Temporary Burst, is confirmed on existing Skill ID `burst-focus`. Upon legal WAIT, the Pilot acquires the normal one binary Reaction. If no Reaction is spent before the following own Faction Phase, that Reaction expires as normal and the Skill activates automatically: for the Pilot's next Activation, effective **SHOOTING and MELEE +2/+4/+6** by Skill Lv1/2/3. Ends on Activation completion, does not stack, and no additional UI action is needed. An INTERCEPT/COVER/etc Reaction spent during the intervening phases disqualifies the bonus.

The following are **not confirmed**, with explicit provisional numerical effects shown solely to compare builds:
- **臨戦警戒 / Combat Vigilance** (reuse existing Skill ID `certain-evasion`, replacing the old guaranteed-evasion draft): while a WAIT-granted Reaction remains available, raise evasion by **floor(base AWARENESS/3), floor(2×base AWARENESS/3), base AWARENESS percentage points** for Lv1/2/3. It does **not** guarantee a dodge nor consume a Reaction simply for being attacked. Weapon/attack-family eligibility, exact base/effective AWARENESS source, combination with Combat Focus when an unspent Reaction earns both benefits, and balancing against enemy mass attacks remain unresolved.
- **Charlene / 愛用武器** (new Skill ID `charlene-favorite-weapon`): when attacking **with the one chosen weapon definition**, strengthen the attack's applicable SHOOTING/MELEE by provisional **+2/+4/+6** for Lv1/2/3. It is not an all-rifles category buff, not an always-on combat ability buff, and not an effect when attacking using another weapon. Weapon selection rules and exact effect strength are unapproved.

**The lab still simulates only Training Point allocation, not live battle conditions, Reaction lifecycle, weapon registration or attack probabilities.** Charlene's selected weapon is stated conceptually only; there is no weapon selection control yet. Existing saved builds retain the IDs for the three renamed Frame skills, `early-starter`, `burst-focus` and `certain-evasion`, preventing loss of owned ranks. No private Core, Godot or master specification files are modified by this release. Older sections above record historical design proposals; for the current Skill Lab state use this v0.12 section.

Related tracked work: GitHub Issues #4–#8.

## v0.13 — Activation-condition categories and opportunity-cost research UI (2026-10-23)

The Skill Lab now groups **all 32 cards by their primary activation/eligibility condition** rather than mixing the strengthened combat stat and trigger. The former broad `汎用`, `射撃`, `白兵` etc. category labels have been replaced with the following **ten research categories, in explicit display order**:

| Primary category | Cards | Purpose |
|---|---:|---|
| 機体・武器固定 | 4 | Match Frame class or a particular weapon; Frame Combat Proficiency remains the first baseline reference |
| 時間経過 | 2 | Opening-only or delayed Turn activation |
| WAIT・Reaction | 4 | WAIT, ordinary INTERCEPT/COVER, Reaction held or spent |
| 移動・静止 | 7 | MOVE, no-MOVE, route-length constraints |
| 距離・布陣 | 2 | Isolation, particular Hex range |
| 天候・環境 | 1 | Weather-dependent activation |
| 姿勢・走査 | 3 | BRACE, CONCEAL or ACTIVE SCAN Main Action |
| 攻撃・弾薬 | 4 | Direct attacks, Hit conditions, ammunition and special attack effect |
| 被弾・HP | 3 | HP thresholds, fatal damage, attacks received |
| 行動後・撃破 | 2 | End-of-action chance or kill-triggered effect |

Every card also includes independent `costTags` and a plain-language `tradeoffDetail` to describe **the resource, tradeoff or restrictive requirement**: Frame/weapon commitment, limited effective Turns, WAIT/Reaction opportunity, stationary/movement choice, separation and geometry, attack Signature exposure, Main Action, added ammunition, dangerous HP, special chance/uses, etc. A new **制約・対価** dropdown filters by these tags; keyword search also includes the new metadata. **Activation requirements, resource expenditure, opportunity costs and mere conditional limits are not identical**; the UI label explicitly warns against counting inherent Core action costs twice.

The category tab bar, `すべて` grouped sections and category dropdown use the same ordering, and the default page opens the **すべて** view with Frame/weapon specialists first. The `確定スキルを見る` toggle also retains the selected tradeoff filter when restoring previous selections.

No Skill's identifier, cost, numeric effect, approved status, or trigger text changed. It remains **6 confirmed / 26 exploratory**; existing local-storage/JSON build data stays compatible. All categories and tag assignments are **research UI taxonomy**, not an implementation of in-battle effects and not a change to private Core.

Related issue: #10.

## v0.14 — Pilot-aware Level previews (2026-10-23)

**The main Lv1 / Lv2 / Lv3 descriptions prioritize concrete sample-Pilot values over formulas.** Formula details are available in each relevant card's expandable **計算式・設計上の補足** section. The prototype still simulates Training Point allocation, not full battle resolution.

The research sample Pilot **PHANTOM-01** has base Abilities of 10 before the user's permanent point allocations. For the following existing draft Skills, visible Lv results are calculated using the sample's current base Abilities and update immediately when they are changed:

- **臨戦警戒 / Combat Vigilance** (`certain-evasion`): direct evasion bonus in **percentage points** from base AWARENESS; display Lv1/2/3 values using `floor(AWARENESS × Lv / 3)` (the Lv3 expression is equivalent to the full AWARENESS value).
- **反射機動** (`reflex-followup-move`), **見切り回避** (`reflex-second-chance`): probability `clamp(REFLEX × Lv,0,100)%`.
- **脚部制圧射撃** (`leg-disrupting-shot`): probability `clamp(SHOOTING × Lv,0,100)%`.
- **移動射撃術** (`moving-fire-discipline`): result of reducing weapon movement modifiers **−10 and −20** by up to `floor(REFLEX × Lv / 3)`, capped at zero penalty; show both practical examples for the same sample Pilot. Weapons with zero penalty do not acquire a bonus.

For the confirmed **初動警戒 / Opening Vigilance**, the shown expiry Turn is now the sample's computed `max(1,floor(base AWARENESS/2))`; for **戦況適応 / Tactical Adaptation**, the start Turn is `max(3,20-base AWARENESS)`. Their approved level bonuses and triggering rules have not changed.

**Disclosure and scope:** The pilot number is the current displayed *base* Ability after point allocation, not the entire battle-effective Ability after other conditional Skills. Dynamic drafts remain **未確定**, and values are illustrations, not guaranteed outcomes in a specific battle. Original detailed research formulas remain present in expanded notes; existing Skill IDs, level effects, training costs and confirmed-status count (**6**) are unchanged. Skill count stays **32**. Browser-stored and JSON builds remain backward compatible. No changes to private Core or master gameplay specs.

## v0.15 — INSIGHT, English-first naming and retirement archive (2026-10-23)

**The current five confirmed Skill IDs and their displayed names** are:

| Stable Skill ID | English name | Confirmed effect |
|---|---|---|
| `frame-light` | **Frame Combat Proficiency (Light)** | Matching class: effective SHOOTING & MELEE +1/+2/+3 |
| `frame-standard` | **Frame Combat Proficiency (Standard)** | Matching class: effective SHOOTING & MELEE +1/+2/+3 |
| `frame-heavy` | **Frame Combat Proficiency (Heavy)** | Matching class: effective SHOOTING & MELEE +1/+2/+3 |
| `early-starter` | **First Watch** | During global Turn 1 through `max(1,floor(base INSIGHT / 2))`: effective INSIGHT & REFLEX +1/+2/+3 |
| `burst-focus` | **Steady Nerves** | After WAIT with its Reaction unspent through the start of next friendly phase: next Activation effective SHOOTING & MELEE +2/+4/+6 |

**INSIGHT** is the English name for the pilot's cognitive awareness/detection stat previously called **AWARENESS**. This is a **Skill Lab presentation/data key change**, not a changed combat formula or a change to private C# `PilotStats.Detection` / `Frame.Sensor`. First Watch uses **base INSIGHT at sortie** as a duration snapshot; its temporary INSIGHT bonus never extends its duration.

**The formerly confirmed Tactical Adaptation, subsequently renamed Quick Study, has been retired.** Stable historical ID `tactical-adaptation` is **absent from the 31 active Skills**, no longer learnable or included in filters. It is listed in a separate collapsed **Archived Skills** section, with its former behavior and retirement rationale. Its former passive offense bonus could come online very early for high-INSIGHT pilots, remain indefinitely, and overlap with class-limited Frame Combat Proficiency. The suggestion to delay it until First Watch ends was also rejected because it would paradoxically activate later for higher-INSIGHT pilots. Do not implement or assume that rejected change.

**Legacy build migration:** same browser storage key `fd-skill-lab-v1` and unchanged schema version 1. On load/import, input `abilityBonus.INSIGHT` is preferred; older `abilityBonus.AWARENESS` and older `abilityBonus.SENSOR` are accepted and converted to INSIGHT. When `skillLevels["tactical-adaptation"]` is found, its historical Lv is stored under `retiredSkillLevels["tactical-adaptation"]` for archival display, but it **does not consume training points**. The abandoned rank's points are thus available for new training. New JSON exports retain the archival rank metadata and use INSIGHT. All other Skill IDs, acquisition ranks and costs remain intact. Reset preserves archived-history metadata.

This release changes public Skill Lab only; private game Core and canonical specifications remain unchanged. Candidate Skill names among the 26 unfinished concepts have **not** been wholesale renamed to English or approved. Historical sections in this README and the notes are preserved as design records; this v0.15 section supersedes conflicts in older names, counts and Skill decisions.

## v0.16 — Stay Frosty confirmed (2026-10-23)

**Current Skill Lab:** 31 active Skills (6 confirmed, 25 experimental), plus Quick Study in Archived Skills. Existing five approved Skill effects are unchanged.

The former experimental `certain-evasion` / 臨戦警戒 / Combat Vigilance is now the sixth confirmed Skill, **Stay Frosty**. Its unchanged stable identifier protects localStorage and exported build ranks. Only its **newly approved rules** are reflected:

- WAIT grants an ordinary binary Reaction. **While that Reaction is still AVAILABLE**, Stay Frosty decreases the attacker's **pre-clamp HitRaw** by a Skill-dependent flat number of HitRaw points. It does not directly increase REFLEX or guarantee the same numeric improvement to the final evasion probability.
- Apply `N=base INSIGHT at sortie` (permanent training included, temporary buffs excluded): **Lv1: −floor(N/2)**, **Lv2: −floor(3N/4)**, **Lv3: −N** HitRaw points.
- Sample N10 => −5/−7/−10; N12 => −6/−9/−12; N15 => −7/−11/−15; N20 => −10/−15/−20. The Skill Lab displays the computed sample pilot numbers on each Lv and recalculates when INSIGHT is trained.
- Resolve eligible attacks with the same rules on either faction: form HitRaw, subtract Stay Frosty, then clamp ordinary hit probability to 0..100 and calculate any excess-hit Critical Penetration conversion from that final HitRaw. For example with N15 and Lv3, incoming original HitRaw130 becomes 115; hit chance stays 100% but the *excess-accuracy addition* to CritPen changes from 15 percentage points to 7.5 percentage points under the proposed CritPen conversion.
- The effect is automatic and remains active for **multiple eligible attacks as long as the usual Reaction remains unused**. Evading or being hit does not itself consume Reaction. INTERCEPT/COVER/Missile Intercept spends Reaction and ends the bonus; unused Reaction expires normally at the next own Faction Phase.
- Compatible with **Steady Nerves**: if the Reaction was not spent, it can still trigger Steady Nerves in the next own Activation. Does not extend itself with temporary INSIGHT, including First Watch's effects.
- Ordinary unit-targeted Direct FIRE / MELEE and eligible guided-impact hit checks are in the intended scope; immunity to attacks that have no such hit/evasion roll is not created. Edge cases (special profiles, area attack, multi-hit and priority of other modifiers) still require private Core implementation design and combat tests, with hidden Faction information safeguarded.
- **Important:** The public simulator is still a *Skill point planner* displaying research-defined effects; it does not execute battles, CritPen rolls or a combat pipeline. `docs/IDEAS.md` in the private game repo holds the candidate 100% excess accuracy to CritPen conversion (50% of excess and no 8% artificial cap); `docs/CORE_SPEC.md` continues to describe legacy Core. Skill Lab v0.16 does not modify the private Core or canonical specifications.

Previous sections of this document are retained as historical snapshots; this v0.16 section supersedes their older Skill status and placeholder numeric descriptions.

## v0.17 — Right on Cue and Got Your Six confirmed (2026-10-23)

**31 active Skills: 8 confirmed and 23 exploratory, plus Quick Study archived separately.** Previous six confirmed Skills retain their effects.

**Right on Cue** (stable ID `reaction-shooter`, formerly 迎撃射撃術): legal ordinary Reaction INTERCEPT **and** Missile Intercept gain effective **SHOOTING +2/+4/+6** at Lv1/2/3. Ordinary INTERCEPT unit-targeted accuracy has SHOOTING coefficient 3, so gains HitRaw **+6/+12/+18**, contributing to over-100 hit accuracy/CritPen on eligible weapons under the design study. Missile Intercept instead has SHOOTING coefficient 2, so gains InterceptHitRaw **+4/+8/+12**. Missile Intercept has no CritPen. It works for eligible self- or allied-target Missile Intercept but not Main Action attacks or COVER. All normal Reaction, weapon/ammo and legality requirements remain.

**Got Your Six** (stable ID `guardian-reaction`, formerly 護衛反応 and DRS Option-inspired): the Pilot gains effective **REFLEX +3/+6/+9** at Lv1/2/3 **only while using COVER or Missile Intercept to protect another Friendly Unit**. COVER protects a different adjacent Friendly Unit from an eligible already committed single-target attack by substituting the coverer as the final defender, without physically moving; normal Direct FIRE, single-target Melee and guided missiles are in scope, while area/hex/direction-targeted attacks and attacks generated by Reaction are excluded. When COVERing an eligible Direct FIRE/Melee/guided Missile hit, REFLEX coefficient 3 yields enemy HitRaw **−9/−18/−27**. When performing Missile Intercept for an ally, REFLEX coefficient 2 yields InterceptHitRaw **+6/+12/+18**. Does not improve self-defense, self-target Missile Intercept or ordinary attacking INTERCEPT. No extra Reaction is granted.

**Core separation:** Defensive Response Suite is still a physical Option implemented in the private game's Core with a separate +2 qualifying REFLEX effect. Skill Lab confirmation is **not** equipment deletion, a decision to stack effects, or implementation of the skill into Core. Preserve the existing Skill IDs and browser/JSON saves. Gameplay formulas are notes in the simulator; it only allocates points, not actual battle resolution. Historical descriptions in this README are superseded by v0.17 where they conflict.

## v0.18 — Stay Frosty effective REFLEX rework (2026-10-23)

The confirmed **Stay Frosty** skill (ID `certain-evasion`) has been redesigned as a conditional **effective REFLEX boost** while the Pilot holds an AVAILABLE Reaction from WAIT. The former bespoke, direct negative incoming-HitRaw modifier is superseded. All other confirmed Skill effects and stable Skill IDs are preserved.

- On sortie snapshot **base INSIGHT** after permanent pilot training; exclude temporary INSIGHT Skill bonuses (including First Watch). Use the base to calculate Lv1 **effective REFLEX +ceil(INSIGHT/6)**, Lv2 **+ceil(INSIGHT/4)**, Lv3 **+ceil(INSIGHT/3)**.
- Sample INSIGHT 10 gives **REFLEX +2/+3/+4**; INSIGHT 15 gives **+3/+4/+5**; INSIGHT 18 gives **+3/+5/+6**; INSIGHT 20 gives **+4/+5/+7**. The main Lv1–3 card fields show these numerical sample-Pilot REFLEX gains, recalculated from the user's INSIGHT point allocation; expanded per-Skill details retain the exact formulas.
- This is **effective REFLEX, not an extra bonus only on being attacked**. Apply it consistently in any otherwise eligible REFLEX-derived computation while Reaction is held: ordinary target defense, qualified guided-Missile terminal hit defense, Missile Intercept accuracy, and a committed qualifying COVER. For ordinary single-unit Direct FIRE / Melee, REFLEX +1 lowers attacker's pre-clamp HitRaw by 3; for Missile Intercept, REFLEX +1 increases InterceptHitRaw by 2. If an eligible attack is already above 100 HitRaw, the reduced attacker HitRaw also decreases prospective excess-accuracy CritPen (candidate design) under the same normal formula.
- If the Pilot **starts a legal INTERCEPT / COVER / Missile Intercept while Reaction is available**, the skill bonus applies through **that Reaction's own resolution**, even though the Reaction is consumed by the action's commit. It is no longer available for subsequent attacks or checks after the consumed Reaction. Merely being attacked, hitting or dodging does not itself consume Reaction. Unspent Reaction expires at the next own Faction Phase as usual; this may trigger separately purchased Steady Nerves.
- No new button, Reaction stock, cooldown or uses. `Got Your Six` may strengthen REFLEX further in an eligible ally-protection Reaction when both skills are learned; the *private Core Option* Defensive Response Suite's equipment/stacking treatment is still unresolved.
- The public simulator only models **Training Point allocations and per-skill sample values**, not actual battles, Reaction timing, or CritPen rolls. The private game Core and canonical specifications are not modified.

## v0.19 — Against the Odds (2026-10-26)

**Against the Odds** (new stable Skill ID `against-the-odds`) is added as an active research candidate. **English name is selected; numerical coefficients are research baselines, not final balance approval.** This is **not** a ninth confirmed Skill. Active catalogue: **32 Skills (8 confirmed, 24 provisional)**; archived Quick Study remains separate.

- **Concept:** A passive mental/combat-instinct technique that makes an infrequent successful Hit more likely to find an armor weakness when normal Hit Chance is low. It neither increases ordinary Hit Chance nor multiplies weapon Power. Applies to **both shooting and melee**, but only to attacks whose weapon has **CritPen YES**, and only when normal Penetration leaves `EffectiveArmor > 0`. No extra command, Action, Reaction, charge or currency.
- **Research formula:** Set `H = clamp(floor(HitRaw), 0, 100)`, `C0 = min(100, max(2, 4 + 0.5*(EffectiveSHOOTING_or_MELEE - 10)) + 0.5*max(0, floor(HitRaw)-100))`. For Skill level `L` in 1..3, `BonusRaw = min(10*L, 60*L*((100-H)/100)^2)`, `Bonus = floor(2*BonusRaw)/2` in percentage points, and `CritPenWithSkill = min(100, C0 + Bonus)`. Use half-point precision, existing CritPen qualification and usual probability clamp; this remains a study design only.
- **Examples:** At H=70%, Skill Bonuses are +5/+10.5/+16pt at Lv1/2/3, and with C0=4% the resulting conditional CritPen rates are 9/14.5/20%. At H=60% bonuses are +9.5/+19/+28.5pt, resulting in 13.5/23/32.5% with C0=4%. Increasing low-H effects and preserving high-H excess-accuracy rewards are deliberate. The possibility that a lower-H attack yields greater expected armor-bypass damage against very heavy armor is accepted as a potential tactical specialization, not an automatic reason for rejection.
- **Eligible melee under the current weapon table:** Combat Knife (CritPen YES). BASH, Assault Lance and Explosive Axe currently have CritPen NO. Current ranged NO weapons, guided Missile, Missile Intercept and Area/Hex attacks gain no CritPen.
- **Existing resolution preserved:** In ordinary multi-hit Direct FIRE, each attempt has its own Hit roll but the whole Attack has at most one CritPen roll, and only the corresponding successful Hit ignores Armor. Combat Knife's six-Hex AreaMelee treats each affected target as its own Melee Attack for CritPen eligibility. Do not grant repeated CritPen rolls to SMG/GPMG bursts.
- **Scope:** Skill Lab is a Training Point allocation simulator, not a combat simulator. New card and formula help illustrate prospective outcomes; no RNG, attack resolution or change to the private Core. Preserve existing Skill IDs and saved builds. Old README design-log paragraphs are historical and are overridden by the current main-repository canonical specifications where inconsistent.

## v0.20 — Provisional simultaneous paired-weapon FIRE skill (2026-10-26)

**Provisional card:** `二丁同時射撃（仮）` (`paired-fire`). The name and Lv1–3 penalties are **not finalized**. The Skill Lab now shows 33 active Skills (8 confirmed, 25 provisional), plus archived Quick Study.

**Proposed player behavior:** Equip two copies of exactly the same standard `UnitTargetedDirectFire` Weapon Definition and select either one for an ordinary FIRE. If both are eligible for firing, the passive skill automatically fires **both** at the same original Unit target. No extra active ability button or second Main Action is added. The 1 Main Action contains two independent weapon Attacks; both equipped entries retain distinct runtime ammunition identities and spend their normal `AmmoCostPerAttack`. No automatic retargeting on destruction.

**Provisional level values:** Lv1: both weapon Attack HitRaw values **−40 points**; Lv2 **−30 points**; Lv3 **−20 points**. Apply each penalty within its weapon's normal accuracy calculation, along with the usual shooter SHOOTING, target REFLEX, movement/terrain and other permitted situational modifiers; clamp to 0–100% per Hit attempt. Example with SHOOTING10, REFLEX10, no other modifier: SMG or Assault Rifle (ACC95) gives per-Hit 55/65/75%, and Shotgun (ACC105) 65/75/85%, across Lv1/2/3. The build planner shows these examples dynamically as the sample pilot's base SHOOTING changes; it does not simulate combat.

**Ammo, capacity, hit attempts:** SMG×2 has 3+3 Hit attempts and spends 3+3 Ready rounds; GPMG-6×2 has 2+2 attempts and spends 2+2 rounds; Shotgun/Assault Rifle/Sniper Rifle×2 each produces two single-shot Attacks with one round spent from each copy. Weapon capacity is paid twice: SMG/Assault Rifle/Shotgun pairs cost 2 (any Frame class); GPMG-6/Sniper Rifle pairs cost 4 (Heavy only). Each weapon's own RELOAD rules remain.

**CritPen:** Two independent weapon Attacks mean that a **CritPen YES** pair can make up to one CritPen roll **per weapon Attack** (two total), contingent on qualifying Hits and remaining effective Armor. In each Attack, success ignores armor for only its own eligible Hit. A Shotgun is CritPen NO and gains no CritPen. Against the Odds can stack on the two qualifying Attack calculations, but the combined Skill investment at Lv3+Lv3 would be six Training Points.

**Open mechanics / scope:** Final naming, balance, auto-single fallback when the second weapon is not ready, Reaction-INTERCEPT scope, and exact COVER/Exposure/Signature once-per-composite-action orchestration still require separate design work. The preferred concept gives only one original targeting/COVER/Exposure opportunity despite two weapon Attacks. Fired ammunition is spent for both as part of the committed composite action, with unneeded Hit attempts skipped after destruction. Presentation may depict simultaneous fire while Core resolves outcomes deterministically. Do not automatically extend the skill to missiles, direction-/Hex-targeted Area weapons, Melee, Missile Intercept or other attack families. No edits to private game Core and no confirmed individual Skill migration. This is a Training Point build planner, not a tactical simulator.


## v0.21 — First Watch design status reopened (2026-10-26)

First Watch (stable ID `early-starter`) is now **under review**, not confirmed. Its old level effects and INSIGHT-dependent duration remain provisional reference values; the Skill Lab saved builds and skill IDs are preserved. 33 active entries: 7 confirmed and 26 provisional. This change does not modify the private game's Core.

## v0.22 — Plant Your Feet / Keep Moving; observation deferred (2026-10-26)

**Current Skill Lab status:** 33 active entries, 9 Skill Lab design-confirmed and 24 provisional/on hold; 1 archived Quick Study. Changes here concern **research design**, not canonical individual Core Skill implementation. Existing Skill IDs, storage key and saved builds are unchanged.

### Plant Your Feet — design-confirmed

- Stable Skill ID: `marksmanship` (renamed from the provisional Japanese label 精密射撃).
- Passive trigger: make a qualifying **ordinary Unit-targeted Direct FIRE** before performing one's own ordinary MOVE in the same Activation. This requires a legal target Track, Range and Direct-Fire LOS before moving; moving afterward via a valid MSU sequence does **not** disqualify the shot retroactively. A Light Frame's post-action DISPLACE similarly does not change an already-resolved FIRE.
- Effective SHOOTING is **+2 / +4 / +6** for Lv1 / Lv2 / Lv3. In normal unit-target accuracy, that contributes **+6 / +12 / +18 HitRaw points** before clamp. The approved effective-Ability/excess-HitRaw CritPen design uses the same applicable effective SHOOTING. No extra ammo, dedicated Action or Skill-charge system.
- This confirmation covers the normal own-Activation Unit-targeted FIRE use discussed. Reaction INTERCEPT and special attack families are **not automatically broadened** by this entry. Original Fire Control Stabilizer Option remains in private Core; its eventual migration/replacement and stacking are separately open.

### Keep Moving — design-confirmed

- Stable Skill ID: `mobile-evasion` (renamed from provisional 機動回避).
- Passive trigger: successfully enter **at least 3 actual Hexes** during the Pilot's own **ordinary MOVE**. The third successful Hex entry activates the effect, not a planned path length or 3 Movement-cost points. If movement is halted earlier, it never activates. REPOSITION and Light DISPLACE do not supply qualifying ordinary-MOVE entries.
- Effective REFLEX **+2 / +4 / +6** at Lv1 / Lv2 / Lv3; effect persists through intervening Faction Phases and expires at start of the Unit's next own Faction Phase. In normal direct-fire or Melee defense, attacker HitRaw is reduced by **6 / 12 / 18** points; other otherwise-eligible effective REFLEX uses (including guided missile terminal defense and Missile Intercept) also receive the bonus through their respective formulas. Missile Intercept's coefficient 2 yields **+4 / +8 / +12** accuracy points while this Skill is active.
- Movement can expose the Pilot to enemy sensors/INTERCEPT; eligible weapons may incur their ordinary self-movement firing modifiers. No separate gauge, penalty or command is invented. The existing Maneuver Assist System (MAS) Option remains in the private Core; eventual removal/stacking and full migration details are separately open.

### Reopened / deferred candidates

- **First Watch** (ID `early-starter`): remains *under review* following v0.21; former INSIGHT-based duration and Lv1–3 values are comparison material, not confirmed design.
- **定点観測** (ID `observation-discipline`): **on hold**. The former stationary Activation completion → INSIGHT +4/+8/+12 design is historical comparison data, not adopted. MOVE→WAIT or WAIT-only variants were explored but are not approved: WAIT is often the default when a moved unit has no legal attack, and passive extended detection risks displacing the distinct ACTIVE SCAN action. Do not add a complex second WAIT variant or suppress the normal Reaction as a forced cost.
- All other Skill Lab confirmed/provisional entries retain their prior state. The independent Skill Lab remains an allocation/suggestion tool, not a combat simulator.


## v0.23 — Reopen three WAIT / Reaction skill designs (2026-10-26)

The user requested that **every confirmed WAIT / Reaction Skill except Got Your Six** return to design review. These three Skill Lab cards now have status **under review**, without removing or archiving their prior effects and Lv1–3 research values:

- `reaction-shooter` — Right on Cue
- `burst-focus` — Steady Nerves
- `certain-evasion` — Stay Frosty

**Got Your Six** (`guardian-reaction`) remains **confirmed**. The other five confirmed entries are Frame Combat Proficiency (Light / Standard / Heavy), Plant Your Feet, and Keep Moving. First Watch remains under review and 定点観測 remains on hold. The total active catalogue is unchanged at **33**: **6 confirmed / 27 provisional or on hold**. Archived Quick Study remains 1.

These are status changes only, not automatic balance adjustments. The former formulas and effect details stay accessible for design comparisons; Skill IDs, point-allocation behavior, JSON imports/exports and existing browser saves stay intact. Historical README sections describing older confirmed counts and effects remain dated design history, superseded for current status by this v0.23 record. Nothing is migrated to, or changed in, the private production Core.

## v0.24 — On the Charge, Hunker Down, Fired Up, Go Dark (2026-10-27)

**Current status:** 34 active Skills, 10 Skill Lab design-confirmed and 24 under review/on hold; archived Quick Study remains unchanged. Research design decisions in Skill Lab are **not** changes to the private production Core. This update preserves every pre-existing Skill ID, build JSON schema, storage key, existing saved point allocations and archived entries. Fired Up adds one entirely new Skill ID. Confirmed names remain English-only.

### On the Charge — confirmed

- Existing ID `momentum-melee` (previous Japanese working title 助走白兵), Option-derived from Close Combat Assist System.
- When the Pilot's **own ordinary MOVE** successfully enters at least three Hexes, eligible **MELEE in the same Activation** receives effective MELEE **+2/+4/+6** by Lv, equal to typical normal melee HitRaw **+6/+12/+18** before clamp. Movement-point costs and planned routes do not substitute for actual successful entries; Light DISPLACE and REPOSITION are excluded.
- Effective MELEE participates in the revised CritPen calculation for eligible CritPen YES attacks, such as Combat Knife. The existing CCAS Option remains in private Core; Skill/Option migration and stacking are not approved.

### Hunker Down — confirmed for Skill Lab

- Existing ID `brace-discipline` (former working title 防御姿勢術), Option-derived from Armor Reinforcement Suite.
- On **BRACE**, gain **additional Armor +1/+2/+3** beyond the BRACE baseline +2, for a **total BRACE bonus of +3/+4/+5**, following ordinary BRACE duration and expiry.
- In addition, after ordinary Armor/Penetration/damage resolution, a Hit that would inflict exactly **1 final HP damage** instead inflicts **0**. This is an explicit exception to the current minimum-damage rule and applies separately to each Hit in multi-hit attacks. The attack still **Hit**, and the Hit remains eligible to trigger Fired Up even at 0 damage.
- Strong penetration and eligible CritPen armor bypass remain dangerous. No new action command or free Reaction. Existing Armor Reinforcement Suite persists in Core, not changed by this Lab decision.

### Fired Up — newly added, confirmed for Skill Lab

- **New stable Skill ID:** `fired-up`, category 被弾・HP; 3 levels, 1 Training Point per level.
- One or more actual **Hits** from hostile Attacks activate a **binary** boost for the Pilot's **next own Activation**: effective SHOOTING and MELEE **+6/+9/+12** for Lv1/2/3. **Non-stacking**: two or more attacks do not increase the amount. All Hits in one multihit Attack count as that Attack having Hit, not multiple stacks. Normal defensive Armor or Hunker Down zeroing the final damage does **not** cancel the Hit trigger.
- The boost benefits eligible HitRaw calculations (+18/+27/+36 for ordinary coefficient-3 Hit formulas) and the approved revised effective-Ability/excess-HitRaw CritPen calculation. It expires **at the end of that next own Activation**, rather than lasting a mission or stacking through later turns.
- Timing of a hostile INTERCEPT Hit during the Pilot's current Activation is explicitly **next**, not retroactive. Exact Hit/affected-target qualification for attacks with no usual Hit roll (e.g. Area weapons) remains for future Core integration review. The Skill Lab is an allocation preview, not a battle simulation.

### Go Dark — foundational design confirmed; Signature levels provisional

- Existing ID `conceal-discipline` (former working title 隠密動作), Option-derived from Signature Reduction Suite.
- On **CONCEAL**, the Unit's own sensor-based Detection and sensor-derived Local Track contribution **stop entirely** while the effect is active; merely setting Detection Power to zero is inadequate, because target Signature may still yield valid detections. Other established Track sources such as adjacency Proximity are not silently disabled.
- Legitimate **Datalink reception remains available**; the unit can rely on another friendly observer but loses the ability to detect advancing targets itself. CONCEAL still uses its normal Main Action and expires at the start of the next own Faction Phase; ordinary sensing then resumes, with normal information reconciliation. The unit cannot maintain CONCEAL while moving the following own Turn under the current action rules.
- For comparison, the Skill Lab displays **total CONCEAL Signature modifiers of −2/−3/−4** at Lv1/2/3 (baseline normal CONCEAL is −1), explicitly marked **provisional numeric levels**. The general stealth/sensor tradeoff and Go Dark name are selected, but those numbers are NOT final approved game balance.
- Existing SRS Option stays in private Core; future Skill/Option stacking and replacement remain separate decisions.

### Current confirmed roster

Frame Combat Proficiency (Light, Standard, Heavy); Plant Your Feet; Keep Moving; On the Charge; Got Your Six; Hunker Down; Go Dark (Signature numbers provisional); Fired Up.

First Watch, Right on Cue, Steady Nerves and Stay Frosty remain reopened for design review, and 定点観測 remains on hold. Against the Odds has an agreed **name**, but its mathematical formula has **not** been promoted to confirmed. 二丁同時射撃 remains provisional. Prior version logs are historical; this v0.24 section overrides older status and counts.

## v0.25 — Keep Watch and Sweep the Sector confirmed (2026-10-27)

Skill Lab version v0.25 maintains **34 active Skills (12 confirmed, 22 under review/on hold)** and the separately archived Quick Study. No source Skill IDs, localStorage key, saved build format or retired histories have changed. These decisions concern independent Skill Lab research, not private production Core changes.

### Keep Watch (former 定点観測), existing ID `observation-discipline`

- **Confirmed Skill Lab name and Lv effects**: Lv1/2/3 **effective INSIGHT +4/+8/+12**.
- Trigger: finish an own Activation without committing an ordinary self-MOVE. The Skill activates only **after** its Main Action (FIRE, ACTIVE SCAN, etc.) or WAIT fully resolves and the Activation is Completed. Earlier Attack/scan/Reaction results are not modified retroactively.
- Duration: through intervening hostile/other-faction Phases and own Faction Phase transitions, until the Unit begins its **next own Activation** (not simply the next Faction Phase start). A not-yet-activated observing Unit can still share legitimate Track while allies act first.
- Effective INSIGHT contributes to Detection Power one-for-one: BasicDetectionBudget = floor(DetectionPower/4), hence the +4/+8/+12 provides **+1/+2/+3 base sensor budget**. This is not guaranteed geographical Hex detection; target Signature, Terrain Sensor Cost, blockers, weather, Smoke and Datalink restrictions remain authoritative.
- The Skill creates meaningful decisions about movement versus positional overwatch, early versus late Activation, flank observations, and combination with **Plant Your Feet**. Light Frame's native post-Action DISPLACE does not count as ordinary MOVE. Standard/Heavy MSU post-Action ordinary MOVE does count and prevents qualification.
- Existing Sensor Stabilizer Option remains in private Core, including its current +4 Detection Power and lifecycle. Future replacement/stacking with Keep Watch is unresolved.

### Sweep the Sector (former 能動走査術), existing ID `scan-interpretation`

- **Confirmed Skill Lab name and Lv effects**: during the instantaneous **ACTIVE SCAN** calculation, effective INSIGHT **+4/+8/+12**.
- The standard ACTIVE SCAN contribution remains instant **Detection Power +12**, making its total Skill-assisted instant bonus **+16/+20/+24** at levels 1/2/3 (excluding other unconfirmed stacking from Options). There is no continued INSIGHT bonus after the scan completes.
- ACTIVE SCAN still consumes the Main Action and creates its ordinary temporary **scanner Signature +2**, preserving normal information reconciliation, exposure, Datalink, range/line cost and blockers.
- **Synergy, not simultaneity:** if ACTIVE SCAN is used without ordinary MOVE and the Unit also owns Keep Watch, the scan first uses Sweep the Sector's instantaneous bonus, then after the entire Activation completes Keep Watch's passive observation boost begins. Keep Watch's bonus is **not** added during that ACTIVE SCAN. The wider instant scan can produce contacts/Last Known, while the smaller continued observation can preserve some valid Tracks for allies.
- The existing Active Scan Amplifier Option remains in the private Core; its replacement, stacking and integration with the Skill are separate future decisions.

### Confirmed roster and remaining statuses

Confirmed Skill Lab entries now comprise Frame Combat Proficiency (Light/Standard/Heavy), Plant Your Feet, Keep Moving, On the Charge, Got Your Six, Hunker Down, Go Dark (its Signature numbers remain explicitly provisional), Fired Up, Keep Watch and Sweep the Sector.

First Watch, Right on Cue, Steady Nerves and Stay Frosty remain under review. Against the Odds keeps its agreed name but provisional formula; paired fire remains provisional. Previous notes treating 定点観測 as on hold or 能動走査術 as undecided are historical and superseded by this record. No code implementation or game balance certification is implied.

## v0.26 — On Your Own confirmed (2026-10-27)

The existing Skill Lab entry `solo-operator` is now named **On Your Own** and moved to **confirmed** status. It is not a new Skill entry; IDs, existing allocations, archived entries, import/export and `fd-skill-lab-v1` saved builds are unchanged. Total: **34 active Skills; 13 confirmed, 21 unconfirmed; 1 separately archived Quick Study**. This changes the **independent Skill Lab's research design only**, not the private production Core.

### Conditions and approved Skill Lab research formula

- While there is **no other Friendly Unit within geometric Hex distance 4 inclusive** of the Pilot, the Pilot receives an effective **SHOOTING** increase. At Hex distance 5 and beyond the isolation condition can be met. Range to Hostiles is **not** an extra condition. Distance is Hex geometry, not MOVE path cost.
- This is a positional condition rather than a distinct Action: it updates as other Friendly Unit positions change, and does not require the Pilot to MOVE. Enemy position, forward/back rank, terrain, weapon class and Action order are not extra gates.
- The current explicit Skill Lab scaling model is `1 + floor(SortieBaseINSIGHT * SkillLevel / 6)`. The **SortieBaseINSIGHT** includes permanent Training Point gains but does **not** include temporary INSIGHT boosts from Keep Watch, Sweep the Sector and other conditions. This protects against recursive temporary scaling.
- Illustrative effective SHOOTING bonuses: INSIGHT 10 → Lv1 +2, Lv2 +4, Lv3 +6; INSIGHT 14 → +3/+5/+8; INSIGHT 18 → +4/+7/+10. The Skill Lab displays computed values dynamically as the sample Pilot's permanently trained INSIGHT changes.
- There is **no REFLEX bonus**, no MELEE bonus and no added defensive protection. Isolation makes COVER by nearby allies unavailable and exposes a forward scout to risk; a slower Heavy Frame left behind might instead exploit this condition for long-range FIRE but must still satisfy range, LOS and legal Track requirements.
- Legitimate Datalink reception remains available even when isolated, subject to existing jamming/sharing rules. SHOOTING affects eligible HitRaw and CritPen calculations; it does not automatically grant a shot or alter weapon range. Combines with Plant Your Feet when stationary, with Go Dark for a temporary concealment/then-fire pattern, and possibly with Keep Watch in flanking observation positions.
- The category remains `距離・布陣`, origin `IDEAS`, Skill ID `solo-operator`. Unlike the discarded early concept, **SHOOTING and REFLEX are NOT both increased**. The high-INSIGHT scaling and geometric isolation are approved as Skill Lab's current concrete design, but have not undergone comprehensive combat balance tests.

### Other statuses unchanged

First Watch, Right on Cue, Steady Nerves and Stay Frosty remain in review, and numerical Go Dark Signature effects remain provisional. Keep Watch, Sweep the Sector and the other previously confirmed skills are unchanged. The prior v0.25 totals/history are superseded by this dated entry.

## v0.27 — Pick Your Ground confirmed (2026-10-27)

**Pick Your Ground** is a newly added Skill with ID `pick-your-ground`, category `地形・陣地`, source `新規アイデア`, and Skill Lab status **confirmed**. Now **35 active Skills: 14 confirmed, 21 unconfirmed**, plus 1 archived Quick Study. The existing localStorage format/key `fd-skill-lab-v1`, existing 34 active Skill IDs and saved allocation semantics remain unchanged. The production Core has **not** been modified.

### Mechanics (skill-specific additive positional-cover protection)

- While the Pilot's Hex carries a **negative positional CoverHitModifier** from Forest, Rubble or a stronger Fortified Position such as Revetment, improve that cover by **−5/−10/−15 HitRaw points at Lv1/Lv2/Lv3**, respectively. It does not change REFLEX, Armor, Signature or the Pilot's other effective Abilities.
- Baseline Forest/Rubble cover −10 becomes −15/−20/−25; baseline Revetment cover −15 becomes −20/−25/−30. Plain, road, passable Rock and other Hexes with cover 0 **do not gain cover from this Skill**. Fortification may grant cover on otherwise open ground.
- Preserve Core's strongest-only positional rule: `BaseCover = min(TerrainCover, FortifiedPositionCover)`. If `BaseCover < 0`, use `BaseCover - (5 × SkillLv)`; otherwise use `BaseCover`. **Do not add the bonuses separately to terrain and emplacement and then stack them.**
- Applies only to attacks whose existing Core hit calculation actually consults positional cover: ordinary Unit-targeted Direct FIRE and applicable guided missile hits. Does **not** grant protection against MELEE or Area/Hex damage that does not consult the positional cover modifier; does **not** enhance the ally-protecting Reaction named COVER. This is **not** a global evasion/REFLEX buff.
- Movement costs, Line of Sight, Range and detection/Track constraints still apply. Synergies: Keep Moving for moving into a strong cover Hex; Plant Your Feet/Keep Watch for holding favorable firing/observation positions; On Your Own for isolated covered flanking.
- The Skill Lab is a **Training Point allocation and Skill comparison simulator, not an actual battlefield simulator**. The Skill's Lv cards and expanded calculation notes give deterministic examples. Balance and implementation interactions remain subject to later Core integration and playtesting.

The v0.26 On Your Own skill and other existing Skill statuses remain unchanged.
