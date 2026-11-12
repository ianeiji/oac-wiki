# OAC/地物（0.57、XMLから生成）

- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）
- 生成元: `Terrain/CIV4FeatureInfos.xml`
- 読み方: 主要な項目は日本語ラベル付きで先頭に、それ以外の既定値でない設定は「その他の設定」にXMLのタグ名のまま列挙する。値の内部名は日本語名に置き換えている。Pythonで実装された効果はXMLにないため含まない（ゲーム内ヘルプの説明文があれば載せている）。

### Kelp - 海藻

- 内部名: `FEATURE_KELP`
- 産出の変化: iYieldChange=1
- その他の設定:
  - `iMovement`: 2
  - `iSeeThrough`: 1
  - `iDefense`: 20
  - `iAppearance`: 500
  - `iGrowth`: 1
  - `bNoLake`: 1
  - `TerrainBooleans`: 近海
  - `bNormalize`: 1
  - `FeatureSpread`: 海藻

### Ice - 氷棚

- 内部名: `FEATURE_ICE`
- その他の設定:
  - `iMovement`: 1
  - `bImpassable`: 1
  - `TerrainBooleans`: 近海 / 外洋

### Jungle - 密林

- 内部名: `FEATURE_JUNGLE`
- その他の設定:
  - `iMovement`: 2
  - `iSeeThrough`: 1
  - `iHealthPercent`: -25
  - `iDefense`: 25
  - `iGrowth`: 16
  - `TerrainBooleans`: 草原 / 湿地
  - `EffectType`: Birds flying out and fading.
  - `iEffectProbability`: 15
  - `iAdvancedStartRemoveCost`: 40
  - `bNormalize`: 1
  - `bFlammable`: 1
  - `FeatureSpread`: 密林

### Oasis - オアシス

- 内部名: `FEATURE_OASIS`
- 産出の変化: iYieldChange=3 / iYieldChange=2
- その他の設定:
  - `iMovement`: 2
  - `iSeeThrough`: 1
  - `iAppearance`: 500
  - `bNoCoast`: 1
  - `bNoRiver`: 1
  - `bNoAdjacent`: 1
  - `bRequiresFlatlands`: 1
  - `bAddsFreshWater`: 1
  - `bNoCity`: 1
  - `bNoImprovement`: 1
  - `TerrainBooleans`: 砂漠
  - `bNormalize`: 1

### Flood Plains - 氾濫原

- 内部名: `FEATURE_FLOOD_PLAINS`
- 産出の変化: iYieldChange=3
- その他の設定:
  - `RiverYieldChange`: +1[商業]
  - `iMovement`: 1
  - `iHealthPercent`: -40
  - `iAppearance`: 10000
  - `bRequiresFlatlands`: 1
  - `bRequiresRiver`: 1
  - `bRestoreAutomatically`: 1
  - `bMaintainWithCity`: 1
  - `bOverrideTerrain`: 1
  - `TerrainBooleans`: 砂漠
  - `bNormalize`: 1
  - `FeatureUp`: 黒の氾濫原

### Forest - 森林

- 内部名: `FEATURE_FOREST`
- 産出の変化: iYieldChange=1
- その他の設定:
  - `iMovement`: 2
  - `iSeeThrough`: 1
  - `iHealthPercent`: 50
  - `iDefense`: 25
  - `iGrowth`: 8
  - `iUpgradeProbability`: 3
  - `TerrainBooleans`: 草原 / 平原 / 凍土
  - `EffectType`: Birds flying out and fading.
  - `iEffectProbability`: 15
  - `bNormalize`: 1
  - `bFlammable`: 1
  - `FeatureUpgrade`: 古代樹林
  - `FeatureUp`: 捩れた森林
  - `FeatureSpread`: 若き森林

### Burnt Forest - 焼け落ちた森林

- 内部名: `FEATURE_FOREST_BURNT`
- 産出の変化: iYieldChange=1
- その他の設定:
  - `iMovement`: 1
  - `iSeeThrough`: 1
  - `iUpgradeProbability`: 3
  - `TerrainBooleans`: 草原 / 平原 / 凍土
  - `EffectType`: Birds flying out and fading.
  - `iEffectProbability`: 15
  - `FeatureUpgrade`: 若き森林

### New Forest - 若き森林

- 内部名: `FEATURE_FOREST_NEW`
- 産出の変化: iYieldChange=1
- その他の設定:
  - `iMovement`: 1
  - `iSeeThrough`: 1
  - `iHealthPercent`: 25
  - `iGrowth`: 2
  - `iUpgradeProbability`: 3
  - `TerrainBooleans`: 草原 / 平原 / 凍土
  - `EffectType`: Birds flying out and fading.
  - `iEffectProbability`: 15
  - `FeatureUpgrade`: 森林
  - `FeatureSpread`: 若き森林

