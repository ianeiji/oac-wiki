# OAC/資源（0.57、XMLから生成）

- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）
- 生成元: `Terrain/CIV4BonusInfos.xml`
- 読み方: 主要な項目は日本語ラベル付きで先頭に、それ以外の既定値でない設定は「その他の設定」にXMLのタグ名のまま列挙する。値の内部名は日本語名に置き換えている。Pythonで実装された効果はXMLにないため含まない（ゲーム内ヘルプの説明文があれば載せている）。

### Copper - 銅

- 内部名: `BONUS_COPPER`
- 分類: BONUSCLASS_RUSH
- 発見テクノロジー: 採鉱
- 有効化テクノロジー: 青銅器
- 産出: iYieldChange=1
- その他の設定:
  - `iPlacementOrder`: 1
  - `iConstAppearance`: 100
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=15 / iRandApp2=15
  - `iPlayer`: 100
  - `iUnique`: 6
  - `bHills`: 1
  - `bFlatlands`: 1
  - `bNoRiverSide`: 1
  - `TerrainBooleans`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 草原 / 平原 / 砂漠 / 凍土 / 氷原
  - `DamageType`: 武器

### Iron - 鉄

- 内部名: `BONUS_IRON`
- 分類: BONUSCLASS_RUSH
- 発見テクノロジー: 製錬
- 有効化テクノロジー: 鉄器
- 産出: iYieldChange=1
- その他の設定:
  - `iConstAppearance`: 100
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=10 / iRandApp2=10
  - `iPlayer`: 75
  - `iUnique`: 7
  - `bHills`: 1
  - `bFlatlands`: 1
  - `bNoRiverSide`: 1
  - `TerrainBooleans`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 草原 / 平原 / 砂漠 / 凍土 / 氷原
  - `DamageType`: 武器

### Mithril - ミスリル

- 内部名: `BONUS_MITHRIL`
- 分類: BONUSCLASS_RUSH
- 発見テクノロジー: ミスリル器
- 有効化テクノロジー: ミスリル器
- 産出: iYieldChange=1
- その他の設定:
  - `iPlacementOrder`: 2
  - `iConstAppearance`: 100
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=10 / iRandApp2=10
  - `iPlayer`: 50
  - `iUnique`: 7
  - `bHills`: 1
  - `bFlatlands`: 1
  - `TerrainBooleans`: 灼熱の砂地 / 破滅の原野 / 平原 / 砂漠 / 凍土 / 氷原
  - `DamageType`: 武器

### Gunpowder - 火薬

- 内部名: `BONUS_GUNPOWDER`
- 分類: BONUSCLASS_RUSH
- 発見テクノロジー: 錬金術
- 有効化テクノロジー: 爆薬
- 産出: iYieldChange=1
- その他の設定:
  - `iPlacementOrder`: 2
  - `iConstAppearance`: 100
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=10 / iRandApp2=10
  - `iPlayer`: 75
  - `iUnique`: 6
  - `bHills`: 1
  - `TerrainBooleans`: 死滅の大地 / 破滅の原野 / 草原 / 平原 / 砂漠 / 凍土 / 氷原

### Horse - 馬

- 内部名: `BONUS_HORSE`
- 分類: BONUSCLASS_RUSH
- 発見テクノロジー: 畜産
- 有効化テクノロジー: 畜産
- 産出: iYieldChange=1
- その他の設定:
  - `iPlacementOrder`: 1
  - `iConstAppearance`: 100
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=10 / iRandApp2=10
  - `iPlayer`: 100
  - `iUnique`: 6
  - `bFlatlands`: 1
  - `bNoRiverSide`: 1
  - `TerrainBooleans`: 草原 / 平原 / 凍土
  - `iPlotCounterThreshold`: 10
  - `PlotCounterBonus`: ナイトメア

### Nightmare - ナイトメア

- 内部名: `BONUS_NIGHTMARE`
- 分類: BONUSCLASS_RUSH
- 発見テクノロジー: 畜産
- 有効化テクノロジー: 畜産
- 産出: iYieldChange=1
- その他の設定:
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `TerrainBooleans`: 死滅の大地 / 破滅の原野
  - `FreePromotion`: ナイトメア
  - `iFreePromotionChance`: 100

