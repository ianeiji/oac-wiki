# OAC/宗教（0.57、XMLから生成）

- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）
- 生成元: `Gameinfo/CIV4ReligionInfo.xml`
- 読み方: 主要な項目は日本語ラベル付きで先頭に、それ以外の既定値でない設定は「その他の設定」にXMLのタグ名のまま列挙する。値の内部名は日本語名に置き換えている。Pythonで実装された効果はXMLにないため含まない（ゲーム内ヘルプの説明文があれば載せている）。

### Fellowship of Leaves - 緑葉の同胞

- 内部名: `RELIGION_FELLOWSHIP_OF_LEAVES`
- 創始テクノロジー: 深き森への道
- その他の設定:
  - `FreeUnitClass`: TXT_KEY_UNIT_DISCIPLE
  - `iFreeUnits`: 1
  - `iSpreadFactor`: 100
  - `GlobalReligionCommerces`: iGlobalReligionCommerce=1
  - `HolyCityCommerces`: iHolyCityCommerce=4
  - `StateReligionCommerces`: iStateReligionCommerce=1
  - `TechButton`: Art/Interface/Buttons/Religions/Fellowship.dds
  - `GenericTechButton`: Art/Interface/Buttons/Religions/Fellowship.dds
  - `Alignment`: 中立
  - `AlignmentBest`: 善良
  - `AlignmentWorst`: 邪悪

### Order - 秩序の修道会

- 内部名: `RELIGION_THE_ORDER`
- 創始テクノロジー: 天界からの指令
- その他の設定:
  - `FreeUnitClass`: TXT_KEY_UNIT_DISCIPLE
  - `iFreeUnits`: 1
  - `iSpreadFactor`: 175
  - `GlobalReligionCommerces`: iGlobalReligionCommerce=1
  - `HolyCityCommerces`: iHolyCityCommerce=4
  - `StateReligionCommerces`: iStateReligionCommerce=1
  - `TechButton`: Art/Interface/Buttons/Religions/Order.dds
  - `GenericTechButton`: Art/Interface/Buttons/Religions/Order.dds
  - `Alignment`: 善良
  - `AlignmentBest`: 善良
  - `AlignmentWorst`: 善良

### Octopus Overlords - 深海の旧支配者

- 内部名: `RELIGION_OCTOPUS_OVERLORDS`
- 創始テクノロジー: 深海からの神託
- その他の設定:
  - `FreeUnitClass`: TXT_KEY_UNIT_DISCIPLE
  - `iFreeUnits`: 1
  - `iSpreadFactor`: 75
  - `GlobalReligionCommerces`: iGlobalReligionCommerce=1
  - `HolyCityCommerces`: iHolyCityCommerce=2
  - `StateReligionCommerces`: iStateReligionCommerce=2
  - `TechButton`: Art/Interface/Buttons/Religions/Overlords.dds
  - `GenericTechButton`: Art/Interface/Buttons/Religions/Overlords.dds
  - `iGlobalCounterFound`: 3
  - `Alignment`: 邪悪
  - `AlignmentBest`: 中立
  - `AlignmentWorst`: 邪悪

### Runes of Kilmorph - キルモフのルーン

- 内部名: `RELIGION_RUNES_OF_KILMORPH`
- 創始テクノロジー: 母なる大地への道
- その他の設定:
  - `FreeUnitClass`: TXT_KEY_UNIT_DISCIPLE
  - `iFreeUnits`: 1
  - `iSpreadFactor`: 100
  - `GlobalReligionCommerces`: iGlobalReligionCommerce=1
  - `HolyCityCommerces`: iHolyCityCommerce=2 / iHolyCityCommerce=2
  - `StateReligionCommerces`: iStateReligionCommerce=1
  - `TechButton`: Art/Interface/Buttons/Religions/Runes.dds
  - `GenericTechButton`: Art/Interface/Buttons/Religions/Runes.dds
  - `Alignment`: 善良
  - `AlignmentBest`: 善良
  - `AlignmentWorst`: 中立

### Ashen Veil - 蒼褪めたヴェール

- 内部名: `RELIGION_THE_ASHEN_VEIL`
- 創始テクノロジー: 魂の堕落
- その他の設定:
  - `FreeUnitClass`: TXT_KEY_UNIT_DISCIPLE
  - `iFreeUnits`: 1
  - `iSpreadFactor`: 150
  - `GlobalReligionCommerces`: iGlobalReligionCommerce=1
  - `HolyCityCommerces`: iHolyCityCommerce=2 / iHolyCityCommerce=2
  - `StateReligionCommerces`: iStateReligionCommerce=1
  - `TechButton`: Art/Interface/Buttons/Religions/Ashen.dds
  - `GenericTechButton`: Art/Interface/Buttons/Religions/Ashen.dds
  - `iGlobalCounterFound`: 6
  - `iGlobalCounterSpread`: 1
  - `Alignment`: 邪悪
  - `AlignmentBest`: 邪悪
  - `AlignmentWorst`: 邪悪

### Empyrean - 至光なる天空

- 内部名: `RELIGION_THE_EMPYREAN`
- 創始テクノロジー: 名誉
- その他の設定:
  - `FreeUnitClass`: TXT_KEY_UNIT_DISCIPLE
  - `iFreeUnits`: 1
  - `iSpreadFactor`: 100
  - `GlobalReligionCommerces`: iGlobalReligionCommerce=1
  - `HolyCityCommerces`: iHolyCityCommerce=4
  - `StateReligionCommerces`: iStateReligionCommerce=1
  - `TechButton`: Art/Interface/Buttons/Religions/Empyrean.dds
  - `GenericTechButton`: Art/Interface/Buttons/Religions/Empyrean.dds
  - `Alignment`: 善良
  - `AlignmentBest`: 善良
  - `AlignmentWorst`: 中立

### Council of Esus - エススの枢密院

- 内部名: `RELIGION_COUNCIL_OF_ESUS`
- 創始テクノロジー: 詐欺
- その他の設定:
  - `FreeUnitClass`: 夜警隊
  - `iFreeUnits`: 1
  - `iSpreadFactor`: 100
  - `GlobalReligionCommerces`: iGlobalReligionCommerce=1
  - `HolyCityCommerces`: iHolyCityCommerce=4
  - `StateReligionCommerces`: iStateReligionCommerce=1
  - `TechButton`: Art/Interface/Buttons/Religions/Council of Esus.dds
  - `GenericTechButton`: Art/Interface/Buttons/Religions/Council of Esus.dds
  - `bHidden`: 1
  - `bSneakAttack`: 1
  - `bUpdateSight`: 1
  - `Alignment`: 邪悪
  - `AlignmentBest`: 中立
  - `AlignmentWorst`: 邪悪

### Cult of the Dragon - ドラゴン崇拝

- 内部名: `RELIGION_CULT_OF_THE_DRAGON`
- 創始テクノロジー: Never
- その他の設定:
  - `iSpreadFactor`: 260
  - `GlobalReligionCommerces`: iGlobalReligionCommerce=1
  - `HolyCityCommerces`: iHolyCityCommerce=1 / iHolyCityCommerce=3
  - `TechButton`: Art_Kaijin/Interface/Buttons/Religions/cultofthedragon.dds
  - `GenericTechButton`: Art_Kaijin/Interface/Buttons/Religions/cultofthedragon.dds
  - `Alignment`: 中立
  - `AlignmentBest`: 善良
  - `AlignmentWorst`: 邪悪
