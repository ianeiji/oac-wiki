# OAC/専門家（0.57、XMLから生成）

- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）
- 生成元: `Gameinfo/CIV4SpecialistInfos.xml`
- 読み方: 主要な項目は日本語ラベル付きで先頭に、それ以外の既定値でない設定は「その他の設定」にXMLのタグ名のまま列挙する。値の内部名は日本語名に置き換えている。Pythonで実装された効果はXMLにないため含まない（ゲーム内ヘルプの説明文があれば載せている）。

### Citizen - 特別市民

- 内部名: `SPECIALIST_CITIZEN`
- 産出: +1[ハンマー]
- その他の設定:
  - `Texture`: Art/Interface/MainScreen/CityScreen/Citizen.dds

### Great Priest - 神官

- 内部名: `SPECIALIST_PRIEST`
- 産出: +1[ハンマー]
- 産出(商業系): 1[ゴールド]
- 偉人: 偉大な預言者
- 偉人ポイント: 3
- その他の設定:
  - `Texture`: Art/Interface/MainScreen/CityScreen/Priest.dds

### Bard - 吟遊詩人

- 内部名: `SPECIALIST_ARTIST`
- 産出(商業系): 1[研究], 4[文化]
- 偉人: 偉大な吟遊詩人
- 偉人ポイント: 3
- その他の設定:
  - `Texture`: Art/Interface/MainScreen/CityScreen/Artist.dds

### Sage - 賢者

- 内部名: `SPECIALIST_SCIENTIST`
- 産出(商業系): 3[研究]
- 偉人: 偉大な賢者
- 偉人ポイント: 3
- その他の設定:
  - `Texture`: Art/Interface/MainScreen/CityScreen/scientist.dds

### Merchant - 商人

- 内部名: `SPECIALIST_MERCHANT`
- 産出(商業系): 3[ゴールド]
- 偉人: 偉大な商人
- 偉人ポイント: 3
- その他の設定:
  - `Texture`: Art/Interface/MainScreen/CityScreen/merchant.dds

### Engineer - 技師

- 内部名: `SPECIALIST_ENGINEER`
- 産出: +2[ハンマー]
- 偉人: 偉大な技師
- 偉人ポイント: 3
- その他の設定:
  - `Texture`: Art/Interface/MainScreen/CityScreen/engineer.dds

### Great Priest - 偉大な神官

- 内部名: `SPECIALIST_GREAT_PRIEST`
- 産出: +2[ハンマー]
- 産出(商業系): 5[ゴールド]
- その他の設定:
  - `Texture`: Art/Interface/MainScreen/CityScreen/Great_Priest.dds

### Great Bard - 偉大な吟遊詩人

- 内部名: `SPECIALIST_GREAT_ARTIST`
- 産出(商業系): 3[ゴールド], 12[文化]
- その他の設定:
  - `Texture`: Art/Interface/MainScreen/CityScreen/Great_Artist.dds
  - `iHappiness`: 3

### Great Sage - 偉大な賢者

- 内部名: `SPECIALIST_GREAT_SCIENTIST`
- 産出: +1[ハンマー]
- 産出(商業系): 6[研究]
- その他の設定:
  - `Texture`: Art/Interface/MainScreen/CityScreen/Great_Scientist.dds

### Great Merchant - 偉大な商人

- 内部名: `SPECIALIST_GREAT_MERCHANT`
- 産出: +1[食料]
- 産出(商業系): 6[ゴールド]
- その他の設定:
  - `Texture`: Art/Interface/MainScreen/CityScreen/Great_Merchant.dds

### Great Engineer - 偉大な技師

- 内部名: `SPECIALIST_GREAT_ENGINEER`
- 産出: +3[ハンマー]
- 産出(商業系): 3[研究]
- その他の設定:
  - `Texture`: Art/Interface/MainScreen/CityScreen/Great_Engineer.dds

### Great Military Instructor - 大軍事教官

- 内部名: `SPECIALIST_GREAT_GENERAL`
- 産出: +1[ハンマー]
- 偉人: 偉大な指揮官
- 偉人ポイント: 3
- その他の設定:
  - `Texture`: ,Art/Interface/MainScreen/CityScreen/Great_Engineer.dds,Art/Interface/Buttons/Warlords_Atlas_2.dds,2,6
  - `iExperience`: 3
