# OAC/昇進（0.57、XMLから生成）

- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）
- 生成元: `Units/CIV4PromotionInfos.xml`
- 読み方: 主要な項目は日本語ラベル付きで先頭に、それ以外の既定値でない設定は「その他の設定」にXMLのタグ名のまま列挙する。値の内部名は日本語名に置き換えている。Pythonで実装された効果はXMLにないため含まない（ゲーム内ヘルプの説明文があれば載せている）。

### Combat I - 戦闘Ⅰ

- 内部名: `PROMOTION_COMBAT1`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット
- +%[戦闘力]: 10
- その他の設定:
  - `bMutation`: 1
  - `iCombatPercentDefense`: 10
  - `iSpellDamageModify`: 10
  - `PromotionSummonPerk`: 強化Ⅰ
  - `PromotionNextLevel`: 戦闘Ⅱ

### Combat II - 戦闘Ⅱ

- 内部名: `PROMOTION_COMBAT2`
- 前提昇進: 戦闘Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット
- +%[戦闘力]: 15
- その他の設定:
  - `iCasterResistModify`: -5
  - `iCombatPercentDefense`: 15
  - `iSpellDamageModify`: 15
  - `PromotionSummonPerk`: 強化Ⅱ
  - `PromotionNextLevel`: 戦闘Ⅲ

### Combat III - 戦闘Ⅲ

- 内部名: `PROMOTION_COMBAT3`
- 前提昇進: 戦闘Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット
- +%[戦闘力]: 20
- その他の設定:
  - `iCollateralDamageProtection`: 20
  - `iCasterResistModify`: -5
  - `iCombatPercentDefense`: 20
  - `iSpellDamageModify`: 20
  - `PromotionSummonPerk`: 強化Ⅲ
  - `PromotionNextLevel`: 戦闘Ⅳ

### Combat IV - 戦闘Ⅳ

- 内部名: `PROMOTION_COMBAT4`
- 前提昇進: 戦闘Ⅲ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット
- +%[戦闘力]: 25
- その他の設定:
  - `iCollateralDamageProtection`: 20
  - `iCasterResistModify`: -5
  - `iCombatPercentDefense`: 25
  - `iSpellDamageModify`: 25
  - `PromotionSummonPerk`: 強化Ⅳ
  - `PromotionNextLevel`: 戦闘Ⅴ

### Combat V - 戦闘Ⅴ

- 内部名: `PROMOTION_COMBAT5`
- 前提昇進: 戦闘Ⅳ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット
- +%[戦闘力]: 30
- その他の設定:
  - `iCollateralDamageProtection`: 20
  - `iCasterResistModify`: -5
  - `iCombatPercentDefense`: 30
  - `iSpellDamageModify`: 30
  - `PromotionSummonPerk`: 強化Ⅴ

### Drill I - 教練Ⅰ

- 内部名: `PROMOTION_DRILL1`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iAirCombatLimitChange`: 5
  - `iEnemyWithdrawalChange`: -10
  - `iFirstStrikesChange`: 1
  - `PromotionSummonPerk`: 教練Ⅰ
  - `PromotionNextLevel`: 教練Ⅱ

### Drill II - 教練Ⅱ

- 内部名: `PROMOTION_DRILL2`
- 前提昇進: 教練Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iAirCombatLimitChange`: 5
  - `iEnemyWithdrawalChange`: -10
  - `iFirstStrikesChange`: 1
  - `PromotionSummonPerk`: 教練Ⅱ
  - `PromotionNextLevel`: 教練Ⅲ

### Drill III - 教練Ⅲ

- 内部名: `PROMOTION_DRILL3`
- 前提昇進: 教練Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iAirCombatLimitChange`: 10
  - `iEnemyWithdrawalChange`: -10
  - `iChanceFirstStrikesChange`: 2
  - `PromotionSummonPerk`: 教練Ⅲ
  - `PromotionNextLevel`: 教練Ⅳ

### Drill IV - 教練Ⅳ

- 内部名: `PROMOTION_DRILL4`
- 前提昇進: 教練Ⅲ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iAirCombatLimitChange`: 10
  - `iEnemyWithdrawalChange`: -10
  - `iChanceFirstStrikesChange`: 3
  - `UnitCombatMods`: 騎乗ユニット iUnitCombatMod=10
  - `PromotionSummonPerk`: 教練Ⅳ

### City Garrison I - 都市駐留Ⅰ

- 内部名: `PROMOTION_CITY_GARRISON1`
- 対象の兵科: 弓術ユニット / 信奉ユニット
- その他の設定:
  - `iCityDefense`: 40
  - `PromotionNextLevel`: 都市駐留Ⅱ

### City Garrison II - 都市駐留Ⅱ

- 内部名: `PROMOTION_CITY_GARRISON2`
- 前提昇進: 都市駐留Ⅰ
- 必要テクノロジー: 軍事行動
- 対象の兵科: 弓術ユニット / 信奉ユニット
- その他の設定:
  - `iCityDefense`: 50
  - `PromotionNextLevel`: 都市駐留Ⅲ

### City Garrison III - 都市駐留Ⅲ

- 内部名: `PROMOTION_CITY_GARRISON3`
- 前提昇進: 都市駐留Ⅱ
- 対象の兵科: 弓術ユニット
- その他の設定:
  - `iCityDefense`: 60
  - `UnitCombatMods`: 白兵ユニット iUnitCombatMod=20

### City Raider I - 都市襲撃Ⅰ

- 内部名: `PROMOTION_CITY_RAIDER1`
- 対象の兵科: 動物ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 攻城兵器
- その他の設定:
  - `iCityAttack`: 30
  - `PromotionNextLevel`: 都市襲撃Ⅱ

### City Raider II - 都市襲撃Ⅱ

- 内部名: `PROMOTION_CITY_RAIDER2`
- 前提昇進: 都市襲撃Ⅰ
- 必要テクノロジー: 軍事行動
- 対象の兵科: 動物ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 攻城兵器 / 偵察ユニット
- その他の設定:
  - `iCityAttack`: 40
  - `PromotionNextLevel`: 都市襲撃Ⅲ

### City Raider III - 都市襲撃Ⅲ

- 内部名: `PROMOTION_CITY_RAIDER3`
- 前提昇進: 都市襲撃Ⅱ
- 対象の兵科: 動物ユニット / 魔獣ユニット / 白兵ユニット / 騎乗ユニット / 攻城兵器 / 偵察ユニット
- その他の設定:
  - `iCityAttack`: 50
  - `UnitCombatMods`: 弓術ユニット iUnitCombatMod=20

### Barrage I - 弾幕Ⅰ

- 内部名: `PROMOTION_BARRAGE1`
- 対象の兵科: 海軍ユニット / 攻城兵器
- その他の設定:
  - `iCollateralDamageChange`: 40
  - `iExtraTargetLimit`: 1
  - `PromotionNextLevel`: 弾幕Ⅱ

### Barrage II - 弾幕Ⅱ

- 内部名: `PROMOTION_BARRAGE2`
- 前提昇進: 弾幕Ⅰ
- 対象の兵科: 海軍ユニット / 攻城兵器
- その他の設定:
  - `iAirCombatChange`: 1
  - `iCollateralDamageChange`: 60
  - `iBombardRateChange`: 5
  - `UnitCombatMods`: 白兵ユニット iUnitCombatMod=20
  - `iExtraTargetLimit`: 1
  - `PromotionNextLevel`: 弾幕Ⅲ

### Barrage III - 弾幕Ⅲ

- 内部名: `PROMOTION_BARRAGE3`
- 前提昇進: 弾幕Ⅱ
- 対象の兵科: 海軍ユニット / 攻城兵器
- その他の設定:
  - `iAirCombatChange`: 2
  - `iAirCombatLimitChange`: 10
  - `iCollateralDamageChange`: 100
  - `UnitCombatMods`: 弓術ユニット iUnitCombatMod=20
  - `iExtraTargetLimit`: 1

### Accuracy - 精密砲撃

- 内部名: `PROMOTION_ACCURACY`
- 前提昇進: 弾幕Ⅱ
- 対象の兵科: 海軍ユニット / 攻城兵器
- その他の設定:
  - `iAirCombatLimitChange`: 10
  - `iBombardRateChange`: 10

### Shock I - 強襲Ⅰ

- 内部名: `PROMOTION_SHOCK`
- 前提昇進(いずれか): 戦闘Ⅰ
- 対象の兵科: 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `UnitCombatMods`: 白兵ユニット iUnitCombatMod=40
  - `PromotionPrereqOr3`: 教練Ⅰ
  - `PromotionNextLevel`: 強襲Ⅱ

### Shock II - 強襲Ⅱ

- 内部名: `PROMOTION_SHOCK2`
- 前提昇進: 強襲Ⅰ
- 対象の兵科: 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `UnitCombatMods`: 白兵ユニット iUnitCombatMod=60

### Formation I - 隊形Ⅰ

- 内部名: `PROMOTION_FORMATION`
- 前提昇進(いずれか): 戦闘Ⅰ
- 対象の兵科: 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 偵察ユニット
- その他の設定:
  - `UnitCombatMods`: 騎乗ユニット iUnitCombatMod=40
  - `PromotionPrereqOr3`: 教練Ⅰ
  - `PromotionNextLevel`: 隊形Ⅱ

### Formation II - 隊形Ⅱ

- 内部名: `PROMOTION_FORMATION2`
- 前提昇進: 隊形Ⅰ
- 対象の兵科: 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 偵察ユニット
- その他の設定:
  - `UnitCombatMods`: 騎乗ユニット iUnitCombatMod=60

### Cover I - 掩護Ⅰ

- 内部名: `PROMOTION_COVER`
- 前提昇進(いずれか): 戦闘Ⅱ
- 対象の兵科: 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット
- その他の設定:
  - `UnitCombatMods`: 弓術ユニット iUnitCombatMod=40
  - `PromotionPrereqOr3`: 教練Ⅱ
  - `PromotionNextLevel`: 掩護Ⅱ

### Cover II - 掩護Ⅱ

- 内部名: `PROMOTION_COVER2`
- 前提昇進: 掩護Ⅰ
- 対象の兵科: 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット
- その他の設定:
  - `UnitCombatMods`: 弓術ユニット iUnitCombatMod=60

### Scourge - 災厄

- 内部名: `PROMOTION_SCOURGE`
- 前提昇進(いずれか): 戦闘Ⅰ
- 必要テクノロジー: 邪悪への道
- 対象の兵科: 魔獣ユニット / 白兵ユニット / 偵察ユニット
- その他の設定:
  - `UnitCombatMods`: 信奉ユニット iUnitCombatMod=50
  - `PromotionPrereqOr3`: 教練Ⅰ

### Flanking I - 側面攻撃Ⅰ

- 内部名: `PROMOTION_FLANKING1`
- 対象の兵科: 騎乗ユニット / 海軍ユニット / 偵察ユニット
- その他の設定:
  - `iWithdrawalChange`: 15
  - `PromotionNextLevel`: 側面攻撃Ⅱ

### Flanking II - 側面攻撃Ⅱ

- 内部名: `PROMOTION_FLANKING2`
- 前提昇進: 側面攻撃Ⅰ
- 対象の兵科: 騎乗ユニット / 海軍ユニット
- その他の設定:
  - `iWithdrawalChange`: 20
  - `PromotionNextLevel`: 側面攻撃Ⅲ

### Flanking III - 側面攻撃Ⅲ

- 内部名: `PROMOTION_FLANKING3`
- 前提昇進: 側面攻撃Ⅱ
- 対象の兵科: 騎乗ユニット / 海軍ユニット
- その他の設定:
  - `bImmuneToFirstStrikes`: 1
  - `iWithdrawalChange`: 25
  - `bImmuneToDefensiveStrike`: 1

### Mobility I - 機動力Ⅰ

- 内部名: `PROMOTION_MOBILITY1`
- 必要テクノロジー: 騎乗
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iMovesChange`: 1
  - `bMutation`: 1
  - `PromotionNextLevel`: 機動力Ⅱ

### Mobility II - 機動力Ⅱ

- 内部名: `PROMOTION_MOBILITY2`
- 前提昇進: 機動力Ⅰ
- 必要テクノロジー: 鐙
- 対象の兵科: 動物ユニット / 騎乗ユニット
- その他の設定:
  - `iMovesChange`: 1
  - `iMoveDiscountChange`: 2

### Sentry I - 歩哨Ⅰ

- 内部名: `PROMOTION_SENTRY`
- 前提昇進(いずれか): 戦闘Ⅱ
- 前提昇進(いずれか): 教練Ⅰ
- 対象の兵科: 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット
- その他の設定:
  - `iVisibilityChange`: 1
  - `UnitCombatMods`: 偵察ユニット iUnitCombatMod=30
  - `bMutation`: 1
  - `PromotionNextLevel`: 歩哨Ⅱ

### Sentry II - 歩哨Ⅱ

- 内部名: `PROMOTION_SENTRY2`
- 前提昇進: 歩哨Ⅰ
- 対象の兵科: 弓術ユニット / 偵察ユニット
- その他の設定:
  - `iVisibilityChange`: 1
  - `UnitCombatMods`: 偵察ユニット iUnitCombatMod=40

### Perfect Sight - 看破の目

- 内部名: `PROMOTION_PERFECT_SIGHT`
- 前提昇進(いずれか): 戦闘Ⅲ
- 前提昇進(いずれか): 教練Ⅱ
- 対象の兵科: 弓術ユニット / 偵察ユニット
- その他の設定:
  - `UnitCombatMods`: 偵察ユニット iUnitCombatMod=30
  - `SeeInvisible`: INVISIBLE_STEALTH
  - `PromotionCombatType`: 幻影
  - `iPromotionCombatMod`: 100
  - `ImmuneToPromotions`: 盲目

### Keen Sight - 鷹の目

- 内部名: `PROMOTION_KEEN_SIGHT`
- 前提昇進(いずれか): 教練Ⅱ
- 対象の兵科: 弓術ユニット
- その他の設定:
  - `bAlwaysDefensiveStrike`: 1
  - `iEnemyWithdrawalChange`: -20
  - `iDefensiveStrikeChance`: 30
  - `iDefensiveStrikeDamage`: 20
  - `PromotionPrereqOr3`: 器用

### Precision - 精密射撃

- 内部名: `PROMOTION_PRECISION`
- 前提昇進(いずれか): 教練Ⅲ
- 必要テクノロジー: 精密射撃
- 対象の兵科: 弓術ユニット
- その他の設定:
  - `iAirCombatLimitChange`: 15
  - `iCollateralDamageChange`: 50
  - `iExtraTargetLimit`: 1
  - `PromotionPrereqOr3`: 器用

### Marksman - 狙撃

- 内部名: `PROMOTION_MARKSMAN`
- 前提昇進(いずれか): 教練Ⅳ
- 必要テクノロジー: 複合弓
- 対象の兵科: 弓術ユニット / 偵察ユニット
- その他の設定:
  - `iFirstStrikesChange`: 1
  - `bTargetWeakestUnit`: 1

### Magic Resistance - 魔法抵抗

- 内部名: `PROMOTION_MAGIC_RESISTANCE`
- 説明（ゲーム内ヘルプ）: 敵の呪文にかかりにくい
- その他の設定:
  - `iResistMagic`: 20
  - `DamageTypeResists`: 冷気 iResist=20 / 死 iResist=20 / 火炎 iResist=20 / 神聖 iResist=20 / 電撃 iResist=20 / 物理 / 毒 / 不浄 iResist=20

### Resist Cold - 冷気抵抗

- 内部名: `PROMOTION_COLD_RESISTANCE`
- 前提昇進(いずれか): 戦闘Ⅲ
- 前提昇進(いずれか): 魔法抵抗
- 対象の兵科: 秘術ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット
- 説明（ゲーム内ヘルプ）: 猛吹雪のダメージを無力化する
- その他の設定:
  - `TerrainAttacks`: 氷原 iTerrainAttack=10 / 凍土 iTerrainAttack=10
  - `TerrainDefenses`: 氷原 iTerrainDefense=10 / 凍土 iTerrainDefense=10
  - `UnitCombatMods`: 弓術ユニット iUnitCombatMod=10 / 白兵ユニット iUnitCombatMod=10 / 騎乗ユニット iUnitCombatMod=10
  - `TerrainDoubleMoves`: 氷原 / 凍土
  - `bMutation`: 1
  - `PromotionPrereqOr3`: 教練Ⅲ
  - `DamageTypeResists`: 冷気 iResist=50

### Resist Fire - 火炎抵抗

- 内部名: `PROMOTION_FIRE_RESISTANCE`
- 前提昇進(いずれか): 戦闘Ⅲ
- 前提昇進(いずれか): 魔法抵抗
- 対象の兵科: 秘術ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット
- その他の設定:
  - `TerrainAttacks`: 砂漠 iTerrainAttack=10 / 灼熱の砂地 iTerrainAttack=10
  - `TerrainDefenses`: 砂漠 iTerrainDefense=10 / 灼熱の砂地 iTerrainDefense=10
  - `UnitCombatMods`: 秘術ユニット iUnitCombatMod=50
  - `TerrainDoubleMoves`: 砂漠 / 灼熱の砂地
  - `bMutation`: 1
  - `PromotionPrereqOr3`: 教練Ⅲ
  - `DamageTypeResists`: 火炎 iResist=50

### Resist Lightning - 電撃抵抗

- 内部名: `PROMOTION_LIGHTNING_RESISTANCE`
- 前提昇進(いずれか): 戦闘Ⅲ
- 前提昇進(いずれか): 魔法抵抗
- 対象の兵科: 秘術ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット
- その他の設定:
  - `UnitCombatMods`: 信奉ユニット iUnitCombatMod=30
  - `bMutation`: 1
  - `iResistMagic`: 20
  - `PromotionPrereqOr3`: 教練Ⅲ
  - `DamageTypeResists`: 電撃 iResist=50

### Resist Poison - 毒抵抗

- 内部名: `PROMOTION_POISON_RESISTANCE`
- 前提昇進(いずれか): 戦闘Ⅲ
- 前提昇進(いずれか): 魔法抵抗
- 対象の兵科: 秘術ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット
- その他の設定:
  - `UnitCombatMods`: 偵察ユニット iUnitCombatMod=40
  - `bMutation`: 1
  - `PromotionPrereqOr3`: 教練Ⅲ
  - `DamageTypeResists`: 毒 iResist=50

### Guerilla I - ゲリラⅠ

- 内部名: `PROMOTION_GUERILLA1`
- 対象の兵科: 動物ユニット / 偵察ユニット
- その他の設定:
  - `bHillsDoubleMove`: 1
  - `iHillsAttack`: 30
  - `iHillsDefense`: 30
  - `FeatureAttacks`: 沼 iFeatureAttack=30
  - `FeatureDefenses`: 沼 iFeatureDefense=30
  - `FeatureDoubleMoves`: 沼
  - `PromotionNextLevel`: ゲリラⅡ

### Guerilla II - ゲリラⅡ

- 内部名: `PROMOTION_GUERILLA2`
- 前提昇進: ゲリラⅠ
- 必要テクノロジー: 追跡術
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iEnemyWithdrawalChange`: -15
  - `iFirstStrikesChange`: 1
  - `iHillsAttack`: 40
  - `iHillsDefense`: 40
  - `FeatureAttacks`: 沼 iFeatureAttack=40
  - `FeatureDefenses`: 沼 iFeatureDefense=40
  - `UnitCombatMods`: 弓術ユニット iUnitCombatMod=20
  - `PromotionNextLevel`: ゲリラⅢ