### Twisted Forest - 捩れた森林

- 内部名: `FEATURE_FOREST_BLIGHTED`
- その他の設定:
  - `iMovement`: 2
  - `iSeeThrough`: 1
  - `iHealthPercent`: -25
  - `iDefense`: 25
  - `TerrainBooleans`: 死滅の大地 / 破滅の原野 / 凍土
  - `bFlammable`: 1

### Fallout - 死の灰

- 内部名: `FEATURE_FALLOUT`
- 産出の変化: iYieldChange=-3 / iYieldChange=-3 / iYieldChange=-3
- その他の設定:
  - `iMovement`: 2
  - `iHealthPercent`: -50
  - `bImpassable`: 1
  - `bNoImprovement`: 1
  - `bOverrideTerrain`: 1
  - `TerrainBooleans`: 砂漠 / 草原 / 平原 / 湿地 / 氷原 / 凍土

### Ancient Forest - 古代樹林

- 内部名: `FEATURE_FOREST_ANCIENT`
- 産出の変化: iYieldChange=1 / iYieldChange=1
- その他の設定:
  - `iMovement`: 2
  - `iSeeThrough`: 1
  - `iHealthPercent`: 50
  - `iDefense`: 50
  - `iGrowth`: 8
  - `bNoCoast`: 1
  - `bNoRiver`: 1
  - `bIgnorePlotCounter`: 1
  - `TerrainBooleans`: 草原 / 平原
  - `FeatureSpread`: 若き森林
  - `PrereqStateReligion`: 緑葉の同胞
  - `PythonAtRange`: atRangeAncientForest

### Flames - 延焼

- 内部名: `FEATURE_FLAMES`
- その他の設定:
  - `iMovement`: 2
  - `iSeeThrough`: 1
  - `iHealthPercent`: -25
  - `TerrainBooleans`: 灼熱の砂地
  - `RequireResist`: 火炎

### Obsidian Plains - 黒の氾濫原

- 内部名: `FEATURE_OBSIDIAN_PLAINS`
- 産出の変化: iYieldChange=1
- その他の設定:
  - `RiverYieldChange`: +1[商業]
  - `iMovement`: 1
  - `iHealthPercent`: -40
  - `bRequiresFlatlands`: 1
  - `bRequiresRiver`: 1
  - `bRestoreAutomatically`: 1
  - `bMaintainWithCity`: 1
  - `bOverrideTerrain`: 1
  - `TerrainBooleans`: 灼熱の砂地

### Volcano - 活火山

- 内部名: `FEATURE_VOLCANO`
- その他の設定:
  - `iMovement`: 2
  - `iSeeThrough`: 2
  - `bRequiresFlatlands`: 1
  - `bImpassable`: 1
  - `bOverrideTerrain`: 1
  - `TerrainBooleans`: 死滅の大地 / 灼熱の砂地 / 砂漠 / 破滅の原野 / 草原 / 平原 / 湿地 / 地獄の浅瀬 / 氷原 / 凍土
  - `EffectType`: Volcano Effect
  - `iEffectProbability`: 25

### Scrubs - 灌木林

- 内部名: `FEATURE_SCRUB`
- 産出の変化: iYieldChange=1
- その他の設定:
  - `iMovement`: 2
  - `iAppearance`: 1000
  - `iGrowth`: 2
  - `bNoRiver`: 1
  - `bRequiresFlatlands`: 1
  - `TerrainBooleans`: 砂漠
  - `bFlammable`: 1
  - `FeatureSpread`: 灌木林

### Crystal Plains - 水晶原

- 内部名: `FEATURE_CRYSTAL_PLAINS`
- 産出の変化: iYieldChange=1
- その他の設定:
  - `iMovement`: 1
  - `iHealthPercent`: -40
  - `iAppearance`: 5000
  - `bRequiresFlatlands`: 1
  - `bRequiresRiver`: 1
  - `bMaintainWithCity`: 1
  - `bOverrideTerrain`: 1
  - `TerrainBooleans`: 氷原 / 凍土

### Blizzard - 猛吹雪

- 内部名: `FEATURE_BLIZZARD`
- その他の設定:
  - `iMovement`: 1
  - `iSeeThrough`: 2
  - `TerrainBooleans`: 氷原 / 凍土
  - `PythonOnMove`: onMoveBlizzard

### Tormented Souls - 責め苦の霊魂

- 内部名: `FEATURE_TORMENTED_SOULS`
- その他の設定:
  - `iMovement`: 1