### Incense - 香木

- 内部名: `BONUS_INCENSE`
- 分類: BONUSCLASS_MYSTIC
- 発見テクノロジー: 原初の祈り
- 有効化テクノロジー: 哲学
- 産出: iYieldChange=1
- その他の設定:
  - `iPlacementOrder`: 2
  - `iConstAppearance`: 100
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=10 / iRandApp2=10
  - `iPlayer`: 75
  - `iUnique`: 4
  - `bHills`: 1
  - `bFlatlands`: 1
  - `TerrainBooleans`: 灼熱の砂地 / 砂漠
  - `FeatureBooleans`: 密林 / 森林
  - `FeatureTerrainBooleans`: 破滅の原野 / 平原

### Reagents - 秘薬

- 内部名: `BONUS_REAGENTS`
- 分類: BONUSCLASS_MYSTIC
- 発見テクノロジー: 原初の祈り
- 有効化テクノロジー: エーテルの知識
- 産出: iYieldChange=1
- その他の設定:
  - `iConstAppearance`: 100
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=10 / iRandApp2=10
  - `iPlayer`: 75
  - `iUnique`: 5
  - `bHills`: 1
  - `bFlatlands`: 1
  - `TerrainBooleans`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 草原 / 平原 / 砂漠

### Marble - 大理石

- 内部名: `BONUS_MARBLE`
- 分類: BONUSCLASS_WONDER
- 有効化テクノロジー: 石工
- 産出: iYieldChange=1
- その他の設定:
  - `iPlacementOrder`: 3
  - `iConstAppearance`: 100
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=10 / iRandApp2=10
  - `iPlayer`: 50
  - `bHills`: 1
  - `bFlatlands`: 1
  - `bNoRiverSide`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 破滅の原野 / 平原 / 凍土 / 氷原
  - `iPlotCounterThreshold`: 10
  - `PlotCounterBonus`: 影石

### Sheut Stone - 影石

- 内部名: `BONUS_SHEUT_STONE`
- 分類: BONUSCLASS_RUSH
- 有効化テクノロジー: 地獄の契約
- その他の設定:
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `TerrainBooleans`: 破滅の原野
  - `FreePromotion`: 影石
  - `iFreePromotionChance`: 100

### Gems - 宝石

- 内部名: `BONUS_GEMS`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 採鉱
- 産出: iYieldChange=1
- [幸福]: 1
- その他の設定:
  - `iPlacementOrder`: 5
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=20 / iRandApp2=20
  - `iPlayer`: 67
  - `iGroupRange`: 1
  - `bHills`: 1
  - `bFlatlands`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 死滅の大地
  - `FeatureBooleans`: 密林
  - `FeatureTerrainBooleans`: 草原

### Gold - 金

- 内部名: `BONUS_GOLD`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 採鉱
- 産出: iYieldChange=1
- [幸福]: 1
- その他の設定:
  - `iPlacementOrder`: 5
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=20 / iRandApp2=20
  - `iPlayer`: 100
  - `iGroupRange`: 1
  - `bHills`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 灼熱の砂地 / 破滅の原野 / 平原 / 砂漠

### Corn - トウモロコシ

- 内部名: `BONUS_CORN`
- 分類: BONUSCLASS_GRAIN
- 有効化テクノロジー: 農業
- 産出: iYieldChange=1
- [衛生]: 1
- その他の設定:
  - `iPlacementOrder`: 4
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 60
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iTilesPer`: 16
  - `bArea`: 1
  - `bFlatlands`: 1
  - `bNoRiverSide`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 草原
  - `bUseLSystem`: 1
  - `iPlotCounterThreshold`: 10

### Rice - 米

- 内部名: `BONUS_RICE`
- 分類: BONUSCLASS_GRAIN
- 有効化テクノロジー: 農業
- 産出: iYieldChange=1
- [衛生]: 1
- その他の設定:
  - `iPlacementOrder`: 4
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 40
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iTilesPer`: 16
  - `bArea`: 1
  - `bFlatlands`: 1
  - `bNoRiverSide`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 草原 / 湿地
  - `FeatureBooleans`: 密林 / 沼
  - `FeatureTerrainBooleans`: 草原 / 湿地
  - `iPlotCounterThreshold`: 10