### Guerilla 3 - ゲリラⅢ

- 内部名: `PROMOTION_GUERILLA3`
- 前提昇進: ゲリラⅡ
- 必要テクノロジー: 軍事行動
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iWithdrawalChange`: 50
  - `iEnemyWithdrawalChange`: -15
  - `iCollateralDamageProtection`: 20
  - `UnitCombatMods`: 弓術ユニット iUnitCombatMod=30

### Woodsman I - 森番Ⅰ

- 内部名: `PROMOTION_WOODSMAN1`
- 対象の兵科: 動物ユニット / 偵察ユニット
- その他の設定:
  - `FeatureAttacks`: 密林 iFeatureAttack=30 / 森林 iFeatureAttack=30 / 古代樹林 iFeatureAttack=30 / 深い密林 iFeatureAttack=30
  - `FeatureDefenses`: 密林 iFeatureDefense=30 / 森林 iFeatureDefense=30 / 古代樹林 iFeatureDefense=30 / 深い密林 iFeatureDefense=30
  - `FeatureDoubleMoves`: 密林 / 森林 / 古代樹林 / 深い密林
  - `PromotionNextLevel`: 森番Ⅱ

### Woodsman II - 森番Ⅱ

- 内部名: `PROMOTION_WOODSMAN2`
- 前提昇進: 森番Ⅰ
- 必要テクノロジー: 追跡術
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `FeatureAttacks`: 密林 iFeatureAttack=30 / 森林 iFeatureAttack=30 / 古代樹林 iFeatureAttack=30 / 深い密林 iFeatureAttack=30
  - `FeatureDefenses`: 密林 iFeatureDefense=30 / 森林 iFeatureDefense=30 / 古代樹林 iFeatureDefense=30 / 深い密林 iFeatureDefense=30
  - `Invisible`: INVISIBLE_ANIMAL
  - `PromotionNextLevel`: 森番Ⅲ

### Woodsman 3 - 森番Ⅲ

- 内部名: `PROMOTION_WOODSMAN3`
- 前提昇進: 森番Ⅱ
- 必要テクノロジー: 軍事行動
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iFirstStrikesChange`: 2
  - `iChanceFirstStrikesChange`: 1
  - `iEnemyHealChange`: 15
  - `iNeutralHealChange`: 15
  - `iFriendlyHealChange`: 15
  - `UnitCombatMods`: 動物ユニット iUnitCombatMod=40 / 魔獣ユニット iUnitCombatMod=40

### Amphibious - 水陸両用

- 内部名: `PROMOTION_AMPHIBIOUS`
- 前提昇進(いずれか): 戦闘Ⅱ
- 対象の兵科: 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bAmphib`: 1
  - `bRiver`: 1
  - `UnitCombatMods`: 海軍ユニット iUnitCombatMod=20
  - `bMutation`: 1
  - `bWaterWalking`: 1
  - `FreeWaterWalkingTech`: 海図
  - `PromotionPrereqOr3`: 教練Ⅱ

### Blitz - 電撃戦

- 内部名: `PROMOTION_BLITZ`
- 前提昇進(いずれか): 教練Ⅳ
- 必要テクノロジー: 軍事戦略
- 対象の兵科: 秘術ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット
- その他の設定:
  - `bBlitz`: 1
  - `bMutation`: 1
  - `PromotionSummonPerk`: 電撃戦
  - `PromotionPrereqOr3`: 側面攻撃Ⅱ
  - `PromotionPrereqOr4`: 機動力Ⅱ

### Bounty Hunter - 賞金稼ぎ

- 内部名: `PROMOTION_BOUNTY_HUNTER`
- 前提昇進(いずれか): 戦闘Ⅲ
- 対象の兵科: 弓術ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット
- その他の設定:
  - `iGoldFromCombat`: 4
  - `PromotionPrereqOr3`: 教練Ⅲ

### Commando - 特別奇襲

- 内部名: `PROMOTION_COMMANDO`
- 前提昇進(いずれか): 戦闘Ⅲ
- 前提昇進(いずれか): 教練Ⅱ
- 対象の兵科: 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bEnemyRoute`: 1
  - `iChanceFirstStrikesChange`: 1
  - `PromotionPrereqOr4`: 森番Ⅲ

### Defensive - 鉄壁

- 内部名: `PROMOTION_DEFENSIVE`
- 前提昇進(いずれか): 戦闘Ⅱ
- 対象の兵科: 弓術ユニット / 白兵ユニット
- その他の設定:
  - `iCollateralDamageProtection`: 80
  - `bDoubleFortifyBonus`: 1
  - `PromotionPrereqOr3`: 教練Ⅱ
  - `DamageTypeResists`: 物理 iResist=50

### March - 行軍

- 内部名: `PROMOTION_MARCH`
- 前提昇進(いずれか): 戦闘Ⅲ
- 前提昇進(いずれか): 衛生兵Ⅰ
- 対象の兵科: 動物ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット
- その他の設定:
  - `bAlwaysHeal`: 1
  - `iEnemyHealChange`: 10
  - `iNeutralHealChange`: 10
  - `iFriendlyHealChange`: 10
  - `PromotionPrereqOr3`: 教練Ⅲ

### Demon Slaying I - 魔族狩り

- 内部名: `PROMOTION_DEMON_SLAYING`
- 前提昇進(いずれか): 戦闘Ⅰ
- 必要テクノロジー: 叡智への道
- 対象の兵科: 魔獣ユニット / 信奉ユニット / 白兵ユニット
- その他の設定:
  - `iEnemyHealChange`: 10
  - `iNeutralHealChange`: 10
  - `iFriendlyHealChange`: 10
  - `PromotionCombatType`: 魔族
  - `iPromotionCombatMod`: 50
  - `ImmuneToPromotions`: 狂乱 / 睡眠 / 狂暴
  - `PromotionPrereqOr3`: 教練Ⅰ
  - `PromotionPrereqOr4`: 護衛
  - `DamageTypeResists`: 神聖 iResist=20 / 催眠 iResist=50

### Dragon Slaying - ドラゴン狩り

- 内部名: `PROMOTION_DRAGON_SLAYING`
- 前提昇進: 戦闘Ⅴ
- 対象の兵科: 魔獣ユニット / 信奉ユニット / 白兵ユニット
- +%[戦闘力]: 20
- その他の設定:
  - `iCombatPercentDefense`: 20
  - `PromotionCombatType`: ドラゴン
  - `iPromotionCombatMod`: 30

### Undead Slaying - 屍人狩り

- 内部名: `PROMOTION_UNDEAD_SLAYING`
- 前提昇進(いずれか): 戦闘Ⅰ
- 必要テクノロジー: 叡智への道
- 対象の兵科: 魔獣ユニット / 信奉ユニット / 白兵ユニット
- その他の設定:
  - `PromotionCombatType`: 屍人
  - `iPromotionCombatMod`: 50
  - `ImmuneToPromotions`: 病気 / 毒
  - `PromotionPrereqOr3`: 教練Ⅰ
  - `DamageTypeResists`: 神聖 iResist=50 / 毒 iResist=20

### Guardsman - 護衛

- 内部名: `PROMOTION_GUARDSMAN`
- 前提昇進(いずれか): 戦闘Ⅳ
- 前提昇進(いずれか): 教練Ⅲ
- 対象の兵科: 白兵ユニット
- その他の設定:
  - `bTargetWeakestUnitCounter`: 1

### Subdue Animal - 動物調教

- 内部名: `PROMOTION_SUBDUE_ANIMAL`
- 前提昇進(いずれか): 戦闘Ⅰ
- 必要テクノロジー: 畜産
- 対象の兵科: 偵察ユニット
- その他の設定:
  - `UnitCombatMods`: 動物ユニット iUnitCombatMod=40
  - `CaptureUnitCombat`: 動物ユニット
  - `PromotionPrereqOr3`: 教練Ⅰ
  - `PromotionPrereqOr4`: 残存

### Subdue Beasts - 魔獣調教

- 内部名: `PROMOTION_SUBDUE_BEASTS`
- 前提昇進: 動物調教
- 前提昇進(いずれか): 戦闘Ⅲ
- 必要テクノロジー: 動物の極意
- 対象の兵科: 偵察ユニット
- その他の設定:
  - `UnitCombatMods`: 魔獣ユニット iUnitCombatMod=40
  - `CaptureUnitCombat`: 魔獣ユニット
  - `PromotionPrereqOr3`: 教練Ⅲ
  - `PromotionPrereqOr4`: 残存

### Expanded Hull - 船体拡張

- 内部名: `PROMOTION_EXPANDED_HULL`
- 必要テクノロジー: 建設
- 対象の兵科: 海軍ユニット
- その他の設定:
  - `iCargoChange`: 1

### Navigation I - 航海術Ⅰ

- 内部名: `PROMOTION_NAVIGATION1`
- 前提昇進: 側面攻撃Ⅰ
- 必要テクノロジー: 航海術
- 対象の兵科: 海軍ユニット
- その他の設定:
  - `iMovesChange`: 1
  - `PromotionNextLevel`: 航海術Ⅱ

### Navigation II - 航海術Ⅱ

- 内部名: `PROMOTION_NAVIGATION2`
- 前提昇進: 航海術Ⅰ
- 対象の兵科: 海軍ユニット
- その他の設定:
  - `iMovesChange`: 1

### Heroic Defense I - 英雄の盾Ⅰ

- 内部名: `PROMOTION_HEROIC_DEFENSE`
- 前提昇進: 英雄
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `bMutation`: 1
  - `iExtraCombatDefense`: 1
  - `PromotionSummonPerk`: 英雄の盾Ⅰ
  - `PromotionPrereqOr3`: 戦闘Ⅴ
  - `PromotionPrereqOr4`: 教練Ⅳ
  - `PromotionNextLevel`: 英雄の盾Ⅱ

### Heroic Defense II - 英雄の盾Ⅱ

- 内部名: `PROMOTION_HEROIC_DEFENSE2`
- 前提昇進: 英雄の盾Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iExtraCombatDefense`: 1
  - `iMinLevel`: 5
  - `PromotionSummonPerk`: 英雄の盾Ⅱ

### Heroic Strength I - 英雄の力Ⅰ

- 内部名: `PROMOTION_HEROIC_STRENGTH`
- 前提昇進: 英雄
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iAirCombatChange`: 1
  - `bMutation`: 1
  - `iExtraCombatStr`: 1
  - `PromotionSummonPerk`: 英雄の力Ⅰ
  - `PromotionPrereqOr3`: 戦闘Ⅴ
  - `PromotionPrereqOr4`: 教練Ⅳ
  - `PromotionNextLevel`: 英雄の力Ⅱ

### Heroic Strength II - 英雄の力Ⅱ

- 内部名: `PROMOTION_HEROIC_STRENGTH2`
- 前提昇進: 英雄の力Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iAirCombatChange`: 1
  - `iExtraCombatStr`: 1
  - `iMinLevel`: 5
  - `PromotionSummonPerk`: 英雄の力Ⅱ

### Twincast - 双つ術

- 内部名: `PROMOTION_TWINCAST`
- 前提昇進: 英雄
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `bTwincast`: 1
  - `PromotionPrereqOr3`: 戦闘Ⅴ
  - `PromotionPrereqOr4`: 教練Ⅳ

### Summoner - 召喚術師

- 内部名: `PROMOTION_SUMMONER`
- 前提昇進: 英雄
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `iSpellCasterXP`: 10
  - `PromotionSummonPerk`: 突撃
  - `PromotionPrereqOr3`: 戦闘Ⅴ
  - `PromotionPrereqOr4`: 教練Ⅳ

### Cannibalize - 人食い

- 内部名: `PROMOTION_CANNIBALIZE`
- 前提昇進: 屍人
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bCarnivorous`: 1
  - `bMutation`: 1
  - `iCombatHealPercent`: 10
  - `PromotionPrereqOr3`: 戦闘Ⅱ
  - `PromotionPrereqOr4`: 教練Ⅱ

### Fear - 恐怖

- 内部名: `PROMOTION_FEAR`
- 前提昇進(いずれか): 魔族
- 前提昇進(いずれか): 屍人
- 対象の兵科: 秘術ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bFear`: 1
  - `PromotionPrereqAnd`: 戦闘Ⅴ
  - `PromotionPrereqOr3`: ナイトメア

### Stigmata - 烙印

- 内部名: `PROMOTION_STIGMATA`
- 前提昇進: 魔族
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iCombatPercentGlobalCounter`: 50
  - `PromotionPrereqAnd`: 戦闘Ⅴ

### Sundered - 呪刻

- 内部名: `PROMOTION_SUNDERED`
- 前提昇進: 精神集中Ⅱ
- 必要テクノロジー: 魂の堕落
- 対象の兵科: 秘術ユニット / 信奉ユニット
- その他の設定:
  - `StateReligionPrereq`: 蒼褪めたヴェール
  - `iSpellCasterXP`: 10
  - `PromotionSummonPerk`: 烙印
  - `DamageTypeResists`: 不浄 iResist=25

### Command I - 折伏Ⅰ

- 内部名: `PROMOTION_COMMAND1`
- 前提昇進(いずれか): 精神集中Ⅱ
- 対象の兵科: 信奉ユニット
- その他の設定:
  - `iCombatCapturePercent`: 10
  - `PromotionNextLevel`: 折伏Ⅱ

### Command II - 折伏Ⅱ

- 内部名: `PROMOTION_COMMAND2`
- 前提昇進: 折伏Ⅰ
- 対象の兵科: 信奉ユニット
- その他の設定:
  - `iCombatCapturePercent`: 15
  - `PromotionPrereqAnd`: 精神集中Ⅲ
  - `PromotionNextLevel`: 折伏Ⅲ

### Command III - 折伏Ⅲ

- 内部名: `PROMOTION_COMMAND3`
- 前提昇進: 折伏Ⅱ
- 対象の兵科: 信奉ユニット
- その他の設定:
  - `iCombatCapturePercent`: 20
  - `PromotionPrereqAnd`: 精神集中Ⅲ
  - `PromotionNextLevel`: 折伏Ⅳ

### Command IV - 折伏Ⅳ

- 内部名: `PROMOTION_COMMAND4`
- 前提昇進: 折伏Ⅲ
- 対象の兵科: 信奉ユニット
- その他の設定:
  - `StateReligionPrereq`: 秩序の修道会
  - `iCombatCapturePercent`: 25
  - `PromotionPrereqAnd`: 精神集中Ⅲ

### Spell Extension I - 呪文伸長Ⅰ

- 内部名: `PROMOTION_EXTENSION1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `iExtraTargetLimit`: 1
  - `PromotionSummonPerk`: 機動力Ⅰ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 呪文伸長Ⅱ

### Spell Extension II - 呪文伸長Ⅱ

- 内部名: `PROMOTION_EXTENSION2`
- 前提昇進: 呪文伸長Ⅰ
- 必要テクノロジー: 秘術の伝承知識
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `iExtraSpellRange`: 1
  - `iExtraTargetLimit`: 1
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 呪文伸長Ⅲ

### Spell Extension III - 呪文伸長Ⅲ

- 内部名: `PROMOTION_EXTENSION3`
- 前提昇進: 呪文伸長Ⅱ
- 必要テクノロジー: エーテル移動
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `bTwincast`: 1
  - `iExtraTargetLimit`: 2
  - `iMinLevel`: 5
  - `PromotionSummonPerk`: 電撃戦
  - `PromotionPrereqAnd`: 精神集中Ⅲ

### Fast Chant - 高速詠唱

- 内部名: `PROMOTION_FAST_CHANT`
- 前提昇進: 教練Ⅰ
- 前提昇進(いずれか): 精神集中Ⅰ
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット
- その他の設定:
  - `bFastChant`: 1
  - `PromotionPrereqOr3`: 精神集中Ⅱ
  - `PromotionPrereqOr4`: 精神集中Ⅲ

### Illusionist - 幻術士

- 内部名: `PROMOTION_ILLUSIONIST`
- 前提昇進: 影Ⅲ
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `StateReligionPrereq`: エススの枢密院
  - `PromotionSummonPerk`: 幻影

### Inquisitor - 異端審問

- 内部名: `PROMOTION_INQUISITOR`
- 前提昇進: 精神集中Ⅱ
- 対象の兵科: 信奉ユニット

### Air I - 大気Ⅰ

- 内部名: `PROMOTION_AIR1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 大気のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 大気Ⅱ

### Air II - 大気Ⅱ

- 内部名: `PROMOTION_AIR2`
- 前提昇進: 大気Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 大気Ⅲ
  - `DamageTypeResists`: 電撃 iResist=25

### Air III - 大気Ⅲ

- 内部名: `PROMOTION_AIR3`
- 前提昇進: 大気Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionSummonPerk`: 電撃抵抗
  - `PromotionPrereqAnd`: 精神集中Ⅲ
  - `DamageTypeResists`: 電撃 iResist=100

### Earth I - 大地Ⅰ

- 内部名: `PROMOTION_EARTH1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 大地のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 大地Ⅱ

### Earth II - 大地Ⅱ

- 内部名: `PROMOTION_EARTH2`
- 前提昇進: 大地Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iExtraCombatDefense`: 1
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 大地Ⅲ

### Earth III - 大地Ⅲ

- 内部名: `PROMOTION_EARTH3`
- 前提昇進: 大地Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iExtraCombatDefense`: 3
  - `PromotionSummonPerk`: 石の皮膚
  - `PromotionPrereqAnd`: 精神集中Ⅲ

### Fire I - 炎Ⅰ

