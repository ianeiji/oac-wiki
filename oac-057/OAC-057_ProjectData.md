# OAC/大儀式（0.57、XMLから生成）

- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）
- 生成元: `Gameinfo/CIV4ProjectInfo.xml`
- 読み方: 主要な項目は日本語ラベル付きで先頭に、それ以外の既定値でない設定は「その他の設定」にXMLのタグ名のまま列挙する。値の内部名は日本語名に置き換えている。Pythonで実装された効果はXMLにないため含まない（ゲーム内ヘルプの説明文があれば載せている）。

### Bane Divine - 神々の破滅

- 内部名: `PROJECT_BANE_DIVINE`
- 必要テクノロジー: 悪意の企み
- コスト[ハンマー]: 1000
- その他の設定:
  - `iMaxGlobalInstances`: 1
  - `BonusProductionModifiers`: 死のマナ iProductonModifier=100 / 不可逆のマナ iProductonModifier=100
  - `iPrereqGlobalCounter`: 70

### Blood of the Phoenix - 不死鳥の血

- 内部名: `PROJECT_BLOOD_OF_THE_PHOENIX`
- 必要テクノロジー: 神々の本質
- コスト[ハンマー]: 1000
- その他の設定:
  - `iMaxGlobalInstances`: 1
  - `BonusProductionModifiers`: 生命のマナ iProductonModifier=100

### Genesis - 創世記

- 内部名: `PROJECT_GENESIS`
- 必要テクノロジー: 自然との共生
- コスト[ハンマー]: 1000
- その他の設定:
  - `iMaxGlobalInstances`: 1
  - `BonusProductionModifiers`: 自然のマナ iProductonModifier=100

### Glory Everlasting - 不滅の栄光

- 内部名: `PROJECT_GLORY_EVERLASTING`
- 必要テクノロジー: 高潔の証
- コスト[ハンマー]: 1000
- その他の設定:
  - `iMaxGlobalInstances`: 1
  - `BonusProductionModifiers`: 法のマナ iProductonModifier=100 / 生命のマナ iProductonModifier=100
  - `iPrereqGlobalCounter`: 70

### Rites of Oghma - オグマの儀礼

- 内部名: `PROJECT_RITES_OF_OGHMA`
- 必要テクノロジー: 意志の力
- コスト[ハンマー]: 2000
- その他の設定:
  - `iMaxGlobalInstances`: 1
  - `BonusProductionModifiers`: 超魔術のマナ iProductonModifier=100

### Nature's Revolt - 自然界の逆襲

- 内部名: `PROJECT_NATURES_REVOLT`
- 必要テクノロジー: 動物の馴致
- コスト[ハンマー]: 750
- その他の設定:
  - `iMaxGlobalInstances`: 1
  - `BonusProductionModifiers`: 自然のマナ iProductonModifier=100

### Elegy of the Sheaim - シェアイムの挽歌

- 内部名: `PROJECT_ELEGY_OF_THE_SHEAIM`
- 必要テクノロジー: 邪悪への道
- コスト[ハンマー]: 120
- 必要な文明: シェアイム
- その他の設定:
  - `iModifyGlobalCounter`: 3

### Hallowing of the Elohim - エロヒムの聖別

- 内部名: `PROJECT_HALLOWING_OF_THE_ELOHIM`
- 必要テクノロジー: 叡智への道
- コスト[ハンマー]: 120
- 必要な文明: エロヒム
- その他の設定:
  - `iPrereqGlobalCounter`: 1
  - `iModifyGlobalCounter`: -3

### Purge the Unfaithful - 異教の粛清

- 内部名: `PROJECT_PURGE_THE_UNFAITHFUL`
- 必要テクノロジー: 聖職
- コスト[ハンマー]: 300
- その他の設定:
  - `iMaxGlobalInstances`: 1
  - `iModifyGlobalCounter`: 6

### Birthright Regained - 天恵復古

- 内部名: `PROJECT_BIRTHRIGHT_REGAINED`
- 必要テクノロジー: 全知
- コスト[ハンマー]: 700
- その他の設定:
  - `iMaxGlobalInstances`: 1

### Samhain - サウィン祭

- 内部名: `PROJECT_SAMHAIN`
- 必要テクノロジー: 神秘主義
- コスト[ハンマー]: 250
- 必要な文明: イリアン
- その他の設定:
  - `iMaxGlobalInstances`: 1

### The White Hand - 白き御手

- 内部名: `PROJECT_THE_WHITE_HAND`
- 必要テクノロジー: 聖職
- コスト[ハンマー]: 400
- 必要な文明: イリアン
- その他の設定:
  - `iMaxGlobalInstances`: 1

### The Deepening - 冬将軍

