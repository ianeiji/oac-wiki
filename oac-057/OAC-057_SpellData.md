# OAC/呪文・特殊技能（0.57、XMLから生成）

- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）
- 生成元: `Units/CIV4SpellInfos.xml`
- 読み方: 主要な項目は日本語ラベル付きで先頭に、それ以外の既定値でない設定は「その他の設定」にXMLのタグ名のまま列挙する。値の内部名は日本語名に置き換えている。Pythonで実装された効果はXMLにないため含まない（ゲーム内ヘルプの説明文があれば載せている）。

### Add to City - 都市へ定住

- 内部名: `SPELL_ADD_TO_CITY`
- 実行ユニットクラス: マネス
- 説明（ゲーム内ヘルプ）: 都市へ定住し、人口に追加
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `iChangePopulation`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Add to Flesh Golem - 肉のゴーレムへ移植

- 内部名: `SPELL_ADD_TO_FLESH_GOLEM`
- 説明（ゲーム内ヘルプ）: ユニットが持つ昇進を肉のゴーレムへ追加 / 追加したユニットの戦闘力が肉のゴーレムより高い場合、肉のゴーレムの戦闘力を1増加させる
- その他の設定:
  - `UnitInStackPrereq`: 肉のゴーレム
  - `bCasterMustBeAlive`: 1
  - `bCasterNoDuration`: 1
  - `bIgnoreHasCasted`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `PyResult`: spellAddToFleshGolem
  - `PyRequirement`: reqAddToFleshGolem
  - `Effect`: Boom

### Add to Freak Show - 見世物小屋へ引き渡す

- 内部名: `SPELL_ADD_TO_FREAK_SHOW`
- 実行ユニットクラス: 奴隷
- 実行文明: バルセラフ
- 説明（ゲーム内ヘルプ）: ユニットを見世物小屋へ追加
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `PyResult`: spellAddToFreakShow
  - `PyRequirement`: reqAddToFreakShow
  - `Effect`: Boom

### Add to Wolf Pack - 狼の群れへ加わる

- 内部名: `SPELL_ADD_TO_WOLF_PACK`
- 実行ユニットクラス: 狼
- 実行文明: ドヴィエロ
- 説明（ゲーム内ヘルプ）: 狼を消費して狼の群れに強化の昇進を与える
- その他の設定:
  - `UnitInStackPrereq`: 狼の群れ
  - `bCasterNoDuration`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `PyResult`: spellAddToWolfPack
  - `PyRequirement`: reqAddToWolfPack
  - `Effect`: Boom

### Annex Lair - 巣窟を併呑

- 内部名: `SPELL_ANNEX_LAIR`
- 説明（ゲーム内ヘルプ）: 友好的な蛮族の巣窟から住民を都市へ移住させる / 廃墟、ゴブリン砦などの上で実行可能 / 巣窟は破壊される
- その他の設定:
  - `bInBordersOnly`: 1
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `PyResult`: spellAnnexLair
  - `PyRequirement`: reqAnnexLair
  - `PrereqOrUnits`: ランタイン / アセナの末裔 / 闘将
  - `Effect`: Boom

### Arcane Lacuna - 魔力消尽

- 内部名: `SPELL_ARCANE_LACUNA`
- 実行文明: アムリテ
- 説明（ゲーム内ヘルプ）: 配下の秘術ユニットが、ゲーム全体で展開されているマナノードに等しい数の経験値を得る / 他の文明は一時的に呪文を詠唱できなくなる
- その他の設定:
  - `UnitCombatPrereq`: 秘術ユニット
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellArcaneLacuna
  - `PyRequirement`: reqArcaneLacuna
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Ardor - 情熱

- 内部名: `SPELL_ARDOR`
- 実行文明: グリゴリ
- 説明（ゲーム内ヘルプ）: 輩出した偉人の数をリセット
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellArdor
  - `PyRequirement`: reqArdor
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Arena Battle - 闘技場に挑む

- 内部名: `SPELL_ARENA_BATTLE`
- 説明（ゲーム内ヘルプ）: 50%の確率でユニットが死亡 / 生き残れば経験値を取得 / 数ターン都市の満足が増加
- その他の設定:
  - `BuildingPrereq`: 闘技場
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `PyResult`: spellArenaBattle
  - `PyRequirement`: reqArenaBattle
  - `Effect`: Boom

### Blaze - 放火

- 内部名: `SPELL_BLAZE`
- 必要な昇進: 炎Ⅰ
- 説明（ゲーム内ヘルプ）: 可燃性の地物（森林、密林、灌木林）タイルに火を放つ
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `iPlotProbability`: 100
  - `bArson`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Scorch

### Bless - 祝別

- 内部名: `SPELL_BLESS`
- 必要な昇進: 精神集中Ⅱ
- 必要な昇進(2): 神術
- 必要な宗教: 秩序の修道会
- その他の設定:
  - `bHasCasted`: 1
  - `bImmuneNotAlive`: 1
  - `iAutomatePrecastPriority`: 40
  - `iAutomatePostcastPriority`: 1040
  - `AddPromotions`: 祝福
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Bless

### Blinding Light - 目眩ましの光

- 内部名: `SPELL_BLINDING_LIGHT`
- 必要な昇進: 太陽Ⅱ
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bResistable`: 1
  - `iResistModify`: 25
  - `iTargetLimitPerPlot`: 6
  - `iImmobileTurns`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `ImmunePromotions`: 看破の目
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Blinding Light

### Bloom - 花盛り

- 内部名: `SPELL_BLOOM`
- 必要な昇進: 精神集中Ⅱ
- 必要な昇進(2): 神術
- 必要な宗教: 緑葉の同胞
- その他の設定:
  - `bInBordersOnly`: 1
  - `bHasCasted`: 1
  - `iBuildDelay`: 2
  - `CreateFeatureType`: 若き森林
  - `iPlotProbability`: 100
  - `iAutomateTerrainPriority`: 100
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Bloom

### Blur - 陽炎

- 内部名: `SPELL_BLUR`
- 必要な昇進: 影Ⅰ
- その他の設定:
  - `bHasCasted`: 1
  - `iAutomatePostcastPriority`: 1040
  - `AddPromotions`: 陽炎
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Breathe Fire - 火炎の息

- 内部名: `SPELL_BREATH_FIRE`
- 必要な昇進: 原初のドラゴン
- 必要な昇進(2): ドラゴン
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 隕石
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Burning Blood - 燃えたぎる血

- 内部名: `SPELL_BURNING_BLOOD`
- 実行ユニット: モロイ
- その他の設定:
  - `bHasCasted`: 1
  - `bBuffCasterOnly`: 1
  - `AddPromotions`: 燃えたぎる血
  - `Effect`: Burning Blood

### Call Blizzard - 吹雪招来

- 内部名: `SPELL_CALL_BLIZZARD`
- 射程: 1
- 説明（ゲーム内ヘルプ）: 周囲のタイルを寒冷化させた上で猛吹雪を作成する
- その他の設定:
  - `bHasCasted`: 1
  - `PyResult`: spellCallBlizzard
  - `PyRequirement`: reqCallBlizzard
  - `iAutomatePrecastPriority`: 1
  - `PrereqOrUnits`: 冬の司祭 / 冬の司祭長
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Call Form - 魂寄せ

- 内部名: `SPELL_CALL_FORM`
- 実行ユニット: 人魂
- 説明（ゲーム内ヘルプ）: 魂の主たるユニットをこのタイルに呼び寄せる
- その他の設定:
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `PyResult`: spellCallForm
  - `PyRequirement`: reqCallForm
  - `bDisplayWhenDisabled`: 1
  - `bInterruptUnitCycling`: 1
  - `Effect`: Entropy Summon

### Call of the Grave - 墓場の呼び声

- 内部名: `SPELL_CALL_OF_THE_GRAVE`
- 実行ユニットクラス: 死の案内人
- 射程: 2
- 説明（ゲーム内ヘルプ）: 味方の全ての屍人ユニットを回復 / 3体の死霊を墓地から蘇らせる
- その他の設定:
  - `bHasCasted`: 1
  - `iDamage`: 20
  - `iDamageLimit`: 100
  - `DamageType`: 死
  - `CreateUnitType`: 死霊
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `PyResult`: spellCallOfTheGrave
  - `PyEnabled`: enabledCallOfTheGrave
  - `SecondarySpells`: 墓場の呼び声
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom
  - `EffectRangedPlot`: Sacrifice

### Charm Person - 魅了

- 内部名: `SPELL_CHARM_PERSON`
- 必要な昇進: 精神Ⅱ
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bResistable`: 1
  - `DamageType`: 催眠
  - `iResistModify`: 25
  - `iTargetLimitPerPlot`: 12
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 魅了
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Join Commander - 指揮官の合流

- 内部名: `SPELL_COMMANDER_JOIN`
- その他の設定:
  - `UnitInStackPrereq`: 偉大な指揮官
  - `bCasterNoDuration`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellCommanderJoin
  - `PyDisabled`: disabledCommanderJoin
  - `AddPromotions`: 偉大な指揮官の統率
  - `Effect`: Boom

### Join Commander - 指揮官の合流

- 内部名: `SPELL_COMMANDER_JOIN_DECIUS`
- その他の設定:
  - `UnitInStackPrereq`: デキウス
  - `bCasterNoDuration`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellCommanderJoinDecius
  - `PyDisabled`: disabledCommanderJoin
  - `AddPromotions`: 偉大な指揮官の統率
  - `Effect`: Boom

### Split Commander - 指揮官の分離

- 内部名: `SPELL_COMMANDER_SPLIT`
- 必要な昇進: 偉大な指揮官の統率
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellCommanderSplit
  - `RemovePromotions`: 偉大な指揮官の統率
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Consume Soul - 魂喰い

- 内部名: `SPELL_CONSUME_SOUL`
- 実行ユニット: 夢喰い
- その他の設定:
  - `BuildingPrereq`: 次元界の門
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bRemoveHasCasted`: 1
  - `bRemoveMadeAttack`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Wither

### Contagion - 感染

- 内部名: `SPELL_CONTAGION`
- 実行ユニットクラス: 病魔メアリー
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `bResistable`: 1
  - `iDamage`: 25
  - `iDamageLimit`: 40
  - `DamageType`: 死
  - `iResistModify`: 20
  - `bImmuneTeam`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 疫病
  - `ImmunePromotions`: 病気無効
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Convert City - 都市の割譲

- 内部名: `SPELL_CONVERT_CITY_BASIUM`
- 実行ユニットクラス: バシウム
- 説明（ゲーム内ヘルプ）: 都市を割譲させ、術者の文明に組み入れる
- その他の設定:
  - `BuildingPrereq`: マーキュリアンの門
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iCasterImmobileTurns`: 1
  - `PyResult`: spellConvertCityBasium
  - `PyRequirement`: reqConvertCityBasium
  - `Effect`: Boom

### Convert City - 都市の割譲

- 内部名: `SPELL_CONVERT_CITY_RANTINE`
- 実行ユニットクラス: ランタイン
- 説明（ゲーム内ヘルプ）: 都市を割譲させ、術者の文明に組み入れる
- その他の設定:
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iCasterImmobileTurns`: 1
  - `PyResult`: spellConvertCityRantine
  - `PyRequirement`: reqConvertCityRantine
  - `Effect`: Boom

### Courage - 勇気

- 内部名: `SPELL_COURAGE`
- 必要な昇進: 魂Ⅰ
- その他の設定:
  - `bHasCasted`: 1
  - `bImmuneNotAlive`: 1
  - `iAutomatePrecastPriority`: 60
  - `iAutomatePostcastPriority`: 1060
  - `AddPromotions`: 勇気
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Create Battering Ram - 破城槌の作成

- 内部名: `SPELL_CREATE_BATTERING_RAM`
- 必要な昇進: ドワーフ
- 実行文明: カザード
- その他の設定:
  - `UnitCombatPrereq`: 白兵ユニット
  - `FeatureOrPrereq1`: 森林
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 破城槌
  - `bPermanentUnitCreate`: 1
  - `PyResult`: spellCreateBatteringRam
  - `PyDisabled`: disabledCreateBatteringRam
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Create Den - 巣作り

- 内部名: `SPELL_CREATE_DEN_BEAR`
- 実行ユニットクラス: 熊
- 説明（ゲーム内ヘルプ）: 荒野に動物を解き放つ
- その他の設定:
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `CreateImprovementType`: 熊の巣穴
  - `iPlotProbability`: 100
  - `PyResult`: spellCreateDen
  - `PyDisabled`: disabledCreateDen
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Create Den - 巣作り

- 内部名: `SPELL_CREATE_DEN_LION`
- 実行ユニットクラス: ライオンの群れ
- 説明（ゲーム内ヘルプ）: 荒野に動物を解き放つ
- その他の設定:
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `CreateImprovementType`: ライオンのねぐら
  - `iPlotProbability`: 100
  - `PyResult`: spellCreateDen
  - `PyDisabled`: disabledCreateDen
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Create Puppet - 操り人形を作る

- 内部名: `SPELL_CREATE_PUPPET`
- 実行文明: バルセラフ
- その他の設定:
  - `UnitCombatPrereq`: 秘術ユニット
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 操り人形
  - `CreateUnitPromotion`: 人形
  - `bCopyCastersPromotions`: 1
  - `bPermanentUnitCreate`: 1
  - `Effect`: Boom

### Buccaneer Crew - 乗組員- 荒くれ

- 内部名: `SPELL_CREW_BUCCANEERS`
- 説明（ゲーム内ヘルプ）: 戦闘力: +30%、移動力: -1、回復率: +10%、射程修正: +1
- その他の設定:
  - `UnitCombatPrereq`: 海軍ユニット
  - `bBeforeMovementOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyDisabled`: disabledCrewBuccaneers
  - `AddPromotions`: 乗組員- 荒くれ
  - `RemovePromotions`: 乗組員- 船乗り / 乗組員- 最小限
  - `Effect`: Boom

### Longshoremen Crew - 乗組員- 船乗り

- 内部名: `SPELL_CREW_LONGSHOREMEN`
- 説明（ゲーム内ヘルプ）: 移動力: +1、積載量: -1、視界: +1、攻撃力: -10%
- その他の設定:
  - `UnitCombatPrereq`: 海軍ユニット
  - `bBeforeMovementOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyDisabled`: disabledCrewLongshoremen
  - `AddPromotions`: 乗組員- 船乗り
  - `RemovePromotions`: 乗組員- 荒くれ / 乗組員- 最小限
  - `Effect`: Boom

### Crew Normally - 乗組員- 標準的

- 内部名: `SPELL_CREW_NORMAL_CREW`
- その他の設定:
  - `UnitCombatPrereq`: 海軍ユニット
  - `bBeforeMovementOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyDisabled`: disabledCrewNormalCrew
  - `RemovePromotions`: 乗組員- 荒くれ / 乗組員- 船乗り / 乗組員- 最小限
  - `Effect`: Boom

### Skeleton Crew - 乗組員- 最小限

- 内部名: `SPELL_CREW_SKELETON_CREW`
- 説明（ゲーム内ヘルプ）: 積載量: +2、戦闘力: -30%
- その他の設定:
  - `UnitCombatPrereq`: 海軍ユニット
  - `bBeforeMovementOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyDisabled`: disabledCrewSkeletonCrew
  - `AddPromotions`: 乗組員- 最小限
  - `RemovePromotions`: 乗組員- 荒くれ / 乗組員- 船乗り
  - `Effect`: Boom

### Crown of Brilliance - 輝きの王冠

- 内部名: `SPELL_CROWN_OF_BRILLANCE`
- 必要な昇進: 精神集中Ⅲ
- 必要な昇進(2): 神術
- 必要な宗教: 至光なる天空
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `iDamage`: 30
  - `iDamageLimit`: 60
  - `DamageType`: 神聖
  - `iTargetLimitPerPlot`: 12
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `CastFlagPromotions`: 輝きの王冠
  - `BlockToCastPromotions`: 輝きの王冠
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Crush - 粉砕

- 内部名: `SPELL_CRUSH`
- 射程: 2
- 説明（ゲーム内ヘルプ）: 対象のタイルにいる全てのユニットに物理ダメージを与える
- その他の設定:
  - `bHasCasted`: 1
  - `iDamage`: 40
  - `iDamageLimit`: 75
  - `DamageType`: 物理
  - `iTargetLimitPerPlot`: 12
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `PrereqOrUnits`: ドワーフドルイド僧 / 覇竜ザッハーク
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom
  - `EffectRangedPlot`: Crush

### Cure Disease - 病気の治療

- 内部名: `SPELL_CURE_DISEASE`
- 必要な昇進: 衛生兵Ⅱ
- その他の設定:
  - `bHasCasted`: 1
  - `iAutomatePostcastPriority`: 1070
  - `RemovePromotions`: 病気 / 疫病 / 衰弱
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Dance of Blades - 剣の舞

- 内部名: `SPELL_DANCE_OF_BLADES`
- 必要な昇進: 混沌Ⅰ
- その他の設定:
  - `bHasCasted`: 1
  - `iFortifyTurns`: 5
  - `iAutomatePostcastPriority`: 1020
  - `AddPromotions`: 剣の舞
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Frosty swirling air flow

### Declare Nationality - 国籍宣言

- 内部名: `SPELL_DECLARE_NATIONALITY`
- 必要な昇進: 国籍秘匿
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyRequirement`: reqDeclareNationality
  - `RemovePromotions`: 国籍秘匿
  - `Effect`: Boom

### Destroy Undead - 屍人祓い

- 内部名: `SPELL_DESTROY_UNDEAD`
- 必要な昇進: 生命Ⅱ
- 射程: 1
- 説明（ゲーム内ヘルプ）: 周囲1タイル以内の全ての屍人ユニットに約30%のダメージ（上限100%） / 周囲1タイル以内の全ての悪魔ユニットに約15%のダメージ（上限50%）
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `iDamageLimit`: 100
  - `DamageType`: 神聖
  - `PromotionExclusiveDamages`: 屍人 iDamage=30
  - `SecondarySpells`: 屍人祓い
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom
  - `EffectRangedPlot`: Turn Undead

### Dispel Magic - 解呪

- 内部名: `SPELL_DISPEL_MAGIC`
- 必要な昇進: 超魔術Ⅱ
- 射程: 2
- 説明（ゲーム内ヘルプ）: マナノードを無色のマナに戻す
- その他の設定:
  - `bHasCasted`: 1
  - `DamageType`: 催眠
  - `iPlotProbability`: 100
  - `bDispel`: 1
  - `bDispelMana`: 1
  - `PyResult`: spellDispelMagic
  - `PyDisabled`: disabledDispelMagic
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Disrupt - 騒乱

- 内部名: `SPELL_DISRUPT`
- 実行ユニットクラス: ロキ
- 説明（ゲーム内ヘルプ）: 自国都市の文化の届く他国都市で実行可能 / 叛乱の可能性が少しでもあれば即座に叛乱開始
- その他の設定:
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iCasterImmobileTurns`: 1
  - `PyResult`: spellDisrupt
  - `PyRequirement`: reqDisrupt
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Divine Retribution - 天罰

- 内部名: `SPELL_DIVINE_RETRIBUTION`
- 実行ユニットクラス: バシウム
- 実行文明: マーキュリアン
- 説明（ゲーム内ヘルプ）: 世界の全ての魔族および屍人ユニットにダメージを与える
- その他の設定:
  - `bHasCasted`: 1
  - `bGlobal`: 1
  - `iDamageLimit`: 500
  - `DamageType`: 神聖
  - `PyRequirement`: reqDivineRetribution
  - `PromotionExclusiveDamages`: 魔族 iDamage=50 / 屍人 iDamage=50
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Domination - 服従

- 内部名: `SPELL_DOMINATION`
- 必要な昇進: 精神Ⅲ
- 必要な昇進(2): 精神集中Ⅲ
- 射程: 1
- 説明（ゲーム内ヘルプ）: 範囲内の敵ユニット1つを寝返らせる
- その他の設定:
  - `bHasCasted`: 1
  - `bResistable`: 1
  - `DamageType`: 催眠
  - `iResistModify`: 50
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `PyResult`: spellDomination
  - `PyRequirement`: reqDomination
  - `CastFlagPromotions`: 疲労Ⅱ
  - `BlockToCastPromotions`: 疲労Ⅱ
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Drown - 溺死の儀

- 内部名: `SPELL_DROWN`
- 実行ユニットクラス: 戦士
- その他の設定:
  - `BuildingPrereq`: 深海の神殿
  - `StateReligionPrereq`: 深海の旧支配者
  - `bCasterMustBeAlive`: 1
  - `bHasCasted`: 1
  - `iCost`: 60
  - `ConvertUnitType`: 深きものども
  - `PyDisabled`: disabledDrown
  - `Effect`: Boom

### Earthquake - 地震

- 内部名: `SPELL_EARTHQUAKE`
- 必要な昇進: 精神集中Ⅲ
- 必要な昇進(2): 神術
- 必要な宗教: キルモフのルーン
- 射程: 1
- 説明（ゲーム内ヘルプ）: 周囲1タイル以内のタイル整備と都市の建造物を破壊することがある / 範囲内の全てのユニットの固めた守りを崩す / 飛行ユニットには効果なし
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `bResistable`: 1
  - `iResistModify`: 20
  - `iPlotProbability`: 25
  - `bDestroyBuilding`: 1
  - `bDestroyImprovement`: 1
  - `iFortifyTurns`: -5
  - `PyDisabled`: disabledEarthquake
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Snowfall

### Enchant Spellstaff - 呪文の杖の作成

- 内部名: `SPELL_ENCHANT_SPELLSTAFF`
- 必要な昇進: 呪付Ⅲ
- その他の設定:
  - `bHasCasted`: 1
  - `iCasterImmobileTurns`: 1
  - `bBuffCasterOnly`: 1
  - `iAutomatePostcastPriority`: 1200
  - `AddPromotions`: 呪文の杖
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Swords Sparks

### Enchanted Blade - 呪付の刃

- 内部名: `SPELL_ENCHANTED_BLADE`
- 必要な昇進: 呪付Ⅰ
- その他の設定:
  - `bHasCasted`: 1
  - `iAutomatePrecastPriority`: 80
  - `iAutomatePostcastPriority`: 1080
  - `AddPromotions`: 呪付の刃
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Enchanted Blade

### Entangle - 絡め取り

- 内部名: `SPELL_ENTANGLE`
- 実行ユニット: ドルイド僧
- 射程: 1
- 説明（ゲーム内ヘルプ）: 範囲内のユニットの移動を封じる
- その他の設定:
  - `bHasCasted`: 1
  - `bResistable`: 1
  - `iResistModify`: 20
  - `iTargetLimitPerPlot`: 13
  - `iImmobileTurns`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneFlying`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Enter Portal - 転移門をくぐる

- 内部名: `SPELL_ENTER_PORTAL`
- 説明（ゲーム内ヘルプ）: ユニットを転移門の反対側に転移させる
- その他の設定:
  - `ImprovementPrereq`: 転移門
  - `bIgnoreHasCasted`: 1
  - `bHasCasted`: 1
  - `PyResult`: spellEnterPortal
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Entertain - 公演