- 内部名: `PROMOTION_FIRE1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 炎のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 炎Ⅱ

### Fire II - 炎Ⅱ

- 内部名: `PROMOTION_FIRE2`
- 前提昇進: 炎Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 炎Ⅲ
  - `DamageTypeResists`: 火炎 iResist=25

### Fire III - 炎Ⅲ

- 内部名: `PROMOTION_FIRE3`
- 前提昇進: 炎Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionSummonPerk`: 火炎抵抗
  - `PromotionPrereqAnd`: 精神集中Ⅲ
  - `DamageTypeResists`: 火炎 iResist=100

### Water I - 水Ⅰ

- 内部名: `PROMOTION_WATER1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 水のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 水Ⅱ

### Water II - 水Ⅱ

- 内部名: `PROMOTION_WATER2`
- 前提昇進: 水Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `bWaterWalking`: 1
  - `FreeWaterWalkingTech`: 魔術
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 水Ⅲ

### Water III - 水Ⅲ

- 内部名: `PROMOTION_WATER3`
- 前提昇進: 水Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionSummonPerk`: 水上歩行
  - `PromotionPrereqAnd`: 精神集中Ⅲ

### Body I - 肉体Ⅰ

- 内部名: `PROMOTION_BODY1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 肉体のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 肉体Ⅱ

### Body II - 肉体Ⅱ

- 内部名: `PROMOTION_BODY2`
- 前提昇進: 肉体Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iEnemyHealChange`: 5
  - `iNeutralHealChange`: 5
  - `iFriendlyHealChange`: 5
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 肉体Ⅲ

### Body III - 肉体Ⅲ

- 内部名: `PROMOTION_BODY3`
- 前提昇進: 肉体Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `bAlwaysHeal`: 1
  - `PromotionPrereqAnd`: 精神集中Ⅲ

### Enchantment I - 呪付Ⅰ

- 内部名: `PROMOTION_ENCHANTMENT1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 呪付のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 呪付Ⅱ

### Enchantment II - 呪付Ⅱ

- 内部名: `PROMOTION_ENCHANTMENT2`
- 前提昇進: 呪付Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iCasterResistModify`: -5
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 呪付Ⅲ

### Enchantment III - 呪付Ⅲ

- 内部名: `PROMOTION_ENCHANTMENT3`
- 前提昇進: 呪付Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iCasterResistModify`: -10
  - `PromotionPrereqAnd`: 精神集中Ⅲ

### Mind I - 精神Ⅰ

- 内部名: `PROMOTION_MIND1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 精神のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 精神Ⅱ

### Mind II - 精神Ⅱ

- 内部名: `PROMOTION_MIND2`
- 前提昇進: 精神Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iResistMagic`: 5
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 精神Ⅲ

### Mind III - 精神Ⅲ

- 内部名: `PROMOTION_MIND3`
- 前提昇進: 精神Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iResistMagic`: 10
  - `PromotionPrereqAnd`: 精神集中Ⅲ

### Nature I - 自然Ⅰ

- 内部名: `PROMOTION_NATURE1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 自然のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 自然Ⅱ

### Nature II - 自然Ⅱ

- 内部名: `PROMOTION_NATURE2`
- 前提昇進: 自然Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 自然Ⅲ
  - `DamageTypeResists`: 毒 iResist=25

### Nature III - 自然Ⅲ

- 内部名: `PROMOTION_NATURE3`
- 前提昇進: 自然Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionSummonPerk`: 毒抵抗
  - `PromotionPrereqAnd`: 精神集中Ⅲ
  - `DamageTypeResists`: 毒 iResist=100

### Chaos I - 混沌Ⅰ

- 内部名: `PROMOTION_CHAOS1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 混沌のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 混沌Ⅱ

### Chaos II - 混沌Ⅱ

- 内部名: `PROMOTION_CHAOS2`
- 前提昇進: 混沌Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionSummonPerk`: 異形
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 混沌Ⅲ

### Chaos III - 混沌Ⅲ

- 内部名: `PROMOTION_CHAOS3`
- 前提昇進: 混沌Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iSpellDamageModify`: 5
  - `PromotionSummonPerk`: 自爆装置
  - `PromotionPrereqAnd`: 精神集中Ⅲ

### Death I - 死Ⅰ

- 内部名: `PROMOTION_DEATH1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 死のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 死Ⅱ

### Death II - 死Ⅱ

- 内部名: `PROMOTION_DEATH2`
- 前提昇進: 死Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 死Ⅲ
  - `DamageTypeResists`: 死 iResist=25

### Death III - 死Ⅲ

- 内部名: `PROMOTION_DEATH3`
- 前提昇進: 死Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionSummonPerk`: 影石
  - `PromotionPrereqAnd`: 精神集中Ⅲ
  - `DamageTypeResists`: 死 iResist=100

### Entropy I - 不可逆Ⅰ

- 内部名: `PROMOTION_ENTROPY1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 不可逆のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 不可逆Ⅱ

### Entropy II - 不可逆Ⅱ

- 内部名: `PROMOTION_ENTROPY2`
- 前提昇進: 不可逆Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 不可逆Ⅲ
  - `DamageTypeResists`: 不浄 iResist=25

### Entropy III - 不可逆Ⅲ

- 内部名: `PROMOTION_ENTROPY3`
- 前提昇進: 不可逆Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionSummonPerk`: 災厄
  - `PromotionPrereqAnd`: 精神集中Ⅲ
  - `DamageTypeResists`: 不浄 iResist=100

### Shadow I - 影Ⅰ

- 内部名: `PROMOTION_SHADOW1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 影のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 影Ⅱ

### Shadow II - 影Ⅱ

- 内部名: `PROMOTION_SHADOW2`
- 前提昇進: 影Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionSummonPerk`: 陽炎
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 影Ⅲ

### Shadow III - 影Ⅲ

- 内部名: `PROMOTION_SHADOW3`
- 前提昇進: 影Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionSummonPerk`: 影渡り
  - `PromotionPrereqAnd`: 精神集中Ⅲ

### Law I - 法Ⅰ

- 内部名: `PROMOTION_LAW1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 法のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 法Ⅱ

### Law II - 法Ⅱ

- 内部名: `PROMOTION_LAW2`
- 前提昇進: 法Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 法Ⅲ
  - `DamageTypeResists`: 神聖 iResist=25

### Law III - 法Ⅲ

- 内部名: `PROMOTION_LAW3`
- 前提昇進: 法Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionSummonPerk`: 祝福
  - `PromotionPrereqAnd`: 精神集中Ⅲ
  - `DamageTypeResists`: 神聖 iResist=100

### Life I - 生命Ⅰ

- 内部名: `PROMOTION_LIFE1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 生命のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 生命Ⅱ

### Life II - 生命Ⅱ

- 内部名: `PROMOTION_LIFE2`
- 前提昇進: 生命Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iSpellCasterXP`: 10
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 生命Ⅲ

### Life III - 生命Ⅲ

- 内部名: `PROMOTION_LIFE3`
- 前提昇進: 生命Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iSpellCasterXP`: 15
  - `PromotionPrereqAnd`: 精神集中Ⅲ

### Spirit I - 魂Ⅰ

- 内部名: `PROMOTION_SPIRIT1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 魂のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 魂Ⅱ

### Spirit II - 魂Ⅱ

- 内部名: `PROMOTION_SPIRIT2`
- 前提昇進: 魂Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iSpellCasterXP`: 10
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 魂Ⅲ

### Spirit III - 魂Ⅲ

- 内部名: `PROMOTION_SPIRIT3`
- 前提昇進: 魂Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iSpellCasterXP`: 15
  - `PromotionPrereqAnd`: 精神集中Ⅲ

### Sun I - 太陽Ⅰ

- 内部名: `PROMOTION_SUN1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 太陽のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 太陽Ⅱ

### Sun II - 太陽Ⅱ

- 内部名: `PROMOTION_SUN2`
- 前提昇進: 太陽Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionSummonPerk`: 歩哨Ⅰ
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 太陽Ⅲ

### Sun III - 太陽Ⅲ

- 内部名: `PROMOTION_SUN3`
- 前提昇進: 太陽Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iSpellDamageModify`: 5
  - `PromotionSummonPerk`: 歩哨Ⅱ
  - `PromotionPrereqAnd`: 精神集中Ⅲ

### Ice I - 氷Ⅰ

- 内部名: `PROMOTION_ICE1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 氷のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 氷Ⅱ

### Ice II - 氷Ⅱ

- 内部名: `PROMOTION_ICE2`
- 前提昇進: 氷Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 氷Ⅲ
  - `DamageTypeResists`: 冷気 iResist=25

### Ice III - 氷Ⅲ

- 内部名: `PROMOTION_ICE3`
- 前提昇進: 氷Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `PromotionSummonPerk`: 冷気抵抗
  - `PromotionPrereqAnd`: 精神集中Ⅲ
  - `DamageTypeResists`: 冷気 iResist=100

### Metamagic I - 超魔術Ⅰ

- 内部名: `PROMOTION_METAMAGIC1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `iCasterResistModify`: -5
  - `iSpellDamageModify`: 10
  - `BonusPrereq`: 超魔術のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 超魔術Ⅱ

### Metamagic II - 超魔術Ⅱ

- 内部名: `PROMOTION_METAMAGIC2`
- 前提昇進: 超魔術Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iCasterResistModify`: -5
  - `iSpellDamageModify`: 10
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 超魔術Ⅲ

### Metamagic III - 超魔術Ⅲ

- 内部名: `PROMOTION_METAMAGIC3`
- 前提昇進: 超魔術Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iCasterResistModify`: -5
  - `iSpellDamageModify`: 10
  - `PromotionPrereqAnd`: 精神集中Ⅲ

### Channeling I - 精神集中Ⅰ

- 内部名: `PROMOTION_CHANNELING1`
- 説明（ゲーム内ヘルプ）: ランク1の呪文を習得可能
- その他の設定:
  - `iBetterDefenderThanPercent`: -25
  - `iSpellCasterXP`: 25
  - `ImmuneToPromotions`: 睡眠
  - `PromotionNextLevel`: 精神集中Ⅱ

### Channeling II - 精神集中Ⅱ

- 内部名: `PROMOTION_CHANNELING2`
- 説明（ゲーム内ヘルプ）: ランク2の呪文を習得可能
- その他の設定:
  - `iBetterDefenderThanPercent`: -25
  - `iCasterResistModify`: -5
  - `iSpellCasterXP`: 30
  - `ImmuneToPromotions`: 睡眠
  - `PromotionNextLevel`: 精神集中Ⅲ

### Channeling III - 精神集中Ⅲ

- 内部名: `PROMOTION_CHANNELING3`
- 説明（ゲーム内ヘルプ）: ランク3の呪文を習得可能
- その他の設定:
  - `iBetterDefenderThanPercent`: -25
  - `iCasterResistModify`: -5
  - `iSpellCasterXP`: 40
  - `ImmuneToPromotions`: 睡眠 / 狂暴

### Divine - 神術

- 内部名: `PROMOTION_DIVINE`
- 説明（ゲーム内ヘルプ）: 神術呪文を詠唱可能
- その他の設定:
  - `iSpellCasterXP`: 10

### Medic I - 衛生兵Ⅰ

- 内部名: `PROMOTION_MEDIC1`
- その他の設定:
  - `iSameTileHealChange`: 10
  - `PromotionNextLevel`: 衛生兵Ⅱ

### Medic II - 衛生兵Ⅱ

- 内部名: `PROMOTION_MEDIC2`
- その他の設定:
  - `iSameTileHealChange`: 15
  - `PromotionNextLevel`: 衛生兵Ⅲ

### Medic III - 衛生兵Ⅲ

- 内部名: `PROMOTION_MEDIC3`
- その他の設定:
  - `iSameTileHealChange`: 20
  - `iAdjacentTileHealChange`: 20

### Blessed - 祝福

- 内部名: `PROMOTION_BLESSED`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 動物ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bDispellable`: 1
  - `bRemovedByCombat`: 1
  - `PromotionCombatType`: 魔族
  - `iPromotionCombatMod`: 20
  - `DamageTypeCombats`: 神聖 iCombat=1

### Hidden - 身隠し

- 内部名: `PROMOTION_HIDDEN`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 10
- その他の設定:
  - `iFirstStrikesChange`: 1
  - `iCombatPercentDefense`: 10
  - `Invisible`: INVISIBLE_STEALTH
  - `bRemovedByCasting`: 1
  - `bRemovedByCombat`: 1

### Blur - 陽炎

- 内部名: `PROMOTION_BLUR`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット
- その他の設定:
  - `bImmuneToFirstStrikes`: 1
  - `UnitCombatMods`: 弓術ユニット iUnitCombatMod=10
  - `iExpireChance`: 50

### Dance of Blades - 剣の舞

- 内部名: `PROMOTION_DANCE_OF_BLADES`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iChanceFirstStrikesChange`: 2
  - `iCollateralDamageProtection`: 20
  - `bDispellable`: 1
  - `iExpireChance`: 100

### Fair Winds - 追い風

- 内部名: `PROMOTION_FAIR_WINDS`
- 対象の兵科: 海軍ユニット
- その他の設定:
  - `iMovesChange`: 1
  - `iWithdrawalChange`: 25
  - `bDispellable`: 1
  - `iExpireChance`: 5

### Hasted - 快足

- 内部名: `PROMOTION_HASTED`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iMovesChange`: 1
  - `bBeforeMovementOnly`: 1
  - `bDispellable`: 1
  - `iExpireChance`: 100
  - `OppositePromotions`: 鈍足

### Morale - 士気

- 内部名: `PROMOTION_MORALE`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 10
- その他の設定:
  - `iCityAttack`: 10
  - `iCombatPercentDefense`: 10
  - `iExpireChance`: 10

### Regeneration - 再生

- 内部名: `PROMOTION_REGENERATION`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bAlwaysHeal`: 1
  - `iEnemyHealChange`: 10
  - `iNeutralHealChange`: 10
  - `iFriendlyHealChange`: 10
  - `bDispellable`: 1
  - `bMutation`: 1
  - `bRemovedWhenHealed`: 1

### Shadowwalk - 影渡り

- 内部名: `PROMOTION_SHADOWWALK`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iFirstStrikesChange`: 1
  - `bIgnoreBuildingDefense`: 1
  - `bImmuneToDefensiveStrike`: 1
  - `iExpireChance`: 25

### Warcry - 鬨の声

- 内部名: `PROMOTION_WARCRY`
- その他の設定:
  - `bBlitz`: 1
  - `iMovesChange`: 1
  - `iExpireChance`: 5
  - `iExtraCombatStr`: 1
  - `iExtraCombatDefense`: 1

### Courage - 勇気

- 内部名: `PROMOTION_COURAGE`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iSameTileHealChange`: 10
  - `bDispellable`: 1
  - `bImmuneToFear`: 1
  - `bPrereqAlive`: 1

### Loyalty - 忠誠

- 内部名: `PROMOTION_LOYALTY`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- 説明（ゲーム内ヘルプ）: 戦闘で倒されたとき、寝返らずに自決する / +20% 魅了への抵抗確率
- その他の設定:
  - `iCityAttack`: 10
  - `bDispellable`: 1
  - `bImmuneToCapture`: 1
  - `DamageTypeResists`: 催眠 iResist=20

### Valor - 武勇

- 内部名: `PROMOTION_VALOR`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 10
- その他の設定:
  - `bDispellable`: 1
  - `bPrereqAlive`: 1
  - `iCombatPercentDefense`: 10
  - `iFreeXPFromCombat`: 1
  - `iResistMagic`: 10

### Enchanted Blade - 呪付の刃

- 内部名: `PROMOTION_ENCHANTED_BLADE`
- 対象の兵科: 白兵ユニット
- +%[戦闘力]: 20
- その他の設定:
  - `bDispellable`: 1
  - `bValidate`: 1
  - `iCombatPercentDefense`: 20
  - `OppositePromotions`: 武器の腐食

### Flaming Arrows - 炎の矢

- 内部名: `PROMOTION_FLAMING_ARROWS`
- 対象の兵科: 弓術ユニット
- その他の設定:
  - `bDispellable`: 1
  - `bValidate`: 1
  - `DamageTypeCombats`: 火炎 iCombat=1

### Poisoned Blade - 毒の刃

- 内部名: `PROMOTION_POISONED_BLADE`
- 対象の兵科: 偵察ユニット
- その他の設定:
  - `bValidate`: 1
  - `DamageTypeCombats`: 毒 iCombat=1

### Shield of Faith - 信仰の盾

- 内部名: `PROMOTION_SHIELD_OF_FAITH`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 動物ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 10
- その他の設定:
  - `bDispellable`: 1
  - `iCombatPercentDefense`: 30

### Crown of Brilliance - 輝きの王冠

- 内部名: `PROMOTION_CROWN_OF_BRILLANCE`
- 説明（ゲーム内ヘルプ）: ターンの開始時に輝きの王冠の呪文（劣化版）を自動的に唱える
- その他の設定:
  - `bDispellable`: 1
  - `SeeInvisible`: INVISIBLE_STEALTH
  - `iExpireChance`: 25

### Hidden Nationality - 国籍秘匿

- 内部名: `PROMOTION_HIDDEN_NATIONALITY`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `bHiddenNationality`: 1
  - `PromotionSummonPerk`: 国籍秘匿

### Spellstaff - 呪文の杖

- 内部名: `PROMOTION_SPELLSTAFF`
- 対象の兵科: 秘術ユニット
- 説明（ゲーム内ヘルプ）: 杖を消費して詠唱済みのターンに再び呪文を実行可能
- その他の設定:
  - `bDispellable`: 1

### Stoneskin - 石の皮膚

- 内部名: `PROMOTION_STONESKIN`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iFirstStrikesChange`: 3
  - `bDispellable`: 1
  - `bMutation`: 1
  - `bRemovedByCombat`: 1
  - `iExtraCombatDefense`: 2
  - `DamageTypeResists`: 冷気 iResist=50 / 死 iResist=50 / 火炎 iResist=50 / 神聖 iResist=50 / 電撃 iResist=50 / 毒 iResist=50 / 不浄 iResist=50

### Water Walking - 水上歩行

- 内部名: `PROMOTION_WATER_WALKING`
- その他の設定:
  - `bAmphib`: 1
  - `bRiver`: 1
  - `TerrainDoubleMoves`: 近海 / 外洋
  - `bWaterWalking`: 1
  - `FreeWaterWalkingTech`: 魔術

### Empower I - 強化Ⅰ

- 内部名: `PROMOTION_EMPOWER1`
- +%[戦闘力]: 10
- その他の設定:
  - `bMutation`: 1
  - `iCombatPercentDefense`: 10
  - `PromotionNextLevel`: 強化Ⅱ

