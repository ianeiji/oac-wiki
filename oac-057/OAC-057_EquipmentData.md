# OAC/装備品（0.57、XMLから生成）

- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）
- 生成元: `Gameinfo/CIV4EquipmentInfos.xml`
- 読み方: 主要な項目は日本語ラベル付きで先頭に、それ以外の既定値でない設定は「その他の設定」にXMLのタグ名のまま列挙する。値の内部名は日本語名に置き換えている。Pythonで実装された効果はXMLにないため含まない（ゲーム内ヘルプの説明文があれば載せている）。

### Athame - アセイミー

- 内部名: `EQUIPMENT_ATHAME`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_ATHAME
  - `EquipmentUnit`: UNIT_ATHAME
  - `EquipmentPromotion`: PROMOTION_ATHAME
  - `PromotionCombatApply`: 疫病
  - `DamageTypeCombats`: 毒 iCombat=3

### Black Mirror - 黒の鏡

- 内部名: `EQUIPMENT_BLACK_MIRROR`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_BLACK_MIRROR
  - `EquipmentUnit`: UNIT_BLACK_MIRROR
  - `EquipmentPromotion`: PROMOTION_BLACK_MIRROR

### Crown of Akharien - アハリエンの宝冠

- 内部名: `EQUIPMENT_CROWN_OF_AKHARIEN`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_CROWN_OF_AKHARIEN
  - `EquipmentUnit`: UNIT_CROWN_OF_AKHARIEN
  - `EquipmentBuilding`: アハリエンの宝冠
  - `EquipmentPromotion`: PROMOTION_CROWN_OF_AKHARIEN
  - `bImmuneToMagic`: 1

### Crown of Command - 折伏の王冠

- 内部名: `EQUIPMENT_CROWN_OF_COMMAND`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_CROWN_OF_COMMAND
  - `EquipmentUnit`: UNIT_CROWN_OF_COMMAND
  - `EquipmentPromotion`: PROMOTION_CROWN_OF_COMMAND
  - `iCombatCapturePercent`: 30

### The Dragon's Hoard - 竜の財宝

- 内部名: `EQUIPMENT_DRAGONS_HORDE`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_DRAGONS_HORDE
  - `EquipmentUnit`: UNIT_DRAGONS_HORDE
  - `EquipmentBuilding`: 竜の財宝
  - `EquipmentPromotion`: PROMOTION_DRAGONS_HORDE

### Empty Bier - 骸なき棺台

- 内部名: `EQUIPMENT_EMPTY_BIER`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_EMPTY_BIER
  - `EquipmentUnit`: UNIT_EMPTY_BIER
  - `EquipmentPromotion`: PROMOTION_EMPTY_BIER
  - `bDoubleFortifyBonus`: 1
  - `iExtraCombatDefense`: 2

### Gela - ゲラ

- 内部名: `EQUIPMENT_GELA`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_GELA
  - `EquipmentUnit`: UNIT_GELA
  - `EquipmentPromotion`: PROMOTION_GELA
  - `bBlitz`: 1
  - `DamageTypeCombats`: 不浄 iCombat=2

### Godslayer - ゴッドスレイヤー

- 内部名: `EQUIPMENT_GODSLAYER`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_GODSLAYER
  - `EquipmentUnit`: UNIT_GODSLAYER
  - `EquipmentPromotion`: PROMOTION_GODSLAYER
  - `iExtraCombatAttack`: 3
  - `iExtraCombatDefense`: 3
  - `iResistMagic`: 100
  - `iGroupSize`: 1
  - `PromotionCombatType`: 化身
  - `iPromotionCombatMod`: 1000
  - `DamageTypeResists`: 冷気 iResist=100 / 死 iResist=100 / 火炎 iResist=100 / 神聖 iResist=100 / 電撃 iResist=100 / 毒 iResist=100 / 不浄 iResist=100

### Golden Hammer - ゴールデンハンマー