- 内部名: `SPELL_ENTERTAIN`
- 実行ユニットクラス: ロキ
- 説明（ゲーム内ヘルプ）: 都市に一時的な幸福をもたらす（幸福の残る間は追加公演や騒乱は実行不可） / 都市タイルに術者文明の文化をもたらす / 術者は都市から人口2につき1を得る
- その他の設定:
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iCasterImmobileTurns`: 1
  - `PyResult`: spellEntertain
  - `PyRequirement`: reqEntertain
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Escape - 脱出

- 内部名: `SPELL_ESCAPE`
- 必要な昇進: 次元Ⅰ
- 説明（ゲーム内ヘルプ）: 一瞬で首都まで移動
- その他の設定:
  - `bIgnoreMadeAttack`: 1
  - `bHasCasted`: 1
  - `iCasterImmobileTurns`: 1
  - `PyResult`: spellEscape
  - `PyRequirement`: reqEscape
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Fair Winds - 追い風

- 内部名: `SPELL_FAIR_WINDS`
- 必要な昇進: 大気Ⅰ
- その他の設定:
  - `bHasCasted`: 1
  - `iAutomatePrecastPriority`: 120
  - `iAutomatePostcastPriority`: 1120
  - `AddPromotions`: 追い風
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Frosty swirling air flow

### Feast - 血の饗宴

- 内部名: `SPELL_FEAST`
- 必要な昇進: 吸血鬼
- 実行文明: カラビム
- 説明（ゲーム内ヘルプ）: 都市の人口を消費して経験値を取得
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `PyResult`: spellFeast
  - `PyRequirement`: reqFeast
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Sacrifice

### Feed - 吸血

- 内部名: `SPELL_FEED`
- 必要な昇進: 吸血鬼
- その他の設定:
  - `UnitInStackPrereq`: 血のしもべ
  - `bHasCasted`: 1
  - `iHealAmount`: 100
  - `bRemoveMadeAttack`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellFeed
  - `PyRequirement`: reqFeed
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Sacrifice

### Fireball - 火球

- 内部名: `SPELL_FIREBALL`
- 必要な昇進: 炎Ⅰ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 火球
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Flaming Arrows - 炎の矢

- 内部名: `SPELL_FLAMING_ARROWS`
- 必要な昇進: 呪付Ⅱ
- その他の設定:
  - `bHasCasted`: 1
  - `iAutomatePrecastPriority`: 100
  - `iAutomatePostcastPriority`: 1100
  - `AddPromotions`: 炎の矢
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Swords Sparks

### Floating Eye - 浮遊する眼の召喚

- 内部名: `SPELL_FLOATING_EYE`
- 必要な昇進: 超魔術Ⅰ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 浮遊する眼
  - `iAutomatePrecastPriority`: 2
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### For the Horde - 一族のために！

- 内部名: `SPELL_FOR_THE_HORDE`
- 実行文明: 残り火一族
- 説明（ゲーム内ヘルプ）: 世界中の蛮族オークユニットの半数を術者の文明に引き入れる
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellForTheHorde
  - `PyRequirement`: reqForTheHorde
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Form Wolf Pack - 狼の群れを成す

- 内部名: `SPELL_FORM_WOLF_PACK`
- 実行ユニットクラス: 狼
- 実行文明: ドヴィエロ
- 説明（ゲーム内ヘルプ）: 2匹の狼を消費して、狼の群れを作り出す
- その他の設定:
  - `UnitInStackPrereq`: 狼
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `ConvertUnitType`: 狼の群れ
  - `PyResult`: spellFormWolfPack
  - `Effect`: Boom

### Found Temple of Kilmorph - キルモフの神殿を建立

- 内部名: `SPELL_FOUND_TEMPLE_OF_KILMORPH`
- 実行ユニットクラス: キルモフの宝石番
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `CreateBuildingType`: キルモフの神殿
  - `SpreadReligion`: キルモフのルーン
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Found Temple of Leaves - 緑葉の神殿を建立

- 内部名: `SPELL_FOUND_TEMPLE_OF_LEAVES`
- 実行ユニットクラス: 緑葉の司祭
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `CreateBuildingType`: 緑葉の神殿
  - `SpreadReligion`: 緑葉の同胞
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Found Temple of the Empyrean - 至天の神殿を建立

- 内部名: `SPELL_FOUND_TEMPLE_OF_THE_EMPYREAN`
- 実行ユニットクラス: 至天の代行者
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `CreateBuildingType`: 至天の神殿
  - `SpreadReligion`: 至光なる天空
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Found Temple of the Order - 秩序の神殿を建立

- 内部名: `SPELL_FOUND_TEMPLE_OF_THE_ORDER`
- 実行ユニットクラス: 秩序の聴罪司祭
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `CreateBuildingType`: 秩序の神殿
  - `SpreadReligion`: 秩序の修道会
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Found Temple of the Overlords - 深海の神殿を建立

- 内部名: `SPELL_FOUND_TEMPLE_OF_THE_OVERLORDS`
- 実行ユニットクラス: 深海の狂信者
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `CreateBuildingType`: 深海の神殿
  - `SpreadReligion`: 深海の旧支配者
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Found Temple of the Veil - ヴェールの神殿を建立

- 内部名: `SPELL_FOUND_TEMPLE_OF_THE_VEIL`
- 実行ユニットクラス: ヴェールの儀式官
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `CreateBuildingType`: ヴェールの神殿
  - `SpreadReligion`: 蒼褪めたヴェール
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Gift Vampirism - 血族の盟約

- 内部名: `SPELL_GIFT_VAMPIRISM`
- 必要な昇進: 吸血鬼
- 説明（ゲーム内ヘルプ）: 同じタイルのユニットに吸血鬼を与える / 6レベル以上の生命を持つユニットに対してのみ有効
- その他の設定:
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `bImmuneNotAlive`: 1
  - `PyResult`: spellGiftVampirism
  - `PyRequirement`: reqGiftVampirism
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Gifts of Nantosuelta - ナントスエルタの贈り物

- 内部名: `SPELL_GIFTS_OF_NANTOSUELTA`
- 必要テクノロジー: 石工
- 実行文明: ルシュイアープ
- 説明（ゲーム内ヘルプ）: 全ての都市にゴールデンハンマーが出現
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellGiftsOfNantosuelta
  - `PyRequirement`: reqGiftsOfNantosuelta
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Give Hammer to Craftsman - 職人にハンマーを与える

- 内部名: `SPELL_GIVE_HAMMER_TO_CRAFTSMAN`
- 必要な昇進: PROMOTION_GOLDEN_HAMMER
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellGiveHammerToCraftsman
  - `RemovePromotions`: PROMOTION_GOLDEN_HAMMER
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Graft Flesh - 肉体移植

- 内部名: `SPELL_GRAFT_FLESH`
- 必要な昇進: 肉体Ⅲ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 肉のゴーレム
  - `bPermanentUnitCreate`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Haste - 快足

- 内部名: `SPELL_HASTE`
- 必要な昇進: 肉体Ⅰ
- その他の設定:
  - `bBeforeMovementOnly`: 1
  - `bHasCasted`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `bImmuneNotAlive`: 1
  - `iAutomatePrecastPriority`: 10
  - `AddPromotions`: 快足
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Frosty swirling air flow

### Hastur's Razor - ハスターの剃刀

- 内部名: `SPELL_HASTURS_RAZOR`
- 実行ユニットクラス: ヘマーハ
- 射程: 1
- 説明（ゲーム内ヘルプ）: 範囲内の全てのユニットのダメージを無作為に入れ替える
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `PyResult`: spellHastursRazor
  - `PyRequirement`: reqHastursRazor
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Heal - 治癒

- 内部名: `SPELL_HEAL`
- 必要な昇進: 衛生兵Ⅲ
- 説明（ゲーム内ヘルプ）: 同じタイルにいる全てのユニットを回復
- その他の設定:
  - `bHasCasted`: 1
  - `iHealAmount`: 20
  - `iTargetLimitPerPlot`: 16
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `bImmuneNotAlive`: 1
  - `iAutomatePostcastPriority`: 1060
  - `RemovePromotions`: 毒
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Healing Salve - 治癒の軟膏を塗る

- 内部名: `SPELL_HEALING_SALVE`
- 必要な昇進: PROMOTION_HEALING_SALVE
- その他の設定:
  - `bHasCasted`: 1
  - `PromotionCost`: PROMOTION_HEALING_SALVE
  - `bAbility`: 1
  - `iHealAmount`: 100
  - `PyDisabled`: disabledHealingSalve
  - `RemovePromotions`: 毒 / 病気 / 疫病 / 衰弱
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Hellfire - 地獄の業火

- 内部名: `SPELL_HELLFIRE`
- 必要な昇進: 精神集中Ⅲ
- 必要な昇進(2): 神術
- 実行文明: 地獄の軍勢
- 必要な宗教: 蒼褪めたヴェール
- 説明（ゲーム内ヘルプ）: 他の地獄の業火から2タイル以内では実行できない
- その他の設定:
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `CreateImprovementType`: 地獄の業火
  - `iPlotProbability`: 100
  - `PyDisabled`: disabledHellfire
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Entropy Summon

### Herald's Call - 死の先触れ

- 内部名: `SPELL_HERALDS_CALL`
- 実行ユニット: 御使い
- 説明（ゲーム内ヘルプ）: これらのユニットはターンの終わりに死亡する
- その他の設定:
  - `bHasCasted`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `bImmuneNotAlive`: 1
  - `PyResult`: spellHeraldsCall
  - `AddPromotions`: 死の先触れ
  - `ImmunePromotions`: 英雄
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Hide - 身を隠す

- 内部名: `SPELL_HIDE`
- 必要な昇進: 隠れる技能
- その他の設定:
  - `bIgnoreMadeAttack`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `AddPromotions`: 身隠し
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Hire Archer - 弓兵を雇う

- 内部名: `SPELL_HIRE_ARCHER`
- 必要テクノロジー: 弓術
- その他の設定:
  - `ImprovementPrereq`: ゴブリン砦
  - `bHasCasted`: 1
  - `iCost`: 60
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 弓兵
  - `CreateUnitPromotion`: 蠍一族
  - `bPermanentUnitCreate`: 1
  - `PyRequirement`: reqHireScorpionClan
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Hire Chariot - 戦車兵を雇う

- 内部名: `SPELL_HIRE_CHARIOT`
- 必要テクノロジー: 交易
- その他の設定:
  - `ImprovementPrereq`: ゴブリン砦
  - `bHasCasted`: 1
  - `iCost`: 90
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 狼の戦車兵
  - `CreateUnitPromotion`: 蠍一族
  - `bPermanentUnitCreate`: 1
  - `PyRequirement`: reqHireScorpionClan
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Hire Goblin - ゴブリンを雇う

- 内部名: `SPELL_HIRE_GOBLIN`
- その他の設定:
  - `ImprovementPrereq`: ゴブリン砦
  - `bHasCasted`: 1
  - `iCost`: 30
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: ゴブリン
  - `CreateUnitPromotion`: 蠍一族
  - `bPermanentUnitCreate`: 1
  - `PyRequirement`: reqHireScorpionClan
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Hire Units - ユニットを雇う

- 内部名: `SPELL_HIRE_UNITS`
- 実行ユニットクラス: マグナダイン
- 説明（ゲーム内ヘルプ）: 様々なユニットを金銭により自軍に加えることが出来る。 / 対象となるユニットは、傭騎兵、弓兵、斧兵、騎乗兵、長弓兵、勇士、弓騎兵、カタパルト。 / 加わったユニットには忠誠が与えられる。
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `PyResult`: spellHireUnits
  - `PyRequirement`: reqHireUnits
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Hire Wolf Rider - 狼の騎乗兵を雇う

- 内部名: `SPELL_HIRE_WOLF_RIDER`
- 必要テクノロジー: 騎乗
- その他の設定:
  - `ImprovementPrereq`: ゴブリン砦
  - `bHasCasted`: 1
  - `iCost`: 60
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 狼の騎乗兵
  - `CreateUnitPromotion`: 蠍一族
  - `bPermanentUnitCreate`: 1
  - `PyRequirement`: reqHireScorpionClan
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Hope - 希望

- 内部名: `SPELL_HOPE`
- 必要な昇進: 魂Ⅱ
- 説明（ゲーム内ヘルプ）: 都市の人々を啓発する（+4/ターン、+1、ユニットに勇気を与える）
- その他の設定:
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `CreateBuildingType`: 希望
  - `iAutomatePostcastPriority`: 1120
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Hyborem's Whisper - ハイボレムの囁き

- 内部名: `SPELL_HYBOREMS_WHISPER`
- 必要テクノロジー: 悪意の企み
- 実行ユニットクラス: ハイボレム
- 実行文明: 地獄の軍勢
- 説明（ゲーム内ヘルプ）: 蒼褪めたヴェールが布教された都市の統治権を奪い取る
- その他の設定:
  - `bHasCasted`: 1
  - `bGlobal`: 1
  - `PyResult`: spellHyboremsWhisper
  - `PyRequirement`: reqHyboremsWhisper
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Impersonate Leader - なりすまし

- 内部名: `SPELL_IMPERSONATE_LEADER`
- 実行ユニットクラス: ギボン・ゴエティア
- 説明（ゲーム内ヘルプ）: 数ターンの間、操作する文明を入れ替える
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `PyResult`: spellImpersonateLeader
  - `PyRequirement`: reqImpersonateLeader
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Inquisition - 宗教裁判

- 内部名: `SPELL_INQUISITION`
- 必要な昇進: 異端審問
- 説明（ゲーム内ヘルプ）: 都市から国教以外の宗教を排除
- その他の設定:
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iBuildDelay`: 3
  - `PyResult`: spellInquisition
  - `PyRequirement`: reqInquisition
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Inspiration - 閃き

- 内部名: `SPELL_INSPIRATION`
- 必要な昇進: 精神Ⅰ
- 説明（ゲーム内ヘルプ）: 都市の人々を啓発する（+2/ターン、+1/ターン: 賢者）
- その他の設定:
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `CreateBuildingType`: 閃き
  - `iAutomatePostcastPriority`: 1110
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Into the Mist - 霧の中へ

- 内部名: `SPELL_INTO_THE_MIST`
- 実行文明: シダー
- 説明（ゲーム内ヘルプ）: 配下の全てのユニットが身隠しを得る
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellIntoTheMist
  - `PyRequirement`: reqIntoTheMist
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Ira Unleashed - イラを解き放つ

- 内部名: `SPELL_IRA_UNLEASHED`
- 実行ユニットクラス: 復讐の化身
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 6
  - `CreateUnitType`: イラ
  - `bPermanentUnitCreate`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: EFFECT_ABADDON_DEVASTATE

### Kidnap - 誘拐

- 内部名: `SPELL_KIDNAP`
- 実行文明: スヴァルトアールヴ
- 説明（ゲーム内ヘルプ）: 都市から偉人ユニットを誘拐する
- その他の設定:
  - `UnitCombatPrereq`: 偵察ユニット
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bCausesWar`: 1
  - `iDelay`: 3
  - `PyResult`: spellKidnap
  - `PyRequirement`: reqKidnap
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Legends - 伝説

- 内部名: `SPELL_LEGENDS`
- 実行文明: クリオテイテ
- 説明（ゲーム内ヘルプ）: 領内の全ての都市で文化力が増加
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellLegends
  - `PyRequirement`: reqLegends
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Lichdom - 不死の秘法

- 内部名: `SPELL_LICHDOM`
- 必要な昇進: 死Ⅲ
- その他の設定:
  - `BuildingClassOwnedPrereq`: 屍霊の塔
  - `bHasCasted`: 1
  - `ConvertUnitType`: リッチ
  - `PyDisabled`: disabledLichdom
  - `BlockToCastPromotions`: 人形
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Loyalty - 忠誠

- 内部名: `SPELL_LOYALTY`
- 必要な昇進: 法Ⅰ
- その他の設定:
  - `bHasCasted`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `iAutomatePrecastPriority`: 50
  - `iAutomatePostcastPriority`: 1050
  - `AddPromotions`: 忠誠
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Maelstrom - 竜巻

- 内部名: `SPELL_MAELSTROM`
- 必要な昇進: 大気Ⅰ
- 射程: 2
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `iDamage`: 10
  - `iDamageLimit`: 25
  - `DamageType`: 電撃
  - `iTargetLimitPerPlot`: 8
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Maelstrom
  - `EffectRangedPlot`: Storm

### March of the Trees - 大樹の行進

- 内部名: `SPELL_MARCH_OF_THE_TREES`
- 必要テクノロジー: 深き森への道
- 実行文明: リョースアールヴ
- 説明（ゲーム内ヘルプ）: 数ターンの間、領内の全ての森林がトレントに変身する
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellMarchOfTheTrees
  - `PyRequirement`: reqMarchOfTheTrees
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Mask - 仮面

- 内部名: `SPELL_MASK`
- 必要な昇進: 狙撃
- 必要テクノロジー: 詐欺
- 必要な宗教: エススの枢密院
- その他の設定:
  - `bHasCasted`: 1
  - `bBuffCasterOnly`: 1
  - `PyDisabled`: disabledMask
  - `AddPromotions`: 国籍秘匿
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Mesmerize Animal - 動物惑乱

- 内部名: `SPELL_MEZMERIZE_ANIMAL`
- 実行ユニットクラス: サテュロス
- 射程: 1
- 説明（ゲーム内ヘルプ）: 周囲の動物ユニットを味方に引き入れる
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bResistable`: 1
  - `DamageType`: 催眠
  - `iResistModify`: 20
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `PyResult`: spellMezmerizeAnimal
  - `PyRequirement`: reqMezmerizeAnimal
  - `ImmunePromotions`: 野性
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Mirror - 写し身

- 内部名: `SPELL_MIRROR`
- 必要な昇進: PROMOTION_BLACK_MIRROR
- 説明（ゲーム内ヘルプ）: 術者の複製となる幻影ユニットを作り出す / 殺し屋アラズカンのみ2体作り出せる
- その他の設定:
  - `bCasterMustBeAlive`: 1
  - `bHasCasted`: 1
  - `PyResult`: spellMirror
  - `PyRequirement`: reqMirror
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Morale - 鼓舞

- 内部名: `SPELL_MORALE`
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `bImmuneNotAlive`: 1
  - `iAutomatePostcastPriority`: 1050
  - `PrereqOrUnits`: 旗手 / 上杉謙信 / 聖将上杉謙信 / 軍神上杉謙信 / 毘沙門天上杉謙信
  - `AddPromotions`: 士気
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Mother Lode - 母なる鉱脈

- 内部名: `SPELL_MOTHER_LODE`
- 必要テクノロジー: 採鉱
- 実行文明: カザード
- 説明（ゲーム内ヘルプ）: 領内の鉱山ひとつにつき25を得る / 領内の全ての平坦な地形がそれぞれ10%の確率で丘陵になる
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellMotherLode
  - `PyRequirement`: reqMotherLode
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Mutation - 変異

- 内部名: `SPELL_MUTATION`
- 必要な昇進: 混沌Ⅱ
- 説明（ゲーム内ヘルプ）: 変異に伴い、規定の昇進が無作為に与えられる
- その他の設定:
  - `bHasCasted`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 異形
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Open Chest - 宝箱を開ける

- 内部名: `SPELL_OPEN_CHEST`
- その他の設定:
  - `UnitInStackPrereq`: 宝箱
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `PyResult`: spellOpenChest
  - `PyRequirement`: reqTargetFree
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Open Chest - 宝箱を開ける

- 内部名: `SPELL_OPEN_CHEST_ADVENTURE_MODE`
- その他の設定:
  - `UnitInStackPrereq`: 宝箱
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `PyResult`: spellOpenChest
  - `PyRequirement`: reqTargetFree
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Peace - 和平

- 内部名: `SPELL_PEACE`
- 実行ユニットクラス: コーリンデール
- 説明（ゲーム内ヘルプ）: 他の全ての文明と和平する / アルマゲドンカウンタを半分にする
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `PyResult`: spellPeace
  - `PyRequirement`: reqPeace
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Peace - 和平

- 内部名: `SPELL_PEACE_SEVEN_PINES`
- 説明（ゲーム内ヘルプ）: 他の全ての文明と和平する / アルマゲドンカウンタを半分にする
- その他の設定:
  - `ImprovementPrereq`: 七本松
  - `bInBordersOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `PyResult`: spellPeaceSevenPines
  - `PyRequirement`: reqPeaceSevenPines
  - `Effect`: Creation Effect Dim

### Pillar of Fire - 燃え立つ火柱

- 内部名: `SPELL_PILLAR_OF_FIRE`
- 実行ユニットクラス: ハリッド・アストラケイン
- 射程: 2
- 説明（ゲーム内ヘルプ）: 対象の単一タイルにいる全てのユニットに火炎ダメージ / （対象は、射程内で最も多く敵ユニットがいるタイルが自動的に選択されます）
- その他の設定:
  - `bHasCasted`: 1
  - `iDamage`: 40
  - `iDamageLimit`: 80
  - `DamageType`: 火炎
  - `iTargetLimitPerPlot`: 14
  - `iPlotProbability`: 50
  - `bArson`: 1
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom
  - `EffectRangedPlot`: Pillar of Fire

### Poisoned Blade - 毒の刃

- 内部名: `SPELL_POISONED_BLADE`
- 必要な昇進: 自然Ⅱ
- その他の設定:
  - `bHasCasted`: 1
  - `bImmuneNeutral`: 1
  - `iAutomatePrecastPriority`: 90
  - `iAutomatePostcastPriority`: 1090
  - `AddPromotions`: 毒の刃
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Potion of Invisibility - 透明化の飲み薬を飲む

- 内部名: `SPELL_POTION_OF_INVISIBILITY`
- 必要な昇進: PROMOTION_POTION_OF_INVISIBILITY
- その他の設定:
  - `bHasCasted`: 1
  - `PromotionCost`: PROMOTION_POTION_OF_INVISIBILITY
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `AddPromotions`: 身隠し
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Potion of Restoration - 魔力回復の飲み薬を飲む

- 内部名: `SPELL_POTION_OF_RESTORATION`
- 必要な昇進: PROMOTION_POTION_OF_RESTORATION
- その他の設定:
  - `bIgnoreHasCasted`: 1
  - `PromotionCost`: PROMOTION_POTION_OF_RESTORATION
  - `bAbility`: 1
  - `bRemoveHasCasted`: 1
  - `bBuffCasterOnly`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Promote Settlement - 集落を都市に

- 内部名: `SPELL_PROMOTE_SETTLEMENT`
- 説明（ゲーム内ヘルプ）: 大都市志向の指導者のみ実行可能
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `PyResult`: spellPromoteSettlement
  - `PyRequirement`: reqPromoteSettlement
  - `Effect`: Boom

### Rage - 乱心

- 内部名: `SPELL_RAGE`
- 実行ユニットクラス: ブーボーズ
- 射程: 1
- 説明（ゲーム内ヘルプ）: ユニットを蛮族にする
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `bResistable`: 1
  - `DamageType`: 催眠
  - `iResistModify`: 20
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 燃えたぎる血
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Raging Seas - 荒れ狂う海原

- 内部名: `SPELL_RAGING_SEAS`
- 必要テクノロジー: 光学
- 実行文明: ラヌーン
- 説明（ゲーム内ヘルプ）: 水タイルに隣接した全てのユニットに冷気ダメージを与える
- その他の設定:
  - `bAdjacentToWaterOnly`: 1
  - `bInCityOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `iDamage`: 75
  - `iDamageLimit`: 500
  - `DamageType`: 冷気
  - `iPlotProbability`: 25
  - `bDouse`: 1
  - `bDestroyImprovement`: 1
  - `bImmuneTeam`: 1
  - `PyRequirement`: reqRagingSeas
  - `Effect`: Boom
  - `EffectRangedPlot`: Spring

### Raise Skeleton - 骸骨再生

- 内部名: `SPELL_RAISE_SKELETON`
- 必要な昇進: 死Ⅰ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 骸骨
  - `bPermanentUnitCreate`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellRaiseSkeleton
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Rally - 結集

- 内部名: `SPELL_RALLY`
- 実行文明: バンノール
- 説明（ゲーム内ヘルプ）: 全ての都市と町（タイル整備）から煽動家が出現
- その他の設定:
  - `CivicPrereq`: 聖戦
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellRally
  - `PyRequirement`: reqRally
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Read the Grimoire - 地獄全書を紐解く

- 内部名: `SPELL_READ_THE_GRIMOIRE`
- 必要な昇進: PROMOTION_INFERNAL_GRIMOIRE
- 説明（ゲーム内ヘルプ）: 無作為に呪文が発動 / 術者が死ぬ場合がある
- その他の設定:
  - `bHasCasted`: 1
  - `PyResult`: spellReadTheGrimoire
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Rebuild Barnaxus - バルナクサスの復元

- 内部名: `SPELL_REBUILD_BARNAXUS`
- 必要な昇進: PROMOTION_PIECES_OF_BARNAXUS
- 説明（ゲーム内ヘルプ）: バルナクサスを復元する （ルシュイアープ配下のユニットとなる） / ルシュイアープの都市で実行可能
- その他の設定:
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellRebuildBarnaxus
  - `PyRequirement`: reqRebuildBarnaxus
  - `RemovePromotions`: PROMOTION_PIECES_OF_BARNAXUS
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Recruit - 募兵

- 内部名: `SPELL_RECRUIT`
- 必要な昇進: 募兵官
- 説明（ゲーム内ヘルプ）: 都市の人口に応じた数のユニットを雇用 / 実行者は死亡（ドナル・ルーは死亡しない代わりに雇用数が少ない）
- その他の設定:
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellRecruit
  - `PyRequirement`: reqRecruit
  - `RemovePromotions`: 募兵官
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Recruit Mercenary - 傭兵を募る

- 内部名: `SPELL_RECRUIT_MERCENARY_TAVERN`
- その他の設定:
  - `BuildingPrereq`: 酒場
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iCost`: 180
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitClassType`: 傭兵
  - `bPermanentUnitCreate`: 1
  - `PyResult`: spellRecruitMercenary
  - `PyDisabled`: disabledRecruitMercenary
  - `Effect`: Boom