### Wheat - 小麦

- 内部名: `BONUS_WHEAT`
- 分類: BONUSCLASS_GRAIN
- 有効化テクノロジー: 農業
- 産出: iYieldChange=1
- [衛生]: 1
- その他の設定:
  - `iPlacementOrder`: 4
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iTilesPer`: 16
  - `bArea`: 1
  - `bFlatlands`: 1
  - `bNoRiverSide`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 平原
  - `iPlotCounterThreshold`: 10

### Cow - 牛

- 内部名: `BONUS_COW`
- 分類: BONUSCLASS_LIVESTOCK
- 有効化テクノロジー: 畜産
- 産出: iYieldChange=1
- [衛生]: 1
- その他の設定:
  - `iPlacementOrder`: 4
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 50
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iTilesPer`: 16
  - `bArea`: 1
  - `bFlatlands`: 1
  - `bNoRiverSide`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 草原 / 平原
  - `iPlotCounterThreshold`: 10
  - `PlotCounterBonus`: 蛙

### Pig - 豚

- 内部名: `BONUS_PIG`
- 分類: BONUSCLASS_LIVESTOCK
- 有効化テクノロジー: 畜産
- 産出: iYieldChange=1
- [衛生]: 1
- その他の設定:
  - `iPlacementOrder`: 4
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMinLatitude`: 10
  - `iMaxLatitude`: 50
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iTilesPer`: 16
  - `bArea`: 1
  - `bHills`: 1
  - `bFlatlands`: 1
  - `bNoRiverSide`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 草原
  - `FeatureBooleans`: 密林
  - `FeatureTerrainBooleans`: 草原
  - `iPlotCounterThreshold`: 10
  - `PlotCounterBonus`: 蛙

### Sheep - 羊

- 内部名: `BONUS_SHEEP`
- 分類: BONUSCLASS_LIVESTOCK
- 有効化テクノロジー: 畜産
- 産出: iYieldChange=1
- [衛生]: 1
- その他の設定:
  - `iPlacementOrder`: 4
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMinLatitude`: 30
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iTilesPer`: 16
  - `bArea`: 1
  - `bHills`: 1
  - `bFlatlands`: 1
  - `bNoRiverSide`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 草原 / 平原
  - `iPlotCounterThreshold`: 10
  - `PlotCounterBonus`: 蛙

### Toads - 蛙

- 内部名: `BONUS_TOAD`
- 分類: BONUSCLASS_LIVESTOCK
- 有効化テクノロジー: 畜産
- 産出: iYieldChange=1
- [衛生]: 1
- その他の設定:
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `TerrainBooleans`: 死滅の大地 / 破滅の原野

### Deer - 鹿

- 内部名: `BONUS_DEER`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 狩猟
- 産出: iYieldChange=1
- [衛生]: 1
- その他の設定:
  - `iPlacementOrder`: 4
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMinLatitude`: 30
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iTilesPer`: 16
  - `iUnique`: 2
  - `bHills`: 1
  - `bFlatlands`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 凍土
  - `FeatureBooleans`: 森林
  - `FeatureTerrainBooleans`: 凍土

### Fur - 毛皮

- 内部名: `BONUS_FUR`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 狩猟
- 産出: iYieldChange=1
- [幸福]: 1
- その他の設定:
  - `iPlacementOrder`: 5
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iPlayer`: 100
  - `iGroupRange`: 1
  - `bHills`: 1
  - `bFlatlands`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 凍土 / 氷原
  - `FeatureBooleans`: 森林
  - `FeatureTerrainBooleans`: 凍土 / 氷原

### Ivory - 象牙

- 内部名: `BONUS_IVORY`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 狩猟
- 産出: iYieldChange=1
- [幸福]: 1
- その他の設定:
  - `iPlacementOrder`: 5
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 40
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iPlayer`: 75
  - `iUnique`: 4
  - `iGroupRange`: 1
  - `bArea`: 1
  - `bFlatlands`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 平原
  - `FeatureBooleans`: 密林
  - `FeatureTerrainBooleans`: 草原