- 内部名: `EQUIPMENT_GOLDEN_HAMMER`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_GOLDEN_HAMMER
  - `EquipmentUnit`: UNIT_GOLDEN_HAMMER
  - `EquipmentPromotion`: PROMOTION_GOLDEN_HAMMER
  - `iExtraCombatAttack`: 1

### Healing Salve - 治癒の軟膏

- 内部名: `EQUIPMENT_HEALING_SALVE`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_HEALING_SALVE
  - `EquipmentUnit`: UNIT_HEALING_SALVE
  - `EquipmentPromotion`: PROMOTION_HEALING_SALVE

### Infernal Grimoire - 地獄全書

- 内部名: `EQUIPMENT_INFERNAL_GRIMOIRE`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_INFERNAL_GRIMOIRE
  - `EquipmentUnit`: UNIT_INFERNAL_GRIMOIRE
  - `EquipmentBuilding`: 地獄全書
  - `EquipmentPromotion`: PROMOTION_INFERNAL_GRIMOIRE

### Jade Torc - 翡翠の腕輪

- 内部名: `EQUIPMENT_JADE_TORC`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_JADE_TORC
  - `EquipmentUnit`: UNIT_JADE_TORC
  - `EquipmentPromotion`: PROMOTION_JADE_TORC
  - `iResistMagic`: 20
  - `DamageTypeResists`: 毒 iResist=100

### Mokka's Cauldron - モッカの大釜

- 内部名: `EQUIPMENT_MOKKAS_CAULDRON`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_MOKKAS_CAULDRON
  - `EquipmentUnit`: UNIT_MOKKAS_CAULDRON
  - `EquipmentBuilding`: モッカの大釜
  - `EquipmentPromotion`: PROMOTION_MOKKAS_CAULDRON

### Nether Blade - ネザーブレイド

- 内部名: `EQUIPMENT_NETHER_BLADE`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_NETHER_BLADE
  - `EquipmentUnit`: UNIT_NETHER_BLADE
  - `EquipmentPromotion`: PROMOTION_NETHER_BLADE
  - `bKillImmortal`: 1
  - `PromotionCombatType`: 英雄
  - `iPromotionCombatMod`: 80
  - `DamageTypeCombats`: 死 iCombat=2

### Orthus's Axe - オルタスの斧

- 内部名: `EQUIPMENT_ORTHUSS_AXE`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_ORTHUSS_AXE
  - `EquipmentUnit`: UNIT_ORTHUSS_AXE
  - `EquipmentPromotion`: PROMOTION_ORTHUSS_AXE
  - `bBlitz`: 1
  - `DamageTypeCombats`: 火炎 iCombat=1

### Pieces of Barnaxus - バルナクサスのかけら

- 内部名: `EQUIPMENT_PIECES_OF_BARNAXUS`
- 説明（ゲーム内ヘルプ）: ルシュイアープの都市に帰還するとバルナクサスが復活
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_PIECES_OF_BARNAXUS
  - `EquipmentUnit`: UNIT_PIECES_OF_BARNAXUS
  - `EquipmentPromotion`: PROMOTION_PIECES_OF_BARNAXUS

### Potion of Invisibility - 透明化の飲み薬

- 内部名: `EQUIPMENT_POTION_OF_INVISIBILITY`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_POTION_OF_INVISIBILITY
  - `EquipmentUnit`: UNIT_POTION_OF_INVISIBILITY
  - `EquipmentPromotion`: PROMOTION_POTION_OF_INVISIBILITY

### Potion of Restoration - 魔力回復の飲み薬

- 内部名: `EQUIPMENT_POTION_OF_RESTORATION`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_POTION_OF_RESTORATION
  - `EquipmentUnit`: UNIT_POTION_OF_RESTORATION
  - `EquipmentPromotion`: PROMOTION_POTION_OF_RESTORATION

### Rod of Winds - 風のロッド

- 内部名: `EQUIPMENT_ROD_OF_WINDS`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_ROD_OF_WINDS
  - `EquipmentUnit`: UNIT_ROD_OF_WINDS
  - `EquipmentPromotion`: PROMOTION_ROD_OF_WINDS
  - `BonusAffinityType`: 大気のマナ
  - `iBonusAffinityTimes100`: 100

