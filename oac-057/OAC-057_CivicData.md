# OAC/社会制度（0.57、XMLから生成）

- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）
- 生成元: `Gameinfo/CIV4CivicInfos.xml`
- 読み方: 主要な項目は日本語ラベル付きで先頭に、それ以外の既定値でない設定は「その他の設定」にXMLのタグ名のまま列挙する。値の内部名は日本語名に置き換えている。Pythonで実装された効果はXMLにないため含まない（ゲーム内ヘルプの説明文があれば載せている）。

## 労働制度

### Tribalism - 部族社会

- 内部名: `CIVIC_TRIBALISM`
- 分類: 労働制度
- その他の設定:
  - `iAnarchyLength`: 1

### Apprenticeship - 徒弟制

- 内部名: `CIVIC_APPRENTICESHIP`
- 分類: 労働制度
- 必要テクノロジー: 教育
- 維持費: 低額
- その他の設定:
  - `iAnarchyLength`: 1
  - `iFreeExperience`: 2
  - `SpecialBuildingNotRequireds`: SPECIALBUILDING_TEMPLE / SPECIALBUILDING_MAGE_GUILD

### Emancipation - 奴隷解放

- 内部名: `CIVIC_EMANCIPATION`
- 分類: 労働制度
- 必要テクノロジー: 叡智への道
- 維持費: 高額
- その他の設定:
  - `iAnarchyLength`: 1
  - `iBuildingProductionModifier`: 15
  - `iWarWearinessModifier`: 50
  - `iFreeSpecialist`: 1
  - `BuildingHappinessChanges`: 巡業サーカス iHappinessChange=1
  - `BuildingHealthChanges`: 薬草師 iHealthChange=1
  - `ImprovementUpgradeRateModifiers`: 小屋 iImprovementUpgradeRateModifier=100 / 部落 iImprovementUpgradeRateModifier=100 / 村 iImprovementUpgradeRateModifier=100 / 町 iImprovementUpgradeRateModifier=100 / ユルト iImprovementUpgradeRateModifier=100 / ゴウム iImprovementUpgradeRateModifier=100 / 砦 iImprovementUpgradeRateModifier=100 / 城 iImprovementUpgradeRateModifier=100 / 城塞 iImprovementUpgradeRateModifier=100 / 狩猟場 iImprovementUpgradeRateModifier=100 / 牧草地 iImprovementUpgradeRateModifier=100 / 鉱山 iImprovementUpgradeRateModifier=100 / 工房 iImprovementUpgradeRateModifier=100 / 緑葉の庵 iImprovementUpgradeRateModifier=100 / 緑葉の邑 iImprovementUpgradeRateModifier=100 / 緑葉の里 iImprovementUpgradeRateModifier=100
  - `ImprovementYieldChanges`: 大農園 +1[商業]
  - `BlockAlignment`: 邪悪

### Slavery - 奴隷制

- 内部名: `CIVIC_SLAVERY`
- 分類: 労働制度
- 必要テクノロジー: 採鉱
- 維持費: 低額
- その他の設定:
  - `iAnarchyLength`: 1
  - `Hurrys`: HURRY_POPULATION
  - `ImprovementYieldChanges`: 採石場 +1[商業] / 養蚕場 +3[商業]
  - `iEnslavementChance`: 25
  - `BlockAlignment`: 善良

### Military State - 軍事国家

- 内部名: `CIVIC_MILITARY_STATE`
- 分類: 労働制度
- 必要テクノロジー: 軍事行動
- 維持費: 高額
- その他の設定:
  - `iAnarchyLength`: 1
  - `iMilitaryProductionModifier`: 25
  - `iFreeUnitsPopulationPercent`: 20
  - `iMaxConscript`: 3
  - `iWarWearinessModifier`: -50
  - `CommerceModifiers`: -25[文化]
  - `Hurrys`: HURRY_GOLD

### Caste System - カースト制

