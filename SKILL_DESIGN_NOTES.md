# Skill Lab — パッシブ中心のスキル設計・コスト一覧

**現行版 v0.30（2026-10-29）：** 現役37件（確定16、検討中・保留21）＋取り下げたQuick Studyのアーカイブ1件。確定スキル名は日本語UIでも英語表記。現行の第3Pilot Ability表示はINSIGHT（旧AWARENESS）。以下の以前の検討メモは歴史的な記録であり、競合する場合には末尾の最新バージョンの決定を優先する。


**2026-10-23の研究メモ。正式ゲーム仕様・実装依頼ではない。途中で方針変更可能。**

## 設計原則

原則として**パッシブ・条件付き・Reaction連動型のスキル**を優先する。新たなアクティブコマンド、MP、スタミナ、クールダウン、ミッション専用の回数カウンターは標準装備にしない。アクティブスキルも禁止はしないが、追加する場合は操作とリソース管理の負担に見合う意味がある場合に限る。

カードゲームのコストとリターンの発想を採用する。「どんな利益か」だけでなく「何を犠牲にするか」「どんな戦術上の危険を受けるか」「何と交換になるか」から設計する。

- **発動条件**と**消費コスト**と**機会損失・危険**を区別する。
- プレイヤーがすでに管理している資源（Action、Reaction、MOVE、弾薬、位置、索敵、Signature、時間）を優先する。
- 能力値を参照して発動確率や効果量が変わるスキルを積極的に検討する。参照するのは効果中の**実効Ability**。
- 高Abilityなら高確率・強効果を許す方針だが、確率そのものは0～100%で扱う。
- 発動条件、判定回数、対象攻撃を透明化し、Battle Logやプレビューで説明可能にする。

## 既存リソース・交換可能なコスト

| 種類 | 種別 | スキル設計への応用 |
|---|---|---|
| Main Action | 既存 | 攻撃・索敵・BRACEなど他の主行動を諦める |
| Reaction | 既存 | WAITで得られる1回のINTERCEPT／COVERを何に使うか |
| MOVEの機会 | 既存 | 移動せず精密射撃・観測する |
| 移動量・経路 | 既存 | 3Hex助走、回り道、警戒移動とのトレードオフ |
| 弾薬・RELOAD | 既存 | 追加弾薬と装填の機会を払って連射する |
| HP・被弾リスク | 既存 | 体力を払う、低HPで危険を引き受ける |
| 位置・地形・遮蔽 | 既存 | 孤立・接近・遮蔽放棄で別の利点を得る |
| Signature／CONCEAL | 既存 | 露見リスク、隠密喪失と交換する |
| TRACK・LOS | 既存条件 | 索敵・追跡維持の達成条件。直接支払う消費資源ではない |
| 残り時間・Extraction Deadline | 既存 | 準備のための待機・遅れは撤収リスク |
| 味方布陣・連携 | 既存条件 | 友軍距離・援護態勢・行動順の制約 |
| 装備枠・武器相性 | 既存 | 装備選択・不適合装備という機会費用 |
| 育成ポイント | 研究中の育成経済 | 他のAbilityやSkillを取得しない選択 |
| 専用の発動回数 | 新規管理 | 必中・完全回避向けの例外。増やしすぎない |

## 現行Coreとの対応

- 普通MOVEは通常1Activationにつき最大1回、Main Actionも最大1回。MSUとLight DISPLACEは別の明示的例外。
- WAITで得られるReactionはAVAILABLE/UNAVAILABLEの二値で、複数ストックできない。使わずに消えることもコストになる。
- Normal/Cautious MOVEの違いがすでにあり、移動・索敵・露見などがつながっている。
- `AmmoCostPerAttack` と `HitAttemptCount` は**独立した項目**。弾薬2発消費でHit Attempt2回など、1回のFIREを複数命中判定にできる土台は存在する。ただし今回のスキルは未実装。
- 発射Signatureとその継続、TRACK、射線、地形、Extraction Deadlineは既存のコストや条件として使える。

## 新規スキル候補（すべて仮案）

### 見切り回避
命中後に実効REFLEX×倍率%で「攻撃が当たらなかった」扱いにするパッシブ候補。Lv1/2/3倍率は1/2/3倍を仮置き。多段攻撃で各弾ごとに抽選すると効果が大きく変わるため判定単位を決める。必中・完全回避との競合も要検討。

### 脚部制圧射撃
命中した射撃で実効SHOOTING×倍率%の確率で相手の次の自Faction Phaseの普通MOVEを妨害する候補。Lv倍率1/2/3倍は仮置き。相手の全Actionは封じない比較案。生物・飛行・車両・特殊敵への適用、新状態の必要性、各Hit/Attack単位の判定回数を検討。現行IR-9 Forced Halt（現在の移動中断）とは別効果。

### 二連速射
追加の弾薬消費で1回のFIRE内に複数回のHit Attemptを生む候補。単発単体対象射撃なら、弾薬2発で命中判定2回が例。Lv2/3の追加発数と追加命中判定は単なる叩き台。対象武器と追加弾薬の消費方法を検討する。自動発動のパッシブで弾薬を**望まないのに浪費させる**仕様は危険。専用アクティブコマンドなしで選択性を残す方法（事前の射撃姿勢・ロードアウト設定・射撃モード）とのトレードオフを研究する。

**重要：**スキル設計の優先順位は「パッシブ中心」であり、上記3候補の採用を意味しない。元のCoreや非公開資料を変更しない。

## 2026-10-23 追記：発動を意識させるが、発動操作は増やさない

- 自動発動型でも、条件として**特定の射程帯・距離、移動方向、射線、配置**などを要求できる。プレイヤーは必要な位置取りだけを考える。コマンドの追加とは区別する。
- **ラッキースター（仮）**：例として「7Hex先から攻撃するときにだけ有効」のような位置条件を持つスキル。これは聞き取りに基づく例で最終の距離条件ではない。効果・レベル上昇は未決。二連速射など追加弾薬を使うSkillの条件案としても検討。消耗品追加支出があれば攻撃確定の時点で一度確認できる。
- **移動射撃術（仮）**：自己MOVE後の射撃武器の既存Movement Modifierの負値を、実効REFLEXとSkill Lvを参照して緩和する。案：Lv1 floor(REFLEX/3)、Lv2 floor(2REFLEX/3)、Lv3 REFLEXだけ減少量を軽減。ただし元の負の補正の絶対値を上限とし、移動しなかった場合の攻撃より有利にしない。REFLEX10では軽減量3/6/10、REFLEX20では6/13/20。例えばアサルトライフルの-10はLv2 REFLEX10で-4、Lv3で0になる。この式は研究の仮案で、性能を保証しない。

現行Coreの事実関係：
- Assault Rifle、Heavy Autocannon、IR-9等：Move Modifier -10
- Sniper Rifle、Heavy Rail、Recoilless Rifle等：-20
- SMG、GPMG-6、Shotgun等：0
- 自己MOVEのあと同じActivationでFIREしたときの固有ペナルティ。以前のTurnのMOVEは後続Reaction射撃のペナルティとならない。DISPLACEや他者によるREPOSITIONもこの自己MOVE判定ではない。
- このSkillはAbility強化型とは違う「REFLEXを参照して状況ペナルティを軽減する型」。**単なる命中率増加と混同しない**。
- Hex-targeted、誘導Missile、Reaction/INTERCEPT等へ拡張するかは未決定。本編Coreは変更しない。

