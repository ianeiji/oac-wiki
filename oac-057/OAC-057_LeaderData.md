# OAC/指導者（0.57、XMLから生成）

- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）
- 生成元: `Civilizations/CIV4LeaderHeadInfos.xml`
- 読み方: 主要な項目は日本語ラベル付きで先頭に、それ以外の既定値でない設定は「その他の設定」にXMLのタグ名のまま列挙する。値の内部名は日本語名に置き換えている。Pythonで実装された効果はXMLにないため含まない（ゲーム内ヘルプの説明文があれば載せている）。

### Random Good Leader - ランダム（善良限定）

- 内部名: `LEADER_RANDOM_GOOD`
- 属性: 善良
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_GOOD

### Random Neutral Leader - ランダム（中立限定）

- 内部名: `LEADER_RANDOM_NEUTRAL`
- 属性: 中立
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_NEUTRAL

### Random Evil Leader - ランダム（邪悪限定）

- 内部名: `LEADER_RANDOM_EVIL`
- 属性: 邪悪
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_EVIL

### (Vanilla Leader) - （ヴァニラの指導者）

- 内部名: `LEADER_RANDOM_VANILLA`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_VANILLA

### TXT_KEY_LEADER_RANDOM_MALE - TXT_KEY_LEADER_RANDOM_MALE

- 内部名: `LEADER_RANDOM_MALE`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_MALE

### (Female Leader) - （女性の指導者）

- 内部名: `LEADER_RANDOM_FEMALE`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_FEMALE

### (Dwarven Leader) - （ドワーフ指導者）

- 内部名: `LEADER_RANDOM_DWARF`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_DWARF

### (Elvish Leader) - （エルフ指導者）

- 内部名: `LEADER_RANDOM_ELF`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_ELF

### TXT_KEY_LEADER_RANDOM_WINTERBORN - TXT_KEY_LEADER_RANDOM_WINTERBORN

- 内部名: `LEADER_RANDOM_WINTERBORN`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_WINTERBORN

### TXT_KEY_LEADER_RANDOM_LIZARDMAN - TXT_KEY_LEADER_RANDOM_LIZARDMAN

- 内部名: `LEADER_RANDOM_LIZARDMAN`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_LIZARDMAN

### (No Alive Leader) - （無生物指導者）

- 内部名: `LEADER_RANDOM_NO_ALIVE`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_NO_ALIVE

### TXT_KEY_LEADER_RANDOM_AGGRESSIVE - TXT_KEY_LEADER_RANDOM_AGGRESSIVE

- 内部名: `LEADER_RANDOM_AGGRESSIVE`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_AGGRESSIVE

### TXT_KEY_LEADER_RANDOM_SPIRITUAL - TXT_KEY_LEADER_RANDOM_SPIRITUAL

- 内部名: `LEADER_RANDOM_SPIRITUAL`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_SPIRITUAL

### TXT_KEY_LEADER_RANDOM_INDUSTRIOUS - TXT_KEY_LEADER_RANDOM_INDUSTRIOUS

- 内部名: `LEADER_RANDOM_INDUSTRIOUS`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_INDUSTRIOUS

### TXT_KEY_LEADER_RANDOM_FINANCIAL - TXT_KEY_LEADER_RANDOM_FINANCIAL

- 内部名: `LEADER_RANDOM_FINANCIAL`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_FINANCIAL

### TXT_KEY_LEADER_RANDOM_ARCANE - TXT_KEY_LEADER_RANDOM_ARCANE

- 内部名: `LEADER_RANDOM_ARCANE`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_ARCANE

### TXT_KEY_LEADER_RANDOM_RAIDERS - TXT_KEY_LEADER_RANDOM_RAIDERS

- 内部名: `LEADER_RANDOM_RAIDERS`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_RAIDERS

### TXT_KEY_LEADER_RANDOM_DEFENDER - TXT_KEY_LEADER_RANDOM_DEFENDER

- 内部名: `LEADER_RANDOM_DEFENDER`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_DEFENDER

### TXT_KEY_LEADER_RANDOM_CHARGE - TXT_KEY_LEADER_RANDOM_CHARGE

- 内部名: `LEADER_RANDOM_CHARGE`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_CHARGE

### TXT_KEY_LEADER_RANDOM_SPEECH - TXT_KEY_LEADER_RANDOM_SPEECH

- 内部名: `LEADER_RANDOM_SPEECH`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_SPEECH

### TXT_KEY_LEADER_RANDOM_NOURISH - TXT_KEY_LEADER_RANDOM_NOURISH

- 内部名: `LEADER_RANDOM_NOURISH`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_NOURISH

### TXT_KEY_LEADER_RANDOM_CONSTRUCTION - TXT_KEY_LEADER_RANDOM_CONSTRUCTION

- 内部名: `LEADER_RANDOM_CONSTRUCTION`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_CONSTRUCTION

### TXT_KEY_LEADER_RANDOM_BUILDER - TXT_KEY_LEADER_RANDOM_BUILDER

- 内部名: `LEADER_RANDOM_BUILDER`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_BUILDER

### TXT_KEY_LEADER_RANDOM_GENERAL - TXT_KEY_LEADER_RANDOM_GENERAL

- 内部名: `LEADER_RANDOM_GENERAL`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_GENERAL

### TXT_KEY_LEADER_RANDOM_AGNOSTIC - TXT_KEY_LEADER_RANDOM_AGNOSTIC

- 内部名: `LEADER_RANDOM_AGNOSTIC`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_AGNOSTIC

### TXT_KEY_LEADER_RANDOM_BARBARIAN - TXT_KEY_LEADER_RANDOM_BARBARIAN

- 内部名: `LEADER_RANDOM_BARBARIAN`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_BARBARIAN

### TXT_KEY_LEADER_RANDOM_SPRAWLING - TXT_KEY_LEADER_RANDOM_SPRAWLING

- 内部名: `LEADER_RANDOM_SPRAWLING`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_SPRAWLING

### TXT_KEY_LEADER_RANDOM_ADAPTIVE - TXT_KEY_LEADER_RANDOM_ADAPTIVE

- 内部名: `LEADER_RANDOM_ADAPTIVE`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_ADAPTIVE

### TXT_KEY_LEADER_RANDOM_FALLOW - TXT_KEY_LEADER_RANDOM_FALLOW

- 内部名: `LEADER_RANDOM_FALLOW`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_FALLOW

### (Magic Master Leader) - （呪文の達人指導者）

- 内部名: `LEADER_RANDOM_MAGIC_MASTER`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_MAGIC_MASTER

### (No Financial Leader) - （非金融志向の指導者）

- 内部名: `LEADER_RANDOM_NO_FINANCIAL`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_NO_FINANCIAL

### (No Agnostic Leader) - （非無神論の指導者）

- 内部名: `LEADER_RANDOM_NO_AGNOSTIC`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_NO_AGNOSTIC

### TXT_KEY_LEADER_RANDOM_NO_BARBARIAN - TXT_KEY_LEADER_RANDOM_NO_BARBARIAN

- 内部名: `LEADER_RANDOM_NO_BARBARIAN`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_NO_BARBARIAN

### TXT_KEY_LEADER_RANDOM_NO_SPRAWLING - TXT_KEY_LEADER_RANDOM_NO_SPRAWLING

- 内部名: `LEADER_RANDOM_NO_SPRAWLING`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_NO_SPRAWLING

### TXT_KEY_LEADER_RANDOM_NO_FALLOW - TXT_KEY_LEADER_RANDOM_NO_FALLOW

- 内部名: `LEADER_RANDOM_NO_FALLOW`
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `RandomLeader`: RANDOM_LEADER_NO_FALLOW

### Barbarian - 蛮族

- 内部名: `LEADER_BARBARIAN`
- 属性: 邪悪
- 志向: 無神論志向
- その他の設定:
  - `FavoriteUnitCombat`: 白兵ユニット

### Sabathiel - サバシエル

- 内部名: `LEADER_SABATHIEL`
- 属性: 善良
- 志向: カリスマ志向 / 伝説志向 / 殉死志向
- 好む社会制度: 神権政治
- 好む遺産: スケルスの鉱泉
- お気に入りの宗教: 秩序の修道会
- 宗教の重視度: エススの枢密院 iWeightModifier=-30 / 深海の旧支配者 iWeightModifier=-30 / 蒼褪めたヴェール iWeightModifier=-50 / 至光なる天空 iWeightModifier=10 / 秩序の修道会 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 25
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 55
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 40
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 狂信

### Capria - カプリア

- 内部名: `LEADER_CAPRIA`
- 属性: 善良
- 志向: 勤労志向 / 宗教志向 / 殉死志向
- 好む社会制度: 宗教主義
- 好む遺産: マーキュリアンの門
- お気に入りの宗教: 秩序の修道会
- 宗教の重視度: エススの枢密院 iWeightModifier=-30 / 深海の旧支配者 iWeightModifier=-30 / 蒼褪めたヴェール iWeightModifier=-50 / 至光なる天空 iWeightModifier=10 / 秩序の修道会 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 45
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 高潔の証
  - `FavoriteUnitCombat`: 信奉ユニット

### Tethira - テシラ

- 内部名: `LEADER_TETHIRA`
- 属性: 善良
- 志向: 攻撃志向 / 将官志向 / 魔法抵抗志向
- 好む社会制度: 宗教主義
- 好む遺産: アウレウスの竈
- お気に入りの宗教: 秩序の修道会
- 宗教の重視度: エススの枢密院 iWeightModifier=-30 / 深海の旧支配者 iWeightModifier=-30 / 蒼褪めたヴェール iWeightModifier=-50 / 至光なる天空 iWeightModifier=10 / 秩序の修道会 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 6
  - `iEconomyTechValue`: 100

### Decius - デキウス

- 内部名: `LEADER_DECIUS`
- 属性: 中立
- 志向: 侵掠志向 / 軍事志向 / 不屈
- 好む社会制度: 国民国家
- 好む遺産: ティターンの巨像
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 15
  - `iConquestVictoryWeight`: 55
  - `iDominationVictoryWeight`: 40
  - `iReligionVictoryWeight`: 5
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 30
  - `bReligionOpportunist`: 1
  - `FavoriteTech`: 軍事行動
  - `FavoriteUnitCombat`: 白兵ユニット

### Gaheris - ガヘリス

- 内部名: `LEADER_GAHERIS`
- 属性: 善良
- 志向: 宗教志向 / 侵掠志向
- 好む社会制度: 軍事国家
- 好む遺産: 聖者の偶像
- お気に入りの宗教: 秩序の修道会
- 宗教の重視度: エススの枢密院 iWeightModifier=-50 / 緑葉の同胞 iWeightModifier=-25 / 深海の旧支配者 iWeightModifier=-25 / 蒼褪めたヴェール iWeightModifier=-25 / 至光なる天空 iWeightModifier=25 / 秩序の修道会 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 封建制
  - `FavoriteUnitCombat`: 騎乗ユニット

### Angaad - アンガード

- 内部名: `LEADER_ANGAAD`
- 属性: 善良
- 志向: 組織志向 / TXT_KEY_TRAIT_IMPERIALIST
- 好む社会制度: 貴族制
- 好む遺産: ティターンの巨像
- お気に入りの宗教: 秩序の修道会
- 宗教の重視度: エススの枢密院 iWeightModifier=-50 / 深海の旧支配者 iWeightModifier=-30 / 蒼褪めたヴェール iWeightModifier=-30 / 至光なる天空 iWeightModifier=40 / 秩序の修道会 iWeightModifier=80 / キルモフのルーン iWeightModifier=20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 45
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 軍事戦略

### Varn Gosam - ヴァーン・ゴッサム

- 内部名: `LEADER_VARN`
- 属性: 善良
- 志向: 適応志向 / 宗教志向 / 信仰志向
- 好む社会制度: 天上評議会
- 好む遺産: 物見の塔
- お気に入りの宗教: 至光なる天空
- 宗教の重視度: エススの枢密院 iWeightModifier=-50 / 深海の旧支配者 iWeightModifier=-30 / 蒼褪めたヴェール iWeightModifier=-30 / 至光なる天空 iWeightModifier=50 / 秩序の修道会 iWeightModifier=10 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iAltarVictoryWeight`: 45
  - `iConquestVictoryWeight`: 10
  - `iDominationVictoryWeight`: 15
  - `iReligionVictoryWeight`: 55
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `TemporaryTraits`: 創造志向
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 聖職
  - `FavoriteUnitCombat`: 信奉ユニット

### Kane - ケイン

- 内部名: `LEADER_KANE`
- 属性: 中立
- 志向: 蛮族志向 / 金融志向 / 防御志向
- 好む社会制度: 天上評議会
- 好む遺産: 物見の塔
- 宗教の重視度: エススの枢密院 iWeightModifier=-50 / 深海の旧支配者 iWeightModifier=-30 / 蒼褪めたヴェール iWeightModifier=-30 / 至光なる天空 iWeightModifier=50 / 秩序の修道会 iWeightModifier=10 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 4
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 騎乗ユニット

### Shamash - シャマシュ

- 内部名: `LEADER_SHAMASH`
- 属性: 善良
- 志向: 宗教志向 / 交易志向
- 好む社会制度: 天上評議会
- 好む遺産: 物見の塔
- お気に入りの宗教: 至光なる天空
- 宗教の重視度: エススの枢密院 iWeightModifier=-99 / 緑葉の同胞 iWeightModifier=-99 / 深海の旧支配者 iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=-30 / 至光なる天空 iWeightModifier=75 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 交易
  - `FavoriteUnitCombat`: 信奉ユニット

### Usheeja - ユシージャ

- 内部名: `LEADER_USHEEJA`
- 属性: 中立
- 志向: 伝道志向 / 賢人志向
- 好む社会制度: 大量消費
- 好む遺産: 物見の塔
- お気に入りの宗教: 至光なる天空
- 宗教の重視度: エススの枢密院 iWeightModifier=-99 / 深海の旧支配者 iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=-99 / 至光なる天空 iWeightModifier=99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 魔術

### Saralet - サラレット

- 内部名: `LEADER_SARALET`
- 属性: 善良
- 志向: 金融志向 / 預言志向
- 好む社会制度: 国民国家
- 好む遺産: 天球の羅針盤
- お気に入りの宗教: 秩序の修道会
- 宗教の重視度: エススの枢密院 iWeightModifier=-50 / 深海の旧支配者 iWeightModifier=-30 / 蒼褪めたヴェール iWeightModifier=-30 / 至光なる天空 iWeightModifier=10 / 秩序の修道会 iWeightModifier=80 / キルモフのルーン iWeightModifier=10 / 緑葉の同胞 iWeightModifier=30 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 信奉ユニット

### Ethne the White - 白きエスネ

- 内部名: `LEADER_ETHNE`
- 属性: 善良
- 志向: 創造志向 / 預言志向 / 早熟志向
- 好む社会制度: 自由主義
- 好む遺産: シロナの祭殿
- 宗教の重視度: エススの枢密院 iWeightModifier=-10 / 深海の旧支配者 iWeightModifier=-10 / キルモフのルーン iWeightModifier=10 / 蒼褪めたヴェール iWeightModifier=-20 / 至光なる天空 iWeightModifier=10 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 40
  - `iTowerVictoryWeight`: 10
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 10
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 聖職

### Einion Logos - エイニオン・ロゴス

- 内部名: `LEADER_EINION`
- 属性: 善良
- 志向: 防御志向 / 哲学志向 / 殉死志向
- 好む社会制度: 平和主義
- 好む遺産: テンポランス神殿
- 宗教の重視度: エススの枢密院 iWeightModifier=-10 / 深海の旧支配者 iWeightModifier=-10 / キルモフのルーン iWeightModifier=10 / 蒼褪めたヴェール iWeightModifier=-20 / 至光なる天空 iWeightModifier=10 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 10
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 70
  - `iConquestVictoryWeight`: 5
  - `iDominationVictoryWeight`: 10
  - `iReligionVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iVassalPowerModifier`: 10
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 筆記
  - `FavoriteUnitCombat`: 弓術ユニット

### Thessalonica - テサロニカ

- 内部名: `LEADER_THESSALONICA`
- 属性: 善良
- 志向: 防御志向 / 宗教志向
- 好む社会制度: 平和主義
- 好む遺産: テンポランス神殿
- 宗教の重視度: エススの枢密院 iWeightModifier=-10 / 深海の旧支配者 iWeightModifier=-10 / キルモフのルーン iWeightModifier=10 / 蒼褪めたヴェール iWeightModifier=-20 / 至光なる天空 iWeightModifier=10 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 6
  - `bFemale`: 1
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 宗教法
  - `FavoriteUnitCombat`: 信奉ユニット

### Nephele - ネフェレ

- 内部名: `LEADER_NEPHELE`
- 属性: 善良
- 志向: 宗教志向 / 秘術志向 / 生命の達人
- 好む社会制度: 平和主義
- 好む遺産: 聖者の偶像
- 宗教の重視度: エススの枢密院 iWeightModifier=-99 / 深海の旧支配者 iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=-99 / 至光なる天空 iWeightModifier=75 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 狂信

### Meelais - ミレス

- 内部名: `LEADER_MEELAIS`
- 属性: 善良
- 志向: 預言志向 / 話術志向
- 好む社会制度: 平和主義
- 好む遺産: 聖者の偶像
- 宗教の重視度: エススの枢密院 iWeightModifier=-10 / 深海の旧支配者 iWeightModifier=-10 / キルモフのルーン iWeightModifier=10 / 蒼褪めたヴェール iWeightModifier=-20 / 至光なる天空 iWeightModifier=99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 70
  - `iConquestVictoryWeight`: 5
  - `iDominationVictoryWeight`: 10
  - `iReligionVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 130
  - `FavoriteUnitCombat`: 信奉ユニット

### Vesta - ヴェスタ

- 内部名: `LEADER_VESTA`
- 属性: 善良
- 志向: 防御志向 / 建設志向 / 大都市志向
- 好む社会制度: 平和主義
- 好む遺産: 聖者の偶像
- 宗教の重視度: エススの枢密院 iWeightModifier=-99 / 深海の旧支配者 iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=-99 / 至光なる天空 iWeightModifier=75 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 複合弓
  - `FavoriteUnitCombat`: 弓術ユニット