### Scorched Staff - 焦熱の杖

- 内部名: `EQUIPMENT_SCORCHED_STAFF`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_SCORCHED_STAFF
  - `EquipmentUnit`: UNIT_SCORCHED_STAFF
  - `EquipmentPromotion`: PROMOTION_SCORCHED_STAFF
  - `BonusAffinityType`: 炎のマナ
  - `iBonusAffinityTimes100`: 100

### Staff of Souls - 霊魂の杖

- 内部名: `EQUIPMENT_STAFF_OF_SOULS`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_STAFF_OF_SOULS
  - `EquipmentUnit`: UNIT_STAFF_OF_SOULS
  - `EquipmentPromotion`: PROMOTION_STAFF_OF_SOULS
  - `DamageTypeCombats`: 死 iCombat=3
  - `BonusAffinityType`: 死のマナ
  - `iBonusAffinityTimes100`: 100

### Syliven's Perfect Lyre - シリヴェンの完璧なる竪琴

- 内部名: `EQUIPMENT_SYLIVENS_PERFECT_LYRE`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_SYLIVENS_PERFECT_LYRE
  - `EquipmentUnit`: UNIT_SYLIVENS_PERFECT_LYRE
  - `EquipmentBuilding`: シリヴェンの完璧なる竪琴
  - `EquipmentPromotion`: PROMOTION_SYLIVENS_PERFECT_LYRE

### Timor Mask - ティモールの仮面

- 内部名: `EQUIPMENT_TIMOR_MASK`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_TIMOR_MASK
  - `EquipmentUnit`: UNIT_TIMOR_MASK
  - `EquipmentPromotion`: PROMOTION_TIMOR_MASK
  - `bFear`: 1
  - `bImmuneToFear`: 1

### War - いくさ丸

- 内部名: `EQUIPMENT_WAR`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_WAR
  - `EquipmentUnit`: UNIT_WAR
  - `EquipmentPromotion`: PROMOTION_WAR
  - `iModifyGlobalCounterOnCombat`: 1
  - `DamageTypeCombats`: 不浄 iCombat=3

### Muramasa - ムラマサ

- 内部名: `EQUIPMENT_MURAMASA_BLADE_ECHIGO`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_MURAMASA_BLADE_ECHIGO
  - `EquipmentUnit`: UNIT_MURAMASA_BLADE_ECHIGO
  - `EquipmentPromotion`: ムラマサ
  - `bBlitz`: 1
  - `iExtraCombatAttack`: 2
  - `iExtraCombatDefense`: 2
  - `BonusAffinityType`: 呪付のマナ
  - `iBonusAffinityTimes100`: 100

### Dark Blade - 常闇ノ刃

- 内部名: `EQUIPMENT_DARK_BLADE`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_DARK_BLADE
  - `EquipmentUnit`: UNIT_DARK_BLADE
  - `EquipmentPromotion`: PROMOTION_DARK_BLADE
  - `bImmuneToFear`: 1
  - `iExtraCombatAttack`: 1
  - `iExtraCombatDefense`: 1
  - `PromotionCombatType`: 魔族
  - `iPromotionCombatMod`: 100

### Earth Pulse - 地脈の戦槌

- 内部名: `EQUIPMENT_EARTH_PULSE`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_EARTH_PULSE
  - `EquipmentUnit`: UNIT_EARTH_PULSE
  - `EquipmentBuilding`: 地脈の戦槌
  - `EquipmentPromotion`: 地脈の戦槌

### Glorious Shield - 栄光の盾

- 内部名: `EQUIPMENT_GLORIOUS_SHIELD`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_GLORIOUS_SHIELD
  - `EquipmentUnit`: UNIT_GLORIOUS_SHIELD
  - `EquipmentBuilding`: 栄光の盾
  - `EquipmentPromotion`: 栄光の盾

### Bracelet of Nightmare - 夢魔の腕輪