## 2026-10-23 — 確定したスキル：機体習熟3種類

**機体習熟：Light / Standard / Heavy** の各スキルは、該当機体に搭乗中、SHOOTINGとMELEEがLv1では各+1、Lv2では各+2、Lv3では各+3。REFLEX・AWARENESSへの効果なし。基礎値は不変、実効Abilityとして該当する全判定に使用する。パッシブで自動発動し、追加Action・Reaction・MP・使用回数は不要。各Lvは育成ポイント1消費。

これはSkill Labにおける正式な設計判断で、旧い+2/+3/+5%命中・回避効果案や後続の仮数値案に優先する。本編Core・マスター仕様書への実装・変更は行わない。ほかのスキルは個別の確定指示まで未確定。

## 2026-10-23 — AWARENESS名称確定・アーリースターター当時の検討記録（後の確定仕様により更新）

- Skill Labおよび今後の会話におけるPilot第3能力を **AWARENESS（状況把握）** とする。以前のSkill Lab表示SENSORとは同じ能力だが、現行C#内部の名称は `PilotStats.Detection`、機体側の `Frame.Sensor` とは別である。本編Coreは変更しない。
- **アーリースターター（当時の未確定案。下記確定仕様により上書き）**：出撃時の基礎AWARENESS÷2の切り捨て（最低1Turn）まで全体Turn 1から自動発動する比較案。AWARENESS 10→5 Turn、20→10 Turn。スキルLvによるSHOOTINGとREFLEX +1/+2/+3も未確定。全体TurnとActivationを区別し、途中のAbility変化で期間を再計算しない。
- 正の値を整数へ量子化する場合は原則floorを採用する方向で検討。現行Coreでも索敵予算や最終命中率にfloorを使用。ただし必要回数等でceilを用いる場面はあり得る。ゲーム全体の丸め仕様を決定したわけではない。
- 確定スキルフィルターボタンは再クリックでフィルター解除し、元のフィルターを復元する（Issue #1）。

## 2026-10-23 — 旧確定仕様：初動掌握 / Opening Advantage（現在は初動警戒に改訂）

- **検討状況：確定。** Skill Labの汎用スキル `early-starter` の表示名称を「初動掌握 / Opening Advantage」に変更するが、ビルド保存互換性のため内部Skill IDは維持する。
- **Lv1：** 実効SHOOTING +1、実効REFLEX +1（1P）。
- **Lv2：** 実効SHOOTING +2、実効REFLEX +2（累計2P）。
- **Lv3：** 実効SHOOTING +3、実効REFLEX +3（累計3P）。
- 完全パッシブ。全体Turn1から効果発動、`max(1, floor(出撃時の基礎AWARENESS / 2))` ターン目の最後のFaction Phaseまで有効。その次の全体Turn開始時に失効。出撃後のAbility変動は持続時間に影響しない。
- 例：基礎AWARENESS 10→5ターン、16→8ターン、20→10ターン。特別な機体制限・Action/Reaction/MP/弾薬/使用回数の追加消費なし。該当するすべてのSHOOTING/REFLEX判定で実効Abilityを使用。基礎値を変更しない。
- **設計上の意図：** AWARENESSの高い索敵型の序盤で命中と回避を強化し、後半の失効で常時スキルと区別する。高AWARENESSと高SHOOTINGが両立しない場合もビルドの価値がある。ただし、初動接敵と実ミッションの持続ターン数をプレイテストで検証。
- **変更範囲：** 独立したSkill Labの設計確定。非公開の本編Core・正式仕様の実装・変更は行わない。前段の「未確定」という記述は当時の履歴として扱い、この項目を現行判断とする。

## 2026-10-23 — 現行確定仕様：初動警戒 / Opening Vigilance

- **確定**：従来の「初動掌握 / Opening Advantage」は **「初動警戒 / Opening Vigilance」** へ改訂。旧初動掌握のSHOOTING・REFLEX強化と途中検討のMELEE追加案は取りやめ、**AWARENESS＋REFLEX** の組へ変更する。
- **Lv1:** 実効AWARENESS +1、実効REFLEX +1（1P）。**Lv2:** それぞれ+2（累計2P）。**Lv3:** それぞれ+3（累計3P）。
- パッシブ自動発動。全体Turn1から **`max(1, floor(出撃時の基礎AWARENESS / 2))`** Turn終了まで有効。全Faction Phaseの適格な索敵・回避等に適用し、次の全体Turn開始時に失効する。
- **持続時間へスキル自身のAWARENESS増加は含めない。** 出撃時の基礎AWARENESS（恒久的なAbility育成反映済み）で持続時間を1回決め、発動中の実効Ability変化では再計算しない。例：基礎AWARENESS10ならすべてのスキルLvで5Turn、16なら8Turn、20なら10Turn。
- 発動中の実効AWARENESS上昇は通常のDetection Powerへ反映する。REFLEXは通常回避とその他適格な判定に反映。機体固定制約・追加Action/Reaction・専用リソースなし。
- **既存スキルID `early-starter` 維持**で保存済みビルドを保護。4種類の確定スキルは「機体習熟Light/Standard/Heavy」と「初動警戒」。機体習熟はSHOOTING＋MELEEの現在の仕様を変更しない。6種の能力ペアを機体習熟へ拡張しない。
- 過去の旧名称・旧効果のメモは設計過程の履歴であり、この項目を現行の確定判断とする。これは公開Skill Labのみ。非公開本編Coreや公式仕様は未変更。

## 2026-10-23 — Skill Lab v0.12 統合リリース（最新版）

現在32件：**確定6件、検討中26件**。過去の各研究段階メモと競合する場合、この節を最新のSkill Lab判断として扱う。

### 仕様確定

- **機体戦闘習熟 Light / Standard / Heavy：** 表示名の変更のみ。機体区分と一致した場合に実効SHOOTING・MELEEが各Lv1:+1、Lv2:+2、Lv3:+3。索敵・防御・移動力は上がらない。既存ID `frame-light` 等を維持。
- **初動警戒 / Opening Vigilance：** 変更なし。基礎AWARENESS÷2（floor、最低1Turn）だけ全体Turn1から実効AWARENESS＋REFLEX各Lv上昇。ID `early-starter`。
- **戦況適応 / Tactical Adaptation：** 新規確定。全体Turn `max(3, 20 - 出撃時の基礎AWARENESS)` からMission終了まで、実効SHOOTING・MELEEがLv1:+1、Lv2:+2、Lv3:+3。途中の一時AWARENESS変動では発動Turnを再計算しない。
- **臨戦集中 / Combat Focus：** 旧「集中バースト」ID `burst-focus` を確定改訂。WAITで取得した通常Reactionを介在する敵/第三Faction Phaseで消費しなかった場合、次自Faction Phase開始時のReaction通常失効により、自動で次の自Activation終了まで実効SHOOTING・MELEEがLv1:+2、Lv2:+4、Lv3:+6。追加コマンドなし、累積なし。

### 新規・再設計された未確定候補