### Basium - バシウム

- 内部名: `LEADER_BASIUM`
- 属性: 善良
- 志向: 侵掠志向 / 伝説志向 / 工夫志向 / 殉死志向 / 復讐志向
- 好む社会制度: 軍事国家
- 好む遺産: テンポランス神殿
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iTowerVictoryWeight`: 10
  - `iAltarVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 50
  - `iEconomyTechValue`: 100

### Garrim Gyr - ガリム・ギュール

- 内部名: `LEADER_GARRIM`
- 属性: 善良
- 志向: 金融志向 / 生産志向
- 好む社会制度: 鎖国令
- 好む遺産: ギルド・オブ・ハンマーズ
- お気に入りの宗教: キルモフのルーン
- 宗教の重視度: キルモフのルーン iWeightModifier=25 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 7
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 20
  - `iDominationVictoryWeight`: 20
  - `iReligionVictoryWeight`: 20
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 建設

### Beeri Bawl - ビーリ・バウル

- 内部名: `LEADER_BEERI`
- 属性: 善良
- 志向: 勤労志向 / 金融志向
- 好む社会制度: ギルド制
- 好む遺産: ティターンの巨像
- お気に入りの宗教: キルモフのルーン
- 宗教の重視度: キルモフのルーン iWeightModifier=25 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 7
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 30
  - `iTowerVictoryWeight`: 40
  - `iAltarVictoryWeight`: 35
  - `iConquestVictoryWeight`: 15
  - `iDominationVictoryWeight`: 15
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 石工

### Gisli - ギズリ

- 内部名: `LEADER_GISLI`
- 属性: 中立
- 志向: 金融志向 / 組織志向
- 好む社会制度: ギルド制
- 好む遺産: デルプトゥスの醸造所
- お気に入りの宗教: キルモフのルーン
- 宗教の重視度: 深海の旧支配者 iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=-99 / キルモフのルーン iWeightModifier=75 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120

### Kish Rika - キシュ・リカ

- 内部名: `LEADER_KISH_RIKA`
- 属性: 善良
- 志向: 農耕志向 / 建設志向
- 好む社会制度: ギルド制
- 好む遺産: 労働者ギルド
- お気に入りの宗教: キルモフのルーン
- 宗教の重視度: キルモフのルーン iWeightModifier=99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 衛生設備

### Letigo - レティゴ

- 内部名: `LEADER_LETIGO`
- 属性: 善良
- 志向: 生産志向 / TXT_KEY_TRAIT_IMPERIALIST
- 好む社会制度: ギルド制
- 好む遺産: 労働者ギルド
- お気に入りの宗教: キルモフのルーン
- 宗教の重視度: キルモフのルーン iWeightModifier=99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 30
  - `iAltarVictoryWeight`: 20
  - `iConquestVictoryWeight`: 20
  - `iDominationVictoryWeight`: 35
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 封建制

### Bear Guin - ベア・グイン

- 内部名: `LEADER_BEAR_GUIN`
- 属性: 善良
- 志向: 建設志向 / 話術志向
- 好む社会制度: ギルド制
- 好む遺産: 労働者ギルド
- お気に入りの宗教: キルモフのルーン
- 宗教の重視度: キルモフのルーン iWeightModifier=99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 9
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 70
  - `iTowerVictoryWeight`: 15
  - `iAltarVictoryWeight`: 50
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 90
  - `iVassalPowerModifier`: -20
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 120

### Cardith Lorda - カーディス・ローダ

- 内部名: `LEADER_CARDITH`
- 属性: 善良
- 志向: 適応志向 / 哲学志向 / 大都市志向
- 好む社会制度: 自由主義
- 好む遺産: テンポランス神殿
- 宗教の重視度: キルモフのルーン iWeightModifier=10 / 至光なる天空 iWeightModifier=10 / 秩序の修道会 iWeightModifier=10 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 9
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 70
  - `iTowerVictoryWeight`: 15
  - `iAltarVictoryWeight`: 50
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 70
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 90
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: 20
  - `TemporaryTraits`: 拡張志向
  - `iEconomyTechValue`: 120

### Teacher Welsh - 教導官ウェルシュ

- 内部名: `LEADER_TEACHER`
- 属性: 善良
- 志向: 詠唱志向 / 話術志向 / 大都市志向 / 大地の達人
- 好む社会制度: 奨学金制
- 好む遺産: トレントンの聖水
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=-25 / エススの枢密院 iWeightModifier=-25 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 70
  - `iTowerVictoryWeight`: 15
  - `iAltarVictoryWeight`: 50
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 90
  - `iVassalPowerModifier`: -20
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 魔術

### Favna - ファーヴナ

- 内部名: `LEADER_FAVNA`
- 属性: 善良
- 志向: 防御志向 / 商才志向 / 大都市志向
- 好む社会制度: 奨学金制
- 好む遺産: アレクサンドリア図書館
- 宗教の重視度: 深海の旧支配者 iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=-99 / 至光なる天空 iWeightModifier=50 / 秩序の修道会 iWeightModifier=25 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 10
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iAltarVictoryWeight`: 40
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 70
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 90
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 通貨
  - `FavoriteUnitCombat`: 弓術ユニット

### Hyunkel - ヒュンケル

- 内部名: `LEADER_HYUNKEL`
- 属性: 善良
- 志向: 防御志向 / TXT_KEY_TRAIT_IMPERIALIST / 大都市志向 / 早熟志向
- 好む社会制度: 国民国家
- 好む遺産: ティターンの巨像
- 宗教の重視度: 深海の旧支配者 iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 10
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 70
  - `iConquestVictoryWeight`: 5
  - `iDominationVictoryWeight`: 10
  - `iReligionVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iVassalPowerModifier`: 10
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 数学

### Herne - ヘルネ

- 内部名: `LEADER_HERNE`
- 属性: 善良
- 志向: 防御志向 / 突撃志向 / 大都市志向 / 工夫志向
- 好む社会制度: 自由主義
- 好む遺産: 三圃組合
- 宗教の重視度: 秩序の修道会 iWeightModifier=10 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 15
  - `iConquestVictoryWeight`: 55
  - `iDominationVictoryWeight`: 40
  - `iReligionVictoryWeight`: 5
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 30
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 軍馬
  - `FavoriteUnitCombat`: 騎乗ユニット

### Cith Mor - シス・モー

- 内部名: `LEADER_CITH_MOR`
- 属性: 善良
- 志向: 拡張志向 / 金融志向 / 大都市志向
- 好む社会制度: 自由主義
- 好む遺産: 三圃組合
- 宗教の重視度: 秩序の修道会 iWeightModifier=10 / 蒼褪めたヴェール iWeightModifier=-20 / 至光なる天空 iWeightModifier=35 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 45
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 交易

### Cheron - シェロン

- 内部名: `LEADER_CHERON`
- 属性: 善良
- 志向: 商才志向 / 詠唱志向 / 大都市志向 / 精神の達人
- 好む社会制度: 自由主義
- 好む遺産: 三圃組合
- 宗教の重視度: 秩序の修道会 iWeightModifier=10 / 深海の旧支配者 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 45
  - `iAltarVictoryWeight`: 30
  - `iConquestVictoryWeight`: 15
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteUnitCombat`: 秘術ユニット

### Amelanchier - アメランキエル

- 内部名: `LEADER_AMELANCHIER`
- 属性: 中立
- 志向: 警邏志向 / 成長志向 / 不屈
- 好む社会制度: 国民国家
- 好む遺産: 物見の塔
- お気に入りの宗教: 緑葉の同胞
- 宗教の重視度: 緑葉の同胞 iWeightModifier=25 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 30
  - `iAltarVictoryWeight`: 25
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iReligionVictoryWeight`: 20
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 野生の触れ合い
  - `FavoriteUnitCombat`: 弓術ユニット

### Arendel Phaedra - アレンデル・パイドラ

- 内部名: `LEADER_ARENDEL`
- 属性: 善良
- 志向: 創造志向 / 伝道志向 / 信仰志向
- 好む社会制度: 貴族制
- 好む遺産: テンポランス神殿
- お気に入りの宗教: 緑葉の同胞
- 宗教の重視度: 緑葉の同胞 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 35
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 35
  - `iConquestVictoryWeight`: 5
  - `iDominationVictoryWeight`: 10
  - `iReligionVictoryWeight`: 40
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 演劇
  - `FavoriteUnitCombat`: 弓術ユニット

### Thessa - テッサ

- 内部名: `LEADER_THESSA`
- 属性: 中立
- 志向: 防御志向 / 秘術志向 / 呪付の達人
- 好む社会制度: 奨学金制
- 好む遺産: 禁書の地下墓所
- お気に入りの宗教: 緑葉の同胞
- 宗教の重視度: 緑葉の同胞 iWeightModifier=25 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 45
  - `iAltarVictoryWeight`: 30
  - `iConquestVictoryWeight`: 15
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 魔術

### Aibell - アイベル

- 内部名: `LEADER_AIBELL`
- 属性: 善良
- 志向: 哲学志向 / 詠唱志向 / 水の達人
- 好む社会制度: 奨学金制
- 好む遺産: 禁書の地下墓所
- お気に入りの宗教: 緑葉の同胞
- 宗教の重視度: 深海の旧支配者 iWeightModifier=-99 / キルモフのルーン iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=-99 / 緑葉の同胞 iWeightModifier=75 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 3
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 筆記

### Saule - サウレー

- 内部名: `LEADER_SAULE`
- 属性: 中立
- 志向: 組織志向 / 警邏志向 / 挽回志向
- 好む社会制度: 自由主義
- 好む遺産: アレクサンドリア図書館
- お気に入りの宗教: 緑葉の同胞
- 宗教の重視度: 深海の旧支配者 iWeightModifier=-99 / キルモフのルーン iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=-99 / 緑葉の同胞 iWeightModifier=75 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 3
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 動物の馴致
  - `FavoriteUnitCombat`: 偵察ユニット

### Eldarwen - エルダーウェン・アルカリン

- 内部名: `LEADER_ELDARWEN`
- 属性: 中立
- 志向: 拡張志向 / 成長志向
- 好む社会制度: 農地改革
- 好む遺産: アレクサンドリア図書館
- お気に入りの宗教: 緑葉の同胞
- 宗教の重視度: 深海の旧支配者 iWeightModifier=-99 / キルモフのルーン iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=-99 / 緑葉の同胞 iWeightModifier=75 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 複合弓
  - `FavoriteUnitCombat`: 弓術ユニット

### Arturus Thorne - アーチュラス・ソーン

- 内部名: `LEADER_ARTURUS`
- 属性: 中立
- 志向: 勤労志向 / 商才志向 / 工夫志向 / 不屈
- 好む社会制度: 大量消費
- 好む遺産: ギルド・オブ・ハンマーズ
- お気に入りの宗教: キルモフのルーン
- 宗教の重視度: エススの枢密院 iWeightModifier=-20 / キルモフのルーン iWeightModifier=50 / 蒼褪めたヴェール iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 30
  - `iAltarVictoryWeight`: 20
  - `iConquestVictoryWeight`: 20
  - `iDominationVictoryWeight`: 35
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 製錬
  - `FavoriteUnitCombat`: 攻城兵器

### Kandros Fir - カンドロス・ファー

- 内部名: `LEADER_KANDROS`
- 属性: 中立
- 志向: 攻撃志向 / 金融志向 / 工夫志向
- 好む社会制度: 大量消費
- 好む遺産: ギルド・オブ・ハンマーズ
- お気に入りの宗教: キルモフのルーン
- 宗教の重視度: エススの枢密院 iWeightModifier=-20 / キルモフのルーン iWeightModifier=50 / 蒼褪めたヴェール iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 20
  - `iAltarVictoryWeight`: 15
  - `iConquestVictoryWeight`: 35
  - `iDominationVictoryWeight`: 45
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 爆薬
  - `FavoriteUnitCombat`: 攻城兵器

### Nicodemus - ニコデマス

- 内部名: `LEADER_NICODEMUS`
- 属性: 善良
- 志向: 金融志向 / 建設志向 / 工夫志向
- 好む社会制度: 大量消費
- 好む遺産: デルプトゥスの醸造所
- お気に入りの宗教: キルモフのルーン
- 宗教の重視度: エススの枢密院 iWeightModifier=-99 / 緑葉の同胞 iWeightModifier=-99 / 深海の旧支配者 iWeightModifier=-99 / キルモフのルーン iWeightModifier=75 / 蒼褪めたヴェール iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 千仞の尾根

### Athel - アゼル

- 内部名: `LEADER_ATHEL`
- 属性: 邪悪
- 志向: 徴税志向 / 強欲志向 / 工夫志向
- 好む社会制度: 大量消費
- 好む遺産: ヴェルギュールの強欲
- 宗教の重視度: エススの枢密院 iWeightModifier=60 / 緑葉の同胞 iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=35 / キルモフのルーン iWeightModifier=25 / 至光なる天空 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 通貨
  - `FavoriteUnitCombat`: 白兵ユニット

### Vitnir - ビトニール

- 内部名: `LEADER_VITNIR`
- 属性: 中立
- 志向: TXT_KEY_TRAIT_IMPERIALIST / 農耕志向 / 工夫志向
- 好む社会制度: 大量消費
- 好む遺産: デルプトゥスの醸造所
- 宗教の重視度: 深海の旧支配者 iWeightModifier=-10 / キルモフのルーン iWeightModifier=99 / 蒼褪めたヴェール iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 7
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 20
  - `iDominationVictoryWeight`: 20
  - `iReligionVictoryWeight`: 20
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 建設

### Llamerada Bada - リャメラダ・バーダ

- 内部名: `LEADER_LLAMERADA`
- 属性: 中立
- 志向: 蒐集志向 / 警邏志向 / 工夫志向
- 好む社会制度: 大量消費
- 好む遺産: デルプトゥスの醸造所
- 宗教の重視度: 深海の旧支配者 iWeightModifier=-10 / キルモフのルーン iWeightModifier=99 / 蒼褪めたヴェール iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 35
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 35
  - `iConquestVictoryWeight`: 5
  - `iDominationVictoryWeight`: 10
  - `iReligionVictoryWeight`: 40
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 医薬

### Sandalphon - サンダルフォン

- 内部名: `LEADER_SANDALPHON`
- 属性: 中立
- 志向: 防御志向 / 勤労志向 / 退魔志向
- 好む社会制度: カースト制
- 好む遺産: アレクサンドリア図書館
- 宗教の重視度: エススの枢密院 iWeightModifier=25 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 60
  - `iAltarVictoryWeight`: 25
  - `iConquestVictoryWeight`: 10
  - `iDominationVictoryWeight`: 10
  - `iReligionVictoryWeight`: 20
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120

### Shekinah - シェキナ

- 内部名: `LEADER_SHEKINAH`
- 属性: 中立
- 志向: カリスマ志向 / 賢人志向
- 好む社会制度: カースト制
- 好む遺産: 鼠捕りギルド
- 宗教の重視度: エススの枢密院 iWeightModifier=25 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 6
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 数学

### Shumuel - シュムエル

- 内部名: `LEADER_SHUMUEL`
- 属性: 邪悪
- 志向: 警邏志向 / 商才志向 / 幻術志向
- 好む社会制度: ギルド制
- 好む遺産: 遠目と早耳の情報網
- 宗教の重視度: エススの枢密院 iWeightModifier=75 / 緑葉の同胞 iWeightModifier=-50 / キルモフのルーン iWeightModifier=-50 / 蒼褪めたヴェール iWeightModifier=25 / 至光なる天空 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=-50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 詐欺
  - `FavoriteUnitCombat`: 偵察ユニット

### Mirrough - ミローフ

- 内部名: `LEADER_MIRROUGH`
- 属性: 中立
- 志向: 哲学志向 / 野戦志向
- 好む社会制度: カースト制
- 好む遺産: 鼠捕りギルド
- 宗教の重視度: エススの枢密院 iWeightModifier=10 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 40
  - `iTowerVictoryWeight`: 45
  - `iAltarVictoryWeight`: 25
  - `iConquestVictoryWeight`: 10
  - `iDominationVictoryWeight`: 10
  - `iReligionVictoryWeight`: 20
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 毒物
  - `FavoriteUnitCombat`: 偵察ユニット

### Leasieigh - リーシー

- 内部名: `LEADER_LEASIEIGH`
- 属性: 善良
- 志向: 話術志向 / 警邏志向
- 好む社会制度: カースト制
- 好む遺産: マーキュリアンの門
- 宗教の重視度: 秩序の修道会 iWeightModifier=99 / 深海の旧支配者 iWeightModifier=-10 / 蒼褪めたヴェール iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 1
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 100
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 30
  - `iMaxWarMinAdjacentLandPercent`: 4
  - `iLimitedWarPowerRatio`: 100
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 動物の馴致
  - `FavoriteUnitCombat`: 偵察ユニット

### Rasiel - ラジエル

- 内部名: `LEADER_RASIEL`
- 属性: 善良
- 志向: 哲学志向 / 成長志向 / 大都市志向
- 好む社会制度: カースト制
- 好む遺産: 鼠捕りギルド
- 宗教の重視度: 秩序の修道会 iWeightModifier=99 / 深海の旧支配者 iWeightModifier=-10 / 蒼褪めたヴェール iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 100
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 毒物
  - `FavoriteUnitCombat`: 偵察ユニット

### Falamar - ファラマー

- 内部名: `LEADER_FALAMAR`
- 属性: 中立
- 志向: カリスマ志向 / 拡張志向 / 不屈
- 好む社会制度: カースト制
- 好む遺産: ファロス灯台
- 宗教の重視度: 深海の旧支配者 iWeightModifier=25 / 蒼褪めたヴェール iWeightModifier=-10 / 秩序の修道会 iWeightModifier=-10 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 3
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 30
  - `iAltarVictoryWeight`: 20
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 40
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteUnitCombat`: 海軍ユニット

### Hannah the Irin - ハンナ・ジ・イリン

