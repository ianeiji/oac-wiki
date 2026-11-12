# OAC/地形改善・名所旧跡（0.57、XMLから生成）

- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）
- 生成元: `Terrain/CIV4ImprovementInfos.xml`
- 読み方: 主要な項目は日本語ラベル付きで先頭に、それ以外の既定値でない設定は「その他の設定」にXMLのタグ名のまま列挙する。値の内部名は日本語名に置き換えている。Pythonで実装された効果はXMLにないため含まない（ゲーム内ヘルプの説明文があれば載せている）。

### Land Worked - 陸地スクエア利用中

- 内部名: `IMPROVEMENT_LAND_WORKED`

### Water Worked - 海洋スクエア利用中

- 内部名: `IMPROVEMENT_WATER_WORKED`

### City Ruins - 都市の廃墟

- 内部名: `IMPROVEMENT_CITY_RUINS`

### Tribal Village - 部族集落

- 内部名: `IMPROVEMENT_GOODY_HUT`
- その他の設定:
  - `bGoody`: 1
  - `iTilesPerGoody`: 60
  - `iGoodyRange`: 3
  - `TerrainMakesValids`: 草原 / 平原 / 砂漠 / 湿地 / 凍土
  - `FeatureMakesValids`: 密林 / 森林

### Farm - 農場

- 内部名: `IMPROVEMENT_FARM`
- 対応資源: トウモロコシ iDiscoverRand=10000 iYieldChange=2 / 米 iDiscoverRand=10000 iYieldChange=1 / 小麦 iDiscoverRand=10000 iYieldChange=2 / 亜麻 iDiscoverRand=10000 iYieldChange=1 / iYieldChange=1 iYieldChange=1 / ジャガイモ iDiscoverRand=10000 iYieldChange=1
- テクノロジーによる産出変化: 錬金術 +1[食料] / 衛生設備 +1[商業]
- 説明（ゲーム内ヘルプ）: を産出しない地形には建設できない
- その他の設定:
  - `PrereqNatureYields`: +1[食料]
  - `IrrigatedYieldChange`: +1[食料]
  - `bFreshWaterMakesValid`: 1
  - `bRequiresFlatlands`: 1
  - `bRequiresIrrigation`: 1
  - `bCarriesIrrigation`: 1
  - `bUseLSystem`: 1
  - `iPillageGold`: 5
  - `TerrainMakesValids`: 死滅の大地 / 破滅の原野 / 草原 / 平原

### Fishing Boats - 漁船

- 内部名: `IMPROVEMENT_FISHING_BOATS`
- 対応資源: 貝 iYieldChange=2 / 蟹 iYieldChange=2 / 魚 iYieldChange=3 / 真珠 iYieldChange=2 / 海老 iYieldChange=2 / 翡翠 iYieldChange=2
- その他の設定:
  - `bWater`: 1
  - `bUseLSystem`: 1
  - `iPillageGold`: 5

### Whaling Boats - 捕鯨船

- 内部名: `IMPROVEMENT_WHALING_BOATS`
- 対応資源: 鯨 iYieldChange=1 / iYieldChange=1 / iYieldChange=2 iYieldChange=1 iYieldChange=2
- テクノロジーによる産出変化: 光学 +1[食料], +1[商業] / 天文学 +1[ハンマー], +1[商業]
- その他の設定:
  - `bWater`: 1
  - `iPillageGold`: 5

### Mine - 鉱山

- 内部名: `IMPROVEMENT_MINE`
- 昇格先: 立坑鉱山
- 昇格ターン: 60
- 対応資源: 銅 iDiscoverRand=10000 iYieldChange=1 / 宝石 iDiscoverRand=10000 iYieldChange=5 / 金 iDiscoverRand=10000 iYieldChange=6 / 鉄 iDiscoverRand=10000 iYieldChange=1 / ミスリル iDiscoverRand=10000 iYieldChange=3 / 火薬 iDiscoverRand=10000 iYieldChange=2 / 琥珀 iDiscoverRand=10000 iYieldChange=3 / キノコ iDiscoverRand=10000 iYieldChange=1 / iYieldChange=1 iYieldChange=1 / 塩 iDiscoverRand=10000 iYieldChange=1 / iYieldChange=2 iYieldChange=1 iYieldChange=2
- テクノロジーによる産出変化: 爆薬 +1[ハンマー]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bHillsMakesValid`: 1
  - `iPillageGold`: 10

### Workshop - 工房

- 内部名: `IMPROVEMENT_WORKSHOP`
- 昇格先: ドワーフの工房
- 昇格ターン: 60
- テクノロジーによる産出変化: 建設 +1[ハンマー] / 鉄器 +1[ハンマー] / ミスリルの武具 +1[ハンマー], +1[商業] / 衛生設備 +1[食料]
- 説明（ゲーム内ヘルプ）: を産出しない地形には建設できない
- その他の設定:
  - `PrereqNatureYields`: +1[食料]
  - `YieldChanges`: iYieldChange=1
  - `bFreshWaterMakesValid`: 1
  - `bRequiresFlatlands`: 1
  - `iHealth`: -20
  - `iPillageGold`: 5
  - `TerrainMakesValids`: 死滅の大地 / 破滅の原野 / 草原 / 平原

### Charcoal Burner's Lodge - 炭焼き小屋

- 内部名: `IMPROVEMENT_CHARCOAL_BURNERS_LODGE`
- 対応資源: 薄闇樹 iDiscoverRand=2500
- テクノロジーによる産出変化: 野生の触れ合い +1[食料] / 機械 +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=1
  - `RiverSideYieldChange`: +1[商業]
  - `iHealth`: -40
  - `iPillageGold`: 5
  - `FeatureMakesValids`: 森林 / 古代樹林

### Lumbermill - 製材所

- 内部名: `IMPROVEMENT_LUMBERMILL`
- 対応資源: 薄闇樹 iDiscoverRand=10000 iYieldChange=2
- テクノロジーによる産出変化: 機械 +1[ハンマー], +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=1
  - `RiverSideYieldChange`: +1[商業]
  - `iPillageGold`: 5
  - `FeatureMakesValids`: 森林 / 古代樹林

### Windmill - 風車

- 内部名: `IMPROVEMENT_WINDMILL`
- テクノロジーによる産出変化: 工学 +1[ハンマー] / 機械 +1[食料], +1[ハンマー], +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=1 / iYieldChange=2
  - `bHillsMakesValid`: 1
  - `bCarriesIrrigation`: 1
  - `iPillageGold`: 5

### Watermill - 水車

- 内部名: `IMPROVEMENT_WATERMILL`
- テクノロジーによる産出変化: 工学 +1[ハンマー], +1[商業] / 機械 +1[食料], +1[ハンマー], +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=1 / iYieldChange=2
  - `bRiverSideMakesValid`: 1
  - `bRequiresFlatlands`: 1
  - `bRequiresRiverSide`: 1
  - `iPillageGold`: 5

### Plantation - 大農園

- 内部名: `IMPROVEMENT_PLANTATION`
- 対応資源: バナナ iYieldChange=2 / 染料 iYieldChange=4 / 香木 iYieldChange=5 / 秘薬 iYieldChange=1 / iYieldChange=2 iYieldChange=1 iYieldChange=2 / 砂糖 iYieldChange=1 / iYieldChange=3 iYieldChange=1 iYieldChange=3 / 綿花 iYieldChange=2 / グラガルム iYieldChange=2 / iYieldChange=1 iYieldChange=2 iYieldChange=1 / 剃刀草 iYieldChange=2 / 茶 iYieldChange=3 / コーヒー iYieldChange=3 / レモン iYieldChange=1 / iYieldChange=1 iYieldChange=1 / オレンジ iYieldChange=1 / iYieldChange=1 iYieldChange=1
- テクノロジーによる産出変化: 重商主義 +1[商業]
- その他の設定:
  - `bUseLSystem`: 1
  - `iPillageGold`: 5

### Silk Mill - 養蚕場

- 内部名: `IMPROVEMENT_SILK_MILL`
- 対応資源: 絹 iYieldChange=8
- その他の設定:
  - `bUseLSystem`: 1
  - `iPillageGold`: 5

### Quarry - 採石場

- 内部名: `IMPROVEMENT_QUARRY`
- 対応資源: 大理石 iYieldChange=2 / 影石 iYieldChange=1 / 石材 iYieldChange=1 / パトリアのアーティファクト iYieldChange=3
- テクノロジーによる産出変化: 爆薬 +1[ハンマー]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `iPillageGold`: 5

### Pasture - 牧草地

- 内部名: `IMPROVEMENT_PASTURE`
- 昇格先: 大牧草地
- 昇格ターン: 60
- 対応資源: 牛 iYieldChange=1 / iYieldChange=2 iYieldChange=1 iYieldChange=2 / 馬 iYieldChange=2 / iYieldChange=1 iYieldChange=2 iYieldChange=1 / 豚 iYieldChange=3 / 羊 iYieldChange=2 / iYieldChange=1 iYieldChange=2 iYieldChange=1 / ナイトメア iYieldChange=2 / iYieldChange=1 iYieldChange=2 iYieldChange=1 / 蛙 iYieldChange=2 / iYieldChange=1 iYieldChange=2 iYieldChange=1
- テクノロジーによる産出変化: 動物の極意 +1[食料]
- その他の設定:
  - `iPillageGold`: 5

### Camp - 狩猟場

- 内部名: `IMPROVEMENT_CAMP`
- 昇格先: 大狩猟場
- 昇格ターン: 60
- 対応資源: 鹿 iYieldChange=2 / 毛皮 iYieldChange=3 / 象牙 iYieldChange=1 / iYieldChange=1 iYieldChange=1
- テクノロジーによる産出変化: 野生の触れ合い +1[食料]
- その他の設定:
  - `iPillageGold`: 5

### Winery - ワイン醸造所

- 内部名: `IMPROVEMENT_WINERY`
- 対応資源: ワイン iYieldChange=1 / iYieldChange=2 iYieldChange=1 iYieldChange=2
- テクノロジーによる産出変化: 衛生設備 +1[商業]
- その他の設定:
  - `bUseLSystem`: 1
  - `iPillageGold`: 10

### Cottage - 小屋

- 内部名: `IMPROVEMENT_COTTAGE`
- 昇格先: 部落
- 昇格ターン: 8
- 説明（ゲーム内ヘルプ）: を産出しない地形には建設できない
- その他の設定:
  - `PrereqNatureYields`: +1[食料]
  - `YieldChanges`: iYieldChange=1
  - `bFreshWaterMakesValid`: 1
  - `bUseLSystem`: 1
  - `iPillageGold`: 10
  - `TerrainMakesValids`: 死滅の大地 / 破滅の原野 / 草原 / 平原

### Hamlet - 部落

- 内部名: `IMPROVEMENT_HAMLET`
- 昇格先: 村
- 昇格ターン: 16
- テクノロジーによる産出変化: 数学 +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bUseLSystem`: 1
  - `iPillageGold`: 15
  - `TerrainMakesValids`: 死滅の大地 / 破滅の原野 / 草原 / 平原
  - `ImprovementPillage`: 小屋