- **臨戦警戒 / Combat Vigilance（`certain-evasion`）**：WAITによるReaction AVAILABLEの間は、受ける適格な攻撃の最終命中率を下げる回避補正を付与。完全回避ではない、回避でReactionを自動消費しない。比較数値：Lv1＝floor(基礎AWARENESS/3)pt、Lv2＝floor(基礎AWARENESS×2/3)pt、Lv3＝基礎AWARENESS pt。攻撃種・実効Abilityとの関係、臨戦集中との二重取得時の相乗効果は未決。Lv補正値は正式決定でない。
- **Charlene / 愛用武器（`charlene-favorite-weapon`）**：選んだ1武器Definitionによる攻撃のAbilityのみ強化。比較数値：攻撃に使用する実効SHOOTINGまたはMELEE Lv1:+2、Lv2:+4、Lv3:+6。ほかの武器には適用せず、武器の選択方法・変更可否・数値は未確定。映画の愛銃にちなむ仮名。

### リリース範囲・保存互換

Skill Labは育成ポイントとスキル取得のシミュレーターであり、戦闘行動・武器指定・Reaction/Turn・確率計算は実行しない。表示カードの条件と効果は設計表示のみ。内部の旧スキルIDを保つことで既存JSON/ブラウザ保存ビルドを保護する。非公開本編Coreおよびマスター仕様書は更新していない。

## 2026-10-23 — Skill Lab v0.13 分類の再設計と公開

**確定済みの効果・候補の数値は変更なし。** 研究用スキル一覧32枚の主分類を、「強化対象」から**発動・成立条件**へ置き換えた。先頭は機体戦闘習熟3種とCharleneが属する「機体・武器固定」、次に時間経過、WAIT・Reaction、移動・静止、距離・布陣、天候・環境、姿勢・走査、攻撃・弾薬、被弾・HP、行動後・撃破とする（合計10分類）。旧「汎用」は廃止。

**別軸の制約・対価タグ**を32枚すべてに割り当て、各カードとプルダウン検索で閲覧できるようにした。タグは「機体固定」「武器固定」「発動待ち」「序盤限定」「WAIT」「Reaction温存」「Reaction使用」「静止」「移動条件」「孤立配置」「指定距離」「環境依存」「Main Action」「Signature増加」「射撃・露見」「追加弾薬」「低HP」「確率条件」等、実際の消費資源・機会費用・成立制約を示す。これらは同一ではないため、説明では区別し、コアで本来必要な行動コストを追加消費させる意味ではない。

- 「すべて」のカテゴリ別並び、カテゴリナビ、カテゴリ選択肢は共通の並び順。
- 初期は「すべて」を表示し、最初に機体・武器固定を提示する。
- 「確定スキルを見る」のトグルは新しい制約・対価フィルターも復元する。
- 32件、確定6件、その他26件。レベル・内部Skill ID・保存データ・各スキルの設計決定は不変。
- 本編Core／Godot／正式仕様書は未変更。ブラウザ内に戦闘シミュレーションは追加していない。

## 2026-10-23 — v0.14 レベル欄をサンプル値で表示（研究用UI）

- Lv1〜3の主要表示から複雑な計算式を外し、表示中の架空パイロットPHANTOM-01の基礎Ability（基準10＋恒久育成ポイント）で算出した**具体的な効果・確率・移動補正の残り**を見せる。Ability +/-操作時に全カードを再描画。
- 対象は臨戦警戒（基礎AWARENESS参照の回避率pt）、反射機動・見切り回避（REFLEX参照の発動率）、脚部制圧射撃（SHOOTING参照の確率）、移動射撃術（REFLEX参照の−10／−20武器の移動補正変化）。
- 初動警戒の終了Turn、戦況適応の発動Turnも計算式そのものではなく、サンプルのAWARENESSから算出した実数値で表示する。
- 各カードの「計算式・設計上の補足」展開欄に元の式や設計経緯を残す。レベル効果が単純固定値のカードはそのまま。
- 他のスキルの一時的なAbility補正、機体・武器・戦闘状況を含めた計算ではないので、**実際の戦場での最終結果を保証しない**。元仕様で実効Abilityを参照するスキルも、Skill Labプレビューでは表示パイロットの現在基礎Abilityを代用して計算する。
- 32スキル（確定6件）の定義と保存形式は変更しない。本編Coreや正式仕様書は未変更。

## 2026-10-23 — v0.15 本番Skill Lab反映結果

### 確定5種類の英語表記

- `Frame Combat Proficiency (Light)`／`Frame Combat Proficiency (Standard)`／`Frame Combat Proficiency (Heavy)`。機体の種類はコロンやカンマでなく末尾の括弧で表す。強化は当該機体に搭乗中の実効SHOOTING・MELEE＋1／2／3のみ。
- `First Watch`（旧初動警戒）：出撃時の基礎INSIGHTから有効終了Turn = max(1,floor(基礎INSIGHT÷2)) を一度決め、Turn1〜そのTurnまで実効INSIGHTとREFLEX＋1／2／3。**高INSIGHTほど持続が長い従来仕様のまま。**
- `Steady Nerves`（旧臨戦集中）：WAITで得たReactionを次自Faction Phase開始まで使わず通常失効した場合、次自Activation終了まで実効SHOOTING・MELEE＋2／4／6。効果・レベルは変更なし。
- 英語名は日本語UIでも英語のまま表示。日本語の発動条件・効果説明は残す。26件の未確定案は一括英語改名しない。

### INSIGHT表示・保存互換

- 表示・検索・式・スキル説明中の旧AWARENESSをINSIGHTへ。索敵に使う能力値であり、Core内部のPilot DetectionとFrame.Sensorは既存名のまま。
- 旧ローカル保存・旧JSONにある `abilityBonus.AWARENESS` / さらに古い `abilityBonus.SENSOR` を INSIGHT に自動移行。新書き出しは `abilityBonus.INSIGHT`。
- 技能のLv／発動条件の算式と他のスキル効果は名前以外変更しない。

### Quick Study（旧戦況適応）の取り下げ

以前の確定技能 `tactical-adaptation` を**現役31カードから除外**し、画面下部の展開可能な「Archived Skills」へ移動。旧式 `max(3, 20-基礎INSIGHT)` 以後Mission終了まで実効SHOOTING・MELEE +1/2/3 はもはや選択・適用されない。

理由：高INSIGHTほど機体制限なしの持続攻撃強化が非常に早く成立して、`Frame Combat Proficiency` と類似の効果をより少ない条件で与えやすい。First Watchの後半へ隙間なく接続する別式は、高INSIGHTほどQuick Studyが遅延するため不採用。

古いビルドで `tactical-adaptation` Lv1〜3 を取得済みなら、当該ランクを `retiredSkillLevels` へ歴史情報として移し、**育成ポイント使用量には算入せず実質全額返却**。Lvはアーカイブ欄と習得欄の注意書きに表示。JSON再保存も履歴を保持。育成配分のリセットは履歴を消去しない。

現在の確定は5件、検討中26件、アーカイブ1件。スキルIDの再割当なし。本編Coreや正式仕様書は更新しない。

## 2026-10-23 — v0.16 Stay Frosty 確定・反映