- 内部名: `LEADER_HANNAH`
- 属性: 中立
- 志向: 金融志向 / 侵掠志向 / 信仰志向
- 好む社会制度: 対外貿易
- 好む遺産: ファロス灯台
- お気に入りの宗教: 深海の旧支配者
- 宗教の重視度: 深海の旧支配者 iWeightModifier=50 / 至光なる天空 iWeightModifier=-20 / 秩序の修道会 iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 40
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 15
  - `iAltarVictoryWeight`: 10
  - `iConquestVictoryWeight`: 50
  - `iDominationVictoryWeight`: 35
  - `iReligionVictoryWeight`: 30
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 通貨
  - `FavoriteUnitCombat`: 海軍ユニット

### Captain Fritz - フリッツ船長

- 内部名: `LEADER_FRITZ`
- 属性: 邪悪
- 志向: 攻撃志向 / 交易志向
- 好む社会制度: 大量消費
- 好む遺産: ヘロンの玉座
- お気に入りの宗教: 深海の旧支配者
- 宗教の重視度: エススの枢密院 iWeightModifier=20 / 緑葉の同胞 iWeightModifier=-99 / キルモフのルーン iWeightModifier=-25 / 深海の旧支配者 iWeightModifier=50 / 至光なる天空 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 鉄器
  - `FavoriteUnitCombat`: 海軍ユニット

### Naias - ナイアス

- 内部名: `LEADER_NAIAS`
- 属性: 中立
- 志向: 金融志向 / 交易志向
- 好む社会制度: カースト制
- 好む遺産: ファロス灯台
- 宗教の重視度: エススの枢密院 iWeightModifier=15 / 緑葉の同胞 iWeightModifier=-99 / 深海の旧支配者 iWeightModifier=25 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 海図
  - `FavoriteUnitCombat`: 海軍ユニット

### Casin Loveless - カジン・ラヴレス

- 内部名: `LEADER_CASIN`
- 属性: 中立
- 志向: 建設志向 / 交易志向
- 好む社会制度: 対外貿易
- 好む遺産: ヴェルギュールの強欲
- 宗教の重視度: 深海の旧支配者 iWeightModifier=80 / 至光なる天空 iWeightModifier=-20 / 秩序の修道会 iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 30
  - `iConquestVictoryWeight`: 55
  - `iDominationVictoryWeight`: 45
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 天文学
  - `FavoriteUnitCombat`: 海軍ユニット

### Mordmorgan - モードモーガン

- 内部名: `LEADER_MORDMORGAN`
- 属性: 邪悪
- 志向: 話術志向 / 交易志向
- 好む社会制度: 農地改革
- 好む遺産: ヘロンの玉座
- 宗教の重視度: 深海の旧支配者 iWeightModifier=99 / 至光なる天空 iWeightModifier=-20 / 秩序の修道会 iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 90
  - `iVassalPowerModifier`: -20
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 交易
  - `FavoriteUnitCombat`: 海軍ユニット

### Cassiel - カシエル

- 内部名: `LEADER_CASSIEL`
- 属性: 中立
- 志向: 無神論志向 / 適応志向 / 哲学志向
- 好む社会制度: 平和主義
- 好む遺産: 国王記念館
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 7
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 30
  - `TemporaryTraits`: 勤労志向
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 筆記

### Minister Koun - コウン大臣

- 内部名: `LEADER_KOUN`
- 属性: 中立
- 志向: 無神論志向 / 哲学志向 / TXT_KEY_TRAIT_IMPERIALIST
- 好む社会制度: 平和主義
- 好む遺産: 国王記念館
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 7
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 8
  - `iEconomyTechValue`: 120

### Golbez - ゴルベーザ

- 内部名: `LEADER_GOLBEZ`
- 属性: 中立
- 志向: 無神論志向 / 軍事志向 / 詠唱志向 / 影の達人
- 好む社会制度: 国民国家
- 好む遺産: シロナの祭殿
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 80
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 製錬
  - `FavoriteUnitCombat`: 白兵ユニット

### Melissa Drizzle - メリッサ・ドリズル

- 内部名: `LEADER_MELISSA`
- 属性: 中立
- 志向: 無神論志向 / 秘術志向 / 将官志向 / 炎の達人
- 好む社会制度: 国民国家
- 好む遺産: 八魔陣
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 3
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 45
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 魔術
  - `FavoriteUnitCombat`: 秘術ユニット

### Goodreau - グッドレオー

- 内部名: `LEADER_GOODREAU`
- 属性: 中立
- 志向: 無神論志向 / 賢人志向 / 商才志向 / 多様志向
- 好む社会制度: 平和主義
- 好む遺産: グッドレオーの大理石像
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `FavoriteTech`: 通貨

### Menec - メネク

- 内部名: `LEADER_MENEC`
- 属性: 中立
- 志向: 無神論志向 / カリスマ志向 / 蒐集志向 / 多様志向
- 好む社会制度: 共和制
- 好む遺産: スケルスの鉱泉
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 40
  - `iTowerVictoryWeight`: 10
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 10
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 医薬
  - `FavoriteUnitCombat`: 白兵ユニット

### Zodalore - ゾーダロール

- 内部名: `LEADER_ZODALORE`
- 属性: 中立
- 志向: 無神論志向 / 哲学志向 / 強化志向 / 多様志向 / 混沌の達人
- 好む社会制度: 大量消費
- 好む遺産: 遠目と早耳の情報網
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 20
  - `iTechTradeKnownPercent`: 60
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 90
  - `iAltarVictoryWeight`: 10
  - `iConquestVictoryWeight`: 5
  - `iDominationVictoryWeight`: 5
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 120

### Outhe - オーセ

- 内部名: `LEADER_OUTHE`
- 属性: 中立
- 志向: 無神論志向 / 探求志向 / 賢人志向 / 大都市志向 / 多様志向
- 好む社会制度: 大量消費
- 好む遺産: トレントンの聖水
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 7
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 30
  - `iTowerVictoryWeight`: 40
  - `iAltarVictoryWeight`: 35
  - `iConquestVictoryWeight`: 15
  - `iDominationVictoryWeight`: 15
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 魔術
  - `FavoriteUnitCombat`: 白兵ユニット

### Tasunke - タスンケ

- 内部名: `LEADER_TASUNKE`
- 属性: 中立
- 志向: 侵掠志向 / 突撃志向 / 早熟志向
- 好む社会制度: ギルド制
- 好む遺産: 九人衆ギルド
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 15
  - `iAltarVictoryWeight`: 15
  - `iConquestVictoryWeight`: 55
  - `iDominationVictoryWeight`: 45
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 建設
  - `FavoriteUnitCombat`: 騎乗ユニット

### Rhoanna - ロアンナ

- 内部名: `LEADER_RHOANNA`
- 属性: 中立
- 志向: 金融志向 / 野戦志向 / 掠奪
- 好む社会制度: 大量消費
- 好む遺産: 九王者の騎獣
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 3
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 20
  - `iAltarVictoryWeight`: 20
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 80
  - `FavoriteTech`: 通貨
  - `FavoriteUnitCombat`: 騎乗ユニット

### Captain Ostanes - オスタネス隊長

- 内部名: `LEADER_OSTANES`
- 属性: 中立
- 志向: 迅速志向 / 将官志向
- 好む社会制度: 大量消費
- 好む遺産: 九王者の騎獣
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 6
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 80
  - `FavoriteTech`: 地図
  - `FavoriteUnitCombat`: 騎乗ユニット

### Captain Uldanor - ウルダンノール隊長

- 内部名: `LEADER_ULDANOR`
- 属性: 中立
- 志向: 防御志向 / 将官志向
- 好む社会制度: 大量消費
- 好む遺産: 九王者の騎獣
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 6
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 80
  - `FavoriteTech`: 鐙
  - `FavoriteUnitCombat`: 騎乗ユニット

### Selma - セルマ

- 内部名: `LEADER_SELMA`
- 属性: 中立
- 志向: 侵掠志向 / 万能志向
- 好む社会制度: 自由主義
- 好む遺産: 九王者の騎獣
- 宗教の重視度: エススの枢密院 iWeightModifier=25 / 緑葉の同胞 iWeightModifier=25 / キルモフのルーン iWeightModifier=25 / 深海の旧支配者 iWeightModifier=-50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 軍事行動
  - `FavoriteUnitCombat`: 騎乗ユニット

### Ilithiridan - イリシリダン

- 内部名: `LEADER_ILITHIRIDAN`
- 属性: 善良
- 志向: 組織志向 / カリスマ志向
- 好む社会制度: 大量消費
- 好む遺産: 九王者の騎獣
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 20
  - `iAltarVictoryWeight`: 20
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 80
  - `FavoriteTech`: 軍事戦略
  - `FavoriteUnitCombat`: 騎乗ユニット

### Valledia the Even - 均等なるヴァレディア

- 内部名: `LEADER_VALLEDIA`
- 属性: 中立
- 志向: 秘術志向 / 組織志向 / 法の達人
- 好む社会制度: 徒弟制
- 好む遺産: アハリエンの宝冠
- 宗教の重視度: 緑葉の同胞 iWeightModifier=10 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 15
  - `iTechTradeKnownPercent`: 5
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 70
  - `iAltarVictoryWeight`: 20
  - `iConquestVictoryWeight`: 20
  - `iDominationVictoryWeight`: 15
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 魔術

### Dain the Caswallawn - デイン・ザ・カスワラウン

- 内部名: `LEADER_DAIN`
- 属性: 中立
- 志向: 秘術志向 / 哲学志向 / 精神の達人
- 好む社会制度: 奨学金制
- 好む遺産: 禁書の地下墓所
- 宗教の重視度: 緑葉の同胞 iWeightModifier=10 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 20
  - `iTechTradeKnownPercent`: 60
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 90
  - `iAltarVictoryWeight`: 10
  - `iConquestVictoryWeight`: 5
  - `iDominationVictoryWeight`: 5
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 10
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 筆記

### Tya Kiri - ティヤ・キリ

- 内部名: `LEADER_TYA`
- 属性: 中立
- 志向: 秘術志向 / 賢人志向 / 愚鈍志向 / 混沌の達人 / 超魔術の達人 / 魂の達人
- 好む社会制度: 貴族制
- 好む遺産: 八魔陣
- 宗教の重視度: 深海の旧支配者 iWeightModifier=80 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 20
  - `iTechTradeKnownPercent`: 60
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 6
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 秘術の伝承知識
  - `FavoriteUnitCombat`: 秘術ユニット

### Gwyen - グウィエン

- 内部名: `LEADER_GWYEN`
- 属性: 中立
- 志向: 秘術志向 / 金融志向 / 幻術志向
- 好む社会制度: 鎖国令
- 好む遺産: アハリエンの宝冠
- 宗教の重視度: エススの枢密院 iWeightModifier=20 / 緑葉の同胞 iWeightModifier=20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 天文学
  - `FavoriteUnitCombat`: 秘術ユニット

### Verlain - バーレイン

- 内部名: `LEADER_VERLAIN`
- 属性: 邪悪
- 志向: 秘術志向 / 侵掠志向 / 触死志向
- 好む社会制度: 奨学金制
- 好む遺産: レウケティオスのアトリエ
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=50 / 深海の旧支配者 iWeightModifier=50 / エススの枢密院 iWeightModifier=25 / キルモフのルーン iWeightModifier=-10 / 至光なる天空 iWeightModifier=-10 / 秩序の修道会 iWeightModifier=-15 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 70
  - `iAltarVictoryWeight`: 10
  - `iConquestVictoryWeight`: 15
  - `iDominationVictoryWeight`: 15
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 屍霊術
  - `FavoriteUnitCombat`: 秘術ユニット

### Lorelei Coral - ローレライ・コーラル

- 内部名: `LEADER_LORELEI`
- 属性: 中立
- 志向: 詠唱志向 / 強化志向 / 水の達人
- 好む社会制度: 徒弟制
- 好む遺産: アハリエンの宝冠
- 宗教の重視度: 深海の旧支配者 iWeightModifier=80 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 60
  - `iAltarVictoryWeight`: 20
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 20
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 錬金術

### Charadon - キャラドン

- 内部名: `LEADER_CHARADON`
- 属性: 邪悪
- 志向: 攻撃志向 / 弱肉強食志向 / 蛮族志向
- 好む社会制度: 奴隷制
- 好む遺産: グッドレオーの大理石像
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 1
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 5
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 75
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 20
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 80
  - `FavoriteTech`: 青銅器
  - `FavoriteUnitCombat`: 白兵ユニット

### Mahala - マヘイラ

- 内部名: `LEADER_MAHALA`
- 属性: 邪悪
- 志向: 組織志向 / 侵掠志向 / 工夫志向
- 好む社会制度: 軍事国家
- 好む遺産: 問い掛けるものの石像
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 1
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 25
  - `iConquestVictoryWeight`: 60
  - `iDominationVictoryWeight`: 40
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 80
  - `FavoriteTech`: 軍事戦略
  - `FavoriteUnitCombat`: 白兵ユニット

### Baron Duin Halfmorn - 半獣のデュイン男爵

- 内部名: `LEADER_DUIN`
- 属性: 邪悪
- 志向: 突撃志向 / 将官志向 / 魔法抵抗志向
- 好む社会制度: 都市国家
- 好む遺産: 三圃組合
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 1
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 20
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 80
  - `FavoriteTech`: 野生の触れ合い
  - `FavoriteUnitCombat`: 白兵ユニット

### Byggbir - ビュグヴィル

- 内部名: `LEADER_BYGGVIR`
- 属性: 邪悪
- 志向: 攻撃志向 / 詠唱志向 / 蛮族志向 / 大気の達人
- 好む社会制度: 軍需優先
- 好む遺産: トレントンの聖水
- 宗教の重視度: キルモフのルーン iWeightModifier=-10 / 深海の旧支配者 iWeightModifier=10 / 至光なる天空 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: エーテルの知識

### Sirvagha - シルバガー

- 内部名: `LEADER_SIRVAGHA`
- 属性: 邪悪
- 志向: 攻撃志向 / 軍事志向 / 蛮族志向
- 好む社会制度: 都市国家
- 好む遺産: 空の霊廟
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 5
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 75
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 20
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 80
  - `FavoriteTech`: 建設
  - `FavoriteUnitCombat`: 白兵ユニット

### Emma Vargamor - エマ・ヴァルガモア

- 内部名: `LEADER_EMMA`
- 属性: 中立
- 志向: 無神論志向 / 適応志向 / 交易志向
- 好む社会制度: 対外貿易
- 好む遺産: ダグダの大神殿
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 7
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 30
  - `TemporaryTraits`: 強欲志向
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 80
  - `FavoriteTech`: 通貨

### Keelyn - キーリン

- 内部名: `LEADER_KEELYN`
- 属性: 邪悪
- 志向: 召喚志向 / 蒐集志向 / 超魔術の達人
- 好む社会制度: 奴隷制
- 好む遺産: シリヴェンの完璧なる竪琴
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=25 / 至光なる天空 iWeightModifier=-10 / 秩序の修道会 iWeightModifier=-25 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 45
  - `iTowerVictoryWeight`: 50
  - `iConquestVictoryWeight`: 20
  - `iDominationVictoryWeight`: 20
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 130

### Perpentach - パーペンタク

- 内部名: `LEADER_PERPENTACH`
- 属性: 邪悪
- 志向: 狂気志向 / 魔法抵抗志向 / 精神の達人
- 好む社会制度: 奴隷制
- 好む遺産: 夢の劇場
- 宗教の重視度: 深海の旧支配者 iWeightModifier=25 / 至光なる天空 iWeightModifier=-20 / 秩序の修道会 iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 45
  - `iTowerVictoryWeight`: 25
  - `iConquestVictoryWeight`: 45
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 30
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iVassalPowerModifier`: 20
  - `TemporaryTraits`: 秘術志向 / カリスマ志向 / 創造志向
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 100

### Weevil, Pickle and Hyde - ウィーヴィルとピクルとハイド

- 内部名: `LEADER_WEEVIL`
- 属性: 邪悪
- 志向: 蒐集志向 / 強欲志向
- 好む社会制度: 奴隷制
- 好む遺産: 夢の劇場
- 宗教の重視度: 深海の旧支配者 iWeightModifier=25 / 至光なる天空 iWeightModifier=-20 / 秩序の修道会 iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iVassalPowerModifier`: 20
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 通貨

### Furia the Mad - 狂気のフューリア

- 内部名: `LEADER_FURIA`
- 属性: 邪悪
- 志向: 軍事志向 / 強化志向 / 混沌の達人
- 好む社会制度: 奴隷制
- 好む遺産: シリヴェンの完璧なる竪琴
- 宗教の重視度: 深海の旧支配者 iWeightModifier=25 / 至光なる天空 iWeightModifier=-20 / 秩序の修道会 iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 製錬

### Melisandre - メリサンドラ

- 内部名: `LEADER_MELISANDRE`
- 属性: 邪悪
- 志向: 召喚志向 / 徴税志向 / 肉体の達人
- 好む社会制度: 奴隷制
- 好む遺産: シリヴェンの完璧なる竪琴
- 宗教の重視度: 深海の旧支配者 iWeightModifier=25 / 至光なる天空 iWeightModifier=-20 / 秩序の修道会 iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 税制

### Taliesin - タリエシン

- 内部名: `LEADER_TALIESIN`
- 属性: 邪悪
- 志向: 召喚志向 / 話術志向 / 生命の達人
- 好む社会制度: 奴隷制
- 好む遺産: 創造の酒造
- 宗教の重視度: エススの枢密院 iWeightModifier=30 / 緑葉の同胞 iWeightModifier=-99 / キルモフのルーン iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=40 / 至光なる天空 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 90
  - `iVassalPowerModifier`: -20
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 毒物

### Nojah the Fake - だまし絵のノヤ－