### Regeneration - 再生

- 内部名: `SPELL_REGENERATION`
- 必要な昇進: 肉体Ⅱ
- その他の設定:
  - `bHasCasted`: 1
  - `bImmuneNotAlive`: 1
  - `PyDisabled`: disabledRegeneration
  - `AddPromotions`: 再生
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Release from Cage - 檻から解放する

- 内部名: `SPELL_RELEASE_FROM_CAGE`
- 説明（ゲーム内ヘルプ）: 檻に囚われたユニットを自由にする
- その他の設定:
  - `ImprovementPrereq`: 檻
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `PyResult`: spellReleaseFromCage
  - `PyRequirement`: reqTargetFree
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Religious Fervor - 信仰者の熱狂

- 内部名: `SPELL_RELIGIOUS_FERVOR`
- 必要テクノロジー: 聖職
- 実行文明: マラキム
- 説明（ゲーム内ヘルプ）: 国教が布教された全ての都市から司祭ユニットが出現 / それらの司祭は領内の国教が布教された都市の数に等しい経験値を得る
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellReligiousFervor
  - `PyRequirement`: reqReligiousFervor
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Repair - 修理

- 内部名: `SPELL_REPAIR`
- 必要な昇進: 呪付Ⅰ
- 必要な昇進(2): ドワーフ
- 説明（ゲーム内ヘルプ）: ゴーレム、海軍ユニット、攻城兵器を回復
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iHealAmount`: 20
  - `iTargetLimitPerPlot`: 7
  - `bImmuneNotMech`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Resurrection - 英雄の再誕

- 内部名: `SPELL_RESURRECTION`
- 必要な昇進: 生命Ⅲ
- 説明（ゲーム内ヘルプ）: 文明の英雄を復活させる
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iBuildDelay`: 7
  - `PyResult`: spellResurrection
  - `PyRequirement`: reqResurrection
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Resurrection

### Resurrection - 蘇生

- 内部名: `SPELL_RESURRECTION_GRAVEYARD`
- 必要な昇進: 生命Ⅲ
- 説明（ゲーム内ヘルプ）: 勇士を召喚する（永続的） / 　　勇士には英雄が与えられる / 　　墓地で実行可能 / 　　使用すると墓地は破壊される
- その他の設定:
  - `ImprovementPrereq`: 墓地
  - `bInBordersOnly`: 1
  - `bHasCasted`: 1
  - `PyResult`: spellResurrectionGraveyard
  - `PyRequirement`: reqTargetFree
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Resurrection

### Reveal - 出現

- 内部名: `SPELL_REVEAL`
- 説明（ゲーム内ヘルプ）: ノクス=ノクティスによる不可視効果を無効にする
- その他の設定:
  - `BuildingClassOwnedPrereq`: ノクス=ノクティス
  - `StateReligionPrereq`: エススの枢密院
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `PyResult`: spellReveal
  - `PyRequirement`: reqReveal
  - `Effect`: Boom

### Revelation - 発覚

- 内部名: `SPELL_REVELATION`
- 必要な昇進: 精神集中Ⅱ
- 必要な昇進(2): 神術
- 必要な宗教: 至光なる天空
- 射程: 3
- 説明（ゲーム内ヘルプ）: 範囲内の全ての幻影ユニットを破壊
- その他の設定:
  - `bHasCasted`: 1
  - `iDamageLimit`: 100
  - `DamageType`: 致死
  - `bDispel`: 1
  - `bImmuneTeam`: 1
  - `PyResult`: spellRevelation
  - `PyRequirement`: reqRevelation
  - `iAutomatePrecastPriority`: 3
  - `PromotionExclusiveDamages`: 幻影 iDamage=100
  - `AddPromotions`: 露見
  - `RemovePromotions`: 身隠し / 姿隠し / 自失 / 悪霊体 / 幽体
  - `ImmunePromotions`: 英雄
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Revelry - お祭り騒ぎ

- 内部名: `SPELL_REVELRY`
- 必要テクノロジー: 祝祭
- 実行文明: バルセラフ
- 説明（ゲーム内ヘルプ）: 黄金時代を開始
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellRevelry
  - `PyRequirement`: reqRevelry
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Ring of Flames - 炎の輪

- 内部名: `SPELL_RING_OF_FLAMES`
- 必要な昇進: 精神集中Ⅱ
- 必要な昇進(2): 神術
- 必要な宗教: 蒼褪めたヴェール
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `iDamage`: 15
  - `iDamageLimit`: 40
  - `DamageType`: 火炎
  - `iTargetLimitPerPlot`: 7
  - `iPlotProbability`: 25
  - `bArson`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Ring of Flames

### River of Blood - 血の大河

- 内部名: `SPELL_RIVER_OF_BLOOD`
- 実行文明: カラビム
- 説明（ゲーム内ヘルプ）: カラビム以外の全ての都市の人口が減少 / カラビムの全ての都市の人口が増加
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellRiverOfBlood
  - `PyRequirement`: reqRiverOfBlood
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Roar - 竜の咆哮

- 内部名: `SPELL_ROAR`
- 必要な昇進: 原初のドラゴン
- 必要な昇進(2): ドラゴン
- 射程: 1
- 説明（ゲーム内ヘルプ）: 周囲1タイル以内の全ての敵ユニットに恐怖の攻撃を行う
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bResistable`: 1
  - `iResistModify`: 20
  - `bImmuneTeam`: 1
  - `PyResult`: spellRoar
  - `PyRequirement`: reqRoar
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Rob Graveyard - 墓を荒らす

- 内部名: `SPELL_ROB_GRAVE`
- 説明（ゲーム内ヘルプ）: 何が出るかな？
- その他の設定:
  - `ImprovementPrereq`: 墓地
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `PyResult`: spellRobGrave
  - `PyRequirement`: reqRobGrave
  - `Effect`: Boom

### Rust - 腐食

- 内部名: `SPELL_RUST`
- 必要な昇進: 不可逆Ⅱ
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bResistable`: 1
  - `iResistModify`: 25
  - `iTargetLimitPerPlot`: 16
  - `RustPromotion`: 武器の腐食
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Sacrifice - 生贄に捧げる

- 内部名: `SPELL_SACRIFICE_ALTAR`
- 説明（ゲーム内ヘルプ）: を得る / 1ターンに1回のみ使用可能
- その他の設定:
  - `BuildingPrereq`: 悪魔の供犠台
  - `iCasterMinLevel`: 2
  - `bCasterMustBeAlive`: 1
  - `bCasterNoDuration`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `PyResult`: spellSacrificeAltar
  - `PyRequirement`: reqSacrificeAltar
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Sacrifice

### Sacrifice - 生贄に捧げる

- 内部名: `SPELL_SACRIFICE_PYRE`
- 必要な昇進: 天使
- 射程: 1
- その他の設定:
  - `ImprovementPrereq`: 熾天使の火葬
  - `bCasterNoDuration`: 1
  - `bInBordersOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `bCausesWar`: 1
  - `iDamage`: 15
  - `iDamageLimit`: 40
  - `DamageType`: 火炎
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 炎の精霊
  - `bPermanentUnitCreate`: 1
  - `iPlotProbability`: 25
  - `bArson`: 1
  - `PyResult`: spellSacrificePyre
  - `PyDisabled`: disabledSacrificePyre
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Sacrifice

### Sanctify - 大地浄化

- 内部名: `SPELL_SANCTIFY`
- 必要な昇進: 生命Ⅰ
- 射程: 1
- 説明（ゲーム内ヘルプ）: 周囲のタイルから地獄の侵蝕を除去 / 周囲のタイルから都市の廃墟、墓地、悪霊の遺跡を除去 / 　　同時にアルマゲドンカウンタを減少させてエインヘリヤルの軍勢を召喚する（永続的）
- その他の設定:
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `iPlotProbability`: 100
  - `iPlotCounterChange`: -100
  - `PyResult`: spellSanctify
  - `PyDisabled`: disabledSanctify
  - `PyEnabled`: enabledSanctify
  - `iAutomateTerrainPriority`: 30
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Sanctuary - 聖域

- 内部名: `SPELL_SANCTUARY`
- 実行文明: エロヒム
- 説明（ゲーム内ヘルプ）: 領内からエロヒム以外の全てのユニットを追い出す / 30ターンのあいだ他国のユニットは領内に侵入できない
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellSanctuary
  - `PyRequirement`: reqSanctuary
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Scorch - 日照り

- 内部名: `SPELL_SCORCH`
- 必要な昇進: 太陽Ⅰ
- 説明（ゲーム内ヘルプ）: 周囲1タイルの猛吹雪を除去 / 周囲1タイルの寒冷化の融解を促進（領内に限る）
- その他の設定:
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bCausesWar`: 1
  - `iPlotProbability`: 100
  - `PyResult`: spellScorch
  - `PyDisabled`: disabledScorch
  - `PyEnabled`: enabledScorch
  - `iAutomateTerrainPriority`: 70
  - `AlteredTerrains`: 平原 砂漠 / 湿地 草原 / 氷原 凍土
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Scorch

### Sever Soul - 魂分け

- 内部名: `SPELL_SEVER`
- 必要テクノロジー: 追跡術
- 実行文明: シダー
- その他の設定:
  - `UnitCombatPrereq`: 偵察ユニット
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 人魂
  - `PyDisabled`: disabledSever
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Entropy Summon

### Shadowwalk - 影渡り

- 内部名: `SPELL_SHADOWWALK`
- 必要な昇進: 影Ⅱ
- その他の設定:
  - `bHasCasted`: 1
  - `iAutomatePostcastPriority`: 1050
  - `AddPromotions`: 影渡り
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Swords Sparks

### Shield of Faith - 信仰の盾

- 内部名: `SPELL_SHIELD_OF_FAITH`
- 必要な昇進: 精神集中Ⅱ
- 必要な昇進(2): 神術
- 必要な宗教: キルモフのルーン
- その他の設定:
  - `bHasCasted`: 1
  - `iAutomatePrecastPriority`: 70
  - `iAutomatePostcastPriority`: 1070
  - `AddPromotions`: 信仰の盾
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Swords Sparks

### Sing - 歌を歌う

- 内部名: `SPELL_SING`
- 実行ユニットクラス: ガイブラシ・スリープウッド
- 説明（ゲーム内ヘルプ）: まったく役に立ちません。完全に趣味の能力として用意されています。
- その他の設定:
  - `bIgnoreHasCasted`: 1
  - `bAbility`: 1
  - `PyResult`: spellSing
  - `PyRequirement`: reqTargetFree

### Sirona's Touch - シロナの抱擁

- 内部名: `SPELL_SIRONAS_TOUCH`
- 説明（ゲーム内ヘルプ）: ユニットを即座に15%回復
- その他の設定:
  - `BuildingClassOwnedPrereq`: シロナの祭殿
  - `bCasterMustBeAlive`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bAbility`: 1
  - `iHealAmount`: 25
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellSironasTouch
  - `PyDisabled`: disabledSironasTouch
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Buy a Slave - 奴隷の購入

- 内部名: `SPELL_SLAVE_TRADE_BUY`
- 説明（ゲーム内ヘルプ）: 奴隷ユニットを得る
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bPrereqSlaveTrade`: 1
  - `bHasCasted`: 1
  - `iCost`: 30
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 奴隷
  - `bPermanentUnitCreate`: 1
  - `PyResult`: spellSlaveTradeBuy
  - `PyDisabled`: disabledSlaveTrade
  - `Effect`: Boom

### Sell a Slave - 奴隷の売却

- 内部名: `SPELL_SLAVE_TRADE_SELL`
- 実行ユニットクラス: 奴隷
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bPrereqSlaveTrade`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `iCost`: -20
  - `bAbility`: 1
  - `Effect`: Boom

### Slow - 鈍足

- 内部名: `SPELL_SLOW`
- 必要な昇進: 氷Ⅰ
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bResistable`: 1
  - `iResistModify`: 10
  - `iTargetLimitPerPlot`: 15
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `AddPromotions`: 鈍足
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Slow Effect

### Snowfall - 豪雪

- 内部名: `SPELL_SNOWFALL`
- 必要な昇進: 氷Ⅲ
- 射程: 1
- 説明（ゲーム内ヘルプ）: 周囲のタイルを一時的に氷原に変える
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `iDamage`: 40
  - `iDamageLimit`: 80
  - `DamageType`: 冷気
  - `iTargetLimitPerPlot`: 13
  - `iPlotProbability`: 100
  - `bDouse`: 1
  - `PyResult`: spellSnowfall
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Snowfall

### Snowfall - 豪雪

- 内部名: `SPELL_SNOWFALL_GREATOR`
- 実行ユニットクラス: 冬の化身オーリック
- 射程: 3
- 説明（ゲーム内ヘルプ）: 周囲のタイルを一時的に氷原に変える
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `iDamage`: 200
  - `iDamageLimit`: 100
  - `DamageType`: 冷気
  - `bDouse`: 1
  - `bImmuneTeam`: 1
  - `PyResult`: spellSnowfall
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Snowfall Greator

### Spellstaff - 呪文の杖の開放

- 内部名: `SPELL_SPELLSTAFF`
- 必要な昇進: 呪文の杖
- その他の設定:
  - `bIgnoreHasCasted`: 1
  - `PromotionCost`: 呪文の杖
  - `bRemoveHasCasted`: 1
  - `bBuffCasterOnly`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Spores - 胞子

- 内部名: `SPELL_SPORES`
- 実行ユニット: マイコニド
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bCausesWar`: 1
  - `bResistable`: 1
  - `iResistModify`: 10
  - `iTargetLimitPerPlot`: 11
  - `iImmobileTurns`: 2
  - `bImmuneTeam`: 1
  - `bImmuneNotAlive`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Spores Effect

### Spreads the Council of Esus - エススの枢密院を布教

- 内部名: `SPELL_SPREAD_THE_COUNCIL_OF_ESUS`
- 必要な宗教: エススの枢密院
- その他の設定:
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iCost`: 25
  - `bAbility`: 1
  - `SpreadReligion`: エススの枢密院
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Spring - 湧き水

- 内部名: `SPELL_SPRING`
- 必要な昇進: 水Ⅰ
- 説明（ゲーム内ヘルプ）: 周囲のタイルの延焼を鎮火
- その他の設定:
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bCausesWar`: 1
  - `iBuildDelay`: 2
  - `iPlotProbability`: 100
  - `PyDisabled`: disabledSpring
  - `iAutomateTerrainPriority`: 90
  - `AlteredTerrains`: 砂漠 平原 / 草原 湿地
  - `Effect`: Spring

### Spring - 湧き水

- 内部名: `SPELL_SPRING_EXTINGUISH`
- 必要な昇進: 水Ⅰ
- 射程: 1
- 説明（ゲーム内ヘルプ）: 周囲の延焼を鎮火
- その他の設定:
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `iPlotProbability`: 100
  - `bDouse`: 1
  - `PyRequirement`: reqSpringExtinguish
  - `iAutomateTerrainPriority`: 10
  - `Effect`: Spring

### Sprint - 全力疾走

- 内部名: `SPELL_SPRINT`
- 必要な昇進: ケンタウロス
- その他の設定:
  - `bBeforeMovementOnly`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `AddPromotions`: 快足
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 快足 / 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Frosty swirling air flow

### Stasis - 停滞

- 内部名: `SPELL_STASIS`
- 実行文明: イリアン
- 説明（ゲーム内ヘルプ）: 他の文明は一時的に研究と生産ができなくなる / 実行には昇神を完成させていなければならない
- その他の設定:
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellStasis
  - `PyRequirement`: reqStasis
  - `PrereqOrUnits`: 白邪竜ドリファ / 冬の化身オーリック / 北風のフィアクラ
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Steal - 盗む

- 内部名: `SPELL_STEAL`
- 必要な宗教: エススの枢密院
- 説明（ゲーム内ヘルプ）: 同じタイルにいるユニットや都市から装備品を奪い取る
- その他の設定:
  - `UnitCombatPrereq`: 偵察ユニット
  - `StateReligionPrereq`: エススの枢密院
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bCausesWar`: 1
  - `bImmuneTeam`: 1
  - `PyResult`: spellSteal
  - `PyRequirement`: reqSteal
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Stoneskin - 石の皮膚

- 内部名: `SPELL_STONESKIN`
- 必要な昇進: 大地Ⅰ
- その他の設定:
  - `bHasCasted`: 1
  - `bBuffCasterOnly`: 1
  - `iAutomatePrecastPriority`: 30
  - `iAutomatePostcastPriority`: 1030
  - `AddPromotions`: 石の皮膚
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Stoneskin

### Summon Air Elemental - 大気の精霊の召喚

- 内部名: `SPELL_SUMMON_AIR_ELEMENTAL`
- 必要な昇進: 大気Ⅱ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 大気の精霊
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Air Summon

### Summon Aurealis - オーリアリスの召喚

- 内部名: `SPELL_SUMMON_AUREALIS`
- 必要な昇進: 太陽Ⅲ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: オーリアリス
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Sun Light

### Summon Balor - バロールの召喚

- 内部名: `SPELL_SUMMON_BALOR`
- 必要な昇進: 精神集中Ⅲ
- 必要な昇進(2): 神術
- 必要な宗教: 蒼褪めたヴェール
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 2
  - `CreateUnitType`: バロール
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Entropy Summon

### Summon Djinn - 魔人の召喚

- 内部名: `SPELL_SUMMON_DJINN`
- 必要な昇進: 超魔術Ⅲ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 魔人
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Summon Earth Elemental - 大地の精霊の召喚

- 内部名: `SPELL_SUMMON_EARTH_ELEMENTAL`
- 必要な昇進: 大地Ⅱ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 大地の精霊
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Summon Host of the Einherjar - エインヘルヤルの軍勢の召喚

- 内部名: `SPELL_SUMMON_EINHERJAR`
- 必要な昇進: 法Ⅱ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: エインヘルヤルの軍勢
  - `bPermanentUnitCreate`: 1
  - `bBuffCasterOnly`: 1
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Life Summon

### Summon Fire Elemental - 炎の精霊の召喚

- 内部名: `SPELL_SUMMON_FIRE_ELEMENTAL`
- 必要な昇進: 炎Ⅱ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 炎の精霊
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fire Summon

### Summon Guardian Vines - 生きている蔦の召喚

- 内部名: `SPELL_SUMMON_GUARDIAN_VINES`
- 必要な昇進: 自然Ⅰ
- その他の設定:
  - `TerrainOrPrereq1`: 草原
  - `TerrainOrPrereq2`: 平原
  - `bHasCasted`: 1
  - `iDelay`: 2
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 生きている蔦
  - `bPermanentUnitCreate`: 1
  - `bBuffCasterOnly`: 1
  - `PyDisabled`: disabledSummonGuardianVines
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Nature Summon

### Summon Griffon - グリフォンの召喚

- 内部名: `SPELL_SUMMON_GRIFFON`
- 必要な昇進: 自然Ⅰ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: グリフォン
  - `CreateUnitPromotion`: 精霊
  - `bPermanentUnitCreate`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellSummonAnimal
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Life Summon

### Summon Ice Elemental - 氷の精霊の召喚

- 内部名: `SPELL_SUMMON_ICE_ELEMENTAL`
- 必要な昇進: 氷Ⅰ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 氷の精霊
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Ice Summon Effect

### Summon Illusion - 幻影の召喚

- 内部名: `SPELL_SUMMON_ILLUSION`
- 必要な昇進: 幻術士
- 射程: 1
- 説明（ゲーム内ヘルプ）: 術者の周囲にいるユニットの複製となる幻影を作り出す
- その他の設定:
  - `bHasCasted`: 1
  - `bGeneralAffectUnit`: 1
  - `PyResult`: spellSummonIllusion
  - `PyRequirement`: reqSummonIllusion
  - `ImmunePromotions`: 幻影 / 吸血鬼
  - `BlockToCastPromotions`: 幻影
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Summon Kraken - クラーケンの召喚

- 内部名: `SPELL_SUMMON_KRAKEN`
- 必要な昇進: 精神集中Ⅲ
- 必要な昇進(2): 神術
- 必要な宗教: 深海の旧支配者
- その他の設定:
  - `bAdjacentToWaterOnly`: 1
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: クラーケン
  - `bPermanentUnitCreate`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Summon Mistform - 霧の生命体の召喚

- 内部名: `SPELL_SUMMON_MISTFORM`
- 必要な昇進: 影Ⅲ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 霧の生命体
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Summon Pit Beast - 奈落の魔獣の召喚

- 内部名: `SPELL_SUMMON_PIT_BEAST`
- 必要な昇進: 不可逆Ⅰ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 奈落の魔獣
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Pit Beast Spell Effect

### Summon Sand Lion - 砂獅子の召喚

- 内部名: `SPELL_SUMMON_SAND_LION`
- 必要な昇進: 精神集中Ⅱ
- 実行文明: マラキム
- その他の設定:
  - `UnitCombatPrereq`: 秘術ユニット
  - `TerrainOrPrereq1`: 砂漠
  - `TerrainOrPrereq2`: 灼熱の砂地
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 砂獅子
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Summon Spectre - 悪霊の召喚

- 内部名: `SPELL_SUMMON_SPECTRE`
- 必要な昇進: 死Ⅱ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 悪霊
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Summon Tiger - 虎の召喚

- 内部名: `SPELL_SUMMON_TIGER`
- 必要な昇進: 精神集中Ⅱ
- 必要な昇進(2): 神術
- 必要な宗教: 緑葉の同胞
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 虎
  - `CreateUnitPromotion`: 精霊
  - `bPermanentUnitCreate`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellSummonAnimal
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Nature Summon

### Summon Treant - トレントの召喚

- 内部名: `SPELL_SUMMON_TREANT`
- 必要な昇進: 精神集中Ⅲ
- 必要な昇進(2): 神術
- 必要な宗教: 緑葉の同胞
- その他の設定:
  - `FeatureOrPrereq1`: 森林
  - `FeatureOrPrereq2`: 古代樹林
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: トレント
  - `bPermanentUnitCreate`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Nature Summon

### Summon Water Elemental - 水の精霊の召喚

- 内部名: `SPELL_SUMMON_WATER_ELEMENTAL`
- 必要な昇進: 水Ⅱ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 水の精霊
  - `bPermanentUnitCreate`: 1
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Water Summon

### Summon Wraith - 死霊の召喚

- 内部名: `SPELL_SUMMON_WRAITH`
- 必要な昇進: 死Ⅲ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 死霊
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Wraith Spell Effect

### Taunt - 嘲笑