- 内部名: `PROJECT_THE_DEEPENING`
- 必要テクノロジー: 聖職
- コスト[ハンマー]: 1200
- 必要な文明: イリアン
- その他の設定:
  - `iMaxGlobalInstances`: 1

### Stir from Slumber - 微睡みからの目覚め

- 内部名: `PROJECT_STIR_FROM_SLUMBER`
- 必要テクノロジー: 意志の力
- コスト[ハンマー]: 2000
- 必要な文明: イリアン
- その他の設定:
  - `iMaxGlobalInstances`: 1

### The Draw - 冬至

- 内部名: `PROJECT_THE_DRAW`
- 必要テクノロジー: 意志の力
- コスト[ハンマー]: 1500
- 必要な文明: イリアン
- その他の設定:
  - `iMaxGlobalInstances`: 1
  - `iModifyGlobalCounter`: 15

### Ascension - 昇神

- 内部名: `PROJECT_ASCENSION`
- 必要テクノロジー: 全知
- コスト[ハンマー]: 2500
- 必要な文明: イリアン
- その他の設定:
  - `AnyonePrereqProject`: 冬至
  - `iMaxGlobalInstances`: 1

### Pact of the Nilhorn - ニルホーン条約

- 内部名: `PROJECT_PACT_OF_THE_NILHORN`
- 必要テクノロジー: 地図
- コスト[ハンマー]: 150
- その他の設定:
  - `iMaxGlobalInstances`: 1

### Secret of Evolution - 進化の秘法

- 内部名: `PROJECT_SECRET_OF_EVOLUTION_DROAUM`
- 必要テクノロジー: 聖職
- コスト[ハンマー]: 300
- 必要な文明: ドロアウム
- その他の設定:
  - `iMaxTeamInstances`: 1

### Life of the immortal - 不定の生命

- 内部名: `PROJECT_LIFE_OF_THE_IMMORTAL`
- 必要テクノロジー: 神々の本質
- コスト[ハンマー]: 1500
- 必要な文明: デスピエル
- その他の設定:
  - `iMaxGlobalInstances`: 1
  - `iModifyGlobalCounter`: 10

### Spread corruption - 拡散する堕落

- 内部名: `PROJECT_SPREAD_CORRUPTION`
- 必要テクノロジー: 哲学
- コスト[ハンマー]: 200
- 必要な文明: ラーナ
- その他の設定:
  - `iMaxGlobalInstances`: 1

### Fire inheritance - 火の継承

- 内部名: `PROJECT_FIRE_INHERITANCE`
- 必要テクノロジー: 狂信
- コスト[ハンマー]: 300
- 必要な文明: ラーナ
- その他の設定:
  - `AnyonePrereqProject`: 拡散する堕落
  - `iMaxGlobalInstances`: 1

### Princess of Darkness - 闇の王女

- 内部名: `PROJECT_PRINCESS_OF_DARKNESS`
- 必要テクノロジー: 悪意の企み
- コスト[ハンマー]: 450
- 必要な文明: ラーナ
- その他の設定:
  - `AnyonePrereqProject`: 火の継承
  - `iMaxGlobalInstances`: 1

### Death Pact - 死の盟約Ⅰ

- 内部名: `PROJECT_DEATH_PACT_1`
- コスト[ハンマー]: 40
- 必要な文明: アリストラク
- その他の設定:
  - `bNoAnnounce`: 1

### Death Pact - 死の盟約Ⅱ

- 内部名: `PROJECT_DEATH_PACT_2`
- コスト[ハンマー]: 90
- 必要な文明: アリストラク
- その他の設定:
  - `bNoAnnounce`: 1

### Death Pact - 死の盟約Ⅲ

- 内部名: `PROJECT_DEATH_PACT_3`
- コスト[ハンマー]: 180
- 必要な文明: アリストラク
- その他の設定:
  - `bNoAnnounce`: 1

### Death Pact - 死の盟約Ⅳ

- 内部名: `PROJECT_DEATH_PACT_4`
- コスト[ハンマー]: 360
- 必要な文明: アリストラク
- その他の設定:
  - `bNoAnnounce`: 1

### Death Pact - 死の盟約Ⅴ

- 内部名: `PROJECT_DEATH_PACT_5`
- コスト[ハンマー]: 540
- 必要な文明: アリストラク
- その他の設定:
  - `bNoAnnounce`: 1

### Death Pact - 暗黒の儀式

- 内部名: `PROJECT_DEATH_RITUAL`
- 必要テクノロジー: 哲学
- コスト[ハンマー]: 450
- 必要な文明: アリストラク
- その他の設定:
  - `iMaxTeamInstances`: 4

### Flying to the Sky - 天空への飛翔