- 内部名: `LEADER_NOJAH`
- 属性: 中立
- 志向: 召喚志向 / 万能志向 / 幻術志向 / 自然の達人
- 好む社会制度: 奨学金制
- 好む遺産: シリヴェンの完璧なる竪琴
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 45
  - `iTowerVictoryWeight`: 25
  - `iConquestVictoryWeight`: 45
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 30
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iVassalPowerModifier`: 20
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 変成術

### Nell the Swift - 早業のネル

- 内部名: `LEADER_NELL`
- 属性: 善良
- 志向: 創造志向 / 迅速志向 / 魔法抵抗志向
- 好む社会制度: 奨学金制
- 好む遺産: ダグダの大神殿
- 宗教の重視度: 緑葉の同胞 iWeightModifier=99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 50
  - `iMaxGoldTradePercent`: 15
  - `iMaxGoldPerTurnTradePercent`: 15
  - `iCultureVictoryWeight`: 45
  - `iTowerVictoryWeight`: 50
  - `iConquestVictoryWeight`: 20
  - `iDominationVictoryWeight`: 20
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 100
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 演劇
  - `FavoriteUnitCombat`: 偵察ユニット

### Jonas Endain - ヨナス・エンダイン

- 内部名: `LEADER_JONAS`
- 属性: 邪悪
- 志向: 蛮族志向 / 宗教志向 / 生産志向 / 信仰志向
- 好む社会制度: 軍需優先
- 好む遺産: 竜の財宝
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 3
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 45
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 製錬

### Sheelba - シェルバ

- 内部名: `LEADER_SHEELBA`
- 属性: 邪悪
- 志向: 蛮族志向 / 組織志向 / 突撃志向 / 復讐志向
- 好む社会制度: 徒弟制
- 好む遺産: 竜の財宝
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 15
  - `iConquestVictoryWeight`: 65
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 法律
  - `FavoriteUnitCombat`: 白兵ユニット

### Hafgan the Purger - 追放者ハウゲン

- 内部名: `LEADER_HAFGAN`
- 属性: 邪悪
- 志向: 蛮族志向 / カリスマ志向 / 防御志向 / 魔法抵抗志向
- 好む社会制度: 徒弟制
- 好む遺産: 竜の財宝
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 建設
  - `FavoriteUnitCombat`: 白兵ユニット

### Azzan - アザン

- 内部名: `LEADER_AZZAN`
- 属性: 邪悪
- 志向: 蛮族志向 / 建設志向 / 警邏志向 / 工夫志向
- 好む社会制度: ギルド制
- 好む遺産: 竜の財宝
- 宗教の重視度: エススの枢密院 iWeightModifier=10 / 緑葉の同胞 iWeightModifier=-20 / 深海の旧支配者 iWeightModifier=10 / 蒼褪めたヴェール iWeightModifier=30 / 至光なる天空 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 石工

### Ji - ジー

- 内部名: `LEADER_JI`
- 属性: 中立
- 志向: 蛮族志向 / 宗教志向 / 弱肉強食志向
- 好む社会制度: 軍需優先
- 好む遺産: ガル=デュールの鉱山
- 宗教の重視度: キルモフのルーン iWeightModifier=99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 45
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 青銅器
  - `FavoriteUnitCombat`: 白兵ユニット

### Hehnku - ヘンク

- 内部名: `LEADER_HEHNKU`
- 属性: 邪悪
- 志向: 蛮族志向 / 攻撃志向 / 迅速志向
- 好む社会制度: 徒弟制
- 好む遺産: 竜の財宝
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 15
  - `iConquestVictoryWeight`: 65
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 騎乗
  - `FavoriteUnitCombat`: 騎乗ユニット

### Faeryl Viconia - ファエリル・ヴィコーニア

- 内部名: `LEADER_FAERYL`
- 属性: 邪悪
- 志向: 秘術志向 / 突撃志向 / 復讐志向 / 早熟志向 / 肉体の達人
- 好む社会制度: 地下評議会
- 好む遺産: 冬の宮殿
- お気に入りの宗教: エススの枢密院
- 宗教の重視度: エススの枢密院 iWeightModifier=75 / 緑葉の同胞 iWeightModifier=50 / キルモフのルーン iWeightModifier=-20 / 至光なる天空 iWeightModifier=-50 / 秩序の修道会 iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 3
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 55
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 55
  - `iReligionVictoryWeight`: 5
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 偵察ユニット

### Rivanna the Wraith Lord - 死霊の主リヴァンナ

- 内部名: `LEADER_RIVANNA`
- 属性: 邪悪
- 志向: 召喚志向 / 警邏志向 / 死の達人
- 好む社会制度: 地下評議会
- 好む遺産: 魂の溶鉱炉
- お気に入りの宗教: エススの枢密院
- 宗教の重視度: エススの枢密院 iWeightModifier=75 / 緑葉の同胞 iWeightModifier=50 / キルモフのルーン iWeightModifier=-20 / 至光なる天空 iWeightModifier=-50 / 秩序の修道会 iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 3
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 魔術

### Volanna - ヴォランナ

- 内部名: `LEADER_VOLANNA`
- 属性: 邪悪
- 志向: 侵掠志向 / 野戦志向 / 復讐志向
- 好む社会制度: 地下評議会
- 好む遺産: 鼠捕りギルド
- お気に入りの宗教: エススの枢密院
- 宗教の重視度: エススの枢密院 iWeightModifier=75 / 緑葉の同胞 iWeightModifier=50 / キルモフのルーン iWeightModifier=-20 / 至光なる天空 iWeightModifier=-50 / 秩序の修道会 iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 3
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 毒物
  - `FavoriteUnitCombat`: 偵察ユニット

### Matheus - マテウス

- 内部名: `LEADER_MATHEUS`
- 属性: 邪悪
- 志向: 拡張志向 / 将官志向
- 好む社会制度: ギルド制
- 好む遺産: 遠目と早耳の情報網
- お気に入りの宗教: エススの枢密院
- 宗教の重視度: エススの枢密院 iWeightModifier=99 / 緑葉の同胞 iWeightModifier=50 / キルモフのルーン iWeightModifier=-99 / 至光なる天空 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 詐欺
  - `FavoriteUnitCombat`: 偵察ユニット

### Hatheim - ハセイム

- 内部名: `LEADER_HATHEIM`
- 属性: 邪悪
- 志向: 金融志向 / 警邏志向 / 工夫志向
- 好む社会制度: カースト制
- 好む遺産: 鼠捕りギルド
- お気に入りの宗教: 緑葉の同胞
- 宗教の重視度: 緑葉の同胞 iWeightModifier=99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 動物の馴致
  - `FavoriteUnitCombat`: 偵察ユニット

### Utiruso - ウティルソ

- 内部名: `LEADER_UTIRUSO`
- 属性: 邪悪
- 志向: 探求志向 / 強欲志向 / 蛮族志向 / 触死志向
- 好む社会制度: カースト制
- 好む遺産: アレクサンドリア図書館
- お気に入りの宗教: 緑葉の同胞
- 宗教の重視度: 緑葉の同胞 iWeightModifier=99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: ギルド
  - `FavoriteUnitCombat`: 偵察ユニット

### Alexis - アレクシス

- 内部名: `LEADER_ALEXIS`
- 属性: 邪悪
- 志向: 組織志向 / 話術志向 / 魔法抵抗志向
- 好む社会制度: 貴族制
- 好む遺産: 魂の溶鉱炉
- 宗教の重視度: エススの枢密院 iWeightModifier=25 / 蒼褪めたヴェール iWeightModifier=25 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 30
  - `iConquestVictoryWeight`: 55
  - `iDominationVictoryWeight`: 45
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 80
  - `FavoriteTech`: 狂信
  - `FavoriteUnitCombat`: 白兵ユニット

### Flauros - フラウロス

- 内部名: `LEADER_FLAUROS`
- 属性: 邪悪
- 志向: 金融志向 / 徴税志向 / 早熟志向
- 好む社会制度: 貴族制
- 好む遺産: 縛鎖の柱
- 宗教の重視度: エススの枢密院 iWeightModifier=25 / 深海の旧支配者 iWeightModifier=25 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 40
  - `iTowerVictoryWeight`: 35
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 通貨
  - `FavoriteUnitCombat`: 白兵ユニット

### Mahon the Butcher - 皆殺しのマホン

- 内部名: `LEADER_MAHON`
- 属性: 邪悪
- 志向: 攻撃志向 / 拡張志向
- 好む社会制度: 貴族制
- 好む遺産: 縛鎖の柱
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=25 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteUnitCombat`: 白兵ユニット

### Nergal - ネルガル

- 内部名: `LEADER_NERGAL`
- 属性: 邪悪
- 志向: 組織志向 / 農耕志向
- 好む社会制度: 貴族制
- 好む遺産: 三圃組合
- 宗教の重視度: 緑葉の同胞 iWeightModifier=-99 / 深海の旧支配者 iWeightModifier=50 / キルモフのルーン iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=75 / 至光なる天空 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 封建制

### Elena - エレナ

- 内部名: `LEADER_ELENA`
- 属性: 善良
- 志向: 召喚志向 / 強欲志向 / 挽回志向 / 大気の達人
- 好む社会制度: 貴族制
- 好む遺産: 問い掛けるものの石像
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=25 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 110
  - `iBaseAttackOddsChange`: 2
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 錬金術
  - `FavoriteUnitCombat`: 白兵ユニット

### Elijah Arnaud - エリヤ・アルノー

- 内部名: `LEADER_ELIJAH`
- 属性: 邪悪
- 志向: 成長志向 / 農耕志向 / 奴隷志向
- 好む社会制度: 農地改革
- 好む遺産: 縛鎖の柱
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=25 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 9
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 90
  - `iVassalPowerModifier`: -20
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 暦
  - `FavoriteUnitCombat`: 白兵ユニット

### Ailimer - 緋のエイリメール

- 内部名: `LEADER_AILIMER`
- 属性: 邪悪
- 志向: 組織志向 / 万能志向
- 好む社会制度: 軍事国家
- 好む遺産: 問い掛けるものの石像
- お気に入りの宗教: エススの枢密院
- 宗教の重視度: エススの枢密院 iWeightModifier=60 / 緑葉の同胞 iWeightModifier=-99 / 深海の旧支配者 / キルモフのルーン iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=60 / 至光なる天空 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=60 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 45
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 70
  - `iLimitedWarPowerRatio`: 130
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 数学
  - `FavoriteUnitCombat`: 白兵ユニット

### Tebryn Arbandi - テブリン・アルバンディ

- 内部名: `LEADER_TEBRYN`
- 属性: 邪悪
- 志向: 秘術志向 / 召喚志向 / 魔法抵抗志向 / 触死志向 / 炎の達人
- 好む社会制度: 奨学金制
- 好む遺産: ラグナロクの預言
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: キルモフのルーン iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=50 / 至光なる天空 iWeightModifier=-20 / 秩序の修道会 iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 50
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 20
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 魔術
  - `FavoriteUnitCombat`: 秘術ユニット

### Os-Gabella - オズ=ガベラ

- 内部名: `LEADER_OS-GABELLA`
- 属性: 邪悪
- 志向: 勤労志向 / 召喚志向 / 復讐志向 / 次元の達人
- 好む社会制度: 奴隷制
- 好む遺産: ラグナロクの預言
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: キルモフのルーン iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=50 / 至光なる天空 iWeightModifier=-20 / 秩序の修道会 iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 50
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 20
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 邪悪への道
  - `FavoriteUnitCombat`: 秘術ユニット

### Averax the Cambion - 半妖のアヴェラクス

- 内部名: `LEADER_AVERAX`
- 属性: 邪悪
- 志向: 召喚志向 / 強化志向 / 蛮族志向 / 影の達人
- 好む社会制度: 奴隷制
- 好む遺産: ラグナロクの預言
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: キルモフのルーン iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=50 / 至光なる天空 iWeightModifier=-20 / 秩序の修道会 iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 4
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 魂の堕落

### Gosea - ゴセア

- 内部名: `LEADER_GOSEA`
- 属性: 邪悪
- 志向: 哲学志向 / 召喚志向 / 魔法抵抗志向 / 太陽の達人
- 好む社会制度: 奴隷制
- 好む遺産: ラグナロクの預言
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: キルモフのルーン iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=50 / 至光なる天空 iWeightModifier=-20 / 秩序の修道会 iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 4
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 筆記

### Malchavic - マルキャヴィーク

- 内部名: `LEADER_MALCHAVIC`
- 属性: 邪悪
- 志向: 召喚志向 / 軍事志向 / 魂の達人
- 好む社会制度: 奴隷制
- 好む遺産: ラグナロクの預言
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: キルモフのルーン iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=50 / 至光なる天空 iWeightModifier=-20 / 秩序の修道会 iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 4
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 製錬

### Sir.Eromkcalb - エロンカル卿

- 内部名: `LEADER_EROMKCALB`
- 属性: 邪悪
- 志向: 召喚志向 / 詠唱志向 / 触死志向
- 好む社会制度: 奨学金制
- 好む遺産: ラグナロクの預言
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: キルモフのルーン iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=50 / 至光なる天空 iWeightModifier=-20 / 秩序の修道会 iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 50
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 20
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: エーテルの知識
  - `FavoriteUnitCombat`: 秘術ユニット

### Hyborem - ハイボレム

- 内部名: `LEADER_HYBOREM`
- 属性: 邪悪
- 志向: 哲学志向 / 伝説志向 / 挽回志向 / 不可逆の達人 / 炎の達人
- 好む社会制度: 奨学金制
- 好む遺産: 地獄全書
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=50 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 40
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 50
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 悪意の企み

### Auric Ulvin - オーリック・ウルヴィン

- 内部名: `LEADER_AURIC`
- 属性: 邪悪
- 志向: 無神論志向 / 防御志向 / 伝説志向 / 氷の達人
- 好む社会制度: 対外貿易
- 好む遺産: 竜骨の宮殿
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 40
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 55
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 鉄器

### Braeden the Laconic - 静かなるブリーデン

- 内部名: `LEADER_BRAEDEN`
- 属性: 邪悪
- 志向: 無神論志向 / 非力志向 / 金融志向 / 成長志向 / 生産志向 / 大都市志向 / 挽回志向
- 好む社会制度: 農地改革
- 好む遺産: 竜骨の宮殿
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 宗教法

### Dumannios - デュマンニオス

- 内部名: `LEADER_DUMANNIOS`
- 属性: 邪悪
- 志向: 無神論志向 / 金融志向 / 詠唱志向 / 氷の達人
- 好む社会制度: 対外貿易
- 好む遺産: 竜骨の宮殿
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 100

### Riuros - リウロス

- 内部名: `LEADER_RIUROS`
- 属性: 邪悪
- 志向: 無神論志向 / カリスマ志向 / 強化志向 / 氷の達人
- 好む社会制度: 対外貿易
- 好む遺産: 竜骨の宮殿
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 魔術

### Anagantios - アナガンティオス

- 内部名: `LEADER_ANAGANTIOS`
- 属性: 邪悪
- 志向: 無神論志向 / 組織志向 / 預言志向 / 氷の達人
- 好む社会制度: 対外貿易
- 好む遺産: 竜骨の宮殿
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 聖職

### Raitlor - レイトロール

- 内部名: `LEADER_RAITLOR`
- 属性: 中立
- 志向: 無神論志向 / 秘術志向 / 交易志向 / 氷の達人
- 好む社会制度: 対外貿易
- 好む遺産: 竜骨の宮殿
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 筆記

### M.A. - M.A.

- 内部名: `LEADER_NIRAIKANAI_MA`
- 属性: 善良
- 志向: 拡張志向 / 探求志向 / 不屈
- 好む社会制度: 奴隷解放
- 好む遺産: アレクサンドリア図書館
- 宗教の重視度: 緑葉の同胞 iWeightModifier=80 / 深海の旧支配者 iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=-99 / 至光なる天空 iWeightModifier=80 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 15
  - `iTechTradeKnownPercent`: 5
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 30
  - `iAltarVictoryWeight`: 25
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iReligionVictoryWeight`: 20
  - `iMaxWarNearbyPowerRatio`: 120
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 4
  - `iLimitedWarPowerRatio`: 90
  - `iBaseAttackOddsChange`: 1
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 2
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 動物の馴致
  - `FavoriteUnitCombat`: 動物ユニット

### Tina - ティナ

- 内部名: `LEADER_NIRAIKANAI_TINA`
- 属性: 善良
- 志向: 哲学志向 / 警邏志向 / 不屈
- 好む社会制度: 奴隷解放
- 好む遺産: エルヴェの塔
- 宗教の重視度: 緑葉の同胞 iWeightModifier=80 / 深海の旧支配者 iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=-99 / 至光なる天空 iWeightModifier=80 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 3
  - `iMaxGoldPerTurnTradePercent`: 5
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 45
  - `iAltarVictoryWeight`: 30
  - `iConquestVictoryWeight`: 15
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 120
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 4
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 1
  - `iVassalPowerModifier`: 50
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 動物の馴致
  - `FavoriteUnitCombat`: 動物ユニット

### Lisa - リーザ

- 内部名: `LEADER_NIRAIKANAI_LISA`
- 属性: 善良
- 志向: 成長志向 / 蒐集志向 / 挽回志向
- 好む社会制度: 農地改革
- 好む遺産: シロナの祭殿
- 宗教の重視度: 緑葉の同胞 iWeightModifier=80 / 深海の旧支配者 iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=-99 / 至光なる天空 iWeightModifier=80 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 15
  - `iTechTradeKnownPercent`: 5
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 30
  - `iAltarVictoryWeight`: 25
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iReligionVictoryWeight`: 20
  - `iMaxWarNearbyPowerRatio`: 120
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 4
  - `iLimitedWarPowerRatio`: 90
  - `iBaseAttackOddsChange`: 1
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 2
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 動物の馴致
  - `FavoriteUnitCombat`: 動物ユニット

### Sendak - センダック