- 旧「臨戦警戒 / Combat Vigilance」の `certain-evasion` を名称 **Stay Frosty** に確定変更。安定Skill IDは維持し、古いビルドの取得Lvを失わない。日本語版でもスキル名は英語のみ。
- WAIT後の既存Reaction権がAVAILABLEの間、受ける適格攻撃の**攻撃側HitRawへ負の補正**を与える。直接回避率を加算したりREFLEXを上げたりしない。Lv1 `−floor(基礎INSIGHT/2)`、Lv2 `−floor(基礎INSIGHT×3/4)`、Lv3 `−基礎INSIGHT`。基礎INSIGHTは出撃時の恒久育成値を使用し、First Watch等の一時Ability強化で変化しない。
- 例 INSIGHT10→−5/−7/−10、15→−7/−11/−15、20→−10/−15/−20。Level表示はサンプル基礎INSIGHTを反映して自動更新、計算式は詳細欄へ。
- 補正適用順序：攻撃側命中・防御側REFLEX等を含むHitRaw → Stay Frostyの減算 → 0〜100%のHitChanceクランプ＆100超過HitRawをCritPenへ変換。敵味方共通。もともとHitRaw130、Lv3・基礎INSIGHT15ではHitRaw115、命中率100%のままでも超過命中加算が15→7.5ptに減る（CritPen対応攻撃の研究式）。
- 普通の単体Direct FIRE、MELEE、適格な誘導ミサイル着弾など回避判定がある攻撃に作用する方向。必中・Area・特異な命中プロファイル、多段Hit等は本編Coreを改修する前に仕様詳細を検証。UNKNOWN FIREに敵情報を表示しない。
- 攻撃をかわした／受けたことではReactionを消費しない。保持中は複数攻撃に適用。INTERCEPT／COVER／Missile InterceptにReactionを使用すると失効。敵Phaseをまたいで未使用だったらSteady Nervesと併用可。追加の専用回数管理やコマンドなし。
- 現役31件（確定6、検討中25）、Quick Studyはアーカイブ1件で不変。既存5確定スキルの効果・ポイント数も変更なし。公開ブラウザのSkill Labのみの更新で非公開Coreは未変更。超過命中値50%→CritPenの規則はIDEAS.mdの未実装研究案。

## 2026-10-23 — v0.17 Right on Cue / Got Your Six 正式反映

- **Right on Cue**（旧迎撃射撃術、ID `reaction-shooter`）：通常Reaction INTERCEPT射撃とMissile Interceptの双方で実効SHOOTING+2/+4/+6を確定。通常単体INTERCEPTはHitRaw+6/+12/+18、ミサイル迎撃はHitRaw+4/+8/+12。通常のMain Action射撃には適用しない。Missile InterceptにCritPenはない。Reaction消費、合法武器・弾薬・LOS等は既存どおり。英語名は、敵の行動を予期して待っていたところ予想どおり動いた、という意味。
- **Got Your Six**（旧護衛反応、ID `guardian-reaction`）：別の味方Friendly Unitを守るCOVERまたは味方へ向かうミサイルのMissile Interceptに限り、実効REFLEX+3/+6/+9。COVERは隣接1Hexの味方に対する単体Direct FIRE／単体MELEE／単体誘導Missileの攻撃全体をReaction消費で自機が引き受ける。通常のCOVER命中係数3で敵HitRaw−9/−18/−27、味方へのミサイル迎撃は係数2で迎撃HitRaw+6/+12/+18。自身へのCOVERや自己Missile Interceptは対象外。範囲・Hex・方向指定、Reaction由来攻撃はCOVERできない。
- 元の物理Option Defensive Response Suiteは本編Coreに残存。技能研究確定はOption削除や重複バフの自動許可ではない。統合方法は将来の仕様決定事項。
- 現行31スキル、確定8、研究中23、Quick Studyアーカイブ1。Skill ID、育成ポイント、ローカル保存/JSON互換、他のスキル効果は変更なし。private Coreには触れていない。

## 2026-10-23 — v0.18 Stay Frostyを実効REFLEX上昇へ改訂

- **Stay Frosty（ID `certain-evasion`）**：旧版v0.16／v0.17の「敵HitRaw −floor(INSIGHT×50%/75%/100%)」は**撤回・置換**。Reactionを保持している間に**実効REFLEXを加算する**。Lv1 `+ceil(出撃時の基礎INSIGHT/6)`、Lv2 `+ceil(出撃時の基礎INSIGHT/4)`、Lv3 `+ceil(出撃時の基礎INSIGHT/3)`。
- 例：基礎INSIGHT10→REFLEX +2/+3/+4、15→+3/+4/+5、18→+3/+5/+6、20→+4/+5/+7。Skill LabのLv欄は具体値を表示し、サンプルのINSIGHT育成で再計算。計算式は折りたたみ詳細欄に記載。
- **「被攻撃時のみ」の独自制約は設けない**。通常の実効REFLEXを参照する適格判定に適用し、通常単体FIRE／MELEEでREFLEX+1ごとに敵HitRaw−3、Missile InterceptでREFLEX+1ごとに命中値+2、誘導ミサイルの着弾防御でも対応するREFLEXを参照する。命中値→命中率クランプ→100%超過分のCritical Penetrationという共通順序は変えず、専用の直接命中値補正は廃止。
- 通常Reactionを使用して開始したCOVER／INTERCEPT／Missile Interceptは**行動開始時にReactionがAVAILABLEだった事実でStay Frostyの適格性を決め、その行動の解決まではREFLEX上昇を適用**。行動後は通常のReaction消費により効果終了。この順序で実装時の消費タイミングによる消滅を避ける。
- 基礎INSIGHTは出撃時の永続成長込み・一時バフなしの固定値。First Watch自身の一時INSIGHT増加ではStay Frostyの加算量を増やさない。未使用ReactionならSteady Nervesと別途組み合わせ可能。
- この改訂によって確定件数は変化しない：31現役・8確定・23候補、Quick Studyはアーカイブ1。元のOption DRSは本編Coreに残存し、併用／廃止は未決。Skill ID・保存JSONの互換も維持。本編Core未変更。

## 2026-10-26 — Against the Odds（名称確定／数値は研究基準値）

- 新規スキル `against-the-odds` / **Against the Odds** をSkill Labに追加。武器を問わない精神的・戦闘感覚の技能名として英語名は確定。総32候補、**設計確定8・検討中24**、Archived Quick Study 1。独立のSkill Lab v0.19に反映。
- **適用対象：** 射撃と白兵の両方。ただし既存の武器定義で **CritPen YES**、通常貫通後 `EffectiveArmor > 0`、かつ命中したHitに限る。射撃のSHOOTING、白兵のMELEEを既存CritPen基礎式に用いる。スキル自体は命中率やPowerを変更せず、新コマンド／MP／使用回数／Reactionを追加しない。
- **研究式（Lv係数と上限はまだ正式確定ではない）：** `H=clamp(floor(HitRaw),0,100)`, `BaseCritPen=max(2,4+0.5*(実効SHOOTINGまたはMELEE−10))`, `C0=min(100,BaseCritPen+0.5*max(0,floor(HitRaw)−100))`; `BonusRaw=min(10*Lv,60*Lv*((100−H)/100)^2)`; `Bonus=floor(BonusRaw*2)/2`（0.5ポイント切捨て）；`FinalCritPen=min(100,C0+Bonus)`。
- **命中率70%：** Lv1/2/3追加CritPen +5/+10.5/+16pt、基礎CritPen 4%の例では命中時9/14.5/20%。**命中率60%：** 追加 +9.5/+19/+28.5pt、同例では13.5/23/32.5%。高命中時は小さく、60〜70%程度から目立つ二乗型。数値自体は敵Armor・REFLEX・他Skillとの比較を続ける。
- **複数Hitのルールを変えない：** 通常Direct FIREのShots 2/3などはHit判定ごと、CritPenはAttackにつき最大1回・成功した該当Hitだけ装甲無視。Combat KnifeのAreaMeleeは各対象を独立Melee Attackとして扱う。現行白兵でCritPen YESはCombat Knifeだけ。BASH／Assault Lance／Explosive Axeを勝手にCritPen対応へ変更しない。誘導ミサイル／Missile Intercept／現行CritPen NO範囲攻撃にも付与しない。
- **ゲームデザイン意図：** 70%台の心許ない命中率でも、一発の装甲突破が狙える攻撃専門化。高SHOOTINGの人物が追加命中系Skillを取らずに索敵・回避等を育てる選択、平均的な攻撃Abilityで重装甲を狙う選択、SMG/GPMGの多段Hitと1回CritPenの関係を評価する。低命中率の原因にかかわらず効果が増える抽象表現であり、移動でわざと命中率を下げると対重装甲の期待ダメージが上がる場合があることも設計上許容する。
- **位置付け：** 名前とスキル候補登録は決定。係数60×Lv・追加上限10×Lvは現時点の研究基準値（バランス評価で調整可能）。本編CORE正式スキルへの移管、ゲーム実装は未実施。