- 内部名: `CIVIC_CASTE_SYSTEM`
- 分類: 労働制度
- 必要テクノロジー: 封建制
- 維持費: 中程度
- その他の設定:
  - `iAnarchyLength`: 1
  - `iWorkerSpeedModifier`: 50
  - `YieldModifiers`: +10[ハンマー]
  - `SpecialistExtraYields`: +1[ハンマー]
  - `ImprovementYieldChanges`: 鉱山 +1[商業] / 立坑鉱山 +1[商業] / 工房 +1[ハンマー] / ドワーフの工房 +1[ハンマー]

### Guilds - ギルド制

- 内部名: `CIVIC_GUILDS`
- 分類: 労働制度
- 必要テクノロジー: ギルド
- 維持費: 中程度
- その他の設定:
  - `iAnarchyLength`: 1
  - `Hurrys`: HURRY_GOLD
  - `SpecialistValids`: 吟遊詩人 / 技師 / 商人 / 賢者
  - `ImprovementYieldChanges`: 製材所 +1[ハンマー] / 風車 +1[ハンマー] / 水車 +1[ハンマー]

### Clientera - 庇護制

- 内部名: `CIVIC_CLIENTERA`
- 分類: 労働制度
- 必要テクノロジー: 法律
- 維持費: 高額
- その他の設定:
  - `iAnarchyLength`: 1
  - `iFreeUnitsPopulationPercent`: 30
  - `iWarWearinessModifier`: -10
  - `CommerceModifiers`: 25[文化]
  - `ImprovementYieldChanges`: 村 +1[商業] / 町 +1[商業] / 自治区 +1[商業]
  - `iEnslavementChance`: 25
  - `BlockAlignment`: 邪悪
  - `PrereqCivilization`: リネージ

### Glory - 栄光

- 内部名: `CIVIC_GLORY`
- 分類: 労働制度
- 必要テクノロジー: 工学
- 維持費: 高額
- 説明（ゲーム内ヘルプ）: 他国の都市破壊により人口の1/3の再誕者を獲得
- その他の設定:
  - `iWorkerSpeedModifier`: 50
  - `iLargestCityHappiness`: 1
  - `iWarWearinessModifier`: -25
  - `CommerceModifiers`: 75[文化]
  - `Hurrys`: HURRY_GOLD
  - `SpecialistValids`: 吟遊詩人 / 技師
  - `PrereqCivilization`: パトリアの後継者

## 宗教制度

### Neutrality - 不偏不党

- 内部名: `CIVIC_NO_RELIGION`
- 分類: 宗教制度
- その他の設定:
  - `iAnarchyLength`: 1
  - `bStateReligion`: 1

### Sacrifice the Weak - 弱肉強食

- 内部名: `CIVIC_SACRIFICE_THE_WEAK`
- 分類: 宗教制度
- 必要テクノロジー: 地獄の契約
- その他の設定:
  - `iAnarchyLength`: 1
  - `iExtraHealth`: -4
  - `bStateReligion`: 1
  - `BuildingHappinessChanges`: 薬草師 / 穀倉 / 燻製場
  - `PrereqReligion`: 蒼褪めたヴェール

### Slumbering Coven - 微睡みの集会

- 内部名: `CIVIC_SLUMBERING_COVEN`
- 分類: 宗教制度
- 必要テクノロジー: 宗教法
- 維持費: 高額
- その他の設定:
  - `iAnarchyLength`: 1
  - `iStateReligionGreatPeopleRateModifier`: 50
  - `iFreeSpecialist`: 1
  - `bStateReligion`: 1
  - `CommerceModifiers`: 10[研究]
  - `SpecialistValids`: 神官
  - `PrereqReligion`: 深海の旧支配者

### Social Order - 秩序社会

- 内部名: `CIVIC_SOCIAL_ORDER`
- 分類: 宗教制度
- 必要テクノロジー: 宗教法
- 維持費: 低額
- その他の設定:
  - `iAnarchyLength`: 1
  - `iHappyPerMilitaryUnit`: 1
  - `bStateReligion`: 1
  - `iStateReligionUnitProductionModifier`: 25
  - `iStateReligionFreeExperience`: 2
  - `BuildingHappinessChanges`: 裁判所 iHappinessChange=1 / バシリカ iHappinessChange=1
  - `PrereqReligion`: 秩序の修道会

### Arete - 連峰制