- 内部名: `LEADER_NIRAIKANAI_SENDAK`
- 属性: 善良
- 志向: 万能志向 / 成長志向 / 挽回志向
- 好む社会制度: 農地改革
- 好む遺産: 労働者ギルド
- 宗教の重視度: 緑葉の同胞 iWeightModifier=80 / 深海の旧支配者 iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=-99 / 至光なる天空 iWeightModifier=80 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 15
  - `iTechTradeKnownPercent`: 5
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 30
  - `iAltarVictoryWeight`: 25
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iReligionVictoryWeight`: 20
  - `iMaxWarNearbyPowerRatio`: 120
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 4
  - `iLimitedWarPowerRatio`: 90
  - `iBaseAttackOddsChange`: 1
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 2
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 動物の馴致
  - `FavoriteUnitCombat`: 動物ユニット

### Terry the Dragon Slayer - 竜殺しのテリー

- 内部名: `LEADER_NIRAIKANAI_TERRY`
- 属性: 善良
- 志向: 成長志向 / 強欲志向 / 悋気志向
- 好む社会制度: 農地改革
- 好む遺産: 天球の羅針盤
- 宗教の重視度: 緑葉の同胞 iWeightModifier=80 / 至光なる天空 iWeightModifier=80 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 15
  - `iTechTradeKnownPercent`: 5
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 30
  - `iAltarVictoryWeight`: 25
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iReligionVictoryWeight`: 20
  - `iMaxWarNearbyPowerRatio`: 120
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 4
  - `iLimitedWarPowerRatio`: 90
  - `iBaseAttackOddsChange`: 1
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 2
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 動物の馴致
  - `FavoriteUnitCombat`: 動物ユニット

### Leakage Arrow - リーケッジ・アロー

- 内部名: `LEADER_NIRAIKANAI_LEAKAGE`
- 属性: 善良
- 志向: 宗教志向 / 農耕志向 / 挽回志向 / 大地の達人
- 好む社会制度: 奴隷解放
- 好む遺産: レウケティオスのアトリエ
- 宗教の重視度: 緑葉の同胞 iWeightModifier=80 / 深海の旧支配者 iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=-99 / 至光なる天空 iWeightModifier=80 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 3
  - `iMaxGoldPerTurnTradePercent`: 5
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 45
  - `iAltarVictoryWeight`: 30
  - `iConquestVictoryWeight`: 15
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 120
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 4
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 1
  - `iVassalPowerModifier`: 50
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 聖職
  - `FavoriteUnitCombat`: 信奉ユニット

### The Dark - 常闇ノ魔女

- 内部名: `LEADER_DARK`
- 属性: 邪悪
- 志向: 宗教志向 / 詠唱志向 / 蛮族志向 / 次元の達人
- 好む社会制度: 弱肉強食
- 好む遺産: 天球の羅針盤
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: エススの枢密院 iWeightModifier=-99 / 緑葉の同胞 iWeightModifier=-99 / 深海の旧支配者 / キルモフのルーン iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=99 / 至光なる天空 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 30
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iVassalPowerModifier`: 80
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: エーテルの知識
  - `FavoriteUnitCombat`: 秘術ユニット

### Professor - 教授

- 内部名: `LEADER_PROFESSOR`
- 属性: 邪悪
- 志向: カリスマ志向 / 召喚志向 / 不世出志向 / 混沌の達人
- 好む社会制度: 弱肉強食
- 好む遺産: 創造の酒造
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: エススの枢密院 / 緑葉の同胞 iWeightModifier=-50 / 深海の旧支配者 / キルモフのルーン iWeightModifier=-50 / 蒼褪めたヴェール iWeightModifier=80 / 至光なる天空 iWeightModifier=-50 / 秩序の修道会 iWeightModifier=-50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 3
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 5
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 30
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 90
  - `iVassalPowerModifier`: 50
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 魔術
  - `FavoriteUnitCombat`: 秘術ユニット

### Avatar of Siva - シヴァの化身

- 内部名: `LEADER_OMAEMONA`
- 属性: 邪悪
- 志向: 宗教志向 / 軍事志向 / 狂信志向
- 好む社会制度: カースト制
- 好む遺産: テンポランス神殿
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: 緑葉の同胞 iWeightModifier=-99 / 深海の旧支配者 iWeightModifier=40 / 蒼褪めたヴェール iWeightModifier=90 / エススの枢密院 iWeightModifier=50 / 至光なる天空 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 7
  - `iTechTradeKnownPercent`: 60
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 45
  - `iMaxWarNearbyPowerRatio`: 120
  - `iMaxWarDistantPowerRatio`: 100
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 120
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 10
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 鉄器
  - `FavoriteUnitCombat`: 信奉ユニット

### Warload Sturm - 猛将シュトゥルム

- 内部名: `LEADER_GIKO_HANYAAN`
- 属性: 邪悪
- 志向: 侵掠志向 / 迅速志向 / 戦争狂志向
- 好む社会制度: 軍需優先
- 好む遺産: アウレウスの竈
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 40
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 110
  - `iBaseAttackOddsChange`: 10
  - `iVassalPowerModifier`: 50
  - `iEconomyTechValue`: 100

### Instigator of hypocrisy - 偽善の扇動者

- 内部名: `LEADER_MORALER`
- 属性: 邪悪
- 志向: 勤労志向 / 建設志向 / 遺産狂志向
- 好む社会制度: 宗教主義
- 好む遺産: マーキュリアンの門
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: エススの枢密院 iWeightModifier=-99 / 緑葉の同胞 iWeightModifier=-99 / 深海の旧支配者 / キルモフのルーン iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=100 / 至光なる天空 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 30
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iVassalPowerModifier`: 80
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: エーテルの知識
  - `FavoriteUnitCombat`: 弓術ユニット

### King of the intuition - 直観の王君

- 内部名: `LEADER_HAGURUMA_OH`
- 属性: 邪悪
- 志向: 預言志向 / 生産志向 / 無機質志向
- 好む社会制度: ギルド制
- 好む遺産: ギルド・オブ・ハンマーズ
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: エススの枢密院 / 緑葉の同胞 iWeightModifier=-50 / 深海の旧支配者 / キルモフのルーン iWeightModifier=-50 / 蒼褪めたヴェール iWeightModifier=80 / 至光なる天空 iWeightModifier=-50 / 秩序の修道会 iWeightModifier=-50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 3
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 5
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 30
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 90
  - `iVassalPowerModifier`: 50
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 魔術

### Reah - レア

- 内部名: `LEADER_REAH`
- 属性: 善良
- 志向: 適応志向 / 軍事志向
- 好む社会制度: 神権政治
- 好む遺産: アレクサンドリア図書館
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=-50 / エススの枢密院 iWeightModifier=-50 / 緑葉の同胞 / キルモフのルーン / 深海の旧支配者 iWeightModifier=-50 / 至光なる天空 iWeightModifier=20 / 秩序の修道会 iWeightModifier=75 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 7
  - `iNoTechTradeThreshold`: 7
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 9
  - `iCultureVictoryWeight`: 25
  - `iAltarVictoryWeight`: 45
  - `iConquestVictoryWeight`: 10
  - `iDominationVictoryWeight`: 15
  - `iReligionVictoryWeight`: 55
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 110
  - `iVassalPowerModifier`: 30
  - `iFreedomAppreciation`: 3
  - `TemporaryTraits`: 拡張志向
  - `bFemale`: 1
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 筆記
  - `FavoriteUnitCombat`: 白兵ユニット

### Feena - フィーナ

- 内部名: `LEADER_FEENA`
- 属性: 善良
- 志向: 適応志向 / 徴税志向 / 大都市志向
- 好む社会制度: 自由主義
- 好む遺産: 夢の劇場
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=-50 / エススの枢密院 iWeightModifier=-10 / 深海の旧支配者 iWeightModifier=-10 / 至光なる天空 iWeightModifier=30 / 秩序の修道会 iWeightModifier=10 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 8
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 5
  - `iCultureVictoryWeight`: 70
  - `iTowerVictoryWeight`: 15
  - `iAltarVictoryWeight`: 50
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iLimitedWarPowerRatio`: 80
  - `iVassalPowerModifier`: 25
  - `iFreedomAppreciation`: 1
  - `TemporaryTraits`: 建設志向
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 交易
  - `FavoriteUnitCombat`: 白兵ユニット

### Fleurette - フローレット

- 内部名: `LEADER_FLEURETTE`
- 属性: 善良
- 志向: TXT_KEY_TRAIT_IMPERIALIST / 将官志向 / 退魔志向
- 好む社会制度: カースト制
- 好む遺産: ティターンの巨像
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=-50 / エススの枢密院 iWeightModifier=-50 / 緑葉の同胞 iWeightModifier=-50 / キルモフのルーン iWeightModifier=-50 / 深海の旧支配者 iWeightModifier=75 / 至光なる天空 iWeightModifier=20 / 秩序の修道会 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 9
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 8
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 15
  - `iAltarVictoryWeight`: 15
  - `iConquestVictoryWeight`: 55
  - `iDominationVictoryWeight`: 45
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 60
  - `iLimitedWarPowerRatio`: 120
  - `iBaseAttackOddsChange`: 3
  - `iVassalPowerModifier`: 35
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 教育
  - `FavoriteUnitCombat`: 白兵ユニット

### Jahl - ヤール

- 内部名: `LEADER_JAHL`
- 属性: 善良
- 志向: 突撃志向 / 万能志向 / 殉死志向
- 好む社会制度: カースト制
- 好む遺産: ティターンの巨像
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=-50 / キルモフのルーン iWeightModifier=10 / 至光なる天空 iWeightModifier=20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 9
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 8
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 15
  - `iAltarVictoryWeight`: 15
  - `iConquestVictoryWeight`: 55
  - `iDominationVictoryWeight`: 45
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 3
  - `iVassalPowerModifier`: 35
  - `iFreedomAppreciation`: 10
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 教育
  - `FavoriteUnitCombat`: 騎乗ユニット

### Lise - リーゼ

- 内部名: `LEADER_LISE`
- 属性: 善良
- 志向: 勤労志向 / 詠唱志向 / 挽回志向 / 影の達人
- 好む社会制度: 神権政治
- 好む遺産: レウケティオスのアトリエ
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: エススの枢密院 iWeightModifier=50 / 緑葉の同胞 iWeightModifier=-80 / 深海の旧支配者 iWeightModifier=20 / 蒼褪めたヴェール iWeightModifier=99 / 至光なる天空 iWeightModifier=-30 / 秩序の修道会 iWeightModifier=-80 / キルモフのルーン iWeightModifier=-30 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 40
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 50
  - `bFemale`: 1
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 筆記
  - `FavoriteUnitCombat`: 騎乗ユニット

### Gerd the White witch - 白き魔女ゲルド

- 内部名: `LEADER_GERD`
- 属性: 中立
- 志向: 秘術志向 / 強化志向 / 水の達人
- 好む社会制度: カースト制
- 好む遺産: エルヴェの塔
- 宗教の重視度: 深海の旧支配者 iWeightModifier=80 / 至光なる天空 iWeightModifier=80 / 秩序の修道会 iWeightModifier=10 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 9
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 8
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 15
  - `iAltarVictoryWeight`: 15
  - `iConquestVictoryWeight`: 55
  - `iDominationVictoryWeight`: 45
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 3
  - `iVassalPowerModifier`: 35
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 教育
  - `FavoriteUnitCombat`: 秘術ユニット

### Olivier - オリビエ

- 内部名: `LEADER_OLIVIER`
- 属性: 善良
- 志向: 金融志向 / 話術志向 / 魔法抵抗志向 / 愚鈍志向 / 幻術志向 / 悋気志向 / 早熟志向
- 好む社会制度: カースト制
- 好む遺産: 夢の劇場
- 宗教の重視度: 深海の旧支配者 iWeightModifier=80 / 至光なる天空 iWeightModifier=80 / 秩序の修道会 iWeightModifier=10 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 9
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 8
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 15
  - `iAltarVictoryWeight`: 15
  - `iConquestVictoryWeight`: 55
  - `iDominationVictoryWeight`: 45
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 3
  - `iVassalPowerModifier`: 35
  - `iFreedomAppreciation`: 10
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 教育

### Uesugi Kenshin - 上杉謙信

- 内部名: `LEADER_KENSHIN`
- 属性: 善良
- 志向: 無神論志向 / 迅速志向 / 突撃志向 / 退魔志向
- 好む社会制度: 現人神制
- 好む遺産: 創造の酒造
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 40
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 55
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 80
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 30
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 鐙
  - `FavoriteUnitCombat`: 騎乗ユニット

### Naoe Yamashiro no Kami - 直江山城守

- 内部名: `LEADER_NAOE`
- 属性: 中立
- 志向: 無神論志向 / 勤労志向 / 将官志向 / 工夫志向
- 好む社会制度: 貴族制
- 好む遺産: 労働者ギルド
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 9
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 150
  - `iMaxWarDistantPowerRatio`: 100
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 30
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 80
  - `FavoriteTech`: 通貨
  - `FavoriteUnitCombat`: 白兵ユニット

### Naoe Kagetsuna - 直江景綱

- 内部名: `LEADER_KAGETSUNA`
- 属性: 善良
- 志向: 無神論志向 / 宗教志向 / 迅速志向 / 魔法抵抗志向
- 好む社会制度: 奴隷解放
- 好む遺産: 国王記念館
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 15
  - `iTechTradeKnownPercent`: 5
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 4
  - `iLimitedWarPowerRatio`: 90
  - `iBaseAttackOddsChange`: 1
  - `iVassalPowerModifier`: 40
  - `iFreedomAppreciation`: 2
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 動物の馴致
  - `FavoriteUnitCombat`: 信奉ユニット

### Kakizaki Kageie - 柿崎景家

- 内部名: `LEADER_KAKIZAKI`
- 属性: 善良
- 志向: 無神論志向 / 迅速志向 / 軍事志向
- 好む社会制度: 貴族制
- 好む遺産: 三圃組合
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 40
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 55
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 80
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 30
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 鐙
  - `FavoriteUnitCombat`: 騎乗ユニット

### Usami Suruganokami Sadamitsu - 宇佐美駿河守定満

- 内部名: `LEADER_USAMI`
- 属性: 善良
- 志向: 無神論志向 / 迅速志向 / 野戦志向
- 好む社会制度: 貴族制
- 好む遺産: 三圃組合
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 40
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 55
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 80
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 30
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 鐙
  - `FavoriteUnitCombat`: 騎乗ユニット

### Amakasu Kagemochi - 甘粕景持

- 内部名: `LEADER_AMAKASU`
- 属性: 中立
- 志向: 無神論志向 / 迅速志向 / 蒐集志向
- 好む社会制度: 貴族制
- 好む遺産: 三圃組合
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 9
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 150
  - `iMaxWarDistantPowerRatio`: 100
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 30
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 80
  - `FavoriteTech`: 通貨
  - `FavoriteUnitCombat`: 白兵ユニット

### Soma Katra - ソーマ・カトラ

- 内部名: `LEADER_KATRA`
- 属性: 邪悪
- 志向: 秘術志向 / 徴税志向 / 死の達人
- 好む社会制度: 奴隷制
- 好む遺産: アレクサンドリア図書館
- 宗教の重視度: エススの枢密院 iWeightModifier=80 / 緑葉の同胞 iWeightModifier=-20 / 深海の旧支配者 iWeightModifier=20 / キルモフのルーン iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=20 / 至光なる天空 iWeightModifier=-90 / 秩序の修道会 iWeightModifier=-90 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 7
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 50
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 20
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 110
  - `iBaseAttackOddsChange`: 2
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 屍霊術

### Soma Teraza - ソーマ・テラザ

- 内部名: `LEADER_TERAZA`
- 属性: 邪悪
- 志向: 哲学志向 / 預言志向 / 屍人志向 / 不可逆の達人
- 好む社会制度: 奴隷制
- 好む遺産: 八魔陣
- 宗教の重視度: エススの枢密院 iWeightModifier=80 / 緑葉の同胞 iWeightModifier=-20 / 深海の旧支配者 / キルモフのルーン iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=20 / 至光なる天空 iWeightModifier=-60 / 秩序の修道会 iWeightModifier=-90 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 110
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: -20
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 屍霊術
  - `FavoriteUnitCombat`: 白兵ユニット

### Robert Thorne - ロバート・ソーン

- 内部名: `LEADER_ROBERT`
- 属性: 邪悪
- 志向: 話術志向 / 蒐集志向 / 屍人志向
- 好む社会制度: 奴隷制
- 好む遺産: モッカの大釜
- 宗教の重視度: エススの枢密院 iWeightModifier=80 / 緑葉の同胞 iWeightModifier=-20 / 深海の旧支配者 iWeightModifier=80 / キルモフのルーン iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=20 / 至光なる天空 iWeightModifier=-90 / 秩序の修道会 iWeightModifier=-90 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 50
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 20
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 90
  - `iVassalPowerModifier`: -20
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 屍霊術
  - `FavoriteUnitCombat`: 白兵ユニット

### Richard Thorne - リチャード・ソーン

- 内部名: `LEADER_RICHARD`
- 属性: 邪悪
- 志向: 哲学志向 / 伝道志向 / 屍人志向
- 好む社会制度: 奴隷制
- 好む遺産: モッカの大釜
- 宗教の重視度: エススの枢密院 iWeightModifier=80 / 緑葉の同胞 iWeightModifier=-20 / 深海の旧支配者 iWeightModifier=80 / キルモフのルーン iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=20 / 至光なる天空 iWeightModifier=-90 / 秩序の修道会 iWeightModifier=-90 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 7
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 50
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 20
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 110
  - `iBaseAttackOddsChange`: 2
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 屍霊術
  - `FavoriteUnitCombat`: 白兵ユニット

### Darsk - ダースク

- 内部名: `LEADER_DARSK`
- 属性: 邪悪
- 志向: 蒐集志向 / 徴税志向
- 好む社会制度: 奴隷制
- 好む遺産: 鼠捕りギルド
- 宗教の重視度: エススの枢密院 iWeightModifier=80 / 緑葉の同胞 iWeightModifier=-20 / 深海の旧支配者 iWeightModifier=20 / キルモフのルーン iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=20 / 至光なる天空 iWeightModifier=-90 / 秩序の修道会 iWeightModifier=-90 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 7
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 50
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 20
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 110
  - `iBaseAttackOddsChange`: 2
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 屍霊術
  - `FavoriteUnitCombat`: 白兵ユニット

### Sherlalaque - シェーララク

- 内部名: `LEADER_SHERLALAQUE`
- 属性: 邪悪
- 志向: 拡張志向 / 賢人志向
- 好む社会制度: 奴隷制
- 好む遺産: ワイアーム砦
- 宗教の重視度: エススの枢密院 iWeightModifier=80 / 緑葉の同胞 iWeightModifier=-20 / 深海の旧支配者 iWeightModifier=80 / キルモフのルーン iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=20 / 至光なる天空 iWeightModifier=-90 / 秩序の修道会 iWeightModifier=-90 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 7
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 50
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 20
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 110
  - `iBaseAttackOddsChange`: 2
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 屍霊術
  - `FavoriteUnitCombat`: 白兵ユニット

### Yenoiah Golgotha - イェノイア・ゴルゴダ

- 内部名: `LEADER_YENOIAH`
- 属性: 邪悪
- 志向: 秘術志向 / 探求志向 / 超魔術の達人
- 好む社会制度: カースト制
- 好む遺産: 魂の溶鉱炉
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: 緑葉の同胞 iWeightModifier=-99 / キルモフのルーン iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=75 / 至光なる天空 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 50
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 20
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 30
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 100
  - `iVassalPowerModifier`: 10
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 魔術

### Ladibarre de Sable - ラディバール・ド・サブレ

- 内部名: `LEADER_LADIBARRE`
- 属性: 邪悪
- 志向: 哲学志向 / 宗教志向 / 幻術志向
- 好む社会制度: カースト制
- 好む遺産: 魂の溶鉱炉
- 宗教の重視度: 緑葉の同胞 iWeightModifier=-99 / キルモフのルーン iWeightModifier=-99 / 深海の旧支配者 iWeightModifier=80 / 蒼褪めたヴェール iWeightModifier=40 / 至光なる天空 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 70
  - `iConquestVictoryWeight`: 5
  - `iDominationVictoryWeight`: 10
  - `iReligionVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 70
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 100
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 神学