- 内部名: `SPELL_TAUNT`
- 射程: 1
- 説明（ゲーム内ヘルプ）: 周囲1タイル以内の敵ユニットは狂乱し、術者のいるタイルを攻撃する
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bResistable`: 1
  - `DamageType`: 催眠
  - `iResistModify`: 10
  - `iTargetLimitPerPlot`: 5
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `PyResult`: spellTaunt
  - `PyRequirement`: reqTaunt
  - `PrereqOrUnits`: 道化師 / 嘲笑う者
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Sacrifice

### Trust - 信頼

- 内部名: `SPELL_TRUST`
- 必要な昇進: 魂Ⅲ
- 説明（ゲーム内ヘルプ）: 術者の文明に対する他の全指導者の態度が好転
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `PyResult`: spellTrust
  - `PyRequirement`: reqTrust
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Tsunami - 津波

- 内部名: `SPELL_TSUNAMI`
- 必要な昇進: 精神集中Ⅱ
- 必要な昇進(2): 神術
- 必要な宗教: 深海の旧支配者
- 射程: 2
- 説明（ゲーム内ヘルプ）: 水タイルおよびそれに隣接するタイルのユニットにダメージ / タイル整備を破壊することがある
- その他の設定:
  - `bAdjacentToWaterOnly`: 1
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `iDamage`: 30
  - `iDamageLimit`: 75
  - `DamageType`: 冷気
  - `iTargetLimitPerPlot`: 20
  - `iPlotProbability`: 25
  - `bDouse`: 1
  - `bDestroyImprovement`: 1
  - `bImmuneFlying`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom
  - `EffectRangedPlot`: Spring

### Unyielding Order - 揺るぎない秩序

- 内部名: `SPELL_UNYIELDING_ORDER`
- 必要な昇進: 精神集中Ⅲ
- 必要な昇進(2): 神術
- 必要な宗教: 秩序の修道会
- 説明（ゲーム内ヘルプ）: 都市の叛乱や憤りが鎮圧され、術者の滞在中は都市のが取り除かれる
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `CreateBuildingType`: 揺るぎない秩序
  - `PyResult`: spellUnyieldingOrder
  - `iAutomatePostcastPriority`: 1130
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### TXT_KEY_SPELL_UPGRADE_ARCHER - TXT_KEY_SPELL_UPGRADE_ARCHER

- 内部名: `SPELL_UPGRADE_ARCHER`
- 必要な昇進: 蠍一族
- 必要テクノロジー: 弓術
- 実行ユニット: ゴブリン
- その他の設定:
  - `bHasCasted`: 1
  - `iCost`: 50
  - `bAbility`: 1
  - `ConvertUnitType`: 弓兵
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Upgrade to Warrior - 野蛮人へ昇格

- 内部名: `SPELL_UPGRADE_DOVIELLO_WARRIOR`
- 実行文明: ドヴィエロ
- その他の設定:
  - `bHasCasted`: 1
  - `iCost`: 20
  - `bAbility`: 1
  - `ConvertUnitType`: 野蛮人
  - `PyRequirement`: reqUpgradeDovielloWarrior
  - `PrereqOrUnits`: 労働者 / 奴隷
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Valor - 武勇

- 内部名: `SPELL_VALOR`
- 必要な昇進: 法Ⅲ
- その他の設定:
  - `bHasCasted`: 1
  - `bImmuneNotAlive`: 1
  - `iAutomatePrecastPriority`: 110
  - `iAutomatePostcastPriority`: 1110
  - `AddPromotions`: 武勇
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Veil of Night - 夜の帳

- 内部名: `SPELL_VEIL_OF_NIGHT`
- 必要テクノロジー: 詐欺
- 実行文明: スヴァルトアールヴ
- 説明（ゲーム内ヘルプ）: 配下の全てのユニットが国籍秘匿を得る / 配下の全ての偵察ユニットがエススの枢密院を信仰するようになる
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellVeilOfNight
  - `PyRequirement`: reqVeilOfNight
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Vitalize - 肥沃化

- 内部名: `SPELL_VITALIZE`
- 必要な昇進: 自然Ⅲ
- 説明（ゲーム内ヘルプ）: 術者がいるタイルの地形を肥沃化
- その他の設定:
  - `bInBordersOnly`: 1
  - `bHasCasted`: 1
  - `iPlotProbability`: 100
  - `PyPlotRequirement`: plotReqVitalize
  - `iAutomateTerrainPriority`: 50
  - `AlteredTerrains`: 平原 草原 / 砂漠 平原 / 湿地 平原 / 凍土 平原 / 氷原 凍土
  - `Effect`: Vitalize

### Vitalize - 肥沃化

- 内部名: `SPELL_VITALIZE_FLOOD_PLAINS`
- 必要な昇進: 自然Ⅲ
- 説明（ゲーム内ヘルプ）: 術者がいるタイルの地形を肥沃化
- その他の設定:
  - `bInBordersOnly`: 1
  - `bHasCasted`: 1
  - `iBuildDelay`: 6
  - `CreateFeatureType`: 氾濫原
  - `iPlotProbability`: 100
  - `PyResult`: spellVitalizeFloodPlains
  - `PyPlotRequirement`: plotReqVitalizeFloodPlains
  - `iAutomateTerrainPriority`: 20
  - `AlteredTerrains`: 草原 砂漠
  - `Effect`: Vitalize

### Wall of Stone - 石の壁

- 内部名: `SPELL_WALL_OF_STONE`
- 必要な昇進: 精神集中Ⅰ
- 必要な昇進(2): 大地Ⅰ
- その他の設定:
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `CreateBuildingType`: 石の壁
  - `iAutomatePostcastPriority`: 1100
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Wane - 魂の翳り

- 内部名: `SPELL_WANE`
- 実行文明: シダー
- 説明（ゲーム内ヘルプ）: 1文明につき6回まで実行可能
- その他の設定:
  - `iCasterMinLevel`: 4
  - `bCasterMustBeAlive`: 1
  - `bHasCasted`: 1
  - `ConvertUnitType`: 朧人
  - `PyResult`: spellWane
  - `PyRequirement`: reqWane
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Warcry - 鬨の声

- 内部名: `SPELL_WARCRY`
- 実行文明: ヒッパス
- 説明（ゲーム内ヘルプ）: 配下の全てのユニットが鬨の声を得る
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellWarcry
  - `PyRequirement`: reqWarcry
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Whiteout - 雪隠れ

- 内部名: `SPELL_WHITEOUT`
- 実行ユニットクラス: 暗殺者
- 実行文明: イリアン
- その他の設定:
  - `TerrainOrPrereq1`: 氷原
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `AddPromotions`: 身隠し
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Wild Hunt - 野生の狩り

- 内部名: `SPELL_WILD_HUNT`
- 実行文明: ドヴィエロ
- 説明（ゲーム内ヘルプ）: 配下の軍事ユニット1体につき1匹の狼を生み出す（強いユニットからは、より強力な狼が生み出される）
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `CreateUnitType`: 狼
  - `PyResult`: spellWildHunt
  - `PyRequirement`: reqWildHunt
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Wither - 衰弱

- 内部名: `SPELL_WITHER`
- 必要な昇進: 不可逆Ⅲ
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bResistable`: 1
  - `iDamage`: 40
  - `iDamageLimit`: 80
  - `DamageType`: 死
  - `iResistModify`: 40
  - `iTargetLimitPerPlot`: 18
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 衰弱
  - `RemovePromotions`: 勇気 / 士気 / 武勇
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Wonder - 不可思議

- 内部名: `SPELL_WONDER`
- 必要な昇進: 混沌Ⅲ
- 説明（ゲーム内ヘルプ）: 3つから5つの予想できない効果を起こす
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `PyResult`: spellWonder
  - `PyRequirement`: reqTargetFree
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Worldbreak - 崩壊する世界

- 内部名: `SPELL_WORLDBREAK`
- 実行文明: シェアイム
- 説明（ゲーム内ヘルプ）: シェアイム以外の全ての領土にアルマゲドンカウンタに比例した規模の破壊をもたらす
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `iDamage`: 100
  - `iDamageLimit`: 500
  - `DamageType`: 火炎
  - `iPlotProbability`: 50
  - `bArson`: 1
  - `bDestroyBuilding`: 1
  - `bGlobalCounterDependent`: 1
  - `bImmuneTeam`: 1
  - `PyRequirement`: reqWorldbreak
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Self-Explode - 自爆

- 内部名: `SPELL_PYRE_EXPLODE`
- 射程: 1
- その他の設定:
  - `bAbility`: 1
  - `bTriggeredSpell`: 1
  - `iDamage`: 15
  - `iDamageLimit`: 90
  - `DamageType`: 火炎
  - `iTargetLimitPerPlot`: 7
  - `iPlotProbability`: 25
  - `bArson`: 1

### Citadel of Light - 光の城塞

- 内部名: `SPELL_CITADEL_OF_LIGHT`
- 射程: 2
- その他の設定:
  - `bTriggeredSpell`: 1
  - `iDamage`: 30
  - `iDamageLimit`: 50
  - `DamageType`: 火炎
  - `iTargetLimitPerPlot`: 7
  - `iPlotProbability`: 25
  - `bArson`: 1
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `EffectRangedPlot`: Pillar of Fire

### Call of the Grave - 墓場の呼び声

- 内部名: `SPELL_CALL_OF_THE_GRAVE_UNDEAD_HEAL`
- 射程: 2
- その他の設定:
  - `bTriggeredSpell`: 1
  - `iHealAmount`: 100
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `ExclusivePromotions`: 屍人
  - `EffectRangedPlot`: Sacrifice

### Crown of Brilliance - 輝きの王冠

- 内部名: `SPELL_CROWN_OF_BRILLANCE_PER_TURN`
- 射程: 1
- その他の設定:
  - `bTriggeredSpell`: 1
  - `iDamage`: 20
  - `iDamageLimit`: 50
  - `DamageType`: 神聖
  - `iTargetLimitPerPlot`: 9
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `Effect`: Boom

### Organize the landing crew - 上陸員の編成

- 内部名: `SPELL_ORGANIZE_THE_LANDING_CREW`
- 実行ユニットクラス: 私掠船
- その他の設定:
  - `TerrainOrPrereq1`: 近海
  - `bHasCasted`: 1
  - `iCost`: 160
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 上陸兵
  - `CreateUnitPromotion`: 国籍秘匿
  - `bPermanentUnitCreate`: 1
  - `bBuffCasterOnly`: 1
  - `PyDisabled`: disabledOrganizeTheLandingCrew
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Organize the landing crew II - 上陸員の編成Ⅱ

- 内部名: `SPELL_ORGANIZE_THE_LANDING_CREW_2`
- 実行ユニットクラス: メスケト
- その他の設定:
  - `TerrainOrPrereq1`: 近海
  - `bHasCasted`: 1
  - `iCost`: 300
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 船乗り
  - `CreateUnitPromotion`: 国籍秘匿
  - `bPermanentUnitCreate`: 1
  - `bBuffCasterOnly`: 1
  - `PyDisabled`: disabledOrganizeTheLandingCrew
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Balmy Breeze - 妖風

- 内部名: `SPELL_BALMY_BREEZE`
- 必要な昇進: 大気Ⅱ
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `bResistable`: 1
  - `DamageType`: 催眠
  - `iResistModify`: 25
  - `iTargetLimitPerPlot`: 14
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 疲労 / 睡眠
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Balmy Breeze

### Thunder - 雷

- 内部名: `SPELL_THUNDER`
- 必要な昇進: 大気Ⅲ
- 射程: 4
- 説明（ゲーム内ヘルプ）: 対象の単一タイルにいる全てのユニットに電撃ダメージ / （対象は、射程内で最も多く敵ユニットがいるタイルが自動的に選択されます）
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `iDamage`: 40
  - `iDamageLimit`: 80
  - `DamageType`: 電撃
  - `iTargetLimitPerPlot`: 11
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Storm
  - `EffectRangedPlot`: Storm Cloud

### Restoration - 復元

- 内部名: `SPELL_RESTORATION`
- 必要な昇進: 肉体Ⅲ
- 必要な昇進(2): 精神集中Ⅲ
- その他の設定:
  - `bHasCasted`: 1
  - `iHealAmount`: 15
  - `iTargetLimitPerPlot`: 8
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `bImmuneNotAlive`: 1
  - `iAutomatePrecastPriority`: 131
  - `iAutomatePostcastPriority`: 1131
  - `RemovePromotions`: 発狂 / 狂乱 / 病気 / 疫病 / 毒 / 衰弱 / 非力 / 黒死病 / 弱体化 / 睡眠 / 狂暴 / 盲目
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Death Cloud - 死の雲

- 内部名: `SPELL_DEATH_CLOUD`
- 必要な昇進: 混沌Ⅲ
- 必要な昇進(2): 精神集中Ⅲ
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `bResistable`: 1
  - `iDamage`: 25
  - `iDamageLimit`: 50
  - `DamageType`: 死
  - `iResistModify`: 20
  - `iTargetLimitPerPlot`: 16
  - `bImmuneTeam`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 黒死病
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Spores Effect

### Exhaustion - 倦怠

- 内部名: `SPELL_EXHAUSTION`
- 必要な昇進: 死Ⅱ
- 射程: 2
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `bResistable`: 1
  - `iResistModify`: 40
  - `iTargetLimitPerPlot`: 17
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 弱体化 / 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Hand of the Dead - 亡者の手

- 内部名: `SPELL_HAND_OF_THE_DEAD`
- 必要な昇進: 死Ⅲ
- 必要な昇進(2): 精神集中Ⅲ
- 射程: 1
- 説明（ゲーム内ヘルプ）: 抵抗された場合は実行者のスタックに死ダメージが与えられる
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `bResistable`: 1
  - `iDamage`: 100
  - `iDamageLimit`: 100
  - `DamageType`: 死
  - `iResistModify`: 20
  - `iTargetLimitPerPlot`: 6
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `PyResult`: spellHandoftheDead
  - `PyDisabled`: disabledHandoftheDead
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom
  - `EffectRangedPlot`: Entropy Summon

### Thaw - 雪解け

- 内部名: `SPELL_THAW`
- 必要な昇進: 大地Ⅱ
- 説明（ゲーム内ヘルプ）: 周囲1タイルの寒冷化の融解を促進（領内に限る）
- その他の設定:
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bCausesWar`: 1
  - `iPlotProbability`: 100
  - `PyResult`: spellThaw
  - `PyDisabled`: disabledThaw
  - `PyEnabled`: enabledThaw
  - `iAutomateTerrainPriority`: 70
  - `AlteredTerrains`: 凍土 平原
  - `ColdCounterChanges`: 凍土 iChange=-5000
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Scorch

### Soil Preparation - 整地

- 内部名: `SPELL_SOIL_PREPARATION`
- 必要な昇進: 大地Ⅲ
- 射程: 1
- 説明（ゲーム内ヘルプ）: 他国の領土を巻き込むと宣戦 / 周囲の山岳を丘陵に変える / 活火山を消滅させる / 周囲のユニットがいない水タイルを50%の確率で埋め立てる
- その他の設定:
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bCausesWar`: 1
  - `PyResult`: spellSoilPreparation
  - `PyRequirement`: reqSoilPreparation
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Activation - 活性

- 内部名: `SPELL_ACTIVATION`
- 必要な昇進: 呪付Ⅲ
- 必要な昇進(2): 精神集中Ⅲ
- その他の設定:
  - `bHasCasted`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 活性化 / 疲労
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Summon Ahalpuh - アハルプーの召喚

- 内部名: `SPELL_SUMMON_AHALPUH`
- 必要な昇進: 不可逆Ⅲ
- 必要な昇進(2): 精神集中Ⅲ
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: アハルプー
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Fire storm - 炎の嵐

- 内部名: `SPELL_FIRE_STORM`
- 必要な昇進: 炎Ⅲ
- 射程: 2
- 説明（ゲーム内ヘルプ）: 周囲の森林に燻る煙が立つ
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `iDamage`: 30
  - `iDamageLimit`: 80
  - `DamageType`: 火炎
  - `iTargetLimitPerPlot`: 10
  - `iPlotProbability`: 75
  - `bArson`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fire Storm

### Icicle Arrow - 氷柱の矢

- 内部名: `SPELL_ICICLE_ARROW`
- 必要な昇進: 氷Ⅱ
- 射程: 2
- 説明（ゲーム内ヘルプ）: 対象の単一タイルにいる全てのユニットに冷気ダメージ / （対象は、射程内で最も多く敵ユニットがいるタイルが自動的に選択されます）
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `iDamage`: 15
  - `iDamageLimit`: 40
  - `DamageType`: 冷気
  - `iTargetLimitPerPlot`: 12
  - `iPlotProbability`: 50
  - `bDouse`: 1
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle
  - `EffectRangedPlot`: Snowfall

### Sealed - 封印

- 内部名: `SPELL_SEALED`
- 必要な昇進: 法Ⅱ
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `bResistable`: 1
  - `DamageType`: 催眠
  - `iResistModify`: 30
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `PyResult`: spellSealed
  - `AddPromotions`: 封印
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Control - 統制

- 内部名: `SPELL_CONTROL`
- 必要な昇進: 法Ⅲ
- 必要な昇進(2): 精神集中Ⅲ
- 説明（ゲーム内ヘルプ）: 実行者タイルの味方ユニットは移動力が全回復し、さらに再攻撃が可能になる
- その他の設定:
  - `bHasCasted`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `PyResult`: spellControl
  - `PyRequirement`: reqControl
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Control - 統制

- 内部名: `SPELL_CONTROL_MOVEMENT_HEAL`
- その他の設定:
  - `iMovementCost`: -999
  - `bTriggeredSpell`: 1
  - `bRemoveMadeAttack`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1

### Revival of one-time-only - 一度きりの復活

- 内部名: `SPELL_REVIVAL_OF_ONETIMEONLY`
- 必要な昇進: 生命Ⅲ
- 必要な昇進(2): 精神集中Ⅲ
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iTargetLimitPerPlot`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `bImmuneNotAlive`: 1
  - `PyDisabled`: disabledRevivalOfOnetimeonly
  - `AddPromotions`: 不死身
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Tiltowaito - 核撃

- 内部名: `SPELL_TILTOWAITO`
- 必要な昇進: 超魔術Ⅲ
- 必要な昇進(2): 精神集中Ⅲ
- 射程: 2
- 説明（ゲーム内ヘルプ）: 効果範囲タイルに悪霊の地が作成される
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `bResistable`: 1
  - `iDamage`: 15
  - `iDamageLimit`: 50
  - `DamageType`: 物理
  - `iResistModify`: 10
  - `iTargetLimitPerPlot`: 24
  - `bImmuneTeam`: 1
  - `bImmuneNotAlive`: 1
  - `PyResult`: spellTiltowaito
  - `PyDisabled`: disabledTiltowaito
  - `AddPromotions`: 毒 / 弱体化 / 生命力低下
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Tiltowaito

### Tranquilizing - 鎮静

- 内部名: `SPELL_TRANQUILIZING`
- 必要な昇進: 精神Ⅱ
- その他の設定:
  - `bHasCasted`: 1
  - `iAutomatePrecastPriority`: 130
  - `iAutomatePostcastPriority`: 1130
  - `RemovePromotions`: 狂乱 / 発狂 / 自失 / 不安定 / 狂暴
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Depression - 恐慌

- 内部名: `SPELL_DEPRESSION`
- 必要な昇進: 精神Ⅲ
- 射程: 1
- 説明（ゲーム内ヘルプ）: 周囲1タイル以内の全ての敵ユニットに恐怖の攻撃を行う
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `bResistable`: 1
  - `iResistModify`: 20
  - `bImmuneTeam`: 1
  - `PyResult`: spellDepression
  - `PyRequirement`: reqDepression
  - `AddPromotions`: 怯懦
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Poison Cloud - 毒の雲

- 内部名: `SPELL_POISON_CLOUD`
- 必要な昇進: 自然Ⅲ
- 必要な昇進(2): 精神集中Ⅲ
- 射程: 2
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `bResistable`: 1
  - `iDamage`: 50
  - `iDamageLimit`: 80
  - `DamageType`: 毒
  - `iResistModify`: 10
  - `iTargetLimitPerPlot`: 12
  - `bImmuneTeam`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 毒
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Poison Cloud

### Blindness - 盲目

- 内部名: `SPELL_BLINDNESS`
- 必要な昇進: 影Ⅱ
- 射程: 2
- その他の設定:
  - `bHasCasted`: 1
  - `bResistable`: 1
  - `DamageType`: 催眠
  - `iResistModify`: 20
  - `iFortifyTurns`: -5
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 盲目
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Gloom - 姿隠し

- 内部名: `SPELL_GLOOM`
- 必要な昇進: 影Ⅲ
- 必要な昇進(2): 精神集中Ⅲ
- その他の設定:
  - `bHasCasted`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `AddPromotions`: 姿隠し
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Ire - 憤怒

- 内部名: `SPELL_IRE`
- 必要な昇進: 魂Ⅲ
- 必要な昇進(2): 精神集中Ⅲ
- その他の設定:
  - `bHasCasted`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 憤怒
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Prismic Missile - 虹

- 内部名: `SPELL_PRISMIC_MISSILE`
- 必要な昇進: 太陽Ⅲ
- 必要な昇進(2): 精神集中Ⅲ
- 射程: 1
- 説明（ゲーム内ヘルプ）: 対象ユニットにランダムな効果を与える / （悪性効果やダメージ、または即死）
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `bResistable`: 1
  - `DamageType`: 催眠
  - `iResistModify`: 15
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `PyResult`: spellPrismicMissile
  - `PyRequirement`: reqPrismicMissile
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Sun Light

### Hurricane - 暴風雨

- 内部名: `SPELL_HURRICANE`
- 必要な昇進: 水Ⅲ
- 射程: 3
- 説明（ゲーム内ヘルプ）: 効果範囲の都市の建造物を破壊する / 効果範囲の平地タイルを海洋タイルに変化させることがある / 効果範囲の砂漠を湿地に変化させることがある
- その他の設定:
  - `BuildingClassOwnedPrereq`: 精霊の塔
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `iDamage`: 30
  - `iDamageLimit`: 90
  - `DamageType`: 冷気
  - `iTargetLimitPerPlot`: 12
  - `iPlotProbability`: 25
  - `bDouse`: 1
  - `bDestroyBuilding`: 1
  - `bDestroyImprovement`: 1
  - `iImmobileTurns`: 1
  - `PyResult`: spellHurricane
  - `PyDisabled`: disabledHurricane
  - `PyEnabled`: enabledDummy
  - `AddPromotions`: 鈍足
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Tiltowaito

### Different layer transition - 異層転移

- 内部名: `SPELL_DIFFERENT_LAYER_TRANSITION`
- 必要な昇進: 次元Ⅱ
- その他の設定:
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `CreateBuildingType`: 異層の門
  - `iAutomatePostcastPriority`: 1100
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Open Teleport - 瞬間移動の門を開く

- 内部名: `SPELL_TELEPORT`
- 必要な昇進: 次元Ⅲ
- その他の設定:
  - `bBeforeMovementOnly`: 1
  - `bHasCasted`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `iAutomatePrecastPriority`: 11
  - `AddPromotions`: 瞬間移動
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Transfer - 転送

- 内部名: `SPELL_TRANSFER`
- 必要な昇進: 次元Ⅲ
- 必要な昇進(2): 精神集中Ⅲ
- 射程: 1
- 説明（ゲーム内ヘルプ）: 対象ユニットを一瞬でどこかへ移動させる / 移動先が進入不可能な地形だった場合は死亡する / 抵抗された場合は自身が転移することがある
- その他の設定:
  - `bHasCasted`: 1
  - `bResistable`: 1
  - `DamageType`: 催眠
  - `iResistModify`: 10
  - `iTargetLimitPerPlot`: 6
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `PyResult`: spellTransfer
  - `PyRequirement`: reqTransfer
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle
  - `EffectRangedPlot`: Fizzle

### Hell Worm - 毒虫

- 内部名: `SPELL_HELL_WORM`
- 必要な昇進: 暗黒魔法Ⅰ
- 射程: 2
- 説明（ゲーム内ヘルプ）: 対象の単一タイルにいる全てのユニットに毒ダメージ / 対象の単一タイルにいる全てのユニットに毒と病気を与えることがある / （対象は、射程内で最も多く敵ユニットがいるタイルが自動的に選択されます）
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `bResistable`: 1
  - `iDamage`: 5
  - `iDamageLimit`: 30
  - `DamageType`: 毒
  - `iResistModify`: 20
  - `iTargetLimitPerPlot`: 12
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 病気
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom
  - `EffectRangedPlot`: Entropy Summon

### Hypnotism - 催眠

- 内部名: `SPELL_HYPNOTISM`
- 必要な昇進: 暗黒魔法Ⅱ
- 射程: 2
- 説明（ゲーム内ヘルプ）: 対象の単一タイルにいる全てのユニットに睡眠を与えることがある / （対象は、射程内で最も多く敵ユニットがいるタイルが自動的に選択されます）
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `bResistable`: 1
  - `DamageType`: 催眠
  - `iResistModify`: 20
  - `iTargetLimitPerPlot`: 12
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 睡眠
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom
  - `EffectRangedPlot`: Entropy Summon

### Dark Heal - 暗黒の癒やし

- 内部名: `SPELL_DARK_HEAL`
- 必要な昇進: 暗黒魔法Ⅱ
- 説明（ゲーム内ヘルプ）: 同じタイルにいる天使・魔族・精霊のユニットを回復
- その他の設定:
  - `bHasCasted`: 1
  - `iHealAmount`: 20
  - `iTargetLimitPerPlot`: 16
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `iAutomatePostcastPriority`: 1061
  - `ExclusivePromotions`: 天使
  - `SecondarySpells`: 暗黒の癒やし / 暗黒の癒やし
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Entropy Summon

### Dark Heal - 暗黒の癒やし

- 内部名: `SPELL_DARK_HEAL_DEMON`
- その他の設定:
  - `bTriggeredSpell`: 1
  - `iHealAmount`: 20
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `ExclusivePromotions`: 魔族

### Dark Heal - 暗黒の癒やし

- 内部名: `SPELL_DARK_HEAL_ELEMENTAL`
- その他の設定:
  - `bTriggeredSpell`: 1
  - `iHealAmount`: 20
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `ExclusivePromotions`: 精霊

### Feral - 狂暴

- 内部名: `SPELL_FERAL`
- 必要な昇進: 暗黒魔法Ⅲ
- 射程: 3
- 説明（ゲーム内ヘルプ）: 対象の単一タイルにいる全てのユニットに狂暴を与えることがある / （対象は、射程内で最も多く敵ユニットがいるタイルが自動的に選択されます）
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `DamageType`: 催眠
  - `iTargetLimitPerPlot`: 11
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `AddPromotions`: 狂暴
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom
  - `EffectRangedPlot`: Entropy Summon

### Comet - 彗星

- 内部名: `SPELL_COMET`
- 必要な昇進: 暗黒魔法Ⅳ
- 射程: 999
- 説明（ゲーム内ヘルプ）: 対象の単一タイルにいる全てのユニットに火炎属性ダメージを与える。 / （対象は、射程内で最も多く敵ユニットがいるタイルが自動的に選択されます）
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `iDamage`: 25
  - `iDamageLimit`: 80
  - `DamageType`: 火炎
  - `iTargetLimitPerPlot`: 12
  - `iPlotProbability`: 100
  - `bArson`: 1
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom
  - `EffectRangedPlot`: Artillery's Shell explosion

### Replenish - 再充填

- 内部名: `SPELL_REPLENISH`
- 必要な昇進: 肉体Ⅰ
- 必要な昇進(2): 屍霊術
- 説明（ゲーム内ヘルプ）: 屍人ユニットにのみ効果あり
- その他の設定:
  - `bHasCasted`: 1
  - `bImmuneEnemy`: 1
  - `PyDisabled`: disabledRegeneration
  - `AddPromotions`: 充填
  - `ExclusivePromotions`: 屍人
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Infect - 汚染

- 内部名: `SPELL_INFECT`
- 必要な昇進: 肉体Ⅱ
- 必要な昇進(2): 屍霊術
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bResistable`: 1
  - `iDamage`: 20
  - `iDamageLimit`: 30
  - `DamageType`: 毒
  - `iResistModify`: 10
  - `iTargetLimitPerPlot`: 18
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 病気
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Untiring Flesh - 不屈の肉体