- 内部名: `CIVIC_ARETE`
- 分類: 宗教制度
- 必要テクノロジー: 千仞の尾根
- 維持費: 低額
- その他の設定:
  - `iAnarchyLength`: 1
  - `bStateReligion`: 1
  - `YieldModifiers`: +10[ハンマー]
  - `Hurrys`: HURRY_GOLD
  - `ImprovementYieldChanges`: 鉱山 +1[ハンマー] / 立坑鉱山 +1[ハンマー]
  - `PrereqReligion`: キルモフのルーン

### Enlightement - 啓蒙主義

- 内部名: `CIVIC_ENLIGHTEMENT`
- 分類: 宗教制度
- 必要テクノロジー: 宗教法
- 維持費: 中程度
- その他の設定:
  - `iAnarchyLength`: 1
  - `iGreatPeopleRateModifier`: 50
  - `bStateReligion`: 1
  - `TradeYieldModifiers`: +25[商業]
  - `CommerceModifiers`: 10[研究], 10[文化]
  - `BuildingHappinessChanges`: 裁判所 iHappinessChange=1 / 診療所 iHappinessChange=1
  - `PrereqReligion`: 至光なる天空

### Shadow Court - 影の法廷

- 内部名: `CIVIC_SHADOW_COURT`
- 分類: 宗教制度
- 必要テクノロジー: 税制
- 維持費: 中程度
- その他の設定:
  - `iAnarchyLength`: 1
  - `iDistanceMaintenanceModifier`: -25
  - `iNumCitiesMaintenanceModifier`: -25
  - `iExpInBorderModifier`: 20
  - `bStateReligion`: 1
  - `SpecialistExtraCommerces`: 1[ゴールド], 1[研究]
  - `PrereqReligion`: エススの枢密院

### Guardian of Nature - 大自然の守護者

- 内部名: `CIVIC_GUARDIAN_OF_NATURE`
- 分類: 宗教制度
- 必要テクノロジー: 秘密の抜け道
- 維持費: 高額
- その他の設定:
  - `iAnarchyLength`: 1
  - `iExtraHealth`: 5
  - `iWorkerSpeedModifier`: 25
  - `bStateReligion`: 1
  - `BuildingHappinessChanges`: 鎮守の杜 iHappinessChange=2
  - `FeatureHappinessChanges`: 密林 iHappinessChange=100 / 森林 iHappinessChange=100 / 古代樹林 iHappinessChange=100 / 深い密林 iHappinessChange=100
  - `ImprovementYieldChanges`: 炭焼き小屋 +1[食料] / 製材所 +1[ハンマー]
  - `PrereqReligion`: 緑葉の同胞

### Faith of Winter - 冬の信仰

- 内部名: `CIVIC_FAITH_OF_WINTER`
- 分類: 宗教制度
- 必要テクノロジー: 宗教法
- 説明（ゲーム内ヘルプ）: 冬の儀式の執行に必要となる費用が減額
- その他の設定:
  - `iAnarchyLength`: 1
  - `bStateReligion`: 1
  - `YieldModifiers`: +15[ハンマー]
  - `CommerceModifiers`: 15[ゴールド], 15[研究], -15[文化]
  - `PrereqCivilization`: イリアン

## 所属

### No Membership - 無所属

- 内部名: `CIVIC_NO_MEMBERSHIP`
- 分類: 所属

### Overcouncil - 天上評議会

- 内部名: `CIVIC_OVERCOUNCIL`
- 分類: 所属
- 必要テクノロジー: 名誉
- その他の設定:
  - `ResolutionAngerLevels`: DIPLOVOTE_UNDERCOUNCIL iAngerLevel=5
  - `BlockAlignment`: 邪悪

### Undercouncil - 地下評議会

- 内部名: `CIVIC_UNDERCOUNCIL`
- 分類: 所属
- 必要テクノロジー: 詐欺
- その他の設定:
  - `bHidden`: 1
  - `BlockAlignment`: 善良

## 政治体制

### Despotism - 専制政治

- 内部名: `CIVIC_DESPOTISM`
- 分類: 政治体制
- その他の設定:
  - `iAnarchyLength`: 1
  - `iNumCitiesMaintenanceModifier`: 25
  - `iWarWearinessModifier`: -50
  - `WeLoveTheKing`: 「専制君主感謝祭」