### Empower II - 強化Ⅱ

- 内部名: `PROMOTION_EMPOWER2`
- +%[戦闘力]: 15
- その他の設定:
  - `iCombatPercentDefense`: 15
  - `PromotionNextLevel`: 強化Ⅲ

### Empower III - 強化Ⅲ

- 内部名: `PROMOTION_EMPOWER3`
- +%[戦闘力]: 20
- その他の設定:
  - `iAirCombatLimitChange`: 5
  - `iCombatPercentDefense`: 20
  - `PromotionNextLevel`: 強化Ⅳ

### Empower IV - 強化Ⅳ

- 内部名: `PROMOTION_EMPOWER4`
- +%[戦闘力]: 25
- その他の設定:
  - `iCombatPercentDefense`: 25
  - `PromotionNextLevel`: 強化Ⅴ

### Empower V - 強化Ⅴ

- 内部名: `PROMOTION_EMPOWER5`
- +%[戦闘力]: 30
- その他の設定:
  - `iAirCombatLimitChange`: 5
  - `iCombatPercentDefense`: 30

### Aeron's Chosen - アーロンに選ばれし者

- 内部名: `PROMOTION_AERONS_CHOSEN`
- その他の設定:
  - `bImmuneToFirstStrikes`: 1
  - `bImmuneToFear`: 1
  - `iCombatHealPercent`: 20
  - `DamageTypeCombats`: 不浄 iCombat=2

### Immortal - 不死身

- 内部名: `PROMOTION_IMMORTAL`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `bImmortal`: 1

### Recruiter - 募兵官

- 内部名: `PROMOTION_RECRUITER`

### Homeland - 母国

- 内部名: `PROMOTION_HOMELAND`
- その他の設定:
  - `iWithdrawalChange`: 10
  - `iCombatPercentInBorders`: 20

### Potency - 潜在力

- 内部名: `PROMOTION_POTENCY`
- 対象の兵科: 秘術ユニット / 信奉ユニット
- その他の設定:
  - `iUpgradeDiscount`: 50
  - `bValidate`: 1
  - `iCasterResistModify`: -5
  - `iExtraTargetLimit`: 1
  - `iSpellCasterXP`: 20
  - `iSpellDamageModify`: 20
  - `iWorkRateModify`: 100

### Unholy Taint - 不浄の聖痕

- 内部名: `PROMOTION_UNHOLY_TAINT`
- 対象の兵科: 秘術ユニット / 信奉ユニット
- +%[戦闘力]: -25
- 説明（ゲーム内ヘルプ）: 秘術使いと法術使いの経験値の自然獲得を促進
- その他の設定:
  - `iCombatPercentDefense`: -25
  - `iSpellCasterXP`: 10
  - `iSpellDamageModify`: 20
  - `DamageTypeCombats`: 不浄 iCombat=1
  - `DamageTypeResists`: 不浄 iResist=25

### Dexterous - 器用

- 内部名: `PROMOTION_DEXTEROUS`
- 対象の兵科: 弓術ユニット
- その他の設定:
  - `iAirCombatChange`: 1
  - `iAirCombatLimitChange`: 15
  - `iAirRangeChange`: 1
  - `bValidate`: 1
  - `iExtraCombatStr`: 1

### Horselord - 駿馬

- 内部名: `PROMOTION_HORSELORD`
- 対象の兵科: 騎乗ユニット
- その他の設定:
  - `iMovesChange`: 1
  - `iMoveDiscountChange`: 2
  - `iWithdrawalChange`: 10
  - `iChanceFirstStrikesChange`: 1
  - `bValidate`: 1
  - `BonusAffinities`: 馬 iAffinity=25

### Sinister - 凶刃

- 内部名: `PROMOTION_SINISTER`
- 対象の兵科: 偵察ユニット
- その他の設定:
  - `iEnemyWithdrawalChange`: -10
  - `iFirstStrikesChange`: 1
  - `bValidate`: 1
  - `DamageTypeCombats`: 毒 iCombat=1

### Prophecy Mark - 黙示録の証

- 内部名: `PROMOTION_PROPHECY_MARK`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- 説明（ゲーム内ヘルプ）: （黙示録の証を持つユニットが誕生するとアルマゲドンカウンタが増加し、死亡すると減少します）
- その他の設定:
  - `iModifyGlobalCounter`: 1
  - `bImmuneToFear`: 1

### Spirit Guide - 聖霊の導き

- 内部名: `PROMOTION_SPIRIT_GUIDE`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- 説明（ゲーム内ヘルプ）: 死亡すると経験値の半分を同じタイルの味方に分け与える
- その他の設定:
  - `bDispellable`: 1
  - `iResistAgainstRemove`: 20

### Nightmare - ナイトメア

- 内部名: `PROMOTION_NIGHTMARE`
- 対象の兵科: 騎乗ユニット
- その他の設定:
  - `TerrainAttacks`: 死滅の大地 iTerrainAttack=10 / 破滅の原野 iTerrainAttack=10 / 灼熱の砂地 iTerrainAttack=10
  - `TerrainDefenses`: 死滅の大地 iTerrainDefense=10 / 破滅の原野 iTerrainDefense=10 / 灼熱の砂地 iTerrainDefense=10
  - `bValidate`: 1
  - `iExtraCombatStr`: 1
  - `iExtraCombatDefense`: 1

### Sheut Stone - 影石

- 内部名: `PROMOTION_SHEUT_STONE`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `DamageTypeCombats`: 死 iCombat=1
  - `DamageTypeResists`: 死 iResist=25 / 神聖 iResist=-10

### Boarding - 接舷攻撃

- 内部名: `PROMOTION_BOARDING`
- その他の設定:
  - `bBoarding`: 1
  - `CaptureUnitCombat`: 海軍ユニット

### Flying - 飛行

- 内部名: `PROMOTION_FLYING`
- その他の設定:
  - `bAmphib`: 1
  - `bRiver`: 1
  - `iMovesChange`: 1
  - `UnitCombatMods`: 弓術ユニット iUnitCombatMod=-20
  - `bIgnoreBuildingDefense`: 1
  - `bFlying`: 1

### Immune to Cold - 冷気無効

- 内部名: `PROMOTION_IMMUNE_COLD`
- 説明（ゲーム内ヘルプ）: 猛吹雪のダメージを無力化する
- その他の設定:
  - `bMutation`: 1
  - `DamageTypeResists`: 冷気 iResist=100

### Immune to Disease - 病気無効

- 内部名: `PROMOTION_IMMUNE_DISEASE`
- その他の設定:
  - `bMutation`: 1
  - `ImmuneToPromotions`: 病気 / 疫病 / 衰弱 / 非力

### Immune to Fire - 火炎無効

- 内部名: `PROMOTION_IMMUNE_FIRE`
- その他の設定:
  - `bMutation`: 1
  - `DamageTypeResists`: 火炎 iResist=100

### Immune to Lightning - 電撃無効

- 内部名: `PROMOTION_IMMUNE_LIGHTNING`
- その他の設定:
  - `bMutation`: 1
  - `DamageTypeResists`: 電撃 iResist=100

### Magic Immune - 魔法無効

- 内部名: `PROMOTION_MAGIC_IMMUNE`
- その他の設定:
  - `bImmuneToMagic`: 1
  - `iResistMagic`: 100
  - `DamageTypeResists`: 冷気 iResist=50 / 死 iResist=50 / 火炎 iResist=50 / 電撃 iResist=50

### Invisible - 不可視

- 内部名: `PROMOTION_INVISIBLE`
- その他の設定:
  - `Invisible`: INVISIBLE_STEALTH

### Hero - 英雄

- 内部名: `PROMOTION_HERO`
- その他の設定:
  - `iEnemyHealChange`: 10
  - `iNeutralHealChange`: 10
  - `iFriendlyHealChange`: 10
  - `iFreeXPPerTurn`: 1
  - `ImmuneToPromotions`: 露見
  - `iResistMagic`: 20
  - `iGroupSize`: 1
  - `iUpgradeDiscount`: 100

### Starting Settler Bonus - 初期開拓者ボーナス

- 内部名: `PROMOTION_STARTING_SETTLER`
- その他の設定:
  - `iVisibilityChange`: 3
  - `iMovesChange`: 2
  - `bNoMaintenanceCost`: 1

### Stealth - 隠れる技能

- 内部名: `PROMOTION_STEALTH`

### Crazed - 発狂

- 内部名: `PROMOTION_CRAZED`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bPrereqAlive`: 1
  - `PromotionRandomApply`: 狂乱
  - `iResistAgainstRemove`: 50

### Held - 拘束

- 内部名: `PROMOTION_HELD`
- その他の設定:
  - `bHeld`: 1

### Charmed - 魅了

- 内部名: `PROMOTION_CHARMED`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bOnlyDefensive`: 1
  - `bDispellable`: 1
  - `bPrereqAlive`: 1
  - `iExpireChance`: 20
  - `iResistAgainstRemove`: 40

### Fatigued - 疲労

- 内部名: `PROMOTION_FATIGUED`
- +%[戦闘力]: -10
- その他の設定:
  - `iCombatPercentDefense`: -10
  - `iExpireChance`: 50

### Revealed - 露見

- 内部名: `PROMOTION_REVEALED`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器 / 労働ユニット
- その他の設定:
  - `bDispellable`: 1
  - `bLoseInvisibility`: 1
  - `iExpireChance`: 5

### Rusted - 武器の腐食

- 内部名: `PROMOTION_RUSTED`
- +%[戦闘力]: -10
- 説明（ゲーム内ヘルプ）: 鍛冶屋のある都市で効果消滅
- その他の設定:
  - `iCombatPercentDefense`: -10
  - `iResistAgainstRemove`: 30
  - `OppositePromotions`: 呪付の刃

### Slow - 鈍足

- 内部名: `PROMOTION_SLOW`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iWithdrawalChange`: -10
  - `iExpireChance`: 30
  - `iResistAgainstRemove`: 50
  - `OppositePromotions`: 快足

### Enraged - 狂乱

- 内部名: `PROMOTION_ENRAGED`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 20
- 説明（ゲーム内ヘルプ）: ユニットの操作はAIが行う（非常に攻撃的になる）
- その他の設定:
  - `iMovesChange`: 1
  - `bBerserk`: 1
  - `bImmuneToFear`: 1
  - `bPrereqAlive`: 1
  - `bRemovedByCombat`: 1
  - `iCombatPercentDefense`: -20
  - `iExpireChance`: 20
  - `iResistAgainstRemove`: 30

### Burning Blood - 燃えたぎる血

- 内部名: `PROMOTION_BURNING_BLOOD`
- 対象の兵科: 動物ユニット / 弓術ユニット / 魔獣ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 20
- その他の設定:
  - `bBlitz`: 1
  - `iMovesChange`: 1
  - `bFastChant`: 1
  - `bImmuneToFear`: 1
  - `iBetrayalChance`: 20
  - `iCombatPercentDefense`: 20
  - `iExpireChance`: 10

### Poisoned - 毒

- 内部名: `PROMOTION_POISONED`
- +%[戦闘力]: -10
- 説明（ゲーム内ヘルプ）: （毒による戦闘力を持つユニットからダメージを受けると、毒に侵されることがあります）
- その他の設定:
  - `iEnemyHealChange`: -5
  - `iNeutralHealChange`: -5
  - `iFriendlyHealChange`: -5
  - `bRemovedWhenHealed`: 1
  - `iCombatPercentDefense`: -10

### Diseased - 病気

- 内部名: `PROMOTION_DISEASED`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- +%[戦闘力]: -30
- その他の設定:
  - `iEnemyHealChange`: -10
  - `iNeutralHealChange`: -10
  - `iFriendlyHealChange`: -10
  - `bMutation`: 1
  - `bPrereqAlive`: 1
  - `iCombatPercentDefense`: -30
  - `PromotionCombatApply`: 病気
  - `iResistAgainstRemove`: 30

### Plagued - 疫病

- 内部名: `PROMOTION_PLAGUED`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- +%[戦闘力]: -60
- その他の設定:
  - `iEnemyHealChange`: -20
  - `iNeutralHealChange`: -20
  - `iFriendlyHealChange`: -20
  - `bPrereqAlive`: 1
  - `iCombatPercentDefense`: -60
  - `iResistAgainstRemove`: 50

### Withered - 衰弱

- 内部名: `PROMOTION_WITHERED`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: -40
- その他の設定:
  - `iEnemyHealChange`: -20
  - `iNeutralHealChange`: -20
  - `iFriendlyHealChange`: -20
  - `iExperiencePercent`: -50
  - `bDispellable`: 1
  - `bMutation`: 1
  - `bPrereqAlive`: 1
  - `iExpireChance`: 3
  - `iCombatPercentDefense`: -40
  - `iResistAgainstRemove`: 30

### Plague Carrier - 保菌者

- 内部名: `PROMOTION_PLAGUE_CARRIER`
- 説明（ゲーム内ヘルプ）: 戦闘を行うと、相手に疫病を感染させることがある
- その他の設定:
  - `PromotionCombatApply`: 疫病

### Vile Touch - 忌まわしき抱擁

- 内部名: `PROMOTION_VILE_TOUCH`
- その他の設定:
  - `PromotionCombatApply`: 衰弱

### Werewolf - 狼人間

- 内部名: `PROMOTION_WEREWOLF`
- 説明（ゲーム内ヘルプ）: （狼人間に殺されたユニットは、飢えた狼人間となって自分を殺した狼人間の陣営に加わります）

### Vampirism - 吸血鬼

- 内部名: `PROMOTION_VAMPIRE`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 10
- 説明（ゲーム内ヘルプ）: 渡河ペナルティ2倍
- その他の設定:
  - `iEnemyHealChange`: 5
  - `iNeutralHealChange`: 5
  - `iFriendlyHealChange`: 5
  - `bFastChant`: 1
  - `bPrereqAlive`: 1
  - `iCombatPercentDefense`: 10

### Mutated - 異形

- 内部名: `PROMOTION_MUTATED`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- 説明（ゲーム内ヘルプ）: 変異済み

### Heavy - 重量級

- 内部名: `PROMOTION_HEAVY`
- +%[戦闘力]: 30
- その他の設定:
  - `iWithdrawalChange`: -10
  - `bMutation`: 1
  - `iCombatPercentDefense`: 30
  - `OppositePromotions`: 軽量級

### Light - 軽量級

- 内部名: `PROMOTION_LIGHT`
- +%[戦闘力]: -10
- その他の設定:
  - `iMovesChange`: 1
  - `iMoveDiscountChange`: 1
  - `iWithdrawalChange`: 10
  - `bMutation`: 1
  - `iCombatPercentDefense`: -10
  - `OppositePromotions`: 重量級

### Strong - 怪力

- 内部名: `PROMOTION_STRONG`
- その他の設定:
  - `bMutation`: 1
  - `iExtraCombatStr`: 1
  - `iExtraCombatDefense`: 1
  - `OppositePromotions`: 非力

### Weak - 非力

- 内部名: `PROMOTION_WEAK`
- +%[戦闘力]: -25
- その他の設定:
  - `bMutation`: 1
  - `iCombatPercentDefense`: -25
  - `OppositePromotions`: 怪力

### Vulnerable to Fire - 可燃性

- 内部名: `PROMOTION_VULNERABLE_TO_FIRE`
- その他の設定:
  - `bMutation`: 1
  - `DamageTypeResists`: 火炎 iResist=-50

### Buccaneers - 乗組員- 荒くれ

- 内部名: `PROMOTION_BUCCANEERS`
- 対象の兵科: 海軍ユニット
- +%[戦闘力]: 30
- その他の設定:
  - `iVisibilityChange`: 1
  - `iAirRangeChange`: 1
  - `iEnemyHealChange`: 10
  - `iNeutralHealChange`: 10
  - `iFriendlyHealChange`: 10
  - `iCombatPercentDefense`: 30

### Longshoremen - 乗組員- 船乗り

- 内部名: `PROMOTION_LONGSHOREMEN`
- 対象の兵科: 海軍ユニット
- +%[戦闘力]: -30
- その他の設定:
  - `iVisibilityChange`: 2
  - `iMovesChange`: 1

### Skeleton Crew - 乗組員- 最小限

- 内部名: `PROMOTION_SKELETON_CREW`
- 対象の兵科: 海軍ユニット
- +%[戦闘力]: -30
- その他の設定:
  - `iCargoChange`: 2
  - `iCombatPercentDefense`: -30

### Bronze Weapons - 青銅の武器

- 内部名: `PROMOTION_BRONZE_WEAPONS`
- 必要テクノロジー: 採鉱
- その他の設定:
  - `DamageTypeCombats`: 武器 iCombat=1
  - `DamageTypeResists`: 電撃 iResist=-25
  - `BonusAffinities`: 銅 iAffinity=10

### Iron Weapons - 鉄の武器

- 内部名: `PROMOTION_IRON_WEAPONS`
- 必要テクノロジー: 製錬
- その他の設定:
  - `PromotionCombatType`: 青銅の武器
  - `iPromotionCombatMod`: 10
  - `DamageTypeCombats`: 武器 iCombat=2
  - `DamageTypeResists`: 電撃 iResist=-25
  - `BonusAffinities`: 鉄 iAffinity=25

### Mithril Weapons - ミスリルの武器

- 内部名: `PROMOTION_MITHRIL_WEAPONS`
- 必要テクノロジー: ミスリルの武具
- その他の設定:
  - `PromotionCombatType`: 鉄の武器
  - `iPromotionCombatMod`: 30
  - `DamageTypeCombats`: 武器 iCombat=3
  - `BonusAffinities`: ミスリル iAffinity=100

### Scorpion Clan - 蠍一族

- 内部名: `PROMOTION_SCORPION_CLAN`
- 対象の兵科: 弓術ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iUpgradeDiscount`: 50
  - `DamageTypeCombats`: 毒 iCombat=1

### Nomad - 砂漠の民

- 内部名: `PROMOTION_NOMAD`
- その他の設定:
  - `iVisibilityChange`: 1
  - `TerrainWorks`: 砂漠 iTerrainWork=25
  - `TerrainAttacks`: 砂漠 iTerrainAttack=20
  - `TerrainDefenses`: 砂漠 iTerrainDefense=20
  - `TerrainDoubleMoves`: 砂漠

### Winterborn - 寒冷種