- 内部名: `SPELL_UNTIRING_FLESH`
- 必要な昇進: 肉体Ⅲ
- 必要な昇進(2): 屍霊術
- 説明（ゲーム内ヘルプ）: 屍人ユニットにのみ効果あり
- その他の設定:
  - `bHasCasted`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `iAutomatePrecastPriority`: 16
  - `AddPromotions`: 不屈の肉体
  - `RemovePromotions`: 鈍足
  - `ExclusivePromotions`: 屍人
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Frosty swirling air flow

### Summon Sentinel - 番兵の召喚

- 内部名: `SPELL_SUMMON_SENTINEL`
- 必要な昇進: 精神集中Ⅱ
- 必要な昇進(2): 神術
- 必要な宗教: キルモフのルーン
- その他の設定:
  - `StateReligionPrereq`: キルモフのルーン
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: キルモフの番兵
  - `CastFlagPromotions`: 疲労Ⅱ
  - `BlockToCastPromotions`: 疲労Ⅱ
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Life Summon

### Seaweed bed - 藻場

- 内部名: `SPELL_SEAWEED_BED`
- 必要な昇進: 精神集中Ⅱ
- 必要な昇進(2): 神術
- 必要な宗教: 深海の旧支配者
- その他の設定:
  - `StateReligionPrereq`: 深海の旧支配者
  - `bInBordersOnly`: 1
  - `bHasCasted`: 1
  - `iBuildDelay`: 2
  - `CreateFeatureType`: 海藻
  - `iPlotProbability`: 100
  - `iAutomateTerrainPriority`: 100
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Bloom

### Firesplash - 火の飛沫

- 内部名: `SPELL_FIRESPLASH_CULT_OF_THE_DRAGON`
- 必要な昇進: 精神集中Ⅱ
- 必要な昇進(2): 神術
- 必要な宗教: ドラゴン崇拝
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: アザー
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Firerain - 炎の雨

- 内部名: `SPELL_FIRERAIN_CULT_OF_THE_DRAGON`
- 必要な昇進: 精神集中Ⅲ
- 必要な昇進(2): 神術
- 必要な宗教: ドラゴン崇拝
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 3
  - `CreateUnitType`: 隕石
  - `iCasterImmobileTurns`: 2
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Raise Orthus - オルタスの還魂

- 内部名: `SPELL_RAISE_ORTHUS`
- 必要な昇進: PROMOTION_ORTHUSS_AXE
- 必要な昇進(2): 召喚術師
- 説明（ゲーム内ヘルプ）: 蛮族王オルタスを復活させる / 人口3（首都7）以上必要、人口3消費 / 次元界の門によって前提条件の人口数を減少 / 悪魔の供犠台によって消費される人口数を減少 / 実行した都市の周辺1タイルに地獄の侵食が広がる / 実行した都市に荒廃による不衛生が発生
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `PromotionCost`: PROMOTION_ORTHUSS_AXE
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellRaiseOrthus
  - `PyRequirement`: reqRaiseOrthus
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Entropy Summon

### Raise Acheron - アケロンの還魂

- 内部名: `SPELL_RAISE_ACHERON`
- 必要な昇進: PROMOTION_DRAGONS_HORDE
- 必要な昇進(2): 召喚術師
- 説明（ゲーム内ヘルプ）: アケロンを復活させる / 人口8（首都12）以上必要、人口10消費 / 次元界の門によって前提条件の人口数を減少 / 悪魔の供犠台によって消費される人口数を減少 / 実行した都市の周辺1タイルに地獄の侵食が広がる / 実行した都市に荒廃による不衛生が発生
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `PromotionCost`: PROMOTION_DRAGONS_HORDE
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellRaiseAcheron
  - `PyRequirement`: reqRaiseAcheron
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Entropy Summon

### Raise Hyborem - ハイボレムの還魂

- 内部名: `SPELL_RAISE_HYBOREM`
- 必要な昇進: PROMOTION_GELA
- 必要な昇進(2): 召喚術師
- 説明（ゲーム内ヘルプ）: ハイボレムを復活させる / 人口5（首都9）以上必要、人口7消費 / 次元界の門によって前提条件の人口数を減少 / 悪魔の供犠台によって消費される人口数を減少 / 実行した都市の周辺1タイルに地獄の侵食が広がる / 実行した都市に荒廃による不衛生が発生
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `PromotionCost`: PROMOTION_GELA
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellRaiseHyborem
  - `PyRequirement`: reqRaiseHyborem
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Entropy Summon

### Raise Stephanos - ステファノスの還魂

- 内部名: `SPELL_RAISE_STEPHANOS`
- 必要な昇進: PROMOTION_CROWN_OF_COMMAND
- 必要な昇進(2): 召喚術師
- 説明（ゲーム内ヘルプ）: ステファノスを復活させる / 人口12（首都16）以上必要、人口15消費 / 次元界の門によって前提条件の人口数を減少 / 悪魔の供犠台によって消費される人口数を減少 / 実行した都市の周辺1タイルに地獄の侵食が広がる / 実行した都市に荒廃による不衛生が発生
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `PromotionCost`: PROMOTION_CROWN_OF_COMMAND
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellRaiseStephanos
  - `PyRequirement`: reqRaiseStephanos
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Entropy Summon

### Raise Buboes - ブーボーズの還魂

- 内部名: `SPELL_RAISE_BUBOES`
- 必要な昇進: PROMOTION_WAR
- 必要な昇進(2): 召喚術師
- 説明（ゲーム内ヘルプ）: ブーボーズを復活させる / 人口12（首都16）以上必要、人口15消費 / 次元界の門によって前提条件の人口数を減少 / 悪魔の供犠台によって消費される人口数を減少 / 実行した都市の周辺1タイルに地獄の侵食が広がる / 実行した都市に荒廃による不衛生が発生
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `PromotionCost`: PROMOTION_WAR
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellRaiseBuboes
  - `PyRequirement`: reqRaiseBuboes
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Entropy Summon

### Raise Yersinia - エルシニアの還魂

- 内部名: `SPELL_RAISE_YERSINIA`
- 必要な昇進: PROMOTION_ATHAME
- 必要な昇進(2): 召喚術師
- 説明（ゲーム内ヘルプ）: エルシニアを復活させる / 人口12（首都16）以上必要、人口15消費 / 次元界の門によって前提条件の人口数を減少 / 悪魔の供犠台によって消費される人口数を減少 / 実行した都市の周辺1タイルに地獄の侵食が広がる / 実行した都市に荒廃による不衛生が発生
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `PromotionCost`: PROMOTION_ATHAME
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellRaiseYersinia
  - `PyRequirement`: reqRaiseYersinia
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Entropy Summon

### Raise Ars Moriendi - 死の案内人の還魂

- 内部名: `SPELL_RAISE_ARS`
- 必要な昇進: PROMOTION_STAFF_OF_SOULS
- 必要な昇進(2): 召喚術師
- 説明（ゲーム内ヘルプ）: 死の案内人を復活させる / 人口12（首都16）以上必要、人口15消費 / 次元界の門によって前提条件の人口数を減少 / 悪魔の供犠台によって消費される人口数を減少 / 実行した都市の周辺1タイルに地獄の侵食が広がる / 実行した都市に荒廃による不衛生が発生
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `PromotionCost`: PROMOTION_STAFF_OF_SOULS
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellRaiseArs
  - `PyRequirement`: reqRaiseArs
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Entropy Summon

### Add to City as Citizen - 特別市民として定住

- 内部名: `SPELL_SLAVE_ADD_CITY_SPECIAL`
- 実行ユニット: 奴隷
- 説明（ゲーム内ヘルプ）: 都市に無償の特別市民を定住させます(5人まで)
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `iCost`: 30
  - `bAbility`: 1
  - `PyResult`: spellSlaveInThePit
  - `PyRequirement`: reqSlaveAddCitySpecial
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Evolution - 形相実現

- 内部名: `SPELL_EVOLUTION`
- その他の設定:
  - `iCasterMinLevel`: 12
  - `bIgnoreHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `AddPromotions`: 英雄
  - `Effect`: Boom

### TXT_KEY_SPELL_OFFER_GELA - TXT_KEY_SPELL_OFFER_GELA

- 内部名: `SPELL_OFFER_GELA`
- 必要な昇進: PROMOTION_GELA
- その他の設定:
  - `BuildingPrereq`: マーキュリアンの門
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `PyResult`: spellOfferGela
  - `PyRequirement`: reqOfferGela
  - `Effect`: Boom

### Conversion - 改宗

- 内部名: `SPELL_CONVERSION`
- 実行ユニット: 自由司祭オルウェン
- 説明（ゲーム内ヘルプ）: 実行者は自身の文明に広まっている任意の宗教を信奉できる
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `PyResult`: spellConversion
  - `PyRequirement`: reqConversion
  - `Effect`: Boom

### Hospitable - ねんごろ

- 内部名: `SPELL_HOSPITABLE`
- 実行ユニット: ファラマー
- 説明（ゲーム内ヘルプ）: 対象都市の文明の指導者から外交態度ボーナスを獲得できる
- その他の設定:
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iCasterImmobileTurns`: 10
  - `PyResult`: spellHospitable
  - `PyRequirement`: reqHospitable
  - `CastFlagPromotions`: 疲労Ⅱ
  - `BlockToCastPromotions`: 疲労Ⅱ
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Concentration - 再詠唱

- 内部名: `SPELL_CONCENTRATION`
- 必要な昇進: 達人
- その他の設定:
  - `bIgnoreHasCasted`: 1
  - `bRemoveHasCasted`: 1
  - `bBuffCasterOnly`: 1
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 疲労
  - `Effect`: Boom

### Gain Hero Promotion - 英雄の誇り

- 内部名: `SPELL_LUCIAN_HERO`
- 実行ユニット: ルシアン
- その他の設定:
  - `iCasterMinLevel`: 5
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `AddPromotions`: 鉄の武器 / 呪付の刃 / 英雄 / 疫病
  - `BlockToCastPromotions`: 英雄
  - `Effect`: Boom

### Way of war - 戦の道

- 内部名: `SPELL_WAY_OF_WAR`
- 実行文明: グリゴリ
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `ConvertUnitType`: 冒険者
  - `PrereqOrUnits`: 偉大な技師 / 偉大な商人 / 偉大な賢者 / 偉大な吟遊詩人 / 偉大な預言者
  - `Effect`: Boom

### Hyborem's Smile - ハイボレムの微笑

- 内部名: `SPELL_HYBOREMS_SMILE`
- 実行ユニット: ハイボレム
- 射程: 1
- 説明（ゲーム内ヘルプ）: 蒼褪めたヴェールを信仰するユニットを味方にします。 / 生命を持つユニット、もしくはデーモンにのみ効果あり。 / 英雄、忠誠の昇進を持つユニットには効果なし。 / 中立ユニットにも戦争を引き起こさずに使用可能
- その他の設定:
  - `bHasCasted`: 1
  - `bResistable`: 1
  - `DamageType`: 催眠
  - `iResistModify`: 40
  - `bImmuneTeam`: 1
  - `PyResult`: spellHyboremSmile
  - `PyRequirement`: reqHyboremSmile
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Theft Tech - テクノロジーの窃盗

- 内部名: `SPELL_THEFT_TECH`
- 必要テクノロジー: 詐欺
- 実行文明: シダー
- 説明（ゲーム内ヘルプ）: 対象文明が持つ未知のテクノロジーを1つ獲得 / 失敗すると対象に宣戦、実行ユニットは50%の確率で死亡し、死ななければ首都に帰還する
- その他の設定:
  - `UnitCombatPrereq`: 偵察ユニット
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bCausesWar`: 1
  - `iCasterImmobileTurns`: 5
  - `PyResult`: spellTheftTech
  - `PyRequirement`: reqTheftTech
  - `Effect`: Boom

### Theft Gold - 富の窃盗

- 内部名: `SPELL_THEFT_GOLD`
- 必要テクノロジー: 詐欺
- 実行文明: シダー
- 説明（ゲーム内ヘルプ）: 都市人口に比例した富を奪取する / 獲得した金額分だけ対象文明の富の残額が減少する / 対象の所持金の半分以上の富は奪えない / 失敗すると対象に宣戦、実行ユニットは首都に帰還する
- その他の設定:
  - `UnitCombatPrereq`: 偵察ユニット
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bCausesWar`: 1
  - `iCasterImmobileTurns`: 1
  - `PyResult`: spellTheftGold
  - `PyRequirement`: reqTheftGold
  - `Effect`: Boom

### Hexproof - 呪禁

- 内部名: `SPELL_HEXPROOF`
- 射程: 2
- 説明（ゲーム内ヘルプ）: 対象の単一タイルにいるユニット1体に無属性ダメージを与え、2ターン拘束する。 / （対象は、射程内で最も多く敵ユニットがいるタイルが自動的に選択されます）
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bResistable`: 1
  - `iDamage`: 40
  - `iDamageLimit`: 75
  - `DamageType`: 物理
  - `iResistModify`: 20
  - `iTargetLimitPerPlot`: 1
  - `iImmobileTurns`: 1
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `PrereqOrUnits`: 禍祓い / 依巫
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Summon KOD - 騎士の召喚

- 内部名: `SPELL_SUMMON_KOD`
- 実行ユニットクラス: ダイヤモンドの騎士聖竜
- 説明（ゲーム内ヘルプ）: ユニットはレベル12、+2800、且つダイヤモンドの武具の効果を得て召喚される / 同時にスコルージを実行する
- その他の設定:
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `iCreateUnitNum`: 3
  - `CreateUnitType`: ダイヤモンドの騎士
  - `PyResult`: spellSummonKOD
  - `PyDisabled`: disabledSummonKOD
  - `SecondarySpells`: スコルージ
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Wraith Spell Effect

### Give birth Azathi - 落とし仔の生誕

- 内部名: `SPELL_GIVE_BIRTH_AZATHI`
- 実行ユニット: アザトース
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iCreateUnitNum`: 4
  - `CreateUnitType`: ニャルラトテップ
  - `bPermanentUnitCreate`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Almadel - アルマデル

- 内部名: `SPELL_ALMADEL`
- 実行ユニット: レメゲトン
- 射程: 3
- 説明（ゲーム内ヘルプ）: 効果範囲のタイルは地獄の侵蝕を受ける
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iCreateUnitNum`: 4
  - `CreateUnitType`: アガレスの魔獣
  - `iPlotProbability`: 100
  - `iPlotCounterChange`: 100
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Entropy Summon

### Scourge - スコルージ

- 内部名: `SPELL_DRAGON_SCOURGE`
- 実行ユニット: 神竜王アレキサンダー
- 射程: 3
- 説明（ゲーム内ヘルプ）: 効果範囲のタイルは地獄の侵蝕を除かれる
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iDamage`: 30
  - `iDamageLimit`: 80
  - `DamageType`: 神聖
  - `iTargetLimitPerPlot`: 24
  - `iPlotProbability`: 100
  - `iPlotCounterChange`: -100
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Recast - 再詠唱

- 内部名: `SPELL_RECAST`
- 必要な昇進: 詠唱者
- その他の設定:
  - `bIgnoreHasCasted`: 1
  - `bRemoveHasCasted`: 1
  - `bBuffCasterOnly`: 1
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 疲労
  - `Effect`: Boom

### Creation Muramasa - ムラマサの製造

- 内部名: `SPELL_MURAMASA_BLADE_ECHIGO`
- 必要テクノロジー: ミスリル器
- 実行文明: エチゴ
- 説明（ゲーム内ヘルプ）: 村正が銘刀ムラマサを製造します
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellMurasamaBlade
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Harakiri - ハラキリ

- 内部名: `SPELL_HARAKIRI_ECHIGO`
- 実行ユニット: 侍
- 射程: 1
- 説明（ゲーム内ヘルプ）: 神聖ダメージを与える / ダメージ量および上限は術者の経験値に依存 / 　(威力: 20+経験値, 上限: 60+経験値)
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `bCausesWar`: 1
  - `DamageType`: 神聖
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `PyResult`: spellHarakiri_Echigo
  - `PyRequirement`: reqTargetFree
  - `Effect`: Maelstrom

### Mask - 仮面

- 内部名: `SPELL_MASK_ECHIGO`
- 必要テクノロジー: 詐欺
- 実行文明: エチゴ
- その他の設定:
  - `UnitCombatPrereq`: 偵察ユニット
  - `bHasCasted`: 1
  - `bBuffCasterOnly`: 1
  - `PyDisabled`: disabledMask
  - `AddPromotions`: 国籍秘匿
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Steal - 盗む

- 内部名: `SPELL_STEAL_ECHIGO`
- 必要テクノロジー: 詐欺
- 実行文明: エチゴ
- 説明（ゲーム内ヘルプ）: 同じタイルにいるユニットや都市から装備品を奪い取る
- その他の設定:
  - `UnitCombatPrereq`: 偵察ユニット
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bCausesWar`: 1
  - `bImmuneTeam`: 1
  - `PyResult`: spellSteal
  - `PyRequirement`: reqSteal
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Iai. - 居合

- 内部名: `SPELL_IAI_ECHIGO`
- 必要テクノロジー: 青銅器
- その他の設定:
  - `iCasterMinLevel`: 4
  - `bBeforeMovementOnly`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `iAutomatePrecastPriority`: 17
  - `PrereqOrUnits`: 剣客 / 侍 / 夜叉
  - `AddPromotions`: 活性化
  - `Effect`: Burning Blood

### Kuruma Gakari - 車懸

- 内部名: `SPELL_KURUMA_ECHIGO`
- 必要テクノロジー: 高潔の証
- 実行ユニット: 直江山城守
- 射程: 4
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `iAutomatePostcastPriority`: 1100
  - `AddPromotions`: 車懸の陣
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Kagura - 神楽

- 内部名: `SPELL_KAGURA_ECHIGO`
- 実行ユニット: 巫女
- 説明（ゲーム内ヘルプ）: +4/ターン、+50%/ターン、+5
- その他の設定:
  - `iCasterMinLevel`: 4
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `CreateBuildingType`: 神楽
  - `iAutomatePostcastPriority`: 1050
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Zintou Siki. - 陣頭指揮

- 内部名: `SPELL_ZINTOU_ECHIGO`
- 実行ユニット: 直江山城守
- 射程: 4
- 説明（ゲーム内ヘルプ）: レベル5以上のユニットを一時的に強化 / 　白兵ユニットに錐行の陣を与える / 　騎乗ユニットに鋒矢の陣を与える / 　弓術ユニットに亀甲陣を与える / 　信奉ユニットに守り刀を与える / 　攻城兵器に砲術を与える
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `PyResult`: spellZintoushiki
  - `PyRequirement`: reqZintoushiki
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Betrayal - 内応

- 内部名: `SPELL_NAIOU_ECHIGO`
- 実行ユニット: 直江山城守
- 射程: 3
- 説明（ゲーム内ヘルプ）: 敵ユニットを味方に引き込む / 引き込めなかった対象には忠誠、車懸けの陣が与えられる
- その他の設定:
  - `iCasterMinLevel`: 6
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bResistable`: 1
  - `DamageType`: 催眠
  - `iResistModify`: 40
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `PyResult`: spellNAIOU_ECHIGO
  - `PyRequirement`: reqNAIOU_ECHIGO
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Undead in Sacrifice - 屍の贄

- 内部名: `SPELL_UNDEAD_IN_SACRIFICE`
- 必要テクノロジー: 邪悪への道
- 実行文明: ドロアウム
- 説明（ゲーム内ヘルプ）: 各都市から1体ずつ非力持ちのゾンビが生まれる / 奴隷はすべてゾンビに転生する
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellUndeadInSacrifice
  - `PyRequirement`: reqUndeadInSacrifice
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Sacrifice

### Add to City - 都市へ定住

- 内部名: `SPELL_ADD_TO_CITY_DROAUM`
- 実行ユニット: 奴隷
- 実行文明: ドロアウム
- 説明（ゲーム内ヘルプ）: 都市へ定住し、人口に追加 / 実行する都市のとに余裕が必要となる / 実行には進化の秘法を完成させていなければならない
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `iChangePopulation`: 1
  - `PyRequirement`: reqAddCityDroaum
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Experiment - 実験

- 内部名: `SPELL_EXPERIMENT_DROAUM`
- 実行文明: ドロアウム
- 説明（ゲーム内ヘルプ）: 奴隷ユニットを消費することによって秘術ユニットは経験値を得る。 / 文明はわずかな研究力を得る。
- その他の設定:
  - `UnitCombatPrereq`: 秘術ユニット
  - `UnitInStackPrereq`: 奴隷
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `PyResult`: spellExperimentDroaum
  - `PyRequirement`: reqExperimentDroaum
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Blighted - 破滅への誘い

- 内部名: `SPELL_BLIGHTED_DROAUM`
- 実行ユニット: ゾンビ首長
- 説明（ゲーム内ヘルプ）: 屍人ユニットにのみ効果あり
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `iAutomatePostcastPriority`: 1050
  - `AddPromotions`: 破滅
  - `ExclusivePromotions`: 屍人
  - `Effect`: Creation Effect Dim

### Eating Hero's spirit - 英雄の魂を喰らう

- 内部名: `SPELL_MAENYA_CONVERT_DROAUM`
- 必要な昇進: 竜鱗
- 必要な昇進(2): 英雄の頭蓋骨
- 実行ユニット: ソーマ・メーニャ
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `AddPromotions`: 弾幕Ⅰ / 怪力 / 無双
  - `Effect`: Boom

### Infection Spread - 感染拡大

- 内部名: `SPELL_INFECTION_DROAUM`
- 必要な昇進: 病原巣
- 射程: 1
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `bCausesWar`: 1
  - `iDamage`: 20
  - `iDamageLimit`: 60
  - `DamageType`: 毒
  - `iTargetLimitPerPlot`: 9
  - `bImmuneTeam`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 病気
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Poison Cloud

### Zombie powder - ゾンビパウダー

- 内部名: `SPELL_ZOMBIEPOWDER_DROAUM`
- 必要テクノロジー: 屍霊術
- 実行ユニット: 奴隷
- 実行文明: ドロアウム
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `ConvertUnitType`: ゾンビ
  - `PyDisabled`: disabledZombiepowderDroaum
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Promotion - 位階の上昇

- 内部名: `SPELL_PROMOTION_DROAUM`
- 必要な昇進: 魔族
- 実行文明: ドロアウム
- 説明（ゲーム内ヘルプ）: 奴隷ユニットを消費 / アルマゲドンカウンタ30までは経験ポイント0～3を得ます。それ以降は10上がるごとに3ずつ獲得経験ポイントの最大値が増加します。
- その他の設定:
  - `UnitInStackPrereq`: 奴隷
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `PyResult`: spellPromotionDroaum
  - `PyRequirement`: reqPromotionDroaum
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Overeat - 暴飲暴食