### City States - 都市国家

- 内部名: `CIVIC_CITY_STATES`
- 分類: 政治体制
- 必要テクノロジー: 地図
- 維持費: 低額
- 説明（ゲーム内ヘルプ）: 国境における自国の文化圧力が低下
- その他の設定:
  - `iAnarchyLength`: 1
  - `iDistanceMaintenanceModifier`: -80
  - `iNumCitiesMaintenanceModifier`: -50
  - `iMilitaryProductionModifier`: 30
  - `iWarWearinessModifier`: 25
  - `iPlotClaimModifier`: -50
  - `BuildingHappinessChanges`: 記念碑 iHappinessChange=1 / 防護柵 iHappinessChange=1
  - `WeLoveTheKing`: 「国王感謝祭」

### God King - 現人神制

- 内部名: `CIVIC_GOD_KING`
- 分類: 政治体制
- 必要テクノロジー: 神秘主義
- 維持費: 高額
- その他の設定:
  - `iAnarchyLength`: 1
  - `iDistanceMaintenanceModifier`: 10
  - `CapitalYieldModifiers`: +50[ハンマー]
  - `CapitalCommerceModifiers`: 50[ゴールド]
  - `WeLoveTheKing`: 「現人神感謝祭」

### Aristocracy - 貴族制

- 内部名: `CIVIC_ARISTOCRACY`
- 分類: 政治体制
- 必要テクノロジー: 法律
- 維持費: 低額
- その他の設定:
  - `iAnarchyLength`: 1
  - `iDistanceMaintenanceModifier`: -40
  - `YieldModifiers`: -10[食料]
  - `CapitalYieldModifiers`: +15[商業]
  - `ImprovementYieldChanges`: 町 +1[ハンマー] / 自治区 +1[ハンマー] / 緑葉の大地 +1[ハンマー] / 農場 +2[商業] / 城 +2[商業] / 城塞 +2[商業] / 要塞 +2[商業]
  - `WeLoveTheKing`: 「国王感謝祭」

### Theocracy - 神権政治

- 内部名: `CIVIC_THEOCRACY`
- 分類: 政治体制
- 必要テクノロジー: 宗教法
- 維持費: 中程度
- その他の設定:
  - `iAnarchyLength`: 1
  - `iFreeExperience`: 2
  - `bNoNonStateReligionSpread`: 1
  - `iStateReligionHappiness`: 1
  - `iStateReligionUnitProductionModifier`: 10
  - `iStateReligionFreeExperience`: 3
  - `StateReligionBuildingCommerces`: 2[ゴールド]
  - `SpecialistValids`: 神官
  - `WeLoveTheKing`: 「教主感謝祭」

### Republic - 共和制

- 内部名: `CIVIC_REPUBLIC`
- 分類: 政治体制
- 必要テクノロジー: 税制
- 維持費: 中程度
- その他の設定:
  - `iAnarchyLength`: 1
  - `iLargestCityHappiness`: 3
  - `iCivicPercentAnger`: 500
  - `ImprovementYieldChanges`: 町 +1[食料] / 自治区 +1[食料] / 緑葉の大地 +1[食料]
  - `WeLoveTheKing`: 「執政官感謝祭」

## 文化制度

### Religion - 宗教主義

- 内部名: `CIVIC_RELIGION`
- 分類: 文化制度
- 維持費: 低額
- その他の設定:
  - `iAnarchyLength`: 1
  - `bStateReligion`: 1
  - `iStateReligionHappiness`: 1
  - `iStateReligionBuildingProductionModifier`: 15
  - `CommerceModifiers`: 20[文化]
  - `BuildingHappinessChanges`: キルモフの神殿 iHappinessChange=1 / 緑葉の神殿 iHappinessChange=1 / 秩序の神殿 iHappinessChange=1 / 深海の神殿 iHappinessChange=1 / ヴェールの神殿 iHappinessChange=1 / 至天の神殿 iHappinessChange=1

### Pacifism - 平和主義