### Banana - バナナ

- 内部名: `BONUS_BANANA`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 暦
- 産出: iYieldChange=1
- [衛生]: 1
- その他の設定:
  - `iPlacementOrder`: 4
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 40
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iTilesPer`: 16
  - `iUnique`: 2
  - `bArea`: 1
  - `bFlatlands`: 1
  - `bNormalize`: 1
  - `FeatureBooleans`: 密林
  - `FeatureTerrainBooleans`: 草原
  - `iPlotCounterThreshold`: 10
  - `PlotCounterBonus`: グラガルム

### Sugar - 砂糖

- 内部名: `BONUS_SUGAR`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 暦
- 産出: iYieldChange=1
- [幸福]: 1
- その他の設定:
  - `iPlacementOrder`: 5
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iPlayer`: 100
  - `iGroupRange`: 1
  - `bArea`: 1
  - `bFlatlands`: 1
  - `bNormalize`: 1
  - `FeatureBooleans`: 密林
  - `FeatureTerrainBooleans`: 草原
  - `iPlotCounterThreshold`: 10
  - `PlotCounterBonus`: グラガルム

### Gulagarm - グラガルム

- 内部名: `BONUS_GULAGARM`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 邪悪への道
- 産出: iYieldChange=1
- [幸福]: 1
- その他の設定:
  - `iMaxLatitude`: 90
  - `TerrainBooleans`: 死滅の大地 / 破滅の原野

### Cotton - 綿花

- 内部名: `BONUS_COTTON`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 暦
- 産出: iYieldChange=1
- [幸福]: 1
- その他の設定:
  - `iPlacementOrder`: 5
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iPlayer`: 100
  - `iGroupRange`: 1
  - `bArea`: 1
  - `bFlatlands`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 草原 / 平原
  - `iPlotCounterThreshold`: 10
  - `PlotCounterBonus`: 剃刀草

### Dye - 染料

- 内部名: `BONUS_DYE`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 暦
- 産出: iYieldChange=1
- [幸福]: 1
- その他の設定:
  - `iPlacementOrder`: 5
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iPlayer`: 100
  - `iGroupRange`: 1
  - `bArea`: 1
  - `bFlatlands`: 1
  - `bNormalize`: 1
  - `FeatureBooleans`: 密林
  - `FeatureTerrainBooleans`: 草原 / 湿地
  - `iPlotCounterThreshold`: 10
  - `PlotCounterBonus`: 剃刀草

### Silk - 絹

- 内部名: `BONUS_SILK`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 動物の馴致
- 産出: iYieldChange=1
- [幸福]: 1
- その他の設定:
  - `iPlacementOrder`: 5
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iPlayer`: 50
  - `bArea`: 1
  - `bFlatlands`: 1
  - `FeatureBooleans`: 森林
  - `FeatureTerrainBooleans`: 草原 / 平原
  - `bUseLSystem`: 1
  - `iPlotCounterThreshold`: 10
  - `PlotCounterBonus`: 剃刀草

### Razorweed - 剃刀草

- 内部名: `BONUS_RAZORWEED`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 毒物
- 産出: iYieldChange=1
- その他の設定:
  - `iMaxLatitude`: 90
  - `TerrainBooleans`: 死滅の大地 / 破滅の原野 / 地獄の浅瀬

### Wine - ワイン

- 内部名: `BONUS_WINE`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 道具の作成
- 産出: iYieldChange=1
- [幸福]: 1
- その他の設定:
  - `iPlacementOrder`: 5
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMinLatitude`: 20
  - `iMaxLatitude`: 50
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iPlayer`: 100
  - `iGroupRange`: 1
  - `bArea`: 1
  - `bHills`: 1
  - `bFlatlands`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 死滅の大地 / 草原
  - `bUseLSystem`: 1

### Clam - 貝

- 内部名: `BONUS_CLAM`
- 分類: BONUSCLASS_GENERAL
- 産出: iYieldChange=1
- [衛生]: 1
- その他の設定:
  - `iPlacementOrder`: 6
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 40
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iTilesPer`: 32
  - `iUnique`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 近海
  - `FeatureBooleans`: 海藻
  - `FeatureTerrainBooleans`: 近海