## 2026-10-26 — 二丁同時射撃（仮） / paired-fire — Skill Lab v0.20

- **候補ID：** `paired-fire`。英語名・最終名称は未決定。現役33件（確定8、検討中25）＋Quick StudyはArchivedのまま。既存の`double-tap`（1丁の追加弾薬による射撃回数追加候補）とは別技能。新しいMain Actionや専用発動コマンドは追加しない。
- **運用案：** 同一Weapon Definitionの通常`UnitTargetedDirectFire`武器を2丁装備して、いずれかを選んだ通常FIRE時に自動で双方が発砲。1 Main Actionから同一対象への独立した2 Attackを生成する（別WeaponRuntimeState、個別のHitAttemptCountとAmmoCostPerAttackを使用）。双方が発砲可能な必要あり。途中撃破時は後続Hitをスキップして別敵へ自動転射しない。
- **研究値（未確定）：** Lv1は各武器のHitRaw −40pt、Lv2 −30pt、Lv3 −20pt。移動・地形Cover・敵REFLEX等の既存補正とは別に反映し、各HitChanceを既存の0〜100%へ制限。SHOOTING10対REFLEX10、ほかの補正なしではSMG/Assault Rifleの命中率55/65/75%、Shotgun65/75/85%。Skill Labはサンプルの基礎SHOOTING配分に追従してこの例を表示する。
- **現行Core上の装備コスト：** SMG×2、Assault Rifle×2、Shotgun×2はArmament Capacity合計2（Light/Standard/Heavy可）。GPMG-6×2、Sniper Rifle×2は合計4（Heavyのみ）。同一武器の重複装備は既存COREの許可済み規則。装弾数は武器ごとに独立。
- **複数Hitと弾：** SMG×2は各3Hit判定・弾3+3発、GPMG-6×2は各2Hit判定・弾2+2発。Shotgun、Assault Rifle、Sniper Rifleなど単発銃×2は各1Hit判定・弾1+1発。両武器のMagazineやRELOADは別々に管理する。
- **CritPen：** CritPen YESの2武器は独立したAttackとして各最大1回のCritical Penetration機会を持つ（成功時にはそれぞれ該当する1Hitだけ装甲無視）。SMG/GPMG-6の1丁の複数HitにCritPen判定を2回・3回付与することはない。CritPen NOのShotgun等にはCritPenを新規付与しない。Against the Oddsとの併用候補だがLv3同士なら計6Pを要する。
- **決定していない詳細：** 片方の銃が弾不足やRELOAD待ちの場合に単独FIREへフォールバックするか。通常INTERCEPTにも適用するか（現在は通常Main ActionのFIREを検討）。COVER／行動露見／Signature／Reactionの単位と厳密な処理順序。高SHOOTINGでのLv1取得とLight Shotgun2丁、Heavy Sniper Rifle2丁などのビルド比較。これらは実装前に明示的に決める。
- **責務境界：** 今回は独立Skill Labへの追加のみ。本編COREの個別Skill仕様には移管しない。計算表示はモデル例であり実際の戦闘をシミュレートしない。保存済みビルドのSkill IDやローカル保存JSONを破壊しない。


## 2026-10-26 — First Watchは再検討へ

- First Watch（`early-starter`）の確定表示を解除。旧INSIGHT/REFLEX +1/+2/+3とINSIGHT依存の持続式は仮値として保持し、廃案・アーカイブにはしない。無条件の序盤強化が戦術判断を十分に変えるか検証する。
- 現役33件・確定7件・検討中26件。Skill IDおよび既存のビルドは維持。本編Coreには移管していない。
- 次の候補は機動回避（`mobile-evasion`）：3Hex以上の自MOVE後に実効REFLEX +2/+4/+6という仮値を、発動しやすさと既存MASとの差を中心に再検討する。

## 2026-10-26 — v0.22 名称・効果決定の一括反映

現役33件、Skill Lab内確定9件、未確定・保留24件。過去の決定ログで古いスキル件数や旧称が残っている場合、現在の状態はこの最新節を優先する。今回の変更は独立Skill Labに限定し、private Coreや本編正式個別Skill仕様には移管しない。

### Plant Your Feet（旧：精密射撃、ID `marksmanship`）— Skill Lab設計確定

- 英語名 **Plant Your Feet**、Lv1/2/3の実効SHOOTING **+2/+4/+6** を確定。
- 自分の通常MOVEより前に、適格な通常の対Unit Direct FIREを行うと自動適用。通常の命中計算ではHitRaw +6/+12/+18。適格なCritical Penetrationも実効SHOOTINGと超過命中値から計算する。通常の武器・Track・射程・Direct-Fire LOS制約は維持。
- MSU（Standard/Heavy）で射撃後に未使用の通常MOVEを実行しても、射撃へ遡ってペナルティを適用しない。ただし射撃後の露見や敵INTERCEPTを先に解決する。Light DISPLACEも同じく後の移動であり、発砲前に移動できたことにはならない。
- 通常Main ActionのUnit-targeted FIREを確定対象とし、Reaction INTERCEPT・特殊攻撃への適用拡張は未決。元のFCS Optionの削除や重複は別途整理。

### Keep Moving（旧：機動回避、ID `mobile-evasion`）— Skill Lab設計確定

- 英語名 **Keep Moving**、Lv1/2/3の実効REFLEX **+2/+4/+6** を確定。
- 自己の通常MOVEで実際に3Hex以上成功進入した時点から、次の自軍Faction Phase開始まで効果が継続。経路予約・Movement Cost合計で判定しない。途中HALT等で3Hexに届かなければ不発。REPOSITION・Light DISPLACEはカウントしない。
- 通常射撃・白兵で敵の命中値を−6/−12/−18pt。誘導ミサイル着弾や適格なMissile Interceptでも実効REFLEXとして評価し、迎撃命中値は+4/+8/+12pt。REFLEX値を参照する全ての適格判定で元の式を尊重する。
- 移動後の武器固有命中補正、敵からの露見・Reactionなど、既存MOVEの帰結は残る。元MAS Optionの廃止・併用は未決。

### 保留・再検討

- First Watch（`early-starter`）はv0.21から再検討状態を継続。旧値を研究資料として保持。
- 定点観測（`observation-discipline`）は**保留・再設計待ち**。旧「移動せずActivation完了でINSIGHT+4/+8/+12」は実用場面が限定的。代替「MOVE後WAIT」「WAITだけ」は、攻撃できない時のWAITに索敵をほぼ無償で加えるため採用しない。Reactionを取り上げるような複雑な条件も作らない。現行のカードは旧研究数値を残すだけで、確定扱いではない。
- 追加ルールや未決の数値をまとめて無断で確定させない。本編コードは別工程。