- 内部名: `SPELL_OVEREAT_DROAUM`
- 必要な昇進: 魔族
- 実行文明: ドロアウム
- 説明（ゲーム内ヘルプ）: 奴隷を消費
- その他の設定:
  - `UnitInStackPrereq`: 奴隷
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iHealAmount`: 40
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellOvereatDroaum
  - `PyRequirement`: reqOvereatDroaum
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Sacrifice

### Cursed Breath - 呪われし吐息

- 内部名: `SPELL_DEATH_BREATH_DROAUM`
- 必要な昇進: 魔族
- 実行文明: ドロアウム
- 射程: 2
- 説明（ゲーム内ヘルプ）: 奴隷を消費して対象の単一タイルにいる全てのユニットに死ダメージ / （対象は、射程内で最も多く敵ユニットがいるタイルが自動的に選択されます） / アルマゲドンカウンタが高いほどダメージが大きい
- その他の設定:
  - `UnitInStackPrereq`: 奴隷
  - `bHasCasted`: 1
  - `iDamage`: 75
  - `iDamageLimit`: 75
  - `DamageType`: 死
  - `iTargetLimitPerPlot`: 7
  - `bGlobalCounterDependent`: 1
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `PyResult`: spellDeathBreathDroaum
  - `PyDisabled`: disabledDeathBreathDroaum
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Decoy Heart - 身代わりの心臓

- 内部名: `SPELL_DECOY_HEART_DROAUM`
- 必要な昇進: 魔族
- 実行文明: ドロアウム
- 説明（ゲーム内ヘルプ）: 奴隷ユニットを消費 / 10レベル必要 / アルマゲドンカウンタが100のときはレベル制限なし
- その他の設定:
  - `UnitInStackPrereq`: 奴隷
  - `bHasCasted`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellDecoyHeartDroaum
  - `PyRequirement`: reqDecoyHeartDroaum
  - `AddPromotions`: 不死身
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Genesis - 大神降ろし

- 内部名: `SPELL_GENESIS_NIRAIKANAI`
- 必要テクノロジー: 野生の触れ合い
- 実行ユニット: アマテラス
- 実行文明: ニライカナイ
- 説明（ゲーム内ヘルプ）: 創世記と同じ効果を起こします。
- その他の設定:
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellGenesis
  - `PyRequirement`: reqGenesis
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Plant Sacred Tree - 巨大樹の苗を植える

- 内部名: `SPELL_PLANT_SACRED_TREE`
- 実行ユニット: 庭師
- その他の設定:
  - `FeatureOrPrereq1`: 森林
  - `FeatureOrPrereq2`: 古代樹林
  - `bCasterNoDuration`: 1
  - `bInBordersOnly`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `CreateImprovementType`: 巨大樹の苗
  - `iPlotProbability`: 100
  - `iAutomateTerrainPriority`: 100
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Bloom

### Hudesirabe-Kounmyou - 筆しらべ・光明

- 内部名: `SPELL_HUDESIRABE_KOUMYOU`
- 必要テクノロジー: 自然との共生
- 実行ユニット: アマテラス
- 射程: 3
- 説明（ゲーム内ヘルプ）: 周囲2タイルの魔族か屍人ユニットに神聖ダメージを与えます。 / 中立ユニットの魔族か屍人ユニットを巻き込んだ場合宣戦布告になります。
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `iDamageLimit`: 100
  - `DamageType`: 神聖
  - `PromotionExclusiveDamages`: 屍人 iDamage=20 / 魔族 iDamage=20
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Omikuzi - 御神籤

- 内部名: `SPELL_OMIKUZI`
- 実行ユニット: 風祝のアーリー・シードリング
- 説明（ゲーム内ヘルプ）: 様々な効果を起こす。
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellOmikuzi
  - `PyRequirement`: reqTargetFree
  - `CastFlagPromotions`: 疲労Ⅱ
  - `BlockToCastPromotions`: 疲労Ⅱ
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Beast king - 獣の王者

- 内部名: `SPELL_BEAST_KING`
- 必要な昇進: 野性
- その他の設定:
  - `iCasterMinLevel`: 6
  - `bHasCasted`: 1
  - `bBuffCasterOnly`: 1
  - `AddPromotions`: 魔獣調教 / 自然Ⅰ / 自然Ⅱ / 行軍
  - `Effect`: Burning Blood

### Soranaki - 空亡

- 内部名: `SPELL_SORANAKI`
- 必要テクノロジー: 聖職
- 実行文明: 常闇ノ国
- 説明（ゲーム内ヘルプ）: アルマゲドンカウンタ50以上が必要 / 世界各地にて地獄の業火とともに魔族の勇士が現れる
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellSoranaki
  - `PyRequirement`: reqSoranaki
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fire Storm

### Dark Call up - 常闇の召集

- 内部名: `SPELL_DARK_CALL_UP`
- 実行文明: 常闇ノ国
- 説明（ゲーム内ヘルプ）: 墓地か土塚で実行可能 / 使用することで破壊される
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 戦士
  - `bPermanentUnitCreate`: 1
  - `PyResult`: spellRessurectionDark
  - `PyRequirement`: reqRessurectionDark
  - `Effect`: Resurrection

### Evil Favor - 魔の恩恵

- 内部名: `SPELL_GIFT_DEMON`
- 実行ユニット: 教授
- 説明（ゲーム内ヘルプ）: 同じスタックのユニットに悪魔の昇進を与える。 / この魔法によって教授自身が悪魔の昇進を得ることはない
- その他の設定:
  - `bHasCasted`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `bImmuneNotAlive`: 1
  - `PyResult`: spellGiftDemon
  - `PyRequirement`: reqGiftDemon
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Frosty swirling air flow

### Tokoyami Flames - 常闇の炎獄

- 内部名: `SPELL_TOKOYAMI_FLAMES`
- 実行ユニット: 常闇ノ皇
- 射程: 2
- 説明（ゲーム内ヘルプ）: 対象の単一タイルにいる全てのユニットに火炎ダメージ / （対象は、射程内で最も多く敵ユニットがいるタイルが自動的に選択されます）
- その他の設定:
  - `bHasCasted`: 1
  - `iDamage`: 30
  - `iDamageLimit`: 60
  - `DamageType`: 火炎
  - `iTargetLimitPerPlot`: 14
  - `iPlotProbability`: 50
  - `bArson`: 1
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom
  - `EffectRangedPlot`: Pillar of Fire

### Specchio del Zeme - ゼーメの神鏡

- 内部名: `SPELL_SPECCHIO_DEL_ZEME`
- 必要テクノロジー: 聖職
- 実行文明: イース
- 説明（ゲーム内ヘルプ）: 配下の全てのユニットに10の経験値を与える
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellSpecchioDelZeme
  - `PyRequirement`: reqSpecchioDelZeme
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Blade of thunder - 雷鳴の刃

- 内部名: `SPELL_BLADE_OF_THUNDER`
- 実行ユニット: アッシュ
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iDamage`: 40
  - `iDamageLimit`: 80
  - `DamageType`: 電撃
  - `iTargetLimitPerPlot`: 12
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle
  - `EffectRangedPlot`: Blade of thunder Effect

### New game remains strong - 強くてNEWGAME

- 内部名: `SPELL_REMAINS_STRONG`
- 説明（ゲーム内ヘルプ）: 経験点50以上が必要 / 赤毛のアドルが上位ユニットに転生する / レベルと経験点が初期値に戻る / (昇進は引き継がれる)
- その他の設定:
  - `bInCityOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellRemainStrong
  - `PyRequirement`: reqRemainStrong
  - `PrereqOrUnits`: 赤毛のアドル / 赤毛の剣士アドル
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### New game - NEWGAME

- 内部名: `SPELL_NEWGAME`
- 実行文明: イース
- 説明（ゲーム内ヘルプ）: 偉人ユニットのみ使用可能
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 赤毛のアドル
  - `bPermanentUnitCreate`: 1
  - `PyRequirement`: reqNewGame
  - `PrereqOrUnits`: 偉大な預言者 / 偉大な吟遊詩人 / 偉大な賢者 / 偉大な商人 / 偉大な技師
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Buy a Weapon - 装備品の購入

- 内部名: `SPELL_BUY_WEAPON`
- 実行文明: イース
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `PyResult`: spellYsEventBuyWeapon
  - `PyRequirement`: reqYsEventBuyWeapon
  - `PrereqOrUnits`: アッシュ / 赤毛のアドル / 赤毛の剣士アドル / 赤毛の冒険者アドル / 神殿騎士ユニカ
  - `Effect`: Boom

### Flame - 紅蓮

- 内部名: `SPELL_YS_FLAME`
- 必要な昇進: 紅蓮
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: アザー
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Tiltowaito

### Adamantine - 金剛

- 内部名: `SPELL_YS_ADAMANTINE`
- 必要な昇進: 金剛
- 射程: 2
- その他の設定:
  - `bHasCasted`: 1
  - `iDamage`: 20
  - `iDamageLimit`: 45
  - `DamageType`: 物理
  - `iTargetLimitPerPlot`: 12
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle
  - `EffectRangedPlot`: Stoneskin

### Wind - 旋風

- 内部名: `SPELL_YS_WIND`
- 必要な昇進: 旋風
- 射程: 2
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `iDamage`: 20
  - `iDamageLimit`: 40
  - `DamageType`: 電撃
  - `iTargetLimitPerPlot`: 11
  - `Effect`: Balmy Breeze

### Death and decay - 死と腐敗

- 内部名: `SPELL_DEATH_AND_DECAY`
- 実行文明: デスピエル
- 説明（ゲーム内ヘルプ）: デスピエル以外のすべての生物ユニットに、アルマゲドンカウンタに比例する死のダメージをもたらします。また都市を荒廃させます。
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `iDamage`: 100
  - `iDamageLimit`: 100
  - `DamageType`: 死
  - `bGlobalCounterDependent`: 1
  - `bImmuneTeam`: 1
  - `PyResult`: spellDeathAndDecay
  - `PyRequirement`: reqDeathAndDecay
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Energy Exploitation - 精気収奪

- 内部名: `SPELL_ENERGY_EXPLOITATION_GOGUREG`
- 射程: 1
- 説明（ゲーム内ヘルプ）: 敵味方問わず、範囲内の全てのユニットの経験値を1～3ポイント奪い取る / 範囲内の敵ユニット1体の昇進を1つ覚える
- その他の設定:
  - `bHasCasted`: 1
  - `PyResult`: spellEnergyExploitationKaijin
  - `PyRequirement`: reqEnergyExploitationKaijin
  - `PrereqOrUnits`: ゴグレグ・グリュンベルグ / ゴグレグ・グリュンベルグ / 不死者イェノイア
  - `CastFlagPromotions`: 疲労Ⅱ
  - `BlockToCastPromotions`: 疲労Ⅱ
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Wither

### Double Owner - 分身

- 内部名: `SPELL_DOUBLE_OWNER_PULUFRAUS`
- 説明（ゲーム内ヘルプ）: 術者の複製となる幻影ユニットを作り出す
- その他の設定:
  - `bCasterMustBeAlive`: 1
  - `bHasCasted`: 1
  - `PyResult`: spellMirror
  - `PyRequirement`: reqMirror
  - `PrereqOrUnits`: プルフラウス・ルァロッツ / プルフラウス・ルァロッツ / 忍者
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Annihilation - 反作用爆発

- 内部名: `SPELL_EXPLOSION_BLIME`
- 射程: 2
- 説明（ゲーム内ヘルプ）: ユニットに約25%の火炎ダメージ(上限80%)
- その他の設定:
  - `iCasterMinLevel`: 6
  - `bBeforeMovementOnly`: 1
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bCausesWar`: 1
  - `iDamage`: 25
  - `iDamageLimit`: 80
  - `DamageType`: 冷気
  - `bImmuneTeam`: 1
  - `SecondarySpells`: 反作用爆発
  - `PrereqOrUnits`: ブリム・フレイザード / ブリム・フレイザード / 不死者イェノイア
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Annihilation

### Curse of death - 死の呪い

- 内部名: `SPELL_CURSE_OF_THE_DEATH`
- 実行ユニット: 黒魔導師
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bResistable`: 1
  - `iDamage`: 20
  - `iDamageLimit`: 80
  - `DamageType`: 死
  - `iResistModify`: 10
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 生命力低下
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Summon Cuchumaquic - クチュマキックの召喚

- 内部名: `SPELL_SUMMON_CUCHUMAQUIC`
- 必要な昇進: 壊人
- 必要な昇進(2): 次元Ⅰ
- 説明（ゲーム内ヘルプ）: クチュマキックの戦闘力は術者に依存する / [25-(術者のレベル)*5]％の確率で詠唱失敗となり術者はクチュマキックに転生する
- その他の設定:
  - `UnitCombatPrereq`: 秘術ユニット
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: クチュマキック
  - `PyResult`: spellSummonCuchumaquic
  - `PyRequirement`: reqSummonCuchumaquic
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Entropy Summon

### Summon Marchosias - マルコシアスの召喚

- 内部名: `SPELL_SUMMON_MARCHOSIAS`
- 必要な昇進: 壊人
- 必要な昇進(2): 次元Ⅱ
- 必要テクノロジー: 魔術
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: マルコシアス
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Entropy Summon

### Summon Dragonliche - ドラゴンリッチの召喚

- 内部名: `SPELL_SUMMON_DRAGONLICHE`
- 必要な昇進: 壊人
- 必要な昇進(2): 次元Ⅲ
- 必要テクノロジー: 意志の力
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: ドラゴンリッチ
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Entropy Summon

### Venom - 死の毒液

- 内部名: `SPELL_VENOM`
- 必要な昇進: 原初のドラゴン
- 必要な昇進(2): 屍人
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bResistable`: 1
  - `iDamage`: 20
  - `iDamageLimit`: 80
  - `DamageType`: 死
  - `iResistModify`: 10
  - `iTargetLimitPerPlot`: 24
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 病気
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom
  - `EffectRangedPlot`: Entropy Summon

### Pollution Law Library - 汚染法書院

- 内部名: `SPELL_POLLUTION_LAW_LIBRARY`
- 射程: 2
- その他の設定:
  - `bTriggeredSpell`: 1
  - `iDamage`: 10
  - `iDamageLimit`: 50
  - `DamageType`: 毒
  - `iTargetLimitPerPlot`: 7
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `EffectRangedPlot`: Poison Cloud

### Bravely - 号令

- 内部名: `SPELL_BRAVELY`
- 必要テクノロジー: 軍事行動
- 実行文明: リネージ
- 説明（ゲーム内ヘルプ）: 配下の全てのユニットに2つの無償の昇進を与えます。
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellBravely
  - `PyRequirement`: reqBravely
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Add to City - 都市に定住

- 内部名: `SPELL_ADD_TO_CITY_COMMANDER`
- 実行ユニットクラス: 偉大な指揮官
- 実行文明: リネージ
- 説明（ゲーム内ヘルプ）: 大軍事教官として定住する
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `PyResult`: spellAddToCityCommander
  - `PyRequirement`: reqAddToCityCommander
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Awaken Soul - 魂の鼓舞

- 内部名: `SPELL_AWAKEN_SOUL`
- 実行ユニット: ゴーゼワロス
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iAutomatePrecastPriority`: 6
  - `iAutomatePostcastPriority`: 1006
  - `AddPromotions`: 熱血
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Released as Legionnaire - 軍団兵として解放

- 内部名: `SPELL_UPGRADE_FREEDMAN_WARRIOR`
- 実行ユニット: 奴隷
- 実行文明: リネージ
- その他の設定:
  - `CivicPrereq`: 庇護制
  - `bHasCasted`: 1
  - `iCost`: 10
  - `bAbility`: 1
  - `ConvertUnitType`: レギオン
  - `bBuffCasterOnly`: 1
  - `PyRequirement`: reqUpgradeFreedmanWarrior
  - `AddPromotions`: 解放奴隷 / 忠誠
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Released as Freedman - 労働者として解放

- 内部名: `SPELL_UPGRADE_FREEDMAN_WORKER`
- 実行ユニット: 奴隷
- 実行文明: リネージ
- その他の設定:
  - `CivicPrereq`: 庇護制
  - `bHasCasted`: 1
  - `iCost`: 20
  - `bAbility`: 1
  - `ConvertUnitType`: 労働者
  - `bBuffCasterOnly`: 1
  - `PyRequirement`: reqUpgradeFreedmanWorker
  - `AddPromotions`: 解放奴隷 / 忠誠
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Promote Supply-Base - 兵站基地の都市化

- 内部名: `SPELL_PROMOTE_SUPPLY_BASE`
- 必要テクノロジー: 教育
- 実行文明: リネージ
- 説明（ゲーム内ヘルプ）: 周囲2タイル以内に都市がある場合は実行不可
- その他の設定:
  - `ImprovementPrereq`: 兵站基地
  - `bHasCasted`: 1
  - `iCost`: 100
  - `bAbility`: 1
  - `PyResult`: spellPromoteSupplyBase
  - `PyRequirement`: reqPromoteSupplyBase
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Move with full force - 全力移動

- 内部名: `SPELL_SPRINT_LINEAGE_MOUNTED`
- 実行文明: リネージ
- その他の設定:
  - `UnitCombatPrereq`: 騎乗ユニット
  - `bBeforeMovementOnly`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `AddPromotions`: 快足
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 快足 / 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Frosty swirling air flow

### Concealment - 潜む

- 内部名: `SPELL_CONCEALMENT_LINEAGE_RECON`
- 必要テクノロジー: 追跡術
- 実行文明: リネージ
- 説明（ゲーム内ヘルプ）: 森林/古代樹林/密林/深い密林/灌木林/砦/城/城塞でのみ実行可能。
- その他の設定:
  - `UnitCombatPrereq`: 偵察ユニット
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyRequirement`: reqIncubationLineage
  - `AddPromotions`: 身隠し
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 身隠し / 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Surprise - 奇襲

- 内部名: `SPELL_SURPRISE_LINEAGE_RECON`
- 必要な昇進: 身隠し
- 必要テクノロジー: 毒物
- 実行文明: リネージ
- 射程: 1
- 説明（ゲーム内ヘルプ）: 対象の単一タイルにいるユニット一体にダメージ / （対象は、射程内で最もダメージを与えられる敵ユニットが自動的に選択されます）
- その他の設定:
  - `UnitCombatPrereq`: 偵察ユニット
  - `iCasterMinLevel`: 5
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iDamage`: 90
  - `iDamageLimit`: 99
  - `DamageType`: 物理
  - `iTargetLimitPerPlot`: 2
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Frosty swirling air flow

### Mounting - 騎乗

- 内部名: `SPELL_LINEAGE_MOUNTED`
- 必要な昇進: 馬持ち
- 必要テクノロジー: 鐙
- 実行文明: リネージ
- 説明（ゲーム内ヘルプ）: 馬かナイトメアが必要 / 実行者は騎乗ユニットになる / (採用可能な昇進は変化しない)
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellLineageHorseMounting
  - `PyDisabled`: disabledLineageHorseMounting
  - `PrereqOrUnits`: 狩人 / デクリオン / 弓兵 / 暗殺者 / レンジャー / センチュリオン / 長弓兵 / 聖戦士 / 傭兵 / 盗賊 / ハルムベルテ / アペイロン / 聖騎士 / ゴーゼワロス
  - `AddPromotions`: 騎乗状態
  - `Effect`: Boom

### Dismounting - 下馬

- 内部名: `SPELL_LINEAGE_UNMOUNTED`
- 必要な昇進: 馬持ち
- 必要な昇進(2): 騎乗状態
- 必要テクノロジー: 鐙
- 実行文明: リネージ
- 説明（ゲーム内ヘルプ）: 実行者は騎乗する前の元の兵科に戻る
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellLineageHorseUnMounting
  - `PyRequirement`: reqLineageHorseUnMounting
  - `PrereqOrUnits`: 狩人 / デクリオン / 弓兵 / 暗殺者 / レンジャー / センチュリオン / 長弓兵 / 聖戦士 / 傭兵 / 盗賊 / ハルムベルテ / アペイロン / 聖騎士 / ゴーゼワロス
  - `RemovePromotions`: 騎乗状態
  - `Effect`: Boom

### Transformation - 輸送形態へ変形

- 内部名: `SPELL_TRANSFORMATION_TRANSPORT_MODE`
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyDisabled`: disabledLineageHorseMounting
  - `PrereqOrUnits`: 重バリスタ / ドーラ
  - `AddPromotions`: 輸送形態
  - `Effect`: Boom

### Transformation - 攻撃形態へ変形

- 内部名: `SPELL_TRANSFORMATION_ATTACK_MODE`
- 必要な昇進: 輸送形態
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyRequirement`: reqLineageHorseUnMounting
  - `PrereqOrUnits`: 重バリスタ / ドーラ
  - `RemovePromotions`: 輸送形態
  - `Effect`: Boom

### Monsoon - 豪雨

- 内部名: `SPELL_MONSOON`
- 必要テクノロジー: 変成術
- 実行文明: マサトル
- 説明（ゲーム内ヘルプ）: 敵部隊にダメージを与え、火事を消火し、草原に生えた森林は密林になり、低地では洪水が起きる。
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellMonsoon
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Create Jungle - 密林を作成

- 内部名: `SPELL_JUNGLE`
- 必要な昇進: リザードマン
- 必要な昇進(2): 精神集中Ⅰ
- 必要テクノロジー: 変成術
- その他の設定:
  - `TerrainOrPrereq1`: 草原
  - `TerrainOrPrereq2`: 湿地
  - `bInBordersOnly`: 1
  - `bHasCasted`: 1
  - `iBuildDelay`: 2
  - `CreateFeatureType`: 密林
  - `iPlotProbability`: 100
  - `iAutomateTerrainPriority`: 100
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Bloom

### Spiritual Hammer - 聖霊のハンマー

- 内部名: `SPELL_SPIRITUAL_HAMMER`
- 必要な昇進: 監視者の証
- その他の設定:
  - `bHasCasted`: 1
  - `iAutomatePostcastPriority`: 1020
  - `AddPromotions`: 聖霊のハンマー
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Spiritual Hammer

### Slave Drive - 奴隷の酷使

- 内部名: `SPELL_SLAVE_DRIVE`
- 必要テクノロジー: 邪悪への道
- 実行文明: クアリ
- 説明（ゲーム内ヘルプ）: 現在のすべての都市に奴隷の穴居を建造 / （建造物の効果で都市の特別市民が+4されます）
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellSlaveDrive
  - `PyRequirement`: reqSlaveDrive
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Slave in the Pit - 穴居に放り込む

- 内部名: `SPELL_SLAVE_IN_THE_PIT`
- 必要テクノロジー: 邪悪への道
- 実行ユニット: 奴隷
- 実行文明: クアリ
- 説明（ゲーム内ヘルプ）: 奴隷の穴居のある都市で実行可能 / 都市に無償の特別市民を定住させます
- その他の設定:
  - `BuildingPrereq`: 奴隷の穴居
  - `bCasterNoDuration`: 1
  - `bInBordersOnly`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `PyResult`: spellSlaveInThePit
  - `PyRequirement`: reqSlaveInThePit
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Sacrifice and Blessing - 犠牲と天恵

- 内部名: `SPELL_SACRIFICE_AND_BLESSING`
- 必要な昇進: 神術
- 実行文明: クアリ
- 説明（ゲーム内ヘルプ）: 奴隷を消費
- その他の設定:
  - `UnitInStackPrereq`: 奴隷
  - `bHasCasted`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `PyResult`: spellSacrificeAndBlessing
  - `PyDisabled`: disabledSacrificeAndBlessing
  - `AddPromotions`: 血の刃
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Enchanted Blade

### Bless of Agruonn - アグルオンの祝福

- 内部名: `SPELL_BLESS_OF_AGRUONN`
- 実行ユニット: 奴隷
- 実行文明: クアリ
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `PyDisabled`: disabledBlessedOfAgruonn
  - `AddPromotions`: 鮮血の祝別
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Bless

### Bless of Agruonn - アグルオンの祝福

- 内部名: `SPELL_BLESS_OF_AGRUONN_2`
- 実行ユニット: 奴隷使い
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `iAutomatePostcastPriority`: 1020
  - `AddPromotions`: 鮮血の祝別
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Bless

### Sacrifice for Agruonn - 流血の儀式

- 内部名: `SPELL_SACRIFICE_FOR_AGRUONN`
- 実行ユニット: 奴隷
- 実行文明: クアリ
- 説明（ゲーム内ヘルプ）: 実行する都市上のすべての奴隷を生贄に捧げる / 3体以上を捧げれば、配下の全てのユニットに鮮血の祝別を与える / 9体以上を捧げれば、さらに経験値を4ポイント与える / 15体以上を捧げれば、さらに短めの黄金期が発動し、配下の全ユニットに血の刃を与えて全快させる
- その他の設定:
  - `BuildingPrereq`: アグルオンの祭壇
  - `bCasterNoDuration`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `PyResult`: spellSacrificeForAgronn
  - `PyRequirement`: reqSacrificeForAgronn
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Awakening - 古き者の目覚め

- 内部名: `SPELL_AWAKENING`
- 必要テクノロジー: 意志の力
- 実行ユニット: 人竜王メタトロン
- 実行文明: アルタイル
- 説明（ゲーム内ヘルプ）: 無神論以外の志向を失う / アルタイルの全てのユニットが原初のドラゴンを獲得 / 全てのライバル文明に宣戦布告 / 永続的に外交不能になる
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bSacrificeCaster`: 1
  - `bGlobal`: 1
  - `PyResult`: spellAwakening
  - `PyRequirement`: reqAwakening
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Awakening

