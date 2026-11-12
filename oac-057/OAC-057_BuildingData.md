# OAC/建造物・文化遺産（0.57、XMLから生成）

- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）
- 生成元: `Buildings/CIV4BuildingInfos.xml`
- 読み方: 主要な項目は日本語ラベル付きで先頭に、それ以外の既定値でない設定は「その他の設定」にXMLのタグ名のまま列挙する。値の内部名は日本語名に置き換えている。Pythonで実装された効果はXMLにないため含まない（ゲーム内ヘルプの説明文があれば載せている）。

### Bannor Palace - バンノールの宮殿

- 内部名: `BUILDING_PALACE_BANNOR`
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 法のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 魂のマナ iBonusCount=1 / 大地のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -10
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `ImprovementFreeSpecialists`: 砦 iFreeSpecialistCount=1 / 城 iFreeSpecialistCount=1 / 城塞 iFreeSpecialistCount=1 / 要塞 iFreeSpecialistCount=1
  - `iCrime`: -10

### Malakim Palace - マラキムの宮殿

- 内部名: `BUILDING_PALACE_MALAKIM`
- 固有: マラキム（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 太陽のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 精神のマナ iBonusCount=1 / 生命のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: 10
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `StateReligionCommerces`: 1[ゴールド], 1[研究]
  - `iCrime`: -10

### Elohim Palace - エロヒムの宮殿

- 内部名: `BUILDING_PALACE_ELOHIM`
- 固有: エロヒム（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- [都市防御]: 25
- 供給する資源: 魂のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 自然のマナ iBonusCount=1 / 水のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: 20
  - `iEnemyWarWearinessModifier`: 50
  - `iBombardDefense`: 50
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Mercurian Palace - マーキュリアンの宮殿

- 内部名: `BUILDING_PALACE_MERCURIANS`
- 固有: マーキュリアン（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 生命のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 大地のマナ iBonusCount=1 / 鉄 iBonusCount=1
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 4
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -50
  - `iMilitaryProductionModifier`: 40
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `iCrime`: -10
  - `iFreePromotionPick`: 1

### Luchuirp Palace - ルシュイアープの宮殿

- 内部名: `BUILDING_PALACE_LUCHUIRP`
- 固有: ルシュイアープ（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 呪付のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 生命のマナ iBonusCount=1 / 大地のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: 10
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Kuriotate Palace - クリオテイテの宮殿

- 内部名: `BUILDING_PALACE_KURIOTATES`
- 固有: クリオテイテ（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 太陽のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 魂のマナ iBonusCount=1 / 水のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGreatPeopleRateModifier`: 20
  - `iGlobalWarWearinessModifier`: 20
  - `iGlobalHealth`: 1
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Ljosalfar Palace - リョースアールヴの宮殿

- 内部名: `BUILDING_PALACE_LJOSALFAR`
- 固有: リョースアールヴ（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 自然のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 大気のマナ iBonusCount=1 / 生命のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: 10
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Khazad Palace - カザードの宮殿

- 内部名: `BUILDING_PALACE_KHAZAD`
- 固有: カザード（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 大地のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 金 iBonusCount=1 / 法のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -10
  - `iAllCityDefense`: 20
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Sidar Palace - シダーの宮殿

- 内部名: `BUILDING_PALACE_SIDAR`
- 固有: シダー（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 魂のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 呪付のマナ iBonusCount=1 / 影のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `SpecialistYieldChanges`: 技師 +1[ハンマー] / 偉大な技師 +1[ハンマー]
  - `iCrime`: -10
  - `SpecialistCommerceChanges`: 吟遊詩人 1[文化] / 商人 1[ゴールド] / 神官 1[ゴールド] / 賢者 1[研究] / 偉大な吟遊詩人 1[文化] / 偉大な商人 1[ゴールド] / 偉大な賢者 1[研究] / 偉大な神官 1[ゴールド]

### Lanun Palace - ラヌーンの宮殿

- 内部名: `BUILDING_PALACE_LANUN`
- 固有: ラヌーン（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 水のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 混沌のマナ iBonusCount=1 / 大気のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Grigori Palace - グリゴリの宮殿

- 内部名: `BUILDING_PALACE_GRIGORI`
- 固有: グリゴリ（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 魂のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 呪付のマナ iBonusCount=1 / 水のマナ iBonusCount=1
  - `GreatPeopleUnitClass`: 冒険者
  - `iGreatPeopleRateChange`: 2
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGreatPeopleRateModifier`: 15
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Hippus Palace - ヒッパスの宮殿

- 内部名: `BUILDING_PALACE_HIPPUS`
- 固有: ヒッパス（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 馬
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 自然のマナ iBonusCount=1 / 大気のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Amurite Palace - アムリテの宮殿

- 内部名: `BUILDING_PALACE_AMURITES`
- 固有: アムリテ（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 超魔術のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 炎のマナ iBonusCount=1 / 肉体のマナ iBonusCount=1 / 精神のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Doviello Palace - ドヴィエロの宮殿

- 内部名: `BUILDING_PALACE_DOVIELLO`
- 固有: ドヴィエロ（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 混沌のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 大地のマナ iBonusCount=1 / 肉体のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -40
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Balseraphs Palace - バルセラフの宮殿

- 内部名: `BUILDING_PALACE_BALSERAPHS`
- 固有: バルセラフ（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 精神のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 混沌のマナ iBonusCount=1 / 大気のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Clan of Embers Palace - 残り火一族の宮殿