### Hydor Argyros - ヒュドール・アルギュロス

- 内部名: `LEADER_ARGYROS`
- 属性: 邪悪
- 志向: 組織志向 / 詠唱志向 / 魔法抵抗志向
- 好む社会制度: カースト制
- 好む遺産: 魂の溶鉱炉
- 宗教の重視度: 緑葉の同胞 iWeightModifier=-99 / 深海の旧支配者 iWeightModifier=80 / 蒼褪めたヴェール iWeightModifier=20 / エススの枢密院 iWeightModifier=20 / 至光なる天空 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 7
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 45
  - `iMaxWarNearbyPowerRatio`: 120
  - `iMaxWarDistantPowerRatio`: 100
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 100
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 10
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 鉄器

### Goly the godhand - ゴリィー・ザ・ゴッドハンド

- 内部名: `LEADER_GOLY`
- 属性: 邪悪
- 志向: 暗愚志向 / 金融志向
- 好む社会制度: カースト制
- 好む遺産: 魂の溶鉱炉
- 宗教の重視度: 深海の旧支配者 iWeightModifier=60 / 緑葉の同胞 iWeightModifier=-99 / キルモフのルーン iWeightModifier=-99 / 至光なる天空 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 15
  - `iMaxGoldPerTurnTradePercent`: 15
  - `iCultureVictoryWeight`: 40
  - `iTowerVictoryWeight`: 35
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 100
  - `iFreedomAppreciation`: 10
  - `TemporaryTraits`: 探求志向 / 強欲志向
  - `bFemale`: 1
  - `iEconomyTechValue`: 120

### Arsine Bismuth - アルシン・ビスミュス

- 内部名: `LEADER_ARSINE`
- 属性: 邪悪
- 志向: 召喚志向 / 探求志向 / 触死志向
- 好む社会制度: カースト制
- 好む遺産: 魂の溶鉱炉
- 宗教の重視度: 深海の旧支配者 iWeightModifier=60 / 緑葉の同胞 iWeightModifier=-99 / キルモフのルーン iWeightModifier=-99 / 至光なる天空 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 15
  - `iMaxGoldPerTurnTradePercent`: 15
  - `iCultureVictoryWeight`: 40
  - `iTowerVictoryWeight`: 35
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 100
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 120

### Pzev Dar Gyros - プゼヴ・ダル・ギュロス

- 内部名: `LEADER_PZEVDARGYROS`
- 属性: 邪悪
- 志向: 詠唱志向 / 賢人志向 / 死の達人
- 好む社会制度: カースト制
- 好む遺産: 魂の溶鉱炉
- 宗教の重視度: 深海の旧支配者 iWeightModifier=60 / 緑葉の同胞 iWeightModifier=-99 / キルモフのルーン iWeightModifier=-99 / 至光なる天空 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 15
  - `iMaxGoldPerTurnTradePercent`: 15
  - `iCultureVictoryWeight`: 40
  - `iTowerVictoryWeight`: 35
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 100
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 120

### Baldwin de Maris - ボールドウィン・ド・マリス

- 内部名: `LEADER_MARIS`
- 属性: 善良
- 志向: 無神論志向 / 攻撃志向 / 防御志向 / 復讐志向
- 好む社会制度: 共和制
- 好む遺産: ネクサス
- 宗教の重視度: 秩序の修道会 iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / エススの枢密院 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 7
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 50
  - `iMaxWarDistantPowerRatio`: 100
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 120
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 鉄器
  - `FavoriteUnitCombat`: 白兵ユニット

### Neustadt Leord - ノイシュタット・レオード

- 内部名: `LEADER_LEORD`
- 属性: 善良
- 志向: 無神論志向 / TXT_KEY_TRAIT_IMPERIALIST / 話術志向
- 好む社会制度: 共和制
- 好む遺産: ネクサス
- 宗教の重視度: 秩序の修道会 iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / エススの枢密院 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 5
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 75
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 40
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 狂信
  - `FavoriteUnitCombat`: 信奉ユニット

### Georistalpehn - ジョリスターペン

- 内部名: `LEADER_GEORISTALPEHN`
- 属性: 善良
- 志向: 無神論志向 / 宗教志向 / 万能志向
- 好む社会制度: 共和制
- 好む遺産: ネクサス
- 宗教の重視度: 秩序の修道会 iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / エススの枢密院 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 7
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 45
  - `iMaxWarNearbyPowerRatio`: 40
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 狂信
  - `FavoriteUnitCombat`: 信奉ユニット

### Carse - カース

- 内部名: `LEADER_CARSE`
- 属性: 中立
- 志向: 適応志向 / 侵掠志向
- 好む社会制度: 国民国家
- 好む遺産: 物見の塔
- 宗教の重視度: 秩序の修道会 iWeightModifier=-99 / 緑葉の同胞 iWeightModifier=-99 / エススの枢密院 iWeightModifier=100 / 深海の旧支配者 iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 15
  - `iAltarVictoryWeight`: 15
  - `iConquestVictoryWeight`: 55
  - `iDominationVictoryWeight`: 45
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 50
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `TemporaryTraits`: 防御志向
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 複合弓
  - `FavoriteUnitCombat`: 弓術ユニット

### Diana - ディアナ

- 内部名: `LEADER_DIANA`
- 属性: 善良
- 志向: 哲学志向 / 金融志向
- 好む社会制度: 共和制
- 好む遺産: 鼠捕りギルド
- 宗教の重視度: エススの枢密院 iWeightModifier=-99 / 深海の旧支配者 iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=-99 / 至光なる天空 iWeightModifier=75 / 秩序の修道会 iWeightModifier=40 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 10
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 25
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 55
  - `iMaxWarNearbyPowerRatio`: 50
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 40
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 80
  - `FavoriteTech`: 通貨

### Ching Yamamoto - 山本沈愚

- 内部名: `LEADER_YAMAMOTO`
- 属性: 中立
- 志向: 拡張志向 / 突撃志向 / 脳筋志向
- 好む社会制度: 軍需優先
- 好む遺産: ティターンの巨像
- 宗教の重視度: 深海の旧支配者 iWeightModifier=-99 / 蒼褪めたヴェール iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 5
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 75
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 20
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 20
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteUnitCombat`: 白兵ユニット

### Hianthrogh - ヒアンスローフ

- 内部名: `LEADER_HIANTHROGH`
- 属性: 善良
- 志向: 防御志向 / 警邏志向 / 魔法抵抗志向
- 好む社会制度: 対外貿易
- 好む遺産: 聖者の偶像
- 宗教の重視度: 秩序の修道会 iWeightModifier=10 / 至光なる天空 iWeightModifier=90 / キルモフのルーン iWeightModifier=50 / 深海の旧支配者 iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 35
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 35
  - `iConquestVictoryWeight`: 5
  - `iDominationVictoryWeight`: 10
  - `iReligionVictoryWeight`: 40
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 70
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 名誉

### Khset - クゥセット

- 内部名: `LEADER_KHSET`
- 属性: 善良
- 志向: 農耕志向 / 生産志向
- 好む社会制度: 対外貿易
- 好む遺産: 聖者の偶像
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=-99 / 深海の旧支配者 iWeightModifier=-20 / 緑葉の同胞 iWeightModifier=10 / キルモフのルーン iWeightModifier=50 / 至光なる天空 iWeightModifier=90 / 秩序の修道会 iWeightModifier=10 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 60
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 45
  - `iAltarVictoryWeight`: 30
  - `iConquestVictoryWeight`: 15
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 110
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 100
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 名誉

### Aminzerugh - アミンゼルフ

- 内部名: `LEADER_AMINZERUGH`
- 属性: 善良
- 志向: 警邏志向 / 交易志向
- 好む社会制度: 対外貿易
- 好む遺産: 聖者の偶像
- 宗教の重視度: 秩序の修道会 iWeightModifier=10 / 至光なる天空 iWeightModifier=90 / キルモフのルーン iWeightModifier=50 / 深海の旧支配者 iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 10
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 50
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 35
  - `iReligionVictoryWeight`: 20
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 120
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 名誉
  - `FavoriteUnitCombat`: 弓術ユニット

### Marst - マルスト

- 内部名: `LEADER_MARST`
- 属性: 善良
- 志向: 拡張志向 / 伝道志向
- 好む社会制度: 対外貿易
- 好む遺産: 聖者の偶像
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=-99 / 深海の旧支配者 iWeightModifier=-20 / 緑葉の同胞 iWeightModifier=10 / キルモフのルーン iWeightModifier=50 / 至光なる天空 iWeightModifier=90 / 秩序の修道会 iWeightModifier=10 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 80
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 35
  - `iConquestVictoryWeight`: 15
  - `iDominationVictoryWeight`: 15
  - `iReligionVictoryWeight`: 50
  - `iMaxWarNearbyPowerRatio`: 110
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 140
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 名誉
  - `FavoriteUnitCombat`: 信奉ユニット

### Sacchathroghn - サッカスローン

- 内部名: `LEADER_SACCHATHROGHN`
- 属性: 善良
- 志向: 農耕志向 / 商才志向
- 好む社会制度: 対外貿易
- 好む遺産: 聖者の偶像
- 宗教の重視度: 秩序の修道会 iWeightModifier=10 / 至光なる天空 iWeightModifier=90 / キルモフのルーン iWeightModifier=50 / 深海の旧支配者 iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 50
  - `iTowerVictoryWeight`: 40
  - `iAltarVictoryWeight`: 20
  - `iConquestVictoryWeight`: 5
  - `iDominationVictoryWeight`: 5
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 120
  - `iMaxWarDistantPowerRatio`: 100
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 200
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: -20
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 名誉

### Raffiseruno - ラフィセルノ

- 内部名: `LEADER_RAFFISERUNO`
- 属性: 善良
- 志向: 野戦志向 / 伝道志向
- 好む社会制度: 対外貿易
- 好む遺産: 聖者の偶像
- 宗教の重視度: 秩序の修道会 iWeightModifier=10 / 至光なる天空 iWeightModifier=90 / キルモフのルーン iWeightModifier=50 / 深海の旧支配者 iWeightModifier=-20 / 蒼褪めたヴェール iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 50
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 5
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 5
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 30
  - `iReligionVictoryWeight`: 5
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 40
  - `iLimitedWarPowerRatio`: 90
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 50
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 名誉

### Kolsehvahn - コルセヴァン

- 内部名: `LEADER_KOLSEHVAHN`
- 属性: 邪悪
- 志向: 蒐集志向 / 生産志向
- 好む社会制度: 奴隷制
- 好む遺産: 縛鎖の柱
- 宗教の重視度: 深海の旧支配者 iWeightModifier=10 / エススの枢密院 iWeightModifier=80 / 緑葉の同胞 iWeightModifier=40 / キルモフのルーン iWeightModifier=40 / 至光なる天空 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 55
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 55
  - `iReligionVictoryWeight`: 5
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 30
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 詐欺

### Mihuatl - ミファトル

- 内部名: `LEADER_MIHUATL`
- 属性: 邪悪
- 志向: 秘術志向 / 蒐集志向 / 不可逆の達人
- 好む社会制度: 奴隷制
- 好む遺産: 魂の溶鉱炉
- 宗教の重視度: エススの枢密院 iWeightModifier=25 / 深海の旧支配者 iWeightModifier=80 / 緑葉の同胞 iWeightModifier=10 / キルモフのルーン iWeightModifier=-40 / 至光なる天空 iWeightModifier=-80 / 秩序の修道会 iWeightModifier=-80 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 4
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 5
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 55
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 55
  - `iReligionVictoryWeight`: 5
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 30
  - `iFreedomAppreciation`: 2
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 詐欺

### Ghurovah - グロヴァー

- 内部名: `LEADER_GHUROVAH`
- 属性: 邪悪
- 志向: 侵掠志向 / 強欲志向 / 蛮族志向
- 好む社会制度: 奴隷制
- 好む遺産: 縛鎖の柱
- 宗教の重視度: 深海の旧支配者 iWeightModifier=80 / エススの枢密院 iWeightModifier=20 / 緑葉の同胞 iWeightModifier=40 / 至光なる天空 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 55
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 55
  - `iReligionVictoryWeight`: 5
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 70
  - `iLimitedWarPowerRatio`: 130
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 30
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 詐欺
  - `FavoriteUnitCombat`: 信奉ユニット

### Inveruphu - インベールフ

- 内部名: `LEADER_INVERUPH`
- 属性: 邪悪
- 志向: 攻撃志向 / 建設志向
- 好む社会制度: 奴隷制
- 好む遺産: 縛鎖の柱
- 宗教の重視度: 深海の旧支配者 iWeightModifier=80 / エススの枢密院 iWeightModifier=40 / 緑葉の同胞 iWeightModifier=40 / キルモフのルーン iWeightModifier=-50 / 至光なる天空 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 55
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 55
  - `iReligionVictoryWeight`: 5
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 30
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 詐欺

### Chystaolli - キスタオーリ

- 内部名: `LEADER_CHYSTAOLLI`
- 属性: 邪悪
- 志向: 野戦志向 / 将官志向 / 蛮族志向
- 好む社会制度: 奴隷制
- 好む遺産: 魂の溶鉱炉
- 宗教の重視度: エススの枢密院 iWeightModifier=25 / 深海の旧支配者 iWeightModifier=80 / 緑葉の同胞 iWeightModifier=10 / キルモフのルーン iWeightModifier=-40 / 至光なる天空 iWeightModifier=-80 / 秩序の修道会 iWeightModifier=-80 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 1
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 15
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 55
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 55
  - `iReligionVictoryWeight`: 5
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 110
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: 30
  - `iFreedomAppreciation`: 2
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 詐欺

### Glucoatl - グルコァトル

- 内部名: `LEADER_GLUCOATL`
- 属性: 邪悪
- 志向: 迅速志向 / 警邏志向 / 蛮族志向
- 好む社会制度: 奴隷制
- 好む遺産: 魂の溶鉱炉
- 宗教の重視度: エススの枢密院 iWeightModifier=25 / 深海の旧支配者 iWeightModifier=80 / 緑葉の同胞 iWeightModifier=10 / キルモフのルーン iWeightModifier=-40 / 至光なる天空 iWeightModifier=-80 / 秩序の修道会 iWeightModifier=-80 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 4
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 5
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 55
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 55
  - `iReligionVictoryWeight`: 5
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 30
  - `iFreedomAppreciation`: 2
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 詐欺

### Metatoron - メタトロン

- 内部名: `LEADER_METATORON`
- 属性: 中立
- 志向: 無神論志向 / カリスマ志向 / 侵掠志向 / 工夫志向
- 好む社会制度: 軍事国家
- 好む遺産: 竜の財宝
- 宗教の重視度: 秩序の修道会 iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / エススの枢密院 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 50
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 100
  - `iLimitedWarPowerRatio`: 130
  - `iBaseAttackOddsChange`: 10
  - `iVassalPowerModifier`: 500
  - `iFreedomAppreciation`: 50
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 四大元素

### L'Kbreth - エル'ケブレス

- 内部名: `LEADER_LKBRETH`
- 属性: 中立
- 志向: 無神論志向 / 拡張志向 / 侵掠志向
- 好む社会制度: 大量消費
- 好む遺産: 竜の財宝
- 宗教の重視度: 秩序の修道会 iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / エススの枢密院 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 20
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 10
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 10
  - `iVassalPowerModifier`: 500
  - `iFreedomAppreciation`: 50
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 四大元素

### Bjew the Dragon Master - 竜使いビュウ

- 内部名: `LEADER_BJEW`
- 属性: 中立
- 志向: 無神論志向 / 組織志向 / 軍事志向
- 好む社会制度: 大量消費
- 好む遺産: 九人衆ギルド
- 宗教の重視度: 秩序の修道会 iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / エススの枢密院 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 40
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 10
  - `iVassalPowerModifier`: 500
  - `iFreedomAppreciation`: 50
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 四大元素

### Yahweh the Pillarkeeper - 柱守ヤーヴェ

- 内部名: `LEADER_YAHWEH`
- 属性: 中立
- 志向: 無神論志向 / 創造志向 / 侵掠志向
- 好む社会制度: 軍事国家
- 好む遺産: 竜の財宝
- 宗教の重視度: 秩序の修道会 iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / エススの枢密院 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 40
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 10
  - `iVassalPowerModifier`: 500
  - `iFreedomAppreciation`: 50
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 四大元素

### Astarte the Winged - 有翼のアスタルテ

- 内部名: `LEADER_ASTARTE`
- 属性: 中立
- 志向: 無神論志向 / 弱肉強食志向 / 強欲志向
- 好む社会制度: 大量消費
- 好む遺産: 竜の財宝
- 宗教の重視度: 秩序の修道会 iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / エススの枢密院 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 40
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 10
  - `iVassalPowerModifier`: 500
  - `iFreedomAppreciation`: 50
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 四大元素

### Gehenna - ゲヘナ

- 内部名: `LEADER_GEHENNA`
- 属性: 中立
- 志向: 無神論志向 / カリスマ志向 / 探求志向
- 好む社会制度: 大量消費
- 好む遺産: 竜の財宝
- 宗教の重視度: 秩序の修道会 iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / エススの枢密院 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 1
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 15
  - `iMaxGoldPerTurnTradePercent`: 7
  - `iTowerVictoryWeight`: 35
  - `iConquestVictoryWeight`: 30
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 100
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 130
  - `iBaseAttackOddsChange`: 10
  - `iVassalPowerModifier`: 500
  - `iFreedomAppreciation`: 50
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteTech`: 四大元素