- 内部名: `EQUIPMENT_BRACELET_OF_NIGHTMARE`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_BRACELET_OF_NIGHTMARE
  - `EquipmentUnit`: UNIT_BRACELET_OF_NIGHTMARE
  - `EquipmentBuilding`: 夢魔の腕輪
  - `EquipmentPromotion`: 夢魔の腕輪

### Orb of Yggdrasil - 世界樹の宝珠

- 内部名: `EQUIPMENT_ORB_OF_YGGFRASIL`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_ORB_OF_YGGFRASIL
  - `EquipmentUnit`: UNIT_ORB_OF_YGGFRASIL
  - `EquipmentBuilding`: 世界樹の宝珠
  - `EquipmentPromotion`: 世界樹の宝珠

### Demon's Fang - 悪魔の牙

- 内部名: `EQUIPMENT_DEMONS_FANG`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_DEMONS_FANG
  - `EquipmentUnit`: UNIT_DEMONS_FANG
  - `EquipmentBuilding`: 悪魔の牙
  - `EquipmentPromotion`: 悪魔の牙

### Ring of the Sun - 太陽の指輪

- 内部名: `EQUIPMENT_RING_OF_THE_SUN`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_RING_OF_THE_SUN
  - `EquipmentUnit`: UNIT_RING_OF_THE_SUN
  - `EquipmentBuilding`: 太陽の指輪
  - `EquipmentPromotion`: 太陽の指輪

### Bloody Oath - 血塗れた誓いの剣

- 内部名: `EQUIPMENT_BLOODY_OATH`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_BLOODY_OATH
  - `EquipmentUnit`: UNIT_BLOODY_OATH
  - `EquipmentBuilding`: 血塗れた誓いの剣
  - `EquipmentPromotion`: 血塗れた誓いの剣

### Kurikara - 倶利伽羅剣

- 内部名: `EQUIPMENT_KURIKARA`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_GLUTTONY
  - `EquipmentUnit`: UNIT_GLUTTONY
  - `EquipmentPromotion`: 倶利伽羅剣
  - `bDoubleFortifyBonus`: 1
  - `iExtraCombatDefense`: 1

### TXT_KEY_EQUIPMENT_PIKE_OF_TEARS - TXT_KEY_EQUIPMENT_PIKE_OF_TEARS

- 内部名: `EQUIPMENT_PIKE_OF_TEARS`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_PIKE_OF_TEARS
  - `EquipmentUnit`: UNIT_PIKE_OF_TEARS
  - `EquipmentPromotion`: TXT_KEY_EQUIPMENT_PIKE_OF_TEARS
  - `bBlitz`: 1
  - `BonusAffinityType`: 水のマナ
  - `iBonusAffinityTimes100`: 100

### TXT_KEY_EQUIPMENT_SOL - TXT_KEY_EQUIPMENT_SOL

- 内部名: `EQUIPMENT_SOL`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_SOL
  - `EquipmentUnit`: UNIT_SOL
  - `EquipmentPromotion`: PROMOTION_SOL
  - `bBlitz`: 1
  - `DamageTypeCombats`: 神聖 iCombat=2
  - `BonusAffinityType`: 太陽のマナ
  - `iBonusAffinityTimes100`: 100

### TXT_KEY_EQUIPMENT_FROZEN_FLAME - TXT_KEY_EQUIPMENT_FROZEN_FLAME

- 内部名: `EQUIPMENT_FROZEN_FLAME`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_FROZEN_FLAME
  - `EquipmentUnit`: UNIT_FROZEN_FLAME
  - `EquipmentBuilding`: TXT_KEY_EQUIPMENT_FROZEN_FLAME
  - `EquipmentPromotion`: PROMOTION_FROZEN_FLAME

### Mutation Potion - 突然変異の秘薬

- 内部名: `EQUIPMENT_MUTATION_POTION`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_MUTATION_POTION
  - `EquipmentUnit`: UNIT_MUTATION_POTION
  - `EquipmentPromotion`: PROMOTION_MUTATION_POTION