- 内部名: `CIVIC_PACIFISM`
- 分類: 文化制度
- 維持費: 低額
- その他の設定:
  - `iAnarchyLength`: 1
  - `iGreatPeopleRateModifier`: 75
  - `iGoldPerMilitaryUnit`: 25
  - `iWarWearinessModifier`: 100
  - `bStateReligion`: 1

### Nationhood - 国民国家

- 内部名: `CIVIC_NATIONHOOD`
- 分類: 文化制度
- 維持費: 低額
- その他の設定:
  - `iAnarchyLength`: 1
  - `iMilitaryProductionModifier`: 15
  - `iWarWearinessModifier`: -25
  - `bStateReligion`: 1
  - `BuildingHappinessChanges`: 練兵場 iHappinessChange=1 / 防壁 iHappinessChange=1

### Consumption - 大量消費

- 内部名: `CIVIC_CONSUMPTION`
- 分類: 文化制度
- 必要テクノロジー: 通貨
- 維持費: 中程度
- その他の設定:
  - `iAnarchyLength`: 1
  - `bStateReligion`: 1
  - `CommerceModifiers`: 25[ゴールド]
  - `SpecialistExtraCommerces`: 2[ゴールド]
  - `BuildingHappinessChanges`: 市場 iHappinessChange=1 / 酒場 iHappinessChange=1 / 劇場 iHappinessChange=1

### Scholarship - 奨学金制

- 内部名: `CIVIC_SCHOLARSHIP`
- 分類: 文化制度
- 必要テクノロジー: 魔術
- 維持費: 高額
- その他の設定:
  - `iAnarchyLength`: 1
  - `bStateReligion`: 1
  - `CommerceModifiers`: 30[研究]
  - `SpecialistExtraCommerces`: 2[研究]
  - `SpecialistValids`: 賢者
  - `BuildingHappinessChanges`: 図書館 iHappinessChange=1 / 閃き iHappinessChange=1

### Liberty - 自由主義

- 内部名: `CIVIC_LIBERTY`
- 分類: 文化制度
- 必要テクノロジー: 重商主義
- 維持費: 中程度
- その他の設定:
  - `iAnarchyLength`: 1
  - `iWarWearinessModifier`: 50
  - `iFreeSpecialist`: 2
  - `bStateReligion`: 1
  - `CommerceModifiers`: 100[文化]
  - `SpecialistExtraCommerces`: 2[文化]
  - `SpecialistValids`: 吟遊詩人

### Crusade - 聖戦

- 内部名: `CIVIC_CRUSADE`
- 分類: 文化制度
- 必要テクノロジー: 狂信
- 維持費: 中程度
- その他の設定:
  - `iAnarchyLength`: 5
  - `iFreeUnitsPopulationPercent`: 50
  - `iWarWearinessModifier`: -75
  - `bStateReligion`: 1
  - `iStateReligionHappiness`: 2
  - `iStateReligionUnitProductionModifier`: 25
  - `iStateReligionFreeExperience`: 2
  - `YieldModifiers`: +10[ハンマー]
  - `ImprovementYieldChanges`: 村 +1[ハンマー] / 町 +1[ハンマー] / 自治区 +1[ハンマー]
  - `bNoDiplomacyWithEnemies`: 1
  - `bPrereqWar`: 1
  - `bNoNonMilitaryBuildingConstruct`: 1
  - `PrereqCivilization`: バンノール

### Burn One's Boats - 背水の陣

- 内部名: `CIVIC_CRUSADE_ECHIGO`
- 分類: 文化制度
- 必要テクノロジー: 軍事戦略
- 維持費: 高額
- その他の設定:
  - `iAnarchyLength`: 1
  - `iGreatPeopleRateModifier`: -10
  - `iDomesticGreatGeneralRateModifier`: 50
  - `iFreeExperience`: 4
  - `iMilitaryProductionModifier`: 25
  - `iFreeUnitsPopulationPercent`: 50
  - `bMilitaryFoodProduction`: 1
  - `iMaxConscript`: 3
  - `iExpInBorderModifier`: 50
  - `iWarWearinessModifier`: -75
  - `bStateReligion`: 1
  - `CommerceModifiers`: -10[ゴールド], -10[研究], -10[文化]
  - `bNoDiplomacyWithEnemies`: 1
  - `bPrereqWar`: 1
  - `bNoNonMilitaryBuildingConstruct`: 1
  - `PrereqCivilization`: エチゴ