### Door - 扉

- 内部名: `FEATURE_DOOR_WEST_CLOSED`
- その他の設定:
  - `iMovement`: 5
  - `iSeeThrough`: 1
  - `bNoCity`: 1
  - `bNoImprovement`: 1
  - `OnUnitChangeTo`: 扉

### Door - 扉

- 内部名: `FEATURE_DOOR_WEST_OPEN`
- その他の設定:
  - `iMovement`: 1
  - `bNoCity`: 1
  - `bNoImprovement`: 1

### Door - 扉

- 内部名: `FEATURE_DOOR_NORTH_CLOSED`
- その他の設定:
  - `iMovement`: 5
  - `iSeeThrough`: 1
  - `bNoCity`: 1
  - `bNoImprovement`: 1
  - `OnUnitChangeTo`: 扉

### Door - 扉

- 内部名: `FEATURE_DOOR_NORTH_OPEN`
- その他の設定:
  - `iMovement`: 1
  - `bNoCity`: 1
  - `bNoImprovement`: 1

### Walls - 壁

- 内部名: `FEATURE_WALLS`
- その他の設定:
  - `iMovement`: 1
  - `iSeeThrough`: 9
  - `bImpassable`: 1

### Swamp - 沼

- 内部名: `FEATURE_SWAMP`
- 産出の変化: iYieldChange=2 / iYieldChange=1
- その他の設定:
  - `iMovement`: 2
  - `iSeeThrough`: 1
  - `iHealthPercent`: -50
  - `iDefense`: -25
  - `iAppearance`: 2000
  - `iGrowth`: 8
  - `bNoCoast`: 1
  - `bRequiresFlatlands`: 1
  - `bAddsFreshWater`: 1
  - `bOverrideTerrain`: 1
  - `TerrainBooleans`: 湿地 / 凍土
  - `bNormalize`: 1
  - `FeatureSpread`: 沼

### Deep Jungle - 深い密林

- 内部名: `FEATURE_DEEP_JUNGLE`
- 産出の変化: iYieldChange=1 / iYieldChange=1
- その他の設定:
  - `RiverYieldChange`: +1[食料]
  - `iMovement`: 3
  - `iSeeThrough`: 1
  - `iHealthPercent`: 50
  - `iDefense`: 50
  - `iGrowth`: 8
  - `bNoCoast`: 1
  - `bNoRiver`: 1
  - `bIgnorePlotCounter`: 1
  - `TerrainBooleans`: 草原 / 湿地
  - `EffectType`: Birds flying out and fading.
  - `iEffectProbability`: 15
  - `iAdvancedStartRemoveCost`: 40
  - `FeatureSpread`: 密林

### Cistern - 貯水池

- 内部名: `FEATURE_CISTERN`
- その他の設定:
  - `iMovement`: 1
  - `iSeeThrough`: 1
  - `bRequiresFlatlands`: 1
  - `bAddsFreshWater`: 1

### Haunted Lands - 悪霊の地

- 内部名: `FEATURE_HAUNTED_LANDS`
- その他の設定:
  - `RiverYieldChange`: +1[商業]
  - `iMovement`: 2
  - `iSeeThrough`: 1
  - `iAppearance`: 100
  - `bOverrideTerrain`: 1
  - `TerrainBooleans`: 湿地 / 草原 / 平原 / 砂漠 / 凍土 / 氷原 / 地獄の浅瀬 / 死滅の大地 / 破滅の原野 / 灼熱の砂地
  - `EffectType`: Birds flying out and fading.
  - `iEffectProbability`: 15
  - `bNormalize`: 1

### Void - 虚空

- 内部名: `FEATURE_VOID`
- 産出の変化: iYieldChange=-3 / iYieldChange=-3 / iYieldChange=-3
- その他の設定:
  - `iMovement`: 1
  - `iSeeThrough`: 3
  - `iTurnDamage`: 100
  - `bImpassable`: 1
  - `bNoImprovement`: 1
  - `bVisibleAlways`: 1
  - `bOverrideTerrain`: 1
  - `PythonOnMove`: onMoveDistortion

### Distortion - 歪んだ空間

- 内部名: `FEATURE_DISTORTION`
- 産出の変化: iYieldChange=-3 / iYieldChange=-3 / iYieldChange=-3
- その他の設定:
  - `iMovement`: 1
  - `iSeeThrough`: 3
  - `iTurnDamage`: 100
  - `bImpassable`: 1
  - `bNoImprovement`: 1
  - `bVisibleAlways`: 1
  - `bOverrideTerrain`: 1
  - `PythonOnMove`: onMoveDistortion