## 2026-10-26 — v0.23 WAIT・Reactionの3件を再検討へ

ユーザーの指示により、WAIT・Reaction分類の4件のうち **Got Your Six以外の3件はSkill Labの確定扱いを解除**する。

- Right on Cue（`reaction-shooter`）：**再検討**
- Steady Nerves（`burst-focus`）：**再検討**
- Stay Frosty（`certain-evasion`）：**再検討**
- Got Your Six（`guardian-reaction`）：**確定維持**

変更は現在の研究上の**確定ステータスだけ**。3件のLv1～3、発動条件、説明、Ability計算参考値は削除・変更せず、過去の比較用仮案として残す。廃案やArchivedへ移す判断ではない。過去の「確定」の記録は当時の研究履歴であって、現状の確定状況を意味しない。

First Watchの再検討、定点観測の保留も継続。現役33件中**確定6件、未確定・保留27件**。確定はFrame Combat Proficiency 3件、Plant Your Feet、Keep Moving、Got Your Sixの6件。スキルID・ローカル保存・ビルドのJSON形式は保持。本編COREおよび既存Optionには変更を加えない。

## 2026-10-27 — v0.24 On the Charge / Hunker Down / Fired Up / Go Dark

ユーザーとのゲームデザイン検討をSkill Labにまとめて反映。**現役34件（確定10件・再検討／保留24件）**、Quick Studyアーカイブ1件。既存のSkill ID、localStorage `fd-skill-lab-v1`、保存ビルド、既存34件中元33件のレベル選択互換性を維持。本編 private Coreのゲームロジック・既存Optionは変更しない。ここでの「確定」は**Skill Labの設計研究上**の暫定採用で、コード実装済みを意味しない。

### On the Charge（旧助走白兵、ID `momentum-melee`）— 確定

- 自Activation中に自分の通常MOVEで**実際に3Hex以上進入成功**したあと、同じActivationで適格なMELEE攻撃を行う際の**実効MELEE +2/+4/+6**（Lv1/2/3）。通常の命中値なら+6/+12/+18pt。Combat KnifeなどCritPen YES武器では実効MELEE・HitRaw超過命中も通常どおり参照。
- 予定経路やMovement Cost 3では条件を満たさない。REPOSITION・Light DISPLACEでは進入カウントを増やさない。白兵攻撃と前進の危険を引き受ける。
- 元CCAS Optionの廃止や重複有無は未決定。

### Hunker Down（旧防御姿勢術、ID `brace-discipline`）— 確定

- BRACEのArmor +2を、Lv1/2/3に応じて**追加Armor +1/+2/+3**で合計**+3/+4/+5**に強化。
- さらに、BRACEが有効な間、通常の装甲・Penetration・最低保証ダメージ処理を行った結果が**ちょうど1ダメージのHitのみ、最終HPダメージを0へ置換**する。複数Hit武器にはHit単位で適用。命中の事実は消えないのでFired Upは発動できる。
- 通常BRACEの寿命とMain Actionコストを変えない。強力な貫通攻撃、CritPenなどの反撃対策がある。元ARS Optionとの併用・置換は未決。通常の最小ダメージ1ルールの例外は本編Coreへまだ実装していない。

### Fired Up（新規ID `fired-up`）— 確定

- 相手からの**Attackに1回以上Hitされたら**、最終HPダメージが0でも発動準備。**次の自Activation**に限り、Lv1/2/3で**SHOOTING・MELEE +6/+9/+12**。
- **完全非累積の二値条件**：敵のAttackが2回・3回命中しても上昇幅は変わらない。同じAttackの多段Hitも1Attackとみなす。次の自Activationが完了すると失効。
- 一般的な命中式HitRaw+18/+27/+36、CritPen YES武器なら実効Abilityと超過命中値にも反映する。MISSのみなら発動しない。自Activation中の敵INTERCEPT Hitも、その自Activationに遡及させず**次の**自Activationに回す。特殊な命中判定なしArea攻撃などは本編Coreに移管する段階で発動対象を要整理。
- Hunker Downと組み合わせれば、BRACEで敵のHitを装甲で受け、0ダメージでも次の自Activationの反撃にボーナスを得る。狙って被弾する難しさがあり、強化は1回分のActivationに限る。

### Go Dark（旧隠密動作、ID `conceal-discipline`）— 基本方針確定、Lv数値は暫定

- CONCEAL中の低Signatureと引き換えに**自機センサーによるDetectionおよびLocal Trackを完全停止**。Detection Powerを単に0にするだけでは正Signatureの目標を検出できてしまうので、センサー観測源を無効化する設計。隣接Proximityなど別の情報源は維持。
- 他味方からのDatalink Track受信は**可能**。通信妨害や別観測者の情報喪失に依存する。敵フェーズ中に周辺で敵が移動しても気づかず、次の自軍Faction Phase開始でセンサーが戻り、突然敵を多数発見し得る。
- 通常CONCEALの主行動消費と次の自軍Faction Phase開始で失効するルールを維持。潜伏状態を維持したまま次の自軍ターンにMOVEするような例外は設けない。
- Lv1/2/3の**CONCEALによるSignature合計−2/−3/−4**は比較用の**暫定値であり、未だ数値確定ではない**。名前と技能の軸は確定。元SRS Optionの重複・置換は未決。

### 確定数と未決事項

確定10件＝Frame Combat Proficiency（Light/Standard/Heavy）3件、Plant Your Feet、Keep Moving、On the Charge、Got Your Six、Hunker Down、Go Dark（Signature数値仮）、Fired Up。今回名称未確定だった戦闘適応はFired Upという名前になった。以前確定を解除したFirst Watch、Right on Cue、Steady Nerves、Stay Frostyは引き続き再検討、定点観測は保留。Against the Oddsは名称のみ確定で計算係数は未確定。二丁同時射撃も研究段階。いずれも今回勝手に確定数へ加算しない。

旧版の記録は履歴であり、現在のstatusは本項とSkill Labのカード表示を優先する。数値未確定の効果を正式戦闘仕様や実装指示として流用しない。

## 2026-10-27 — v0.25 Keep Watch / Sweep the Sectorを確定

Skill Labで以下2件の**名称・Lv1～3・発動タイミング**を確定扱いへ変更。現在は現役34件（確定12、再検討・保留22）、Quick Studyアーカイブ1件。既存Skill IDとlocalStorage保存形式は不変。すべてSkill Lab内の育成設計判断であり、private本編Coreおよび既存Optionには変更を加えない。

### Keep Watch（旧定点観測、ID `observation-discipline`）

- **通常MOVEをせずに自Activationを完全に終了した直後**から実効INSIGHT **+4/+8/+12**（Lv1/2/3）。内部Pilot DetectionとしてDetection Powerに1:1加算され、基本索敵予算は**+1/+2/+3**。地形コスト、敵Signature、天候、遮蔽物・煙、Datalink制限などはそのまま。
- 効果を得るために終了させたMain Action（FIRE、ACTIVE SCAN等）には遡及しない。終了時の通常索敵再評価で新しい合法なLocal Trackが成立すれば味方へ共有可能。該当範囲に敵を見つけられなかった情報も価値がある。
- **次の自Activationを開始するまで維持**。自Faction Phaseが切り替わっただけでは失効しない。主に行動順の前後調整、右翼・左翼・前線の警戒、Plant Your Feetとの併用で専門化を形成する。
- Light DISPLACEは通常MOVE扱いでないため資格を妨げない。MSUで行動後に通常MOVEすると発動条件を失う。元のSensor Stabilizer Optionは本編に現存し、併用/置換は未決。