### Hatching of juveniles - 幼生の孵化

- 内部名: `SPELL_BORN_DRAGON_PUPPY`
- 必要テクノロジー: 青銅器
- 実行文明: アルタイル
- その他の設定:
  - `BuildingPrereq`: 竜の巣
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iCost`: 40
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: ドラゴンパピー
  - `bPermanentUnitCreate`: 1
  - `iCasterImmobileTurns`: 2
  - `PyResult`: spellBornDragonPuppy
  - `PyDisabled`: disabledBornDragonPuppy
  - `PrereqOrUnits`: 功労者 / 火竜サラマンダー / 黒竜ウシュムガル / 翼竜ナナワトル / 地竜ジャムシード / 炎獄竜フレアブラス / 魔竜ティアマット / 陽煌竜ケツアルコアトル / 覇竜ザッハーク / 水晶竜バハムート / メタトロン / 蒼生のメタトロン / 天荒のメタトロン / 人竜王メタトロン
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Burning breath - 高熱の息吹

- 内部名: `SPELL_DRAGON_SALAMANDER_BLAZE`
- 射程: 1
- 説明（ゲーム内ヘルプ）: 対象の単一タイルにいる全てのユニットに火炎ダメージ / （対象は、射程内で最も多く敵ユニットがいるタイルが自動的に選択されます）
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iDamage`: 10
  - `iDamageLimit`: 60
  - `DamageType`: 火炎
  - `iTargetLimitPerPlot`: 14
  - `iPlotProbability`: 100
  - `bArson`: 1
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `PrereqOrUnits`: 火竜サラマンダー / 炎獄竜フレアブラス
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Scorch
  - `EffectRangedPlot`: Pillar of Fire

### Rotten breath - 腐食の息吹

- 内部名: `SPELL_DRAGON_USHUMGALLU_RUST`
- 射程: 1
- 説明（ゲーム内ヘルプ）: 対象の単一タイルにいる全てのユニットに死ダメージ / （対象は、射程内で最も多く敵ユニットがいるタイルが自動的に選択されます）
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bResistable`: 1
  - `iDamage`: 10
  - `iDamageLimit`: 60
  - `DamageType`: 死
  - `iResistModify`: 10
  - `iTargetLimitPerPlot`: 9
  - `RustPromotion`: 武器の腐食
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `PrereqOrUnits`: 黒竜ウシュムガル / 魔竜ティアマット
  - `AddPromotions`: 弱体化
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom
  - `EffectRangedPlot`: 死と腐敗

### Strong wind - 強風

- 内部名: `SPELL_DRAGON_NANAHUATL_FAIR_WINDS`
- 必要な昇進: 飛行
- その他の設定:
  - `UnitCombatPrereq`: 魔獣ユニット
  - `bBeforeMovementOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `iAutomatePrecastPriority`: 12
  - `iAutomatePostcastPriority`: 1012
  - `AddPromotions`: 追い風
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Frosty swirling air flow

### Protection - 硬化

- 内部名: `SPELL_DRAGON_JAMSHEED_DEFENCE`
- その他の設定:
  - `TerrainOrPrereq1`: 砂漠
  - `TerrainOrPrereq2`: 灼熱の砂地
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iFortifyTurns`: 5
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `iAutomatePostcastPriority`: 1050
  - `PrereqOrUnits`: 地竜ジャムシード / 覇竜ザッハーク
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Stoneskin

### Growth to Elder Dragon - 上級ドラゴンへ成長

- 内部名: `SPELL_ELDER_DRAGON`
- 必要な昇進: 下級ドラゴン
- 必要テクノロジー: 衛生設備
- 実行文明: アルタイル
- その他の設定:
  - `bHasCasted`: 1
  - `iCost`: 30
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyDisabled`: disabledDragonGrow
  - `AddPromotions`: 上級ドラゴン
  - `RemovePromotions`: 下級ドラゴン
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Growth to Greater Dragon - 偉大なドラゴンへ成長

- 内部名: `SPELL_GREATER_DRAGON`
- 必要な昇進: 上級ドラゴン
- 必要テクノロジー: 鉄器
- 実行文明: アルタイル
- その他の設定:
  - `bHasCasted`: 1
  - `iCost`: 50
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyDisabled`: disabledDragonGrow
  - `AddPromotions`: 偉大なドラゴン
  - `RemovePromotions`: 上級ドラゴン
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Mightiness - 強大化

- 内部名: `SPELL_GREAT_DRAGON_SCALE`
- 必要な昇進: ドラゴン
- 必要テクノロジー: ミスリル器
- 実行文明: アルタイル
- その他の設定:
  - `bHasCasted`: 1
  - `iCost`: 100
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyDisabled`: disabledDragonScale
  - `AddPromotions`: 無双
  - `BlockToCastPromotions`: 無双
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Crimson Nought - 紅蓮の弾泡

- 内部名: `SPELL_CRIMSON_NOUGHT`
- 必要な昇進: 原初のドラゴン
- 必要テクノロジー: 全知
- 実行ユニット: 炎獄竜フレアブラス
- 射程: 3
- 説明（ゲーム内ヘルプ）: 効果範囲の地物のない地形に延焼を発生させる / 効果範囲の地形が25%の確率で砂漠か凍土に変化する
- その他の設定:
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `bCausesWar`: 1
  - `iDamage`: 30
  - `iDamageLimit`: 99
  - `DamageType`: 火炎
  - `iTargetLimitPerPlot`: 32
  - `iPlotProbability`: 100
  - `bArson`: 1
  - `RustPromotion`: 武器の腐食
  - `bImmuneTeam`: 1
  - `PyResult`: spellCrimsonNote
  - `PyEnabled`: enabledDummy
  - `RemovePromotions`: 青銅の武器 / 鉄の武器
  - `CastFlagPromotions`: 疲労 / 弱体化
  - `BlockToCastPromotions`: 疲労 / 弱体化
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Tiltowaito

### Evil Dead - 屍霊の臓腑

- 内部名: `SPELL_EVIL_DEAD`
- 必要な昇進: 原初のドラゴン
- 必要テクノロジー: 全知
- 実行ユニット: 魔竜ティアマット
- 射程: 3
- 説明（ゲーム内ヘルプ）: 効果範囲の地物のない地形に悪霊の地を発生させる / アルタイルと休耕志向の文明以外の効果範囲の都市に荒廃による不衛生を発生させる / (不衛生の増加は人口に比例する)
- その他の設定:
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `bCausesWar`: 1
  - `bResistable`: 1
  - `iDamage`: 30
  - `iDamageLimit`: 99
  - `DamageType`: 不浄
  - `iResistModify`: 10
  - `iTargetLimitPerPlot`: 32
  - `bImmuneTeam`: 1
  - `bImmuneNotAlive`: 1
  - `PyResult`: spellEvilDead
  - `PyEnabled`: enabledDummy
  - `AddPromotions`: 病気 / 疫病 / 黒死病
  - `CastFlagPromotions`: 疲労 / 弱体化
  - `BlockToCastPromotions`: 疲労 / 弱体化
  - `bDisplayWhenDisabled`: 1
  - `Effect`: 死と腐敗

### Radiant Gale - 光輝の烈風

- 内部名: `SPELL_RADIANT_GALE`
- 必要な昇進: 原初のドラゴン
- 必要テクノロジー: 全知
- 実行ユニット: 陽煌竜ケツアルコアトル
- 射程: 3
- 説明（ゲーム内ヘルプ）: 効果範囲のタイル整備を破壊する / 効果範囲の都市の建造物を破壊する / 効果範囲の平地タイルを、20%の確率で海洋タイルに変化させる / 効果範囲の砂漠を、50%の確率で湿地に変化させる
- その他の設定:
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `bCausesWar`: 1
  - `iDamage`: 30
  - `iDamageLimit`: 99
  - `DamageType`: 電撃
  - `iTargetLimitPerPlot`: 32
  - `iPlotProbability`: 50
  - `bDouse`: 1
  - `bDestroyBuilding`: 1
  - `bDestroyImprovement`: 1
  - `bImmuneTeam`: 1
  - `PyResult`: spellRadiantGale
  - `PyEnabled`: enabledDummy
  - `AddPromotions`: 鈍足
  - `CastFlagPromotions`: 疲労 / 弱体化
  - `BlockToCastPromotions`: 疲労 / 弱体化
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Tiltowaito

### Crustal Movement - 地殻変動

- 内部名: `SPELL_CRUSTAL_MOVEMENT`
- 必要な昇進: 原初のドラゴン
- 必要テクノロジー: 全知
- 実行ユニット: 覇竜ザッハーク
- 射程: 3
- 説明（ゲーム内ヘルプ）: 効果範囲のタイル整備を破壊する / 効果範囲の都市の建造物を破壊する / 効果範囲の都市とユニットが存在しないタイルは下記の条件で変化する / [SPACE][SPACE]山岳タイルは50%の確率で丘陵タイルに変化する / [SPACE][SPACE]丘陵タイルは30%の確率で平地タイルに変化し、20%の確率で山岳タイルに変化する / [SPACE][SPACE]平地タイルは30%の確率で丘陵タイルに変化し、川沿いでなければ20%の確率で海洋タイルに変化する / [SPACE][SPACE]海洋タイルは川沿いでなければ50%の確率で平地タイルに変化する
- その他の設定:
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `bCausesWar`: 1
  - `iDamage`: 40
  - `iDamageLimit`: 99
  - `DamageType`: 物理
  - `iTargetLimitPerPlot`: 32
  - `iPlotProbability`: 50
  - `bDestroyBuilding`: 1
  - `bDestroyImprovement`: 1
  - `iFortifyTurns`: -5
  - `bImmuneTeam`: 1
  - `bImmuneFlying`: 1
  - `PyResult`: spellEarthquakeZahhak
  - `PyEnabled`: enabledDummy
  - `AddPromotions`: 弱体化
  - `CastFlagPromotions`: 疲労 / 弱体化
  - `BlockToCastPromotions`: 疲労 / 弱体化
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Snowfall

### Freezing breath - 凍てつく息吹

- 内部名: `SPELL_FREEZING_BREATH`
- 実行ユニット: 水晶竜バハムート
- 射程: 2
- 説明（ゲーム内ヘルプ）: 目標の周囲2タイル以内の全ての敵に約20%の冷気ダメージ(上限80%) / 目標の周囲2タイル以内を氷原に変える
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iDamage`: 20
  - `iDamageLimit`: 80
  - `DamageType`: 冷気
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `PyResult`: spellFreezingBreath
  - `AddPromotions`: 弱体化
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Clear Disaster - 清冽なる災い

- 内部名: `SPELL_CLEAR_DISASTER`
- 必要な昇進: 原初のドラゴン
- 必要テクノロジー: 全知
- 実行ユニット: 水晶竜バハムート
- 射程: 3
- 説明（ゲーム内ヘルプ）: 実行者の周囲3タイル以内を氷原に変える
- その他の設定:
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `bCausesWar`: 1
  - `iDamage`: 40
  - `iDamageLimit`: 100
  - `DamageType`: 冷気
  - `iTargetLimitPerPlot`: 32
  - `iPlotProbability`: 100
  - `bDouse`: 1
  - `bImmuneTeam`: 1
  - `PyResult`: spellFreezingBreathGreator
  - `PyEnabled`: enabledDummy
  - `AddPromotions`: 弱体化
  - `CastFlagPromotions`: 疲労 / 弱体化
  - `BlockToCastPromotions`: 疲労 / 弱体化
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Snowfall Greator

### Awakening of induction - 目覚めの誘発

- 内部名: `SPELL_GIFT_ANCIENT_DRAGON`
- 必要な昇進: 原初のドラゴン
- 必要テクノロジー: 意志の力
- 実行文明: アルタイル
- 説明（ゲーム内ヘルプ）: 同じタイルにいる竜人および全てのドラゴンに、原初のドラゴンを与える / 古き者の目覚めの実行が必要
- その他の設定:
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `bImmuneNotAlive`: 1
  - `PyResult`: spellGiftAncientDragon
  - `PyRequirement`: reqGiftAncientDragon
  - `Effect`: Boom

### Add to Dragonmaster - 竜使いの指揮下に入る

- 内部名: `SPELL_ADD_TO_DRAGON_MASTER`
- 実行ユニット: ドラゴンパピー
- 実行文明: アルタイル
- 説明（ゲーム内ヘルプ）: ドラゴンパピーを消費して竜使いに強化の昇進を与える
- その他の設定:
  - `UnitInStackPrereq`: 竜使い
  - `bCasterNoDuration`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `PyResult`: spellAddToDragonMaster
  - `PyRequirement`: reqAddToDragonMaster
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Feeding - 餌を喰う

- 内部名: `SPELL_ANIMAL_EATEN_PUPPY`
- 実行ユニット: ドラゴンパピー
- 実行文明: アルタイル
- 説明（ゲーム内ヘルプ）: 実行ユニットは経験点17未満でなければならない / 術者のいるタイルの動物ユニットを全て消費し、消費した数に応じた経験値を獲得する
- その他の設定:
  - `bIgnoreHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `PyResult`: spellAnimalEatenPuppy
  - `PyRequirement`: reqAnimalEatenPuppy
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Predation - 捕食

- 内部名: `SPELL_PREDATION`
- 実行文明: アルタイル
- 説明（ゲーム内ヘルプ）: ドラゴンまたは竜人が必要 / 術者のいるタイルのドラゴン・竜人以外のユニット1体を消費する / 対象には最も戦闘力の高いユニットが選ばれる
- その他の設定:
  - `bIgnoreMadeAttack`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iHealAmount`: 20
  - `bRemoveMadeAttack`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellPredation
  - `PyRequirement`: reqPredation
  - `RemovePromotions`: 病気 / 疫病 / 衰弱 / 黒死病
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Sacrifice

### Steamworks - 蒸気駆動

- 内部名: `SPELL_STEAMWORKS`
- 必要テクノロジー: 建設
- 実行文明: メカノス
- 説明（ゲーム内ヘルプ）: 国境内の全ての工房、水車、風車から研究を得、呪文が使われた都市に蒸気駆動装置を建設します。
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `CreateBuildingType`: 蒸気駆動装置
  - `PyResult`: spellSteamworks
  - `PyRequirement`: reqSteamworks
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Scorch

### Repair - 修理

- 内部名: `SPELL_REPAIR_MECHANOS`
- 説明（ゲーム内ヘルプ）: ゴーレム、海軍ユニット、攻城兵器を回復
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iHealAmount`: 20
  - `iTargetLimitPerPlot`: 7
  - `bImmuneNotMech`: 1
  - `PrereqOrUnits`: 精製術師 / テックプリースト
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Awaken Machine Spirit - 機械魂を目覚めさせる

- 内部名: `SPELL_AWAKEN_MACHINE`
- 実行ユニット: テックプリースト
- 説明（ゲーム内ヘルプ）: 機械魂の昇進を攻城ユニットに与える
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iAutomatePostcastPriority`: 1020
  - `AddPromotions`: 機械魂
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Entrench - 堅守

- 内部名: `SPELL_ENTRENCH`
- 必要な昇進: 衛生兵Ⅱ
- 実行文明: メカノス
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iFortifyTurns`: 5
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `iAutomatePostcastPriority`: 1050
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Create Dark Council - 闇の協議会を設立

- 内部名: `SPELL_DARK_COUNCIL`
- 実行ユニット: 狡猾なるメランテ
- 実行文明: パトリアの後継者
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `CreateBuildingType`: 闇の協議会
  - `iCreateUnitNum`: 3
  - `CreateUnitType`: 再誕者
  - `bPermanentUnitCreate`: 1
  - `PyRequirement`: reqDarkCouncil
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Add To City - 都市に定住する

- 内部名: `SPELL_SCIONS_ADD_POPULATION`
- 説明（ゲーム内ヘルプ）: 都市へ定住し、人口に追加 / 実行する都市のとに余裕が必要となる
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bSacrificeCaster`: 1
  - `bAbility`: 1
  - `iChangePopulation`: 1
  - `PyRequirement`: reqScionsAddPopuration
  - `PrereqOrUnits`: 覚醒者 / 再誕者
  - `Effect`: Boom

### Blight - 荒廃

- 内部名: `SPELL_BLIGHT`
- 実行ユニット: 嫌われ者
- その他の設定:
  - `bInBordersOnly`: 1
  - `bHasCasted`: 1
  - `iBuildDelay`: 3
  - `CreateFeatureType`: 悪霊の地
  - `iPlotProbability`: 100
  - `iAutomateTerrainPriority`: 100
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Bloom

### Assume Haunt form - 悪霊体になる

- 内部名: `SPELL_HAUNT`
- その他の設定:
  - `FeatureOrPrereq1`: 悪霊の地
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PrereqOrUnits`: 彷徨い人 / 黒衣の貴婦人コリンナ
  - `AddPromotions`: 悪霊体
  - `RemovePromotions`: 幽体
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Burrowing Thorns - 荊棘を埋める

- 内部名: `SPELL_BURRS`
- 必要な昇進: 肥育された蔦
- 実行ユニット: 伸びた蔦
- 射程: 1
- 説明（ゲーム内ヘルプ）: ターン経過毎に30%の確率でダメージを受ける / 80%以上のダメージを負ったユニットは即死 / 都市外で死亡すると蛮族の伸びた蔦が産まれる
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bResistable`: 1
  - `DamageType`: 催眠
  - `iResistModify`: 20
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 毬
  - `Effect`: Sacrifice

### Glory of the Empire - 帝国の栄光

- 内部名: `SPELL_GLORY`
- 実行ユニット: 神祇官
- 実行文明: パトリアの後継者
- その他の設定:
  - `bHasCasted`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `iAutomatePostcastPriority`: 1020
  - `AddPromotions`: 帝国の栄光
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Grand Ward - 偉大なる監視

- 内部名: `SPELL_GRAND_WARD`
- 実行ユニット: 神祇官
- 実行文明: パトリアの後継者
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `bImmuneNotAlive`: 1
  - `iAutomatePostcastPriority`: 1050
  - `AddPromotions`: 士気
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Hauntstalk - 幽体化

- 内部名: `SPELL_HAUNTSTALK`
- 必要な昇進: 屍人
- 実行文明: パトリアの後継者
- その他の設定:
  - `FeatureOrPrereq1`: 悪霊の地
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `AddPromotions`: 幽体
  - `Effect`: Boom

### Summon Creeper - 蔦の召喚

- 内部名: `SPELL_SUMMON_CREEPER`
- 実行文明: パトリアの後継者
- その他の設定:
  - `UnitCombatPrereq`: 偵察ユニット
  - `FeatureOrPrereq1`: 悪霊の地
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 伸びた蔦
  - `bPermanentUnitCreate`: 1
  - `bBuffCasterOnly`: 1
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Embrace Gift - ギフトを受け取る

- 内部名: `SPELL_EMBRACE_GIFT`
- 実行文明: パトリアの後継者
- その他の設定:
  - `BuildingPrereq`: ギフトの寺院
  - `bCasterMustBeAlive`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iDelay`: 1
  - `bBuffCasterOnly`: 1
  - `PyRequirement`: reqEmbraceGift
  - `AddPromotions`: 屍人
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Geas - 制約

- 内部名: `SPELL_GEAS`
- 必要な昇進: 神術
- 実行文明: パトリアの後継者
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bResistable`: 1
  - `iResistModify`: 30
  - `iTargetLimitPerPlot`: 9
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 制約
  - `RemovePromotions`: 祝福 / 信仰の盾
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Mend - 修繕

- 内部名: `SPELL_MEND`
- 必要な昇進: 神術
- 実行文明: パトリアの後継者
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `iHealAmount`: 20
  - `iTargetLimitPerPlot`: 16
  - `RemovePromotions`: 毒 / 衰弱
  - `ExclusivePromotions`: 屍人
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Become Corporeal - 肉体を取り戻す

- 内部名: `SPELL_DEHAUNT_KORRINA`
- 必要な昇進: 悪霊体
- 実行ユニット: 黒衣の貴婦人コリンナ
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `RemovePromotions`: 悪霊体
  - `Effect`: Boom

### Build Thaumaturge's Keep - 魔道士の砦の建設

- 内部名: `SPELL_THAUMATURGE_KEEP`
- 実行ユニット: 奇術師アルキヌス
- 説明（ゲーム内ヘルプ）: 4つの特殊施設をランダムに作成する / 首都では実行不可（OCCの場合を除く）
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `CreateBuildingType`: 魔道士の砦
  - `PyResult`: spellThaumaturge
  - `PyRequirement`: reqThaumaturge
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Oration - 演説

- 内部名: `SPELL_ROUSING_ORATION`
- 実行ユニット: 金舌のプレモク
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `CreateBuildingType`: 情熱溢るる演説
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Succor - 支援

- 内部名: `SPELL_SCIONS_SUCCOR`
- 実行ユニット: 金舌のプレモク
- 説明（ゲーム内ヘルプ）: 他国の都市で人口に比例した数の再誕者を獲得して自国の首都に送る
- その他の設定:
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iCost`: 25
  - `bAbility`: 1
  - `iDelay`: 12
  - `PyResult`: spellSuccor
  - `PyRequirement`: reqSuccor
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Wither

### Govern City - 都市を統治

- 内部名: `SPELL_MELANTE_RESIDENCE`
- 実行ユニット: 狡猾なるメランテ
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `CreateBuildingType`: メランテの大邸宅
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Tricks - わるだくみ

- 内部名: `SPELL_TRICKS_NIVAL`
- 必要テクノロジー: 祝祭
- 実行文明: ニバル
- 説明（ゲーム内ヘルプ）: ニバル以外の全ての都市のが減少 / ニバルの全ての都市のが増大
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellTricksNival
  - `PyRequirement`: reqTricksNival
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Prank - いたずら

- 内部名: `SPELL_PRANK_NIVAL`
- 必要な昇進: フロストリング
- 必要テクノロジー: 青銅器
- 実行文明: ニバル
- 射程: 1
- 説明（ゲーム内ヘルプ）: 術者のタイルに、術者の文明のを生み出す / 術者の文明の文化圏の外側に隣接していなければならない
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `PyResult`: spellPrankNival
  - `PyRequirement`: reqPrankNival
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Pathetic Fire - 悲壮の炎

- 内部名: `SPELL_PATHETIC_FIRE`
- 必要テクノロジー: 狂信
- 実行文明: ラーナ
- 説明（ゲーム内ヘルプ）: 敵味方問わず、すべての都市の防御力を0にする / 敵味方問わず、すべてのユニットに約50%の火炎ダメージ(上限90%)
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellPatheticFire
  - `PyRequirement`: reqPatheticFire
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Bhava-agra - 無色の火

- 内部名: `SPELL_BHAVA_AGRA`
- 実行ユニット: ミカエル
- 射程: 5
- 説明（ゲーム内ヘルプ）: 他国の領土を巻き込むと宣戦 / 範囲内にある都市防御値をランダムに減らす(最大100%) / 自国都市に対しても効果が及ぶ
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `iDamage`: 20
  - `iDamageLimit`: 60
  - `DamageType`: 火炎
  - `iTargetLimitPerPlot`: 7
  - `iPlotProbability`: 100
  - `bArson`: 1
  - `PyResult`: spellBhavaagra
  - `PyDisabled`: disabledBhavaagra
  - `PyEnabled`: enabledBhavaagra
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fire Storm
  - `EffectRangedPlot`: Artillery's Shell explosion

### Wedge of Return - 帰路の楔