### Verocchio - ヴェロッキオ

- 内部名: `LEADER_VEROCCHIO`
- 属性: 中立
- 志向: 無神論志向 / 勤労志向 / 哲学志向 / 工夫志向
- 好む社会制度: 対外貿易
- 好む遺産: 労働者ギルド
- 宗教の重視度: 秩序の修道会 iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / エススの枢密院 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 機械

### Maer - メイヤー

- 内部名: `LEADER_MAER`
- 属性: 中立
- 志向: 無神論志向 / カリスマ志向 / 勤労志向
- 好む社会制度: 国民国家
- 好む遺産: アレクサンドリア図書館
- 宗教の重視度: 秩序の修道会 iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / エススの枢密院 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteUnitCombat`: 弓術ユニット

### Metal Wolf - メタルヴォルフ

- 内部名: `LEADER_METALWOLF`
- 属性: 中立
- 志向: 無神論志向 / 攻撃志向 / 突撃志向 / 不屈
- 好む社会制度: 軍事国家
- 好む遺産: ギルド・オブ・ハンマーズ
- 宗教の重視度: 秩序の修道会 iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / エススの枢密院 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 機械

### Raiden - ライデン

- 内部名: `LEADER_RAIDEN`
- 属性: 中立
- 志向: 無神論志向 / 勤労志向 / 生産志向
- 好む社会制度: 軍事国家
- 好む遺産: 労働者ギルド
- 宗教の重視度: 秩序の修道会 iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / エススの枢密院 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 機械

### Atman - アートマン

- 内部名: `LEADER_ATMAN`
- 属性: 邪悪
- 志向: 無神論志向 / 哲学志向 / 建設志向 / 工夫志向
- 好む社会制度: 対外貿易
- 好む遺産: ヴェルギュールの強欲
- 宗教の重視度: 秩序の修道会 iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / エススの枢密院 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 機械

### Amazigh - アマジーグ

- 内部名: `LEADER_AMAZIGH`
- 属性: 中立
- 志向: 無神論志向 / 攻撃志向 / 警邏志向
- 好む社会制度: 国民国家
- 好む遺産: 問い掛けるものの石像
- 宗教の重視度: 秩序の修道会 iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / エススの枢密院 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteUnitCombat`: 弓術ユニット

### Risen Emperor - 上帝

- 内部名: `LEADER_RISEN_EMPEROR`
- 属性: 中立
- 志向: カリスマ志向 / 秘術志向 / 無神論志向 / 魂の達人
- 好む社会制度: 現人神制
- 好む遺産: 空の霊廟
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 5
  - `iVassalPowerModifier`: 50
  - `iFreedomAppreciation`: 50
  - `iEconomyTechValue`: 120

### Korinna the Protector - 守護者コリンナ

- 内部名: `LEADER_KORRINA`
- 属性: 中立
- 志向: 攻撃志向 / カリスマ志向 / 早熟志向
- 好む社会制度: 現人神制
- 好む遺産: 空の霊廟
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=-20 / エススの枢密院 iWeightModifier=10 / 秩序の修道会 iWeightModifier=-20 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 30
  - `iAltarVictoryWeight`: 20
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 40
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 5
  - `iVassalPowerModifier`: 50
  - `iFreedomAppreciation`: 50
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteUnitCombat`: 白兵ユニット

### Ophelia - オフェリア

- 内部名: `LEADER_OPHELIA`
- 属性: 中立
- 志向: 無神論志向 / 強化志向 / 万能志向 / 触死志向
- 好む社会制度: 現人神制
- 好む遺産: 魂の溶鉱炉
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 30
  - `iAltarVictoryWeight`: 20
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 40
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 5
  - `iVassalPowerModifier`: 50
  - `iFreedomAppreciation`: 50
  - `bFemale`: 1
  - `iEconomyTechValue`: 120

### Xivan - シーヴァン

- 内部名: `LEADER_XIVAN`
- 属性: 邪悪
- 志向: カリスマ志向 / 話術志向
- 好む社会制度: 現人神制
- 好む遺産: 縛鎖の柱
- 宗教の重視度: エススの枢密院 iWeightModifier=-99 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 90
  - `iVassalPowerModifier`: -20
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 120
  - `FavoriteUnitCombat`: 信奉ユニット

### Nero - ネロ

- 内部名: `LEADER_NERO`
- 属性: 邪悪
- 志向: 徴税志向 / 拡張志向
- 好む社会制度: 共和制
- 好む遺産: 国王記念館
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=-90 / 深海の旧支配者 iWeightModifier=-30 / エススの枢密院 iWeightModifier=30 / キルモフのルーン iWeightModifier=20 / 至光なる天空 iWeightModifier=10 / 秩序の修道会 iWeightModifier=80 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 40
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 30
  - `iAltarVictoryWeight`: 20
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 40
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 110
  - `iMaxWarDistantPowerRatio`: 80
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 100
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 120

### Tiberius - ティベリウス

- 内部名: `LEADER_TIBERIUS`
- 属性: 善良
- 志向: 組織志向 / 拡張志向
- 好む社会制度: 共和制
- 好む遺産: テンポランス神殿
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=-90 / 深海の旧支配者 iWeightModifier=-30 / エススの枢密院 iWeightModifier=30 / キルモフのルーン iWeightModifier=20 / 至光なる天空 iWeightModifier=10 / 秩序の修道会 iWeightModifier=80 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 40
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 30
  - `iAltarVictoryWeight`: 20
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 40
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 110
  - `iMaxWarDistantPowerRatio`: 80
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 100
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 120

### Ekhlo - エクロ

- 内部名: `LEADER_EKHLO`
- 属性: 邪悪
- 志向: 蛮族志向 / カリスマ志向 / 野戦志向 / 残存
- 好む社会制度: 自由主義
- 好む遺産: トレントンの聖水
- 宗教の重視度: 深海の旧支配者 iWeightModifier=50 / エススの枢密院 iWeightModifier=80 / 緑葉の同胞 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 90
  - `iTowerVictoryWeight`: 10
  - `iAltarVictoryWeight`: 10
  - `iConquestVictoryWeight`: 5
  - `iDominationVictoryWeight`: 5
  - `iReligionVictoryWeight`: 50
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 魔獣ユニット

### Qiturn - キタン

- 内部名: `LEADER_QITURN`
- 属性: 邪悪
- 志向: 蛮族志向 / 創造志向 / 秘術志向 / 生命の達人
- 好む社会制度: 平和主義
- 好む遺産: 国王記念館
- 宗教の重視度: 深海の旧支配者 iWeightModifier=50 / エススの枢密院 iWeightModifier=20 / 緑葉の同胞 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 90
  - `iTowerVictoryWeight`: 10
  - `iAltarVictoryWeight`: 10
  - `iConquestVictoryWeight`: 5
  - `iDominationVictoryWeight`: 5
  - `iReligionVictoryWeight`: 50
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 100

### Schoengar - シェンガ

- 内部名: `LEADER_SCHOENGAR`
- 属性: 邪悪
- 志向: 蛮族志向 / 探求志向 / 生産志向
- 好む社会制度: 自由主義
- 好む遺産: トレントンの聖水
- 宗教の重視度: 深海の旧支配者 iWeightModifier=50 / エススの枢密院 iWeightModifier=50 / 緑葉の同胞 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 90
  - `iTowerVictoryWeight`: 10
  - `iAltarVictoryWeight`: 10
  - `iConquestVictoryWeight`: 5
  - `iDominationVictoryWeight`: 5
  - `iReligionVictoryWeight`: 50
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 魔獣ユニット

### Neige - ネージュ

- 内部名: `LEADER_NEIGE`
- 属性: 邪悪
- 志向: 蛮族志向 / 創造志向 / 建設志向
- 好む社会制度: 平和主義
- 好む遺産: エルヴェの塔
- 宗教の重視度: 深海の旧支配者 iWeightModifier=50 / 緑葉の同胞 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 90
  - `iTowerVictoryWeight`: 10
  - `iAltarVictoryWeight`: 10
  - `iConquestVictoryWeight`: 5
  - `iDominationVictoryWeight`: 5
  - `iReligionVictoryWeight`: 50
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 100

### Hiver - イヴェール

- 内部名: `LEADER_HIVER`
- 属性: 邪悪
- 志向: 蛮族志向 / 哲学志向 / 万能志向
- 好む社会制度: 自由主義
- 好む遺産: ヴェルギュールの強欲
- 宗教の重視度: 深海の旧支配者 iWeightModifier=50 / 緑葉の同胞 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 90
  - `iTowerVictoryWeight`: 10
  - `iAltarVictoryWeight`: 10
  - `iConquestVictoryWeight`: 5
  - `iDominationVictoryWeight`: 5
  - `iReligionVictoryWeight`: 50
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 魔獣ユニット

### Givre - ジーヴル

- 内部名: `LEADER_GIVRE`
- 属性: 邪悪
- 志向: 蛮族志向 / 創造志向 / 賢人志向
- 好む社会制度: 自由主義
- 好む遺産: レウケティオスのアトリエ
- 宗教の重視度: 深海の旧支配者 iWeightModifier=50 / 緑葉の同胞 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iRefuseToTalkWarThreshold`: 5
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 90
  - `iTowerVictoryWeight`: 10
  - `iAltarVictoryWeight`: 10
  - `iConquestVictoryWeight`: 5
  - `iDominationVictoryWeight`: 5
  - `iReligionVictoryWeight`: 50
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 100

### Raphel - ラファエル

- 内部名: `LEADER_RAPHEL`
- 属性: 善良
- 志向: 金融志向 / 宗教志向 / 次元の達人
- 好む社会制度: 神権政治
- 好む遺産: テンポランス神殿
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=90 / 緑葉の同胞 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 7
  - `iNoTechTradeThreshold`: 7
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 9
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 25
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 55
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 110
  - `iVassalPowerModifier`: 30
  - `iFreedomAppreciation`: 3
  - `bFemale`: 1
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 筆記
  - `FavoriteUnitCombat`: 白兵ユニット

### Georges Longhill - ジョルジュ・ロングヒル

- 内部名: `LEADER_GEORGES`
- 属性: 善良
- 志向: 防御志向 / 預言志向 / 信仰志向
- 好む社会制度: 神権政治
- 好む遺産: 天球の羅針盤
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=50 / 緑葉の同胞 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 50
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 20
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 哲学
  - `FavoriteUnitCombat`: 白兵ユニット

### Margarete - マルガレーテ

- 内部名: `LEADER_MARGARETE`
- 属性: 中立
- 志向: 創造志向 / 徴税志向 / 挽回志向
- 好む社会制度: 神権政治
- 好む遺産: 天球の羅針盤
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=90 / 緑葉の同胞 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 7
  - `iNoTechTradeThreshold`: 7
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 9
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 25
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 55
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 110
  - `iVassalPowerModifier`: 30
  - `iFreedomAppreciation`: 3
  - `bFemale`: 1
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 筆記
  - `FavoriteUnitCombat`: 信奉ユニット

### Oswald - オズワルド

- 内部名: `LEADER_OSWALD`
- 属性: 善良
- 志向: 突撃志向 / 軍事志向 / 殉死志向
- 好む社会制度: 神権政治
- 好む遺産: 九王者の騎獣
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=50 / 緑葉の同胞 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 7
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 9
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 45
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 120
  - `iMaxWarDistantPowerRatio`: 70
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 110
  - `iVassalPowerModifier`: 30
  - `iFreedomAppreciation`: 3
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 哲学
  - `FavoriteUnitCombat`: 白兵ユニット

### Laslo - ラスロー

- 内部名: `LEADER_LASLO`
- 属性: 善良
- 志向: 組織志向 / 賢人志向 / 退魔志向
- 好む社会制度: 神権政治
- 好む遺産: 八魔陣
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=50 / 緑葉の同胞 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 7
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 9
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 45
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 120
  - `iMaxWarDistantPowerRatio`: 70
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 110
  - `iVassalPowerModifier`: 30
  - `iFreedomAppreciation`: 3
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 哲学
  - `FavoriteUnitCombat`: 信奉ユニット

### Ignatius - イグナティウス

- 内部名: `LEADER_IGNATIUS`
- 属性: 善良
- 志向: 宗教志向 / 召喚志向 / 復讐志向 / 生命の達人
- 好む社会制度: 神権政治
- 好む遺産: アウレウスの竈
- 宗教の重視度: 蒼褪めたヴェール iWeightModifier=50 / 緑葉の同胞 iWeightModifier=-99 / 秩序の修道会 iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 50
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 20
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 哲学
  - `FavoriteUnitCombat`: 信奉ユニット

### Fox - フォックス

- 内部名: `LEADER_FOX`
- 属性: 中立
- 志向: 金融志向 / カリスマ志向 / 不屈
- 好む社会制度: 大量消費
- 好む遺産: 九人衆ギルド
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 3
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 20
  - `iAltarVictoryWeight`: 20
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 6
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 80
  - `FavoriteTech`: 通貨
  - `FavoriteUnitCombat`: 騎乗ユニット

### Hound - ハウンド

- 内部名: `LEADER_HOUND`
- 属性: 中立
- 志向: 警邏志向 / 将官志向 / 工夫志向
- 好む社会制度: ギルド制
- 好む遺産: 九人衆ギルド
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 7
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 30
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 通貨
  - `FavoriteUnitCombat`: 白兵ユニット

### Vulepes - ブランフォード

- 内部名: `LEADER_VULEPES`
- 属性: 中立
- 志向: 話術志向 / 万能志向 / 挽回志向
- 好む社会制度: 大量消費
- 好む遺産: デルプトゥスの醸造所
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 15
  - `iConquestVictoryWeight`: 55
  - `iDominationVictoryWeight`: 40
  - `iReligionVictoryWeight`: 5
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 90
  - `iVassalPowerModifier`: -20
  - `iFreedomAppreciation`: 10
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 80
  - `FavoriteTech`: 通貨
  - `FavoriteUnitCombat`: 騎乗ユニット

### Coyote - コヨーテ

- 内部名: `LEADER_COYOTE`
- 属性: 中立
- 志向: 勤労志向 / 万能志向 / 工夫志向
- 好む社会制度: ギルド制
- 好む遺産: 九人衆ギルド
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 3
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 30
  - `iAltarVictoryWeight`: 20
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 40
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteTech`: 通貨
  - `FavoriteUnitCombat`: 白兵ユニット

### Steindorf - シュタインドルフ

- 内部名: `LEADER_STEINDORF`
- 属性: 善良
- 志向: カリスマ志向 / 農耕志向 / 早熟志向
- 好む社会制度: 大量消費
- 好む遺産: 国王記念館
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 15
  - `iTowerVictoryWeight`: 40
  - `iConquestVictoryWeight`: 40
  - `iDominationVictoryWeight`: 55
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 80
  - `FavoriteTech`: 通貨

### Smiley - スマイリー

- 内部名: `LEADER_SMILEY`
- 属性: 邪悪
- 志向: 金融志向 / 突撃志向 / 魔法抵抗志向 / 触死志向
- 好む社会制度: 軍事国家
- 好む遺産: 遠目と早耳の情報網
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 1
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 5
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 75
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 20
  - `bReligionOpportunist`: 1
  - `iEconomyTechValue`: 80

### Hydra - ハイドラ

- 内部名: `LEADER_HYDRA`
- 属性: 中立
- 志向: 蛮族志向 / 預言志向 / 伝説志向 / 混沌の達人 / 精神の達人
- 好む社会制度: 奴隷制
- 好む遺産: 愉悦の塔
- お気に入りの宗教: 深海の旧支配者
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=90 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 5
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 75
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 60
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120
  - `FavoriteUnitCombat`: 海軍ユニット

### Ingwe Vanyar - イングウェ・ヴァンヤール

- 内部名: `LEADER_INGWE`
- 属性: 中立
- 志向: 哲学志向 / 賢人志向 / 殉死志向 / 混沌の達人
- 好む社会制度: 大自然の守護者
- 好む遺産: スケルスの鉱泉
- 宗教の重視度: 緑葉の同胞 iWeightModifier=50 / 深海の旧支配者 iWeightModifier=50 / 蒼褪めたヴェール iWeightModifier=50 / キルモフのルーン iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 3
  - `iRefuseToTalkWarThreshold`: 12
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 80
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 5
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 75
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarMinAdjacentLandPercent`: 4
  - `iLimitedWarPowerRatio`: 100
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 50
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 弓術ユニット

### Grebneerg Werdna - グレブニール・ワードナ

- 内部名: `LEADER_WERDNA`
- 属性: 中立
- 志向: 詠唱志向 / 警邏志向 / 復讐志向 / 次元の達人
- 好む社会制度: 大自然の守護者
- 好む遺産: エルヴェの塔
- 宗教の重視度: 緑葉の同胞 iWeightModifier=50 / 深海の旧支配者 iWeightModifier=50 / 蒼褪めたヴェール iWeightModifier=50 / キルモフのルーン iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 40
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 5
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 75
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 100
  - `iBaseAttackOddsChange`: 2
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 弓術ユニット