### Sweep the Sector（旧能動走査術、ID `scan-interpretation`）

- ACTIVE SCANの**瞬間的Detection計算時だけ**実効INSIGHT **+4/+8/+12**（Lv1/2/3）。標準のACTIVE SCANのDetection Power +12は残るので、技能だけを加えた瞬間的な増加総量は**+16/+20/+24**（別Option等は別途未決）。
- ACTIVE SCANの主行動消費、scanner Signature +2、敵への露見・Action INTERCEPTの可能性、情報再評価や地形/Smokeの制約は維持。Skill効果はACTIVE SCAN終了後の継続観測には残らない。
- 同一パイロットがKeep Watchと両方を持ち、通常MOVEせずACTIVE SCANした場合、走査中はSweep the Sector、**Activation完了後に**Keep Watchが発動する。技能ボーナスが同一瞬間のACTIVE SCANに二重加算されるわけではない。結果として「一時的な広域走査→狭めの継続観測」が成立する。
- 元のActive Scan Amplifier Optionは本編に残存。技能化・装備とのスタックは未決。

### v0.25時点の整理

Skill Lab確定12件：Frame Combat Proficiency（Light/Standard/Heavy）、Plant Your Feet、Keep Moving、On the Charge、Got Your Six、Hunker Down、Go Dark（Signature値は暫定）、Fired Up、Keep Watch、Sweep the Sector。

First Watch／Right on Cue／Steady Nerves／Stay Frostyの確定解除は継続。Against the Oddsの数値、二丁同時射撃の詳細も未確定。過去の「定点観測は保留」「能動走査術は要検討」の記載は履歴であり、本節が最新決定として優先する。

## 2026-10-27 — v0.26 On Your Own（旧・単独行動）を設計確定

現役34件、**Skill Lab確定13件・未確定21件**。旧版で提案した「SHOOTINGとREFLEXを両方強化」は採用せず、ユーザーとの検討に沿って**高INSIGHTによる孤立時のSHOOTING強化だけ**に変更する。元ID `solo-operator`、分類 `距離・布陣`、origin `IDEAS` は維持。

- 英語名 **On Your Own**。
- 発動条件：本人の**幾何学的Hex距離4以内にほかの味方Unitが1機もいない間**。5Hex以上離れていれば有効。敵より前方・敵への最短距離・前衛であること等の追加条件は設けない。本人の移動だけでなく味方の移動でも条件を満たせる。味方の近距離COVERなどを受けられないことが弱点。
- 効果：出撃時の**基礎INSIGHT（恒久育成込み）に応じてSHOOTINGが増加**。採用するSkill Lab計算式は `1 + floor(基礎INSIGHT × SkillLevel / 6)`。INSIGHT10ならLv1/2/3でSHOOTING+2/+4/+6、14なら+3/+5/+8、18なら+4/+7/+10。一時的なINSIGHT上昇では計算式を変えず、スキルシミュレーターのサンプルパイロットで恒久INSIGHTを変更した場合はLv別表示が自動更新される。
- REFLEX・MELEE・INSIGHTには補正なし。実効SHOOTINGを参照する適格な命中計算・CritPenへ適用。武器Range・LOS・Track制約は解除しない。Datalink受信は通常ルールどおり可能。
- 前進した高INSIGHTの単独偵察／遊撃手、主力が前進した後に孤立して長射程FIREするHeavy、Go Darkで敵フェーズをしのいで次に撃つ潜伏射手などのビルドに使える。ただし立ち回りが上手くいかなければ低REFLEXの孤立機は撃破されやすい。
- 他の確定スキルとの併用ではPlant Your Feetによる静止射撃、Keep Watchによる翼側・前線観測等が有望。純粋な常時Abilityボーナスではなく、陣形と行動順に依存することを重視。
- 今回の確定は独立Skill Labの設計研究ステータスの変更。本編CORE・既存Option・出撃ロースターは変更しない。古いLv値や確定数の記録は歴史的メモとして保持。

## 2026-10-27 — v0.27 Pick Your Ground（地形活用スキル）を設計確定

新規Skill `pick-your-ground` を追加。名称 **Pick Your Ground**、分類 **地形・陣地**、由来 **新規アイデア**、研究status **確定**。現役35件（確定14・未確定21）＋Quick Studyアーカイブ1件。既存スキルID・習得状態・保存形式は維持。本編Coreは未変更。

- **発動条件：** 自機のいるHexに、実際に敵HitRawを下げる負の地形・陣地CoverHitModifierが存在する間。森林、瓦礫、掩体が例。地形防御0の平地・道路・通常岩場・浅瀬はSkillだけで命中ペナルティを新設しない。
- **効果：** Lv1/2/3で既存Coverに追加**−5/−10/−15 HitRawポイント**（回避率の乗算ではない）。森林・瓦礫は標準−10→−15/−20/−25、掩体は標準−15→−20/−25/−30。基本REFLEX・他Ability・Armor・Signatureは上げない。
- **最強のみ：** 現行Core同様、地形と掩体は重複加算しない。先に `min(地形Cover, 陣地Cover)` で最強の既存遮蔽を選び、それが負なら `−5×Lv` を**一回だけ**上乗せする。森林＋掩体で二重にSkill適用しない。
- **適用範囲：** 既存の地形・陣地Coverに対応する対Unit通常射撃と誘導ミサイル。地形Cover非適用の白兵、範囲・Hex攻撃には適用しない。味方を庇うCOVER Reactionの強化でもない。
- **機会費用：** 適切な地形を選ぶ必要がある。森林・瓦礫の移動コストや射程・LOS・索敵経路、進軍方向と競合する。Keep Moving、Plant Your Feet、Keep Watch、On Your Ownとビルドを組めるが、各技能の発動条件は独立。
- Skill Lab内の研究・取得シミュレーションに反映。実際の地形と敵命中を逐次シミュレートする戦場UIは追加していない。数値・対象を含めて今回の技能案として確定表示するが、実戦バランス検証とCore実装は別工程。

同日のv0.26ではOn Your Ownを確定した。既存13確定スキルの内容は維持し、今回Pick Your Groundを1件追加した。

## 2026-10-29 — v0.28 全確定スキルのMTG由来名称への改名

ユーザーの指示により、**Skill Labの確定済み14件すべて**を実在するMTGカード名へ改名する。機体適性3種は同じカード名 **Tempered Steel** を共通に使用するため、12種類の元カード名を採用した。元カードの効果とPilot Skillの効果を揃えることは命名の条件としない。英語名の語感、作品世界との親和性、14件を並べた際の統一感を優先する。

