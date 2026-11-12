# OAC/地形（0.57、XMLから生成）

- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）
- 生成元: `Terrain/CIV4TerrainInfos.xml`
- 読み方: 主要な項目は日本語ラベル付きで先頭に、それ以外の既定値でない設定は「その他の設定」にXMLのタグ名のまま列挙する。値の内部名は日本語名に置き換えている。Pythonで実装された効果はXMLにないため含まない（ゲーム内ヘルプの説明文があれば載せている）。

### Grassland - 草原

- 内部名: `TERRAIN_GRASS`
- 産出: +2[食料]
- その他の設定:
  - `RiverYieldChange`: +1[商業]
  - `bFound`: 1
  - `iMovement`: 1
  - `iSeeFrom`: 1
  - `iSeeThrough`: 1
  - `bNormalize`: 1
  - `iPlotCounterUp`: 10
  - `TerrainUp`: 死滅の大地
  - `ColdTerrains`: 凍土 iColdThreshold=3000 / 氷原 iColdThreshold=6000

### Plains - 平原

- 内部名: `TERRAIN_PLAINS`
- 産出: +1[食料], +1[ハンマー]
- その他の設定:
  - `RiverYieldChange`: +1[商業]
  - `bFound`: 1
  - `iMovement`: 1
  - `iSeeFrom`: 1
  - `iSeeThrough`: 1
  - `bNormalize`: 1
  - `iPlotCounterUp`: 10
  - `TerrainUp`: 破滅の原野
  - `ColdTerrains`: 凍土 iColdThreshold=3000 / 氷原 iColdThreshold=6000

### Desert - 砂漠

- 内部名: `TERRAIN_DESERT`
- その他の設定:
  - `RiverYieldChange`: +1[商業]
  - `bFound`: 1
  - `iMovement`: 2
  - `iSeeFrom`: 1
  - `iSeeThrough`: 1
  - `iBuildModifier`: 25
  - `iDefense`: -25
  - `bNormalize`: 1
  - `iPlotCounterUp`: 10
  - `TerrainUp`: 灼熱の砂地
  - `ColdTerrains`: 平原 iColdThreshold=3000 / 凍土 iColdThreshold=6000 / 氷原 iColdThreshold=9000

### Marsh - 湿地

- 内部名: `TERRAIN_MARSH`
- 産出: +1[食料]
- その他の設定:
  - `RiverYieldChange`: +1[商業]
  - `bFound`: 1
  - `iMovement`: 2
  - `iSeeFrom`: 1
  - `iSeeThrough`: 1
  - `iBuildModifier`: 50
  - `iDefense`: -25
  - `bNormalize`: 1
  - `iPlotCounterUp`: 10
  - `TerrainUp`: 地獄の浅瀬
  - `ColdTerrains`: 凍土 iColdThreshold=3000 / 氷原 iColdThreshold=6000

### Tundra - 凍土

- 内部名: `TERRAIN_TUNDRA`
- 産出: +1[食料]
- その他の設定:
  - `RiverYieldChange`: +1[商業]
  - `bFound`: 1
  - `iMovement`: 1
  - `iSeeFrom`: 1
  - `iSeeThrough`: 1
  - `iBuildModifier`: 25
  - `bNormalize`: 1
  - `ColdTerrains`: 氷原 iColdThreshold=3000

### Ice - 氷原

- 内部名: `TERRAIN_SNOW`
- その他の設定:
  - `bFound`: 1
  - `iMovement`: 1
  - `iSeeFrom`: 1
  - `iSeeThrough`: 1
  - `iBuildModifier`: 50
  - `bNormalize`: 1

### Burning Sands - 灼熱の砂地

- 内部名: `TERRAIN_BURNING_SANDS`
- その他の設定:
  - `RiverYieldChange`: +1[商業]
  - `bFound`: 1
  - `iMovement`: 2
  - `iSeeFrom`: 1
  - `iSeeThrough`: 1
  - `iBuildModifier`: 25
  - `iDefense`: -25
  - `ColdTerrains`: 平原 iColdThreshold=3000 / 凍土 iColdThreshold=6000 / 氷原 iColdThreshold=9000

### Broken Lands - 死滅の大地

- 内部名: `TERRAIN_BROKEN_LANDS`
- 産出: +2[食料]
- その他の設定:
  - `RiverYieldChange`: +1[商業]
  - `bFound`: 1
  - `iMovement`: 1
  - `iSeeFrom`: 1
  - `iSeeThrough`: 1
  - `ColdTerrains`: 凍土 iColdThreshold=3000 / 氷原 iColdThreshold=6000

### Fields of Perdition - 破滅の原野

- 内部名: `TERRAIN_FIELDS_OF_PERDITION`
- 産出: +1[食料], +1[ハンマー]
- その他の設定:
  - `RiverYieldChange`: +1[商業]
  - `bFound`: 1
  - `iMovement`: 1
  - `iSeeFrom`: 1
  - `iSeeThrough`: 1
  - `ColdTerrains`: 凍土 iColdThreshold=3000 / 氷原 iColdThreshold=6000

### Shallows - 地獄の浅瀬

- 内部名: `TERRAIN_SHALLOWS`
- 産出: +1[食料]
- その他の設定:
  - `RiverYieldChange`: +1[商業]
  - `bFound`: 1
  - `iMovement`: 1
  - `iSeeFrom`: 1
  - `iSeeThrough`: 1
  - `iBuildModifier`: 25
  - `ColdTerrains`: 凍土 iColdThreshold=3000 / 氷原 iColdThreshold=6000

### Coast - 近海

- 内部名: `TERRAIN_COAST`
- 産出: +1[食料], +2[商業]
- その他の設定:
  - `bWater`: 1
  - `iMovement`: 1
  - `iDefense`: 10
  - `bNormalize`: 1

### Ocean - 外洋

- 内部名: `TERRAIN_OCEAN`
- 産出: +1[食料], +1[商業]
- その他の設定:
  - `bWater`: 1
  - `iMovement`: 1
  - `bNormalize`: 1

### Peak - 山頂

- 内部名: `TERRAIN_PEAK`
- その他の設定:
  - `bWater`: 1
  - `iMovement`: 1
  - `bNormalize`: 1

### Hill - 丘陵

- 内部名: `TERRAIN_HILL`
- その他の設定:
  - `bWater`: 1
  - `iMovement`: 1
  - `bNormalize`: 1