### Village - 村

- 内部名: `IMPROVEMENT_VILLAGE`
- 昇格先: 町
- 昇格ターン: 40
- テクノロジーによる産出変化: 数学 +1[商業]
- 説明（ゲーム内ヘルプ）: を産出しない地形には建設できない
- その他の設定:
  - `PrereqNatureYields`: +1[食料]
  - `YieldChanges`: iYieldChange=3
  - `bFreshWaterMakesValid`: 1
  - `bUseLSystem`: 1
  - `iPillageGold`: 20
  - `TerrainMakesValids`: 死滅の大地 / 破滅の原野 / 草原 / 平原
  - `ImprovementPillage`: 部落

### Town - 町

- 内部名: `IMPROVEMENT_TOWN`
- 昇格先: 自治区
- 昇格ターン: 40
- テクノロジーによる産出変化: ギルド +1[商業] / 数学 +1[商業] / 税制 +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=4
  - `bUseLSystem`: 1
  - `iPillageGold`: 25
  - `TerrainMakesValids`: 死滅の大地 / 破滅の原野 / 草原 / 平原
  - `ImprovementPillage`: 村
  - `RouteYieldChanges`: ROUTE_PAVED_ROAD +1[商業]

### Enclave - 自治区

- 内部名: `IMPROVEMENT_ENCLAVE`
- テクノロジーによる産出変化: ギルド +1[商業] / 数学 +1[商業] / 税制 +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=4
  - `bUseLSystem`: 1
  - `iHappiness`: 50
  - `iPillageGold`: 30
  - `TerrainMakesValids`: 死滅の大地 / 破滅の原野 / 草原 / 平原
  - `ImprovementPillage`: 町
  - `RouteYieldChanges`: ROUTE_PAVED_ROAD +1[商業]
  - `PrereqCivilization`: クリオテイテ

### Pirate Cove - 海賊の隠れ家

- 内部名: `IMPROVEMENT_PIRATE_COVE`
- 昇格先: 海賊の港
- 昇格ターン: 25
- 説明（ゲーム内ヘルプ）: 他の隠れ家から2タイル以内には建設できない
- その他の設定:
  - `bWater`: 1
  - `bUseLSystem`: 1
  - `iDefenseModifier`: 10
  - `iPillageGold`: 5
  - `TerrainMakesValids`: 近海
  - `iHealRateChange`: 5
  - `iExclusiveRange`: 2
  - `PrereqCivilization`: ラヌーン

### Pirate Harbor - 海賊の港

- 内部名: `IMPROVEMENT_PIRATE_HARBOR`
- 昇格先: 海賊の港町
- 昇格ターン: 50
- その他の設定:
  - `bWater`: 1
  - `bUseLSystem`: 1
  - `iDefenseModifier`: 20
  - `iPillageGold`: 15
  - `TerrainMakesValids`: 近海
  - `ImprovementPillage`: 海賊の隠れ家
  - `iHealRateChange`: 10
  - `iRange`: 1
  - `iRangeDefenseModifier`: 5
  - `PrereqCivilization`: ラヌーン

### Pirate Port - 海賊の港町

- 内部名: `IMPROVEMENT_PIRATE_PORT`
- その他の設定:
  - `bWater`: 1
  - `bUseLSystem`: 1
  - `iDefenseModifier`: 30
  - `iPillageGold`: 25
  - `TerrainMakesValids`: 近海
  - `ImprovementPillage`: 海賊の港
  - `iHealRateChange`: 20
  - `iRange`: 2
  - `iRangeDefenseModifier`: 10
  - `PrereqCivilization`: ラヌーン

### Fort - 砦

- 内部名: `IMPROVEMENT_FORT`
- 昇格先: 城
- 昇格ターン: 20
- テクノロジーによる産出変化: 石工 +1[商業]
- 説明（ゲーム内ヘルプ）: 他の砦から2タイル以内には建設できない / 領外にて建設可能 / 領内ならば成長に市民配置不要
- その他の設定:
  - `YieldChanges`: iYieldChange=1
  - `bActsAsCity`: 1
  - `bUseLSystem`: 1
  - `iDefenseModifier`: 10
  - `iPillageGold`: 5
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土 / 氷原
  - `iHealRateChange`: 5
  - `iRange`: 1
  - `iRangeDefenseModifier`: 5
  - `iExclusiveRange`: 2