### Blood and Sacrifice - 血と生贄

- 内部名: `CIVIC_BLOOD_AND_SACRIFICE`
- 分類: 文化制度
- 必要テクノロジー: 邪悪への道
- その他の設定:
  - `iAnarchyLength`: 1
  - `iGreatPeopleRateModifier`: -50
  - `iWorkerSpeedModifier`: 50
  - `bStateReligion`: 1
  - `Hurrys`: HURRY_POPULATION
  - `BuildingHappinessChanges`: 土着の神殿 iHappinessChange=1
  - `ImprovementUpgradeRateModifiers`: 小屋 iImprovementUpgradeRateModifier=100 / 部落 iImprovementUpgradeRateModifier=100 / 村 iImprovementUpgradeRateModifier=100 / 町 iImprovementUpgradeRateModifier=100 / ユルト iImprovementUpgradeRateModifier=100 / ゴウム iImprovementUpgradeRateModifier=100 / 砦 iImprovementUpgradeRateModifier=100 / 城 iImprovementUpgradeRateModifier=100 / 城塞 iImprovementUpgradeRateModifier=100 / 狩猟場 iImprovementUpgradeRateModifier=100 / 牧草地 iImprovementUpgradeRateModifier=100 / 鉱山 iImprovementUpgradeRateModifier=100 / 工房 iImprovementUpgradeRateModifier=100 / 緑葉の庵 iImprovementUpgradeRateModifier=100 / 緑葉の邑 iImprovementUpgradeRateModifier=100 / 緑葉の里 iImprovementUpgradeRateModifier=100
  - `iEnslavementChance`: 100
  - `BlockAlignment`: 善良
  - `PrereqCivilization`: クアリ

## 経済制度

### Decentralization - 地方分権

- 内部名: `CIVIC_DECENTRALIZATION`
- 分類: 経済制度
- その他の設定:
  - `iAnarchyLength`: 1

### Agrarianism - 農地改革

- 内部名: `CIVIC_AGRARIANISM`
- 分類: 経済制度
- 必要テクノロジー: 暦
- 維持費: 中程度
- その他の設定:
  - `iAnarchyLength`: 1
  - `iExtraHealth`: 1
  - `iMilitaryProductionModifier`: -10
  - `IrrigatedYieldChanges`: 農場 +1[食料]

### Conquest - 軍需優先

- 内部名: `CIVIC_CONQUEST`
- 分類: 経済制度
- 必要テクノロジー: 軍事行動
- 維持費: 中程度
- 説明（ゲーム内ヘルプ）: 都市の征服で得るが2倍 / 新規ユニットに無償の昇進(+1 任意の昇進)
- その他の設定:
  - `iAnarchyLength`: 1
  - `iMilitaryProductionModifier`: 25
  - `bMilitaryFoodProduction`: 1
  - `BuildingHappinessChanges`: 練兵場 iHappinessChange=1 / 弓術射撃場 iHappinessChange=1 / 厩舎 iHappinessChange=1 / 攻城兵器工廠 iHappinessChange=1 / 造船所 iHappinessChange=1
  - `ImprovementYieldChanges`: 城 +1[ハンマー] / 城塞 +1[ハンマー] / 要塞 +1[ハンマー]

### Exclusion of Foreigners - 鎖国令