### Ardwen Erggebern - アルドウェン・エルゲバーン

- 内部名: `LEADER_ARDWEN`
- 属性: 中立
- 志向: 宗教志向 / 強化志向 / 魂の達人
- 好む社会制度: 大自然の守護者
- 好む遺産: 八魔陣
- 宗教の重視度: 緑葉の同胞 iWeightModifier=50 / 深海の旧支配者 iWeightModifier=50 / 蒼褪めたヴェール iWeightModifier=50 / キルモフのルーン iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 15
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 5
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 75
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 110
  - `iMaxWarDistantPowerRatio`: 70
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 弓術ユニット

### Luthien Tinuviel - ルーシエン・ティヌーヴィエル

- 内部名: `LEADER_LUTHIEN`
- 属性: 中立
- 志向: 話術志向 / 成長志向 / 大気の達人
- 好む社会制度: 大自然の守護者
- 好む遺産: 三圃組合
- 宗教の重視度: 緑葉の同胞 iWeightModifier=50 / 深海の旧支配者 iWeightModifier=50 / 蒼褪めたヴェール iWeightModifier=50 / キルモフのルーン iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 15
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 5
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 75
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 110
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: -20
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 弓術ユニット

### Finwe Noldor - フィンウェ・ノルドール

- 内部名: `LEADER_FINWE`
- 属性: 中立
- 志向: 預言志向 / 徴税志向 / 精神の達人
- 好む社会制度: 大自然の守護者
- 好む遺産: レウケティオスのアトリエ
- 宗教の重視度: 緑葉の同胞 iWeightModifier=50 / 深海の旧支配者 iWeightModifier=50 / 蒼褪めたヴェール iWeightModifier=50 / キルモフのルーン iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 40
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 5
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 75
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 110
  - `iMaxWarDistantPowerRatio`: 80
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 100
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: 20
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 弓術ユニット

### Elwe Elu Thingol - エルウェ・エル・シンゴル

- 内部名: `LEADER_ELWE`
- 属性: 中立
- 志向: 警邏志向 / 探求志向 / 肉体の達人
- 好む社会制度: 大自然の守護者
- 好む遺産: 鼠捕りギルド
- 宗教の重視度: 緑葉の同胞 iWeightModifier=50 / 深海の旧支配者 iWeightModifier=50 / 蒼褪めたヴェール iWeightModifier=50 / キルモフのルーン iWeightModifier=50 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 50
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 5
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 75
  - `iDominationVictoryWeight`: 50
  - `iReligionVictoryWeight`: 10
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 80
  - `iLimitedWarPowerRatio`: 130
  - `iBaseAttackOddsChange`: 4
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 弓術ユニット

### Adelais Morgaterode - アデライズ・モーガティロド

- 内部名: `LEADER_ADELAIS`
- 属性: 中立
- 志向: 攻撃志向 / 蒐集志向 / 殉死志向
- 好む社会制度: 現人神制
- 好む遺産: 広大な貧民街
- お気に入りの宗教: キルモフのルーン
- 宗教の重視度: キルモフのルーン iWeightModifier=90 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 9
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 90
  - `iVassalPowerModifier`: -20
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 攻城兵器

### Yrtsudni Atakas - ユスデニィ・アターカス

- 内部名: `LEADER_YRTSUDNI`
- 属性: 中立
- 志向: 成長志向 / 生産志向
- 好む社会制度: 現人神制
- 好む遺産: ガル=デュールの鉱山
- お気に入りの宗教: キルモフのルーン
- 宗教の重視度: キルモフのルーン iWeightModifier=90 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 50
  - `iMaxGoldTradePercent`: 15
  - `iMaxGoldPerTurnTradePercent`: 15
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 100
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 攻城兵器

### Epytr Maet - エピーティア・メート

- 内部名: `LEADER_EPYTR`
- 属性: 中立
- 志向: 創造志向 / 探求志向
- 好む社会制度: 現人神制
- 好む遺産: ガル=デュールの鉱山
- お気に入りの宗教: キルモフのルーン
- 宗教の重視度: キルモフのルーン iWeightModifier=90 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 15
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 110
  - `iBaseAttackOddsChange`: 2
  - `iVassalPowerModifier`: -20
  - `iFreedomAppreciation`: 10
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 攻城兵器

### Anipusa Etutitsni - エニプサー・エユティツニ

- 内部名: `LEADER_ANIPUSA`
- 属性: 中立
- 志向: 商才志向 / 徴税志向 / 工夫志向
- 好む社会制度: 現人神制
- 好む遺産: ガル=デュールの鉱山
- お気に入りの宗教: キルモフのルーン
- 宗教の重視度: キルモフのルーン iWeightModifier=90 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 8
  - `iRefuseToTalkWarThreshold`: 8
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 90
  - `iMaxWarDistantPowerRatio`: 80
  - `iMaxWarMinAdjacentLandPercent`: 3
  - `iLimitedWarPowerRatio`: 110
  - `iBaseAttackOddsChange`: 2
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 攻城兵器

### Enydlaci Mehc - エニドゥラーシ・メーク

- 内部名: `LEADER_ENYDLACI`
- 属性: 中立
- 志向: 勤労志向 / 軍事志向 / 工夫志向
- 好む社会制度: 現人神制
- 好む遺産: ガル=デュールの鉱山
- お気に入りの宗教: キルモフのルーン
- 宗教の重視度: キルモフのルーン iWeightModifier=90 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 60
  - `iMaxGoldTradePercent`: 5
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 130
  - `iMaxWarDistantPowerRatio`: 100
  - `iLimitedWarPowerRatio`: 100
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 攻城兵器

### Tivavqa Suruat - ティヴァーヴカ・スルーアト

- 内部名: `LEADER_TIVAVQA`
- 属性: 中立
- 志向: 拡張志向 / 建設志向
- 好む社会制度: 現人神制
- 好む遺産: ガル=デュールの鉱山
- お気に入りの宗教: キルモフのルーン
- 宗教の重視度: キルモフのルーン iWeightModifier=90 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 5
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 10
  - `iTowerVictoryWeight`: 10
  - `iConquestVictoryWeight`: 70
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 50
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
  - `FavoriteUnitCombat`: 攻城兵器

### Nikephoros - ニケフォロス

- 内部名: `LEADER_NIKEPHOROS`
- 属性: 邪悪
- 志向: 無神論志向 / 秘術志向 / 話術志向 / 触死志向
- 好む社会制度: 現人神制
- 好む遺産: 魂の溶鉱炉
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: -2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 45
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 哲学

### Najesh - ナージェシュ

- 内部名: `LEADER_NAJESH`
- 属性: 邪悪
- 志向: 無神論志向 / 召喚志向 / 預言志向 / 触死志向
- 好む社会制度: 現人神制
- 好む遺産: 八魔陣
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: -2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 45
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 哲学

### Nusluel - ナスルエル

- 内部名: `LEADER_NUSLUEL`
- 属性: 邪悪
- 志向: 無神論志向 / 勤労志向 / 強化志向 / 復讐志向
- 好む社会制度: 貴族制
- 好む遺産: 創造の酒造
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: -2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 45
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 哲学

### Nohmamare - ノーマメイア

- 内部名: `LEADER_NOHMAMARE`
- 属性: 邪悪
- 志向: 無神論志向 / 強化志向 / 商才志向 / 挽回志向
- 好む社会制度: 大量消費
- 好む遺産: 魂の溶鉱炉
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: -2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 45
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 哲学

### Newt - ニュート

- 内部名: `LEADER_NEWT`
- 属性: 邪悪
- 志向: 無神論志向 / 金融志向 / 強化志向 / 早熟志向
- 好む社会制度: 貴族制
- 好む遺産: 魂の溶鉱炉
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: -2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 45
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 哲学

### Notherly - ノザリー

- 内部名: `LEADER_NOTHERLY`
- 属性: 邪悪
- 志向: 無神論志向 / 強化志向 / 交易志向 / 不可逆の達人
- 好む社会制度: 奨学金制
- 好む遺産: 魂の溶鉱炉
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: -2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 45
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 哲学

### Nesgosym - ネスグオシム

- 内部名: `LEADER_NESGOSYM`
- 属性: 邪悪
- 志向: 無神論志向 / 防御志向 / 強化志向 / 炎の達人
- 好む社会制度: 奴隷制
- 好む遺産: 魂の溶鉱炉
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: -2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 45
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 哲学

### Necrozoure - ネクロゾール

- 内部名: `LEADER_NECROZOURE`
- 属性: 邪悪
- 志向: 無神論志向 / 創造志向 / 強化志向 / 魂の達人
- 好む社会制度: カースト制
- 好む遺産: 魂の溶鉱炉
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=-100 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: -2
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 5
  - `iAltarVictoryWeight`: 45
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 25
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 130
  - `FavoriteTech`: 哲学

### Hermes the Second - ヘルメスⅡ世

- 内部名: `LEADER_HERMES_THE_SECOND`
- 属性: 善良
- 志向: 勤労志向 / 迅速志向 / 不屈
- 好む社会制度: 徒弟制
- 好む遺産: ネクサス
- 宗教の重視度: 緑葉の同胞 iWeightModifier=50 / キルモフのルーン iWeightModifier=50 / 蒼褪めたヴェール iWeightModifier=-80 / 至光なる天空 iWeightModifier=30 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 7
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 20
  - `iDominationVictoryWeight`: 20
  - `iReligionVictoryWeight`: 20
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `bFemale`: 1
  - `iEconomyTechValue`: 120

### Rogeren Baconil - ロージェレン・ベコニル

- 内部名: `LEADER_ROGEREN`
- 属性: 善良
- 志向: 探求志向 / 建設志向
- 好む社会制度: 徒弟制
- 好む遺産: 創造の酒造
- 宗教の重視度: 緑葉の同胞 iWeightModifier=50 / キルモフのルーン iWeightModifier=50 / 蒼褪めたヴェール iWeightModifier=-80 / 至光なる天空 iWeightModifier=30 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 7
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 30
  - `iTowerVictoryWeight`: 40
  - `iAltarVictoryWeight`: 35
  - `iConquestVictoryWeight`: 15
  - `iDominationVictoryWeight`: 15
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120

### Alberat Magnuillion - アルベラット・マグヌイリオン

- 内部名: `LEADER_ALBERAT`
- 属性: 善良
- 志向: 話術志向 / 伝道志向
- 好む社会制度: 徒弟制
- 好む遺産: 天球の羅針盤
- 宗教の重視度: 緑葉の同胞 iWeightModifier=50 / キルモフのルーン iWeightModifier=50 / 蒼褪めたヴェール iWeightModifier=-80 / 至光なる天空 iWeightModifier=30 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 30
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120

### Hermes the Third - ヘルメスⅢ世

- 内部名: `LEADER_HERMES_THE_THIRD`
- 属性: 善良
- 志向: 適応志向 / TXT_KEY_TRAIT_IMPERIALIST / 工夫志向
- 好む社会制度: 徒弟制
- 好む遺産: テンポランス神殿
- 宗教の重視度: 緑葉の同胞 iWeightModifier=50 / キルモフのルーン iWeightModifier=50 / 蒼褪めたヴェール iWeightModifier=-80 / 至光なる天空 iWeightModifier=30 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 6
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 25
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `TemporaryTraits`: カリスマ志向
  - `bFemale`: 1
  - `iEconomyTechValue`: 120

### Parastendi Aureolus - パラステンディ・オーレオルス

- 内部名: `LEADER_PARASTENDI`
- 属性: 善良
- 志向: 召喚志向 / 賢人志向 / 混沌の達人
- 好む社会制度: 徒弟制
- 好む遺産: 八魔陣
- 宗教の重視度: 緑葉の同胞 iWeightModifier=50 / キルモフのルーン iWeightModifier=50 / 蒼褪めたヴェール iWeightModifier=-80 / 至光なる天空 iWeightModifier=30 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 4
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 15
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 10
  - `iCultureVictoryWeight`: 20
  - `iTowerVictoryWeight`: 30
  - `iAltarVictoryWeight`: 20
  - `iConquestVictoryWeight`: 20
  - `iDominationVictoryWeight`: 35
  - `iReligionVictoryWeight`: 25
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 70
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20
  - `iEconomyTechValue`: 120
  - `FavoriteUnitCombat`: 秘術ユニット

### Geberar Alembicil - ゲベラー・アレムビシル

- 内部名: `LEADER_GEBERAR`
- 属性: 善良
- 志向: 勤労志向 / 創造志向
- 好む社会制度: 徒弟制
- 好む遺産: エルヴェの塔
- 宗教の重視度: 緑葉の同胞 iWeightModifier=50 / キルモフのルーン iWeightModifier=50 / 蒼褪めたヴェール iWeightModifier=-80 / 至光なる天空 iWeightModifier=30 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 9
  - `iRefuseToTalkWarThreshold`: 6
  - `iNoTechTradeThreshold`: 20
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 70
  - `iTowerVictoryWeight`: 15
  - `iAltarVictoryWeight`: 50
  - `iReligionVictoryWeight`: 15
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 1
  - `iLimitedWarPowerRatio`: 90
  - `iVassalPowerModifier`: -20
  - `iFreedomAppreciation`: 10
  - `iEconomyTechValue`: 120

### Mulcarn, God of Winter - 冬の神ムルカルン

- 内部名: `LEADER_MULCARN`
- 属性: 中立
- 好む社会制度: 平和主義
- 好む遺産: テンポランス神殿
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 7
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 30
  - `iEconomyTechValue`: 120

### Kylorin the Overload - 天帝カイロリン

- 内部名: `LEADER_KYLORIN`
- 属性: 善良
- 志向: 哲学志向 / カリスマ志向 / 秘術志向 / 万能志向 / 伝説志向
- 好む社会制度: 平和主義
- 好む遺産: テンポランス神殿
- 宗教の重視度: ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iBasePeaceWeight`: 7
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 10
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iCultureVictoryWeight`: 25
  - `iTowerVictoryWeight`: 25
  - `iAltarVictoryWeight`: 40
  - `iConquestVictoryWeight`: 25
  - `iDominationVictoryWeight`: 35
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 60
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 80
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 30
  - `iEconomyTechValue`: 120

### TXT_KEY_LEADER_RANDOM - TXT_KEY_LEADER_RANDOM

- 内部名: `LEADER_RANDOM`
- 属性: 中立
- 好む社会制度: 対外貿易
- その他の設定:
  - `iBasePeaceWeight`: 2
  - `iWarmongerRespect`: 1
  - `iRefuseToTalkWarThreshold`: 10
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 20
  - `iMaxGoldTradePercent`: 10
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 100
  - `iMaxWarDistantPowerRatio`: 50
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 50
  - `iBaseAttackOddsChange`: 4
  - `iVassalPowerModifier`: 20

### Judecca - ジュデッカ

- 内部名: `LEADER_JUDECCA`
- 属性: 邪悪
- 志向: 蛮族志向 / 哲学志向 / 金融志向
- 好む社会制度: 徒弟制
- 好む遺産: 地獄全書
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=50 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 40
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 50
  - `bMinor`: 1
  - `iEconomyTechValue`: 100

### Duke Sallos - サロス公爵

- 内部名: `LEADER_SALLOS`
- 属性: 邪悪
- 志向: 蛮族志向 / 侵掠志向 / 召喚志向
- 好む社会制度: 徒弟制
- 好む遺産: 地獄全書
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=50 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 40
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 50
  - `bMinor`: 1
  - `iEconomyTechValue`: 100

### Ouzza - オウザ

- 内部名: `LEADER_OUZZA`
- 属性: 邪悪
- 志向: 攻撃志向 / 賢人志向 / 蛮族志向
- 好む社会制度: 徒弟制
- 好む遺産: 地獄全書
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=50 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 40
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 50
  - `bMinor`: 1
  - `iEconomyTechValue`: 100

### Meresin - メレシン

- 内部名: `LEADER_MERESIN`
- 属性: 邪悪
- 志向: 蛮族志向 / 拡張志向 / 召喚志向
- 好む社会制度: 徒弟制
- 好む遺産: 地獄全書
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=50 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 40
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 50
  - `bMinor`: 1
  - `iEconomyTechValue`: 100

### Statius the Redeemer - 救世主スタティウス

- 内部名: `LEADER_STATIUS`
- 属性: 邪悪
- 志向: 蛮族志向 / 勤労志向 / 賢人志向
- 好む社会制度: 徒弟制
- 好む遺産: 地獄全書
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=50 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 40
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 50
  - `bMinor`: 1
  - `iEconomyTechValue`: 100

### Lethe, Queen of Sorrow - 嘆きの女王レテ

- 内部名: `LEADER_LETHE`
- 属性: 邪悪
- 志向: 蛮族志向 / 宗教志向 / カリスマ志向
- 好む社会制度: 徒弟制
- 好む遺産: 地獄全書
- お気に入りの宗教: 蒼褪めたヴェール
- 宗教の重視度: エススの枢密院 iWeightModifier=-100 / 緑葉の同胞 iWeightModifier=-100 / 深海の旧支配者 iWeightModifier=-100 / キルモフのルーン iWeightModifier=-100 / 蒼褪めたヴェール iWeightModifier=50 / 至光なる天空 iWeightModifier=-100 / 秩序の修道会 iWeightModifier=-100 / ドラゴン崇拝 iWeightModifier=-100
- その他の設定:
  - `iWarmongerRespect`: 2
  - `iRefuseToTalkWarThreshold`: 20
  - `iNoTechTradeThreshold`: 5
  - `iTechTradeKnownPercent`: 10
  - `iMaxGoldTradePercent`: 20
  - `iMaxGoldPerTurnTradePercent`: 10
  - `iMaxWarNearbyPowerRatio`: 80
  - `iMaxWarDistantPowerRatio`: 40
  - `iMaxWarMinAdjacentLandPercent`: 2
  - `iLimitedWarPowerRatio`: 40
  - `iBaseAttackOddsChange`: 8
  - `iVassalPowerModifier`: 50
  - `bMinor`: 1
  - `bFemale`: 1
  - `iEconomyTechValue`: 100