- 内部名: `PROJECT_FLYING_TO_THE_SKY`
- 必要テクノロジー: 工学
- コスト[ハンマー]: 200
- その他の設定:
  - `VictoryPrereq`: VICTORY_STATUE_OF_LUXURY
  - `iMaxTeamInstances`: 1
  - `VictoryThresholds`: VICTORY_STATUE_OF_LUXURY iThreshold=1
  - `BonusProductionModifiers`: 銅 iProductonModifier=100

### Statue of Luxury - Cockpit - 巨像の操舵室

- 内部名: `PROJECT_STATUE_OF_LUXURY_COCKPIT`
- 必要テクノロジー: 重商主義
- コスト[ハンマー]: 1000
- その他の設定:
  - `VictoryPrereq`: VICTORY_STATUE_OF_LUXURY
  - `iMaxTeamInstances`: 1
  - `bSpaceship`: 1
  - `PrereqProjects`: 天空への飛翔 iNeeded=1
  - `VictoryThresholds`: VICTORY_STATUE_OF_LUXURY iThreshold=1
  - `BonusProductionModifiers`: 銅 iProductonModifier=100

### Statue of Luxury - Life Support - 巨像の生命機関

- 内部名: `PROJECT_STATUE_OF_LUXURY_LIFE_SUPPORT`
- 必要テクノロジー: 機械
- コスト[ハンマー]: 1000
- その他の設定:
  - `VictoryPrereq`: VICTORY_STATUE_OF_LUXURY
  - `iMaxTeamInstances`: 1
  - `bSpaceship`: 1
  - `PrereqProjects`: 天空への飛翔 iNeeded=1
  - `VictoryThresholds`: VICTORY_STATUE_OF_LUXURY iThreshold=1
  - `BonusProductionModifiers`: 銅 iProductonModifier=100

### Statue of Luxury - Stasis Chamber - 巨像の停滞房

- 内部名: `PROJECT_STATUE_OF_LUXURY_STASIS_CHAMBER`
- 必要テクノロジー: 機械
- コスト[ハンマー]: 1200
- その他の設定:
  - `VictoryPrereq`: VICTORY_STATUE_OF_LUXURY
  - `iMaxTeamInstances`: 1
  - `bSpaceship`: 1
  - `PrereqProjects`: 天空への飛翔 iNeeded=1
  - `VictoryThresholds`: VICTORY_STATUE_OF_LUXURY iThreshold=1

### Statue of Luxury - Docking Bay - 巨像の結合機構

- 内部名: `PROJECT_STATUE_OF_LUXURY_DOCKING_BAY`
- 必要テクノロジー: ギルド
- コスト[ハンマー]: 1000
- その他の設定:
  - `VictoryPrereq`: VICTORY_STATUE_OF_LUXURY
  - `iMaxTeamInstances`: 1
  - `bSpaceship`: 1
  - `PrereqProjects`: 天空への飛翔 iNeeded=1
  - `VictoryThresholds`: VICTORY_STATUE_OF_LUXURY iThreshold=1
  - `BonusProductionModifiers`: ミスリル iProductonModifier=100

### Statue of Luxury - Engine - 巨像の動力炉

- 内部名: `PROJECT_STATUE_OF_LUXURY_ENGINE`
- 必要テクノロジー: 爆薬
- コスト[ハンマー]: 1000
- その他の設定:
  - `VictoryPrereq`: VICTORY_STATUE_OF_LUXURY
  - `iMaxTeamInstances`: 2
  - `bSpaceship`: 1
  - `PrereqProjects`: 天空への飛翔 iNeeded=1
  - `VictoryThresholds`: VICTORY_STATUE_OF_LUXURY iThreshold=2

### Statue of Luxury - Casing - 巨像の外殻

- 内部名: `PROJECT_STATUE_OF_LUXURY_CASING`
- 必要テクノロジー: 工学
- コスト[ハンマー]: 600
- その他の設定:
  - `VictoryPrereq`: VICTORY_STATUE_OF_LUXURY
  - `iMaxTeamInstances`: 5
  - `bSpaceship`: 1
  - `PrereqProjects`: 天空への飛翔 iNeeded=1
  - `VictoryThresholds`: VICTORY_STATUE_OF_LUXURY iThreshold=5
  - `iSuccessRate`: 20
  - `BonusProductionModifiers`: ミスリル iProductonModifier=100

### Statue of Luxury - Thrusters - 巨像の推進器

- 内部名: `PROJECT_STATUE_OF_LUXURY_THRUSTERS`
- 必要テクノロジー: 錬金術
- コスト[ハンマー]: 600
- その他の設定:
  - `VictoryPrereq`: VICTORY_STATUE_OF_LUXURY
  - `iMaxTeamInstances`: 5
  - `bSpaceship`: 1
  - `PrereqProjects`: 天空への飛翔 iNeeded=1
  - `VictoryThresholds`: VICTORY_STATUE_OF_LUXURY iThreshold=5
  - `BonusProductionModifiers`: ミスリル iProductonModifier=100