- 内部名: `CIVIC_MERCANTILISM`
- 分類: 経済制度
- 必要テクノロジー: 重商主義
- 維持費: 中程度
- その他の設定:
  - `iAnarchyLength`: 1
  - `iTradeRoutes`: 2
  - `bNoForeignTrade`: 1
  - `CommerceModifiers`: 40[ゴールド]
  - `BuildingHappinessChanges`: 市場 iHappinessChange=1
  - `ImprovementUpgradeRateModifiers`: 小屋 iImprovementUpgradeRateModifier=100 / 部落 iImprovementUpgradeRateModifier=100 / 村 iImprovementUpgradeRateModifier=100 / 町 iImprovementUpgradeRateModifier=100 / 緑葉の庵 iImprovementUpgradeRateModifier=100 / 緑葉の邑 iImprovementUpgradeRateModifier=100 / 緑葉の里 iImprovementUpgradeRateModifier=100 / ユルト iImprovementUpgradeRateModifier=100 / ゴウム iImprovementUpgradeRateModifier=100
  - `ImprovementYieldChanges`: 小屋 +1[商業] / 部落 +1[商業] / 村 +1[商業] / 町 +1[商業] / 自治区 +1[商業] / 緑葉の庵 +1[商業] / 緑葉の邑 +1[商業] / 緑葉の里 +1[商業] / 緑葉の大地 +1[商業]

### Foreign Trade - 対外貿易

- 内部名: `CIVIC_FOREIGN_TRADE`
- 分類: 経済制度
- 必要テクノロジー: 交易
- 維持費: 低額
- その他の設定:
  - `iAnarchyLength`: 1
  - `iTradeRoutes`: 1
  - `TradeYieldModifiers`: +25[商業]
  - `BuildingHappinessChanges`: 宿屋 iHappinessChange=1
  - `iCoastalTradeRoutes`: 1

### Humanism - 人文主義

- 内部名: `CIVIC_HUMANISM`
- 分類: 経済制度
- 必要テクノロジー: 筆記
- 維持費: 中程度
- 説明（ゲーム内ヘルプ）: 必要条件: 無神論志向
- その他の設定:
  - `iAnarchyLength`: 1
  - `iGreatPeopleRateModifier`: 50
  - `CommerceModifiers`: 10[研究], 10[文化]
  - `BuildingHappinessChanges`: 酒場 iHappinessChange=1 / 図書館 iHappinessChange=1 / 無神論者 iHappinessChange=3 / キルモフの神殿 / 緑葉の神殿 / 至天の神殿 / 秩序の神殿 / 深海の神殿 / ヴェールの神殿
  - `BuildingHealthChanges`: 無神論者 iHealthChange=3
  - `ImprovementYieldChanges`: 農場 +1[食料]
  - `BlockAlignment`: 邪悪

### Undying Court - 不朽の宮廷

- 内部名: `CIVIC_UNDYING_COURT_DROAUM`
- 分類: 経済制度
- 必要テクノロジー: 邪悪への道
- 説明（ゲーム内ヘルプ）: 首都における新規ユニットは魔族として生まれる
- その他の設定:
  - `iAnarchyLength`: 1
  - `CapitalYieldModifiers`: +20[食料], +20[ハンマー], +20[商業]
  - `iEnslavementChance`: 25
  - `BlockAlignment`: 善良
  - `PrereqCivilization`: ドロアウム

### Principle of the old - 古の教

- 内部名: `CIVIC_PRINCIPLE_OF_THE_OLD`
- 分類: 経済制度
- 必要テクノロジー: 四大元素
- 説明（ゲーム内ヘルプ）: 必要条件: 無神論志向
- その他の設定:
  - `iAnarchyLength`: 1
  - `iFreeExperience`: 2
  - `bMilitaryFoodProduction`: 1
  - `YieldModifiers`: -20[食料]
  - `CommerceModifiers`: -30[文化]
  - `PrereqCivilization`: アルタイル

### Lost Lands - 失われし大地

- 内部名: `CIVIC_LOST_LANDS`
- 分類: 経済制度
- 必要テクノロジー: 通貨
- 維持費: 高額
- 説明（ゲーム内ヘルプ）: 文化圏内の草原タイルが湿地に変化する / 文化圏内に活火山が出現する
- その他の設定:
  - `iAnarchyLength`: 1
  - `iTradeRoutes`: 2
  - `bNoForeignTrade`: 1
  - `TradeYieldModifiers`: +50[ハンマー], +75[商業]
  - `BuildingHappinessChanges`: 土着の神殿 iHappinessChange=1
  - `FeatureHappinessChanges`: 沼 iHappinessChange=200 / 活火山 iHappinessChange=400
  - `PrereqCivilization`: マサトル