- 内部名: `SPELL_WEDGE_OF_RETURNE`
- 実行文明: ラーナ
- 説明（ゲーム内ヘルプ）: 一瞬で首都まで移動 / 実行者は1ポイントの経験点を失う
- その他の設定:
  - `iCasterMinLevel`: 2
  - `bCasterNoDuration`: 1
  - `bIgnoreMadeAttack`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iHealAmount`: 100
  - `iCasterImmobileTurns`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellWedgeofReturn
  - `PyRequirement`: reqWedgeofReturn
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Soul Depletion - 魂の枯渇

- 内部名: `SPELL_SOUL_DEPLETION`
- 実行文明: ラーナ
- 説明（ゲーム内ヘルプ）: 人間性を都市へ捧げ、人口を増加させる / 実行者は2ポイントの経験点を失う / 実行する都市のととに余裕が必要となる / 実行には拡散する堕落を完成させていなければならない
- その他の設定:
  - `BuildingPrereq`: 要の祭壇
  - `iCasterMinLevel`: 2
  - `bCasterMustBeAlive`: 1
  - `bCasterNoDuration`: 1
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iChangePopulation`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellSoulDepletion
  - `PyRequirement`: reqSoulDepletion
  - `AddPromotions`: 魔族 / 魂の飢餓
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Soul Sucker - 魂吸い

- 内部名: `SPELL_SOUL_SUCKER`
- 必要な昇進: 魂の飢餓
- 実行文明: ラーナ
- 射程: 1
- 説明（ゲーム内ヘルプ）: 対象の単一タイルにいるユニット1体に不浄ダメージ / （対象は、射程内で最も多く敵ユニットがいるタイルが自動的に選択されます） / 実行者は魂の飢餓を失う / 実行者は2ポイントの経験点を得る / 実行者はダメージを全回復する / 実行には拡散する堕落を完成させていなければならない
- その他の設定:
  - `bHasCasted`: 1
  - `PromotionCost`: 魂の飢餓
  - `iDamage`: 80
  - `iDamageLimit`: 99
  - `DamageType`: 不浄
  - `iTargetLimitPerPlot`: 1
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `PyResult`: spellSoulSucker
  - `PyDisabled`: disabledSoulSucker
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom
  - `EffectRangedPlot`: Entropy Summon

### Fame - 名声

- 内部名: `SPELL_FAME`
- 必要テクノロジー: 通貨
- 実行文明: ティーグル
- 説明（ゲーム内ヘルプ）: 全ての都市から人口に応じた数の傭兵を雇う（5人口につき2ユニット） / この呪文では国家ユニットの上限を無視して傭兵を得ることが出来る
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `iCost`: 500
  - `bGlobal`: 1
  - `PyResult`: spellFame
  - `PyRequirement`: reqFame
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Outbreak Contracts - 契約開戦

- 内部名: `SPELL_OUTBREAK_CONTRACTS`
- 必要テクノロジー: 通貨
- 実行文明: ティーグル
- 説明（ゲーム内ヘルプ）: 実行した都市文明のプレイヤーと契約を結び、契約戦争を開始する / 雇用主と交戦中のすべての文明に対して宣戦布告 / 撃破数・都市陥落数に応じて報酬を得られる
- その他の設定:
  - `bInCityOnly`: 1
  - `bAbility`: 1
  - `PyResult`: spellOutbreakContracts
  - `PyRequirement`: reqOutbreakContracts
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Contract Out - 契約の解消

- 内部名: `SPELL_CONTRACT_OUT`
- 必要テクノロジー: 通貨
- 実行文明: ティーグル
- 説明（ゲーム内ヘルプ）: 戦争契約を解消します / 契約宣戦した全ての文明と和平 / 報酬を得る
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bAbility`: 1
  - `PyResult`: spellContractOut
  - `PyRequirement`: reqContractOut
  - `Effect`: Creation Effect Dim

### Recruit Mercenaries - 傭兵募兵

- 内部名: `SPELL_MERCENARIES_RECRUIT`
- 必要な昇進: 勲功
- 実行ユニット: アイン
- 説明（ゲーム内ヘルプ）: 都市の人口に応じた数の傭兵を追加雇用（3人口につき1ユニット）
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iCost`: 500
  - `PromotionCost`: 勲功
  - `bAbility`: 1
  - `PyResult`: spellMercenariesRecruit
  - `PyRequirement`: reqTargetFree
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Recruit Funeral Mercenaries - 傭兵を雇う

- 内部名: `SPELL_RECRUIT_MERCENARY_FUNERAL`
- 実行ユニット: スマイリー
- 説明（ゲーム内ヘルプ）: 4体の葬送傭兵団を配下に加える
- その他の設定:
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iCost`: 500
  - `bAbility`: 1
  - `iCreateUnitNum`: 4
  - `CreateUnitType`: 葬送傭兵団
  - `bPermanentUnitCreate`: 1
  - `PyRequirement`: reqRecruitMercenaryFuneral
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Resurrection of the Dead - 亡者の再生

- 内部名: `SPELL_SUMMON_MERCENARY_UNDEAD`
- 実行ユニット: スマイリー
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 4
  - `CreateUnitType`: 傭兵の亡骸
  - `bPermanentUnitCreate`: 1
  - `bBuffCasterOnly`: 1
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Bribe - 賄賂

- 内部名: `SPELL_MERCENARIES_BRIBE`
- 実行ユニット: ルイーザ
- 実行文明: ティーグル
- 説明（ゲーム内ヘルプ）: 契約戦争における敵文明の都市の隣接タイルで実行可能 / 賄賂を支払い雇用主の文明と停戦させる / 雇用主の指導者から外交態度+2が発生
- その他の設定:
  - `bHasCasted`: 1
  - `iCost`: 200
  - `bAbility`: 1
  - `PyResult`: spellMercenariesBribe
  - `PyRequirement`: reqMercenariesBribe
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Incitement - 裏切り

- 内部名: `SPELL_MERCENARIES_INCITEMENT`
- 実行ユニット: ルイーザ
- 実行文明: ティーグル
- 説明（ゲーム内ヘルプ）: 契約戦争における中立文明の都市で実行可能 / 賄賂を支払い雇用主の文明に宣戦させる / (けしかけた文明は契約戦争の対象にならない) / 雇用主の指導者から外交態度-6が発生
- その他の設定:
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iCost`: 500
  - `bAbility`: 1
  - `PyResult`: spellMercenariesIncitement
  - `PyRequirement`: reqMercenariesIncitement
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Yell - 気合

- 内部名: `SPELL_YELL`
- 実行ユニット: アントニオ
- 説明（ゲーム内ヘルプ）: 気合Ⅰ～Ⅴのうち1つを得る
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellYell
  - `PyRequirement`: reqYell
  - `iAutomatePrecastPriority`: 7
  - `iAutomatePostcastPriority`: 1007
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Frosty swirling air flow

### Recruit Mercenary - 傭兵を募る

- 内部名: `SPELL_RECRUIT_MERCENARY_TIGER`
- 必要テクノロジー: 通貨
- 実行文明: ティーグル
- 説明（ゲーム内ヘルプ）: 酒場があれば2割引き
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iCost`: 120
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: ティーグル傭兵団
  - `bPermanentUnitCreate`: 1
  - `PyResult`: spellRecruitMercenaryTiger
  - `PyDisabled`: disabledRecruitMercenaryTiger
  - `Effect`: Boom

### Call Vulepes - ブランフォードを呼び出す

- 内部名: `SPELL_HIRE_VULEPES`
- 必要テクノロジー: 医薬
- 実行ユニット: フォックス
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: ブランフォード
  - `bPermanentUnitCreate`: 1
  - `bBuffCasterOnly`: 1
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Call Coyote - コヨーテを呼び出す

- 内部名: `SPELL_HIRE_COYOTE`
- 必要テクノロジー: 医薬
- 実行ユニット: ハウンド
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: コヨーテ
  - `bPermanentUnitCreate`: 1
  - `bBuffCasterOnly`: 1
  - `CastFlagPromotions`: 疲労
  - `BlockToCastPromotions`: 疲労
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Call of Overlords - 旧支配者の呼び声

- 内部名: `SPELL_CALL_OF_OVERLORDS`
- 必要テクノロジー: 神学
- 実行文明: ゾス
- 説明（ゲーム内ヘルプ）: -30: 正気度(0より低くはならない) / 深海の旧支配者を信奉する生物に狂乱を与える / 深海の旧支配者を信奉する生物は、10%の確率で深きものどもに転生 / 深海の旧支配者を信奉していない生物は、25%の確率で狂乱を得る / 深海の旧支配者の布教された全都市で感謝祭が発生する / 自国の沿岸都市にクラーケンが一体ずつ与えられる
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellCallofOverlords
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Distorting the dimension - 次元を歪める

- 内部名: `SPELL_DISTORTING_THE_DIMENSION`
- 実行文明: ゾス
- 説明（ゲーム内ヘルプ）: +1: 正気度
- その他の設定:
  - `bBeforeMovementOnly`: 1
  - `bHasCasted`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellDistorting
  - `PyDisabled`: disabledDistorting
  - `PrereqOrUnits`: 深きものども / 黄泉の番人 / シュブ=ニグラス / ニャルラトテップ / ヨグ=ソトース / ショゴス / ティンダロスの猟犬 / イスの大いなる種族 / 古のもの
  - `AddPromotions`: 次元歪曲
  - `BlockToCastPromotions`: 次元歪曲
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Energy Drain - 吸精

- 内部名: `SPELL_ENERGY_DRAIN`
- 実行文明: ゾス
- 射程: 1
- 説明（ゲーム内ヘルプ）: 術者は最大で50%回復 / 術者は経験ポイント: ±0～＋10 / +3: 正気度 / 正気度：40未満が必要
- その他の設定:
  - `bHasCasted`: 1
  - `iDamage`: 25
  - `iDamageLimit`: 50
  - `DamageType`: 不浄
  - `iTargetLimitPerPlot`: 1
  - `bBestPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `PyResult`: spellEnergyDrain
  - `PyDisabled`: disabledEnergyDrain
  - `PrereqOrUnits`: ティンダロスの猟犬 / イスの大いなる種族 / 古のもの
  - `AddPromotions`: 狂乱
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Crazy Eyes - 狂気の眼差し

- 内部名: `SPELL_CRASY_EYES`
- 実行文明: ゾス
- 射程: 2
- 説明（ゲーム内ヘルプ）: +5: 正気度 / 正気度：20未満が必要
- その他の設定:
  - `bHasCasted`: 1
  - `bResistable`: 1
  - `iDamage`: 30
  - `iDamageLimit`: 60
  - `DamageType`: 不浄
  - `iResistModify`: 5
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `PyResult`: spellCrazyEyes
  - `PyDisabled`: disabledCrazyEyes
  - `PrereqOrUnits`: シュブ=ニグラス / ニャルラトテップ / ヨグ=ソトース / ティンダロスの猟犬 / イスの大いなる種族 / 古のもの
  - `AddPromotions`: 狂乱
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### City Emerge - 都市の浮上

- 内部名: `SPELL_CITY_EMERGE`
- 実行文明: ゾス
- 射程: 6
- 説明（ゲーム内ヘルプ）: +5: 正気度 / 正気度：60未満が必要 / 付近の海洋タイルに都市が出現する
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `PyResult`: spellCityEmerge
  - `PyRequirement`: reqCityEmerge
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Body Snatch - 肉体奪取

- 内部名: `SPELL_BODYSNATCH`
- 必要な昇進: イスの大いなる種族
- 実行文明: ゾス
- 射程: 1
- 説明（ゲーム内ヘルプ）: 範囲内の敵ユニット1つの肉体を奪い取る / 成功したら対象者は死に、術者は対象者の昇進を全て獲得する / 正気度が下がると対象の呪文抵抗を無視することがある / 失敗したら術者は死ぬ / +3: 正気度 / 正気度：60未満が必要
- その他の設定:
  - `bHasCasted`: 1
  - `bResistable`: 1
  - `iResistModify`: 20
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `PyResult`: spellBodysnatch
  - `PyRequirement`: reqBodysnatch
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Wind unsayable - 名状し難い風

- 内部名: `SPELL_WIND_UNSAYABLE`
- 必要テクノロジー: 魔術
- 実行文明: バルドルアールヴ
- 説明（ゲーム内ヘルプ）: 世界中のすべての生物の肉体に様々な変異を引き起こし死のダメージを与える
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellWindunsayable
  - `PyRequirement`: reqWindunsayable
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Tutorial of meal - チュートリアル

- 内部名: `SPELL_TUTORIAL_OF_MEAL`
- 実行ユニット: 使者ロミアス
- 射程: 1
- 説明（ゲーム内ヘルプ）: 奴隷を消費
- その他の設定:
  - `UnitInStackPrereq`: 奴隷
  - `bHasCasted`: 1
  - `iMovementCost`: 1
  - `bAbility`: 1
  - `bResistable`: 1
  - `iDamage`: 5
  - `iDamageLimit`: 80
  - `DamageType`: 物理
  - `iResistModify`: 25
  - `iTargetLimitPerPlot`: 7
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `PyResult`: spellTutorialOfMeal
  - `AddPromotions`: 狂乱 / 狂暴 / 寄生体
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Hands of Dimension - 異次元の手

- 内部名: `SPELL_HANDS_OF_DIMENSION`
- 必要テクノロジー: エーテルの知識
- 実行文明: バルドルアールヴ
- 射程: 3
- 説明（ゲーム内ヘルプ）: 対象ユニットを隣接タイルのいずれかへ瞬時に移動させる
- その他の設定:
  - `UnitCombatPrereq`: 弓術ユニット
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bResistable`: 1
  - `DamageType`: 催眠
  - `iResistModify`: 30
  - `iTargetLimitPerPlot`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `PyResult`: spellHandsOfDimension
  - `PyRequirement`: reqHandsOfDimension
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Fizzle

### Breeding - 成長

- 内部名: `SPELL_BLEEDING`
- 必要テクノロジー: 野生の触れ合い
- 実行文明: バルドルアールヴ
- 説明（ゲーム内ヘルプ）: 実行者のいるタイルの森林・古代樹林は若き森林に置き換わる
- その他の設定:
  - `FeatureOrPrereq1`: 森林
  - `FeatureOrPrereq2`: 古代樹林
  - `bInBordersOnly`: 1
  - `bHasCasted`: 1
  - `iCost`: 100
  - `ConvertUnitType`: トレント
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellBreeding
  - `PrereqOrUnits`: ドリュアス / トリフィド
  - `AddPromotions`: 人食い
  - `Effect`: Boom

### Parasite - 寄生

- 内部名: `SPELL_PARASITE`
- 必要な昇進: 植物
- 実行文明: バルドルアールヴ
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `iMovementCost`: 1
  - `bAbility`: 1
  - `bResistable`: 1
  - `iResistModify`: 20
  - `iTargetLimitPerPlot`: 14
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `bImmuneNotAlive`: 1
  - `AddPromotions`: 寄生体
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Reconstruction - 再構築

- 内部名: `SPELL_RECONSTRUCTION`
- 実行文明: ノービアイ
- 説明（ゲーム内ヘルプ）: 領内の陸地に存在する資源が変化する / さらに新たな資源が生成される
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellReconstruction
  - `PyRequirement`: reqReconstruction
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Food distribution - 食糧分配

- 内部名: `SPELL_FOOD_DISTRIBUTION`
- 実行文明: ノービアイ
- 説明（ゲーム内ヘルプ）: 都市の人口を消費して、すべての都市の食糧貯蔵ポイントを増加させる
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `iMovementCost`: 999
  - `bAbility`: 1
  - `PyResult`: spellFoodDistribution
  - `PyRequirement`: reqFoodDistribution
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Transplant a living tissue - 生体移植

- 内部名: `SPELL_TRANSPLANT`
- 必要な昇進: 木偶
- 実行文明: ノービアイ
- 説明（ゲーム内ヘルプ）: -1: 都市の人口 / 実行する都市のに余裕が必要となる
- その他の設定:
  - `bCasterNoDuration`: 1
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bHasCasted`: 1
  - `PromotionCost`: 木偶
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellTransplant
  - `PyDisabled`: disableTransplant
  - `AddPromotions`: 天使の匣
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Missile Injection - 鉄の火球の射出

- 内部名: `SPELL_MISSILE_INJECTION`
- 必要テクノロジー: 機械
- その他の設定:
  - `bBeforeMovementOnly`: 1
  - `bHasCasted`: 1
  - `iMovementCost`: 1
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 鉄の火球
  - `PrereqOrUnits`: ノイン・クーゲル / 戦車のゴーレム / 幻想機甲部隊 / 歩行戦車 / 大蜘蛛のゴーレム
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Death March - 死の行進

- 内部名: `SPELL_DEATH_MARCH`
- 必要テクノロジー: 屍霊術
- 実行文明: アリストラク
- 説明（ゲーム内ヘルプ）: すべての屍人ユニットに死の行進の昇進を与えます
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellDeathMarch
  - `PyRequirement`: reqDeathMarch
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Ouroboros - 永劫回帰

- 内部名: `SPELL_OUROBOROS`
- 必要テクノロジー: 錬金術
- 実行文明: メギスス
- 説明（ゲーム内ヘルプ）: 志向を一つランダムに獲得する
- その他の設定:
  - `bInCapitalOnly`: 1
  - `bIgnoreHasCasted`: 1
  - `bIgnoreMadeAttack`: 1
  - `bGlobal`: 1
  - `PyResult`: spellOuroboros
  - `PyEnabled`: enabledDummy
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Incubation - 孵卵

- 内部名: `SPELL_INCUBATION`
- 実行ユニット: 孵らせる者キリコ
- 実行文明: メギスス
- 説明（ゲーム内ヘルプ）: -1: 都市の人口 / 実行する都市のが増加する / 魔女の素体には長期の召喚期限が与えられる
- その他の設定:
  - `bInBordersOnly`: 1
  - `bInCityOnly`: 1
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: 魔女の素体
  - `bPermanentUnitCreate`: 1
  - `PyResult`: spellIncubation
  - `PyDisabled`: disabledIncubation
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Entropy Summon

### Drilling homunculus - ホムンクルスの錬成

- 内部名: `SPELL_DRILLING_HOMUNCULUS`
- 実行ユニット: 錬金術師
- その他の設定:
  - `bHasCasted`: 1
  - `iCreateUnitNum`: 1
  - `CreateUnitType`: ホムンクルス
  - `bPermanentUnitCreate`: 1
  - `PyResult`: spellDrillingHomunculus
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Entropy Summon

### Destroy Undead - 屍人祓い

- 内部名: `SPELL_DESTROY_DEMON`
- 射程: 1
- その他の設定:
  - `bTriggeredSpell`: 1
  - `iDamageLimit`: 50
  - `DamageType`: 神聖
  - `PromotionExclusiveDamages`: 魔族 iDamage=30

### Self-Explode - 自爆

- 内部名: `SPELL_PYRE_EXPLODE_MINOR`
- 射程: 1
- その他の設定:
  - `bAbility`: 1
  - `bTriggeredSpell`: 1
  - `iDamage`: 10
  - `iDamageLimit`: 80
  - `DamageType`: 火炎
  - `iTargetLimitPerPlot`: 7
  - `iPlotProbability`: 25
  - `bArson`: 1
  - `Effect`: Artillery's Shell explosion

### Self-Explode - 自爆

- 内部名: `SPELL_PYRE_EXPLODE_GREATER`
- 射程: 1
- その他の設定:
  - `bAbility`: 1
  - `bTriggeredSpell`: 1
  - `iDamage`: 20
  - `iDamageLimit`: 90
  - `DamageType`: 火炎
  - `iTargetLimitPerPlot`: 12
  - `iPlotProbability`: 25
  - `bArson`: 1
  - `Effect`: Artillery's Shell explosion

### Self-Explode - 自爆

- 内部名: `SPELL_COMBAT_COLD`
- 射程: 1
- その他の設定:
  - `bAbility`: 1
  - `bTriggeredSpell`: 1
  - `iDamage`: 5
  - `iDamageLimit`: 40
  - `DamageType`: 冷気
  - `iTargetLimitPerPlot`: 7
  - `iPlotProbability`: 25
  - `bDouse`: 1
  - `Effect`: Spring

### Self-Explode - 自爆

- 内部名: `SPELL_COMBAT_LIGHTNING`
- 射程: 1
- その他の設定:
  - `bAbility`: 1
  - `bTriggeredSpell`: 1
  - `iDamage`: 5
  - `iDamageLimit`: 40
  - `DamageType`: 電撃
  - `iTargetLimitPerPlot`: 7
  - `iPlotProbability`: 25
  - `Effect`: Maelstrom

### Self-Explode - 自爆

- 内部名: `SPELL_COMBAT_POISON`
- 射程: 1
- その他の設定:
  - `bAbility`: 1
  - `bTriggeredSpell`: 1
  - `iDamage`: 10
  - `iDamageLimit`: 60
  - `DamageType`: 毒
  - `iTargetLimitPerPlot`: 7
  - `iPlotProbability`: 25
  - `Effect`: Poison Cloud

### Self-Explode - 自爆

- 内部名: `SPELL_COMBAT_BLIZZARD`
- 射程: 1
- その他の設定:
  - `bAbility`: 1
  - `bTriggeredSpell`: 1
  - `iDamage`: 10
  - `iDamageLimit`: 80
  - `DamageType`: 冷気
  - `iTargetLimitPerPlot`: 7
  - `iPlotProbability`: 100
  - `bDouse`: 1
  - `PyResult`: spellCombatBlizzard
  - `Effect`: Spring

### Annihilation - 反作用爆発

- 内部名: `SPELL_EXPLOSION_BLIME_FIRE`
- 射程: 2
- その他の設定:
  - `bCausesWar`: 1
  - `bTriggeredSpell`: 1
  - `iDamage`: 25
  - `iDamageLimit`: 80
  - `DamageType`: 火炎
  - `bImmuneTeam`: 1

### Freezing breath - 凍てつく息吹

- 内部名: `SPELL_FREEZING_BREATH_SECONDARY`
- 射程: 2
- その他の設定:
  - `bAbility`: 1
  - `bTriggeredSpell`: 1
  - `iDamage`: 20
  - `iDamageLimit`: 80
  - `DamageType`: 冷気
  - `iPlotProbability`: 100
  - `bDouse`: 1
  - `bImmuneTeam`: 1
  - `bImmuneNeutral`: 1
  - `PyResult`: spellFreezingBreathSecondary
  - `AddPromotions`: 弱体化

### Protection of the earth - 大地の護り

- 内部名: `SPELL_STONESKIN_EARTH_PULSE`
- 必要な昇進: 地脈の戦槌
- その他の設定:
  - `bHasCasted`: 1
  - `bBuffCasterOnly`: 1
  - `iAutomatePrecastPriority`: 31
  - `iAutomatePostcastPriority`: 1031
  - `AddPromotions`: 石の皮膚
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Stoneskin

### Nightmare - 悪夢

- 内部名: `SPELL_BRACELET_OF_NIGHTMARE_GOSPEL`
- 必要な昇進: 夢魔の腕輪
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bResistable`: 1
  - `DamageType`: 催眠
  - `iResistModify`: 40
  - `bImmuneTeam`: 1
  - `AddPromotions`: 狂暴
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Heal of Yggdrasil - 世界樹の癒し

- 内部名: `SPELL_HEAL_ORB_OF_YGGFRASIL`
- 必要な昇進: 世界樹の宝珠
- その他の設定:
  - `bHasCasted`: 1
  - `iHealAmount`: 10
  - `iTargetLimitPerPlot`: 16
  - `bImmuneNeutral`: 1
  - `bImmuneEnemy`: 1
  - `bImmuneNotAlive`: 1
  - `iAutomatePostcastPriority`: 1030
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Creation Effect Dim

### Darkness - 闇

- 内部名: `SPELL_DEMONS_FANG_DARKNESS`
- 必要な昇進: 悪魔の牙
- 射程: 1
- その他の設定:
  - `bHasCasted`: 1
  - `bCausesWar`: 1
  - `bResistable`: 1
  - `DamageType`: 催眠
  - `iResistModify`: 5
  - `bImmuneTeam`: 1
  - `AddPromotions`: 盲目
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Use Mutation Potion - 突然変異の秘薬を使う

- 内部名: `SPELL_MUTATION_POTION`
- 必要な昇進: PROMOTION_MUTATION_POTION
- 説明（ゲーム内ヘルプ）: この秘薬があと何回使えるかは不明 / ランダムな昇進を1つ獲得
- その他の設定:
  - `bHasCasted`: 1
  - `bAbility`: 1
  - `bBuffCasterOnly`: 1
  - `PyResult`: spellMutationPotion
  - `PyRequirement`: reqTargetFree
  - `bDisplayWhenDisabled`: 1
  - `Effect`: Boom

### Eat Bug Da Rake - バグ・ダ・ラケーを食べる

- 内部名: `SPELL_EAT_BUG_DA_RAKE`
- 必要な昇進: PROMOTION_BUG_DA_RAKE
- 説明（ゲーム内ヘルプ）: 食べられません
- その他の設定:
  - `bIgnoreHasCasted`: 1
  - `bAbility`: 1
  - `PyResult`: spellEatBugDaRake
  - `PyRequirement`: reqTargetFree