### Crab - 蟹

- 内部名: `BONUS_CRAB`
- 分類: BONUSCLASS_GENERAL
- 産出: iYieldChange=1
- [衛生]: 1
- その他の設定:
  - `iPlacementOrder`: 6
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 10
  - `iMinLatitude`: 40
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iTilesPer`: 32
  - `iUnique`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 近海
  - `FeatureBooleans`: 海藻
  - `FeatureTerrainBooleans`: 近海

### Fish - 魚

- 内部名: `BONUS_FISH`
- 分類: BONUSCLASS_GENERAL
- 産出: iYieldChange=1
- [衛生]: 1
- その他の設定:
  - `iPlacementOrder`: 6
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iTilesPer`: 32
  - `iUnique`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 外洋 / 近海
  - `FeatureBooleans`: 海藻
  - `FeatureTerrainBooleans`: 外洋 / 近海

### Whale - 鯨

- 内部名: `BONUS_WHALE`
- 分類: BONUSCLASS_GENERAL
- 産出: iYieldChange=1
- [幸福]: 1
- その他の設定:
  - `iPlacementOrder`: 6
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 10
  - `iMinLatitude`: 50
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iPlayer`: 67
  - `iUnique`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 外洋
  - `FeatureBooleans`: 海藻
  - `FeatureTerrainBooleans`: 外洋

### Pearls - 真珠

- 内部名: `BONUS_PEARL`
- 分類: BONUSCLASS_GENERAL
- 発見テクノロジー: 海洋志向
- 有効化テクノロジー: 海洋志向
- 産出: iYieldChange=1
- [幸福]: 1
- その他の設定:
  - `iPlacementOrder`: 6
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iTilesPer`: 30
  - `bNormalize`: 1
  - `TerrainBooleans`: 外洋 / 近海
  - `FeatureBooleans`: 海藻
  - `FeatureTerrainBooleans`: 外洋 / 近海

### Fruit of Yggdrasil - 世界樹の果実

- 内部名: `BONUS_FRUIT_OF_YGGDRASIL`
- 分類: BONUSCLASS_GENERAL
- [幸福]: 1
- [衛生]: 2
- その他の設定:
  - `iMaxLatitude`: 90

### Ale - エール酒

- 内部名: `BONUS_ALE`
- 分類: BONUSCLASS_GENERAL
- [幸福]: 1
- その他の設定:
  - `iMaxLatitude`: 90

### Mana - マナ

- 内部名: `BONUS_MANA`
- 分類: BONUSCLASS_RAWMANA
- 有効化テクノロジー: Never
- その他の設定:
  - `iPlacementOrder`: 1
  - `iConstAppearance`: 100
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=20 / iRandApp2=20
  - `iPlayer`: 200
  - `iUnique`: 6
  - `bHills`: 1
  - `bFlatlands`: 1
  - `TerrainBooleans`: 死滅の大地 / 灼熱の砂地 / 破滅の原野 / 地獄の浅瀬 / 草原 / 平原 / 砂漠 / 湿地 / 凍土 / 氷原

### Air Mana - 大気のマナ

- 内部名: `BONUS_MANA_AIR`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1
  - `iOverSeasTradeModifier`: 20
  - `DamageType`: 電撃

### Body Mana - 肉体のマナ

- 内部名: `BONUS_MANA_BODY`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1
  - `iHealChange`: 5

### Chaos Mana - 混沌のマナ

- 内部名: `BONUS_MANA_CHAOS`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1
  - `FreePromotion`: 異形
  - `iFreePromotionChance`: 2

### Death Mana - 死のマナ

- 内部名: `BONUS_MANA_DEATH`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1
  - `DamageType`: 死

### Earth Mana - 大地のマナ

- 内部名: `BONUS_MANA_EARTH`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1
  - `iDiscoverRandModifier`: 20
  - `DamageType`: 物理

### Enchantment Mana - 呪付のマナ

- 内部名: `BONUS_MANA_ENCHANTMENT`
- 分類: BONUSCLASS_MANA
- [幸福]: 1
- その他の設定:
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1