### Castle - 城

- 内部名: `IMPROVEMENT_CASTLE`
- 昇格先: 城塞
- 昇格ターン: 40
- テクノロジーによる産出変化: 石工 +1[ハンマー], +2[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=1
  - `bActsAsCity`: 1
  - `bUseLSystem`: 1
  - `iDefenseModifier`: 25
  - `iPillageGold`: 10
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土 / 氷原
  - `ImprovementPillage`: 砦
  - `iHealRateChange`: 10
  - `iRange`: 2
  - `iRangeDefenseModifier`: 10

### Citadel - 城塞

- 内部名: `IMPROVEMENT_CITADEL`
- 昇格先: 要塞
- 昇格ターン: 60
- テクノロジーによる産出変化: 石工 +2[ハンマー], +3[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=1
  - `bActsAsCity`: 1
  - `bUseLSystem`: 1
  - `iDefenseModifier`: 40
  - `iPillageGold`: 15
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土 / 氷原
  - `ImprovementPillage`: 城
  - `iHealRateChange`: 20
  - `iRange`: 3
  - `iRangeDefenseModifier`: 15
  - `iExtraSeeFrom`: 1

### Hermitage - 緑葉の庵

- 内部名: `IMPROVEMENT_LEAF_COTTAGE`
- 昇格先: 緑葉の邑
- 昇格ターン: 8
- 説明（ゲーム内ヘルプ）: を産出しない地形には建設できない
- その他の設定:
  - `PrereqNatureYields`: +1[食料]
  - `YieldChanges`: iYieldChange=1
  - `RiverSideYieldChange`: +1[商業]
  - `IrrigatedYieldChange`: +1[食料]
  - `bCarriesIrrigation`: 1
  - `bUseLSystem`: 1
  - `iFeatureGrowth`: 64
  - `iPillageGold`: 10
  - `FeatureMakesValids`: 森林 / 古代樹林

### Commune - 緑葉の邑

- 内部名: `IMPROVEMENT_LEAF_HAMLET`
- 昇格先: 緑葉の里
- 昇格ターン: 16
- テクノロジーによる産出変化: 自然との共生 +1[商業] / 叡智への道 +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `RiverSideYieldChange`: +1[商業]
  - `IrrigatedYieldChange`: +1[食料]
  - `bCarriesIrrigation`: 1
  - `bUseLSystem`: 1
  - `iFeatureGrowth`: 64
  - `iPillageGold`: 15
  - `FeatureMakesValids`: 森林 / 古代樹林
  - `ImprovementPillage`: 緑葉の庵

### Colony of Leaves - 緑葉の里

- 内部名: `IMPROVEMENT_LEAF_VILLAGE`
- 昇格先: 緑葉の大地
- 昇格ターン: 40
- テクノロジーによる産出変化: 自然との共生 +1[商業] / 叡智への道 +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `RiverSideYieldChange`: +1[商業]
  - `IrrigatedYieldChange`: +1[食料]
  - `bCarriesIrrigation`: 1
  - `bUseLSystem`: 1
  - `iFeatureGrowth`: 64
  - `iPillageGold`: 20
  - `FeatureMakesValids`: 森林 / 古代樹林
  - `ImprovementPillage`: 緑葉の邑
  - `ReligionYieldChanges`: 緑葉の同胞 +1[商業]

### Land of Leaves - 緑葉の大地

- 内部名: `IMPROVEMENT_LEAF_TOWN`
- テクノロジーによる産出変化: 自然との共生 +1[商業] / 野生の触れ合い +1[商業] / 医薬 +1[食料] / 叡智への道 +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `RiverSideYieldChange`: +1[商業]
  - `IrrigatedYieldChange`: +1[食料]
  - `bCarriesIrrigation`: 1
  - `bUseLSystem`: 1
  - `iFeatureGrowth`: 64
  - `iPillageGold`: 25
  - `FeatureMakesValids`: 森林 / 古代樹林
  - `ImprovementPillage`: 緑葉の里
  - `RouteYieldChanges`: ROUTE_PAVED_ROAD +1[商業]
  - `ReligionYieldChanges`: 緑葉の同胞 +2[商業]

### Air Node - 大気のノード

- 内部名: `IMPROVEMENT_MANA_AIR`
- 対応資源: マナ / 大気のマナ iYieldChange=1 / iYieldChange=2 iYieldChange=1 iYieldChange=2
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 大気のマナ

### Body Node - 肉体のノード

- 内部名: `IMPROVEMENT_MANA_BODY`
- 対応資源: マナ / 肉体のマナ iYieldChange=1 / iYieldChange=2 iYieldChange=1 iYieldChange=2
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 肉体のマナ

### Chaos Node - 混沌のノード

- 内部名: `IMPROVEMENT_MANA_CHAOS`
- 対応資源: マナ / 混沌のマナ iYieldChange=1 / iYieldChange=2 iYieldChange=1 iYieldChange=2
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 混沌のマナ

### Death Node - 死のノード

- 内部名: `IMPROVEMENT_MANA_DEATH`
- 対応資源: マナ / 死のマナ iYieldChange=1 / iYieldChange=1 iYieldChange=1
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 死のマナ

### Dimensional Node - 次元のノード

- 内部名: `IMPROVEMENT_MANA_DIMENSIONAL`
- 対応資源: マナ / 次元のマナ iYieldChange=1 / iYieldChange=5 iYieldChange=1 iYieldChange=5
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 次元のマナ

### Earth Node - 大地のノード

- 内部名: `IMPROVEMENT_MANA_EARTH`
- 対応資源: マナ / 大地のマナ iYieldChange=2
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 大地のマナ

### Enchantment Node - 呪付のノード

- 内部名: `IMPROVEMENT_MANA_ENCHANTMENT`
- 対応資源: マナ / 呪付のマナ iYieldChange=2
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 呪付のマナ

### Entropy Node - 不可逆のノード

- 内部名: `IMPROVEMENT_MANA_ENTROPY`
- 対応資源: マナ / 不可逆のマナ iYieldChange=1 / iYieldChange=2 iYieldChange=1 iYieldChange=2
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 不可逆のマナ

### Fire Node - 炎のノード

- 内部名: `IMPROVEMENT_MANA_FIRE`
- 対応資源: マナ / 炎のマナ iYieldChange=1 / iYieldChange=2 iYieldChange=1 iYieldChange=2
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 炎のマナ

### Law Node - 法のノード

- 内部名: `IMPROVEMENT_MANA_LAW`
- 対応資源: マナ / 法のマナ iYieldChange=4
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 法のマナ

### Life Node - 生命のノード

- 内部名: `IMPROVEMENT_MANA_LIFE`
- 対応資源: マナ / 生命のマナ iYieldChange=2
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 生命のマナ

### Metamagic Node - 超魔術のノード

- 内部名: `IMPROVEMENT_MANA_METAMAGIC`
- 対応資源: マナ / 超魔術のマナ iYieldChange=4
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 超魔術のマナ

### Mind Node - 精神のノード

- 内部名: `IMPROVEMENT_MANA_MIND`
- 対応資源: マナ / 精神のマナ iYieldChange=1 / iYieldChange=2 iYieldChange=1 iYieldChange=2
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 精神のマナ

### Nature Node - 自然のノード

- 内部名: `IMPROVEMENT_MANA_NATURE`
- 対応資源: マナ / 自然のマナ iYieldChange=2
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 自然のマナ

### Shadow Node - 影のノード

- 内部名: `IMPROVEMENT_MANA_SHADOW`
- 対応資源: マナ / 影のマナ iYieldChange=1 / iYieldChange=2 iYieldChange=1 iYieldChange=2
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 影のマナ

### Spirit Node - 魂のノード

- 内部名: `IMPROVEMENT_MANA_SPIRIT`
- 対応資源: マナ / 魂のマナ iYieldChange=4
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 魂のマナ

### Sun Node - 太陽のノード

- 内部名: `IMPROVEMENT_MANA_SUN`
- 対応資源: マナ / 太陽のマナ iYieldChange=1 / iYieldChange=1 iYieldChange=1
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 太陽のマナ

### Water Node - 水のノード

- 内部名: `IMPROVEMENT_MANA_WATER`
- 対応資源: マナ / 水のマナ iYieldChange=1 / iYieldChange=2 iYieldChange=1 iYieldChange=2
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 水のマナ

### Mushrooms - キノコ

- 内部名: `IMPROVEMENT_MUSHROOMS`
- テクノロジーによる産出変化: 野生の触れ合い +1[食料]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `TerrainMakesValids`: 草原 / 平原 / 湿地 / 凍土

### Penguins - ペンギン

- 内部名: `IMPROVEMENT_PENGUINS`
- その他の設定:
  - `iHappiness`: 100

### Graveyard - 墓地

- 内部名: `IMPROVEMENT_GRAVEYARD`
- その他の設定:
  - `bPermanent`: 1
  - `TerrainMakesValids`: 死滅の大地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土 / 氷原
  - `iAppearanceProbability`: 25

### Barrow - 土塚

- 内部名: `IMPROVEMENT_BARROW`
- その他の設定:
  - `bPermanent`: 1
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土 / 氷原
  - `iAppearanceProbability`: 75
  - `PythonExplore`: exploreLair
  - `SpawnUnitType`: 骸骨
  - `InitialSpawnUnitType`: 骸骨
  - `SpawnBarbarianType`: BARBARIAN_UNDEAD

### Dungeon - 地下迷宮

- 内部名: `IMPROVEMENT_DUNGEON`
- その他の設定:
  - `bPermanent`: 1
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土 / 氷原
  - `iAppearanceProbability`: 75
  - `PythonExplore`: exploreLair

### Goblin Fort - ゴブリン砦

- 内部名: `IMPROVEMENT_GOBLIN_FORT`
- その他の設定:
  - `bActsAsCity`: 1
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `iDefenseModifier`: 10
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 死滅の大地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 湿地 / 凍土
  - `iAppearanceProbability`: 50
  - `iHealRateChange`: 10
  - `iRange`: 1
  - `iRangeDefenseModifier`: 5
  - `PythonExplore`: exploreLair
  - `SpawnUnitType`: ゴブリン
  - `InitialSpawnUnitType`: 弓兵
  - `SpawnBarbarianType`: BARBARIAN_ORC
  - `SpawnUnitFreePromotions`: 蠍一族

### Ruins - 廃墟

- 内部名: `IMPROVEMENT_RUINS`
- その他の設定:
  - `bPermanent`: 1
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 死滅の大地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 湿地
  - `FeatureMakesValids`: 密林
  - `iAppearanceProbability`: 75
  - `PythonExplore`: exploreLair
  - `SpawnUnitType`: リザードマン
  - `SpawnBarbarianType`: BARBARIAN_ORC
  - `SpawnUnitFreePromotions`: 武器の腐食

### Ship Wreck - 難破船

- 内部名: `IMPROVEMENT_SHIP_WRECK`
- その他の設定:
  - `bWater`: 1
  - `bPermanent`: 1
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 近海
  - `iAppearanceProbability`: 100
  - `PythonExplore`: exploreLair

### Bear Den - 熊の巣穴

- 内部名: `IMPROVEMENT_BEAR_DEN`
- その他の設定:
  - `bRequiresFlatlands`: 1
  - `bPermanent`: 1
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 凍土
  - `PythonExplore`: exploreDen
  - `SpawnUnitType`: 熊
  - `SpawnBarbarianType`: BARBARIAN_ANIMAL

### Lion Den - ライオンのねぐら

- 内部名: `IMPROVEMENT_LION_DEN`
- その他の設定:
  - `bRequiresFlatlands`: 1
  - `bPermanent`: 1
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 平原
  - `PythonExplore`: exploreDen
  - `SpawnUnitType`: ライオン
  - `SpawnBarbarianType`: BARBARIAN_ANIMAL

### Hellfire - 地獄の業火

- 内部名: `IMPROVEMENT_HELLFIRE`
- その他の設定:
  - `bRequiresFlatlands`: 1
  - `iPillageGold`: 10
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土 / 氷原
  - `SpawnUnitType`: 勇士
  - `SpawnBarbarianType`: BARBARIAN_DEMONS

### Smoke - 燻る煙

- 内部名: `IMPROVEMENT_SMOKE`
- その他の設定:
  - `bPermanent`: 1
  - `iDefenseModifier`: -10
  - `bOutsideBorders`: 1
  - `FeatureMakesValids`: 密林 / 森林 / 灌木林

### Snake Pillar - 蛇の柱

- 内部名: `IMPROVEMENT_SNAKE_PILLAR`
- テクノロジーによる産出変化: 邪悪への道 +2[食料], +1[ハンマー] / 地獄の契約 +2[食料], +1[ハンマー], +1[商業]
- その他の設定:
  - `bPermanent`: 1
  - `bOutsideBorders`: 1

### Ancient Tower - 古代の塔

- 内部名: `IMPROVEMENT_TOWER`
- その他の設定:
  - `bHillsMakesValid`: 1
  - `iDefenseModifier`: 50
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土
  - `iAppearanceProbability`: 60
  - `iVisibilityChange`: 2
  - `iExtraSeeFrom`: 1

### Maenalus - マエナルス島

- 内部名: `IMPROVEMENT_AIFON_ISLE`
- 対応資源: 水のマナ
- その他の設定:
  - `YieldChanges`: iYieldChange=3 / iYieldChange=4
  - `bWater`: 1
  - `bPermanent`: 1
  - `TerrainMakesValids`: 外洋
  - `bUnique`: 1
  - `BonusConvert`: 水のマナ
  - `PythonExplore`: exploreLairEpic

### Bradeline's Well - ブラデリンの井戸

- 内部名: `IMPROVEMENT_BRADELINES_WELL`
- 対応資源: 不可逆のマナ
- テクノロジーによる産出変化: 屍霊術 +3[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bRequiresFlatlands`: 1
  - `bPermanent`: 1
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土 / 氷原
  - `bUnique`: 1
  - `BonusConvert`: 不可逆のマナ
  - `PythonExplore`: exploreLairEpic

### Broken Sepulcher - 暴かれた玄室

- 内部名: `IMPROVEMENT_BROKEN_SEPULCHER`
- 対応資源: 死のマナ
- テクノロジーによる産出変化: 屍霊術 +1[ハンマー], +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=1 / iYieldChange=1
  - `bPermanent`: 1
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土 / 氷原
  - `bUnique`: 1
  - `BonusConvert`: 死のマナ
  - `PythonOnMove`: onMoveBrokenSepulcher
  - `PythonExplore`: exploreLairEpic

### Dragon Bones - 竜骨の化石

- 内部名: `IMPROVEMENT_DRAGON_BONES`
- 対応資源: 象牙
- テクノロジーによる産出変化: 交易 +2[商業] / 建設 +2[商業] / 狩猟 +1[ハンマー], +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bPermanent`: 1
  - `iHappiness`: 100
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土
  - `bUnique`: 1
  - `BonusConvert`: 象牙

### Guardian of Pristin Pass - プリスティン峠の道祖神

- 内部名: `IMPROVEMENT_GUARDIAN`
- テクノロジーによる産出変化: 魔術 +3[ハンマー]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bPermanent`: 1
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土
  - `bRequiresPeak`: 1
  - `bUnique`: 1
  - `PythonAtRange`: atRangeGuardian

### Letum Frigus - 荒涼たる死

- 内部名: `IMPROVEMENT_LETUM_FRIGUS`
- 対応資源: 氷のマナ
- テクノロジーによる産出変化: 魔術 +2[ハンマー] / 宗教法 +3[商業] / 神学 +3[ハンマー]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bRequiresHills`: 1
  - `bPermanent`: 1
  - `TerrainMakesValids`: 凍土 / 氷原
  - `bUnique`: 1
  - `BonusConvert`: 氷のマナ
  - `PythonOnMove`: onMoveLetumFrigus

### Maelstrom - 大渦潮

- 内部名: `IMPROVEMENT_MAELSTROM`
- その他の設定:
  - `bWater`: 1
  - `bPermanent`: 1
  - `TerrainMakesValids`: 外洋
  - `bUnique`: 1
  - `PythonOnMove`: onMoveMaelstrom

### Mirror of Heaven - 天界の鏡

- 内部名: `IMPROVEMENT_MIRROR_OF_HEAVEN`
- 対応資源: 太陽のマナ
- テクノロジーによる産出変化: 予言術 +2[商業] / 神秘主義 +1[ハンマー] / 宗教法 +1[ハンマー], +2[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bNoFreshWater`: 1
  - `bPermanent`: 1
  - `iDefenseModifier`: 25
  - `iHappiness`: 100
  - `TerrainMakesValids`: 砂漠
  - `bUnique`: 1
  - `iVisibilityChange`: 6
  - `iExtraSeeFrom`: 5
  - `BonusConvert`: 太陽のマナ
  - `PythonOnMove`: onMoveMirrorOfHeaven

### Odio's Prison - オディオの牢獄

- 内部名: `IMPROVEMENT_ODIOS_PRISON`
- 対応資源: 肉体のマナ
- テクノロジーによる産出変化: 変成術 +2[ハンマー]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bRequiresFlatlands`: 1
  - `bPermanent`: 1
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土
  - `bUnique`: 1
  - `iRange`: 3
  - `iRangeDefenseModifier`: 25
  - `BonusConvert`: 肉体のマナ

### Pool of Tears - 涙の池

- 内部名: `IMPROVEMENT_POOL_OF_TEARS`
- 対応資源: 水のマナ
- テクノロジーによる産出変化: 四大元素 +2[食料]
- 説明（ゲーム内ヘルプ）: 病気を回復 / 疫病を回復 / 毒を回復 / 衰弱を回復
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bRequiresFlatlands`: 1
  - `bAddsFreshWater`: 1
  - `bPermanent`: 1
  - `iHealth`: 300
  - `iHappiness`: 100
  - `TerrainMakesValids`: 草原 / 平原 / 湿地
  - `bUnique`: 1
  - `iHealRateChange`: 50
  - `BonusConvert`: 水のマナ
  - `PythonOnMove`: onMovePoolOfTears

### Pyre of the Seraphic - 熾天使の火葬

- 内部名: `IMPROVEMENT_PYRE_OF_THE_SERAPHIC`
- 対応資源: 炎のマナ
- テクノロジーによる産出変化: 四大元素 +2[ハンマー]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bRequiresFlatlands`: 1
  - `bPermanent`: 1
  - `TerrainMakesValids`: 破滅の原野 / 平原 / 湿地 / 地獄の浅瀬
  - `bUnique`: 1
  - `BonusConvert`: 炎のマナ
  - `PythonOnMove`: onMovePyreOfTheSeraphic
  - `PythonExplore`: exploreLairEpic

### Remnants of Patria - パトリアの名残

- 内部名: `IMPROVEMENT_REMNANTS_OF_PATRIA`
- 対応資源: パトリアのアーティファクト iYieldChange=1 / iYieldChange=2 iYieldChange=1 iYieldChange=2
- テクノロジーによる産出変化: 教育 +2[ハンマー] / 封建制 +2[ハンマー] / 神秘主義 +1[ハンマー]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bPermanent`: 1
  - `iHappiness`: 300
  - `TerrainMakesValids`: 草原 / 平原 / 砂漠 / 湿地 / 凍土
  - `bUnique`: 1
  - `BonusConvert`: パトリアのアーティファクト

### Ring of Carcer - カルセルの輪光

- 内部名: `IMPROVEMENT_RING_OF_CARCER`
- その他の設定:
  - `bPermanent`: 1
  - `TerrainMakesValids`: 氷原
  - `bUnique`: 1

### Seven Pines - 七本松

- 内部名: `IMPROVEMENT_SEVEN_PINES`
- テクノロジーによる産出変化: 自然との共生 +4[ハンマー] / 聖職 +1[ハンマー]
- 説明（ゲーム内ヘルプ）: 他の全ての文明と和平する / 七本松に駐留するユニットのみ実行可能 / ゲームを通じて一度だけ実行可能
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bRequiresFlatlands`: 1
  - `bPermanent`: 1
  - `FeatureMakesValids`: 森林 / 古代樹林
  - `bUnique`: 1

### Standing Stones - そびえ立つ巨石

- 内部名: `IMPROVEMENT_STANDING_STONES`
- 対応資源: 大地のマナ
- テクノロジーによる産出変化: 四大元素 +2[ハンマー]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bRequiresFlatlands`: 1
  - `bPermanent`: 1
  - `iHappiness`: 100
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土 / 氷原
  - `bUnique`: 1
  - `BonusConvert`: 大地のマナ

### Tomb of Sucellus - スケルスの墓所

- 内部名: `IMPROVEMENT_TOMB_OF_SUCELLUS`
- 対応資源: 生命のマナ
- テクノロジーによる産出変化: 錬金術 +2[ハンマー] / 衛生設備 +2[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bPermanent`: 1
  - `iHappiness`: 100
  - `TerrainMakesValids`: 草原 / 平原
  - `FeatureMakesValids`: 密林 / 森林
  - `bUnique`: 1
  - `iHealRateChange`: 25
  - `BonusConvert`: 生命のマナ

### Yggdrasil - ユグドラシルの樹

- 内部名: `IMPROVEMENT_YGGDRASIL`
- 対応資源: 世界樹の果実
- テクノロジーによる産出変化: 深き森への道 +2[食料] / 自然との共生 +2[食料] / 暦 +1[食料]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bPermanent`: 1
  - `iHappiness`: 100
  - `FeatureMakesValids`: 森林 / 古代樹林
  - `bUnique`: 1
  - `BonusConvert`: 世界樹の果実

### Cage - 檻

- 内部名: `IMPROVEMENT_CAGE`
- その他の設定:
  - `bPermanent`: 1

### Jungle Altar - 密林の供犠台

- 内部名: `IMPROVEMENT_JUNGLE_ALTAR`
- その他の設定:
  - `bUseLSystem`: 1
  - `PythonAtRange`: atRangeJungleAltar
  - `PythonOnMove`: onMoveJungleAltar

### Ancient Skeleton - 古代の化石

- 内部名: `IMPROVEMENT_MONSTER_SKELETON`
- その他の設定:
  - `bPermanent`: 1

### Necrototem - 屍霊のトーテム

- 内部名: `IMPROVEMENT_NECROTOTEM`
- その他の設定:
  - `bUseLSystem`: 1
  - `PythonAtRange`: atRangeNecrototem

### Portal - 転移門

- 内部名: `IMPROVEMENT_PORTAL`
- その他の設定:
  - `bPermanent`: 1
  - `PythonOnMove`: onMovePortal

### Warning Post - 警標

- 内部名: `IMPROVEMENT_WARNING_POST`
- その他の設定:
  - `bUseLSystem`: 1
  - `PythonOnMove`: onMoveWarningPost

### Yurt - ユルト

- 内部名: `IMPROVEMENT_YURT`
- 昇格先: ゴウム
- 昇格ターン: 10
- 対応資源: 牛 iDiscoverRand=10000 / 馬 iDiscoverRand=10000 / 豚 iDiscoverRand=10000 / 羊 iDiscoverRand=10000 / 鹿 iDiscoverRand=10000 / 毛皮 iDiscoverRand=10000
- テクノロジーによる産出変化: 騎乗 +1[商業] / 交易 +1[商業] / 重商主義 +1[食料] / 軍馬 +1[ハンマー], +1[商業]
- 説明（ゲーム内ヘルプ）: を産出しない地形には建設できない
- その他の設定:
  - `PrereqNatureYields`: +1[ハンマー]
  - `YieldChanges`: iYieldChange=1 / iYieldChange=1
  - `iPillageGold`: 5
  - `TerrainMakesValids`: 死滅の大地 / 破滅の原野 / 灼熱の砂地 / 草原 / 平原 / 砂漠

### Goum - ゴウム

- 内部名: `IMPROVEMENT_GOUM`
- 昇格先: アデュアル
- 昇格ターン: 30
- 対応資源: 牛 iDiscoverRand=5000 / 馬 iDiscoverRand=5000 / 豚 iDiscoverRand=5000 / 羊 iDiscoverRand=5000 / 鹿 iDiscoverRand=5000 / 毛皮 iDiscoverRand=5000
- テクノロジーによる産出変化: 騎乗 +1[商業] / 交易 +1[商業] / 重商主義 +1[食料], +1[ハンマー] / 軍馬 +1[ハンマー], +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=1 / iYieldChange=2
  - `iPillageGold`: 10
  - `TerrainMakesValids`: 死滅の大地 / 破滅の原野 / 灼熱の砂地 / 草原 / 平原 / 砂漠
  - `ImprovementPillage`: ユルト

### Aduar - アデュアル

- 内部名: `IMPROVEMENT_ADUAR`
- 対応資源: 牛 iDiscoverRand=5000 / 馬 iDiscoverRand=5000 / 豚 iDiscoverRand=5000 / 羊 iDiscoverRand=5000 / 鹿 iDiscoverRand=5000 / 毛皮 iDiscoverRand=5000
- テクノロジーによる産出変化: 騎乗 +1[商業] / 交易 +1[商業] / 重商主義 +1[食料], +1[ハンマー] / 軍馬 +1[ハンマー], +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=1 / iYieldChange=2
  - `iDefenseModifier`: 25
  - `iPillageGold`: 20
  - `TerrainMakesValids`: 死滅の大地 / 破滅の原野 / 灼熱の砂地 / 草原 / 平原 / 砂漠
  - `ImprovementPillage`: ゴウム
  - `iHealRateChange`: 10
  - `PrereqCivilization`: マラキム

### Shaft Mine - 立坑鉱山

- 内部名: `IMPROVEMENT_SHAFT_MINE`
- 対応資源: 銅 iDiscoverRand=5000 iYieldChange=1 / 宝石 iDiscoverRand=5000 iYieldChange=5 / 金 iDiscoverRand=5000 iYieldChange=6 / 鉄 iDiscoverRand=5000 iYieldChange=1 / ミスリル iDiscoverRand=5000 iYieldChange=3 / 火薬 iDiscoverRand=5000 iYieldChange=2 / 琥珀 iDiscoverRand=5000 iYieldChange=3 / キノコ iDiscoverRand=5000 iYieldChange=1 / iYieldChange=1 iYieldChange=1 / 塩 iDiscoverRand=5000 iYieldChange=1 / iYieldChange=2 iYieldChange=1 iYieldChange=2
- テクノロジーによる産出変化: 爆薬 +1[ハンマー]
- その他の設定:
  - `YieldChanges`: iYieldChange=2 / iYieldChange=2
  - `bHillsMakesValid`: 1
  - `iPillageGold`: 25
  - `ImprovementPillage`: 鉱山

### Greater Pasture - 大牧草地

- 内部名: `IMPROVEMENT_GREATER_PASTURE`
- 対応資源: 牛 iYieldChange=1 / iYieldChange=2 iYieldChange=1 iYieldChange=2 / 馬 iYieldChange=2 / iYieldChange=1 iYieldChange=2 iYieldChange=1 / 豚 iYieldChange=3 / 羊 iYieldChange=2 / iYieldChange=1 iYieldChange=2 iYieldChange=1 / ナイトメア iYieldChange=2 / iYieldChange=1 iYieldChange=2 iYieldChange=1 / 蛙 iYieldChange=2 / iYieldChange=1 iYieldChange=2 iYieldChange=1
- テクノロジーによる産出変化: 動物の極意 +1[食料]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `iPillageGold`: 15
  - `ImprovementPillage`: 牧草地

### Hunting Grounds - 大狩猟場

- 内部名: `IMPROVEMENT_HUNTING_GROUNDS`
- 対応資源: 鹿 iYieldChange=2 / 毛皮 iYieldChange=3 / 象牙 iYieldChange=1 / iYieldChange=1 iYieldChange=1
- テクノロジーによる産出変化: 野生の触れ合い +1[食料]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `iPillageGold`: 15
  - `ImprovementPillage`: 狩猟場

### Stronghold - 要塞

- 内部名: `IMPROVEMENT_STRONGHOLD`
- テクノロジーによる産出変化: 石工 +3[ハンマー], +4[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=1
  - `bActsAsCity`: 1
  - `bUseLSystem`: 1
  - `iDefenseModifier`: 50
  - `iPillageGold`: 25
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土 / 氷原
  - `ImprovementPillage`: 城塞
  - `iHealRateChange`: 25
  - `iRange`: 3
  - `iRangeDefenseModifier`: 20
  - `iExtraSeeFrom`: 1
  - `PrereqCivilization`: バンノール

### Dwarven Workshop - ドワーフの工房

- 内部名: `IMPROVEMENT_DWARVEN_WORKSHOP`
- 対応資源: 銅 iDiscoverRand=5000 / 鉄 iDiscoverRand=5000 / ミスリル iDiscoverRand=5000 / 火薬 iDiscoverRand=5000
- テクノロジーによる産出変化: 建設 +1[ハンマー] / 鉄器 +1[ハンマー] / ミスリルの武具 +1[ハンマー], +1[商業] / 衛生設備 +1[食料]
- その他の設定:
  - `PrereqNatureYields`: +1[食料]
  - `YieldChanges`: iYieldChange=2
  - `bFreshWaterMakesValid`: 1
  - `bRequiresFlatlands`: 1
  - `iPillageGold`: 20
  - `TerrainMakesValids`: 死滅の大地 / 破滅の原野 / 草原 / 平原 / 凍土 / 氷原
  - `ImprovementPillage`: 工房
  - `PrereqCivilization`: ルシュイアープ

### Plant Sacred Tree - 巨大樹の苗

- 内部名: `IMPROVEMENT_PLANT_SACRED_TREE`
- 昇格先: 巨大樹
- 昇格ターン: 60
- 対応資源: 世界樹の果実
- その他の設定:
  - `bPermanent`: 1
  - `iHealth`: 200
  - `FeatureMakesValids`: 森林 / 古代樹林

### Sacred Tree - 巨大樹

- 内部名: `IMPROVEMENT_SACRED_TREE`
- 対応資源: 世界樹の果実
- テクノロジーによる産出変化: 自然との共生 +1[食料]
- その他の設定:
  - `bPermanent`: 1
  - `iHealth`: 200
  - `iHappiness`: 100
  - `BonusConvert`: 世界樹の果実

### Supply-Base - 兵站基地

- 内部名: `IMPROVEMENT_SUPPLY_BASE`
- 説明（ゲーム内ヘルプ）: 他の兵站基地から2タイル以内には建設できない / 領外にて建設可能
- その他の設定:
  - `bActsAsCity`: 1
  - `iDefenseModifier`: 10
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 灼熱の砂地 / 死滅の大地 / 破滅の原野 / 地獄の浅瀬 / 砂漠 / 草原 / 平原 / 湿地 / 氷原 / 凍土
  - `iRange`: 1
  - `iRangeDefenseModifier`: 5
  - `iExclusiveRange`: 2

### Snowman - 雪だるま

- 内部名: `IMPROVEMENT_SNOWMAN`
- 昇格先: 大きな雪だるま
- 昇格ターン: 25
- テクノロジーによる産出変化: 衛生設備 +1[商業] / 医薬 +1[商業]
- 説明（ゲーム内ヘルプ）: 破壊されるまで、フロストリングの蛮族ユニットを生み出し続ける / 他の雪だるまから2タイル以内には建設できない
- その他の設定:
  - `bUseLSystem`: 1
  - `iPillageGold`: 5
  - `TerrainMakesValids`: 凍土 / 氷原
  - `iExclusiveRange`: 2
  - `PrereqCivilization`: ニバル

### Giant Snowman - 大きな雪だるま

- 内部名: `IMPROVEMENT_GIANT_SNOWMAN`
- 昇格先: 巨大な雪だるま
- 昇格ターン: 50
- テクノロジーによる産出変化: 衛生設備 +1[商業] / 医薬 +1[商業]
- 説明（ゲーム内ヘルプ）: 破壊されるまで、フロストリングの蛮族ユニットを生み出し続ける / 生み出されるユニットに+2: 経験ポイント
- その他の設定:
  - `bUseLSystem`: 1
  - `iHealth`: 200
  - `iHappiness`: 100
  - `iPillageGold`: 10
  - `TerrainMakesValids`: 凍土 / 氷原
  - `ImprovementPillage`: 雪だるま
  - `PrereqCivilization`: ニバル

### Greater Snowman - 巨大な雪だるま

- 内部名: `IMPROVEMENT_GREATER_SNOWMAN`
- テクノロジーによる産出変化: 衛生設備 +1[商業] / 医薬 +1[商業]
- 説明（ゲーム内ヘルプ）: 破壊されるまで、フロストリングの蛮族ユニットを生み出し続ける / 生み出されるユニットに+5: 経験ポイント
- その他の設定:
  - `bUseLSystem`: 1
  - `iHealth`: 400
  - `iHappiness`: 200
  - `iPillageGold`: 15
  - `TerrainMakesValids`: 凍土 / 氷原
  - `ImprovementPillage`: 大きな雪だるま
  - `PrereqCivilization`: ニバル

### Refinery - 精製装置

- 内部名: `IMPROVEMENT_REFINERY`
- 対応資源: マナ / 精製されたマナ iYieldChange=1 / iYieldChange=2 iYieldChange=1 iYieldChange=2
- テクノロジーによる産出変化: 秘術の伝承知識 +1[ハンマー], +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=1
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `BonusConvert`: 精製されたマナ

### Hoof of Cernunnos - ケルヌンノスの蹄

- 内部名: `IMPROVEMENT_HOOF_OF_CERNUNNOS`
- 対応資源: 自然のマナ
- テクノロジーによる産出変化: 衛生設備 +3[食料]
- 説明（ゲーム内ヘルプ）: 病気を回復 / 疫病を回復 / 毒を回復 / 衰弱を回復
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bRequiresFlatlands`: 1
  - `bPermanent`: 1
  - `iHappiness`: 100
  - `TerrainMakesValids`: 草原 / 平原
  - `bUnique`: 1
  - `iHealRateChange`: 50
  - `BonusConvert`: 自然のマナ
  - `PythonOnMove`: onMoveNaturalStone

### Sacrament of Arawn - アラウンの秘蹟

- 内部名: `IMPROVEMENT_SACRAMENT_OF_ARAWN`
- 対応資源: 魂のマナ
- テクノロジーによる産出変化: 予言術 +2[食料]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bRequiresFlatlands`: 1
  - `bPermanent`: 1
  - `iHappiness`: 100
  - `TerrainMakesValids`: 草原 / 平原
  - `bUnique`: 1
  - `BonusConvert`: 魂のマナ

### Shrine of Fabrication - 虚偽の祭祀場

- 内部名: `IMPROVEMENT_SHRINE_OF_FABRICATION`
- 対応資源: 影のマナ
- テクノロジーによる産出変化: 詐欺 +3[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bRequiresFlatlands`: 1
  - `bPermanent`: 1
  - `TerrainMakesValids`: 草原 / 平原
  - `bUnique`: 1
  - `BonusConvert`: 影のマナ

### Marker Gold - 黄金の巨石

- 内部名: `IMPROVEMENT_MARKER_GOLD`
- 対応資源: 金
- テクノロジーによる産出変化: 採鉱 +1[商業] / 交易 +2[商業] / 母なる大地への道 +2[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=4
  - `bPermanent`: 1
  - `iHappiness`: 50
  - `TerrainMakesValids`: 草原 / 平原
  - `bUnique`: 1
  - `BonusConvert`: 金

### Gate to the Underdark - 闇世界への門

- 内部名: `IMPROVEMENT_GATE_UNDERDARK`
- 対応資源: 次元のマナ
- テクノロジーによる産出変化: 錬金術 +4[商業] / 採鉱 +2[ハンマー] / 交易 +1[食料], +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bPermanent`: 1
  - `iHappiness`: 100
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 草原 / 平原
  - `bUnique`: 1
  - `BonusConvert`: 次元のマナ

### Mount Kalshekk - カルシェック山

- 内部名: `IMPROVEMENT_MOUNT_KALSHEKK`
- 対応資源: 大地のマナ
- テクノロジーによる産出変化: 狂信 +1[ハンマー], +1[商業] / 採鉱 +1[ハンマー], +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bPermanent`: 1
  - `iHappiness`: 100
  - `bOutsideBorders`: 1
  - `FeatureMakesValids`: 密林 / 深い密林
  - `bUnique`: 1
  - `BonusConvert`: 大地のマナ

### Eye of Hastur - ハスターの眼差し

- 内部名: `IMPROVEMENT_EYE_OF_HASTUR`
- 対応資源: 精神のマナ
- テクノロジーによる産出変化: 帆走 +2[商業] / 光学 +2[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bPermanent`: 1
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 湿地 / 凍土 / 氷原
  - `bUnique`: 1
  - `iVisibilityChange`: 6
  - `iExtraSeeFrom`: 1
  - `BonusConvert`: 精神のマナ
  - `PythonExplore`: exploreLairEpic

### Aifon Isle (explored) - マエナルス島（探索済）

- 内部名: `IMPROVEMENT_AIFON_ISLE_EXPLORED`
- 昇格先: マエナルス島
- 昇格ターン: 200
- 対応資源: 水のマナ
- その他の設定:
  - `YieldChanges`: iYieldChange=3 / iYieldChange=4
  - `bWater`: 1
  - `bPermanent`: 1
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 外洋
  - `BonusConvert`: 水のマナ

### Bradelines Well (explored) - ブラデリンの井戸（探索済）

- 内部名: `IMPROVEMENT_BRADELINES_WELL_EXPLORED`
- 昇格先: ブラデリンの井戸
- 昇格ターン: 200
- 対応資源: 不可逆のマナ
- テクノロジーによる産出変化: 屍霊術 +3[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bRequiresFlatlands`: 1
  - `bPermanent`: 1
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 湿地 / 草原 / 平原 / 砂漠 / 凍土 / 氷原 / 地獄の浅瀬 / 死滅の大地 / 破滅の原野 / 灼熱の砂地
  - `BonusConvert`: 不可逆のマナ

### Broken Sepulcher (explored) - 暴かれた玄室（探索済）

- 内部名: `IMPROVEMENT_BROKEN_SEPULCHER_EXPLORED`
- 昇格先: 暴かれた玄室
- 昇格ターン: 200
- 対応資源: 死のマナ
- テクノロジーによる産出変化: 屍霊術 +1[ハンマー], +1[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=1 / iYieldChange=1
  - `bPermanent`: 1
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 湿地 / 草原 / 平原 / 砂漠 / 凍土 / 氷原 / 地獄の浅瀬 / 死滅の大地 / 破滅の原野 / 灼熱の砂地
  - `BonusConvert`: 死のマナ
  - `PythonOnMove`: onMoveBrokenSepulcher

### Pyre of the Seraphic (explored) - 熾天使の火葬（探索済）

- 内部名: `IMPROVEMENT_PYRE_OF_THE_SERAPHIC_EXPLORED`
- 昇格先: 熾天使の火葬
- 昇格ターン: 200
- 対応資源: 炎のマナ
- テクノロジーによる産出変化: 四大元素 +2[ハンマー]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bRequiresFlatlands`: 1
  - `bPermanent`: 1
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 平原 / 砂漠 / 破滅の原野 / 灼熱の砂地
  - `BonusConvert`: 炎のマナ
  - `PythonOnMove`: onMovePyreOfTheSeraphic

### Eye of Hastur (explored) - ハスターの眼差し（探索済）

- 内部名: `IMPROVEMENT_EYE_OF_HASTUR_EXPLORED`
- 昇格先: ハスターの眼差し
- 昇格ターン: 200
- 対応資源: 精神のマナ
- テクノロジーによる産出変化: 帆走 +2[商業] / 光学 +2[商業]
- その他の設定:
  - `YieldChanges`: iYieldChange=2
  - `bPermanent`: 1
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土 / 氷原
  - `iVisibilityChange`: 6
  - `iExtraSeeFrom`: 1
  - `BonusConvert`: 精神のマナ

### Wolf Lair - 狼のねぐら

- 内部名: `IMPROVEMENT_DEN_WOLF`
- その他の設定:
  - `bPermanent`: 1
  - `iDefenseModifier`: 150
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 凍土
  - `FeatureMakesValids`: 森林
  - `iAppearanceProbability`: 100
  - `PythonExplore`: exploreDen
  - `SpawnUnitType`: 狼
  - `SpawnBarbarianType`: BARBARIAN_ANIMAL

### Gorilla Shack - ゴリラの棲家

- 内部名: `IMPROVEMENT_DEN_GORILLA`
- その他の設定:
  - `bPermanent`: 1
  - `iDefenseModifier`: 100
  - `bOutsideBorders`: 1
  - `FeatureMakesValids`: 密林
  - `iAppearanceProbability`: 10
  - `PythonExplore`: exploreDen
  - `SpawnUnitType`: ゴリラ
  - `SpawnBarbarianType`: BARBARIAN_ANIMAL

### Tiger Lair - 虎のねぐら

- 内部名: `IMPROVEMENT_DEN_TIGER`
- その他の設定:
  - `bPermanent`: 1
  - `iDefenseModifier`: 100
  - `bOutsideBorders`: 1
  - `FeatureMakesValids`: 密林 / 森林 / 古代樹林
  - `iAppearanceProbability`: 50
  - `PythonExplore`: exploreDen
  - `SpawnUnitType`: 虎
  - `SpawnBarbarianType`: BARBARIAN_ANIMAL

### Haunted Ruins - 悪霊の遺跡

- 内部名: `IMPROVEMENT_HAUNTED_RUINS`
- その他の設定:
  - `bPermanent`: 1
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 砂漠
  - `iAppearanceProbability`: 20
  - `PythonExplore`: exploreDen
  - `SpawnUnitType`: 悪霊
  - `InitialSpawnUnitType`: 悪霊
  - `SpawnBarbarianType`: BARBARIAN_UNDEAD
  - `SpawnUnitFreePromotions`: 非力

### Spider Den - 蜘蛛の巣

- 内部名: `IMPROVEMENT_DEN_SPIDER`
- その他の設定:
  - `bPermanent`: 1
  - `iDefenseModifier`: 25
  - `bOutsideBorders`: 1
  - `FeatureMakesValids`: 密林 / 森林 / 沼
  - `iAppearanceProbability`: 20
  - `PythonExplore`: exploreDen
  - `SpawnUnitType`: 巨大蜘蛛
  - `SpawnBarbarianType`: BARBARIAN_ANIMAL

### Troll Ruins - トロール遺跡

- 内部名: `IMPROVEMENT_TROLL_CAVE`
- その他の設定:
  - `bPermanent`: 1
  - `bOutsideBorders`: 1
  - `FeatureMakesValids`: 沼
  - `iAppearanceProbability`: 500
  - `PythonExplore`: exploreDen
  - `SpawnUnitType`: 沼トロール
  - `SpawnBarbarianType`: BARBARIAN_ANIMAL

### Hillgiant Steading - 丘巨人の縄張り

- 内部名: `IMPROVEMENT_HILLGIANT_STEADING`
- その他の設定:
  - `bHillsMakesValid`: 1
  - `bPermanent`: 1
  - `bUseLSystem`: 1
  - `iDefenseModifier`: 40
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 草原 / 平原 / 砂漠
  - `iAppearanceProbability`: 10
  - `iHealRateChange`: 20
  - `iRange`: 2
  - `iRangeDefenseModifier`: 15
  - `iExtraSeeFrom`: 1
  - `PythonExplore`: exploreDen
  - `SpawnUnitType`: 丘巨人
  - `SpawnBarbarianType`: BARBARIAN_ANIMAL

### Griffin nest - グリフォンの巣

- 内部名: `IMPROVEMENT_GRIFFIN_NEST`
- その他の設定:
  - `bHillsMakesValid`: 1
  - `bPermanent`: 1
  - `iDefenseModifier`: 75
  - `bOutsideBorders`: 1
  - `iAppearanceProbability`: 20
  - `PythonExplore`: exploreDen
  - `SpawnUnitType`: グリフォン
  - `SpawnBarbarianType`: BARBARIAN_ANIMAL

### Gate of the Marchosias - 巨獣の門

- 内部名: `IMPROVEMENT_DARKGATE`
- その他の設定:
  - `iPillageGold`: 10
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土 / 氷原
  - `SpawnUnitType`: マルコシアス
  - `InitialSpawnUnitType`: マルコシアス
  - `SpawnBarbarianType`: BARBARIAN_DEMONS
  - `SpawnUnitFreePromotions`: 黙示録の証

### Gate of the Dragonliche - 屍竜の門

- 内部名: `IMPROVEMENT_DARKGATE2`
- その他の設定:
  - `iPillageGold`: 10
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土 / 氷原
  - `SpawnUnitType`: ドラゴンリッチ
  - `InitialSpawnUnitType`: ドラゴンリッチ
  - `SpawnBarbarianType`: BARBARIAN_UNDEAD
  - `SpawnUnitFreePromotions`: 黙示録の証

### Frostling Den - フロストリングの巣窟

- 内部名: `IMPROVEMENT_FROSTLING_DEN`
- その他の設定:
  - `bPermanent`: 1
  - `iDefenseModifier`: 25
  - `bOutsideBorders`: 1
  - `TerrainMakesValids`: 氷原
  - `iAppearanceProbability`: 200
  - `PythonExplore`: exploreLair
  - `SpawnUnitType`: フロストリング
  - `InitialSpawnUnitType`: 弓兵
  - `SpawnBarbarianType`: BARBARIAN_FROSTLING