- 内部名: `PROMOTION_WINTERBORN`
- 説明（ゲーム内ヘルプ）: 猛吹雪のダメージを無力化する
- その他の設定:
  - `TerrainWorks`: 氷原 iTerrainWork=25 / 凍土 iTerrainWork=25
  - `TerrainAttacks`: 氷原 iTerrainAttack=20 / 凍土 iTerrainAttack=20
  - `TerrainDefenses`: 氷原 iTerrainDefense=20 / 凍土 iTerrainDefense=20
  - `DamageTypeResists`: 冷気 iResist=20 / 火炎 iResist=-20

### Angel - 天使

- 内部名: `PROMOTION_ANGEL`
- その他の設定:
  - `bFastChant`: 1
  - `bImmuneToFear`: 1
  - `bNotAlive`: 1
  - `bRace`: 1
  - `DamageTypeResists`: 死 iResist=50 / 火炎 iResist=20 / 神聖 iResist=100 / 毒 iResist=100

### Avatar - 化身

- 内部名: `PROMOTION_AVATAR`
- その他の設定:
  - `bAlwaysHeal`: 1
  - `iVisibilityChange`: 3
  - `bFastChant`: 1
  - `bImmuneToCapture`: 1
  - `bImmuneToFear`: 1
  - `bImmuneToMagic`: 1
  - `bNotAlive`: 1
  - `bRace`: 1
  - `iBetterDefenderThanPercent`: 1000
  - `iCasterResistModify`: -50

### Centaur - ケンタウロス

- 内部名: `PROMOTION_CENTAUR`
- その他の設定:
  - `bRace`: 1
  - `ImmuneToPromotions`: ナイトメア

### Demon - 魔族

- 内部名: `PROMOTION_DEMON`
- その他の設定:
  - `TerrainAttacks`: 死滅の大地 iTerrainAttack=10 / 破滅の原野 iTerrainAttack=10 / 灼熱の砂地 iTerrainAttack=10
  - `TerrainDefenses`: 死滅の大地 iTerrainDefense=10 / 破滅の原野 iTerrainDefense=10 / 灼熱の砂地 iTerrainDefense=10
  - `bFastChant`: 1
  - `bImmuneToFear`: 1
  - `bNotAlive`: 1
  - `bRace`: 1
  - `DamageTypeResists`: 死 iResist=100 / 火炎 iResist=20 / 神聖 iResist=-25 / 毒 iResist=100 / 不浄 iResist=100

### Dragon - ドラゴン

- 内部名: `PROMOTION_DRAGON`
- その他の設定:
  - `bImmuneToFear`: 1
  - `bRace`: 1

### Dwarven - ドワーフ

- 内部名: `PROMOTION_DWARF`
- その他の設定:
  - `bHillsDoubleMove`: 1
  - `bRace`: 1
  - `iWorkRateModify`: 25
  - `DamageTypeResists`: 毒 iResist=25

### Elemental - 精霊

- 内部名: `PROMOTION_ELEMENTAL`
- その他の設定:
  - `bImmuneToFear`: 1
  - `bNotAlive`: 1
  - `bRace`: 1
  - `DamageTypeResists`: 死 iResist=100 / 毒 iResist=100

### Elven - エルフ

- 内部名: `PROMOTION_ELF`
- その他の設定:
  - `FeatureAttacks`: 森林 iFeatureAttack=10 / 古代樹林 iFeatureAttack=10
  - `FeatureDefenses`: 森林 iFeatureDefense=10 / 古代樹林 iFeatureDefense=10
  - `FeatureDoubleMoves`: 森林 / 古代樹林
  - `bRace`: 1
  - `iWorkRateModify`: -10
  - `DamageTypeResists`: 冷気 iResist=-25

### Elven - エルフ

- 内部名: `PROMOTION_DARK_ELF`
- その他の設定:
  - `FeatureAttacks`: 森林 iFeatureAttack=10 / 古代樹林 iFeatureAttack=10
  - `FeatureDefenses`: 森林 iFeatureDefense=10 / 古代樹林 iFeatureDefense=10
  - `FeatureDoubleMoves`: 森林 / 古代樹林
  - `bRace`: 1
  - `iWorkRateModify`: -10
  - `DamageTypeResists`: 冷気 iResist=-25

### Frostling - フロストリング

- 内部名: `PROMOTION_FROSTLING`
- 説明（ゲーム内ヘルプ）: 猛吹雪のダメージを無力化する
- その他の設定:
  - `TerrainAttacks`: 氷原 iTerrainAttack=25 / 凍土 iTerrainAttack=10 / 砂漠 iTerrainAttack=-25 / 湿地 iTerrainAttack=-25
  - `TerrainDefenses`: 氷原 iTerrainDefense=25 / 凍土 iTerrainDefense=10 / 砂漠 iTerrainDefense=-25 / 湿地 iTerrainDefense=-25
  - `bRace`: 1
  - `DamageTypeCombats`: 冷気 iCombat=1
  - `DamageTypeResists`: 冷気 iResist=100 / 火炎 iResist=-50

### Goblin - ゴブリン

- 内部名: `PROMOTION_GOBLIN`
- その他の設定:
  - `FeatureAttacks`: 密林 iFeatureAttack=10 / 深い密林 iFeatureAttack=10
  - `bRace`: 1
  - `iWorkRateModify`: -10
  - `DamageTypeResists`: 火炎 iResist=25

### Golem - ゴーレム

- 内部名: `PROMOTION_GOLEM`
- その他の設定:
  - `bAlwaysHeal`: 1
  - `iEnemyHealChange`: 10
  - `iNeutralHealChange`: 10
  - `iFriendlyHealChange`: 10
  - `bFastChant`: 1
  - `bImmuneToFear`: 1
  - `bMechanized`: 1
  - `bNotAlive`: 1
  - `bRace`: 1
  - `DamageTypeResists`: 死 iResist=100 / 毒 iResist=100

### Illusion - 幻影

- 内部名: `PROMOTION_ILLUSION`
- その他の設定:
  - `bFastChant`: 1
  - `bNotAlive`: 1
  - `bRace`: 1
  - `iCombatHealPercent`: 100
  - `iCombatLimitCap`: 90
  - `PromotionSummonPerk`: 幻影
  - `DamageTypeResists`: 死 iResist=100 / 毒 iResist=100

### Lizardman - リザードマン

- 内部名: `PROMOTION_LIZARDMAN`
- その他の設定:
  - `bAmphib`: 1
  - `bRiver`: 1
  - `TerrainAttacks`: 氷原 iTerrainAttack=-20 / 凍土 iTerrainAttack=-20 / 湿地 iTerrainAttack=10
  - `TerrainDefenses`: 氷原 iTerrainDefense=-20 / 凍土 iTerrainDefense=-20 / 湿地 iTerrainDefense=10
  - `FeatureAttacks`: 密林 iFeatureAttack=10 / 深い密林 iFeatureAttack=10
  - `FeatureDefenses`: 密林 iFeatureDefense=10 / 深い密林 iFeatureDefense=10
  - `TerrainDoubleMoves`: 湿地
  - `FeatureDoubleMoves`: 深い密林 / 密林
  - `bRace`: 1
  - `iWorkRateModify`: -10
  - `DamageTypeResists`: 冷気 iResist=-20 / 毒 iResist=20

### Ogre - オーガ

- 内部名: `PROMOTION_OGRE`
- その他の設定:
  - `FeatureAttacks`: 密林 iFeatureAttack=10 / 深い密林 iFeatureAttack=10
  - `bRace`: 1
  - `iWorkRateModify`: -10
  - `DamageTypeResists`: 火炎 iResist=25

### Orcish - オーク

- 内部名: `PROMOTION_ORC`
- その他の設定:
  - `FeatureAttacks`: 密林 iFeatureAttack=10 / 深い密林 iFeatureAttack=10
  - `bRace`: 1
  - `DamageTypeResists`: 火炎 iResist=25

### Puppet - 人形

- 内部名: `PROMOTION_PUPPET`
- +%[戦闘力]: -20
- その他の設定:
  - `bImmuneToFear`: 1
  - `bNotAlive`: 1
  - `bRace`: 1
  - `iCasterResistModify`: 40
  - `iSpellDamageModify`: -30
  - `PromotionSummonPerk`: 人形
  - `DamageTypeResists`: 死 iResist=100 / 毒 iResist=100

### Undead - 屍人

- 内部名: `PROMOTION_UNDEAD`
- その他の設定:
  - `bImmuneToFear`: 1
  - `bNotAlive`: 1
  - `bRace`: 1
  - `DamageTypeResists`: 死 iResist=100 / 神聖 iResist=-50 / 毒 iResist=100 / 不浄 iResist=50
  - `FeatureAttacks`: 悪霊の地 iFeatureAttack=30
  - `FeatureDefenses`: 悪霊の地 iFeatureDefense=30

### Great Commander - 偉大な指揮官の統率

- 内部名: `PROMOTION_GREAT_COMMANDER`
- 必要テクノロジー: Never
- 説明（ゲーム内ヘルプ）: 偉大な指揮官が合流した状態
- その他の設定:
  - `bImmortal`: 1
  - `iExtraCombatStr`: 1
  - `iExtraCombatDefense`: 1
  - `iFreeXPFromCombat`: 1

### Plant - 植物

- 内部名: `PROMOTION_PLANT`
- その他の設定:
  - `FeatureAttacks`: 森林 iFeatureAttack=100 / 古代樹林 iFeatureAttack=100
  - `bFastChant`: 1
  - `bImmuneToFear`: 1
  - `bRace`: 1
  - `DamageTypeResists`: 死 iResist=50 / 火炎 iResist=-50 / 毒 iResist=100

### Satyr - サテュロス

- 内部名: `PROMOTION_SATYR`
- その他の設定:
  - `FeatureAttacks`: 森林 iFeatureAttack=50 / 古代樹林 iFeatureAttack=50
  - `FeatureDefenses`: 森林 iFeatureDefense=50 / 古代樹林 iFeatureDefense=50
  - `FeatureDoubleMoves`: 森林 / 古代樹林
  - `bFastChant`: 1
  - `bRace`: 1
  - `DamageTypeResists`: 毒 iResist=100

### Kaijin - 壊人

- 内部名: `PROMOTION_KAIJIN_RACE`
- +%[戦闘力]: -10
- その他の設定:
  - `bImmuneToFear`: 1
  - `bRace`: 1
  - `iCombatPercentDefense`: -10
  - `ImmuneToPromotions`: 病気 / 疫病 / 黒死病
  - `DamageTypeResists`: 火炎 iResist=50 / 冷気 iResist=-50 / 毒 iResist=-50 / 死 iResist=50 / 神聖 iResist=-50 / 不浄 iResist=50

### Dragonling - 竜人

- 内部名: `PROMOTION_DRAGONLING`
- その他の設定:
  - `TerrainWorks`: 砂漠 iTerrainWork=10 / 氷原 iTerrainWork=10 / 凍土 iTerrainWork=10
  - `TerrainDefenses`: 砂漠 iTerrainDefense=25 / 凍土 iTerrainDefense=10 / 氷原 iTerrainDefense=10
  - `TerrainDoubleMoves`: 砂漠
  - `bRace`: 1
  - `DamageTypeResists`: 火炎 iResist=20 / 冷気 iResist=20

### Dimensional I - 次元Ⅰ

- 内部名: `PROMOTION_DIMENSIONAL1`
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `BonusPrereq`: 次元のマナ
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 次元Ⅱ

### Dimensional II - 次元Ⅱ

- 内部名: `PROMOTION_DIMENSIONAL2`
- 前提昇進: 次元Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iMovesChange`: 1
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 次元Ⅲ

### Dimensional III - 次元Ⅲ

- 内部名: `PROMOTION_DIMENSIONAL3`
- 前提昇進: 次元Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iMovesChange`: 1
  - `iMoveDiscountChange`: 2
  - `PromotionPrereqAnd`: 精神集中Ⅲ

### Dark Magic I - 暗黒魔法Ⅰ

- 内部名: `PROMOTION_DARK_MAGIC1`
- 対象の兵科: 秘術ユニット
- +%[戦闘力]: -10
- その他の設定:
  - `iCombatPercentDefense`: -10
  - `iSpellCasterXP`: 10
  - `BonusPrereq`: 古書物
  - `PromotionPrereqAnd`: 精神集中Ⅰ
  - `PromotionNextLevel`: 暗黒魔法Ⅱ

### Dark Magic II - 暗黒魔法Ⅱ

- 内部名: `PROMOTION_DARK_MAGIC2`
- 前提昇進: 暗黒魔法Ⅰ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- +%[戦闘力]: -15
- その他の設定:
  - `iCombatPercentDefense`: -15
  - `iSpellCasterXP`: 15
  - `PromotionPrereqAnd`: 精神集中Ⅱ
  - `PromotionNextLevel`: 暗黒魔法Ⅲ

### Dark Magic III - 暗黒魔法Ⅲ

- 内部名: `PROMOTION_DARK_MAGIC3`
- 前提昇進: 暗黒魔法Ⅱ
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- +%[戦闘力]: 15
- その他の設定:
  - `iCombatPercentDefense`: 15
  - `iCasterResistModify`: -5
  - `iSpellCasterXP`: 20
  - `PromotionPrereqAnd`: 精神集中Ⅲ
  - `PromotionNextLevel`: 暗黒魔法Ⅳ

### Dark Magic IV - 暗黒魔法Ⅳ

- 内部名: `PROMOTION_DARK_MAGIC4`
- 前提昇進: 暗黒魔法Ⅲ
- 対象の兵科: 秘術ユニット
- その他の設定:
  - `iCasterResistModify`: -5
  - `iExtraTargetLimit`: 1
  - `iSpellCasterXP`: 25
  - `PromotionPrereqAnd`: 精神集中Ⅲ

### Adventurer - 冒険者

- 内部名: `PROMOTION_ADVENTURER`
- 必要テクノロジー: 探検
- 対象の兵科: 偵察ユニット
- 説明（ゲーム内ヘルプ）: 必要条件: レベル3以上 / 巣窟や迷宮を探索した時に良い結果を得られる
- その他の設定:
  - `iMinLevel`: 3

### Tracking - 追跡

- 内部名: `PROMOTION_TRACKING`
- 前提昇進: 機動力Ⅰ
- 前提昇進(いずれか): エルフ
- 前提昇進(いずれか): リザードマン
- 対象の兵科: 弓術ユニット / 騎乗ユニット / 偵察ユニット
- 説明（ゲーム内ヘルプ）: 必要条件: レベル4以上
- その他の設定:
  - `bImmuneToFirstStrikes`: 1
  - `iMovesChange`: 1
  - `iMinLevel`: 4
  - `PromotionPrereqOr3`: エルフ
  - `PromotionPrereqOr4`: サテュロス

### Mimetism - 野戦

- 内部名: `PROMOTION_MIMETISM`
- 前提昇進(いずれか): 森番Ⅱ
- 前提昇進(いずれか): ゲリラⅡ
- 必要テクノロジー: 軍事行動
- 対象の兵科: 動物ユニット / 弓術ユニット / 魔獣ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 25
- その他の設定:
  - `iCityAttack`: -25
  - `iHillsAttack`: 25
  - `FeatureAttacks`: 深い密林 iFeatureAttack=25 / 密林 iFeatureAttack=25 / 森林 iFeatureAttack=25 / 古代樹林 iFeatureAttack=25 / 沼 iFeatureAttack=25
  - `PromotionPrereqOr3`: 戦闘Ⅳ
  - `PromotionPrereqOr4`: 教練Ⅳ

### Charge - 突撃

- 内部名: `PROMOTION_CHARGE`
- 前提昇進(いずれか): 戦闘Ⅳ
- 対象の兵科: 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 30
- その他の設定:
  - `iEnemyWithdrawalChange`: -20
  - `iChanceFirstStrikesChange`: 1
  - `iCollateralDamageProtection`: 20
  - `PromotionPrereqOr3`: 教練Ⅳ
  - `PromotionPrereqOr4`: 森番Ⅲ

### Longrange - 長射程

- 内部名: `PROMOTION_LONGRANGE`
- 前提昇進(いずれか): 弾幕Ⅰ
- 前提昇進(いずれか): 精密射撃
- 必要テクノロジー: 工学
- 対象の兵科: 弓術ユニット / 海軍ユニット / 攻城兵器
- その他の設定:
  - `iAirRangeChange`: 1
  - `iExtraCombatStr`: 1

### Necromancy - 屍霊術

- 内部名: `PROMOTION_NECROMANCY`
- 前提昇進: 精神集中Ⅱ
- 対象の兵科: 秘術ユニット
- 説明（ゲーム内ヘルプ）: 周辺1タイルで死亡した生物ユニットを配下に加える(20%) / (ただし世界ユニットは除く)
- その他の設定:
  - `iCombatHealPercent`: 10
  - `PromotionPrereqOr3`: 死Ⅰ

### Implacable - 執念

- 内部名: `PROMOTION_IMPLACABLE`
- 前提昇進: 屍人
- 必要テクノロジー: 狂信
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bAlwaysHeal`: 1
  - `iFirstStrikesChange`: 1
  - `iEnemyHealChange`: 15
  - `iNeutralHealChange`: 15
  - `iFriendlyHealChange`: 25
  - `PromotionPrereqOr3`: 戦闘Ⅴ
  - `bImmuneToCapture`: 1

### Musou - 無双

- 内部名: `PROMOTION_MUSOU`
- 対象の兵科: 白兵ユニット / 弓術ユニット / 偵察ユニット / 動物ユニット / 騎乗ユニット / 信奉ユニット / 秘術ユニット / 魔獣ユニット
- 説明（ゲーム内ヘルプ）: 必要条件: レベル20以上
- その他の設定:
  - `iExtraCombatStr`: 2
  - `iExtraCombatDefense`: 2
  - `iMinLevel`: 20

### Spell Expert - 達人

- 内部名: `PROMOTION_SPELL_EXPERT`
- 説明（ゲーム内ヘルプ）: 詠唱済みのターンに再び呪文を実行可能

### Tall - 長身

- 内部名: `PROMOTION_TALL`
- その他の設定:
  - `bExtraSeeFrom`: 1

### Skirmisher - 散兵

- 内部名: `PROMOTION_SKIRMISHER`
- 対象の兵科: 弓術ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iWithdrawalChange`: 15
  - `iBetterDefenderThanPercent`: 75

### Kod's Items - ダイヤモンドの武具

