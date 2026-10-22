# FRAME DOCTRINE — PILOT SKILL LAB

A standalone browser-based simulator for experimental pilot skill builds in FRAME DOCTRINE: LAST RESORT.

**Status:** Research prototype v0.4. The game project itself is separate and is not included in this public repository. None of the proposed skills or balance numbers are official game specifications.

## Features

- 25 experimental pilot skills (original research ideas and Option-inspired candidates)
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

When a Skill says it grants an effective Ability bonus (SHOOTING, MELEE, SENSOR or REFLEX), the intended *research direction* is to use the resulting effective Ability in all relevant calculations, rather than granting narrow +Hit% / +Evasion% substitutions. This still requires explicit combat-design review before any change to the private Core.

This app currently simulates **training-point allocation only**, not on-map kill events, HP reductions, Action outcomes, or chance rolls.

## Ability cap removal and limited guaranteed outcomes (2026-10-23)

**New accepted research direction (not yet canonical Core):**
- Remove the numeric ceiling on both *base* and *effective* Pilot Abilities (SHOOTING, MELEE, SENSOR, REFLEX). A player may continue investing Training Points into a base Ability past 20, subject to their finite Training Point budget.
- Conditional Skill boosts stack into the effective Ability and use that full value consistently in all relevant Ability-dependent calculations.
- Extreme accuracy and evasion are allowed to become correspondingly strong. Probability quantities, however, are still bounded by 0–100%; removing an Ability ceiling is **not** removing probability bounds.
- Balance through finite growth points, real activation conditions, opportunity costs and build tradeoffs, not a universal ability ceiling. Do not silently migrate this rule into the private game Core or master specs.

**New speculative Skills (not approved effects):**
- **必中の一撃 / Decisive Shot:** a limited number of eligible attacks per Mission become guaranteed hits; draft ranks allow 1/2/3 uses. Prefer an understandable passive/conditional trigger over another active command. What counts as an eligible attack, how a use is spent and whether a 100% base hit consumes it remain unresolved.
- **完全回避 / Certain Evasion:** evade exactly one qualifying incoming attack after a preparation cost. Working non-active version is to use existing WAIT as its trigger, with 1/2/3 prepared guaranteed evades per Mission by rank. This is a proposal, not approval of specific timing or effect.
- In interactions between guaranteed hit and guaranteed dodge, the governing priority is **undecided**. Direct Fire vs Missile vs Area/multi-hit and interactions with critical penetration need explicit rules. Do not infer priorities from the labels alone.

The skill-list page models **purchase allocation**, not true combat resolution or activation charges. These new entries are deliberately labeled exploratory.