### Heart Amulet - ハートの魔よけ

- 内部名: `EQUIPMENT_HEART_AMULET`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_HEART_AMULET
  - `EquipmentUnit`: UNIT_HEART_AMULET
  - `EquipmentPromotion`: ハートの魔よけ

### Swift Boots - 早駆けブーツ

- 内部名: `EQUIPMENT_SWIFT_BOOTS`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_SWIFT_BOOTS
  - `EquipmentUnit`: UNIT_SWIFT_BOOTS
  - `EquipmentPromotion`: 早駆けブーツ

### Travellers Cloak - 旅行者の外套

- 内部名: `EQUIPMENT_TRAVELLERS_CLOAK`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_TRAVELLERS_CLOAK
  - `EquipmentUnit`: UNIT_TRAVELLERS_CLOAK
  - `EquipmentPromotion`: 旅行者の外套

### Ring of Perception - 知覚の指輪

- 内部名: `EQUIPMENT_RING_OF_PERCEPTION`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_RING_OF_PERCEPTION
  - `EquipmentUnit`: UNIT_RING_OF_PERCEPTION
  - `EquipmentPromotion`: 知覚の指輪

### Ring of Striking - 打撃の指輪

- 内部名: `EQUIPMENT_RING_OF_STRIKING`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_RING_OF_STRIKING
  - `EquipmentUnit`: UNIT_RING_OF_STRIKING
  - `EquipmentPromotion`: 打撃の指輪

### Compelling Jewel - 強制の宝石

- 内部名: `EQUIPMENT_COMPELLING_JEWEL`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_COMPELLING_JEWEL
  - `EquipmentUnit`: UNIT_COMPELLING_JEWEL
  - `EquipmentPromotion`: PROMOTION_COMPELLING_JEWEL
  - `iCombatCapturePercent`: 20

### Cursed Token of Ragnarok - ラグナロクの呪われし証

- 内部名: `EQUIPMENT_CURSED_TOKEN_OF_RAGNAROK`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_CURSED_TOKEN_OF_RAGNAROK
  - `EquipmentUnit`: ラグナロクの呪われし証
  - `EquipmentPromotion`: ラグナロクの呪われし証
  - `iModifyGlobalCounterOnCombat`: 10

### Starvation Helm - 飢餓の兜

- 内部名: `EQUIPMENT_STARVATION_HELM`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_STARVATION_HELM
  - `EquipmentUnit`: UNIT_STARVATION_HELM
  - `EquipmentPromotion`: 飢餓の兜
  - `bFear`: 1
  - `bImmuneToFear`: 1

### Hauberk of Abjuration - 拒絶の鎖帷子

- 内部名: `EQUIPMENT_HAUBERK_OF_ABJURATION`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_HAUBERK_OF_ABJURATION
  - `EquipmentUnit`: UNIT_HAUBERK_OF_ABJURATION
  - `EquipmentPromotion`: PROMOTION_HAUBERK_OF_ABJURATION
  - `bImmuneToMagic`: 1

### Bug Da Rake - バグ・ダ・ラケー

- 内部名: `EQUIPMENT_BUG_DA_RAKE`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_BUG_DA_RAKE
  - `EquipmentUnit`: UNIT_BUG_DA_RAKE
  - `EquipmentPromotion`: PROMOTION_BUG_DA_RAKE
  - `DamageTypeCombats`: 毒 iCombat=1

### Wind shield - 風の盾

- 内部名: `EQUIPMENT_WIND_SHIELD`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_WIND_SHIELD
  - `EquipmentUnit`: UNIT_WIND_SHIELD
  - `EquipmentPromotion`: 風の盾

### Winchester - ウィンチェスター

- 内部名: `EQUIPMENT_WINCHESTAR`
- その他の設定:
  - `EquipmentUnitClass`: UNITCLASS_WINCHESTAR
  - `EquipmentUnit`: UNIT_WINCHESTAR
  - `EquipmentPromotion`: ウィンチェスター