### Entropy Mana - 不可逆のマナ

- 内部名: `BONUS_MANA_ENTROPY`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1
  - `iHealChangeEnemy`: -5
  - `DamageType`: 不浄

### Fire Mana - 炎のマナ

- 内部名: `BONUS_MANA_FIRE`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1
  - `DamageType`: 火炎

### Ice Mana - 氷のマナ

- 内部名: `BONUS_MANA_ICE`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1
  - `DamageType`: 冷気

### Law Mana - 法のマナ

- 内部名: `BONUS_MANA_LAW`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1
  - `iMaintenanceModifier`: -5
  - `DamageType`: 神聖
  - `FreePromotion`: 武勇
  - `iFreePromotionChance`: 1

### Life Mana - 生命のマナ

- 内部名: `BONUS_MANA_LIFE`
- 分類: BONUSCLASS_MANA
- [衛生]: 1
- その他の設定:
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1

### Metamagic Mana - 超魔術のマナ

- 内部名: `BONUS_MANA_METAMAGIC`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1

### Mind Mana - 精神のマナ

- 内部名: `BONUS_MANA_MIND`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1
  - `iResearchModifier`: 3
  - `DamageType`: 催眠

### Nature Mana - 自然のマナ

- 内部名: `BONUS_MANA_NATURE`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1
  - `iFeatureGrowthModifier`: 100
  - `DamageType`: 毒

### Shadow Mana - 影のマナ

- 内部名: `BONUS_MANA_SHADOW`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1
  - `FreePromotion`: 身隠し
  - `iFreePromotionChance`: 2

### Spirit Mana - 魂のマナ

- 内部名: `BONUS_MANA_SPIRIT`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1
  - `iGreatPeopleRateModifier`: 5

### Sun Mana - 太陽のマナ

- 内部名: `BONUS_MANA_SUN`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1
  - `iShortGoldenAgePermil`: 5
  - `DamageType`: 火炎

### Water Mana - 水のマナ

- 内部名: `BONUS_MANA_WATER`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1
  - `bFreshWaterSource`: 1
  - `DamageType`: 冷気

### Antiquarian Book - 古書物

- 内部名: `BONUS_BOOK`
- 分類: BONUSCLASS_RUSH
- [幸福]: 1
- その他の設定:
  - `iMaxLatitude`: 90
  - `iDiscoverRandModifier`: 100
  - `DamageType`: 催眠

### Dragon Boulder - 竜玉石

- 内部名: `BONUS_DRAGONMETAL`
- 分類: BONUSCLASS_RUSH
- [幸福]: 1
- その他の設定:
  - `iDiscoverRandModifier`: 100
  - `FreePromotion`: 竜玉石の武器
  - `iFreePromotionChance`: 100

### Stone - 石材

- 内部名: `BONUS_STONE`
- 分類: BONUSCLASS_WONDER
- 有効化テクノロジー: 石工
- 産出: iYieldChange=1
- その他の設定:
  - `iPlacementOrder`: 3
  - `iConstAppearance`: 100
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=10 / iRandApp2=10
  - `iPlayer`: 50
  - `bHills`: 1
  - `bFlatlands`: 1
  - `bNoRiverSide`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 破滅の原野 / 平原 / 凍土 / 氷原
  - `iPlotCounterThreshold`: 10
  - `PlotCounterBonus`: 影石

### Patrian Artifacts - パトリアのアーティファクト

- 内部名: `BONUS_PATRIAN_ARTIFACTS`
- 分類: BONUSCLASS_GENERAL
- 発見テクノロジー: ギフト
- 有効化テクノロジー: ギフト
- 産出: iYieldChange=3
- [幸福]: 1
- その他の設定:
  - `iPlacementOrder`: 8
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iTilesPer`: 80
  - `bHills`: 1
  - `bFlatlands`: 1
  - `TerrainBooleans`: 草原 / 平原 / 砂漠 / 湿地 / 凍土 / 氷原

### Dimensional Mana - 次元のマナ

- 内部名: `BONUS_MANA_DIMENSIONAL`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iConstAppearance`: 100
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1
  - `iDiscoverRandModifier`: 50
  - `iResearchModifier`: 2