- 内部名: `BUILDING_PALACE_CLAN_OF_EMBERS`
- 固有: 残り火一族（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 炎のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 自然のマナ iBonusCount=1 / 肉体のマナ iBonusCount=1
  - `iHurryAngerModifier`: -25
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalHurryModifier`: -20
  - `iGlobalWarWearinessModifier`: -40
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Svartalfar Palace - スヴァルトアールヴの宮殿

- 内部名: `BUILDING_PALACE_SVARTALFAR`
- 固有: スヴァルトアールヴ（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 影のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 自然のマナ iBonusCount=1 / 精神のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -10
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Calabim Palace - カラビムの宮殿

- 内部名: `BUILDING_PALACE_CALABIM`
- 固有: カラビム（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 肉体のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 法のマナ iBonusCount=1 / 影のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -10
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Sheaim Palace - シェアイムの宮殿

- 内部名: `BUILDING_PALACE_SHEAIM`
- 固有: シェアイム（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 死のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 混沌のマナ iBonusCount=1 / 炎のマナ iBonusCount=1 / 次元のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -10
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Infernal Palace - 地獄の軍勢の宮殿

- 内部名: `BUILDING_PALACE_INFERNAL`
- 固有: 地獄の軍勢（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 産出[%]: +50[ハンマー]
- [都市防御]: 25
- 供給する資源: 不可逆のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 炎のマナ iBonusCount=1 / 鉄 iBonusCount=1
  - `CivicOption`: 文化制度
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -100
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `StateReligionCommerces`: 1[ゴールド], 1[研究], 1[文化]
  - `iCrime`: -10

### Illian Palace - イリアンの宮殿

- 内部名: `BUILDING_PALACE_ILLIANS`
- 固有: イリアン（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 氷のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 呪付のマナ iBonusCount=1 / 法のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Summer Palace - 夏の宮殿

- 内部名: `BUILDING_FORBIDDEN_PALACE`
- 建造物クラス: 夏の宮殿
- コスト[ハンマー]: 250
- 必要テクノロジー: 法律
- その他の設定:
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 8
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `iCrime`: -10

### Winter Palace - 冬の宮殿

- 内部名: `BUILDING_WINTER_PALACE`
- 建造物クラス: 冬の宮殿
- コスト[ハンマー]: 1200
- 必要テクノロジー: 宗教法
- 倍速の資源: 大理石 iProductonModifier=100
- 説明（ゲーム内ヘルプ）: 善良の指導者のみ
- その他の設定:
  - `bTeamShare`: 1
  - `bGovernmentCenter`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iCitiesPrereq`: 8
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 10[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `PrereqBuildingClasses`: 夏の宮殿 iNumBuildingNeeded=1
  - `ImprovementFreeSpecialists`: 町 iFreeSpecialistCount=1 / 自治区 iFreeSpecialistCount=1 / 緑葉の大地 iFreeSpecialistCount=1

### Altar of the Luonnotar - ルオンノタルの祭壇

- 内部名: `BUILDING_ALTAR_OF_THE_LUONNOTAR`
- 建造物クラス: ルオンノタルの祭壇
- 専門家枠: 神官 iSpecialistCount=1
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `UnitCombatFreeExperiences`: 信奉ユニット iExperience=2

### Altar of the Luonnotar (anointed) - ルオンノタルの祭壇（塗油）

- 内部名: `BUILDING_ALTAR_OF_THE_LUONNOTAR_ANOINTED`
- 建造物クラス: ルオンノタルの祭壇（塗油）
- 必要テクノロジー: 哲学
- 必要な建造物: ルオンノタルの祭壇
- [幸福]: 1
- 専門家枠: 神官 iSpecialistCount=1
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 3[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `UnitCombatFreeExperiences`: 信奉ユニット iExperience=4

### Altar of the Luonnotar (blessed) - ルオンノタルの祭壇（祝福）

- 内部名: `BUILDING_ALTAR_OF_THE_LUONNOTAR_BLESSED`
- 建造物クラス: ルオンノタルの祭壇（祝福）
- 必要テクノロジー: 叡智への道
- 必要な建造物: ルオンノタルの祭壇（塗油）
- 専門家枠: 神官 iSpecialistCount=1
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iGlobalHappiness`: 1
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `UnitCombatFreeExperiences`: 信奉ユニット iExperience=6
  - `SupplyPromotionProbabilities`: 祝福 iProbability=100
  - `SpecialistYieldChanges`: 神官 +1[ハンマー] / 偉大な神官 +2[ハンマー]

### Altar of the Luonnotar (consecrated) - ルオンノタルの祭壇（奉献）

- 内部名: `BUILDING_ALTAR_OF_THE_LUONNOTAR_CONSECRATED`
- 建造物クラス: ルオンノタルの祭壇（奉献）
- 必要テクノロジー: 聖職
- 必要な建造物: ルオンノタルの祭壇（祝福）
- 専門家枠: 神官 iSpecialistCount=2
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iGlobalHappiness`: 2
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 5[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `UnitCombatFreeExperiences`: 信奉ユニット iExperience=8
  - `SupplyPromotionProbabilities`: 祝福 iProbability=100
  - `SpecialistYieldChanges`: 神官 +1[ハンマー] / 偉大な神官 +2[ハンマー]

### Altar of the Luonnotar (divine) - ルオンノタルの祭壇（神授）

- 内部名: `BUILDING_ALTAR_OF_THE_LUONNOTAR_DIVINE`
- 建造物クラス: ルオンノタルの祭壇（神授）
- 必要テクノロジー: 狂信
- 必要な建造物: ルオンノタルの祭壇（奉献）
- 専門家枠: 神官 iSpecialistCount=2
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iGlobalHappiness`: 2
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 6[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `UnitCombatFreeExperiences`: 信奉ユニット iExperience=10
  - `SupplyPromotionProbabilities`: 祝福 iProbability=100
  - `SpecialistYieldChanges`: 神官 +2[ハンマー] / 偉大な神官 +3[ハンマー]

### Altar of the Luonnotar (exalted) - ルオンノタルの祭壇（高貴）

- 内部名: `BUILDING_ALTAR_OF_THE_LUONNOTAR_EXALTED`
- 建造物クラス: ルオンノタルの祭壇（高貴）
- 必要テクノロジー: 高潔の証
- 必要な建造物: ルオンノタルの祭壇（神授）
- 専門家枠: 神官 iSpecialistCount=2
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iGlobalHappiness`: 3
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 7[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `UnitCombatFreeExperiences`: 信奉ユニット iExperience=12
  - `SupplyPromotionProbabilities`: 祝福 iProbability=100
  - `SpecialistYieldChanges`: 神官 +2[ハンマー] / 偉大な神官 +3[ハンマー]

### Altar of the Luonnotar (final) - ルオンノタルの祭壇（最終）

- 内部名: `BUILDING_ALTAR_OF_THE_LUONNOTAR_FINAL`
- 建造物クラス: ルオンノタルの祭壇（最終）
- コスト[ハンマー]: 4000
- 必要テクノロジー: 神々の本質
- 必要な建造物: ルオンノタルの祭壇（高貴）
- 専門家枠: 神官 iSpecialistCount=3
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 1
  - `bGoldenAge`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iGlobalHappiness`: 3
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 8[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `UnitCombatFreeExperiences`: 信奉ユニット iExperience=14
  - `SupplyPromotionProbabilities`: 祝福 iProbability=100
  - `SpecialistYieldChanges`: 神官 +3[ハンマー] / 偉大な神官 +4[ハンマー]

### Tower of Alteration - 変成の塔

- 内部名: `BUILDING_TOWER_OF_ALTERATION`
- 建造物クラス: 変成の塔
- コスト[ハンマー]: 400
- 必要テクノロジー: 変成術
- その他の設定:
  - `PrereqAndBonuses`: 肉体のマナ / 生命のマナ / 呪付のマナ / 自然のマナ
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `iGlobalResistEnemyModify`: -20
  - `iGlobalResistModify`: 20

### Tower of Divination - 予言の塔

- 内部名: `BUILDING_TOWER_OF_DIVINATION`
- 建造物クラス: 予言の塔
- コスト[ハンマー]: 400
- 必要テクノロジー: 予言術
- その他の設定:
  - `PrereqAndBonuses`: 法のマナ / 太陽のマナ / 魂のマナ / 精神のマナ
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iFreeTechs`: 1
  - `fVisibilityPriority`: 100

### Tower of the Elements - 精霊の塔

- 内部名: `BUILDING_TOWER_OF_THE_ELEMENTS`
- 建造物クラス: 精霊の塔
- コスト[ハンマー]: 400
- 必要テクノロジー: 四大元素
- 説明（ゲーム内ヘルプ）: 配下の精霊に怪力を初期昇進として与える / 永続的な精霊ユニットを時たま喚び出す
- その他の設定:
  - `PrereqAndBonuses`: 大地のマナ / 炎のマナ / 大気のマナ / 水のマナ
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100

### Tower of Necromancy - 屍霊の塔

- 内部名: `BUILDING_TOWER_OF_NECROMANCY`
- 建造物クラス: 屍霊の塔
- コスト[ハンマー]: 400
- 必要テクノロジー: 屍霊術
- 供給する資源: 死のマナ
- 供給数: 1
- 説明（ゲーム内ヘルプ）: 配下の屍人に怪力を初期昇進として与える
- その他の設定:
  - `PrereqAndBonuses`: 混沌のマナ / 死のマナ / 不可逆のマナ / 影のマナ
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100

### Tower of Mastery - 支配の塔

- 内部名: `BUILDING_TOWER_OF_MASTERY`
- 建造物クラス: 支配の塔
- コスト[ハンマー]: 4000
- 必要テクノロジー: 全知
- その他の設定:
  - `VictoryPrereq`: VICTORY_TOWER_OF_MASTERY
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `PrereqBuildingClasses`: 変成の塔 iNumBuildingNeeded=1 / 予言の塔 iNumBuildingNeeded=1 / 屍霊の塔 iNumBuildingNeeded=1 / 精霊の塔 iNumBuildingNeeded=1

### Palisade - 防護柵

- 内部名: `BUILDING_PALISADE`
- 建造物クラス: 防護柵
- コスト[ハンマー]: 40
- 陳腐化: 蒸気機関
- 産出(商業系)[%]: 5[文化]
- [都市防御]: 25
- 倍速の志向: 防御志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 古典期
  - `MaxStartEra`: 未来
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `iAirModifier`: -25
  - `fVisibilityPriority`: 10

### Walls - 防壁

- 内部名: `BUILDING_WALLS`
- 建造物クラス: 防壁
- コスト[ハンマー]: 120
- 必要テクノロジー: 数学
- 追加で必要なテクノロジー: 石工
- 必要な建造物: 防護柵
- [都市防御]: 50
- 倍速の志向: 防御志向 iProductionTrait=100
- 倍速の資源: 石材 iProductonModifier=100
- その他の設定:
  - `FreeStartEra`: 中世
  - `HappinessTraits`: 防御志向 iHappinessTrait=1
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `iAirModifier`: -50
  - `iBombardDefense`: 25
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `bExtraSeeFrom`: 1

### Archery Range - 弓術射撃場

- 内部名: `BUILDING_ARCHERY_RANGE`
- 建造物クラス: 弓術射撃場
- コスト[ハンマー]: 50
- 必要テクノロジー: 弓術
- [都市防御]: 10
- 倍速の志向: 防御志向 iProductionTrait=100 / TXT_KEY_TRAIT_IMPERIALIST iProductionTrait=50
- 倍速の資源: 薄闇樹 iProductonModifier=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10

### Command Post - 指揮所

- 内部名: `BUILDING_COMMAND_POST`
- 建造物クラス: 指揮所
- コスト[ハンマー]: 240
- 必要テクノロジー: 軍事戦略
- 必要な建造物: 練兵場
- 必要な志向: 組織志向
- その他の設定:
  - `iMaxLatitude`: 90
  - `iMilitaryProductionModifier`: 50
  - `fVisibilityPriority`: 1
  - `DomainFreeExperiences`: DOMAIN_LAND iExperience=3
  - `PrereqBuildingClasses`: 練兵場 iNumBuildingNeeded=3

### Training Yard - 練兵場

- 内部名: `BUILDING_TRAINING_YARD`
- 建造物クラス: 練兵場
- コスト[ハンマー]: 50
- 必要テクノロジー: 青銅器
- 倍速の志向: 軍事志向 iProductionTrait=100 / TXT_KEY_TRAIT_IMPERIALIST iProductionTrait=50
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 2

### Arena - 闘技場

- 内部名: `BUILDING_ARENA`
- 固有: バルセラフ（練兵場 の代替）
- 建造物クラス: 練兵場
- コスト[ハンマー]: 50
- 必要テクノロジー: 青銅器
- 倍速の志向: 軍事志向 iProductionTrait=100 / TXT_KEY_TRAIT_IMPERIALIST iProductionTrait=50
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 2

### Sculptor's Studio - 彫刻家のアトリエ

- 内部名: `BUILDING_SCULPTORS_STUDIO`
- 固有: ルシュイアープ（練兵場 の代替）
- 建造物クラス: 練兵場
- コスト[ハンマー]: 40
- 必要テクノロジー: 石工
- 倍速の志向: 軍事志向 iProductionTrait=100 / TXT_KEY_TRAIT_IMPERIALIST iProductionTrait=50
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `BonusCommerceModifiers`: 象牙 / 大理石

### Hunting Lodge - 狩猟小屋

- 内部名: `BUILDING_HUNTING_LODGE`
- 建造物クラス: 狩猟小屋
- コスト[ハンマー]: 40
- 必要テクノロジー: 追跡術
- 倍速の志向: 警邏志向 iProductionTrait=100 / TXT_KEY_TRAIT_IMPERIALIST iProductionTrait=50
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `BonusHealthChanges`: 鹿 iHealthChange=1
  - `BonusHappinessChanges`: 毛皮 iHappinessChange=1

### Stable - 厩舎

- 内部名: `BUILDING_STABLE`
- 建造物クラス: 厩舎
- コスト[ハンマー]: 50
- 必要テクノロジー: 騎乗
- 倍速の志向: 突撃志向 iProductionTrait=100 / TXT_KEY_TRAIT_IMPERIALIST iProductionTrait=50
- その他の設定:
  - `HappinessTraits`: 迅速志向 iHappinessTrait=1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10

### Mage Guild - 魔術師ギルド

- 内部名: `BUILDING_MAGE_GUILD`
- 建造物クラス: 魔術師ギルド
- コスト[ハンマー]: 60
- 必要テクノロジー: エーテルの知識
- 産出(商業系)[%]: 5[研究]
- 倍速の志向: 秘術志向 iProductionTrait=100 / 詠唱志向 iProductionTrait=100
- その他の設定:
  - `SpecialBuildingType`: SPECIALBUILDING_MAGE_GUILD
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Grove - 鎮守の杜

- 内部名: `BUILDING_GROVE`
- 建造物クラス: 鎮守の杜
- コスト[ハンマー]: 140
- 必要テクノロジー: 野生の触れ合い
- 必要な建造物: 狩猟小屋
- [衛生]: 2
- 産出: +1[食料]
- 倍速の志向: 伝道志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Siege Workshop - 攻城兵器工廠

- 内部名: `BUILDING_SIEGE_WORKSHOP`
- 建造物クラス: 攻城兵器工廠
- コスト[ハンマー]: 90
- 必要テクノロジー: 建設
- 倍速の志向: 攻撃志向 iProductionTrait=100 / TXT_KEY_TRAIT_IMPERIALIST iProductionTrait=50
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `UnitCombatFreeExperiences`: 攻城兵器 iExperience=4

### Granary - 穀倉

- 内部名: `BUILDING_GRANARY`
- 建造物クラス: 穀倉
- コスト[ハンマー]: 100
- 必要テクノロジー: 暦
- 倍速の志向: 拡張志向 iProductionTrait=100 / 農耕志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 古典期
  - `iMaxLatitude`: 90
  - `iFoodKept`: 40
  - `fVisibilityPriority`: 10
  - `BonusHealthChanges`: トウモロコシ iHealthChange=1 / 米 iHealthChange=1 / 小麦 iHealthChange=1 / 亜麻 iHealthChange=1 / ジャガイモ iHealthChange=1

### Smokehouse - 燻製場

- 内部名: `BUILDING_SMOKEHOUSE`
- 建造物クラス: 燻製場
- コスト[ハンマー]: 100
- 必要テクノロジー: 動物の馴致
- 倍速の志向: 農耕志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 9
  - `BonusHealthChanges`: 牛 iHealthChange=1 / 豚 iHealthChange=1 / 羊 iHealthChange=1 / 鯨 iHealthChange=1
  - `BonusYieldModifiers`: 牛 / 豚 / 羊 / 鯨

### Herbalist - 薬草師

- 内部名: `BUILDING_HERBALIST`
- 建造物クラス: 薬草師
- コスト[ハンマー]: 60
- 必要テクノロジー: 農業
- [衛生]: 1
- 倍速の志向: 野戦志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 中世
  - `iMaxLatitude`: 90
  - `iHealRateChange`: 10
  - `fVisibilityPriority`: 10
  - `BonusHealthChanges`: 秘薬 iHealthChange=1 / 綿花 iHealthChange=1 / キノコ iHealthChange=1
  - `SupplyPromotionProbabilities`: 病気 iProbability=-10
  - `RemovePromotion`: 毒

### Aqueduct - 水道橋

- 内部名: `BUILDING_AQUEDUCT`
- 建造物クラス: 水道橋
- コスト[ハンマー]: 140
- 必要テクノロジー: 衛生設備
- [衛生]: 2
- 産出(商業系)[%]: 10[文化]
- 倍速の志向: 拡張志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 未来
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10240000
  - `BonusHealthChanges`: レモン iHealthChange=1 / オレンジ iHealthChange=1

### Infirmary - 診療所

- 内部名: `BUILDING_INFIRMARY`
- 建造物クラス: 診療所
- コスト[ハンマー]: 250
- 必要テクノロジー: 医薬
- 必要な建造物: 薬草師
- [衛生]: 3
- 産出(商業系)[%]: 20[研究], 20[文化]
- 倍速の志向: 野戦志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `iHealRateChange`: 25
  - `fVisibilityPriority`: 1
  - `BonusHealthChanges`: 剃刀草 iHealthChange=1
  - `SupplyPromotionProbabilities`: 病気 iProbability=-100 / 疫病 iProbability=-10 / 衰弱 iProbability=-10 / 黒死病 iProbability=-10

### Brewery - ビール醸造所

- 内部名: `BUILDING_BREWERY`
- 建造物クラス: ビール醸造所
- コスト[ハンマー]: 90
- 必要テクノロジー: 道具の作成
- 必要な資源（いずれか）: トウモロコシ / 米 / 砂糖 / 小麦
- [幸福]: 1
- 倍速の志向: カリスマ志向 iProductionTrait=100
- 説明（ゲーム内ヘルプ）: 新規のドワーフユニットに+2経験値 / 川沿い都市にのみ建設可能
- その他の設定:
  - `bRiver`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Carnival - 巡業サーカス

- 内部名: `BUILDING_CARNIVAL`
- 建造物クラス: 巡業サーカス
- コスト[ハンマー]: 100
- 必要テクノロジー: 祝祭
- 陳腐化: 蒸気機関
- [幸福]: 1
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 吟遊詩人 iSpecialistCount=1
- 倍速の志向: 創造志向 iProductionTrait=100
- その他の設定:
  - `MaxStartEra`: 未来
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `BonusHealthChanges`: 米 iHealthChange=2
  - `BonusHappinessChanges`: 米 iHappinessChange=2
  - `BonusYieldModifiers`: エール酒

### Public Baths - 公衆浴場

- 内部名: `BUILDING_PUBLIC_BATHS`
- 建造物クラス: 公衆浴場
- コスト[ハンマー]: 150
- 必要テクノロジー: 衛生設備
- [幸福]: 5
- 産出(商業系)[%]: 20[ゴールド]
- その他の設定:
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: 10
  - `fVisibilityPriority`: 1
  - `FreePromotionProbabilities`: 病気 iProbability=10
  - `iCrime`: 50

### Lighthouse - 灯台

- 内部名: `BUILDING_LIGHTHOUSE`
- 建造物クラス: 灯台
- コスト[ハンマー]: 120
- 必要テクノロジー: 航海術
- 倍速の志向: 組織志向 iProductionTrait=100 / 交易志向 iProductionTrait=100
- 倍速の資源: 石材 iProductonModifier=100
- その他の設定:
  - `FreeStartEra`: 中世
  - `bWater`: 1
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `iTradeRoutes`: 1
  - `fVisibilityPriority`: 10
  - `SeaPlotYieldChanges`: +1[食料]

### Harbor - 港

- 内部名: `BUILDING_HARBOR`
- 建造物クラス: 港
- コスト[ハンマー]: 100
- 必要テクノロジー: 帆走
- 倍速の志向: 拡張志向 iProductionTrait=100 / 交易志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 未来
  - `bWater`: 1
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `iTradeRouteModifier`: 50
  - `fVisibilityPriority`: 10
  - `BonusHealthChanges`: 貝 iHealthChange=1 / 蟹 iHealthChange=1 / 魚 iHealthChange=1 / 海老 iHealthChange=1

### Sea Haven - 避難港

- 内部名: `BUILDING_HARBOR_LANUN`
- 固有: ラヌーン（港 の代替）
- 建造物クラス: 港
- コスト[ハンマー]: 80
- 必要テクノロジー: 帆走
- 倍速の志向: 拡張志向 iProductionTrait=100 / 交易志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 未来
  - `bWater`: 1
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -10
  - `iTradeRouteModifier`: 50
  - `fVisibilityPriority`: 10
  - `BonusHealthChanges`: 貝 iHealthChange=1 / 蟹 iHealthChange=1 / 魚 iHealthChange=1 / 海老 iHealthChange=1
  - `DomainProductionModifiers`: DOMAIN_SEA iProductionModifier=25

### Smugglers' Port - 密輸港

- 内部名: `BUILDING_SMUGGLERS_PORT`
- 建造物クラス: 密輸港
- コスト[ハンマー]: 200
- 産出[%]: +10[商業]
- 産出(商業系)[%]: 10[ゴールド]
- 専門家枠: 商人 iSpecialistCount=1
- その他の設定:
  - `bWater`: 1
  - `bNeverCapture`: 1
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `iTradeRoutes`: 1
  - `fVisibilityPriority`: 1
  - `iCrime`: 10

### Shipyard - 造船所

- 内部名: `BUILDING_SHIPYARD`
- 建造物クラス: 造船所
- コスト[ハンマー]: 80
- 必要テクノロジー: 鉄器
- 倍速の志向: 攻撃志向 iProductionTrait=100 / TXT_KEY_TRAIT_IMPERIALIST iProductionTrait=50
- その他の設定:
  - `bWater`: 1
  - `iMinAreaSize`: 20
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `DomainFreeExperiences`: DOMAIN_SEA iExperience=4
  - `DomainProductionModifiers`: DOMAIN_SEA iProductionModifier=50

### Obsidian Gate - 黒曜石の門

- 内部名: `BUILDING_OBSIDIAN_GATE`
- 建造物クラス: 黒曜石の門
- コスト[ハンマー]: 240
- 必要テクノロジー: 魔術
- 倍速の志向: 迅速志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `iAirlift`: 1
  - `iTradeRoutes`: 1
  - `iTradeRouteModifier`: 10
  - `fVisibilityPriority`: 1

### Forge - 鍛冶屋

- 内部名: `BUILDING_FORGE`
- 建造物クラス: 鍛冶屋
- コスト[ハンマー]: 150
- 必要テクノロジー: 製錬
- 産出[%]: +25[ハンマー]
- 専門家枠: 技師 iSpecialistCount=1
- 倍速の志向: 勤労志向 iProductionTrait=100 / 軍事志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `BonusHappinessChanges`: 金 iHappinessChange=1
  - `SupplyPromotionProbabilities`: 武器の腐食 iProbability=-50

### Dwarven Smithy - ドワーフの鍛冶場

- 内部名: `BUILDING_DWARVEN_SMITHY`
- 固有: カザード（鍛冶屋 の代替）
- 建造物クラス: 鍛冶屋
- コスト[ハンマー]: 150
- 必要テクノロジー: 製錬
- 産出[%]: +20[ハンマー]
- 専門家枠: 技師 iSpecialistCount=1
- 倍速の志向: 勤労志向 iProductionTrait=100 / 軍事志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 金 iHappinessChange=1
  - `SupplyPromotionProbabilities`: 武器の腐食 iProbability=-50
  - `BonusYieldModifiers`: 銅 / 鉄 / ミスリル

### Monument - 記念碑

- 内部名: `BUILDING_MONUMENT`
- 建造物クラス: 記念碑
- コスト[ハンマー]: 60
- 必要テクノロジー: 原初の祈り
- 陳腐化: 秘術の伝承知識
- 倍速の志向: 創造志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 古典期
  - `MaxStartEra`: 未来
  - `HappinessTraits`: カリスマ志向 iHappinessTrait=1
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 2
  - `ObsoleteSafeCommerceChanges`: 3[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Academy - アカデミー

- 内部名: `BUILDING_ACADEMY`
- 建造物クラス: アカデミー
- コスト[ハンマー]: 240
- 必要テクノロジー: 数学
- 必要な建造物: 長老会議
- 必要な志向: 賢人志向
- 産出(商業系)[%]: 50[研究]
- その他の設定:
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `PrereqBuildingClasses`: 長老会議 iNumBuildingNeeded=3

### Elder Council - 長老会議

- 内部名: `BUILDING_ELDER_COUNCIL`
- 建造物クラス: 長老会議
- コスト[ハンマー]: 60
- 必要テクノロジー: 神秘主義
- 陳腐化: 秘術の伝承知識
- 産出(商業系): 2[研究]
- 専門家枠: 賢者 iSpecialistCount=1
- 倍速の志向: 哲学志向 iProductionTrait=100
- その他の設定:
  - `MaxStartEra`: 未来
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 2

### Library - 図書館

- 内部名: `BUILDING_LIBRARY`
- 建造物クラス: 図書館
- コスト[ハンマー]: 100
- 必要テクノロジー: 筆記
- 産出(商業系)[%]: 25[研究]
- 専門家枠: 賢者 iSpecialistCount=1
- 倍速の志向: 哲学志向 iProductionTrait=100 / 賢人志向 iProductionTrait=50
- その他の設定:
  - `FreeStartEra`: 未来
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Astrological Observatory - 占星台

- 内部名: `BUILDING_ASTROLOGICAL_OBSERVATORY`
- 建造物クラス: 占星台
- コスト[ハンマー]: 240
- 必要テクノロジー: 天文学
- 必要な建造物: 図書館
- 産出(商業系): 4[研究]
- 産出(商業系)[%]: 25[研究]
- 専門家枠: 賢者 iSpecialistCount=1
- 倍速の志向: 秘術志向 iProductionTrait=100 / 探求志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `iSpaceProductionModifier`: 50
  - `fVisibilityPriority`: 1

### Alchemy Lab - 錬金術ラボ

- 内部名: `BUILDING_ALCHEMY_LAB`
- 建造物クラス: 錬金術ラボ
- コスト[ハンマー]: 300
- 必要テクノロジー: 魔術
- 産出(商業系): 4[研究]
- 産出(商業系)[%]: 25[研究], 10[文化]
- 専門家枠: 賢者 iSpecialistCount=1
- 倍速の志向: 探求志向 iProductionTrait=100 / 秘術志向 iProductionTrait=100 / 賢人志向 iProductionTrait=50
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusYieldModifiers`: 秘薬 / 火薬 / 銅

### Theatre - 劇場

- 内部名: `BUILDING_THEATRE`
- 建造物クラス: 劇場
- コスト[ハンマー]: 200
- 必要テクノロジー: 演劇
- 産出(商業系)[%]: 30[文化]
- 専門家枠: 吟遊詩人 iSpecialistCount=1
- 倍速の志向: 創造志向 iProductionTrait=100 / 伝道志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceHappinesses`: 10[文化]
  - `BonusHappinessChanges`: 染料 iHappinessChange=1 / 絹 iHappinessChange=1

### Market - 市場

- 内部名: `BUILDING_MARKET`
- 建造物クラス: 市場
- コスト[ハンマー]: 100
- 必要テクノロジー: 祝祭
- 陳腐化: 蒸気機関
- 産出(商業系): 4[ゴールド], -2[研究]
- 専門家枠: 商人 iSpecialistCount=1
- 倍速の志向: 金融志向 iProductionTrait=100 / 交易志向 iProductionTrait=100 / 強欲志向 iProductionTrait=100
- その他の設定:
  - `MaxStartEra`: 未来
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `BonusHealthChanges`: バナナ iHealthChange=1
  - `BonusHappinessChanges`: 象牙 iHappinessChange=1
  - `iCrime`: 5

### Money Changer - 両替商

- 内部名: `BUILDING_MONEYCHANGER`
- 建造物クラス: 両替商
- コスト[ハンマー]: 250
- 必要テクノロジー: 通貨
- 産出(商業系): 1[ゴールド]
- 産出(商業系)[%]: 25[ゴールド]
- 専門家枠: 商人 iSpecialistCount=1
- 倍速の志向: 金融志向 iProductionTrait=100 / 蒐集志向 iProductionTrait=100 / 徴税志向 iProductionTrait=100 / 強欲志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 未来
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Tax Office - 徴税所

- 内部名: `BUILDING_TAX_OFFICE`
- 建造物クラス: 徴税所
- コスト[ハンマー]: 200
- 必要テクノロジー: 税制
- 産出(商業系): 2[ゴールド]
- 産出(商業系)[%]: 25[ゴールド]
- 倍速の志向: 徴税志向 iProductionTrait=100 / 強欲志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Gambling House - 賭博場

- 内部名: `BUILDING_GAMBLING_HOUSE`
- 建造物クラス: 賭博場
- コスト[ハンマー]: 200
- 必要テクノロジー: 数学
- 産出(商業系): 3[ゴールド]
- 倍速の志向: 強欲志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: 10
  - `fVisibilityPriority`: 1
  - `CommerceHappinesses`: 10[ゴールド]
  - `iCrime`: 10

### Courthouse - 裁判所

- 内部名: `BUILDING_COURTHOUSE`
- 建造物クラス: 裁判所
- コスト[ハンマー]: 100
- 必要テクノロジー: 法律
- 倍速の志向: 組織志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 未来
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -40
  - `fVisibilityPriority`: 10
  - `iCrime`: -10

### Governor's Manor - 領主邸

- 内部名: `BUILDING_GOVERNORS_MANOR`
- 固有: カラビム（裁判所 の代替）
- 建造物クラス: 裁判所
- コスト[ハンマー]: 120
- 必要テクノロジー: 法律
- 倍速の志向: 組織志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 未来
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -25
  - `iWarWearinessModifier`: -25
  - `fVisibilityPriority`: 10
  - `AngryYields`: +3[ハンマー]
  - `iCrime`: -10

### Dungeon - 地下牢

- 内部名: `BUILDING_DUNGEON`
- 建造物クラス: 地下牢
- コスト[ハンマー]: 120
- 必要テクノロジー: 石工
- 倍速の志向: 組織志向 iProductionTrait=100 / カリスマ志向 iProductionTrait=100 / 防御志向 iProductionTrait=100 / 軍事志向 iProductionTrait=100 / 将官志向 iProductionTrait=100
- 倍速の資源: 石材 iProductonModifier=100
- その他の設定:
  - `FreeStartEra`: 中世
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 1
  - `iConscriptAngerModifier`: -50
  - `iCivicAngerModifier`: -50
  - `iMaxLatitude`: 90
  - `iWarWearinessModifier`: -25
  - `fVisibilityPriority`: 1
  - `DomainProductionModifiers`: DOMAIN_LAND iProductionModifier=10
  - `iCrime`: -10

### Inn - 宿屋

- 内部名: `BUILDING_INN`
- 建造物クラス: 宿屋
- コスト[ハンマー]: 180
- 必要テクノロジー: 交易
- 産出[%]: +10[商業]
- 倍速の志向: 交易志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 未来
  - `iMaxLatitude`: 90
  - `iHealRateChange`: 15
  - `iTradeRouteModifier`: 50
  - `fVisibilityPriority`: 1
  - `BonusHealthChanges`: エール酒 iHealthChange=1 / 砂糖 iHealthChange=1 / ワイン iHealthChange=1
  - `BonusHappinessChanges`: 綿花 iHappinessChange=1
  - `iCrime`: 5

### Tavern - 酒場

- 内部名: `BUILDING_TAVERN`
- 建造物クラス: 酒場
- コスト[ハンマー]: 250
- 必要テクノロジー: 通貨
- 必要な資源（いずれか）: エール酒 / ワイン
- 産出[%]: +5[商業]
- 産出(商業系)[%]: 25[文化]
- 倍速の志向: 交易志向 iProductionTrait=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な吟遊詩人
  - `iGreatPeopleRateChange`: 1
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `iTradeRoutes`: 1
  - `iTradeRouteModifier`: 25
  - `fVisibilityPriority`: 1
  - `BonusYieldModifiers`: エール酒
  - `iCrime`: 5

### Pagan Temple - 土着の神殿

- 内部名: `BUILDING_PAGAN_TEMPLE`
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=2
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Temple of the Hand - 御手の神殿

- 内部名: `BUILDING_TEMPLE_OF_THE_HAND`
- 固有: イリアン（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- 説明（ゲーム内ヘルプ）: 都市の周囲2タイル以内を氷原へ変える
- その他の設定:
  - `bNeverCapture`: 1
  - `bStayColdCounter`: 1
  - `iMaxLatitude`: 90
  - `iMilitaryProductionModifier`: 10
  - `iSpaceProductionModifier`: 25
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Desert Shrine - 砂漠の祭殿

- 内部名: `BUILDING_DESERT_SHRINE`
- 固有: マラキム（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- [都市防御]: 10
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1
  - `UnitCombatFreeExperiences`: 信奉ユニット iExperience=2

### Temple of the Order - 秩序の神殿

- 内部名: `BUILDING_TEMPLE_OF_THE_ORDER`
- 建造物クラス: 秩序の神殿
- コスト[ハンマー]: 120
- 必要テクノロジー: 天界からの指令
- 必要な宗教: 秩序の修道会
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=2
- 倍速の志向: 伝道志向 iProductionTrait=100
- その他の設定:
  - `SpecialBuildingType`: SPECIALBUILDING_TEMPLE
  - `ReligionType`: 秩序の修道会
  - `HappinessTraits`: 宗教志向 iHappinessTrait=1
  - `iMaxLatitude`: 90
  - `iMilitaryProductionModifier`: 15
  - `fVisibilityPriority`: 10
  - `BonusHappinessChanges`: 香木 iHappinessChange=1 / エール酒 iHappinessChange=1
  - `iCrime`: -5

### Temple of the Empyrean - 至天の神殿

- 内部名: `BUILDING_TEMPLE_OF_THE_EMPYREAN`
- 建造物クラス: 至天の神殿
- コスト[ハンマー]: 120
- 必要テクノロジー: 名誉
- 必要な宗教: 至光なる天空
- 産出(商業系)[%]: 15[研究], 20[文化]
- 専門家枠: 神官 iSpecialistCount=2
- 倍速の志向: 伝道志向 iProductionTrait=100
- その他の設定:
  - `SpecialBuildingType`: SPECIALBUILDING_TEMPLE
  - `ReligionType`: 至光なる天空
  - `HappinessTraits`: 宗教志向 iHappinessTrait=1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `BonusHappinessChanges`: 香木 iHappinessChange=1 / エール酒 iHappinessChange=1

### Temple of Kilmorph - キルモフの神殿

- 内部名: `BUILDING_TEMPLE_OF_KILMORPH`
- 建造物クラス: キルモフの神殿
- コスト[ハンマー]: 120
- 必要テクノロジー: 母なる大地への道
- 必要な宗教: キルモフのルーン
- 産出(商業系): 2[ゴールド]
- 産出(商業系)[%]: 5[ゴールド], 20[文化]
- 専門家枠: 商人 iSpecialistCount=1 / 神官 iSpecialistCount=1
- 倍速の志向: 伝道志向 iProductionTrait=100
- その他の設定:
  - `SpecialBuildingType`: SPECIALBUILDING_TEMPLE
  - `ReligionType`: キルモフのルーン
  - `HappinessTraits`: 宗教志向 iHappinessTrait=1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `BonusHappinessChanges`: 宝石 iHappinessChange=1 / エール酒 iHappinessChange=1

### Temple of Leaves - 緑葉の神殿

- 内部名: `BUILDING_TEMPLE_OF_LEAVES`
- 建造物クラス: 緑葉の神殿
- コスト[ハンマー]: 120
- 必要テクノロジー: 深き森への道
- 必要な宗教: 緑葉の同胞
- 産出: +1[食料]
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 吟遊詩人 iSpecialistCount=1 / 神官 iSpecialistCount=1
- 倍速の志向: 伝道志向 iProductionTrait=100
- 説明（ゲーム内ヘルプ）: 周辺の古代樹林でトレントの発生率3倍
- その他の設定:
  - `SpecialBuildingType`: SPECIALBUILDING_TEMPLE
  - `ReligionType`: 緑葉の同胞
  - `HappinessTraits`: 宗教志向 iHappinessTrait=1
  - `iMaxLatitude`: 90
  - `iFoodKept`: 10
  - `fVisibilityPriority`: 10
  - `BonusHappinessChanges`: 香木 iHappinessChange=1 / エール酒 iHappinessChange=1

### Temple of the Overlords - 深海の神殿

- 内部名: `BUILDING_TEMPLE_OF_THE_OVERLORDS`
- 建造物クラス: 深海の神殿
- コスト[ハンマー]: 120
- 必要テクノロジー: 深海からの神託
- 必要な宗教: 深海の旧支配者
- 産出(商業系)[%]: 40[文化]
- 専門家枠: 神官 iSpecialistCount=1 / 賢者 iSpecialistCount=1
- 倍速の志向: 伝道志向 iProductionTrait=100
- 説明（ゲーム内ヘルプ）: 実行可能: 溺死の儀
- その他の設定:
  - `SpecialBuildingType`: SPECIALBUILDING_TEMPLE
  - `ReligionType`: 深海の旧支配者
  - `HappinessTraits`: 宗教志向 iHappinessTrait=1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1 / エール酒 iHappinessChange=1

### Temple of the Veil - ヴェールの神殿

- 内部名: `BUILDING_TEMPLE_OF_THE_VEIL`
- 建造物クラス: ヴェールの神殿
- コスト[ハンマー]: 120
- 必要テクノロジー: 魂の堕落
- 必要な宗教: 蒼褪めたヴェール
- 産出(商業系): 3[研究]
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1 / 賢者 iSpecialistCount=1
- 倍速の志向: 伝道志向 iProductionTrait=100
- その他の設定:
  - `SpecialBuildingType`: SPECIALBUILDING_TEMPLE
  - `ReligionType`: 蒼褪めたヴェール
  - `HappinessTraits`: 宗教志向 iHappinessTrait=1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 2
  - `BonusHappinessChanges`: 秘薬 iHappinessChange=1 / エール酒 iHappinessChange=1

### Basilica - バシリカ

- 内部名: `BUILDING_BASILICA`
- 建造物クラス: バシリカ
- コスト[ハンマー]: 180
- 必要テクノロジー: 宗教法
- 必要な宗教: 秩序の修道会
- 必要な国教: 秩序の修道会
- その他の設定:
  - `ReligionType`: 秩序の修道会
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -40
  - `iMilitaryProductionModifier`: 10
  - `fVisibilityPriority`: 1
  - `iCrime`: -10

### Asylum - 精神病院

- 内部名: `BUILDING_ASYLUM`
- 建造物クラス: 精神病院
- コスト[ハンマー]: 120
- 必要テクノロジー: 精神圧搾
- 必要な宗教: 深海の旧支配者
- 必要な国教: 深海の旧支配者
- 産出(商業系)[%]: 15[研究]
- 専門家枠: 賢者 iSpecialistCount=1
- 説明（ゲーム内ヘルプ）: 新規の生物ユニットに10%の確率で発狂・狂乱を与える
- その他の設定:
  - `ReligionType`: 深海の旧支配者
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iWarWearinessModifier`: -25
  - `fVisibilityPriority`: 10

### Demons' Altar - 悪魔の供犠台

- 内部名: `BUILDING_DEMONS_ALTAR`
- 建造物クラス: 悪魔の供犠台
- コスト[ハンマー]: 150
- 必要テクノロジー: 地獄の契約
- 必要な宗教: 蒼褪めたヴェール
- 必要な国教: 蒼褪めたヴェール
- 必要な建造物: ヴェールの神殿
- 産出[%]: +10[ハンマー]
- 産出(商業系)[%]: 10[研究]
- 新規ユニットに昇進: 災厄
- 専門家枠: 賢者 iSpecialistCount=2
- 説明（ゲーム内ヘルプ）: 新規の魔族ユニットに+2: 経験ポイント
- その他の設定:
  - `ReligionType`: 蒼褪めたヴェール
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Citadel of Light - 光の城塞

- 内部名: `BUILDING_CITADEL_OF_LIGHT`
- 建造物クラス: 光の城塞
- コスト[ハンマー]: 180
- 必要テクノロジー: 魔術
- 必要な文明: マラキム
- 産出(商業系): 1[ゴールド], 1[研究], 1[文化]
- [都市防御]: 25
- 説明（ゲーム内ヘルプ）: ターンの開始時に、周囲2タイル以内の敵ユニットに火炎ダメージを与える / 都市の周囲1タイル以内を砂漠へ変える
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 2
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `FreePromotionProbabilities`: 看破の目 iProbability=50

### Chancel of Guardians - 守護の教会

- 内部名: `BUILDING_CHANCEL_OF_GUARDIANS`
- 建造物クラス: 守護の教会
- コスト[ハンマー]: 120
- 必要テクノロジー: 聖職
- 必要な文明: エロヒム
- 新規ユニットに昇進: 都市駐留Ⅰ
- [都市防御]: 25
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iAllCityDefense`: 5
  - `fVisibilityPriority`: 1
  - `FreePromotionProbabilities`: 鉄壁 iProbability=80

### Reliquary - 聖骸殿

- 内部名: `BUILDING_RELIQUARY`
- 建造物クラス: 聖骸殿
- コスト[ハンマー]: 60
- 必要テクノロジー: 叡智への道
- 必要な文明: エロヒム
- 新規ユニットに昇進: 聖霊の導き
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `UnitCombatFreePromotionPicks`: 信奉ユニット iFreePromotionPick=1

### Adularia Chamber - 氷長石の保管庫

- 内部名: `BUILDING_ADULARIA_CHAMBER`
- 建造物クラス: 氷長石の保管庫
- コスト[ハンマー]: 180
- 必要テクノロジー: 魔術
- 必要な文明: ルシュイアープ
- 必要な資源: 影のマナ
- 説明（ゲーム内ヘルプ）: 新規のゴーレムユニットに不可視の昇進
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `iDuplicateUnit`: 1

### Pallens Engine - 秘色機関

- 内部名: `BUILDING_PALLENS_ENGINE`
- 建造物クラス: 秘色機関
- コスト[ハンマー]: 80
- 必要テクノロジー: 予言術
- 必要な文明: ルシュイアープ
- 必要な資源: 太陽のマナ
- 説明（ゲーム内ヘルプ）: 新規のゴーレムユニットに看破の目と魔法抵抗の昇進
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `iDuplicateUnit`: 1

### Blasting Workshop - 爆破工房

- 内部名: `BUILDING_BLASTING_WORKSHOP`
- 建造物クラス: 爆破工房
- コスト[ハンマー]: 80
- 必要テクノロジー: 四大元素
- 必要な文明: ルシュイアープ
- 必要な資源: 炎のマナ
- 説明（ゲーム内ヘルプ）: 新規のゴーレムユニットに火球を発射する能力を与える
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `iDuplicateUnit`: 1

### Jeweler - 宝石商

- 内部名: `BUILDING_JEWELER`
- 建造物クラス: 宝石商
- コスト[ハンマー]: 120
- 必要テクノロジー: 製錬
- 必要な資源（いずれか）: 宝石 / 金 / 真珠 / 琥珀 / 翡翠
- 必要な志向: 大都市志向
- 産出[%]: +20[ハンマー]
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iGlobalHappiness`: 1
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 宝石 iHappinessChange=1 / 金 iHappinessChange=1 / 真珠 iHappinessChange=1 / 琥珀 iHappinessChange=1 / 翡翠 iHappinessChange=1
  - `BonusYieldModifiers`: 金 / 宝石 / 象牙 / 大理石 / 真珠

### Tailor - 仕立屋

- 内部名: `BUILDING_TAILOR`
- 建造物クラス: 仕立屋
- コスト[ハンマー]: 100
- 必要テクノロジー: 道具の作成
- 必要な資源（いずれか）: 綿花 / 染料 / 絹
- 必要な志向: 大都市志向
- 産出: +2[ハンマー]
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iGlobalHappiness`: 1
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 染料 iHappinessChange=1 / 綿花 iHappinessChange=1 / 絹 iHappinessChange=1
  - `BonusYieldModifiers`: 染料 / 綿花 / 毛皮 / 羊 / 絹

### Dwarven Vault (Empty) - ドワーフの金庫（空っぽ）

- 内部名: `BUILDING_DWARVEN_VAULT_EMPTY`
- 建造物クラス: ドワーフの金庫（空っぽ）
- 必要な文明: カザード
- [幸福]: -2
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Dwarven Vault (Low) - ドワーフの金庫（少量）

- 内部名: `BUILDING_DWARVEN_VAULT_LOW`
- 建造物クラス: ドワーフの金庫（少量）
- 必要な文明: カザード
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Dwarven Vault (Abundant) - ドワーフの金庫（潤沢）

- 内部名: `BUILDING_DWARVEN_VAULT_ABUNDANT`
- 建造物クラス: ドワーフの金庫（潤沢）
- 必要な文明: カザード
- [幸福]: 2
- 産出[%]: +10[ハンマー]
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Dwarven Vault - ドワーフの金庫

- 内部名: `BUILDING_DWARVEN_VAULT`
- 建造物クラス: ドワーフの金庫
- 必要な文明: カザード
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Dwarven Vault (Stocked) - ドワーフの金庫（充分）

- 内部名: `BUILDING_DWARVEN_VAULT_STOCKED`
- 建造物クラス: ドワーフの金庫（充分）
- 必要な文明: カザード
- [幸福]: 1
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Dwarven Vault (Full) - ドワーフの金庫（満杯）

- 内部名: `BUILDING_DWARVEN_VAULT_FULL`
- 建造物クラス: ドワーフの金庫（満杯）
- 必要な文明: カザード
- [幸福]: 2
- 産出[%]: +25[ハンマー]
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Dwarven Vault (Overflowing) - ドワーフの金庫（過剰）

- 内部名: `BUILDING_DWARVEN_VAULT_OVERFLOWING`
- 建造物クラス: ドワーフの金庫（過剰）
- 必要な文明: カザード
- [幸福]: 3
- 産出[%]: +40[ハンマー]
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iGreatPeopleRateModifier`: 25
  - `fVisibilityPriority`: 1

### Adventurers' Guild - 冒険者ギルド

- 内部名: `BUILDING_ADVENTURERS_GUILD`
- 建造物クラス: 冒険者ギルド
- コスト[ハンマー]: 120
- 必要テクノロジー: 通貨
- 必要な文明: グリゴリ
- その他の設定:
  - `GreatPeopleUnitClass`: 冒険者
  - `iGreatPeopleRateChange`: 4
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iGreatPeopleRateModifier`: 25
  - `iMilitaryProductionModifier`: 10
  - `fVisibilityPriority`: 1
  - `DomainFreeExperiences`: DOMAIN_LAND iExperience=2

### Cave of Ancestors - 祖霊の洞窟

- 内部名: `BUILDING_CAVE_OF_ANCESTORS`
- 建造物クラス: 祖霊の洞窟
- コスト[ハンマー]: 120
- 必要テクノロジー: 魔術
- 必要な文明: アムリテ
- 説明（ゲーム内ヘルプ）: 新規の秘術ユニットに、所持しているマナ資源の種類に等しい数の経験値を与える
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ImprovementFreeSpecialists`: 大気のノード iFreeSpecialistCount=1 / 肉体のノード iFreeSpecialistCount=1 / 混沌のノード iFreeSpecialistCount=1 / 死のノード iFreeSpecialistCount=1 / 大地のノード iFreeSpecialistCount=1 / 呪付のノード iFreeSpecialistCount=1 / 不可逆のノード iFreeSpecialistCount=1 / 炎のノード iFreeSpecialistCount=1 / 法のノード iFreeSpecialistCount=1 / 生命のノード iFreeSpecialistCount=1 / 超魔術のノード iFreeSpecialistCount=1 / 精神のノード iFreeSpecialistCount=1 / 自然のノード iFreeSpecialistCount=1 / 影のノード iFreeSpecialistCount=1 / 魂のノード iFreeSpecialistCount=1 / 太陽のノード iFreeSpecialistCount=1 / 水のノード iFreeSpecialistCount=1

### Freak Show - 見世物小屋

- 内部名: `BUILDING_FREAK_SHOW`
- 建造物クラス: 見世物小屋
- 必要な文明: バルセラフ
- [幸福]: 1
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な吟遊詩人
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Hall of Mirrors - 鏡の館

- 内部名: `BUILDING_HALL_OF_MIRRORS`
- 建造物クラス: 鏡の館
- コスト[ハンマー]: 180
- 必要テクノロジー: 変成術
- 必要な文明: バルセラフ
- 必要な建造物: 巡業サーカス
- [幸福]: 1
- 産出(商業系)[%]: 30[文化]
- 説明（ゲーム内ヘルプ）: 隣接タイルの敵ユニットを映し出した幻影が配下として出現
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `GlobalCommerceModifiers`: 3[文化]

### Warrens - 繁殖巣

- 内部名: `BUILDING_WARRENS`
- 建造物クラス: 繁殖巣
- コスト[ハンマー]: 180
- 必要テクノロジー: 石工
- 必要な文明: 残り火一族
- 説明（ゲーム内ヘルプ）: 都市で生産する新規ユニットの数が2倍になる / （オーク、ゴブリン、オーガのみ） / 英雄ユニット、国家ユニット、攻城兵器、海軍ユニットには効果なし
- その他の設定:
  - `bNeverCapture`: 1
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `iDuplicateUnit`: 1

### Breeding Pit - 飼育穴

- 内部名: `BUILDING_BREEDING_PIT`
- 建造物クラス: 飼育穴
- コスト[ハンマー]: 120
- 必要な文明: カラビム
- 産出[%]: +10[食料]
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iFoodKept`: 20
  - `fVisibilityPriority`: 10

### Planar Gate - 次元界の門

- 内部名: `BUILDING_PLANAR_GATE`
- 建造物クラス: 次元界の門
- コスト[ハンマー]: 120
- 必要テクノロジー: エーテルの知識
- 必要な文明: シェアイム
- 産出(商業系)[%]: 5[研究]
- 説明（ゲーム内ヘルプ）: 異次元の生物が無作為に現れて配下に加わる
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iSpaceProductionModifier`: 25
  - `fVisibilityPriority`: 1

### Demonic Citizens - 悪魔の市民

- 内部名: `BUILDING_DEMONIC_CITIZENS`
- 建造物クラス: 悪魔の市民
- 必要な文明: 地獄の軍勢
- その他の設定:
  - `bNoUnhappiness`: 1
  - `bNoUnhealthyPopulation`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Human Cage - 人間の檻

- 内部名: `BUILDING_HUMAN_CAGE`
- 建造物クラス: 人間の檻
- [幸福]: 1
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な吟遊詩人
  - `iGreatPeopleRateChange`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Dwarf Cage - ドワーフの檻

- 内部名: `BUILDING_DWARF_CAGE`
- 建造物クラス: ドワーフの檻
- [幸福]: 1
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な吟遊詩人
  - `iGreatPeopleRateChange`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Elf Cage - エルフの檻

- 内部名: `BUILDING_ELF_CAGE`
- 建造物クラス: エルフの檻
- [幸福]: 1
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な吟遊詩人
  - `iGreatPeopleRateChange`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Orc Cage - オークの檻

- 内部名: `BUILDING_ORC_CAGE`
- 建造物クラス: オークの檻
- [幸福]: 1
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な吟遊詩人
  - `iGreatPeopleRateChange`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Dancing Bear - 熊の見世物

- 内部名: `BUILDING_DANCING_BEAR`
- 建造物クラス: 熊の見世物
- [幸福]: 1
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 3[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Gorilla Cage - ゴリラの檻

- 内部名: `BUILDING_GORILLA_CAGE`
- 建造物クラス: ゴリラの檻
- 必要な建造物: 巡業サーカス
- [幸福]: 1
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 3[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Lion Cage - ライオンの檻

- 内部名: `BUILDING_LION_CAGE`
- 建造物クラス: ライオンの檻
- 必要な建造物: 巡業サーカス
- [幸福]: 1
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 3[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Tiger Cage - 虎の檻

- 内部名: `BUILDING_TIGER_CAGE`
- 建造物クラス: 虎の檻
- 必要な建造物: 巡業サーカス
- [幸福]: 1
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 3[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Wolf Pen - 狼の檻

- 内部名: `BUILDING_WOLF_PEN`
- 建造物クラス: 狼の檻
- 必要な建造物: 巡業サーカス
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Spider Pen - 蜘蛛の養殖場

- 内部名: `BUILDING_SPIDER_PEN`
- 建造物クラス: NONE
- 必要テクノロジー: 動物の馴致
- 産出(商業系): 4[ゴールド]
- 新規ユニットに昇進: 毒の刃
- 供給する資源: 絹
- 供給数: 1
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100

### Heroic Epic - 英雄叙事詩

- 内部名: `BUILDING_HEROIC_EPIC`
- 建造物クラス: 英雄叙事詩
- コスト[ハンマー]: 200
- 必要テクノロジー: 軍事戦略
- 倍速の資源: 大理石 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iCombatLevelPrereq`: 1
  - `iMaxLatitude`: 90
  - `iMilitaryProductionModifier`: 100
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### National Epic - 民族叙事詩

- 内部名: `BUILDING_NATIONAL_EPIC`
- 建造物クラス: 民族叙事詩
- コスト[ハンマー]: 250
- 必要テクノロジー: 軍事行動
- 必要な建造物: 図書館
- 倍速の資源: 大理石 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iGreatPeopleRateModifier`: 100
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Bazaar of Mammon - マンモンのバザール

- 内部名: `BUILDING_BAZAAR_OF_MAMMON`
- 建造物クラス: マンモンのバザール
- コスト[ハンマー]: 250
- 必要テクノロジー: 数学
- 必要な建造物: 市場
- 産出(商業系)[%]: 100[ゴールド]
- 専門家枠: 商人 iSpecialistCount=3
- 倍速の資源: バナナ iProductonModifier=10 / 宝石 iProductonModifier=20 / 金 iProductonModifier=30 / 絹 iProductonModifier=20 / 砂糖 iProductonModifier=10 / 染料 iProductonModifier=10
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な商人
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `PrereqBuildingClasses`: 市場 iNumBuildingNeeded=3
  - `iCrime`: 10

### Heron Throne - ヘロンの玉座

- 内部名: `BUILDING_HERON_THRONE`
- 建造物クラス: ヘロンの玉座
- コスト[ハンマー]: 500
- 必要テクノロジー: 海図
- [都市防御]: 25
- 倍速の資源: 大理石 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な技師
  - `iGreatPeopleRateChange`: 2
  - `bWater`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `GlobalSeaPlotYieldChanges`: +1[ハンマー]
  - `ObsoleteSafeCommerceChanges`: 8[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `SpecialistYieldChanges`: 技師 +1[ハンマー] / 偉大な技師 +2[ハンマー]

### Shrine of the Champion - 英雄の殿堂

- 内部名: `BUILDING_SHRINE_OF_THE_CHAMPION`
- 建造物クラス: 英雄の殿堂
- コスト[ハンマー]: 250
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 5[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `iFreePromotionPick`: 1

### Aquae Sucellus - スケルスの鉱泉

- 内部名: `BUILDING_AQUAE_SUCELLUS`
- 建造物クラス: NONE
- コスト[ハンマー]: 450
- 必要テクノロジー: 衛生設備
- 必要な資源: 生命のマナ
- 倍速の資源: 大理石 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な技師
  - `iGreatPeopleRateChange`: 2
  - `bNoUnhealthyPopulation`: 1
  - `bNukeImmune`: 1
  - `bCenterInCity`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iHealRateChange`: 30
  - `iGlobalHealth`: 2
  - `fVisibilityPriority`: 4
  - `ObsoleteSafeCommerceChanges`: 6[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `RemovePromotion`: 衰弱

### Bone Palace - 竜骨の宮殿

- 内部名: `BUILDING_BONE_PALACE`
- 建造物クラス: 竜骨の宮殿
- コスト[ハンマー]: 650
- 必要テクノロジー: 宗教法
- 倍速の資源: 大理石 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な技師
  - `iGreatPeopleRateChange`: 2
  - `bTeamShare`: 1
  - `bGoldenAge`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iGoldenAgeModifier`: 50
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 10[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `iGlobalResistModify`: 20

### Caminus Aureus - アウレウスの竈

- 内部名: `BUILDING_CAMINUS_AUREUS`
- 建造物クラス: アウレウスの竈
- コスト[ハンマー]: 1200
- 必要テクノロジー: ミスリル器
- 供給する資源: ミスリル
- 供給数: 1
- 倍速の資源: 金 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な技師
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Catacomb Libralus - 禁書の地下墓所

- 内部名: `BUILDING_CATACOMB_LIBRALUS`
- 建造物クラス: 禁書の地下墓所
- コスト[ハンマー]: 450
- 必要テクノロジー: エーテルの知識
- 産出(商業系): 8[研究]
- 供給する資源: 古書物
- 供給数: 1
- 倍速の資源: 石材 iProductonModifier=100
- その他の設定:
  - `FreeBuilding`: 魔術師ギルド
  - `GreatPeopleUnitClass`: 偉大な賢者
  - `iGreatPeopleRateChange`: 2
  - `bTeamShare`: 1
  - `bNukeImmune`: 1
  - `bAllCities`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `GlobalSpecialistCounts`: 賢者 iSpecialistCount=1
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `UnitCombatFreePromotionPicks`: 秘術ユニット iFreePromotionPick=1

### Celestial Compass - 天球の羅針盤

- 内部名: `BUILDING_CELESTIAL_COMPASS`
- 建造物クラス: 天球の羅針盤
- コスト[ハンマー]: 450
- 必要テクノロジー: 天文学
- 説明（ゲーム内ヘルプ）: 新しいテクノロジーを発見する度に星座の輝きを発見できる
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iGlobalSpaceProductionModifier`: 100
  - `iGlobalTradeRoutes`: 1
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 10[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### City of a Thousand Slums - 広大な貧民街

- 内部名: `BUILDING_CITY_OF_A_THOUSAND_SLUMS`
- 建造物クラス: 広大な貧民街
- コスト[ハンマー]: 500
- 必要テクノロジー: 建設
- その他の設定:
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: トウモロコシ iHappinessChange=1 / 米 iHappinessChange=1 / 小麦 iHappinessChange=1 / 亜麻 iHappinessChange=1 / ジャガイモ iHappinessChange=1 / エール酒 iHappinessChange=1
  - `iCrime`: 10
  - `iPlotRadius`: 3

### The Eyes and Ears Network - 遠目と早耳の情報網

- 内部名: `BUILDING_EYES_AND_EARS_NETWORK`
- 建造物クラス: 遠目と早耳の情報網
- コスト[ハンマー]: 1500
- 必要テクノロジー: ギルド
- 説明（ゲーム内ヘルプ）: 他の3つ以上の文明が既に獲得しているテクノロジーを自動的に得る / 全てのライバルの研究先を目視可能
- その他の設定:
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iTechShare`: 3
  - `fVisibilityPriority`: 1
  - `PrereqBuildingClasses`: 宿屋 iNumBuildingNeeded=3
  - `iCrime`: 10

### Form of the Titan - ティターンの巨像

- 内部名: `BUILDING_FORM_OF_THE_TITAN`
- 建造物クラス: ティターンの巨像
- コスト[ハンマー]: 400
- 必要テクノロジー: 軍事行動
- 倍速の資源: 銅 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 2
  - `bTeamShare`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iCombatLevelPrereq`: 2
  - `iMaxLatitude`: 90
  - `iGlobalExperience`: 2
  - `fVisibilityPriority`: 100

### Grand Menagerie - 動物博覧会

- 内部名: `BUILDING_GRAND_MENAGERIE`
- 建造物クラス: 動物博覧会
- コスト[ハンマー]: 120
- 必要テクノロジー: 祝祭
- 必要な建造物: 狼の檻 / 熊の見世物 / 虎の檻 / ゴリラの檻 / ライオンの檻
- 産出(商業系)[%]: 20[文化]
- 無償の専門家: 吟遊詩人 iFreeSpecialistCount=1
- その他の設定:
  - `FreeBuilding`: 巡業サーカス
  - `GreatPeopleUnitClass`: 偉大な吟遊詩人
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iGlobalHappiness`: 2
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 8[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Deruptus Brewing House - デルプトゥスの醸造所

- 内部名: `BUILDING_GREAT_BREWERY`
- 建造物クラス: デルプトゥスの醸造所
- コスト[ハンマー]: 500
- 必要テクノロジー: 衛生設備
- 必要な建造物: ビール醸造所
- 供給する資源: エール酒
- 供給数: 3
- 説明（ゲーム内ヘルプ）: 川沿い都市にのみ建設可能
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な商人
  - `iGreatPeopleRateChange`: 2
  - `bRiver`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `RiverPlotYieldChanges`: 1[文化]
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `PrereqBuildingClasses`: ビール醸造所 iNumBuildingNeeded=3

### The Great Library - アレクサンドリア図書館

- 内部名: `BUILDING_GREAT_LIBRARY`
- 建造物クラス: アレクサンドリア図書館
- コスト[ハンマー]: 600
- 必要テクノロジー: 筆記
- 必要な建造物: 図書館
- 産出(商業系): 5[研究]
- 供給する資源: 古書物
- 供給数: 1
- 倍速の資源: 大理石 iProductonModifier=100
- その他の設定:
  - `AllowCivics`: 奨学金制
  - `GreatPeopleUnitClass`: 偉大な賢者
  - `iGreatPeopleRateChange`: 2
  - `bTeamShare`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `PrereqBuildingClasses`: 図書館 iNumBuildingNeeded=3
  - `SpecialistCommerceChanges`: 賢者 1[研究] / 偉大な賢者 3[研究]

### The Great Lighthouse - ファロス灯台

- 内部名: `BUILDING_GREAT_LIGHTHOUSE`
- 建造物クラス: ファロス灯台
- コスト[ハンマー]: 450
- 必要テクノロジー: 航海術
- 追加で必要なテクノロジー: 石工
- 必要な建造物: 灯台
- 倍速の資源: 石材 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な商人
  - `iGreatPeopleRateChange`: 2
  - `bTeamShare`: 1
  - `bWater`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `iCoastalTradeRoutes`: 2
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 6[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Guild of Hammers - ギルド・オブ・ハンマーズ

- 内部名: `BUILDING_GUILD_OF_HAMMERS`
- 建造物クラス: ギルド・オブ・ハンマーズ
- コスト[ハンマー]: 650
- 必要テクノロジー: 工学
- その他の設定:
  - `FreeBuilding`: 鍛冶屋
  - `GreatPeopleUnitClass`: 偉大な技師
  - `iGreatPeopleRateChange`: 2
  - `bTeamShare`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 8[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `SpecialistYieldChanges`: 技師 +1[ハンマー] / 偉大な技師 +2[ハンマー]

### Guild of the Nine - 九人衆ギルド

- 内部名: `BUILDING_GUILD_OF_THE_NINE`
- 建造物クラス: 九人衆ギルド
- コスト[ハンマー]: 700
- 必要テクノロジー: 重商主義
- [都市防御]: 25
- その他の設定:
  - `FreeBuilding`: 酒場
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 2
  - `bTeamShare`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Hall of Kings - 国王記念館

- 内部名: `BUILDING_HALL_OF_KINGS`
- 建造物クラス: 国王記念館
- コスト[ハンマー]: 900
- 必要テクノロジー: 封建制
- 倍速の資源: 大理石 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な吟遊詩人
  - `iGreatPeopleRateChange`: 2
  - `bTeamShare`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iAreaFreeSpecialist`: 1
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 10[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `SpecialistExtraCommerces`: 2[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `SpecialistCommerceChanges`: 吟遊詩人 1[文化] / 偉大な吟遊詩人 2[文化]

### Mercurian Gate - マーキュリアンの門

- 内部名: `BUILDING_MERCURIAN_GATE`
- 建造物クラス: マーキュリアンの門
- コスト[ハンマー]: 400
- 必要テクノロジー: 叡智への道
- 説明（ゲーム内ヘルプ）: アルマゲドンカウンタ30以上か、ライバル文明に地獄の軍勢が必要 / 首都では建設できない
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iGlobalExperience`: 2
  - `iWarWearinessModifier`: -100
  - `iGlobalWarWearinessModifier`: -20
  - `iMilitaryProductionModifier`: 50
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Mokka's Cauldron - モッカの大釜

- 内部名: `BUILDING_MOKKAS_CAULDRON`
- 建造物クラス: モッカの大釜
- コスト[ハンマー]: 450
- 必要テクノロジー: 屍霊術
- 必要な資源: 死のマナ
- 説明（ゲーム内ヘルプ）: 自分の領内で死んだユニットを、この都市で魔族として蘇らせる
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `SpecialistYieldChanges`: 神官 +1[ハンマー] / 偉大な神官 +1[ハンマー]

### The Nexus - ネクサス

- 内部名: `BUILDING_THE_NEXUS`
- 建造物クラス: ネクサス
- コスト[ハンマー]: 600
- 必要テクノロジー: 秘術の伝承知識
- その他の設定:
  - `FreeBuilding`: 黒曜石の門
  - `GreatPeopleUnitClass`: 偉大な賢者
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100

### Ride of the Nine Kings - 九王者の騎獣

- 内部名: `BUILDING_RIDE_OF_THE_NINE_KINGS`
- 建造物クラス: 九王者の騎獣
- コスト[ハンマー]: 600
- 必要テクノロジー: 軍馬
- 必要な資源: 馬
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `bAllCities`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `UnitCombatFreeExperiences`: 騎乗ユニット iExperience=9
  - `SupplyPromotionProbabilities`: 士気 iProbability=100

### Pillar of Chains - 縛鎖の柱

- 内部名: `BUILDING_PILLAR_OF_CHAINS`
- 建造物クラス: 縛鎖の柱
- コスト[ハンマー]: 500
- 必要テクノロジー: 税制
- その他の設定:
  - `bTeamShare`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -10
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `GlobalAngryYields`: +3[ハンマー]
  - `bNoCivicAnger`: 1
  - `iCrime`: -10
  - `iModifyGlobalCounter`: 4

### Prophecy of Ragnarok - ラグナロクの預言

- 内部名: `BUILDING_PROPHECY_OF_RAGNAROK`
- 建造物クラス: ラグナロクの預言
- コスト[ハンマー]: 500
- 必要テクノロジー: 邪悪への道
- 陳腐化: 高潔の証
- 新規ユニットに昇進: 黙示録の証
- 供給する資源: 古書物
- 供給数: 1
- 倍速の資源: 石材 iProductonModifier=100
- その他の設定:
  - `MaxStartEra`: 未来
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 2
  - `bTeamShare`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `GlobalSpecialistCounts`: 神官 iSpecialistCount=2
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Shrine of Sirona - シロナの祭殿

- 内部名: `BUILDING_SHRINE_OF_SIRONA`
- 建造物クラス: シロナの祭殿
- コスト[ハンマー]: 400
- 必要テクノロジー: 予言術
- 必要な資源: 魂のマナ
- 倍速の資源: 大理石 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 10[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Soul Forge - 魂の溶鉱炉

- 内部名: `BUILDING_SOUL_FORGE`
- 建造物クラス: NONE
- コスト[ハンマー]: 600
- 必要テクノロジー: 悪意の企み
- [衛生]: -2
- 産出[%]: +20[ハンマー]
- 供給する資源: 死のマナ
- 供給数: 1
- 説明（ゲーム内ヘルプ）: 領内で死んだ生物ユニットを、あるいは25%の確率で領外で殺した生物ユニットを、都市の生産力に変換する
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な技師
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `BonusYieldModifiers`: 影石

### Temple of Temporance - テンポランス神殿

- 内部名: `BUILDING_TEMPLE_OF_TEMPORENCE`
- 建造物クラス: テンポランス神殿
- コスト[ハンマー]: 700
- 必要テクノロジー: 哲学
- 供給する資源: 香木
- 供給数: 1
- 倍速の資源: 大理石 iProductonModifier=100
- その他の設定:
  - `FreeBuilding`: 土着の神殿
  - `GreatPeopleUnitClass`: 偉大な吟遊詩人
  - `iGreatPeopleRateChange`: 2
  - `bTeamShare`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iAreaHappiness`: 2
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 10[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `StateReligionCommerces`: 8[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Theatre of Dreams - 夢の劇場

- 内部名: `BUILDING_THEATRE_OF_DREAMS`
- 建造物クラス: 夢の劇場
- コスト[ハンマー]: 500
- 必要テクノロジー: 演劇
- 必要な建造物: 劇場
- [幸福]: 1
- 倍速の資源: 大理石 iProductonModifier=100
- その他の設定:
  - `FreeBuilding`: 劇場
  - `GreatPeopleUnitClass`: 偉大な吟遊詩人
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `bAllCities`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iGlobalHappiness`: 1
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 8[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceHappinesses`: 5[文化]
  - `GlobalSpecialistCounts`: 吟遊詩人 iSpecialistCount=1
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `PrereqBuildingClasses`: 劇場 iNumBuildingNeeded=3
  - `SpecialistCommerceChanges`: 吟遊詩人 3[文化] / 偉大な吟遊詩人 6[文化]

### Tower of Eyes - 物見の塔

- 内部名: `BUILDING_TOWER_OF_EYES`
- 建造物クラス: 物見の塔
- コスト[ハンマー]: 500
- 必要テクノロジー: 建設
- 新規ユニットに昇進: 歩哨Ⅰ
- 倍速の資源: 石材 iProductonModifier=100
- その他の設定:
  - `FreeBuilding`: 地下牢
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `bAllCities`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 3[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `bExtraSeeFrom`: 1
  - `iGlobalVisibilityChange`: 1

### Crown of Akharien - アハリエンの宝冠

- 内部名: `BUILDING_CROWN_OF_AKHARIEN`
- 建造物クラス: TXT_KEY_BUILDING_CROWN_OF_AKHARIEN
- コスト[ハンマー]: 900
- 必要テクノロジー: 秘術の伝承知識
- 産出(商業系): 2[研究]
- 産出(商業系)[%]: 100[研究]
- 倍速の資源: 宝石 iProductonModifier=50 / 琥珀 iProductonModifier=50
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な賢者
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Syliven's Perfect Lyre - シリヴェンの完璧なる竪琴

- 内部名: `BUILDING_SYLIVENS_PERFECT_LYRE`
- 建造物クラス: TXT_KEY_BUILDING_SYLIVENS_PERFECT_LYRE
- コスト[ハンマー]: 700
- 必要テクノロジー: 演劇
- 産出(商業系)[%]: 100[文化]
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な吟遊詩人
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 8[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### The Dragon's Hoard - 竜の財宝

- 内部名: `BUILDING_DRAGONS_HORDE`
- 建造物クラス: 竜の財宝
- 産出: +4[ハンマー], +10[商業]
- 供給する資源: 宝石
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 金 iBonusCount=1 / 真珠 iBonusCount=1 / 竜玉石 iBonusCount=1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 8[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `SupplyPromotionProbabilities`: 呪付の刃 iProbability=100 / 炎の矢 iProbability=100 / 呪文の杖 iProbability=20 / ミスリルの武器 iProbability=2

### Mines of Gal-Dur - ガル=デュールの鉱山

- 内部名: `BUILDING_MINES_OF_GALDUR`
- 建造物クラス: ガル=デュールの鉱山
- コスト[ハンマー]: 700
- 必要テクノロジー: 千仞の尾根
- 必要な宗教: キルモフのルーン
- 必要な国教: キルモフのルーン
- [衛生]: -2
- 専門家枠: 技師 iSpecialistCount=3
- 供給する資源: 鉄
- 供給数: 2
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な技師
  - `iGreatPeopleRateChange`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100

### Tower of Complacency - 愉悦の塔

- 内部名: `BUILDING_TOWER_OF_COMPLACENCY`
- 建造物クラス: 愉悦の塔
- コスト[ハンマー]: 750
- 必要テクノロジー: 精神圧搾
- 必要な宗教: 深海の旧支配者
- 必要な国教: 深海の旧支配者
- 倍速の資源: 精神のマナ iProductonModifier=50
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 1
  - `bNoUnhappiness`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -50
  - `iMilitaryProductionModifier`: -10
  - `fVisibilityPriority`: 100

### Infernal Grimoire - 地獄全書

- 内部名: `BUILDING_INFERNAL_GRIMOIRE`
- 建造物クラス: TXT_KEY_BUILDING_INFERNAL_GRIMOIRE
- コスト[ハンマー]: 400
- 必要テクノロジー: 地獄の契約
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な賢者
  - `iGreatPeopleRateChange`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iFreeTechs`: 1
  - `fVisibilityPriority`: 1

### Code of Junil - ユーニルの法典

- 内部名: `BUILDING_CODE_OF_JUNIL`
- 建造物クラス: ユーニルの法典
- 専門家枠: 商人 iSpecialistCount=1 / 神官 iSpecialistCount=2
- その他の設定:
  - `HolyCity`: 秩序の修道会
  - `ReligionType`: 秩序の修道会
  - `bStateReligion`: 1
  - `GlobalReligionCommerce`: 秩序の修道会
  - `ObsoleteSafeFreeBonuses`: 法のマナ iBonusCount=1 / 肉体のマナ iBonusCount=1
  - `GreatPeopleUnitClass`: 偉大な技師
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iGlobalGreatPeopleRateModifier`: 25
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `ReligionChanges`: 秩序の修道会 iReligionChange=1
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `iCrime`: -10

### Dies Diei - ディエス=ディエイ

- 内部名: `BUILDING_DIES_DIEI`
- 建造物クラス: ディエス=ディエイ
- 専門家枠: 神官 iSpecialistCount=1 / 賢者 iSpecialistCount=1
- その他の設定:
  - `HolyCity`: 至光なる天空
  - `ReligionType`: 至光なる天空
  - `bStateReligion`: 1
  - `GlobalReligionCommerce`: 至光なる天空
  - `ObsoleteSafeFreeBonuses`: 太陽のマナ iBonusCount=1 / 魂のマナ iBonusCount=1
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 2
  - `DiploVoteType`: DIPLOVOTE_OVERCOUNCIL
  - `bForceTeamVoteEligible`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iGlobalGreatPeopleRateModifier`: 25
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `ReligionChanges`: 至光なる天空 iReligionChange=1
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `UnitCombatFreeExperiences`: 信奉ユニット iExperience=2
  - `bSeeInvisible`: 1
  - `iCrime`: -10

### Tablets of Bambur - ボンブールの銘板

- 内部名: `BUILDING_TABLETS_OF_BAMBUR`
- 建造物クラス: ボンブールの銘板
- 専門家枠: 技師 iSpecialistCount=1 / 神官 iSpecialistCount=2
- 説明（ゲーム内ヘルプ）: ターン開始時に領内に資源が湧くことがある / （大地のマナを始めとする一部の資源により資源発生の確率上昇）
- その他の設定:
  - `HolyCity`: キルモフのルーン
  - `ReligionType`: キルモフのルーン
  - `bStateReligion`: 1
  - `GlobalReligionCommerce`: キルモフのルーン
  - `ObsoleteSafeFreeBonuses`: 大地のマナ iBonusCount=1 / 呪付のマナ iBonusCount=1
  - `GreatPeopleUnitClass`: 偉大な技師
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iGlobalGreatPeopleRateModifier`: 25
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `ReligionChanges`: キルモフのルーン iReligionChange=1
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Song of Autumn - 豊穣の賛歌

- 内部名: `BUILDING_SONG_OF_AUTUMN`
- 建造物クラス: 豊穣の賛歌
- 専門家枠: 吟遊詩人 iSpecialistCount=1 / 神官 iSpecialistCount=2
- その他の設定:
  - `HolyCity`: 緑葉の同胞
  - `ReligionType`: 緑葉の同胞
  - `bStateReligion`: 1
  - `GlobalReligionCommerce`: 緑葉の同胞
  - `ObsoleteSafeFreeBonuses`: 自然のマナ iBonusCount=1 / 生命のマナ iBonusCount=1
  - `GreatPeopleUnitClass`: 偉大な吟遊詩人
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iGlobalGreatPeopleRateModifier`: 25
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `ReligionChanges`: 緑葉の同胞 iReligionChange=1
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### The Necronomicon - ネクロノミコン

- 内部名: `BUILDING_THE_NECRONOMICON`
- 建造物クラス: ネクロノミコン
- 専門家枠: 神官 iSpecialistCount=2 / 賢者 iSpecialistCount=1
- 説明（ゲーム内ヘルプ）: 新規のナイトメアを持つユニットに20%の確率で鈍足を与える
- その他の設定:
  - `HolyCity`: 深海の旧支配者
  - `ReligionType`: 深海の旧支配者
  - `bStateReligion`: 1
  - `GlobalReligionCommerce`: 深海の旧支配者
  - `ObsoleteSafeFreeBonuses`: 水のマナ iBonusCount=1 / 古書物 iBonusCount=1
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iGlobalGreatPeopleRateModifier`: 25
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `ReligionChanges`: 深海の旧支配者 iReligionChange=1
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `iModifyGlobalCounter`: 3

### Nox Noctis - ノクス=ノクティス

- 内部名: `BUILDING_NOX_NOCTIS`
- 建造物クラス: ノクス=ノクティス
- 専門家枠: 吟遊詩人 iSpecialistCount=1 / 商人 iSpecialistCount=1
- その他の設定:
  - `HolyCity`: エススの枢密院
  - `ReligionType`: エススの枢密院
  - `bStateReligion`: 1
  - `GlobalReligionCommerce`: エススの枢密院
  - `ObsoleteSafeFreeBonuses`: 影のマナ iBonusCount=1 / 精神のマナ iBonusCount=1
  - `GreatPeopleUnitClass`: 偉大な商人
  - `iGreatPeopleRateChange`: 2
  - `DiploVoteType`: DIPLOVOTE_UNDERCOUNCIL
  - `bForceTeamVoteEligible`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iGlobalGreatPeopleRateModifier`: 25
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `ReligionChanges`: エススの枢密院 iReligionChange=1
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `UnitCombatFreeExperiences`: 偵察ユニット iExperience=2
  - `bHideUnits`: 1
  - `iCrime`: 10

### Stigmata on the Unborn - 宿命の烙印

- 内部名: `BUILDING_STIGMATA_ON_THE_UNBORN`
- 建造物クラス: 宿命の烙印
- 新規ユニットに昇進: 烙印
- 専門家枠: 神官 iSpecialistCount=2 / 賢者 iSpecialistCount=1
- その他の設定:
  - `HolyCity`: 蒼褪めたヴェール
  - `ReligionType`: 蒼褪めたヴェール
  - `bStateReligion`: 1
  - `GlobalReligionCommerce`: 蒼褪めたヴェール
  - `ObsoleteSafeFreeBonuses`: 不可逆のマナ iBonusCount=1 / 古書物 iBonusCount=1
  - `GreatPeopleUnitClass`: 偉大な賢者
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iGlobalGreatPeopleRateModifier`: 25
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `ReligionChanges`: 蒼褪めたヴェール iReligionChange=1
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `BonusYieldModifiers`: ナイトメア / 蛙 / 牛 / 豚 / 羊
  - `iModifyGlobalCounter`: 5

### Hope - 希望

- 内部名: `BUILDING_HOPE`
- 建造物クラス: 希望
- [幸福]: 1
- 産出(商業系): 4[文化]
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `SupplyPromotionProbabilities`: 勇気 iProbability=100
  - `bRequiresCaster`: 1

### Inspiration - 閃き

- 内部名: `BUILDING_INSPIRATION`
- 建造物クラス: 閃き
- 産出(商業系): 2[研究]
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な賢者
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `bRequiresCaster`: 1

### Unyielding Order - 揺るぎない秩序

- 内部名: `BUILDING_UNYIELDING_ORDER`
- 建造物クラス: NONE
- その他の設定:
  - `bNoUnhappiness`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -100
  - `fVisibilityPriority`: 1
  - `bRequiresCaster`: 1
  - `iCrime`: -10

### Wall of Stone - 石の壁

- 内部名: `BUILDING_WALL_OF_STONE`
- 建造物クラス: 石の壁
- [都市防御]: 25
- その他の設定:
  - `bNeverCapture`: 1
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `iAirModifier`: -25
  - `iBombardDefense`: 25
  - `fVisibilityPriority`: 10
  - `bRequiresCaster`: 1

### Customs House - 税関

- 内部名: `BUILDING_CUSTOM_HOUSE`
- 建造物クラス: 税関
- コスト[ハンマー]: 180
- 必要テクノロジー: 海図
- 必要な建造物: 港
- 産出[%]: +10[商業]
- 倍速の志向: 拡張志向 iProductionTrait=100 / 徴税志向 iProductionTrait=50
- その他の設定:
  - `bWater`: 1
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `iForeignTradeRouteModifier`: 100
  - `fVisibilityPriority`: 10
  - `SeaPlotYieldChanges`: +1[商業]

### Druid Runes - ドルイドのルーン

- 内部名: `BUILDING_DRUID_RUNES`
- 建造物クラス: ドルイドのルーン
- コスト[ハンマー]: 300
- 必要テクノロジー: 動物の極意
- 必要な建造物: 鎮守の杜
- [衛生]: 2
- 産出[%]: +10[商業]
- 専門家枠: 神官 iSpecialistCount=1 / 賢者 iSpecialistCount=1
- 説明（ゲーム内ヘルプ）: プラントか機械工場があると建造不可 / プラントと機械工場が建造できなくなる
- その他の設定:
  - `iMaxLatitude`: 90
  - `iHealRateChange`: 20
  - `fVisibilityPriority`: 10
  - `UnitCombatFreeExperiences`: 信奉ユニット iExperience=5
  - `SupplyPromotionProbabilities`: 病気 iProbability=-100 / 疫病 iProbability=-100 / 衰弱 iProbability=-100 / 黒死病 iProbability=-100
  - `BonusYieldModifiers`: 鹿 / 毛皮 / 象牙 / 薄闇樹

### Machinists Shop - 機械工場

- 内部名: `BUILDING_MACHINISTS_SHOP`
- 建造物クラス: 機械工場
- コスト[ハンマー]: 300
- 必要テクノロジー: 工学
- 追加で必要なテクノロジー: 蒸気機関
- 必要な建造物: 鍛冶屋
- 産出[%]: +20[ハンマー]
- 専門家枠: 技師 iSpecialistCount=1
- 説明（ゲーム内ヘルプ）: ドルイドのルーンがあると建造不可 / ドルイドのルーンが建造できなくなる
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `PowerYieldModifiers`: +20[ハンマー]
  - `BonusYieldModifiers`: ミスリル / 火薬

### Energy Plant - プラント

- 内部名: `BUILDING_ENERGY_PLANT`
- 建造物クラス: プラント
- コスト[ハンマー]: 300
- 必要テクノロジー: 蒸気機関
- 必要な建造物: 鍛冶屋
- [衛生]: -2
- 専門家枠: 技師 iSpecialistCount=1
- 無償の専門家: 技師 iFreeSpecialistCount=1
- 説明（ゲーム内ヘルプ）: ドルイドのルーンがあると建造不可 / ドルイドのルーンが建造できなくなる
- その他の設定:
  - `bPower`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Transition - 転移の台座

- 内部名: `BUILDING_TRANSITION`
- 建造物クラス: 転移の台座
- コスト[ハンマー]: 600
- 必要テクノロジー: 全知
- 必要な建造物: 黒曜石の門
- 倍速の資源: 次元のマナ iProductonModifier=100
- 説明（ゲーム内ヘルプ）: 異世界の兵が無作為に現れて配下に加わる
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iTradeRoutes`: 1
  - `fVisibilityPriority`: 1

### CulutureLevelBonus Refined - 文化レベル：洗練

- 内部名: `BUILDING_CULTURELEVEL_BONUS_REFINED`
- 建造物クラス: 文化レベル：洗練
- [幸福]: 1
- [衛生]: 1
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -5
  - `fVisibilityPriority`: 1

### CulutureLevelBonus Influential - 文化レベル：興隆

- 内部名: `BUILDING_CULTURELEVEL_BONUS_INFLUENTIAL`
- 建造物クラス: 文化レベル：興隆
- [幸福]: 2
- [衛生]: 2
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -10
  - `fVisibilityPriority`: 1

### CulutureLevelBonus Legendary - 文化レベル：伝説的

- 内部名: `BUILDING_CULTURELEVEL_BONUS_LEGENDARY`
- 建造物クラス: 文化レベル：伝説的
- [幸福]: 3
- [衛生]: 3
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iFreeSpecialist`: 2
  - `iMaintenanceModifier`: -20
  - `fVisibilityPriority`: 1

### Moai Statues - モアイ像

- 内部名: `BUILDING_MOAI_STATUES`
- 建造物クラス: モアイ像
- コスト[ハンマー]: 250
- 必要テクノロジー: 帆走
- 倍速の資源: 石材 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 1
  - `bWater`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `SeaPlotYieldChanges`: +1[ハンマー]
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Order of the One creator - 造物主の秩序

- 内部名: `BUILDING_ORDER_OF_THE_ONE_CREATOR`
- 建造物クラス: 造物主の秩序
- コスト[ハンマー]: 600
- 必要テクノロジー: 神々の本質
- 必要な建造物: 裁判所
- 倍速の資源: 石材 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な吟遊詩人
  - `iGreatPeopleRateChange`: 2
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iEnemyWarWearinessModifier`: 50
  - `fVisibilityPriority`: 100
  - `StateReligionCommerces`: 4[文化]
  - `PrereqBuildingClasses`: 裁判所 iNumBuildingNeeded=3
  - `iGlobalResistModify`: 25

### Magic circle of the curse - 呪詛の魔法陣

- 内部名: `BUILDING_MAGIC_CIRCLE_OF_THE_CURSE`
- 建造物クラス: 呪詛の魔法陣
- 必要テクノロジー: 邪悪への道
- 専門家枠: 賢者 iSpecialistCount=1
- 説明（ゲーム内ヘルプ）: 皐の病を解禁
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な賢者
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `UnitCombatFreeExperiences`: 秘術ユニット iExperience=1

### Magic circle of the sadness - 荒廃の魔法陣

- 内部名: `BUILDING_MAGIC_CIRCLE_OF_THE_SADNESS`
- 建造物クラス: 荒廃の魔法陣
- コスト[ハンマー]: 200
- 必要テクノロジー: 屍霊術
- 必要な建造物: 呪詛の魔法陣
- [幸福]: 1
- 説明（ゲーム内ヘルプ）: 黒い雨を解禁
- その他の設定:
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `UnitCombatFreeExperiences`: 秘術ユニット iExperience=2

### Magic circle of the devastation - 復活の魔法陣

- 内部名: `BUILDING_MAGIC_CIRCLE_OF_THE_DEVASTATION`
- 建造物クラス: 復活の魔法陣
- 必要テクノロジー: 魔術
- 必要な建造物: 荒廃の魔法陣
- 新規ユニットに昇進: 不浄の聖痕
- 説明（ゲーム内ヘルプ）: 魂返しを解禁
- その他の設定:
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `UnitCombatFreeExperiences`: 秘術ユニット iExperience=1
  - `SupplyPromotionProbabilities`: 不浄の聖痕 iProbability=100
  - `SpecialistYieldChanges`: 賢者 +1[ハンマー] / 偉大な賢者 +2[ハンマー]

### Magic circle of the calamity - 災禍の魔法陣

- 内部名: `BUILDING_MAGIC_CIRCLE_OF_THE_CALAMITY`
- 建造物クラス: 災禍の魔法陣
- コスト[ハンマー]: 400
- 必要テクノロジー: 聖職
- 必要な建造物: 復活の魔法陣
- 説明（ゲーム内ヘルプ）: 天地の災いを解禁
- その他の設定:
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `UnitCombatFreeExperiences`: 秘術ユニット iExperience=1

### Magic circle of the rage - 憤怒の魔法陣

- 内部名: `BUILDING_MAGIC_CIRCLE_OF_THE_RAGE`
- 建造物クラス: 憤怒の魔法陣
- 必要テクノロジー: 狂信
- 必要な建造物: 災禍の魔法陣
- 専門家枠: 賢者 iSpecialistCount=1
- 説明（ゲーム内ヘルプ）: 狂戦士の祝祭を解禁
- その他の設定:
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `UnitCombatFreeExperiences`: 秘術ユニット iExperience=2
  - `iModifyGlobalCounter`: 1

### Magic circle of the black death - 黒死の魔法陣

- 内部名: `BUILDING_MAGIC_CIRCLE_OF_THE_BLACK_DEATH`
- 建造物クラス: 黒死の魔法陣
- コスト[ハンマー]: 800
- 必要テクノロジー: 悪意の企み
- 必要な建造物: 憤怒の魔法陣
- 新規ユニットに昇進: 屍霊術
- 説明（ゲーム内ヘルプ）: 黒の烙印を解禁
- その他の設定:
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `UnitCombatFreeExperiences`: 秘術ユニット iExperience=1
  - `SupplyPromotionProbabilities`: 屍霊術 iProbability=100
  - `iModifyGlobalCounter`: 2

### Magic circle of the hollow - 虚無の魔法陣

- 内部名: `BUILDING_MAGIC_CIRCLE_OF_THE_HOLLOW`
- 建造物クラス: 虚無の魔法陣
- 必要テクノロジー: 意志の力
- 必要な建造物: 黒死の魔法陣
- 新規ユニットに昇進: 次元Ⅰ
- 専門家枠: 賢者 iSpecialistCount=1
- 説明（ゲーム内ヘルプ）: 闇の門を解禁
- その他の設定:
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `UnitCombatFreeExperiences`: 秘術ユニット iExperience=2
  - `SupplyPromotionProbabilities`: 次元Ⅰ iProbability=100
  - `SpecialistYieldChanges`: 賢者 +1[ハンマー] / 偉大な賢者 +2[ハンマー]
  - `iModifyGlobalCounter`: 3

### Magic circle of the end - 終末の魔法陣

- 内部名: `BUILDING_MAGIC_CIRCLE_OF_THE_END`
- 建造物クラス: 終末の魔法陣
- コスト[ハンマー]: 1600
- 必要テクノロジー: 全知
- 必要な建造物: 虚無の魔法陣
- 新規ユニットに昇進: 烙印
- 専門家枠: 賢者 iSpecialistCount=1
- 説明（ゲーム内ヘルプ）: 終末への導きを解禁
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 1
  - `bGoldenAge`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `UnitCombatFreeExperiences`: 秘術ユニット iExperience=2
  - `SupplyPromotionProbabilities`: 烙印 iProbability=100
  - `SpecialistYieldChanges`: 賢者 +1[ハンマー] / 偉大な賢者 +2[ハンマー]
  - `iModifyGlobalCounter`: 5

### Vacant Mausoleum - 空の霊廟

- 内部名: `BUILDING_VACANT_MAUSOLEUM`
- 建造物クラス: 空の霊廟
- コスト[ハンマー]: 200
- 必要テクノロジー: 神秘主義
- 倍速の志向: 創造志向 iProductionTrait=100
- 倍速の資源: 石材 iProductonModifier=100
- その他の設定:
  - `FreeBuilding`: 記念碑
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Temple of Dagda - ダグダの大神殿

- 内部名: `BUILDING_TEMPLE_OF_DAGDA`
- 建造物クラス: ダグダの大神殿
- コスト[ハンマー]: 250
- 必要テクノロジー: 地図
- 無償の専門家: 商人 iFreeSpecialistCount=1
- 倍速の資源: 大理石 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な商人
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iTradeRouteModifier`: 100
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Sphinx - 問い掛けるものの石像

- 内部名: `BUILDING_SPHINX`
- 建造物クラス: 問い掛けるものの石像
- コスト[ハンマー]: 350
- 必要テクノロジー: 石工
- 倍速の資源: 石材 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な技師
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iWorkerSpeedModifier`: 50
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Idol of Saint - 聖者の偶像

- 内部名: `BUILDING_IDOL_OF_SAINT`
- 建造物クラス: 聖者の偶像
- コスト[ハンマー]: 500
- 必要テクノロジー: 聖職
- 追加で必要なテクノロジー: 叡智への道
- 陳腐化: 悪意の企み
- 無償の専門家: 神官 iFreeSpecialistCount=1
- 倍速の資源: 大理石 iProductonModifier=100
- その他の設定:
  - `MaxStartEra`: 未来
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 2
  - `bTeamShare`: 1
  - `bNukeImmune`: 1
  - `bAllCities`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 8[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `FreePromotionProbabilities`: 監視者の証 iProbability=20
  - `iModifyGlobalCounter`: -5

### Goodreau statue - グッドレオーの大理石像

- 内部名: `BUILDING_GOODREAU_STATUE`
- 建造物クラス: グッドレオーの大理石像
- コスト[ハンマー]: 120
- 必要テクノロジー: 探検
- 新規ユニットに昇進: 冒険者
- 倍速の志向: 探求志向 iProductionTrait=100
- 倍速の資源: 大理石 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 2
  - `bTeamShare`: 1
  - `bNukeImmune`: 1
  - `bAllCities`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Water of Trenton - トレントンの聖水

- 内部名: `BUILDING_WATER_OF_TRENTON`
- 建造物クラス: トレントンの聖水
- コスト[ハンマー]: 500
- 必要テクノロジー: 交易
- 倍速の資源: 水のマナ iProductonModifier=100
- その他の設定:
  - `CivicOption`: 宗教制度
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 2
  - `bWater`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `iFreeSpecialist`: 1
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 12[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Tower of Herve - エルヴェの塔

- 内部名: `BUILDING_TOWER_OF_HERVE`
- 建造物クラス: エルヴェの塔
- コスト[ハンマー]: 800
- 必要テクノロジー: 野生の触れ合い
- 倍速の資源: 大理石 iProductonModifier=100 / 自然のマナ iProductonModifier=100
- その他の設定:
  - `FreeBuilding`: 鎮守の杜
  - `AllowCivics`: 自由主義
  - `GreatPeopleUnitClass`: 偉大な吟遊詩人
  - `iGreatPeopleRateChange`: 2
  - `bGoldenAge`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iGlobalGreatPeopleRateModifier`: 50
  - `iGoldenAgeModifier`: 50
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 10[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Greed of Velgyr - ヴェルギュールの強欲

- 内部名: `BUILDING_GREED_OF_VELGYR`
- 建造物クラス: ヴェルギュールの強欲
- コスト[ハンマー]: 550
- 必要テクノロジー: 光学
- 倍速の資源: 呪付のマナ iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な商人
  - `iGreatPeopleRateChange`: 2
  - `bWater`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `GlobalSeaPlotYieldChanges`: +1[商業]
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Three-Field Order - 三圃組合

- 内部名: `BUILDING_THREEFIELD_ORDER`
- 建造物クラス: 三圃組合
- コスト[ハンマー]: 350
- 必要テクノロジー: 祝祭
- 必要な建造物: 穀倉
- その他の設定:
  - `FreeBuilding`: 穀倉
  - `GreatPeopleUnitClass`: 偉大な商人
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `BonusHealthChanges`: トウモロコシ iHealthChange=1 / 米 iHealthChange=1 / 小麦 iHealthChange=1 / 亜麻 iHealthChange=1 / ジャガイモ iHealthChange=1

### Ratcatcher Guild - 鼠捕りギルド

- 内部名: `BUILDING_RATCATCHERS_GUILD`
- 建造物クラス: 鼠捕りギルド
- コスト[ハンマー]: 550
- 必要テクノロジー: 毒物
- 必要な建造物: 狩猟小屋
- 産出(商業系)[%]: 10[ゴールド]
- 倍速の資源: 影のマナ iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 1
  - `bNukeImmune`: 1
  - `bAllCities`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iAllCityDefense`: 25
  - `fVisibilityPriority`: 100
  - `UnitCombatFreeExperiences`: 偵察ユニット iExperience=5
  - `UnitCombatFreePromotionPicks`: 偵察ユニット iFreePromotionPick=1
  - `PrereqBuildingClasses`: 狩猟小屋 iNumBuildingNeeded=3
  - `iCrime`: 20

### Leucetious's Atelier - レウケティオスのアトリエ

- 内部名: `BUILDING_LEUCETIOUS_ATELIER`
- 建造物クラス: レウケティオスのアトリエ
- コスト[ハンマー]: 1000
- 必要テクノロジー: 鉄器
- [衛生]: -2
- 専門家枠: 技師 iSpecialistCount=3
- 倍速の資源: 生命のマナ iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な技師
  - `iGreatPeopleRateChange`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `BonusYieldModifiers`: 鉄 / 塩 / キノコ

### Circle of Eight - 八魔陣

- 内部名: `BUILDING_CIRCLE_OF_EIGHT`
- 建造物クラス: 八魔陣
- コスト[ハンマー]: 1200
- 必要テクノロジー: 錬金術
- 産出(商業系)[%]: 50[研究]
- 供給する資源: 超魔術のマナ
- 供給数: 1
- 倍速の資源: 金 iProductonModifier=100
- その他の設定:
  - `FreeBuilding`: 錬金術ラボ
  - `GreatPeopleUnitClass`: 偉大な賢者
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Guild of Endeavors - 労働者ギルド

- 内部名: `BUILDING_GUILD_OF_ENDEAVORS`
- 建造物クラス: 労働者ギルド
- コスト[ハンマー]: 800
- 必要テクノロジー: 税制
- 倍速の志向: 宗教志向 iProductionTrait=50
- 倍速の資源: 石材 iProductonModifier=100
- その他の設定:
  - `AllowCivics`: ギルド制
  - `GreatPeopleUnitClass`: 偉大な技師
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iAnarchyModifier`: -100
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1

### Brewing of Creation - 創造の酒造

- 内部名: `BUILDING_BREWING_OF_CREATION`
- 建造物クラス: 創造の酒造
- コスト[ハンマー]: 1200
- 必要テクノロジー: 医薬
- [幸福]: 3
- [衛生]: 3
- 倍速の資源: 肉体のマナ iProductonModifier=50 / 呪付のマナ iProductonModifier=50 / 生命のマナ iProductonModifier=50
- 説明（ゲーム内ヘルプ）: 川沿い都市にのみ建設可能
- その他の設定:
  - `PrereqAndBonuses`: 自然のマナ
  - `bRiver`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iAreaHealth`: 2
  - `iGlobalHealth`: 1
  - `iAreaHappiness`: 2
  - `iGlobalHappiness`: 1
  - `fVisibilityPriority`: 100
  - `RiverPlotYieldChanges`: 1[ゴールド]
  - `ObsoleteSafeCommerceChanges`: 10[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: bCommerceChangeOriginalOwner=1
  - `BonusYieldModifiers`: 自然のマナ / 肉体のマナ / 呪付のマナ / 生命のマナ

### Wyrmhold - ワイアーム砦

- 内部名: `BUILDING_WYRMHOLD`
- 建造物クラス: ワイアーム砦
- 専門家枠: 神官 iSpecialistCount=3
- その他の設定:
  - `HolyCity`: ドラゴン崇拝
  - `ReligionType`: ドラゴン崇拝
  - `GlobalReligionCommerce`: ドラゴン崇拝
  - `ObsoleteSafeFreeBonuses`: 炎のマナ iBonusCount=1
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 2
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `ReligionChanges`: ドラゴン崇拝 iReligionChange=1
  - `CommerceChangeOriginalOwners`: 1[研究], 1[文化]

### Shrine of Junil - ユーニルの祭壇

- 内部名: `BUILDING_SHRINE_OF_JUNIL`
- 建造物クラス: ユーニルの祭壇
- コスト[ハンマー]: 600
- 必要テクノロジー: 宗教法
- 説明（ゲーム内ヘルプ）: 善良の指導者のみ
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iFreeTechs`: 1
  - `fVisibilityPriority`: 100

### TXT_KEY_EQUIPMENT_FROZEN_FLAME - TXT_KEY_EQUIPMENT_FROZEN_FLAME

- 内部名: `BUILDING_FROZEN_FLAME`
- 建造物クラス: TXT_KEY_EQUIPMENT_FROZEN_FLAME
- [幸福]: -3
- 供給する資源: 混沌のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 不可逆のマナ iBonusCount=1 / 炎のマナ iBonusCount=1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `iMilitaryProductionModifier`: 100
  - `fVisibilityPriority`: 100

### Earth Pulse - 地脈の戦槌

- 内部名: `BUILDING_EARTH_PULSE`
- 建造物クラス: TXT_KEY_BUILDING_EARTH_PULSE
- コスト[ハンマー]: 120
- 必要テクノロジー: 千仞の尾根
- 必要な宗教: キルモフのルーン
- 必要な国教: キルモフのルーン
- その他の設定:
  - `HolyCity`: キルモフのルーン
  - `ReligionType`: キルモフのルーン
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Glorious Shield - 栄光の盾

- 内部名: `BUILDING_GLORIOUS_SHIELD`
- 建造物クラス: TXT_KEY_BUILDING_GLORIOUS_SHIELD
- コスト[ハンマー]: 120
- 必要テクノロジー: 天界からの指令
- 必要な宗教: 秩序の修道会
- 必要な国教: 秩序の修道会
- その他の設定:
  - `HolyCity`: 秩序の修道会
  - `ReligionType`: 秩序の修道会
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Bracelet of Nightmare - 夢魔の腕輪

- 内部名: `BUILDING_BRACELET_OF_NIGHTMARE`
- 建造物クラス: TXT_KEY_BUILDING_BRACELET_OF_NIGHTMARE
- コスト[ハンマー]: 120
- 必要テクノロジー: 精神圧搾
- 必要な宗教: 深海の旧支配者
- 必要な国教: 深海の旧支配者
- その他の設定:
  - `HolyCity`: 深海の旧支配者
  - `ReligionType`: 深海の旧支配者
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Orb of Yggdrasil - 世界樹の宝珠

- 内部名: `BUILDING_ORB_OF_YGGFRASIL`
- 建造物クラス: TXT_KEY_BUILDING_ORB_OF_YGGFRASIL
- コスト[ハンマー]: 120
- 必要テクノロジー: 秘密の抜け道
- 必要な宗教: 緑葉の同胞
- 必要な国教: 緑葉の同胞
- その他の設定:
  - `HolyCity`: 緑葉の同胞
  - `ReligionType`: 緑葉の同胞
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Demon's Fang - 悪魔の牙

- 内部名: `BUILDING_DEMONS_FANG`
- 建造物クラス: TXT_KEY_BUILDING_DEMONS_FANG
- コスト[ハンマー]: 120
- 必要テクノロジー: 詐欺
- 必要な宗教: エススの枢密院
- 必要な国教: エススの枢密院
- その他の設定:
  - `HolyCity`: エススの枢密院
  - `ReligionType`: エススの枢密院
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Ring of the Sun - 太陽の指輪

- 内部名: `BUILDING_RING_OF_THE_SUN`
- 建造物クラス: TXT_KEY_BUILDING_RING_OF_THE_SUN
- コスト[ハンマー]: 120
- 必要テクノロジー: 宗教法
- 必要な宗教: 至光なる天空
- 必要な国教: 至光なる天空
- その他の設定:
  - `HolyCity`: 至光なる天空
  - `ReligionType`: 至光なる天空
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Bloody Oath - 血塗れた誓いの剣

- 内部名: `BUILDING_BLOODY_OATH`
- 建造物クラス: TXT_KEY_BUILDING_BLOODY_OATH
- コスト[ハンマー]: 120
- 必要テクノロジー: 魂の堕落
- 必要な宗教: 蒼褪めたヴェール
- 必要な国教: 蒼褪めたヴェール
- その他の設定:
  - `HolyCity`: 蒼褪めたヴェール
  - `ReligionType`: 蒼褪めたヴェール
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Temple of Junil - ユーニルの神殿

- 内部名: `BUILDING_BANNOR_TEMPLE`
- 固有: バンノール（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -10
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1
  - `iCrime`: -10

### Temple Library - 修道院

- 内部名: `BUILDING_TEMPLE_LIBRARY`
- 固有: イース・エロヒム・バンノール・マラキム（図書館 の代替）
- 建造物クラス: 図書館
- コスト[ハンマー]: 100
- 必要テクノロジー: 筆記
- 産出(商業系)[%]: 25[研究]
- 専門家枠: 神官 iSpecialistCount=1 / 賢者 iSpecialistCount=1
- 倍速の志向: 哲学志向 iProductionTrait=100 / 賢人志向 iProductionTrait=50
- その他の設定:
  - `FreeStartEra`: 未来
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10

### Temple Courthouse - 枢密院

- 内部名: `BUILDING_TEMPLE_COURTHOUSE`
- 固有: イース・エロヒム・バンノール・マラキム（裁判所 の代替）
- 建造物クラス: 裁判所
- コスト[ハンマー]: 100
- 必要テクノロジー: 法律
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 組織志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 未来
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -30
  - `fVisibilityPriority`: 10
  - `iCrime`: -10

### Arc - 至聖所

- 内部名: `BUILDING_ARC`
- 固有: バンノール（民族叙事詩 の代替）
- 建造物クラス: 民族叙事詩
- コスト[ハンマー]: 250
- 必要テクノロジー: 軍事行動
- 必要な建造物: 図書館
- 倍速の資源: 大理石 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iGreatPeopleRateModifier`: 100
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `ImprovementFreeSpecialists`: 砦 iFreeSpecialistCount=1 / 城 iFreeSpecialistCount=1 / 城塞 iFreeSpecialistCount=1 / 要塞 iFreeSpecialistCount=1

### One Thousand and One Nights - 千夜一夜物語

- 内部名: `BUILDING_MALAKIM_NATIONAL_EPIC`
- 固有: マラキム（民族叙事詩 の代替）
- 建造物クラス: 民族叙事詩
- コスト[ハンマー]: 250
- 必要テクノロジー: 軍事行動
- 必要な建造物: 図書館
- 倍速の資源: 大理石 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な預言者
  - `iGreatPeopleRateChange`: 2
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iGreatPeopleRateModifier`: 100
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `StateReligionCommerces`: 1[研究], 1[文化]
  - `UnitCombatFreeExperiences`: 信奉ユニット iExperience=2

### Oracle of Siriona - シロナの神託所

- 内部名: `BUILDING_ELOHIM_TEMPLE`
- 固有: エロヒム（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iHealRateChange`: 5
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1
  - `UnitCombatFreeExperiences`: 信奉ユニット iExperience=2
  - `RemovePromotion`: 衰弱

### Sacred Arc - 聖櫃

- 内部名: `BUILDING_MERCURIANS_TEMPLE`
- 固有: マーキュリアン（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出[%]: +10[食料]
- 産出(商業系)[%]: 20[文化]
- 新規ユニットに昇進: 祝福
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Forge of Nantosuelta - ナントスエルタの鍛冶場

- 内部名: `BUILDING_LUCHUIRP_TEMPLE`
- 固有: ルシュイアープ（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な技師
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Golem Workshop - ゴーレムの工房

- 内部名: `BUILDING_LUCHUIRP_FORGE`
- 固有: ルシュイアープ（鍛冶屋 の代替）
- 建造物クラス: 鍛冶屋
- コスト[ハンマー]: 150
- 必要テクノロジー: 製錬
- 産出: +2[ハンマー]
- 産出[%]: +20[ハンマー]
- 専門家枠: 技師 iSpecialistCount=1
- 倍速の志向: 勤労志向 iProductionTrait=100 / 軍事志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `BonusHappinessChanges`: 金 iHappinessChange=2
  - `SupplyPromotionProbabilities`: 武器の腐食 iProbability=-50
  - `BonusYieldModifiers`: 鉄 / 象牙 / 大理石 / ミスリル

### Temple to Amathaon - アマサオンの神殿

- 内部名: `BUILDING_KURIOTATES_TEMPLE`
- 固有: クリオテイテ（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- [幸福]: 1
- [衛生]: 1
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Grove of Cernunnos - ケルヌンノスの杜

- 内部名: `BUILDING_LJOSALFAR_TEMPLE`
- 固有: リョースアールヴ（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 新規ユニットに昇進: ゲリラⅡ
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1
  - `UnitCombatFreeExperiences`: 弓術ユニット iExperience=2

### Cave of Kilmorph - キルモフの洞穴

- 内部名: `BUILDING_KHAZAD_TEMPLE`
- 固有: カザード（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 10[ゴールド], 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Sanctum - 聖所

- 内部名: `BUILDING_SIDAR_TEMPLE`
- 固有: シダー（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iAllCityDefense`: 5
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1
  - `iGlobalResistModify`: 5

### Danalin's Spring - ダナリンの湧水

- 内部名: `BUILDING_LANUN_TEMPLE`
- 固有: ラヌーン（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iTradeRoutes`: 1
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Dagda's Memorial - ダグダの記念碑

- 内部名: `BUILDING_GRIGORI_TEMPLE`
- 固有: グリゴリ（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iGlobalGreatPeopleRateModifier`: 3
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Adventurer meeting - 冒険者集会

- 内部名: `BUILDING_ADVENTURE_MEETING`
- 固有: グリゴリ（巡業サーカス の代替）
- 建造物クラス: 巡業サーカス
- コスト[ハンマー]: 100
- 必要テクノロジー: 祝祭
- 陳腐化: 蒸気機関
- 必要な資源（いずれか）: エール酒 / ワイン
- [幸福]: 1
- 産出[%]: +5[商業]
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 吟遊詩人 iSpecialistCount=1
- 倍速の志向: 創造志向 iProductionTrait=100
- その他の設定:
  - `MaxStartEra`: 未来
  - `GreatPeopleUnitClass`: 冒険者
  - `iGreatPeopleRateChange`: 2
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `BonusHealthChanges`: 米 iHealthChange=2
  - `BonusHappinessChanges`: 米 iHappinessChange=2
  - `BonusYieldModifiers`: エール酒
  - `iCrime`: 5

### Tower of Winds - 風の塔

- 内部名: `BUILDING_HIPPUS_TEMPLE`
- 固有: ヒッパス（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1
  - `UnitCombatFreeExperiences`: 騎乗ユニット iExperience=2

### Library of Oghma - オグマの図書館

- 内部名: `BUILDING_AMURITES_TEMPLE`
- 固有: アムリテ（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1
  - `UnitCombatFreeExperiences`: 秘術ユニット iExperience=2

### Arcane court - 秘術法廷

- 内部名: `BUILDING_ARCANE_COURT`
- 固有: アムリテ（裁判所 の代替）
- 建造物クラス: 裁判所
- コスト[ハンマー]: 100
- 必要テクノロジー: 法律
- [幸福]: -2
- 専門家枠: 賢者 iSpecialistCount=1
- 倍速の志向: 組織志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 未来
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -25
  - `fVisibilityPriority`: 10
  - `BonusHappinessChanges`: 超魔術のマナ iHappinessChange=1 / 肉体のマナ iHappinessChange=1 / 呪付のマナ iHappinessChange=1 / 自然のマナ iHappinessChange=1 / 炎のマナ iHappinessChange=1 / 大気のマナ iHappinessChange=1 / 大地のマナ iHappinessChange=1 / 水のマナ iHappinessChange=1
  - `iCrime`: -10

### Mage study - 魔導書院

- 内部名: `BUILDING_MAGE_STUDY`
- 固有: アムリテ（図書館 の代替）
- 建造物クラス: 図書館
- コスト[ハンマー]: 100
- 必要テクノロジー: 筆記
- [衛生]: -2
- 産出(商業系)[%]: 25[研究]
- 専門家枠: 賢者 iSpecialistCount=2
- 倍速の志向: 哲学志向 iProductionTrait=100 / 賢人志向 iProductionTrait=50
- その他の設定:
  - `FreeStartEra`: 未来
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `BonusHealthChanges`: 超魔術のマナ iHealthChange=1 / 死のマナ iHealthChange=1 / 混沌のマナ iHealthChange=1 / 不可逆のマナ iHealthChange=1 / 影のマナ iHealthChange=1 / 太陽のマナ iHealthChange=1 / 生命のマナ iHealthChange=1 / 精神のマナ iHealthChange=1 / 魂のマナ iHealthChange=1 / 法のマナ iHealthChange=1

### Berserkers' Pit - 狂戦士の闘技場

- 内部名: `BUILDING_DOVIELLO_TEMPLE`
- 固有: ドヴィエロ（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1
  - `UnitCombatFreeExperiences`: 白兵ユニット iExperience=2

### Mammon's Carnival - マンモンの巡業サーカス

- 内部名: `BUILDING_BALSERAPHS_TEMPLE`
- 固有: バルセラフ（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 30[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な吟遊詩人
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Bhall's Pyre - バアルの篝火

- 内部名: `BUILDING_CLAN_TEMPLE`
- 固有: 残り火一族（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `iHurryAngerModifier`: -25
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iWarWearinessModifier`: -10
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Sacrificial Altar - 生贄の祭壇

- 内部名: `BUILDING_CLAN_COURTHOUSE`
- 固有: 残り火一族（裁判所 の代替）
- 建造物クラス: 裁判所
- コスト[ハンマー]: 120
- 必要テクノロジー: 法律
- 産出[%]: +10[食料]
- 倍速の志向: 組織志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 未来
  - `iHurryAngerModifier`: -25
  - `iMaxLatitude`: 90
  - `iGreatPeopleRateModifier`: -20
  - `iMaintenanceModifier`: -40
  - `fVisibilityPriority`: 10
  - `iCrime`: -10

### Den of Esus - エススの隠れ家

- 内部名: `BUILDING_SVARTALFAR_TEMPLE`
- 固有: スヴァルトアールヴ（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 新規ユニットに昇進: 森番Ⅱ
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1
  - `UnitCombatFreeExperiences`: 偵察ユニット iExperience=2

### Pit of Slaughter - 屠殺穴

- 内部名: `BUILDING_CALABIM_TEMPLE`
- 固有: カラビム（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iFoodKept`: 10
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Observatory of Ceridwen - ケリドウェンの観測所

- 内部名: `BUILDING_SHEAIM_TEMPLE`
- 固有: シェアイム（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 10[研究], 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Gate of Agares - アガレスの門

- 内部名: `BUILDING_INFERNAL_TEMPLE`
- 固有: 地獄の軍勢（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 新規ユニットに昇進: 烙印
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Lizard Cage - リザードマンの檻

- 内部名: `BUILDING_LIZARD_CAGE`
- 建造物クラス: リザードマンの檻
- [幸福]: 1
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な吟遊詩人
  - `iGreatPeopleRateChange`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Gate of Different layer - 異層の門

- 内部名: `BUILDING_GATE_OF_DIFFERENT_LAYER`
- 建造物クラス: 異層の門
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iAirlift`: 8
  - `fVisibilityPriority`: 1
  - `bRequiresCaster`: 1

### Aggressive - 攻撃志向

- 内部名: `BUILDING_AGGRESSIVE`
- 建造物クラス: 攻撃志向
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMilitaryProductionModifier`: 10
  - `fVisibilityPriority`: 1

### Creative - 創造志向

- 内部名: `BUILDING_CREATIVE`
- 建造物クラス: 創造志向
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `CommerceHappinesses`: 10[文化]
  - `BonusHappinessChanges`: 染料 iHappinessChange=1

### Portal - ポータル

- 内部名: `BUILDING_SUMMONER`
- 建造物クラス: ポータル
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iAirlift`: 1
  - `iTradeRoutes`: 1
  - `fVisibilityPriority`: 1

### Agnostic - 無神論者

- 内部名: `BUILDING_AGNOSTIC`
- 建造物クラス: 無神論者
- コスト[ハンマー]: 180
- 必要テクノロジー: 筆記
- 必要な志向: 無神論志向
- 産出(商業系): 1[ゴールド], 1[研究]
- 産出(商業系)[%]: 20[文化]
- 倍速の志向: 伝道志向 iProductionTrait=100
- その他の設定:
  - `HappinessTraits`: 宗教志向 iHappinessTrait=1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMilitaryProductionModifier`: 10
  - `fVisibilityPriority`: 10

### Great People - 不世出の偉人

- 内部名: `BUILDING_GREAT_PEOPLE`
- 建造物クラス: 不世出の偉人
- 説明（ゲーム内ヘルプ）: +1: 不満な市民 / +5: 不満な市民
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `AngryYields`: +4[商業]

### Crazy by Worldheritage - 遺産狂

- 内部名: `BUILDING_CRAZY_BY_WORLDHERITAGE`
- 建造物クラス: 遺産狂
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMilitaryProductionModifier`: -40
  - `fVisibilityPriority`: 10

### Imperialist - 帝国主義志向

- 内部名: `BUILDING_IMPERIALIST`
- 建造物クラス: 帝国主義志向
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iGoldenAgeModifier`: 25
  - `iWorkerSpeedModifier`: 25
  - `fVisibilityPriority`: 10

### Branch - Neutral - 支部

- 内部名: `BUILDING_RICHS`
- 建造物クラス: 支部
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Branch - Poor - 貧弱な支部

- 内部名: `BUILDING_RICHS_EMPTY`
- 建造物クラス: 支部
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Branch - Immature - 未熟な支部

- 内部名: `BUILDING_RICHS_NONE`
- 建造物クラス: 支部
- 産出[%]: +5[ハンマー], +5[商業]
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Branch - Developing - 発展途上の支部

- 内部名: `BUILDING_RICHS_SMALL`
- 建造物クラス: 支部
- 産出[%]: +10[ハンマー], +10[商業]
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Branch - Luxurious - 豪華な支部

- 内部名: `BUILDING_RICHS_SAVED`
- 建造物クラス: 支部
- 産出[%]: +15[ハンマー], +15[商業]
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -5
  - `fVisibilityPriority`: 1

### Branch - Tremendous - 凄まじい支部

- 内部名: `BUILDING_RICHS_STUCKED`
- 建造物クラス: 支部
- 産出[%]: +25[ハンマー], +25[商業]
- 供給する資源: 琥珀
- 供給数: 1
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -10
  - `fVisibilityPriority`: 1

### Branch - Startle - 驚愕の支部

- 内部名: `BUILDING_RICHS_STUCKED_1`
- 建造物クラス: 支部
- 産出[%]: +5[食料], +35[ハンマー], +35[商業]
- 供給する資源: 琥珀
- 供給数: 1
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -15
  - `fVisibilityPriority`: 1

### Branch - Legendary - 伝説の支部

- 内部名: `BUILDING_RICHS_STUCKED_2`
- 建造物クラス: 支部
- 産出[%]: +10[食料], +50[ハンマー], +50[商業]
- 供給する資源: 琥珀
- 供給数: 1
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -25
  - `fVisibilityPriority`: 1

### Agricultural - 農耕志向

- 内部名: `BUILDING_AGRICULTURAL`
- 建造物クラス: 農耕志向
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iFoodKept`: 20
  - `fVisibilityPriority`: 10

### Construction - 建設志向

- 内部名: `BUILDING_CONSTRUCTION`
- 建造物クラス: 建設志向
- 無償の専門家: 特別市民 iFreeSpecialistCount=1
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10

### Martyrdom - 殉死志向

- 内部名: `BUILDING_MARTYRDOM`
- 建造物クラス: 殉死志向
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iWarWearinessModifier`: -20
  - `fVisibilityPriority`: 1

### Echigo Palace - エチゴの宮殿

- 内部名: `BUILDING_PALACE_ECHIGO`
- 固有: エチゴ（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 塩
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 金 iBonusCount=1 / 真珠 iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `BonusHealthChanges`: 貝 iHealthChange=1 / 蟹 iHealthChange=1 / 魚 iHealthChange=1 / 海老 iHealthChange=1
  - `BonusHappinessChanges`: 米 iHappinessChange=1 / 貝 iHappinessChange=1 / 蟹 iHappinessChange=1 / 魚 iHappinessChange=1 / 海老 iHealthChange=1
  - `iCrime`: -10

### Bisyamontenbyou - 毘沙門天廟

- 内部名: `BUILDING_PAGAN_TEMPLE_ECHIGO`
- 固有: エチゴ（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMilitaryProductionModifier`: 10
  - `fVisibilityPriority`: 100
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Dojo - 道場

- 内部名: `BUILDING_TRAINING_YARD_ECHIGO`
- 固有: エチゴ（練兵場 の代替）
- 建造物クラス: 練兵場
- コスト[ハンマー]: 60
- 必要テクノロジー: 青銅器
- 倍速の志向: 軍事志向 iProductionTrait=100 / TXT_KEY_TRAIT_IMPERIALIST iProductionTrait=50
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 2
  - `UnitCombatFreeExperiences`: 白兵ユニット iExperience=2

### Kenshin Throne - 上杉謙信の玉座

- 内部名: `BUILDING_KENSIN_THRONE_ECHIGO`
- 固有: エチゴ（英雄叙事詩 の代替）
- 建造物クラス: 英雄叙事詩
- コスト[ハンマー]: 200
- 必要テクノロジー: 軍事戦略
- 倍速の資源: 薄闇樹 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -25
  - `iMilitaryProductionModifier`: 100
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceChangeOriginalOwners`: 1[文化]

### Kagura - 神楽

- 内部名: `BUILDING_KAGURA_ECHIGO`
- 建造物クラス: 神楽
- [幸福]: 5
- 産出(商業系): 4[文化]
- 産出(商業系)[%]: 50[文化]
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `bRequiresCaster`: 1

### Droaum Palace - ドロアウムの宮殿

- 内部名: `BUILDING_PALACE_DROAUM`
- 固有: ドロアウム（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 精神のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 死のマナ iBonusCount=1 / 炎のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -30
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Temple of Rebirth - 救世の神殿

- 内部名: `BUILDING_DROAUM_TEMPLE`
- 固有: ドロアウム（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系): 2[研究]
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Pandora's box (Empty) - パンドラの箱（空っぽ）

- 内部名: `BUILDING_PANDORA_BOX_DROAUM_EMPTY`
- 建造物クラス: パンドラの箱（空っぽ）
- 必要な文明: ドロアウム
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Pandora's box (Low) - パンドラの箱（少量）

- 内部名: `BUILDING_PANDORA_BOX_DROAUM_LOW`
- 建造物クラス: パンドラの箱（少量）
- 必要な文明: ドロアウム
- [幸福]: 3
- [衛生]: 4
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Pandora's box (Middle) - パンドラの箱（ほどほど）

- 内部名: `BUILDING_PANDORA_BOX_DROAUM_MIDDLE`
- 建造物クラス: パンドラの箱（ほどほど）
- 必要な文明: ドロアウム
- [幸福]: 6
- [衛生]: 8
- その他の設定:
  - `bNeverCapture`: 1
  - `iCitiesPrereq`: 100
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Pandora's box - パンドラの箱

- 内部名: `BUILDING_PANDORA_BOX_DROAUM`
- 建造物クラス: パンドラの箱
- 必要な文明: ドロアウム
- [幸福]: 9
- [衛生]: 12
- 説明（ゲーム内ヘルプ）: ドロアウムの都市に自動で置かれて、アルマゲドンカウンタに応じた恩恵を授かる
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Pandora's box (Stocked) - パンドラの箱（備蓄あり）

- 内部名: `BUILDING_PANDORA_BOX_DROAUM_STOCKED`
- 建造物クラス: パンドラの箱（備蓄あり）
- 必要な文明: ドロアウム
- [幸福]: 12
- [衛生]: 16
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Pandora's box (Abundant) - パンドラの箱（豊富）

- 内部名: `BUILDING_PANDORA_BOX_DROAUM_ABUNDANT`
- 建造物クラス: パンドラの箱（豊富）
- 必要な文明: ドロアウム
- [幸福]: 15
- [衛生]: 20
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Pandora's box (Full) - パンドラの箱（満杯）

- 内部名: `BUILDING_PANDORA_BOX_DROAUM_FULL`
- 建造物クラス: パンドラの箱（満杯）
- 必要な文明: ドロアウム
- [幸福]: 18
- [衛生]: 24
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Pandora's box (Overflowing) - パンドラの箱（溢れんばかり）

- 内部名: `BUILDING_PANDORA_BOX_DROAUM_OVERFLOWING`
- 建造物クラス: パンドラの箱（溢れんばかり）
- 必要な文明: ドロアウム
- [幸福]: 21
- [衛生]: 28
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iGreatPeopleRateModifier`: 25
  - `fVisibilityPriority`: 1

### Ys Palace - イースの宮殿

- 内部名: `BUILDING_PALACE_YS`
- 固有: イース（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 魂のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 自然のマナ iBonusCount=1 / 精神のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGreatPeopleRateModifier`: 20
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Arc of Napishtim - ナピシュテムの匣

- 内部名: `BUILDING_ARK_OF_NAPISHTIM`
- 固有: イース（記念碑 の代替）
- 建造物クラス: 記念碑
- コスト[ハンマー]: 60
- 必要テクノロジー: 原初の祈り
- 倍速の志向: 創造志向 iProductionTrait=100
- 説明（ゲーム内ヘルプ）: 新規の精神集中を持つユニットに、対応するランクの呪文昇進をランダムで与える
- その他の設定:
  - `FreeStartEra`: 古典期
  - `HappinessTraits`: カリスマ志向 iHappinessTrait=1
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 2
  - `ObsoleteSafeCommerceChanges`: 3[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Gods of Roadside - 道祖神

- 内部名: `BUILDING_GODS_OF_ROADSIDE`
- 固有: イース（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系): 2[ゴールド]
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Niraikanai Palace - ニライカナイの宮殿

- 内部名: `BUILDING_PALACE_NIRAIKANAI`
- 固有: ニライカナイ（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 生命のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 太陽のマナ iBonusCount=1 / 自然のマナ iBonusCount=1
  - `GreatPeopleUnitClass`: 庭師
  - `iGreatPeopleRateChange`: 2
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `BonusHealthChanges`: 世界樹の果実 iHealthChange=1 / 死のマナ / 不可逆のマナ / 影石 / ナイトメア / 剃刀草 / 蛙 / グラガルム
  - `BonusHappinessChanges`: 世界樹の果実 iHappinessChange=1 / 死のマナ / 不可逆のマナ / 影石 / ナイトメア / 剃刀草 / 蛙 / グラガルム
  - `iCrime`: -10

### Sinmei Shrine - 神明神社

- 内部名: `BUILDING_NIRAIKANAI_TEMPLE`
- 固有: ニライカナイ（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `GreatPeopleUnitClass`: 庭師
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Circus of the sun - 太陽の曲芸団

- 内部名: `BUILDING_CIRCUS_OF_THE_SUN`
- 固有: ニライカナイ（巡業サーカス の代替）
- 建造物クラス: 巡業サーカス
- コスト[ハンマー]: 100
- 必要テクノロジー: 祝祭
- 陳腐化: 蒸気機関
- [幸福]: 1
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 吟遊詩人 iSpecialistCount=1
- 倍速の志向: 創造志向 iProductionTrait=100
- その他の設定:
  - `MaxStartEra`: 未来
  - `GreatPeopleUnitClass`: 庭師
  - `iGreatPeopleRateChange`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `BonusHealthChanges`: 米 iHealthChange=2
  - `BonusHappinessChanges`: 米 iHappinessChange=2
  - `UnitCombatFreeExperiences`: 動物ユニット iExperience=2
  - `BonusYieldModifiers`: エール酒

### Optistery - 目の院

- 内部名: `BUILDING_NIRAIKANAI_LIBRARY`
- 固有: ニライカナイ（図書館 の代替）
- 建造物クラス: 図書館
- コスト[ハンマー]: 100
- 必要テクノロジー: 筆記
- 産出(商業系)[%]: 20[研究]
- 専門家枠: 賢者 iSpecialistCount=1
- 倍速の志向: 哲学志向 iProductionTrait=100 / 賢人志向 iProductionTrait=50
- その他の設定:
  - `FreeStartEra`: 未来
  - `GreatPeopleUnitClass`: 庭師
  - `iGreatPeopleRateChange`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Rhinostery - 鼻の院

- 内部名: `BUILDING_NIRAIKANAI_ALCHEMY_LAB`
- 固有: ニライカナイ（錬金術ラボ の代替）
- 建造物クラス: 錬金術ラボ
- コスト[ハンマー]: 300
- 必要テクノロジー: 魔術
- 産出(商業系): 4[研究]
- 産出(商業系)[%]: 25[研究], 10[文化]
- 専門家枠: 賢者 iSpecialistCount=1
- 倍速の志向: 探求志向 iProductionTrait=100 / 秘術志向 iProductionTrait=100 / 賢人志向 iProductionTrait=50
- その他の設定:
  - `GreatPeopleUnitClass`: 庭師
  - `iGreatPeopleRateChange`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusYieldModifiers`: 秘薬 / 火薬 / 銅

### Manustery - 手の院

- 内部名: `BUILDING_NIRAIKANAI_FORGE`
- 固有: ニライカナイ（鍛冶屋 の代替）
- 建造物クラス: 鍛冶屋
- コスト[ハンマー]: 150
- 必要テクノロジー: 製錬
- 産出[%]: +15[ハンマー]
- 専門家枠: 技師 iSpecialistCount=1
- 倍速の志向: 勤労志向 iProductionTrait=100 / 軍事志向 iProductionTrait=100
- その他の設定:
  - `GreatPeopleUnitClass`: 庭師
  - `iGreatPeopleRateChange`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `BonusHappinessChanges`: 金 iHappinessChange=1 / 世界樹の果実 iHappinessChange=1
  - `SupplyPromotionProbabilities`: 武器の腐食 iProbability=-50

### Aurastery - 耳の院

- 内部名: `BUILDING_NIRAIKANAI_NATIONAL_EPIC`
- 固有: ニライカナイ（民族叙事詩 の代替）
- 建造物クラス: 民族叙事詩
- コスト[ハンマー]: 250
- 必要テクノロジー: 軍事行動
- 必要な建造物: 図書館
- 倍速の資源: 薄闇樹 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 庭師
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iGreatPeopleRateModifier`: 100
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Orastery - 口の院

- 内部名: `BUILDING_NIRAIKANAI_HEROIC_EPIC`
- 固有: ニライカナイ（英雄叙事詩 の代替）
- 建造物クラス: 英雄叙事詩
- コスト[ハンマー]: 200
- 必要テクノロジー: 軍事戦略
- 倍速の資源: 薄闇樹 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 庭師
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iCombatLevelPrereq`: 1
  - `iMaxLatitude`: 90
  - `iMilitaryProductionModifier`: 100
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Gosinboku - 御神木

- 内部名: `BUILDING_GOSINBOKU`
- 建造物クラス: BUILDINGCLASS_GOSINBOKU
- コスト[ハンマー]: 160
- 必要テクノロジー: 動物の馴致
- 必要な文明: ニライカナイ
- [幸福]: 1
- [衛生]: 1
- 産出: +2[食料]
- その他の設定:
  - `GreatPeopleUnitClass`: 庭師
  - `iGreatPeopleRateChange`: 4
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iGreatPeopleRateModifier`: 25
  - `fVisibilityPriority`: 100
  - `BonusHealthChanges`: 世界樹の果実 iHealthChange=1 / 死のマナ / 不可逆のマナ / 影石 / ナイトメア / 剃刀草 / 蛙 / グラガルム
  - `BonusHappinessChanges`: 世界樹の果実 iHappinessChange=1 / 死のマナ / 不可逆のマナ / 影石 / ナイトメア / 剃刀草 / 蛙 / グラガルム
  - `BonusYieldModifiers`: 世界樹の果実
  - `ImprovementFreeSpecialists`: ユグドラシルの樹 iFreeSpecialistCount=1 / 巨大樹 iFreeSpecialistCount=1

### Dark Palace - 常闇の宮殿

- 内部名: `BUILDING_PALACE_DARK`
- 固有: 常闇ノ国（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- [都市防御]: 25
- 供給する資源: 古書物
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 死のマナ iBonusCount=1 / 不可逆のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iWarWearinessModifier`: -30
  - `iGlobalWarWearinessModifier`: -30
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Altar of the Burning Hell - 炎獄の祭壇

- 内部名: `BUILDING_DARK_TEMPLE`
- 固有: 常闇ノ国（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 10[文化]
- 専門家枠: 賢者 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- 説明（ゲーム内ヘルプ）: 都市の周囲2タイル以内に地獄の浸食を発生させる
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHealthChanges`: 不可逆のマナ iHealthChange=1 / 蛙 iHealthChange=1 / 剃刀草 iHealthChange=1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1 / 死のマナ iHappinessChange=1 / グラガルム iHappinessChange=1
  - `iModifyGlobalCounter`: 3

### Stable of Nightmares - 夢魔の厩舎

- 内部名: `BUILDING_STABLE_OF_NIGHTMARES`
- 固有: シェアイム・ドロアウム・地獄の軍勢・常闇ノ国（厩舎 の代替）
- 建造物クラス: 厩舎
- コスト[ハンマー]: 50
- 必要テクノロジー: 騎乗
- 倍速の志向: 突撃志向 iProductionTrait=100 / TXT_KEY_TRAIT_IMPERIALIST iProductionTrait=50
- 説明（ゲーム内ヘルプ）: 新規のナイトメアを持つユニットに20%の確率で暗黒魔法Ⅰを与える
- その他の設定:
  - `HappinessTraits`: 迅速志向 iHappinessTrait=1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10

### SheutStone Processing Plant - 影石加工場

- 内部名: `BUILDING_DARK_FORGE`
- 固有: シェアイム・ドロアウム・常闇ノ国（鍛冶屋 の代替）
- 建造物クラス: 鍛冶屋
- コスト[ハンマー]: 150
- 必要テクノロジー: 製錬
- 産出[%]: +15[ハンマー]
- 専門家枠: 技師 iSpecialistCount=1
- 倍速の志向: 勤労志向 iProductionTrait=100 / 軍事志向 iProductionTrait=100
- 説明（ゲーム内ヘルプ）: 新規の影石を持つユニットに20%の確率で暗黒魔法Ⅰを与える
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `BonusHappinessChanges`: 金 iHappinessChange=1
  - `SupplyPromotionProbabilities`: 武器の腐食 iProbability=-50
  - `BonusYieldModifiers`: 影石

### Necromancy Lab - 屍霊術研究所

- 内部名: `BUILDING_DARK_ALCHEMY_LAB`
- 固有: シェアイム・ドロアウム・地獄の軍勢・常闇ノ国（錬金術ラボ の代替）
- 建造物クラス: 錬金術ラボ
- コスト[ハンマー]: 300
- 必要テクノロジー: 魔術
- 産出(商業系): 4[研究]
- 産出(商業系)[%]: 10[ゴールド], 10[研究]
- 専門家枠: 賢者 iSpecialistCount=2
- 倍速の志向: 探求志向 iProductionTrait=100 / 秘術志向 iProductionTrait=100 / 賢人志向 iProductionTrait=50
- 説明（ゲーム内ヘルプ）: 新規の屍人ユニットに±0～+8: 経験ポイント
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusYieldModifiers`: 秘薬 / 火薬 / 銅

### Dark Orb - 空亡の宝珠

- 内部名: `BUILDING_DARK_ORB`
- 建造物クラス: 空亡の宝珠
- 必要な文明: 常闇ノ国
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHealthChanges`: 不可逆のマナ iHealthChange=2
  - `BonusHappinessChanges`: 死のマナ iHappinessChange=2
  - `BonusYieldModifiers`: 蛙 / 影石 / 剃刀草
  - `BonusCommerceModifiers`: グラガルム / ナイトメア
  - `ImprovementFreeSpecialists`: 蛇の柱 iFreeSpecialistCount=1

### Despiel Palace - デスピエルの宮殿

- 内部名: `BUILDING_PALACE_DESPIEL`
- 固有: デスピエル（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 不可逆のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 死のマナ iBonusCount=1 / 生命のマナ iBonusCount=1 / 次元のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `BonusHealthChanges`: 超魔術のマナ iHealthChange=1 / 精神のマナ iHealthChange=1 / 魂のマナ iHealthChange=1
  - `BonusHappinessChanges`: 自然のマナ iHappinessChange=1 / 太陽のマナ iHappinessChange=1 / 水のマナ iHappinessChange=1
  - `iCrime`: 30

### Despiel citizens - デスピエルの市民

- 内部名: `BUILDING_DESPIEL_CITIZENS`
- 建造物クラス: デスピエルの市民
- 必要な文明: デスピエル
- 説明（ゲーム内ヘルプ）: 10%の確率で白兵以外の新規の生物ユニットに変異体の昇進を与える
- その他の設定:
  - `bNoUnhealthyPopulation`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iWarWearinessModifier`: -20
  - `fVisibilityPriority`: 1

### Strange butcher - 奇妙な肉屋

- 内部名: `BUILDING_STRANGE_BUTCHER`
- 固有: デスピエル（市場 の代替）
- 建造物クラス: 市場
- コスト[ハンマー]: 100
- 必要テクノロジー: 祝祭
- 陳腐化: 蒸気機関
- [衛生]: -2
- 産出(商業系): 2[ゴールド]
- 専門家枠: 商人 iSpecialistCount=1
- 倍速の志向: 金融志向 iProductionTrait=100 / 交易志向 iProductionTrait=100 / 強欲志向 iProductionTrait=100
- 説明（ゲーム内ヘルプ）: 自領内で死亡した生命体、あるいは領外で殺害した生命体の死体を利用して人口が増加する / (とに余裕が必要)
- その他の設定:
  - `MaxStartEra`: 未来
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `BonusHealthChanges`: バナナ iHealthChange=1
  - `BonusHappinessChanges`: 象牙 iHappinessChange=1
  - `FreePromotionProbabilities`: 人食い iProbability=10
  - `iCrime`: 5

### Soul culture facilities - 霊魂培養所

- 内部名: `BUILDING_SOUL_CULTURE_FACILITIES`
- 固有: デスピエル（錬金術ラボ の代替）
- 建造物クラス: 錬金術ラボ
- コスト[ハンマー]: 380
- 必要テクノロジー: 魔術
- 産出(商業系): 4[研究]
- 産出(商業系)[%]: 25[研究], 10[文化]
- 専門家枠: 賢者 iSpecialistCount=2
- 倍速の志向: 探求志向 iProductionTrait=100 / 秘術志向 iProductionTrait=100 / 賢人志向 iProductionTrait=50
- 説明（ゲーム内ヘルプ）: 都市の建造物は死亡した生命体の魂を何度でも利用できる
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHealthChanges`: 死のマナ / 混沌のマナ / 不可逆のマナ / 影のマナ
  - `UnitCombatFreeExperiences`: 信奉ユニット iExperience=2 / 秘術ユニット iExperience=2
  - `BonusYieldModifiers`: 秘薬 / 火薬 / 銅
  - `BonusCommerceModifiers`: 混沌のマナ / 死のマナ / 不可逆のマナ / 影のマナ
  - `iModifyGlobalCounter`: 1

### Pollution Law Library - 汚染法書院

- 内部名: `BUILDING_POLLUTION_LAW_LIBRARY`
- 固有: デスピエル（図書館 の代替）
- 建造物クラス: 図書館
- コスト[ハンマー]: 100
- 必要テクノロジー: 筆記
- [衛生]: -3
- 産出(商業系)[%]: 25[研究]
- 専門家枠: 賢者 iSpecialistCount=1
- 倍速の志向: 哲学志向 iProductionTrait=100 / 賢人志向 iProductionTrait=50
- 説明（ゲーム内ヘルプ）: ターンの開始時に、周囲2タイル以内の敵ユニットに毒ダメージを与える
- その他の設定:
  - `FreeStartEra`: 未来
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `BonusHealthChanges`: 大気のマナ / 大地のマナ / 炎のマナ / 水のマナ
  - `BonusYieldModifiers`: 大気のマナ / 大地のマナ / 炎のマナ / 水のマナ
  - `BonusCommerceModifiers`: 大気のマナ / 大地のマナ / 炎のマナ / 水のマナ

### Altar of Evil Faith - 奉魔の祭壇

- 内部名: `BUILDING_ALTAR_OF_EVIL_FAITH`
- 固有: デスピエル（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 賢者 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- 説明（ゲーム内ヘルプ）: 自領内で死亡した生命体、あるいは領外で殺害した死体からを得る。
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1
  - `DomainProductionModifiers`: DOMAIN_LAND iProductionModifier=10

### Experimental facility - 実験場

- 内部名: `BUILDING_EXPERIMENTAL_FACILITY`
- 固有: デスピエル（地下牢 の代替）
- 建造物クラス: 地下牢
- コスト[ハンマー]: 120
- 必要テクノロジー: 石工
- 産出(商業系)[%]: 10[研究]
- 専門家枠: 賢者 iSpecialistCount=1
- 倍速の志向: 組織志向 iProductionTrait=100 / カリスマ志向 iProductionTrait=100
- 倍速の資源: 石材 iProductonModifier=100
- 説明（ゲーム内ヘルプ）: 自領内で死亡した生命体、あるいは領外で殺害した生命体は10%～50%の確率で転生し配下のユニットに加わる
- その他の設定:
  - `FreeStartEra`: 中世
  - `iConscriptAngerModifier`: -50
  - `iCivicAngerModifier`: -50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `DomainProductionModifiers`: DOMAIN_LAND iProductionModifier=10
  - `iCrime`: 10

### House of Truth - 真理の館

- 内部名: `BUILDING_HOUSE_OF_TRUTH`
- 固有: デスピエル（裁判所 の代替）
- 建造物クラス: 裁判所
- コスト[ハンマー]: 100
- 必要テクノロジー: 法律
- 専門家枠: 賢者 iSpecialistCount=1
- 倍速の志向: 組織志向 iProductionTrait=100
- 説明（ゲーム内ヘルプ）: 25%の確率で新規ユニットの壊人に高速詠唱の昇進
- その他の設定:
  - `FreeStartEra`: 未来
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -40
  - `fVisibilityPriority`: 10
  - `BonusHappinessChanges`: 肉体のマナ / 呪付のマナ / 自然のマナ / 太陽のマナ
  - `BonusCommerceModifiers`: 肉体のマナ / 呪付のマナ / 自然のマナ / 太陽のマナ
  - `iCrime`: -10

### Soul exchange - 換魂所

- 内部名: `BUILDING_SOUL_EXCHANGE`
- 固有: デスピエル（鍛冶屋 の代替）
- 建造物クラス: 鍛冶屋
- コスト[ハンマー]: 150
- 必要テクノロジー: 製錬
- [衛生]: -2
- 産出[%]: +25[ハンマー]
- 専門家枠: 技師 iSpecialistCount=1 / 賢者 iSpecialistCount=1
- 倍速の志向: 勤労志向 iProductionTrait=100 / 軍事志向 iProductionTrait=100
- 説明（ゲーム内ヘルプ）: 自領内で死亡した生命体、あるいは領外で殺害した生命体の魂を利用してを得る
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `BonusHappinessChanges`: 金 iHappinessChange=1
  - `SupplyPromotionProbabilities`: 武器の腐食 iProbability=-50
  - `BonusYieldModifiers`: 生命のマナ / 精神のマナ / 魂のマナ / 法のマナ
  - `BonusCommerceModifiers`: 生命のマナ / 精神のマナ / 魂のマナ / 法のマナ

### Lineage Palace - リネージの宮殿

- 内部名: `BUILDING_PALACE_LINEAGE`
- 固有: リネージ（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 古書物
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 石材 iBonusCount=1 / 大理石 iBonusCount=1
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -10
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Imperial Stable - 帝国厩舎

- 内部名: `BUILDING_STABLE_OF_LINEAGE`
- 固有: リネージ（厩舎 の代替）
- 建造物クラス: 厩舎
- コスト[ハンマー]: 75
- 必要テクノロジー: 騎乗
- 新規ユニットに昇進: 馬持ち
- 倍速の志向: 突撃志向 iProductionTrait=100 / TXT_KEY_TRAIT_IMPERIALIST iProductionTrait=50
- その他の設定:
  - `HappinessTraits`: 迅速志向 iHappinessTrait=1
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 1
  - `iMaxLatitude`: 90
  - `iTradeRouteModifier`: 50
  - `fVisibilityPriority`: 10
  - `SupplyPromotionProbabilities`: 馬持ち iProbability=100

### Governors Office - 総督府

- 内部名: `BUILDING_GOVERNORS_OFFICE`
- 固有: リネージ（裁判所 の代替）
- 建造物クラス: 裁判所
- コスト[ハンマー]: 100
- 必要テクノロジー: 法律
- 倍速の志向: 組織志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 未来
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 1
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -40
  - `fVisibilityPriority`: 10
  - `iCrime`: -10

### Citadel Walls - 城塞防壁

- 内部名: `BUILDING_CITADEL_WALLS`
- 固有: リネージ（防壁 の代替）
- 建造物クラス: 防壁
- コスト[ハンマー]: 120
- 必要テクノロジー: 数学
- 追加で必要なテクノロジー: 石工
- 産出(商業系)[%]: 10[研究]
- [都市防御]: 40
- 倍速の志向: 防御志向 iProductionTrait=100
- 倍速の資源: 石材 iProductonModifier=100
- その他の設定:
  - `FreeStartEra`: 中世
  - `HappinessTraits`: 防御志向 iHappinessTrait=1
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 1
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `iAirModifier`: -50
  - `iBombardDefense`: 50
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `bExtraSeeFrom`: 1

### Ballista Workshop - バリスタ工房

- 内部名: `BUILDING_BALLISTA_WORKSHOP`
- 固有: リネージ（攻城兵器工廠 の代替）
- 建造物クラス: 攻城兵器工廠
- コスト[ハンマー]: 90
- 必要テクノロジー: 建設
- 倍速の志向: 攻撃志向 iProductionTrait=100 / TXT_KEY_TRAIT_IMPERIALIST iProductionTrait=50
- 倍速の資源: 鉄 iProductonModifier=25 / 薄闇樹 iProductonModifier=25
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `UnitCombatFreeExperiences`: 攻城兵器 iExperience=4

### Temple of Gods - 神々の神殿

- 内部名: `BUILDING_TEMPLE_LINEAGE`
- 固有: リネージ（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系): 1[研究]
- 産出(商業系)[%]: 25[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Imperial Aqueduct - 帝国水道橋

- 内部名: `BUILDING_AQUEDUCT_OF_LINEAGE`
- 固有: リネージ（水道橋 の代替）
- 建造物クラス: 水道橋
- コスト[ハンマー]: 200
- 必要テクノロジー: 衛生設備
- [幸福]: 1
- [衛生]: 4
- 産出: +2[商業]
- 産出[%]: +5[食料], +5[ハンマー]
- 産出(商業系)[%]: 10[文化]
- 倍速の志向: 拡張志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 未来
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 1
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10240000
  - `BonusHealthChanges`: レモン iHealthChange=1 / オレンジ iHealthChange=1

### Temple of Holynorth - 聖北の大神殿

- 内部名: `BUILDING_TEMPLE_OF_HOLY_NORTH`
- 建造物クラス: 聖北の大神殿
- コスト[ハンマー]: 180
- 必要テクノロジー: 聖職
- 必要な文明: リネージ
- 必要な志向: 無神論志向
- 産出[%]: +20[商業]
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=2
- 倍速の志向: 伝道志向 iProductionTrait=100
- その他の設定:
  - `HappinessTraits`: 宗教志向 iHappinessTrait=1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMilitaryProductionModifier`: 10
  - `fVisibilityPriority`: 10
  - `BonusHappinessChanges`: 香木 iHappinessChange=1
  - `DomainFreeExperiences`: DOMAIN_LAND iExperience=2
  - `iCrime`: -5

### Militaly Academy - 士官学校

- 内部名: `BUILDING_MILITALY_ACADEMY`
- 建造物クラス: 士官学校
- コスト[ハンマー]: 300
- 必要テクノロジー: 軍事戦略
- 必要な文明: リネージ
- [都市防御]: 25
- 説明（ゲーム内ヘルプ）: 生産される全ユニットに+1: 任意の無償の昇進
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 4
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: 10
  - `iBombardDefense`: 25
  - `fVisibilityPriority`: 1

### Craftman Studio - 職人工房

- 内部名: `BUILDING_CRAFTMAN_STUDIO`
- 建造物クラス: 職人工房
- コスト[ハンマー]: 220
- 必要テクノロジー: 工学
- 必要な文明: リネージ
- 説明（ゲーム内ヘルプ）: 生産される全ユニットに所有する職人工房の数に応じた強化Ⅰ～Ⅴを初期昇進として与える
- その他の設定:
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `BonusYieldModifiers`: 銅 / 鉄 / ミスリル / 金

### Great Dining - 大衆食堂

- 内部名: `BUILDING_GREAT_DINING`
- 建造物クラス: 大衆食堂
- コスト[ハンマー]: 200
- 必要テクノロジー: 交易
- 必要な文明: リネージ
- その他の設定:
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: 10
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `BonusHealthChanges`: トウモロコシ iHealthChange=1 / 米 iHealthChange=1 / 小麦 iHealthChange=1 / 亜麻 iHealthChange=1 / ジャガイモ iHealthChange=1 / 貝 iHealthChange=1 / 蟹 iHealthChange=1 / 魚 iHealthChange=1 / 海老 iHealthChange=1 / 塩 iHealthChange=1 / キノコ iHealthChange=1 / 馬 iHealthChange=1 / 牛 iHealthChange=1 / 豚 iHealthChange=1 / 羊 iHealthChange=1 / 蛙 iHealthChange=1 / 砂糖 iHealthChange=1 / バナナ iHealthChange=1 / オレンジ iHealthChange=1 / レモン iHealthChange=1

### Mazatl Palace - マサトルの宮殿

- 内部名: `BUILDING_PALACE_MAZATL`
- 固有: マサトル（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 自然のマナ
- 供給数: 1
- その他の設定:
  - `GlobalReligionCommerce`: ドラゴン崇拝
  - `ObsoleteSafeFreeBonuses`: 大地のマナ iBonusCount=1 / 肉体のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -10
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Sacellum of Kalshekk - カルシェックの礼拝所

- 内部名: `BUILDING_SACELLUM_OF_KALSHEKK`
- 固有: マサトル（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 商人 iSpecialistCount=1 / 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iTradeRouteModifier`: 10
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Sacellum of Omorr - オモールの礼拝所

- 内部名: `BUILDING_MONASTERY_OF_OMORR`
- 建造物クラス: オモールの礼拝所
- コスト[ハンマー]: 140
- 必要テクノロジー: 聖職
- 必要な文明: マサトル
- [衛生]: 1
- 産出(商業系)[%]: 5[研究]
- 専門家枠: 神官 iSpecialistCount=1
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iGoldenAgeModifier`: 5
  - `iHealRateChange`: 10
  - `iTradeRoutes`: 1
  - `iTradeRouteModifier`: 15
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Cualli Palace - クアリの宮殿

- 内部名: `BUILDING_PALACE_CUALLI`
- 固有: クアリ（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 自然のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 死のマナ iBonusCount=1 / 肉体のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -10
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Sacrificial Altar - アグルオンの祭壇

- 内部名: `BUILDING_SACRIFICAL_ALTAR`
- 固有: クアリ（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 供給数: 1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `iHurryAngerModifier`: -50
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `DomainFreeExperiences`: DOMAIN_LAND iExperience=1

### Slave Pits - 奴隷の穴居

- 内部名: `BUILDING_SLAVE_PIT`
- 建造物クラス: 奴隷の穴居
- 必要な文明: クアリ
- 無償の専門家: 特別市民 iFreeSpecialistCount=4
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Altair Palace - アルタイルの宮殿

- 内部名: `BUILDING_PALACE_ALTAIR`
- 固有: アルタイル（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 産出[%]: +10[ハンマー]
- 供給する資源: 大地のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 炎のマナ iBonusCount=1 / 太陽のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -40
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `BonusHappinessChanges`: 竜玉石 iHappinessChange=3 / 翡翠 iHappinessChange=1 / 宝石 iHappinessChange=1 / 琥珀 iHappinessChange=1 / 金 iHappinessChange=1 / 真珠 iHappinessChange=1
  - `SupplyPromotionProbabilities`: 病気 iProbability=-50
  - `iCrime`: -10

### Dragon's Nest - 竜の巣

- 内部名: `BUILDING_DRAGONS_NEST`
- 建造物クラス: 竜の巣
- コスト[ハンマー]: 120
- 必要テクノロジー: 教育
- 必要な文明: アルタイル
- その他の設定:
  - `bNeverCapture`: 1
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `iMilitaryProductionModifier`: 20
  - `fVisibilityPriority`: 10

### Energy Stone - 要石

- 内部名: `BUILDING_ENERGY_STONE`
- 固有: アルタイル（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系): 2[研究]
- 産出(商業系)[%]: 20[文化]
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1
  - `RemovePromotion`: 病気

### Line Stone - 列石

- 内部名: `BUILDING_LINE_STONE`
- 固有: アルタイル（診療所 の代替）
- 建造物クラス: 診療所
- コスト[ハンマー]: 250
- 必要テクノロジー: 医薬
- 必要な建造物: 薬草師
- [幸福]: 1
- [衛生]: 1
- 産出(商業系)[%]: 30[研究], 40[文化]
- 倍速の志向: 野戦志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `iHealRateChange`: 25
  - `fVisibilityPriority`: 1
  - `BonusHealthChanges`: 剃刀草 iHealthChange=1
  - `SupplyPromotionProbabilities`: 病気 iProbability=-100 / 疫病 iProbability=-50 / 衰弱 iProbability=-50 / 黒死病 iProbability=-50

### Mechanos Palace - メカノスの宮殿

- 内部名: `BUILDING_PALACE_MECHANOS`
- 固有: メカノス（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 銅
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 呪付のマナ iBonusCount=1 / 火薬 iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: 10
  - `fVisibilityPriority`: 10000
  - `PowerYieldModifiers`: +10[ハンマー]
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Steamworks - 蒸気駆動装置

- 内部名: `BUILDING_STEAMWORKS`
- 建造物クラス: 蒸気駆動装置
- 必要な文明: メカノス
- 産出[%]: +30[ハンマー]
- 産出(商業系)[%]: 30[研究]
- 専門家枠: 技師 iSpecialistCount=3
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な技師
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100

### Power Plant - 発電所

- 内部名: `BUILDING_POWER_PLANT`
- 固有: ノービアイ・メカノス（プラント の代替）
- 建造物クラス: プラント
- コスト[ハンマー]: 180
- 必要テクノロジー: 蒸気機関
- 専門家枠: 技師 iSpecialistCount=1
- 無償の専門家: 技師 iFreeSpecialistCount=1
- その他の設定:
  - `PowerBonus`: 精製されたマナ
  - `bDirtyPower`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Clock Tower - 時計塔

- 内部名: `BUILDING_TEMPLE_MECHANOS`
- 固有: メカノス（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 140
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 10[研究], 20[文化]
- 専門家枠: 賢者 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `PowerYieldModifiers`: +10[ハンマー]
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Smelter - 製錬所

- 内部名: `BUILDING_SMELTER`
- 固有: ノービアイ・メカノス（鍛冶屋 の代替）
- 建造物クラス: 鍛冶屋
- コスト[ハンマー]: 225
- 必要テクノロジー: 製錬
- 産出[%]: +20[ハンマー]
- 専門家枠: 技師 iSpecialistCount=1
- 倍速の志向: 勤労志向 iProductionTrait=100 / 軍事志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `PowerYieldModifiers`: +20[ハンマー]
  - `BonusHappinessChanges`: 金 iHappinessChange=1
  - `SupplyPromotionProbabilities`: 武器の腐食 iProbability=-50
  - `BonusYieldModifiers`: 精製されたマナ / 鉄 / ミスリル

### Dike - ダイク

- 内部名: `BUILDING_DIKE_MECHANOS`
- 建造物クラス: ダイク
- コスト[ハンマー]: 250
- 必要テクノロジー: 蒸気機関
- 追加で必要なテクノロジー: 工学
- 必要な文明: メカノス
- 説明（ゲーム内ヘルプ）: 水域あるいは川に接した都市にのみ建設可能
- その他の設定:
  - `bWater`: 1
  - `bRiver`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `SeaPlotYieldChanges`: +1[ハンマー]
  - `PowerYieldModifiers`: +10[ハンマー]

### Palace of the Scions - 後継者の神殿

- 内部名: `BUILDING_PALACE_SCIONS`
- 固有: パトリアの後継者（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 死のマナ
- 供給数: 1
- その他の設定:
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: 25
  - `iGlobalHealth`: 6
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Flesh Studio - 屍肉工房

- 内部名: `BUILDING_FLESH_STUDIO`
- 固有: パトリアの後継者（診療所 の代替）
- 建造物クラス: 診療所
- コスト[ハンマー]: 250
- 必要テクノロジー: 変成術
- 必要な資源（いずれか）: 肉体のマナ
- 必要な建造物: 薬草師
- [幸福]: 1
- [衛生]: 3
- 産出(商業系)[%]: 20[研究]
- 倍速の志向: 野戦志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `iHealRateChange`: 50
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `BonusHealthChanges`: 剃刀草 iHealthChange=1

### Hall of the Covenant - 契約の大広間

- 内部名: `BUILDING_HALL_OF_THE_COVENANT`
- 固有: パトリアの後継者（劇場 の代替）
- 建造物クラス: 劇場
- コスト[ハンマー]: 200
- 必要テクノロジー: 演劇
- 産出(商業系)[%]: 30[文化]
- 専門家枠: 吟遊詩人 iSpecialistCount=2
- 倍速の志向: 創造志向 iProductionTrait=100 / 伝道志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceHappinesses`: 10[文化]
  - `BonusHappinessChanges`: 染料 iHappinessChange=1 / 絹 iHappinessChange=1

### Imperial Cenotaph - 荘厳なる鎮魂碑

- 内部名: `BUILDING_IMPERIAL_CENOTAPH`
- 固有: パトリアの後継者（裁判所 の代替）
- 建造物クラス: 裁判所
- コスト[ハンマー]: 120
- 必要テクノロジー: 法律
- 産出(商業系)[%]: 10[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 組織志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 未来
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -20
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `iCrime`: -25

### Spirit Mill - 精魂所

- 内部名: `BUILDING_SPIRIT_MILL`
- 固有: パトリアの後継者（ビール醸造所 の代替）
- 建造物クラス: ビール醸造所
- コスト[ハンマー]: 90
- 必要テクノロジー: 道具の作成
- 必要な資源（いずれか）: 牛 / 豚 / 羊
- 倍速の志向: カリスマ志向 iProductionTrait=100
- 説明（ゲーム内ヘルプ）: 川沿い都市にのみ建設可能
- その他の設定:
  - `bRiver`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 牛 iHappinessChange=1 / 豚 iHappinessChange=1 / 羊 iHappinessChange=1

### Shrine to Kylorin - カイロリンの聖廟

- 内部名: `BUILDING_SHRINE_TO_KYLORIN`
- 固有: パトリアの後継者（図書館 の代替）
- 建造物クラス: 図書館
- コスト[ハンマー]: 100
- 必要テクノロジー: 筆記
- 産出(商業系)[%]: 25[研究]
- 専門家枠: 神官 iSpecialistCount=1 / 賢者 iSpecialistCount=1
- 倍速の志向: 哲学志向 iProductionTrait=100 / 賢人志向 iProductionTrait=50
- その他の設定:
  - `FreeStartEra`: 未来
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Temple of the Gift - ギフトの寺院

- 内部名: `BUILDING_TEMPLE_OF_THE_GIFT`
- 固有: パトリアの後継者（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 専門家枠: 神官 iSpecialistCount=1 / 賢者 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- 説明（ゲーム内ヘルプ）: 都市に隣接する陸上タイルに悪霊の地を生成
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 1[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `BonusHappinessChanges`: 香木 iHappinessChange=1 / 絹 iHappinessChange=1

### Patrian Bazaar - パトリアのバザール

- 内部名: `BUILDING_PATRIAN_BAZAAR`
- 建造物クラス: パトリアのバザール
- コスト[ハンマー]: 180
- 必要テクノロジー: 通貨
- 必要な文明: パトリアの後継者
- 産出(商業系)[%]: 15[ゴールド]
- 専門家枠: 商人 iSpecialistCount=2
- その他の設定:
  - `bNoUnhealthyPopulation`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iTradeRoutes`: 1
  - `iForeignTradeRouteModifier`: 100
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 3[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `PrereqBuildingClasses`: 市場 iNumBuildingNeeded=3
  - `iCrime`: 5

### Cathedral of Rebirth - 再誕の大聖堂

- 内部名: `BUILDING_CATHEDRAL_OF_REBIRTH`
- 建造物クラス: 再誕の大聖堂
- コスト[ハンマー]: 280
- 必要テクノロジー: 宗教法
- 必要な文明: パトリアの後継者
- [幸福]: 3
- 産出(商業系)[%]: 25[文化]
- 専門家枠: 商人 iSpecialistCount=1
- [都市防御]: 10
- 倍速の志向: 伝道志向 iProductionTrait=100
- その他の設定:
  - `HappinessTraits`: 宗教志向 iHappinessTrait=1
  - `bNoUnhealthyPopulation`: 1
  - `bNeverCapture`: 1
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -20
  - `iTradeRouteModifier`: 25
  - `iAllCityDefense`: 25
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 3[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `UnitCombatFreeExperiences`: 信奉ユニット iExperience=2
  - `PrereqBuildingClasses`: 市場 iNumBuildingNeeded=3
  - `iCrime`: 5

### Beacon - 標のかがり火

- 内部名: `BUILDING_BEACON`
- 固有: パトリアの後継者（灯台 の代替）
- 建造物クラス: 灯台
- コスト[ハンマー]: 120
- 必要テクノロジー: 航海術
- 専門家枠: 商人 iSpecialistCount=1
- 倍速の志向: 組織志向 iProductionTrait=100 / 交易志向 iProductionTrait=100
- 倍速の資源: 石材 iProductonModifier=100
- その他の設定:
  - `FreeStartEra`: 中世
  - `bWater`: 1
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `iTradeRoutes`: 1
  - `fVisibilityPriority`: 10
  - `SeaPlotYieldChanges`: +1[ハンマー], +1[商業]

### Body Node - 肉体のノード

- 内部名: `BUILDING_KEEP_BODY`
- 建造物クラス: 肉体のノード
- 必要な文明: パトリアの後継者
- 供給する資源: 肉体のマナ
- 供給数: 1
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10

### Law Node - 法のノード

- 内部名: `BUILDING_KEEP_LAW`
- 建造物クラス: 法のノード
- 必要な文明: パトリアの後継者
- 供給する資源: 法のマナ
- 供給数: 1
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10

### Enchantment Node - 呪付のノード

- 内部名: `BUILDING_KEEP_ENCHANTMENT`
- 建造物クラス: 呪付のノード
- 必要な文明: パトリアの後継者
- 供給する資源: 呪付のマナ
- 供給数: 1
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10

### Earth Node - 大地のノード

- 内部名: `BUILDING_KEEP_EARTH`
- 建造物クラス: 大地のノード
- 必要な文明: パトリアの後継者
- 供給する資源: 大地のマナ
- 供給数: 1
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10

### Entropy Node - エントロピーのノード

- 内部名: `BUILDING_KEEP_ENTROPY`
- 建造物クラス: エントロピーのノード
- 必要な文明: パトリアの後継者
- 供給する資源: 不可逆のマナ
- 供給数: 1
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10

### Mind Node - 精神のノード

- 内部名: `BUILDING_KEEP_MIND`
- 建造物クラス: 精神のノード
- 必要な文明: パトリアの後継者
- 供給する資源: 精神のマナ
- 供給数: 1
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10

### Ice Node - 氷のノード

- 内部名: `BUILDING_KEEP_ICE`
- 建造物クラス: 氷のノード
- 必要な文明: パトリアの後継者
- 供給する資源: 氷のマナ
- 供給数: 1
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10

### Shadow Node - 影のノード

- 内部名: `BUILDING_KEEP_SHADOW`
- 建造物クラス: 影のノード
- 必要な文明: パトリアの後継者
- 供給する資源: 影のマナ
- 供給数: 1
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10

### Chaos Node - 混沌のノード

- 内部名: `BUILDING_KEEP_CHAOS`
- 建造物クラス: 混沌のノード
- 必要な文明: パトリアの後継者
- 供給する資源: 混沌のマナ
- 供給数: 1
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10

### Military Abattoir - 軍事畜殺場

- 内部名: `BUILDING_MILITARY_ABATTOIR`
- 建造物クラス: 軍事畜殺場
- 必要な文明: パトリアの後継者
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMilitaryProductionModifier`: 20
  - `fVisibilityPriority`: 10

### Alchemist's Tower - 錬金術師の塔

- 内部名: `BUILDING_KEEP_ALCHEMIST`
- 建造物クラス: 錬金術師の塔
- 必要な文明: パトリアの後継者
- 産出(商業系): 5[研究]
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10

### Schola Furo - 逸脱せし学び舎

- 内部名: `BUILDING_SCHOLA_FURIO`
- 建造物クラス: 逸脱せし学び舎
- 必要な文明: パトリアの後継者
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `UnitCombatFreeExperiences`: 秘術ユニット iExperience=4

### Alcinus' Trove - アルキヌスの発見

- 内部名: `BUILDING_ALCINUS_TROVE`
- 建造物クラス: TXT_KEY_BUILDING_ALCINUS_TROVE
- 必要な文明: パトリアの後継者
- 産出(商業系): 3[ゴールド]
- 供給する資源: 影石
- 供給数: 2
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `UnitCombatFreeExperiences`: 秘術ユニット iExperience=3

### Thaumaturge's Keep - 魔道士の砦

- 内部名: `BUILDING_THAUMATURGE_KEEP`
- 建造物クラス: 魔道士の砦
- 必要な文明: パトリアの後継者
- [幸福]: -2
- [衛生]: -3
- 産出: -2[ハンマー]
- 産出(商業系): 3[研究]
- 産出(商業系)[%]: 10[研究]
- [都市防御]: 20
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 100
  - `UnitCombatFreeExperiences`: 秘術ユニット iExperience=3

### Rousing Oration - 情熱溢るる演説

- 内部名: `BUILDING_ROUSING_ORATION`
- 建造物クラス: 情熱溢るる演説
- 産出[%]: +10[ハンマー]
- 産出(商業系): 6[ゴールド], 1[文化]
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iWarWearinessModifier`: -20
  - `iTradeRouteModifier`: 10
  - `fVisibilityPriority`: 100
  - `bRequiresCaster`: 1
  - `iCrime`: -5

### Dark Council - 闇の協議会

- 内部名: `BUILDING_DARK_COUNCIL`
- 建造物クラス: 闇の協議会
- 必要な文明: パトリアの後継者
- 産出(商業系)[%]: 10[ゴールド]
- 無償の専門家: 商人 iFreeSpecialistCount=1
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -10
  - `iGlobalWarWearinessModifier`: -10
  - `iEnemyWarWearinessModifier`: 15
  - `iGlobalTradeRoutes`: 1
  - `iTradeRouteModifier`: 25
  - `fVisibilityPriority`: 100
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `iCrime`: 5

### Melante's Residence - メランテの大邸宅

- 内部名: `BUILDING_MELANTE_RESIDENCE`
- 建造物クラス: メランテの大邸宅
- 産出(商業系): 1[文化]
- 産出(商業系)[%]: 10[ゴールド], 10[研究], 10[文化]
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -25
  - `iWarWearinessModifier`: -10
  - `iWorkerSpeedModifier`: 20
  - `iMilitaryProductionModifier`: -10
  - `fVisibilityPriority`: 100
  - `bRequiresCaster`: 1
  - `iCrime`: -5

### Nival Palace - ニバルの宮殿

- 内部名: `BUILDING_PALACE_NIVAL`
- 固有: ニバル（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 氷のマナ
- 供給数: 1
- 説明（ゲーム内ヘルプ）: 都市周辺を寒冷化させた上で維持する
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 影のマナ iBonusCount=1 / 混沌のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `bStayColdCounter`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Snowhole - 雪洞

- 内部名: `BUILDING_PAGAN_TEMPLE_NIVAL`
- 固有: ニバル（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 30[文化]
- 専門家枠: 神官 iSpecialistCount=1 / 吟遊詩人 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- 説明（ゲーム内ヘルプ）: 都市周辺の寒冷化を維持する
- その他の設定:
  - `bNeverCapture`: 1
  - `bStayColdCounter`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Atelier of Snow and Ice - 氷雪のアトリエ

- 内部名: `BUILDING_SIEGE_WORKSHOP_NIVAL`
- 固有: ニバル（攻城兵器工廠 の代替）
- 建造物クラス: 攻城兵器工廠
- コスト[ハンマー]: 60
- 必要テクノロジー: 数学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 吟遊詩人 iSpecialistCount=2
- 倍速の志向: 攻撃志向 iProductionTrait=100 / TXT_KEY_TRAIT_IMPERIALIST iProductionTrait=50
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10

### Rarna Palace - ラーナの宮殿

- 内部名: `BUILDING_PALACE_RARNA`
- 固有: ラーナ（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 法のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 炎のマナ iBonusCount=1 / 生命のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: 25
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Temple of the Inheritance - 継承の神殿

- 内部名: `BUILDING_TEMPLE_OF_THE_INHERITANCE`
- 固有: ラーナ（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出[%]: +10[商業]
- 産出(商業系)[%]: 10[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Alter of the Importance - 要の祭壇

- 内部名: `BUILDING_ALTAR_OF_THE_IMPORTANCE`
- 固有: ラーナ（黒曜石の門 の代替）
- 建造物クラス: 黒曜石の門
- コスト[ハンマー]: 240
- 必要テクノロジー: 魔術
- 産出[%]: +10[ハンマー]
- 産出(商業系)[%]: 20[文化]
- 倍速の志向: 迅速志向 iProductionTrait=100
- 説明（ゲーム内ヘルプ）: 死亡した自軍生物ユニットの魂を吸収して研究力に変換する
- その他の設定:
  - `iMaxLatitude`: 90
  - `iAirlift`: 1
  - `iHealRateChange`: 10
  - `iTradeRoutes`: 1
  - `fVisibilityPriority`: 1

### Tower of Martyr - 殉教者の塔

- 内部名: `BUILDING_TOWER_OF_MARTYR`
- 建造物クラス: 殉教者の塔
- コスト[ハンマー]: 150
- 必要テクノロジー: 狂信
- 必要な文明: ラーナ
- 産出(商業系): 8[ゴールド]
- [都市防御]: 25
- 説明（ゲーム内ヘルプ）: 建造した数に比例して、生物ユニットの転生の発生率が上昇する
- その他の設定:
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Tower of Mobius - 捻帯の塔

- 内部名: `BUILDING_TOWER_OF_MOBIUS`
- 建造物クラス: 捻帯の塔
- コスト[ハンマー]: 120
- 必要テクノロジー: 軍事行動
- 必要な文明: ラーナ
- 産出(商業系): 2[研究]
- 説明（ゲーム内ヘルプ）: 転生したユニットに対して、建造した数と同じだけの任意の無償の昇進を与える
- その他の設定:
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `iResistMagic`: 25

### Citizen of the Dead - 亡者の住処

- 内部名: `BUILDING_CITIZEN_OF_THE_DEAD`
- 建造物クラス: 亡者の住処
- 必要な文明: ラーナ
- 産出(商業系)[%]: -10[文化]
- その他の設定:
  - `bNoUnhealthyPopulation`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Immortal citizen - 不死人街

- 内部名: `BUILDING_IMMORTAL_CITIZEN`
- 建造物クラス: 不死人街
- 必要な文明: ラーナ
- 産出(商業系)[%]: -10[文化]
- その他の設定:
  - `bNoUnhappiness`: 1
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: 10
  - `iMilitaryProductionModifier`: -10
  - `fVisibilityPriority`: 1

### Abyss - 深淵

- 内部名: `BUILDING_ABYSS`
- 建造物クラス: 深淵
- 必要な文明: ラーナ
- 専門家枠: 賢者 iSpecialistCount=2
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -25
  - `fVisibilityPriority`: 1

### Tiger Palace - ティーグルの宮殿

- 内部名: `BUILDING_PALACE_TIGER`
- 固有: ティーグル（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 宝石
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 炎のマナ iBonusCount=1 / 肉体のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Victorious Target - 勝利の標

- 内部名: `BUILDING_TIGER_TEMPLE`
- 固有: ティーグル（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iWarWearinessModifier`: -10
  - `iHealRateChange`: 5
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Economic agreement - 経済協定

- 内部名: `BUILDING_ECONOMIC_AGREEMENT`
- 建造物クラス: 経済協定
- 必要な文明: ティーグル
- 説明（ゲーム内ヘルプ）: 契約戦争中のみ有効
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -50
  - `fVisibilityPriority`: 1
  - `GlobalCommerceModifiers`: 20[ゴールド], 20[研究], 40[文化]

### Seal of Overlords - 旧支配者の封印

- 内部名: `BUILDING_PALACE_XOTH`
- 固有: ゾス（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 混沌のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 精神のマナ iBonusCount=1 / 古書物 iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -10
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `StateReligionCommerces`: 1[ゴールド], 1[研究], 1[文化]
  - `iCrime`: -10
  - `iPlotRadius`: 3

### Seabed Temple - 海底神殿

- 内部名: `BUILDING_XOTH_TEMPLE`
- 固有: ゾス（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 30[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bWater`: 1
  - `bNoUnhappiness`: 1
  - `bNeverCapture`: 1
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `SeaPlotYieldChanges`: +1[商業]
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Baldralfar Palace - バルドルアールヴの宮殿

- 内部名: `BUILDING_PALACE_BALDRALFAR`
- 固有: バルドルアールヴ（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 自然のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 薄闇樹 iBonusCount=1 / 混沌のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: 10
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Mandos Palace - マンドスの館

- 内部名: `BUILDING_MANDOS_PALACE`
- 固有: バルドルアールヴ（英雄叙事詩 の代替）
- 建造物クラス: 英雄叙事詩
- コスト[ハンマー]: 200
- 必要テクノロジー: 軍事戦略
- 供給する資源: 生命のマナ
- 供給数: 1
- 倍速の資源: 大理石 iProductonModifier=100
- その他の設定:
  - `GreatPeopleUnitClass`: 偉大な指揮官
  - `iGreatPeopleRateChange`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iMilitaryProductionModifier`: 100
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Altar of the Rebirth - 再生の祭壇

- 内部名: `BUILDING_BALDRALFAR_TEMPLE`
- 固有: バルドルアールヴ（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- 説明（ゲーム内ヘルプ）: 都市の周囲2タイル以内を肥沃化させる
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Nougbii Palace - ノービアイの宮殿

- 内部名: `BUILDING_PALACE_NOUGBII`
- 固有: ノービアイ（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 呪付のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 金 iBonusCount=1 / 大地のマナ iBonusCount=1 / 精製されたマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -10
  - `fVisibilityPriority`: 10000
  - `PowerYieldModifiers`: +10[食料]
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Workshop of Civlent Association - シヴレント工房

- 内部名: `BUILDING_NOUGBII_TEMPLE`
- 固有: ノービアイ（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- 産出[%]: +10[食料]
- 産出(商業系)[%]: 10[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `PowerYieldModifiers`: +5[食料]
  - `BonusHappinessChanges`: 香木 iHappinessChange=1
  - `BonusYieldModifiers`: 精製されたマナ

### Incubator - 複製の竈

- 内部名: `BUILDING_INCUBATOR`
- 固有: ノービアイ（穀倉 の代替）
- 建造物クラス: 穀倉
- コスト[ハンマー]: 100
- 必要テクノロジー: 暦
- [幸福]: -3
- 産出[%]: +10[食料]
- 倍速の志向: 拡張志向 iProductionTrait=100 / 農耕志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 古典期
  - `iMaxLatitude`: 90
  - `iFoodKept`: 60
  - `iMilitaryProductionModifier`: 10
  - `fVisibilityPriority`: 10
  - `PowerYieldModifiers`: +10[食料], +10[ハンマー]

### Tower of the spiral - 螺旋の塔

- 内部名: `BUILDING_TOWER_OF_THE_SPIRAL`
- 固有: ノービアイ（劇場 の代替）
- 建造物クラス: 劇場
- コスト[ハンマー]: 200
- 必要テクノロジー: 演劇
- [幸福]: 6
- 産出(商業系)[%]: 30[文化]
- 専門家枠: 吟遊詩人 iSpecialistCount=1
- 倍速の志向: 創造志向 iProductionTrait=100 / 伝道志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `iMilitaryProductionModifier`: -25
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 4[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `CommerceHappinesses`: 10[文化]
  - `BonusHappinessChanges`: 染料 iHappinessChange=1 / 絹 iHappinessChange=1

### Palace of the Aristrakh - アリストラクの宮殿

- 内部名: `BUILDING_PALACE_ARISTRAKH`
- 固有: アリストラク（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 死のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 肉体のマナ iBonusCount=1 / 影のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -50
  - `fVisibilityPriority`: 20000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Haunted Roads - 悪霊小路

- 内部名: `BUILDING_HAUNTED_ROADS`
- 固有: アリストラク（水道橋 の代替）
- 建造物クラス: 水道橋
- コスト[ハンマー]: 140
- 必要テクノロジー: 衛生設備
- 産出(商業系)[%]: 5[文化]
- 専門家枠: 吟遊詩人 iSpecialistCount=2
- 倍速の志向: 拡張志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 未来
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `iTradeRoutes`: 1
  - `iTradeRouteModifier`: 50
  - `iForeignTradeRouteModifier`: -50
  - `fVisibilityPriority`: 10
  - `ObsoleteSafeCommerceChanges`: 5[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Corrupted Soil - 汚された土壌

- 内部名: `BUILDING_CORRUPTED_SOIL`
- 固有: アリストラク（ビール醸造所 の代替）
- 建造物クラス: ビール醸造所
- コスト[ハンマー]: 90
- 必要テクノロジー: 道具の作成
- 必要な資源（いずれか）: トウモロコシ / 米 / 砂糖 / 小麦
- 専門家枠: 商人 iSpecialistCount=1
- 倍速の志向: カリスマ志向 iProductionTrait=100
- 説明（ゲーム内ヘルプ）: 川沿い都市にのみ建設可能
- その他の設定:
  - `bRiver`: 1
  - `iMaxLatitude`: 90
  - `iForeignTradeRouteModifier`: -25
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Bone Cage - 屍骸の檻

- 内部名: `BUILDING_BONE_CAGE`
- 固有: アリストラク（巡業サーカス の代替）
- 建造物クラス: 巡業サーカス
- コスト[ハンマー]: 120
- 必要テクノロジー: 祝祭
- 陳腐化: 蒸気機関
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 吟遊詩人 iSpecialistCount=2
- 倍速の志向: 創造志向 iProductionTrait=100
- その他の設定:
  - `MaxStartEra`: 未来
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `BonusYieldModifiers`: エール酒

### Burial Mound - 埋葬塚

- 内部名: `BUILDING_BURIAL_MOUND`
- 固有: アリストラク（穀倉 の代替）
- 建造物クラス: 穀倉
- コスト[ハンマー]: 40
- 必要テクノロジー: 暦
- 産出: +1[ハンマー]
- 産出(商業系): 1[ゴールド]
- 専門家枠: 技師 iSpecialistCount=1
- 倍速の志向: 拡張志向 iProductionTrait=100 / 農耕志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 古典期
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Forlorn Vault - 寄る辺なき納骨堂

- 内部名: `BUILDING_FORLORN_VAULT`
- 固有: アリストラク（鎮守の杜 の代替）
- 建造物クラス: 鎮守の杜
- コスト[ハンマー]: 140
- 必要テクノロジー: 野生の触れ合い
- 産出(商業系): 2[ゴールド]
- 専門家枠: 商人 iSpecialistCount=2
- 倍速の志向: 伝道志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -15
  - `fVisibilityPriority`: 1

### Halls of the Dead - 死者の間

- 内部名: `BUILDING_HALLS_OF_THE_DEAD`
- 固有: アリストラク（薬草師 の代替）
- 建造物クラス: 薬草師
- コスト[ハンマー]: 60
- 必要テクノロジー: 農業
- 専門家枠: 商人 iSpecialistCount=1
- 倍速の志向: 野戦志向 iProductionTrait=100
- その他の設定:
  - `FreeStartEra`: 中世
  - `iMaxLatitude`: 90
  - `iHealRateChange`: 10
  - `fVisibilityPriority`: 10
  - `SupplyPromotionProbabilities`: 病気 iProbability=-10
  - `BonusYieldModifiers`: 秘薬 / 綿花 / キノコ
  - `RemovePromotion`: 毒

### Mausoleum - 霊廟

- 内部名: `BUILDING_MAUSOLEUM`
- 固有: アリストラク（診療所 の代替）
- 建造物クラス: 診療所
- コスト[ハンマー]: 250
- 必要テクノロジー: 医薬
- 必要な建造物: 薬草師
- 産出(商業系)[%]: 20[研究], 20[文化]
- 倍速の志向: 野戦志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `iHealRateChange`: 25
  - `iSpaceProductionModifier`: 25
  - `fVisibilityPriority`: 1
  - `SupplyPromotionProbabilities`: 病気 iProbability=-100 / 疫病 iProbability=-10 / 衰弱 iProbability=-10 / 黒死病 iProbability=-10
  - `BonusYieldModifiers`: 剃刀草

### Mortuary Enclosure - 霊安倉

- 内部名: `BUILDING_MORTUARY_ENCLOSURE`
- 固有: アリストラク（灯台 の代替）
- 建造物クラス: 灯台
- コスト[ハンマー]: 120
- 必要テクノロジー: 航海術
- 産出: +1[ハンマー]
- 産出(商業系): 3[ゴールド]
- 専門家枠: 商人 iSpecialistCount=1 / 技師 iSpecialistCount=1
- 倍速の志向: 組織志向 iProductionTrait=100 / 交易志向 iProductionTrait=100
- 倍速の資源: 石材 iProductonModifier=100
- その他の設定:
  - `FreeStartEra`: 中世
  - `bWater`: 1
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `iTradeRoutes`: 1
  - `fVisibilityPriority`: 10

### Haunted Tower - 悪霊の塔

- 内部名: `BUILDING_HAUNTED_TOWER`
- 固有: アリストラク（市場 の代替）
- 建造物クラス: 市場
- コスト[ハンマー]: 150
- 必要テクノロジー: 祝祭
- 陳腐化: 蒸気機関
- 産出(商業系): 3[ゴールド], 2[研究]
- 専門家枠: 商人 iSpecialistCount=1 / 賢者 iSpecialistCount=1
- 倍速の志向: 金融志向 iProductionTrait=100 / 交易志向 iProductionTrait=100 / 強欲志向 iProductionTrait=100
- その他の設定:
  - `MaxStartEra`: 未来
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 10
  - `BonusYieldModifiers`: バナナ / 象牙

### Unholy Glyphs - 不浄なる標

- 内部名: `BUILDING_UNHOLY_GLYPHS`
- 固有: アリストラク（公衆浴場 の代替）
- 建造物クラス: 公衆浴場
- コスト[ハンマー]: 150
- 必要テクノロジー: 衛生設備
- 専門家枠: 神官 iSpecialistCount=2
- その他の設定:
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `iBombardDefense`: 50
  - `fVisibilityPriority`: 1

### Unearthed Graves - 暴かれた墓所

- 内部名: `BUILDING_UNEARTHED_GRAVES`
- 固有: アリストラク（燻製場 の代替）
- 建造物クラス: 燻製場
- コスト[ハンマー]: 35
- 必要テクノロジー: 動物の馴致
- 産出: +2[ハンマー]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 農耕志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 9

### Soulprison - 魂の牢獄

- 内部名: `BUILDING_SOUL_PRISON`
- 固有: アリストラク（徴税所 の代替）
- 建造物クラス: 徴税所
- コスト[ハンマー]: 120
- 必要テクノロジー: 税制
- 産出(商業系)[%]: 25[ゴールド]
- 専門家枠: 商人 iSpecialistCount=1
- 倍速の志向: 徴税志向 iProductionTrait=100 / 強欲志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Catacombs - 墳墓

- 内部名: `BUILDING_CATACOMBS`
- 固有: アリストラク（劇場 の代替）
- 建造物クラス: 劇場
- コスト[ハンマー]: 250
- 必要テクノロジー: 演劇
- 産出(商業系)[%]: 30[文化]
- 専門家枠: 吟遊詩人 iSpecialistCount=3
- 倍速の志向: 創造志向 iProductionTrait=100 / 伝道志向 iProductionTrait=100
- その他の設定:
  - `iMaxLatitude`: 90
  - `iMaintenanceModifier`: -15
  - `iSpaceProductionModifier`: 25
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 5[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]
  - `BonusYieldModifiers`: 染料 / 絹

### Undead City - 死都

- 内部名: `BUILDING_UNDEAD_CITY`
- 建造物クラス: 死都
- 必要な文明: アリストラク
- [幸福]: 3
- その他の設定:
  - `bNoUnhealthyPopulation`: 1
  - `bNeverCapture`: 1
  - `bCenterInCity`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 11000

### Megisus Palace - メギススの宮殿

- 内部名: `BUILDING_PALACE_MEGISUS`
- 固有: メギスス（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- 供給する資源: 大気のマナ
- 供給数: 1
- その他の設定:
  - `ObsoleteSafeFreeBonuses`: 法のマナ iBonusCount=1 / 魂のマナ iBonusCount=1
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: 10
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10

### Temple of Nantosuelta - ナントスエルタの神殿

- 内部名: `BUILDING_MEGISUS_TEMPLE`
- 固有: メギスス（土着の神殿 の代替）
- 建造物クラス: 土着の神殿
- コスト[ハンマー]: 100
- 必要テクノロジー: 哲学
- [幸福]: 1
- [衛生]: 1
- 産出(商業系)[%]: 20[文化]
- 専門家枠: 神官 iSpecialistCount=1
- 倍速の志向: 宗教志向 iProductionTrait=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `BonusHappinessChanges`: 香木 iHappinessChange=1

### Hermes emblem - ヘルメスの紋章

- 内部名: `BUILDING_HELMES_EMBLEM`
- 建造物クラス: ヘルメスの紋章
- コスト[ハンマー]: 200
- 必要テクノロジー: 叡智への道
- 必要な文明: メギスス
- 産出[%]: +15[ハンマー]
- 倍速の資源: 肉体のマナ iProductonModifier=100
- その他の設定:
  - `bNeverCapture`: 1
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `FreePromotionProbabilities`: 機動力Ⅰ iProbability=80

### Spring of Ghnuke - グヌークの泉

- 内部名: `BUILDING_SPRING_OF_GHNUKE`
- 建造物クラス: グヌークの泉
- コスト[ハンマー]: 500
- 必要テクノロジー: 四大元素
- 必要な文明: メギスス
- [衛生]: 2
- 産出(商業系)[%]: 20[文化]
- 供給する資源: 水のマナ
- 供給数: 1
- 倍速の資源: 水のマナ iProductonModifier=100
- 説明（ゲーム内ヘルプ）: 生きている鎧に弾幕Ⅰを与える / 川沿い都市にのみ建設可能
- その他の設定:
  - `bRiver`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iFoodKept`: 20
  - `iGlobalHealth`: 1
  - `fVisibilityPriority`: 1
  - `ObsoleteSafeCommerceChanges`: 3[文化]
  - `CommerceChangeDoubleTimes`: 100[文化]

### Furnace of Midas - ミダスの錬成炉

- 内部名: `BUILDING_FORNACE_OF_MIDAS`
- 建造物クラス: ミダスの錬成炉
- コスト[ハンマー]: 450
- 必要テクノロジー: 変成術
- 必要な文明: メギスス
- [幸福]: 2
- 産出(商業系)[%]: 50[ゴールド], -20[文化]
- 供給する資源: 呪付のマナ
- 供給数: 1
- 倍速の資源: 呪付のマナ iProductonModifier=100
- 説明（ゲーム内ヘルプ）: ホムンクルスの召喚数を1体追加する / ターン経過によりランダムに+1
- その他の設定:
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `iGlobalHappiness`: 1
  - `iGlobalPopulationChange`: 1
  - `fVisibilityPriority`: 1

### Circle of monsoon - 陽と風の魔法円

- 内部名: `BUILDING_CIRCLE_OF_MONSOON`
- 建造物クラス: 陽と風の魔法円
- コスト[ハンマー]: 600
- 必要テクノロジー: 予言術
- 必要な文明: メギスス
- 供給する資源: 太陽のマナ
- 供給数: 1
- 倍速の資源: 太陽のマナ iProductonModifier=100
- 説明（ゲーム内ヘルプ）: 生きている鎧を+1:戦闘力
- その他の設定:
  - `bWater`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMinAreaSize`: 10
  - `iMaxLatitude`: 90
  - `iGlobalGreatPeopleRateModifier`: 25
  - `iGoldenAgeModifier`: 25
  - `fVisibilityPriority`: 1

### Heart of the chaos - 混沌の中心

- 内部名: `BUILDING_HEART_OF_THE_CHAOS`
- 建造物クラス: 混沌の中心
- コスト[ハンマー]: 700
- 必要テクノロジー: 屍霊術
- 必要な文明: メギスス
- 倍速の資源: 混沌のマナ iProductonModifier=100
- 説明（ゲーム内ヘルプ）: 精霊のユニットが戦闘で死亡すると毒ダメージを周囲に与えるようになる
- その他の設定:
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `GlobalYieldModifiers`: +15[ハンマー], +15[商業]
  - `BonusYieldModifiers`: 混沌のマナ
  - `iGlobalResistEnemyModify`: -20

### Forest eclipse - 日食の杜

- 内部名: `BUILDING_FOREST_ECLIPSE`
- 建造物クラス: 日食の杜
- コスト[ハンマー]: 350
- 必要テクノロジー: 魔術
- 必要な文明: メギスス
- 倍速の資源: 超魔術のマナ iProductonModifier=100
- 説明（ゲーム内ヘルプ）: ターン開始時に領内に資源が湧くことがある / （大地のマナにより資源発生の確率上昇）
- その他の設定:
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1

### Force field of creation - 創造の結界

- 内部名: `BUILDING_FORCE_FIELD_OF_CREATION`
- 建造物クラス: 創造の結界
- コスト[ハンマー]: 1500
- 必要テクノロジー: 高潔の証
- 必要な文明: メギスス
- 倍速の資源: 古書物 iProductonModifier=100
- その他の設定:
  - `bBorderObstacle`: 1
  - `bGoldenAge`: 1
  - `bNeverCapture`: 1
  - `iHurryCostModifier`: 50
  - `iMaxLatitude`: 90
  - `fVisibilityPriority`: 1
  - `ImprovementFreeSpecialists`: 緑葉の庵 iFreeSpecialistCount=1 / 緑葉の邑 iFreeSpecialistCount=1 / 緑葉の里 iFreeSpecialistCount=1 / 緑葉の大地 iFreeSpecialistCount=1

### Letum Frigus Palace - レートゥム・フリグスの宮殿

- 内部名: `BUILDING_PALACE_LETUM_FRIGUS`
- 固有: レートゥム・フリグス（バンノールの宮殿 の代替）
- 建造物クラス: 宮殿
- コスト[ハンマー]: 160
- [幸福]: 1
- 産出: +1[ハンマー], +8[商業]
- その他の設定:
  - `bCapital`: 1
  - `bGovernmentCenter`: 1
  - `bNeverCapture`: 1
  - `bNukeImmune`: 1
  - `iHurryCostModifier`: 50
  - `iCitiesPrereq`: 4
  - `iMaxLatitude`: 90
  - `iGlobalWarWearinessModifier`: -10
  - `fVisibilityPriority`: 10000
  - `ObsoleteSafeCommerceChanges`: 2[文化]
  - `iCrime`: -10