| 旧名称 | 現行名称 | 安定ID |
| --- | --- | --- |
| Frame Combat Proficiency (Light) | **Tempered Steel (Light)** | `frame-light` |
| Frame Combat Proficiency (Standard) | **Tempered Steel (Standard)** | `frame-standard` |
| Frame Combat Proficiency (Heavy) | **Tempered Steel (Heavy)** | `frame-heavy` |
| Plant Your Feet | **Last Word** | `marksmanship` |
| Keep Moving | **Escape Velocity** | `mobile-evasion` |
| On the Charge | **Through the Breach** | `momentum-melee` |
| Got Your Six | **No One Left Behind** | `guardian-reaction` |
| Hunker Down | **Built to Last** | `brace-discipline` |
| Go Dark | **Moment of Silence** | `conceal-discipline` |
| Fired Up | **Repercussion** | `fired-up` |
| Keep Watch | **Standstill** | `observation-discipline` |
| Sweep the Sector | **See Beyond** | `scan-interpretation` |
| On Your Own | **Against All Odds** | `solo-operator` |
| Pick Your Ground | **Dead of Winter** | `pick-your-ground` |

元カードへのリンクとその**実際のカード効果の要約**は [MTG_SKILL_NAMES.md](MTG_SKILL_NAMES.md) に記録。

- **名前のみ変更**。Lv1～3の効果・発動条件・数値・確定/検討中ステータス・内部Skill IDはすべて維持。Go Dark（新名 Moment of Silence）のSignature値が暫定であることも変わらない。Skill Lab現役35件、確定14件、未確定21件。
- 保存キー `fd-skill-lab-v1` とSkill IDを変えないため、既存のビルド保存、JSONエクスポート/インポート、育成ポイント配分は維持。**本編Coreには未反映**。
- Skill Lab本体の各カード名と現在の説明文・計算欄・関連Optionメモの呼称を更新。ここより前の設計履歴は**当時の名前を保存**し、過去の判断を書き換えない。
- 研究中（効果未確定）の `against-the-odds` は既に **Against the Odds** という表示名を持つため、確定技能の新名 **Against All Odds** と酷似する。今回それを理由に承認済の14件を差し替えたり、研究中の別技能を無断改名したりしない。今後の命名整理で優先的に検討。
- 今回の名前は現在の採用名だが、将来追加する技能との兼ね合いで**一括再割当・改名は可能**。それは効果設計の変更を意味しない。

## 2026-10-29 — v0.29 静止射撃スキルの名称差し替え

確定済みの静止射撃技能 `marksmanship`（元の名前 Plant Your Feet、v0.28時点の名前 Last Word）を **Iron Verdict** に変更した。元ネタはMTG「カルドハイム」の同名カード。タップ状態のクリーチャーに5点ダメージを与え、予顕を持つ。

**Last Word は現在未割当。** WAIT/Reaction技能への将来的な割り当てが考えられるが、どの技能に割り振るか、そもそも割り振るかは未確定。今回はWAIT/Reaction技能の名称や確定状態を変更していない。

改名のみ。効果（通常MOVE前のUnit対象Direct FIREでSHOOTING +2/+4/+6）、発動条件、Lv値、ID、取得情報、保存形式、他技能名、Skill Lab内の現役35件・確定14件、Coreへの非移植という扱いはすべて維持。以前の意思決定記録は履歴として残す。

## 2026-10-29 — v0.30 Fault Line / Survival Cache の新規確定追加

現役35件・確定14件のv0.29に続き、**新たに2件の設計確定スキル**を追加。現役37件（確定16、未確定21）、Quick Studyアーカイブ1件。両方ともパイロット技能としての研究仕様であり、独立したSkill Labの育成配分UIに登録する。本編Coreの武器計算・Armor永続状態・Repair Kitは変更しない。

### Fault Line — `fault-line`

- **名称**：実在MTGカード *Fault Line*。元カードは飛行しない全クリーチャーと全プレイヤーへのX点ダメージ。名称は装甲亀裂・戦線の綻びをイメージするため採用。カードの効果はゲームへ流用しない。
- **発動**：敵Unitへの適格な射撃または白兵AttackでCritical Penetrationが成功したHit。追加の確率判定はない。既存のCritical Penetration資格・判定回数を維持（同一Attackにつき最大1回、通常PenetrationでArmorが完全に抜けた場合はCritPen判定をしない）。
- **Lv1/2/3**：対象UnitのArmorを **−2/−4/−6**。装甲値の下限0。同一対象への複数回成功は**累積しない**（適用できる最大低下量のみ保持）。
- **順序**：まずCritPen成功HitのArmor無視ダメージを通常どおり解決。**そのHitが終わった直後**、まだ生存する対象へArmor低下。SMGなど同一Attackの後続Hitは低下後のArmorを参照し、先行Hitのダメージを遡及して変えない。
- **複数Hit**：同一AttackでCritPen抽選は1回のみ。SMGの1Hit目成功後は残り2HitへArmor低下が効く。対象が途中で撃破されれば残余Hitは既存ルールどおりスキップ。Combat KnifeのAreaMeleeは対象ごと独立Melee Attackとして判定する。
- **対象武器**：CritPen YESであれば射撃・白兵とも対象。Combat Knifeは対象となるが、現行のAssault Lance／Explosive AxeはCritPen NOのため対象外。ミサイルや通常貫通だけを理由に発動させない。専用AIM属性、追加アクション、弾薬、RNG、使用回数制限は設けない。
- **持続**：ミッション終了または対象撃破まで。後続の味方もArmor低下を利用できる。単独で重火器の火力を上回る必要はなく、低Penetration武器の連携・価値を広げることが目的。
- **数値確認例**：Armor12／SMG Power7・Pen2の3Hitが全命中し、最初のHitでCritPen成功した場合、Lv3で7+3+3=13（Skillなしなら7+1+1=9）。比較値であり、命中率・敵HP・反応行動は固定の想定。

### Survival Cache — `survival-cache`

- **名称**：MTG *Survival Cache*（ライフを回復し、条件付きでドロー、反復を持つカード）。限られた資材の有効活用という名前の意味を重視。
- **発動条件**：Repair Kit物理Optionを装備したパイロットが、合法な通常REPAIRを実行するとき自動適用。
- **Lv1/2/3**：通常Repair Kitの8HP回復に+4/+8/+12を加える。すなわち **12/16/20HP／回**。
- **原仕様維持**：2チャージ／ミッション、Main Action消費、修理対象は自機または隣接する生存中の同Faction味方Frame。最大HPを超えない、HP0／Destroyedは修理不能。射程・チャージ・装備枠・行動回数を増やさない。
- **実修理量**：`min(8+4×Lv, MaxHP−現在HP)`。回復量の余剰は別対象へ持ち越さず、ミッション終了までのKit残チャージの扱いも通常と同じ。修理量だけを強化し、物理Kit自体は残す。
- **実用性**：Repair Kitの装備枠と2チャージ、Main Action機会、前線の位置取りが必要。専門修理パイロットの育成と部隊編成の選択肢を増やす。

### Skill Lab・互換性・正式仕様との境界

- 追加したIDは `fault-line` と `survival-cache`。旧35件の内部ID・名称・効果・ランク・取得状態・カテゴリー・ステータスには一切変更なし。
- Skill Lab画面のLvカード・分類・確定フィルタ・サンプル計算説明に反映。Skill Labは**戦闘シミュレーターではなく育成ポイント配分と技能効果の比較用**であり、装甲破壊の実戦判定や修理実行を直接再現しない。
- 既存ビルドJSONとlocalStorageキー `fd-skill-lab-v1` を維持。旧ビルドの新規2Skillは未取得Lv0として読み込まれる。育成ポイント消費は従来どおり1ランク1P。
- 以前の設計履歴は当時の名前・状態として保持。これら2件はバランス再調整を許容するが、現時点では**設計確定**として扱う。