### Statue of Luxury - Core - 巨像の核

- 内部名: `PROJECT_STATUE_OF_LUXURY_CORE`
- 必要テクノロジー: 栄華
- コスト[ハンマー]: 3000
- その他の設定:
  - `VictoryPrereq`: VICTORY_STATUE_OF_LUXURY
  - `iMaxGlobalInstances`: 1
  - `bSpaceship`: 1
  - `PrereqProjects`: 巨像の操舵室 iNeeded=1 / 巨像の生命機関 iNeeded=1 / 巨像の停滞房 iNeeded=1 / 巨像の結合機構 iNeeded=1 / 巨像の動力炉 iNeeded=2 / 巨像の外殻 iNeeded=5 / 巨像の推進器 iNeeded=5
  - `VictoryThresholds`: VICTORY_STATUE_OF_LUXURY iThreshold=1

### May Sickness - 皐の病

- 内部名: `PROJECT_MAY_SICKNESS`
- コスト[ハンマー]: 150
- その他の設定:
  - `VictoryPrereq`: VICTORY_LED_TO_THE_END
  - `iMaxGlobalInstances`: 1
  - `BonusProductionModifiers`: 超魔術のマナ iProductonModifier=100
  - `iModifyGlobalCounter`: 2

### Black Rain - 黒い雨

- 内部名: `PROJECT_BLACK_RAIN`
- コスト[ハンマー]: 300
- その他の設定:
  - `VictoryPrereq`: VICTORY_LED_TO_THE_END
  - `iMaxGlobalInstances`: 1
  - `BonusProductionModifiers`: 不可逆のマナ iProductonModifier=100
  - `iModifyGlobalCounter`: 2

### Return Soul - 魂返し

- 内部名: `PROJECT_RETURN_SOUL`
- コスト[ハンマー]: 300
- その他の設定:
  - `VictoryPrereq`: VICTORY_LED_TO_THE_END
  - `iMaxGlobalInstances`: 1
  - `BonusProductionModifiers`: 死のマナ iProductonModifier=100
  - `iModifyGlobalCounter`: 3

### Disaster - 天地の災い

- 内部名: `PROJECT_DISASTER`
- コスト[ハンマー]: 900
- その他の設定:
  - `VictoryPrereq`: VICTORY_LED_TO_THE_END
  - `iMaxGlobalInstances`: 1
  - `BonusProductionModifiers`: 大地のマナ iProductonModifier=100 / 大気のマナ iProductonModifier=100
  - `iModifyGlobalCounter`: 3

### Festival of the Berserkers - 狂戦士の祝祭

- 内部名: `PROJECT_FESTIVAL_OF_THE_BERSERKERS`
- コスト[ハンマー]: 900
- その他の設定:
  - `VictoryPrereq`: VICTORY_LED_TO_THE_END
  - `iMaxGlobalInstances`: 1
  - `BonusProductionModifiers`: 精神のマナ iProductonModifier=100 / 魂のマナ iProductonModifier=100
  - `iModifyGlobalCounter`: 7

### Stigma the Black - 黒の烙印

- 内部名: `PROJECT_STIGMA_THE_BLACK`
- コスト[ハンマー]: 900
- その他の設定:
  - `VictoryPrereq`: VICTORY_LED_TO_THE_END
  - `iMaxGlobalInstances`: 1
  - `BonusProductionModifiers`: 死のマナ iProductonModifier=100
  - `iModifyGlobalCounter`: 15

### Dark Gate - 闇の門

- 内部名: `PROJECT_DARK_GATE`
- コスト[ハンマー]: 900
- その他の設定:
  - `VictoryPrereq`: VICTORY_LED_TO_THE_END
  - `iMaxGlobalInstances`: 1
  - `BonusProductionModifiers`: 影のマナ iProductonModifier=100
  - `iModifyGlobalCounter`: 25

### Led to the End - 終末への導き

- 内部名: `PROJECT_LED_TO_THE_END`
- コスト[ハンマー]: 3000
- その他の設定:
  - `VictoryPrereq`: VICTORY_LED_TO_THE_END
  - `iMaxGlobalInstances`: 1
  - `VictoryThresholds`: VICTORY_LED_TO_THE_END iThreshold=1
  - `iPrereqGlobalCounter`: 90

### Ether to collapse - エーテルの崩壊

- 内部名: `PROJECT_ETHER_TO_COLLAPSE`
- 必要テクノロジー: エーテル移動
- コスト[ハンマー]: 300
- その他の設定:
  - `VictoryPrereq`: VICTORY_LED_TO_THE_END
  - `iMaxGlobalInstances`: 1
  - `bAllowsNukes`: 1
  - `PrereqProjects`: 天空への飛翔 iNeeded=1
  - `BonusProductionModifiers`: 次元のマナ iProductonModifier=100