- 内部名: `PROMOTION_KODS_ITEMS`
- 説明（ゲーム内ヘルプ）: ターンの開始時に再生/武器強化/勇気/忠誠/石の皮膚の効果を自動的に得る / ターンの開始時に核撃の呪文を自動的に唱える(20%/ターン)
- その他の設定:
  - `iCollateralDamageProtection`: 20
  - `PromotionCombatType`: 天使
  - `iPromotionCombatMod`: 50
  - `DamageTypeResists`: 致死 iResist=500
  - `ImmuneToPromotions`: 異形 / 発狂 / 病気 / 疫病 / 衰弱 / 非力 / 黒死病 / 弱体化 / 睡眠 / 盲目 / 重力発生 / 蹄 / 四ツ目 / 殺戮衝動 / 甲殻 / 毒手

### Teleportation - 瞬間移動

- 内部名: `PROMOTION_TELEPORT`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iMovesChange`: 2
  - `iMoveDiscountChange`: 2
  - `bDispellable`: 1
  - `iExpireChance`: 100

### Replenishing - 充填

- 内部名: `PROMOTION_REPLENISHING`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bAlwaysHeal`: 1
  - `iEnemyHealChange`: 10
  - `iNeutralHealChange`: 10
  - `iFriendlyHealChange`: 10
  - `bDispellable`: 1
  - `bRemovedWhenHealed`: 1

### Untiring Flesh - 不屈の肉体

- 内部名: `PROMOTION_UNTIRING`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bBlitz`: 1
  - `iMovesChange`: 1
  - `iExpireChance`: 25

### Blighted - 破滅

- 内部名: `PROMOTION_BLIGHTED_TEMP_DROAUM`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iCombatPercentGlobalCounter`: 100
  - `iExpireChance`: 20

### Intensified I - 能力増幅Ⅰ

- 内部名: `PROMOTION_INTENSIFIED_1`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- +%[戦闘力]: 5
- 説明（ゲーム内ヘルプ）: 周囲1タイル以内に増幅を持つユニットの数だけ能力が強化される
- その他の設定:
  - `iCombatPercentDefense`: 5
  - `iSpellDamageModify`: 5
  - `PromotionSummonPerk`: 能力増幅Ⅰ
  - `PromotionNextLevel`: 能力増幅Ⅱ

### Intensified II - 能力増幅Ⅱ

- 内部名: `PROMOTION_INTENSIFIED_2`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- +%[戦闘力]: 5
- 説明（ゲーム内ヘルプ）: 周囲1タイル以内に増幅を持つユニットの数だけ能力が強化される
- その他の設定:
  - `iCombatPercentDefense`: 5
  - `iSpellDamageModify`: 5
  - `PromotionSummonPerk`: 能力増幅Ⅱ
  - `PromotionNextLevel`: 能力増幅Ⅲ

### Intensified III - 能力増幅Ⅲ

- 内部名: `PROMOTION_INTENSIFIED_3`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- +%[戦闘力]: 5
- 説明（ゲーム内ヘルプ）: 周囲1タイル以内に増幅を持つユニットの数だけ能力が強化される
- その他の設定:
  - `iChanceFirstStrikesChange`: 1
  - `iCombatPercentDefense`: 10
  - `iSpellDamageModify`: 5
  - `PromotionSummonPerk`: 能力増幅Ⅲ
  - `PromotionNextLevel`: 能力増幅Ⅳ
  - `iSpellCasterXP`: 5

### Intensified IV - 能力増幅Ⅳ

- 内部名: `PROMOTION_INTENSIFIED_4`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- +%[戦闘力]: 10
- 説明（ゲーム内ヘルプ）: 周囲1タイル以内に増幅を持つユニットの数だけ能力が強化される
- その他の設定:
  - `iChanceFirstStrikesChange`: 1
  - `iCombatPercentDefense`: 15
  - `iSpellDamageModify`: 5
  - `PromotionSummonPerk`: 能力増幅Ⅳ
  - `PromotionNextLevel`: 能力増幅Ⅴ
  - `iSpellCasterXP`: 5

### Intensified V - 能力増幅Ⅴ

- 内部名: `PROMOTION_INTENSIFIED_5`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- +%[戦闘力]: 15
- 説明（ゲーム内ヘルプ）: 周囲1タイル以内に増幅を持つユニットの数だけ能力が強化される
- その他の設定:
  - `iFirstStrikesChange`: 1
  - `iCombatPercentDefense`: 5
  - `iSpellDamageModify`: 5
  - `PromotionSummonPerk`: 能力増幅Ⅴ
  - `iSpellCasterXP`: 5

### Activation - 活性化

- 内部名: `PROMOTION_ACTIVATION`
- 対象の兵科: 信奉ユニット / 白兵ユニット
- +%[戦闘力]: 40
- その他の設定:
  - `bImmuneToFirstStrikes`: 1
  - `iCollateralDamageChange`: 20
  - `iChanceFirstStrikesChange`: 1
  - `bDispellable`: 1
  - `bPrereqAlive`: 1
  - `iCombatPercentDefense`: 40
  - `iExpireChance`: 33

### Gloom - 姿隠し

- 内部名: `PROMOTION_GLOOM`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 10
- その他の設定:
  - `iCityAttack`: 20
  - `iCombatPercentDefense`: 10
  - `Invisible`: INVISIBLE_STEALTH
  - `bRemovedByCasting`: 1
  - `bRemovedByCombat`: 1
  - `bTargetWeakestUnit`: 1

### Ire - 憤怒

- 内部名: `PROMOTION_IRE`
- 対象の兵科: 動物ユニット / 弓術ユニット / 魔獣ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 50
- その他の設定:
  - `bPrereqAlive`: 1
  - `iCombatPercentDefense`: -50
  - `iCombatPercentGlobalCounter`: 50
  - `iExpireChance`: 100
  - `iExtraCombatStr`: 1
  - `iExtraCombatDefense`: 1

### Fatigued II - 疲労Ⅱ

- 内部名: `PROMOTION_FATIGUED2`
- その他の設定:
  - `bPrereqAlive`: 1
  - `iExpireChance`: 15

### Sleep - 睡眠

- 内部名: `PROMOTION_SLEEP`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bPrereqAlive`: 1
  - `iResistMagic`: -50
  - `bHeld`: 1
  - `bRemovedByCombat`: 1
  - `iCombatPercentDefense`: -50
  - `iExpireChance`: 50
  - `iResistAgainstRemove`: 40

### Weaken - 弱体化

- 内部名: `PROMOTION_WEAKEN`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iExpireChance`: 50
  - `iResistAgainstRemove`: 30

### Pest - 黒死病

- 内部名: `PROMOTION_PEST`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- +%[戦闘力]: -30
- その他の設定:
  - `iEnemyHealChange`: -40
  - `iNeutralHealChange`: -40
  - `iFriendlyHealChange`: -40
  - `bPrereqAlive`: 1
  - `iCombatPercentDefense`: -30
  - `iExpireChance`: 5
  - `iResistAgainstRemove`: 50

### Instability - 不安定

- 内部名: `PROMOTION_INSTABILITY`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `PromotionRandomApply`: 狂暴
  - `iResistAgainstRemove`: 50

### Feral - 狂暴

- 内部名: `PROMOTION_FERAL`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- 説明（ゲーム内ヘルプ）: ユニットの操作はAIが行う（非常に攻撃的になる）
- その他の設定:
  - `iEnemyHealChange`: -20
  - `iNeutralHealChange`: -20
  - `iFriendlyHealChange`: -20
  - `bBerserk`: 1
  - `bImmuneToFear`: 1
  - `bRemovedByCombat`: 1
  - `iCombatPercentDefense`: -30
  - `iExpireChance`: 10
  - `iResistAgainstRemove`: 30

### Blind - 盲目

- 内部名: `PROMOTION_BLIND`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- +%[戦闘力]: -10
- その他の設定:
  - `iVisibilityChange`: -9
  - `iMoveDiscountChange`: -9
  - `bOnlyDefensive`: 1
  - `iCombatPercentDefense`: -10
  - `iExpireChance`: 25
  - `iResistAgainstRemove`: 40

### Sealed - 封印

- 内部名: `PROMOTION_SEALED`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: -10
- 説明（ゲーム内ヘルプ）: 詠唱済み状態になる
- その他の設定:
  - `bDispellable`: 1
  - `iCombatPercentDefense`: -10
  - `iResistAgainstRemove`: 40

### Terrified - 怯懦

- 内部名: `PROMOTION_TERRIFIED`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iExpireChance`: 50
  - `bOnlyDefensive`: 1

### Duskwood weapons - 薄闇樹の武器

- 内部名: `PROMOTION_DUSKWOOD`
- 対象の兵科: 弓術ユニット
- その他の設定:
  - `iAirCombatChange`: 1
  - `iAirCombatLimitChange`: 10
  - `iEnemyWithdrawalChange`: -5
  - `iCollateralDamageChange`: 10
  - `BonusPrereq`: 薄闇樹
  - `iDefensiveStrikeChance`: 5
  - `iDefensiveStrikeDamage`: 5

### Dragonmetal - 竜玉石の武器

- 内部名: `PROMOTION_DRAGONMETAL`
- 対象の兵科: 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット / 攻城兵器
- +%[戦闘力]: 10
- その他の設定:
  - `iCollateralDamageChange`: 10
  - `iFirstStrikesChange`: 1
  - `BonusPrereq`: 竜玉石
  - `iCombatPercentDefense`: 10

### Sorcery - 秘術師

- 内部名: `PROMOTION_SORCERY`
- その他の設定:
  - `iCasterResistModify`: -10
  - `iSpellDamageModify`: 10
  - `iSpellCasterXP`: 10

### Chanter - 詠唱者

- 内部名: `PROMOTION_CHANTER`
- 説明（ゲーム内ヘルプ）: 詠唱済みのターンに再び呪文を実行可能
- その他の設定:
  - `iSpellCasterXP`: 10

### Intensification - 増幅

- 内部名: `PROMOTION_INTENSIFICATION`
- 説明（ゲーム内ヘルプ）: 周囲1タイル以内の味方と中立ユニットを強化する
- その他の設定:
  - `iExtraCombatStr`: 1
  - `iExtraCombatDefense`: 1

### Collector - 蒐集

- 内部名: `PROMOTION_COLLECTOR`
- その他の設定:
  - `iGoldFromCombat`: 2
  - `iCombatCapturePercent`: 15

### Oshitari - 忍足

- 内部名: `PROMOTION_OSHITARI`
- その他の設定:
  - `iMovesChange`: 1
  - `iWithdrawalChange`: 10
  - `PromotionCombatType`: 屍人
  - `iPromotionCombatMod`: 20
  - `bValidate`: 1

### Pedigree - 血統

- 内部名: `PROMOTION_PEDIGREE`
- その他の設定:
  - `bFastChant`: 1
  - `iCasterResistModify`: -20
  - `iSpellDamageModify`: 20

### Survival - 残存

- 内部名: `PROMOTION_SURVIVAL`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iEnemyHealChange`: 10
  - `iNeutralHealChange`: 5
  - `bValidate`: 1

### Destruct System - 自爆装置

- 内部名: `PROMOTION_DESTRUCT_SYSTEM`
- 説明（ゲーム内ヘルプ）: 戦闘で死亡すると爆発で周辺ユニットにダメージを与える

### Stranger - 異邦人

- 内部名: `PROMOTION_STRANGER`
- その他の設定:
  - `iResistMagic`: -10
  - `DamageTypeResists`: 冷気 iResist=-50 / 死 iResist=50 / 火炎 iResist=50 / 神聖 iResist=-50 / 不浄 iResist=50

### Revenge - 復讐

- 内部名: `PROMOTION_REVENGER`
- 説明（ゲーム内ヘルプ）: 戦闘で死亡すると周辺の味方に士気を与える

### Herald's Call - 死の先触れ

- 内部名: `PROMOTION_HERALDS_CALL`
- 対象の兵科: 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iKamikazePercent`: 50
  - `bImmuneToCapture`: 1
  - `bImmuneToFear`: 1
  - `bPrereqAlive`: 1
  - `iFreeXPFromCombat`: 1
  - `DamageTypeCombats`: 神聖 iCombat=1
  - `DamageTypeResists`: 死 iResist=100

### Muramasa - ムラマサ

- 内部名: `PROMOTION_MURAMASA_BLADE_ECHIGO`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bBlitz`: 1
  - `iMovesChange`: 2
  - `iExtraCombatStr`: 2
  - `iExtraCombatDefense`: 2
  - `iFreeXPFromCombat`: 1
  - `BonusAffinities`: 呪付のマナ iAffinity=100

### Kabenuke - 壁抜け

- 内部名: `PROMOTION_KABENUKE_ECHIGO`
- 前提昇進(いずれか): 戦闘Ⅳ
- 必要テクノロジー: 軍事戦略
- 対象の兵科: 偵察ユニット
- その他の設定:
  - `CivilizationPrereq`: エチゴ
  - `iCityAttack`: 50
  - `PromotionPrereqOr3`: 教練Ⅳ

### Ikki Tousen - 一騎当千

- 内部名: `PROMOTION_IKKITOUSEN_ECHIGO`
- 前提昇進(いずれか): 戦闘Ⅳ
- 必要テクノロジー: 製錬
- 対象の兵科: 白兵ユニット
- その他の設定:
  - `CivilizationPrereq`: エチゴ
  - `iFirstStrikesChange`: 2
  - `PromotionPrereqOr3`: 教練Ⅳ

### Kuruma Gakari - 車懸の陣

- 内部名: `PROMOTION_KURUMA_ECHIGO`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット / 攻城兵器
- +%[戦闘力]: 20
- 説明（ゲーム内ヘルプ）: 周囲4タイル以内に直江山城守がいない場合はターン開始時に消滅
- その他の設定:
  - `iFirstStrikesChange`: 1

### Suikou - 錐行の陣

- 内部名: `PROMOTION_SUIKOU_ECHIGO`
- 必要テクノロジー: Never
- 対象の兵科: 白兵ユニット
- +%[戦闘力]: 40
- その他の設定:
  - `bImmuneToFear`: 1
  - `iExpireChance`: 100
  - `iMinLevel`: 5

### Houshi - 鋒矢の陣

- 内部名: `PROMOTION_HOUSHI_ECHIGO`
- 必要テクノロジー: Never
- 対象の兵科: 騎乗ユニット
- その他の設定:
  - `iMovesChange`: 3
  - `iExpireChance`: 100
  - `iMinLevel`: 5

### Kikkou - 亀甲陣

- 内部名: `PROMOTION_KIKKOU_ECHIGO`
- 必要テクノロジー: Never
- 対象の兵科: 弓術ユニット
- その他の設定:
  - `bImmuneToFirstStrikes`: 1
  - `iCityDefense`: 40
  - `iHillsDefense`: 25
  - `FeatureDefenses`: 密林 iFeatureDefense=50 / 森林 iFeatureDefense=50 / 古代樹林 iFeatureDefense=50
  - `bRemovedByCombat`: 1
  - `iMinLevel`: 5

### Mamori Gatana - 守り刀

- 内部名: `PROMOTION_MAMORI_ECHIGO`
- 必要テクノロジー: Never
- 対象の兵科: 信奉ユニット
- その他の設定:
  - `bRemovedByCombat`: 1
  - `iExtraCombatStr`: 1
  - `iMinLevel`: 5

### Houjutu - 砲術

- 内部名: `PROMOTION_HOUJUTU_ECHIGO`
- 必要テクノロジー: Never
- 対象の兵科: 攻城兵器
- その他の設定:
  - `iMovesChange`: 1
  - `iWithdrawalChange`: 15
  - `bRemovedByCombat`: 1
  - `iMinLevel`: 5

### Dragon Eater - 竜喰らい

- 内部名: `PROMOTION_DRAGON_EATER_DROAUM`
- その他の設定:
  - `bImmuneToFear`: 1
  - `iCombatHealPercent`: 10
  - `PromotionCombatType`: ドラゴン
  - `iPromotionCombatMod`: 100

### Dragon Scale - 竜鱗

- 内部名: `PROMOTION_DRAGON_SCALE_DROAUM`
- その他の設定:
  - `iFirstStrikesChange`: 2
  - `iExtraCombatDefense`: 10
  - `DamageTypeResists`: 冷気 iResist=50 / 死 iResist=50 / 火炎 iResist=50 / 神聖 iResist=50 / 電撃 iResist=50 / 毒 iResist=50 / 不浄 iResist=50

### Hero Skull - 英雄の頭蓋骨

- 内部名: `PROMOTION_HERO_SKULL_DROAUM`
- その他の設定:
  - `bFear`: 1
  - `iResistMagic`: 20
  - `iGroupSize`: 1

### Mental Derangement - 精神錯乱

- 内部名: `PROMOTION_MENTAL_DERANGEMENT_DROAUM`
- +%[戦闘力]: -30
- その他の設定:
  - `iWithdrawalChange`: -30
  - `iCityDefense`: -30
  - `iCollateralDamageProtection`: -30
  - `iCombatPercentDefense`: -30
  - `iDefensiveStrikeChance`: -15
  - `iDefensiveStrikeDamage`: -15
  - `iExpireChance`: 10

### Reservoirs - 病原巣

- 内部名: `PROMOTION_RESERVOIRS_DROAUM`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- +%[戦闘力]: -10
- その他の設定:
  - `iEnemyHealChange`: -5
  - `iNeutralHealChange`: -5
  - `iFriendlyHealChange`: -5
  - `bPrereqAlive`: 1
  - `iCombatPercentDefense`: -10
  - `PromotionCombatApply`: 病気

### Wild Animal - 野性

- 内部名: `PROMOTION_WILDANIMAL`
- 必要テクノロジー: 動物の馴致
- 対象の兵科: 動物ユニット / 魔獣ユニット
- +%[戦闘力]: 30
- その他の設定:
  - `CivilizationPrereq`: ニライカナイ
  - `bImmuneToCapture`: 1
  - `iCombatPercentDefense`: 30

### Buffalo - 野牛

- 内部名: `PROMOTION_BUFFALO`
- 前提昇進: 野性
- 対象の兵科: 動物ユニット / 魔獣ユニット
- その他の設定:
  - `CivilizationPrereq`: ニライカナイ
  - `iCityAttack`: 20
  - `UnitCombatMods`: 弓術ユニット iUnitCombatMod=40
  - `iMinLevel`: 3
  - `PromotionPrereqAnd`: 都市襲撃Ⅱ
  - `BonusAffinities`: トウモロコシ iAffinity=25 / 小麦 iAffinity=25

### Serpent - 大蛇

- 内部名: `PROMOTION_SERPENT`
- 前提昇進: 野性
- 対象の兵科: 動物ユニット / 魔獣ユニット
- その他の設定:
  - `CivilizationPrereq`: ニライカナイ
  - `UnitCombatMods`: 偵察ユニット iUnitCombatMod=10
  - `DamageTypeCombats`: 毒 iCombat=1
  - `iMinLevel`: 3
  - `PromotionPrereqAnd`: 森番Ⅱ
  - `BonusAffinities`: 牛 iAffinity=25 / 豚 iAffinity=25