### Potato - ジャガイモ

- 内部名: `BONUS_POTATO`
- 分類: BONUSCLASS_GRAIN
- 有効化テクノロジー: 農業
- 産出: iYieldChange=2
- その他の設定:
  - `iPlacementOrder`: 4
  - `iConstAppearance`: 100
  - `iMinAreaSize`: 1
  - `iMinLatitude`: 20
  - `iMaxLatitude`: 80
  - `Rands`: iRandApp1=10 / iRandApp2=10
  - `iTilesPer`: 24
  - `iGroupRange`: 1
  - `bHills`: 1
  - `bFlatlands`: 1
  - `bNoRiverSide`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 平原
  - `iDiscoverRandModifier`: 10
  - `iPlotCounterThreshold`: 10

### Flax - 亜麻

- 内部名: `BONUS_FLAX`
- 分類: BONUSCLASS_GRAIN
- 有効化テクノロジー: 農業
- 産出: iYieldChange=1
- その他の設定:
  - `iPlacementOrder`: 4
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMinLatitude`: 40
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iTilesPer`: 16
  - `bArea`: 1
  - `bFlatlands`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 凍土 / 平原
  - `bUseLSystem`: 1
  - `iOverSeasTradeModifier`: 10
  - `iPlotCounterThreshold`: 10

### Coffee - コーヒー

- 内部名: `BONUS_COFFEE`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 暦
- 産出: iYieldChange=1
- その他の設定:
  - `iPlacementOrder`: 5
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 60
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iPlayer`: 100
  - `iGroupRange`: 1
  - `bArea`: 1
  - `bHills`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 死滅の大地 / 破滅の原野 / 地獄の浅瀬
  - `FeatureBooleans`: 密林 / 森林
  - `FeatureTerrainBooleans`: 草原 / 平原
  - `bUseLSystem`: 1
  - `iResearchModifier`: 3
  - `iPlotCounterThreshold`: 10
  - `PlotCounterBonus`: 剃刀草

### Shrimp - 海老

- 内部名: `BONUS_SHRIMP`
- 分類: BONUSCLASS_GENERAL
- 産出: iYieldChange=1 / iYieldChange=1
- [衛生]: 1
- その他の設定:
  - `iPlacementOrder`: 6
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iTilesPer`: 32
  - `iUnique`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 近海
  - `FeatureBooleans`: 海藻
  - `FeatureTerrainBooleans`: 外洋 / 近海

### Salt - 塩

- 内部名: `BONUS_SALT`
- 分類: BONUSCLASS_GRAIN
- 有効化テクノロジー: 採鉱
- 産出: iYieldChange=1
- [衛生]: 1
- その他の設定:
  - `iPlacementOrder`: 3
  - `iConstAppearance`: 100
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iPlayer`: 50
  - `bHills`: 1
  - `bFlatlands`: 1
  - `bNoRiverSide`: 1
  - `bNormalize`: 1
  - `TerrainBooleans`: 平原 / 砂漠
  - `FeatureBooleans`: 沼
  - `FeatureTerrainBooleans`: 草原 / 湿地
  - `iPlotCounterThreshold`: 10

### Amber - 琥珀

- 内部名: `BONUS_AMBER`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 採鉱
- 産出: iYieldChange=1
- その他の設定:
  - `iPlacementOrder`: 5
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMinLatitude`: 25
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iPlayer`: 50
  - `iGroupRange`: 1
  - `bHills`: 1
  - `bFlatlands`: 1
  - `bNormalize`: 1
  - `FeatureBooleans`: 森林 / 沼
  - `FeatureTerrainBooleans`: 草原 / 平原 / 湿地 / 凍土
  - `iGreatPeopleRateModifier`: 3
  - `iShortGoldenAgePermil`: 2

### Jade - 翡翠

- 内部名: `BONUS_JADE`
- 分類: BONUSCLASS_GENERAL
- 産出: iYieldChange=1
- その他の設定:
  - `iPlacementOrder`: 6
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iTilesPer`: 30
  - `bNormalize`: 1
  - `TerrainBooleans`: 近海
  - `FeatureBooleans`: 海藻
  - `FeatureTerrainBooleans`: 近海
  - `iGreatPeopleRateModifier`: 3