### Mole - 土竜

- 内部名: `PROMOTION_MOLE`
- 前提昇進: 野性
- 対象の兵科: 動物ユニット / 魔獣ユニット
- その他の設定:
  - `CivilizationPrereq`: ニライカナイ
  - `iCityDefense`: 20
  - `UnitCombatMods`: 白兵ユニット iUnitCombatMod=40
  - `iMinLevel`: 3
  - `PromotionPrereqAnd`: ゲリラⅡ
  - `BonusAffinities`: オレンジ iAffinity=25 / レモン iAffinity=25

### Butterfly - 揚羽

- 内部名: `PROMOTION_BUTTERFLY`
- 前提昇進: 野性
- 対象の兵科: 動物ユニット / 魔獣ユニット
- その他の設定:
  - `CivilizationPrereq`: ニライカナイ
  - `iMoveDiscountChange`: 2
  - `iWithdrawalChange`: 25
  - `iChanceFirstStrikesChange`: 1
  - `iMinLevel`: 3
  - `PromotionPrereqAnd`: 機動力Ⅰ
  - `BonusAffinities`: ジャガイモ iAffinity=25 / 亜麻 iAffinity=25

### Hoodoo - 疫病神

- 内部名: `PROMOTION_HOODOO`
- 説明（ゲーム内ヘルプ）: 同じスタックのユニットに弱体化/生命力低下を与える
- その他の設定:
  - `iCombatPercentGlobalCounter`: 100
  - `ImmuneToPromotions`: 弱体化 / 生命力低下

### Flame - 紅蓮

- 内部名: `PROMOTION_YS_FLAME`
- 前提昇進(いずれか): 精神集中Ⅰ
- 前提昇進(いずれか): 精神集中Ⅱ
- 対象の兵科: 騎乗ユニット
- その他の設定:
  - `CivilizationPrereq`: イース
  - `iMinLevel`: 6
  - `BonusPrereq`: 炎のマナ
  - `DamageTypeCombats`: 火炎 iCombat=1

### Adamantine - 金剛

- 内部名: `PROMOTION_YS_ADAMANTINE`
- 前提昇進(いずれか): 精神集中Ⅰ
- 前提昇進(いずれか): 精神集中Ⅱ
- 対象の兵科: 白兵ユニット
- その他の設定:
  - `CivilizationPrereq`: イース
  - `iMinLevel`: 6
  - `BonusPrereq`: 太陽のマナ
  - `DamageTypeCombats`: 神聖 iCombat=1

### Wind - 旋風

- 内部名: `PROMOTION_YS_WIND`
- 前提昇進(いずれか): 精神集中Ⅰ
- 前提昇進(いずれか): 精神集中Ⅱ
- 対象の兵科: 弓術ユニット
- その他の設定:
  - `CivilizationPrereq`: イース
  - `iMinLevel`: 6
  - `BonusPrereq`: 自然のマナ
  - `DamageTypeCombats`: 電撃 iCombat=1

### Short Sword - ショートソード

- 内部名: `PROMOTION_YSSWORD1`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iChanceFirstStrikesChange`: 1
  - `iExtraCombatStr`: 1

### Battle Sword - バトルソード

- 内部名: `PROMOTION_YSSWORD2`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iChanceFirstStrikesChange`: 2
  - `iExtraCombatStr`: 2

### Silver Sword - シルバーソード

- 内部名: `PROMOTION_YSSWORD3`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iFirstStrikesChange`: 1
  - `iChanceFirstStrikesChange`: 2
  - `bImmuneToFear`: 1
  - `PromotionCombatType`: 魔族
  - `iPromotionCombatMod`: 50
  - `iExtraCombatStr`: 2
  - `DamageTypeCombats`: 神聖 iCombat=2

### Chain Mail - チェインメイル

- 内部名: `PROMOTION_YSARMOR1`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iExtraCombatDefense`: 1

### Battle Armor - バトルアーマー

- 内部名: `PROMOTION_YSARMOR2`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iExtraCombatDefense`: 2

### Cleria Armor - クレリアアーマー

- 内部名: `PROMOTION_YSARMOR3`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `PromotionCombatType`: 屍人
  - `iPromotionCombatMod`: 50
  - `bImmuneToDefensiveStrike`: 1
  - `bDoubleFortifyBonus`: 1
  - `iExtraCombatDefense`: 2
  - `DamageTypeCombats`: 神聖 iCombat=2

### Wood Shield - ウッドシールド

- 内部名: `PROMOTION_YSSHIELD1`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 10
- その他の設定:
  - `iWithdrawalChange`: 15
  - `iCombatPercentDefense`: 10
  - `iResistMagic`: 20
  - `DamageTypeResists`: 冷気 iResist=20 / 火炎 iResist=20 / 電撃 iResist=20 / 毒 iResist=20

### Battle Shield - バトルシールド

- 内部名: `PROMOTION_YSSHIELD2`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 20
- その他の設定:
  - `iWithdrawalChange`: 25
  - `iCombatPercentDefense`: 20
  - `iResistMagic`: 35
  - `DamageTypeResists`: 冷気 iResist=40 / 死 iResist=40 / 火炎 iResist=40 / 電撃 iResist=40 / 毒 iResist=40 / 不浄 iResist=40

### Cleria Shield - クレリアシールド

- 内部名: `PROMOTION_YSSHIELD3`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 30
- その他の設定:
  - `bImmuneToFirstStrikes`: 1
  - `iWithdrawalChange`: 40
  - `UnitCombatMods`: 魔獣ユニット iUnitCombatMod=50
  - `iCombatPercentDefense`: 30
  - `iResistMagic`: 50
  - `DamageTypeResists`: 冷気 iResist=60 / 死 iResist=60 / 火炎 iResist=60 / 電撃 iResist=60 / 神聖 iResist=60 / 毒 iResist=60 / 不浄 iResist=60
  - `DamageTypeCombats`: 神聖 iCombat=2

### Neckless of Sprite - 精霊の首飾り

- 内部名: `PROMOTION_YSNECKLESS`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bImmortal`: 1

### Mutant - 変異体

- 内部名: `PROMOTION_KAIJIN_MUTANT`
- 対象の兵科: 弓術ユニット / 偵察ユニット / 騎乗ユニット / 信奉ユニット / 秘術ユニット
- +%[戦闘力]: -15
- その他の設定:
  - `ImmuneToPromotions`: 衰弱 / 非力 / 生命力低下
  - `iCombatPercentDefense`: -15
  - `bFastChant`: 1
  - `bImmuneToMagic`: 1
  - `bPrereqAlive`: 1
  - `DamageTypeResists`: 火炎 iResist=-30 / 冷気 iResist=-30 / 毒 iResist=-30 / 死 iResist=50 / 神聖 iResist=-30 / 不浄 iResist=50
  - `iSpellCasterXP`: 40

### Abstraction - 自失

- 内部名: `PROMOTION_ABSTRACTION`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- 説明（ゲーム内ヘルプ）: ユニットの操作はAIが行う（非常に攻撃的になる）
- その他の設定:
  - `iMovesChange`: 3
  - `iWithdrawalChange`: 45
  - `bBerserk`: 1
  - `bImmuneToFear`: 1
  - `bPrereqAlive`: 1
  - `Invisible`: INVISIBLE_STEALTH
  - `bRemovedByCombat`: 1
  - `iExpireChance`: 80

### Low vitality - 生命力低下

- 内部名: `PROMOTION_LOW_VITALITY`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iEnemyHealChange`: -60
  - `iNeutralHealChange`: -60
  - `iFriendlyHealChange`: -60
  - `bPrereqAlive`: 1
  - `iExpireChance`: 50

### Draw lein - 馬持ち

- 内部名: `PROMOTION_DRAW_LEIN`
- 対象の兵科: 弓術ユニット / 信奉ユニット / 白兵ユニット / 偵察ユニット

### Riding on a horse - 騎乗状態

- 内部名: `PROMOTION_MOUNTED_HORSE`
- 対象の兵科: 弓術ユニット / 信奉ユニット / 白兵ユニット / 偵察ユニット
- その他の設定:
  - `bImmuneToFirstStrikes`: 1
  - `iMovesChange`: 2
  - `iWithdrawalChange`: 50
  - `iCityAttack`: -20
  - `iCombatPercentDefense`: -20

### Transport-Mode - 輸送形態

- 内部名: `PROMOTION_TRANSPORT_MODE`
- 対象の兵科: 攻城兵器
- その他の設定:
  - `iMoveDiscountChange`: 1
  - `iAirCombatChange`: -15
  - `iAirCombatLimitChange`: -200
  - `iBombardRateChange`: -200
  - `iCityAttack`: -50
  - `bOnlyDefensive`: 1
  - `iExtraCombatStr`: -10
  - `iExtraCombatDefense`: -10
  - `iGroupSize`: 2

### Commander - 指揮官

- 内部名: `PROMOTION_COMMANDER`
- 説明（ゲーム内ヘルプ）: ターンの開始時に統率の昇進を周囲3タイル以内の味方に与える

### Ardor - 熱血

- 内部名: `PROMOTION_ARDOR`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- その他の設定:
  - `iExpireChance`: 25
  - `iFreeXPFromCombat`: 1

### Military Leadership - 統率

- 内部名: `PROMOTION_MILITARY_LEADERSHIP`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- +%[戦闘力]: 20
- 説明（ゲーム内ヘルプ）: ターンの開始時に周囲3タイル以内に指揮官を持つユニットがいない場合は昇進を失う
- その他の設定:
  - `iCombatPercentDefense`: 20

### Freedman - 解放奴隷

- 内部名: `PROMOTION_FREEDMAN`
- その他の設定:
  - `iUpgradeDiscount`: 33
  - `iWorkRateModify`: 25

### Strong bow - 強弓

- 内部名: `PROMOTION_STRONGBOW`
- 前提昇進(いずれか): 戦闘Ⅱ
- 対象の兵科: 弓術ユニット
- その他の設定:
  - `CivilizationPrereq`: リネージ
  - `iAirCombatChange`: 1
  - `iAirCombatLimitChange`: 10
  - `iAirRangeChange`: 1
  - `PromotionPrereqOr3`: 教練Ⅱ

### Struggles - 死闘

- 内部名: `PROMOTION_STRUGGLES`
- 前提昇進(いずれか): 戦闘Ⅳ
- 対象の兵科: 白兵ユニット
- +%[戦闘力]: 40
- その他の設定:
  - `CivilizationPrereq`: リネージ
  - `bImmuneToFear`: 1
  - `PromotionPrereqOr3`: 教練Ⅳ

### Wind shield - 風の盾

- 内部名: `PROMOTION_WIND_SHIELD`
- 対象の兵科: 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iVisibilityChange`: -9
  - `iExtraCombatDefense`: 3
  - `DamageTypeResists`: 電撃 iResist=200

### Lesser Dragon - 下級ドラゴン

- 内部名: `PROMOTION_LESSER_DRAGON`
- その他の設定:
  - `bFastChant`: 1
  - `TerrainDefenses`: 砂漠 iTerrainDefense=25 / 凍土 iTerrainDefense=10 / 氷原 iTerrainDefense=10
  - `UnitCombatMods`: 動物ユニット iUnitCombatMod=40
  - `TerrainDoubleMoves`: 砂漠
  - `bImmuneToFear`: 1
  - `DamageTypeResists`: 火炎 iResist=20 / 冷気 iResist=20

### Elder Dragon - 上級ドラゴン

- 内部名: `PROMOTION_ELDER_DRAGON`
- その他の設定:
  - `bFastChant`: 1
  - `TerrainDefenses`: 砂漠 iTerrainDefense=25 / 凍土 iTerrainDefense=10 / 氷原 iTerrainDefense=10
  - `UnitCombatMods`: 動物ユニット iUnitCombatMod=40
  - `TerrainDoubleMoves`: 砂漠
  - `bImmuneToFear`: 1
  - `DamageTypeResists`: 火炎 iResist=20 / 冷気 iResist=20 / 毒 iResist=20 / 電撃 iResist=20

### Greater Dragon - 偉大なドラゴン

- 内部名: `PROMOTION_GREATER_DRAGON`
- その他の設定:
  - `iVisibilityChange`: 1
  - `bFastChant`: 1
  - `TerrainDefenses`: 砂漠 iTerrainDefense=25 / 凍土 iTerrainDefense=10 / 氷原 iTerrainDefense=10
  - `UnitCombatMods`: 動物ユニット iUnitCombatMod=40 / 魔獣ユニット iUnitCombatMod=40
  - `TerrainDoubleMoves`: 砂漠
  - `bImmuneToFear`: 1
  - `iExtraCombatStr`: 1
  - `iExtraCombatDefense`: 1
  - `DamageTypeResists`: 火炎 iResist=35 / 冷気 iResist=35 / 毒 iResist=35 / 電撃 iResist=35

### Ancient Dragon - 原初のドラゴン

- 内部名: `PROMOTION_ANCIENT_DRAGON`
- その他の設定:
  - `iVisibilityChange`: 1
  - `bFastChant`: 1
  - `TerrainDefenses`: 砂漠 iTerrainDefense=25 / 凍土 iTerrainDefense=10 / 氷原 iTerrainDefense=10
  - `UnitCombatMods`: 動物ユニット iUnitCombatMod=40 / 魔獣ユニット iUnitCombatMod=40
  - `TerrainDoubleMoves`: 砂漠
  - `bFear`: 1
  - `bImmuneToFear`: 1
  - `iExtraCombatStr`: 1
  - `iExtraCombatDefense`: 1
  - `ImmuneToPromotions`: 病気 / 疫病 / 黒死病
  - `DamageTypeResists`: 火炎 iResist=50 / 冷気 iResist=50 / 毒 iResist=50 / 電撃 iResist=50

### Fair Winds - 追い風

- 内部名: `PROMOTION_FAIR_WINDS_ALTAIR`
- 対象の兵科: 魔獣ユニット
- その他の設定:
  - `iMovesChange`: 1
  - `iExpireChance`: 20

### Mark of the Warden - 監視者の証

- 内部名: `PROMOTION_MARK_OF_THE_WARDEN`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- 説明（ゲーム内ヘルプ）: （監視者の証を持つユニットが誕生するとアルマゲドンカウンタが減少し、死亡すると増加します）

### Spiritual Hammer - 聖霊のハンマー

- 内部名: `PROMOTION_SPIRITUAL_HAMMER`
- 対象の兵科: 弓術ユニット / 信奉ユニット
- その他の設定:
  - `bDispellable`: 1
  - `iExpireChance`: 20
  - `DamageTypeCombats`: 神聖 iCombat=1
  - `iResistAgainstRemove`: 40

### Blessed of Agruonn - 鮮血の祝別

- 内部名: `PROMOTION_BLESSED_OF_AGRUONN`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bDispellable`: 1
  - `iExpireChance`: 10
  - `iFreeXPFromCombat`: 1
  - `DamageTypeCombats`: 毒 iCombat=1
  - `iResistAgainstRemove`: 80

### Bloody Blade - 血の刃

- 内部名: `PROMOTION_BLOODY_BLADE`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bBlitz`: 1
  - `iMovesChange`: 1
  - `bDispellable`: 1
  - `bImmuneToFear`: 1
  - `iCombatHealPercent`: 10
  - `iExpireChance`: 50
  - `DamageTypeCombats`: 不浄 iCombat=1
  - `iResistAgainstRemove`: 20

### Mechanical - 機械

- 内部名: `PROMOTION_MECHANICAL`
- その他の設定:
  - `BonusAffinities`: 精製されたマナ iAffinity=50

### Resident Machine Spirit - 機械魂宿し

- 内部名: `PROMOTION_RESIDENT_SPIRIT`
- 対象の兵科: 攻城兵器
- その他の設定:
  - `PromotionRandomApply`: 機械魂

### Machine Spirit - 機械魂

- 内部名: `PROMOTION_MACHINE_SPIRIT`
- 対象の兵科: 攻城兵器
- その他の設定:
  - `iMovesChange`: 1
  - `iAirCombatChange`: 2
  - `iAirRangeChange`: 1
  - `iCollateralDamageChange`: 20
  - `iCollateralDamageProtection`: 25
  - `bDispellable`: 1
  - `iExpireChance`: 20
  - `iExtraCombatStr`: 1
  - `iExtraCombatDefense`: 1
  - `iResistAgainstRemove`: 20

### Fed Creeper - 肥育された蔦

- 内部名: `PROMOTION_FED_CREEPER`
- その他の設定:
  - `iExpireChance`: 10
  - `DamageTypeCombats`: 死 iCombat=1

### Haunt form - 悪霊体

- 内部名: `PROMOTION_HAUNT`
- 対象の兵科: 偵察ユニット
- その他の設定:
  - `bBlitz`: 1
  - `bImmuneToFirstStrikes`: 1
  - `iMovesChange`: 1
  - `iWithdrawalChange`: 60
  - `iCityAttack`: -10
  - `FeatureDefenses`: 悪霊の地 iFeatureDefense=45
  - `FeatureDoubleMoves`: 悪霊の地
  - `iExpireChance`: 3
  - `bFlying`: 1
  - `Invisible`: INVISIBLE_STEALTH
  - `iBetrayalChance`: 5
  - `iCombatLimit`: 60
  - `ImmuneToPromotions`: 幽体

### Horned Dread Manifestation - 恐怖の顕現

- 内部名: `PROMOTION_HORNED_DREAD`
- その他の設定:
  - `FeatureDoubleMoves`: 悪霊の地
  - `ImmuneToPromotions`: 幽体 / 悪霊体

### Hauntstalk - 幽体

- 内部名: `PROMOTION_HAUNTSTALK`
- 対象の兵科: 偵察ユニット
- その他の設定:
  - `iMovesChange`: 1
  - `iFirstStrikesChange`: 1
  - `FeatureDoubleMoves`: 悪霊の地
  - `iExpireChance`: 20
  - `Invisible`: INVISIBLE_STEALTH

### Burrs - 毬

- 内部名: `PROMOTION_BURRS`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- 説明（ゲーム内ヘルプ）: ターン経過毎に30%の確率でダメージを受ける / 80%以上のダメージを負ったユニットは即死 / 都市外で死亡すると蛮族の伸びた蔦が産まれる
- その他の設定:
  - `bDispellable`: 1
  - `iExpireChance`: 10
  - `bPrereqAlive`: 1
  - `iResistAgainstRemove`: 40

### Geas - 制約

- 内部名: `PROMOTION_GEAS`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iWithdrawalChange`: -40
  - `iExpireChance`: 10
  - `iBetterDefenderThanPercent`: 100
  - `iCombatLimit`: 80
  - `iFreeXPFromCombat`: 1
  - `PromotionRandomApply`: 狂乱

### Glory of the Empire - 帝国の栄光

- 内部名: `PROMOTION_GLORY`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 20
- その他の設定:
  - `iExpireChance`: 100
  - `bImmuneToCapture`: 1
  - `iCombatCapturePercent`: 25
  - `iFreeXPFromCombat`: 1

### Ice Road - 氷の道

- 内部名: `PROMOTION_ICE_ROAD`
- 前提昇進(いずれか): フロストリング
- 必要テクノロジー: 神秘主義
- 対象の兵科: 秘術ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- 説明（ゲーム内ヘルプ）: ターン開始時に、周囲1タイルを寒冷化させる / （ニバル以外の友好的な文明や蛮族の文化圏内では効力を発揮しない）
- その他の設定:
  - `CivilizationPrereq`: ニバル
  - `TerrainAttacks`: 氷原 iTerrainAttack=25
  - `TerrainDefenses`: 氷原 iTerrainDefense=25
  - `FeatureAttacks`: 水晶原 iFeatureAttack=25
  - `FeatureDefenses`: 水晶原 iFeatureDefense=25
  - `FeatureDoubleMoves`: 水晶原

### Wearing of Snowstorm - 吹雪の衣

- 内部名: `PROMOTION_SNOWSTORM_AVATAR`
- 前提昇進(いずれか): 氷の道
- 必要テクノロジー: 自然との共生
- 対象の兵科: 秘術ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- 説明（ゲーム内ヘルプ）: ターン開始時に、周囲1タイルに猛吹雪を発生させることがある
- その他の設定:
  - `CivilizationPrereq`: ニバル
  - `TerrainAttacks`: 氷原 iTerrainAttack=25
  - `TerrainDefenses`: 氷原 iTerrainDefense=25
  - `FeatureAttacks`: 猛吹雪 iFeatureAttack=50
  - `FeatureDefenses`: 猛吹雪 iFeatureDefense=50
  - `FeatureDoubleMoves`: 猛吹雪

### Soul Hunger - 魂の飢餓

- 内部名: `PROMOTION_SOUL_HUNGER`
- 説明（ゲーム内ヘルプ）: ターン経過により経験値を失うことがある / （魂狩りはこの影響を受けない）

### Mercenaries Commander - 傭兵隊長

- 内部名: `PROMOTION_MERCENARIES_COMMANDER`
- 説明（ゲーム内ヘルプ）: ターン開始時に同じスタックのユニットに士気を与える

### Distinguished services - 勲功

- 内部名: `PROMOTION_MERCENARIES_RECRUITER`

### Ambition - 野心

- 内部名: `PROMOTION_AMBITION`
- その他の設定:
  - `ImmuneToPromotions`: 忠誠

### Yell I - 気合Ⅰ

- 内部名: `PROMOTION_YELL1`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 10
- 説明（ゲーム内ヘルプ）: 10%/ターンの確率で効果を失う
- その他の設定:
  - `bRemovedByCombat`: 1
  - `iCombatPercentDefense`: 10
  - `PromotionNextLevel`: 気合Ⅱ

### Yell II - 気合Ⅱ

- 内部名: `PROMOTION_YELL2`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 10
- 説明（ゲーム内ヘルプ）: 20%/ターンの確率で効果を失う
- その他の設定:
  - `bRemovedByCombat`: 1
  - `iCombatPercentDefense`: 10
  - `PromotionNextLevel`: 気合Ⅲ

### Yell III - 気合Ⅲ

- 内部名: `PROMOTION_YELL3`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 10
- 説明（ゲーム内ヘルプ）: 30%/ターンの確率で効果を失う
- その他の設定:
  - `bRemovedByCombat`: 1
  - `iCombatPercentDefense`: 10
  - `PromotionNextLevel`: 気合Ⅳ

### Yell IV - 気合Ⅳ

- 内部名: `PROMOTION_YELL4`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 10
- 説明（ゲーム内ヘルプ）: 40%/ターンの確率で効果を失う
- その他の設定:
  - `bRemovedByCombat`: 1
  - `iCombatPercentDefense`: 10
  - `PromotionNextLevel`: 気合Ⅴ

### Yell V - 気合Ⅴ

- 内部名: `PROMOTION_YELL5`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 10
- 説明（ゲーム内ヘルプ）: 50%/ターンの確率で効果を失う
- その他の設定:
  - `bRemovedByCombat`: 1
  - `iCombatPercentDefense`: 10

### Exaltation - 高揚

- 内部名: `PROMOTION_EXALTATION`
- 対象の兵科: 騎乗ユニット
- その他の設定:
  - `bBlitz`: 1
  - `bImmuneToFirstStrikes`: 1
  - `iWithdrawalChange`: -20
  - `bPrereqAlive`: 1
  - `bRemovedByCombat`: 1
  - `iExtraCombatStr`: 1
  - `bImmuneToFear`: 1
  - `iBetrayalChance`: 1

### Dimensional distortion - 次元歪曲

- 内部名: `PROMOTION_DIMENSIONAL_DISTORTION`
- その他の設定:
  - `iMovesChange`: 1
  - `iMoveDiscountChange`: 2
  - `bDispellable`: 1
  - `iExpireChance`: 10
  - `iResistAgainstRemove`: 20

### Great Race of Yith - イスの大いなる種族

- 内部名: `PROMOTION_GREATRACE`
- その他の設定:
  - `bFastChant`: 1
  - `bImmuneToFear`: 1

### Variant - 瘴烟

- 内部名: `PROMOTION_VARIANT`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット / 労働ユニット / 無能ユニット
- 説明（ゲーム内ヘルプ）: ターン開始時に3%の確率で、ユニットは変異により昇進を得る
- その他の設定:
  - `bValidate`: 1
  - `ImmuneToPromotions`: 病気 / 疫病 / 衰弱 / 非力 / 黒死病 / 弱体化 / 睡眠 / 盲目
  - `DamageTypeResists`: 死 iResist=100 / 火炎 iResist=-25 / 毒 iResist=25

### Parasitic - 寄生体

- 内部名: `PROMOTION_PARASITIC`
- 対象の兵科: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット / 攻城兵器
- 説明（ゲーム内ヘルプ）: ユニットが死亡するとドリュアスが生まれる / ドリュアスはバルドルアールヴまたは野生動物に帰属する
- その他の設定:
  - `bPrereqAlive`: 1
  - `iExpireChance`: 5
  - `iExpireChance`: 5

### Gravitation - 重力発生

- 内部名: `PROMOTION_GRAVITATION`
- その他の設定:
  - `UnitCombatMods`: 白兵ユニット iUnitCombatMod=20

### Hoof - 蹄

- 内部名: `PROMOTION_HOOF`
- その他の設定:
  - `iMoveDiscountChange`: 3
  - `UnitCombatMods`: 偵察ユニット iUnitCombatMod=-20

### Four eye - 四ツ目

- 内部名: `PROMOTION_FOUR_EYE`
- その他の設定:
  - `iVisibilityChange`: 1

### Slaughter Impulse - 殺戮衝動

- 内部名: `PROMOTION_SLAUGHTER_IMPULSER`
- +%[戦闘力]: 20
- その他の設定:
  - `iCombatPercentDefense`: -20

### Shell - 甲殻

- 内部名: `PROMOTION_SHELL`
- その他の設定:
  - `iExtraCombatDefense`: 1

### Hands of the Poison - 毒手

- 内部名: `PROMOTION_HAND_OF_THE_POISON`
- その他の設定:
  - `iSameTileHealChange`: -5
  - `DamageTypeCombats`: 毒 iCombat=1

### Muppet - 木偶

- 内部名: `PROMOTION_MUPPET`
- 説明（ゲーム内ヘルプ）: 一切の経験ポイントを得られない / 生物ユニットであっても魂の転生は発生しない
- その他の設定:
  - `UnitCombatMods`: 偵察ユニット iUnitCombatMod=40
  - `bImmuneToFear`: 1

### Angel-Pac - 天使の匣

- 内部名: `PROMOTION_ANGEL_PAC`
- 説明（ゲーム内ヘルプ）: 無生物ユニットでも魂の転生が発生する
- その他の設定:
  - `iCombatHealPercent`: 10
  - `iResistMagic`: 30
  - `DamageTypeResists`: 火炎 iResist=-20 / 神聖 iResist=-20 / 電撃 iResist=100 / 不浄 iResist=100

### Death March - 死の行進

- 内部名: `PROMOTION_DEATH_MARCH`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット / 無能ユニット
- その他の設定:
  - `iMovesChange`: 1
  - `iExpireChance`: 1
  - `iSpellDamageModify`: 5
  - `DamageTypeCombats`: 神聖 iCombat=1

### Murderous Frenzy I - 殺意の熱狂Ⅰ

- 内部名: `PROMOTION_MURDEROUS_FRENZY1`
- +%[戦闘力]: 5
- 説明（ゲーム内ヘルプ）: 勝利を重ねることで効果は強さを増していく
- その他の設定:
  - `iEnemyHealChange`: -5
  - `iNeutralHealChange`: -5
  - `iFriendlyHealChange`: -5
  - `bCarnivorous`: 1
  - `iCombatHealPercent`: 2
  - `iCombatPercentDefense`: 5
  - `iExpireChance`: 15
  - `PromotionNextLevel`: 殺意の熱狂Ⅱ

### Murderous Frenzy II - 殺意の熱狂Ⅱ

- 内部名: `PROMOTION_MURDEROUS_FRENZY2`
- +%[戦闘力]: 10
- 説明（ゲーム内ヘルプ）: 勝利を重ねることで効果は強さを増していく
- その他の設定:
  - `iEnemyHealChange`: -10
  - `iNeutralHealChange`: -10
  - `iFriendlyHealChange`: -10
  - `bCarnivorous`: 1
  - `iCombatHealPercent`: 4
  - `iCombatPercentDefense`: 10
  - `iExpireChance`: 15
  - `PromotionNextLevel`: 殺意の熱狂Ⅲ

### Murderous Frenzy III - 殺意の熱狂Ⅲ

- 内部名: `PROMOTION_MURDEROUS_FRENZY3`
- +%[戦闘力]: 15
- 説明（ゲーム内ヘルプ）: 勝利を重ねることで効果は強さを増していく
- その他の設定:
  - `iEnemyHealChange`: -15
  - `iNeutralHealChange`: -15
  - `iFriendlyHealChange`: -15
  - `bCarnivorous`: 1
  - `iCombatHealPercent`: 6
  - `iCombatPercentDefense`: 15
  - `iExpireChance`: 15
  - `PromotionNextLevel`: 殺意の熱狂Ⅳ

### Murderous Frenzy IV - 殺意の熱狂Ⅳ

- 内部名: `PROMOTION_MURDEROUS_FRENZY4`
- +%[戦闘力]: 20
- 説明（ゲーム内ヘルプ）: 勝利を重ねることで効果は強さを増していく
- その他の設定:
  - `iEnemyHealChange`: -20
  - `iNeutralHealChange`: -20
  - `iFriendlyHealChange`: -20
  - `bCarnivorous`: 1
  - `iCombatHealPercent`: 8
  - `iCombatPercentDefense`: 20
  - `iExpireChance`: 15
  - `PromotionNextLevel`: 殺意の熱狂Ⅴ

### Murderous Frenzy V - 殺意の熱狂Ⅴ

- 内部名: `PROMOTION_MURDEROUS_FRENZY5`
- +%[戦闘力]: 25
- その他の設定:
  - `iEnemyHealChange`: -25
  - `iNeutralHealChange`: -25
  - `iFriendlyHealChange`: -25
  - `bCarnivorous`: 1
  - `iCombatHealPercent`: 10
  - `iCombatPercentDefense`: 25
  - `iExpireChance`: 15

### Eternal Servitude - 永久の隷属

- 内部名: `PROMOTION_BRITTLE_BONES`
- その他の設定:
  - `iUpgradeDiscount`: 20
  - `iCombatPercentInBorders`: 10
  - `BonusAffinities`: 香木 iAffinity=50

### Patrol Fishing Boat - 巡視漁船

- 内部名: `PROMOTION_BASQUE`
- 説明（ゲーム内ヘルプ）: 海上巡視のみ可能
- その他の設定:
  - `bNoMaintenanceCost`: 1

### The Omen - 悪魔の子

- 内部名: `PROMOTION_DAMIEN`
- その他の設定:
  - `bImmuneToCapture`: 1
  - `bImmuneToFear`: 1
  - `bImmuneToMagic`: 1

### Earth Pulse - 地脈の戦槌

- 内部名: `PROMOTION_EARTH_PULSE`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bHillsDoubleMove`: 1
  - `iHillsDefense`: 40
  - `ImmuneToPromotions`: 武器の腐食
  - `OppositePromotions`: 武器の腐食
  - `BonusAffinities`: 大地のマナ iAffinity=100

### Glorious Shield - 栄光の盾

- 内部名: `PROMOTION_GLORIOUS_SHIELD`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bTargetWeakestUnitCounter`: 1
  - `iExtraCombatDefense`: 3
  - `iBetterDefenderThanPercent`: 100
  - `DamageTypeResists`: 死 iResist=50 / 不浄 iResist=50

### Bracelet of Nightmare - 夢魔の腕輪

- 内部名: `PROMOTION_BRACELET_OF_NIGHTMARE`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bAmphib`: 1
  - `bRiver`: 1
  - `UnitCombatMods`: 海軍ユニット iUnitCombatMod=100
  - `bWaterWalking`: 1
  - `FreeWaterWalkingTech`: 魔術

### Orb of Yggdrasil - 世界樹の宝珠

- 内部名: `PROMOTION_ORB_OF_YGGFRASIL`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bAlwaysHeal`: 1
  - `iEnemyHealChange`: 20
  - `iNeutralHealChange`: 20
  - `iFriendlyHealChange`: 20
  - `iSameTileHealChange`: 20

### Demon's Fang - 悪魔の牙

- 内部名: `PROMOTION_DEMONS_FANG`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bImmuneToFirstStrikes`: 1
  - `iGoldFromCombat`: 10

### Ring of the Sun - 太陽の指輪

- 内部名: `PROMOTION_RING_OF_THE_SUN`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iVisibilityChange`: 3
  - `SeeInvisible`: INVISIBLE_STEALTH
  - `PromotionCombatType`: 屍人
  - `iPromotionCombatMod`: 100

### Bloody Oath - 血塗れた誓いの剣

- 内部名: `PROMOTION_BLOODY_OATH`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bImmuneToFear`: 1
  - `iExtraCombatStr`: 2
  - `iResistMagic`: 100
  - `PromotionCombatApply`: 狂乱
  - `PromotionRandomApply`: 狂乱
  - `DamageTypeResists`: 冷気 iResist=100 / 死 iResist=100 / 火炎 iResist=100 / 神聖 iResist=100 / 電撃 iResist=100 / 物理 iResist=100 / 毒 iResist=100 / 不浄 iResist=100

### TXT_KEY_EQUIPMENT_PIKE_OF_TEARS - TXT_KEY_EQUIPMENT_PIKE_OF_TEARS

- 内部名: `PROMOTION_PIKE_OF_TEARS`
- その他の設定:
  - `bBlitz`: 1
  - `BonusAffinities`: 自然のマナ iAffinity=100 / 水のマナ iAffinity=100 / 生命のマナ iAffinity=100

### Heart Amulet - ハートの魔よけ

- 内部名: `PROMOTION_HEART_AMULET`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bAlwaysHeal`: 1
  - `iFriendlyHealChange`: 10
  - `iNeutralHealChange`: 10
  - `iEnemyHealChange`: 10

### Swift Boots - 早駆けブーツ

- 内部名: `PROMOTION_SWIFT_BOOTS`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iMovesChange`: 1

### Travellers Cloak - 旅行者の外套

- 内部名: `PROMOTION_TRAVELLERS_CLOAK`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bHillsDoubleMove`: 1
  - `TerrainDoubleMoves`: 砂漠 / 湿地
  - `FeatureDoubleMoves`: 森林 / 古代樹林 / 深い密林 / 密林 / 沼
  - `iMoveDiscountChange`: 2

### Ring of Perception - 知覚の指輪

- 内部名: `PROMOTION_RING_OF_PERCEPTION`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iVisibilityChange`: 2

### Ring of Striking - 打撃の指輪

- 内部名: `PROMOTION_RING_OF_STRIKING`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `iFirstStrikesChange`: 1
  - `bImmuneToFirstStrikes`: 1

### Cursed Token of Ragnarok - ラグナロクの呪われし証

- 内部名: `PROMOTION_CURSED_TOKEN_OF_RAGNAROK`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 20
- 説明（ゲーム内ヘルプ）: 魔物を呼び寄せる
- その他の設定:
  - `iCombatPercentDefense`: 20
  - `iCombatPercentGlobalCounter`: 200
  - `iExtraCombatStr`: -3
  - `iExtraCombatDefense`: -3
  - `iSameTileHealChange`: -10
  - `iModifyGlobalCounter`: 1
  - `DamageTypeCombats`: 不浄 iCombat=4

### Starvation Helm - 飢餓の兜

- 内部名: `PROMOTION_STARVATION_HELM`
- 対象の兵科: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット
- +%[戦闘力]: 20
- その他の設定:
  - `iEnemyHealChange`: -100
  - `iNeutralHealChange`: -100
  - `iFriendlyHealChange`: -100
  - `bFear`: 1
  - `bImmuneToFear`: 1
  - `iCombatPercentDefense`: 20
  - `iCombatHealPercent`: 30

### Kurikara - 倶利伽羅剣

- 内部名: `PROMOTION_KURIKARA`
- 対象の兵科: 白兵ユニット / 騎乗ユニット / 偵察ユニット
- その他の設定:
  - `bDoubleFortifyBonus`: 1
  - `bTargetWeakestUnitCounter`: 1
  - `iBetterDefenderThanPercent`: 100
  - `DamageTypeCombats`: 火炎 iCombat=1

### Winchester - ウィンチェスター

- 内部名: `PROMOTION_WINCHESTAR`
- 対象の兵科: 弓術ユニット / 攻城兵器
- その他の設定:
  - `iAirCombatChange`: 1
  - `iAirCombatLimitChange`: 10
  - `iCollateralDamageChange`: 40