### Orange - オレンジ

- 内部名: `BONUS_ORANGE`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 暦
- 産出: iYieldChange=1
- その他の設定:
  - `iPlacementOrder`: 4
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 60
  - `Rands`: iRandApp1=10 / iRandApp2=10
  - `iTilesPer`: 40
  - `iGroupRange`: 1
  - `bArea`: 1
  - `bHills`: 1
  - `bFlatlands`: 1
  - `bNormalize`: 1
  - `FeatureBooleans`: 密林 / 森林
  - `FeatureTerrainBooleans`: 草原 / 平原
  - `iDiscoverRandModifier`: 10
  - `iPlotCounterThreshold`: 10
  - `PlotCounterBonus`: グラガルム

### Refined Mana - 精製されたマナ

- 内部名: `BONUS_REFINED_MANA`
- 分類: BONUSCLASS_MANA
- その他の設定:
  - `iMaxLatitude`: 90
  - `bModifierPerBonus`: 1
  - `iDiscoverRandModifier`: 10
  - `iResearchModifier`: 5

### Lemon - レモン

- 内部名: `BONUS_LEMON`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 暦
- 産出: iYieldChange=1
- その他の設定:
  - `iPlacementOrder`: 5
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 60
  - `Rands`: iRandApp1=10 / iRandApp2=10
  - `iTilesPer`: 24
  - `iGroupRange`: 1
  - `bArea`: 1
  - `bHills`: 1
  - `bFlatlands`: 1
  - `bNormalize`: 1
  - `FeatureBooleans`: 密林 / 森林
  - `FeatureTerrainBooleans`: 草原 / 平原
  - `iDiscoverRandModifier`: 10
  - `iPlotCounterThreshold`: 10
  - `PlotCounterBonus`: グラガルム

### Mushrooms - キノコ

- 内部名: `BONUS_MUSHROOMS`
- 分類: BONUSCLASS_GRAIN
- 有効化テクノロジー: 採鉱
- 産出: iYieldChange=1
- その他の設定:
  - `iPlacementOrder`: 4
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iPlayer`: 100
  - `iGroupRange`: 1
  - `bHills`: 1
  - `TerrainBooleans`: 草原 / 平原 / 砂漠 / 凍土 / 氷原
  - `iDiscoverRandModifier`: 10
  - `iPlotCounterThreshold`: 10

### Duskwood - 薄闇樹

- 内部名: `BONUS_DUSKWOOD`
- 分類: BONUSCLASS_RUSH
- 発見テクノロジー: 道具の作成
- 有効化テクノロジー: 弓術
- 産出: iYieldChange=1
- その他の設定:
  - `iPlacementOrder`: 3
  - `iConstAppearance`: 75
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 90
  - `Rands`: iRandApp1=20 / iRandApp2=20
  - `iPlayer`: 100
  - `iUnique`: 6
  - `bHills`: 1
  - `bFlatlands`: 1
  - `FeatureBooleans`: 森林
  - `FeatureTerrainBooleans`: 草原 / 平原 / 凍土
  - `iDiscoverRandModifier`: 10
  - `FreePromotion`: 薄闇樹の武器
  - `iFreePromotionChance`: 100

### Tea - 茶

- 内部名: `BONUS_TEA`
- 分類: BONUSCLASS_GENERAL
- 有効化テクノロジー: 暦
- 産出: iYieldChange=1
- その他の設定:
  - `iPlacementOrder`: 5
  - `iConstAppearance`: 50
  - `iMinAreaSize`: 3
  - `iMaxLatitude`: 60
  - `Rands`: iRandApp1=25 / iRandApp2=25
  - `iPlayer`: 100
  - `iGroupRange`: 1
  - `bArea`: 1
  - `bHills`: 1
  - `bNormalize`: 1
  - `FeatureBooleans`: 密林 / 森林
  - `FeatureTerrainBooleans`: 草原
  - `bUseLSystem`: 1
  - `iResearchModifier`: 3
  - `iPlotCounterThreshold`: 10
  - `PlotCounterBonus`: 剃刀草
