# OAC/文明（0.57、XMLから生成）

- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）
- 生成元: `Civilizations/CIV4CivilizationInfos.xml`
- 読み方: 主要な項目は日本語ラベル付きで先頭に、それ以外の既定値でない設定は「その他の設定」にXMLのタグ名のまま列挙する。値の内部名は日本語名に置き換えている。Pythonで実装された効果はXMLにないため含まない（ゲーム内ヘルプの説明文があれば載せている）。

### Bannor - バンノール

- 内部名: `CIVILIZATION_BANNOR`
- 初期テクノロジー: 道具の作成 / 探検
- 指導者: サバシエル / カプリア / テシラ / デキウス / ガヘリス / アンガード
- 代替ユニット: 近衛騎兵 神殿騎士
- 代替建造物: 宮殿 バンノールの宮殿 / 図書館 修道院 / 裁判所 枢密院 / 土着の神殿 ユーニルの神殿 / 民族叙事詩 至聖所
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_BANNOR
  - `ArtStyleType`: ARTSTYLE_BANNOR
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: ファランクス iLimit=12
  - `MinGameProgressPercents`: 数学 iGameProgressPercent=30 / 狂信 iGameProgressPercent=35 / 鉄器 iGameProgressPercent=50 / ミスリルの武具 iGameProgressPercent=70
  - `UnitDescriptions`: 戦士 執行官 / 斧兵 護衛官 / 勇士 守護の勇士
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ImprovementYieldChanges`: 要塞 +1[ハンマー]
  - `InitialCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 護衛

### Malakim - マラキム

- 内部名: `CIVILIZATION_MALAKIM`
- 初期テクノロジー: 狩猟 / 原初の祈り
- 指導者: ヴァーン・ゴッサム / デキウス / ケイン / シャマシュ / ユシージャ / サラレット
- 代替ユニット: 弓騎兵 駱駝射手
- 代替建造物: 土着の神殿 砂漠の祭殿 / 宮殿 マラキムの宮殿 / 図書館 修道院 / 裁判所 枢密院 / 民族叙事詩 千夜一夜物語
- 種族: 砂漠の民
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_MALAKIM
  - `ArtStyleType`: ARTSTYLE_MALAKIM
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: TXT_KEY_UNIT_HIGH_PRIEST_OF_THE_ORDER iLimit=12 / 至天の光輝者 iLimit=12 / TXT_KEY_UNIT_HIGH_PRIEST_OF_KILMORPH iLimit=12
  - `MinGameProgressPercents`: 聖職 iGameProgressPercent=30 / 魔術 iGameProgressPercent=50 / 神学 iGameProgressPercent=70
  - `UnitDescriptions`: 斧兵 剣士 / 勇士 熱砂の番人 / ファランクス スパルティアタイ
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 灯火の信徒 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `TerrainYieldChanges`: 砂漠 +1[ハンマー], +1[商業]
  - `FeatureYieldChanges`: 氾濫原
  - `ImprovementYieldChanges`: ユルト +1[商業] / ゴウム +1[商業] / アデュアル +1[ハンマー], +1[商業]
  - `InitialCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `MaintainFeatures`: 灌木林

### Elohim - エロヒム

- 内部名: `CIVILIZATION_ELOHIM`
- 初期テクノロジー: 農業 / 原初の祈り
- 指導者: 白きエスネ / エイニオン・ロゴス / テサロニカ / ネフェレ / ミレス / ヴェスタ
- 代替ユニット: 暗殺者 篤信家 / 近衛騎兵 神殿騎士
- 代替建造物: 宮殿 エロヒムの宮殿 / 土着の神殿 シロナの神託所 / 図書館 修道院 / 裁判所 枢密院
- 説明（ゲーム内ヘルプ）: 名所旧跡の位置を把握できる
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_ELOHIM
  - `ArtStyleType`: ARTSTYLE_ELOHIM
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 聖騎士 iLimit=12
  - `MinGameProgressPercents`: 叡智への道 iGameProgressPercent=25 / 聖職 iGameProgressPercent=35 / 狂信 iGameProgressPercent=45
  - `UnitDescriptions`: 勇士 退魔士 / 斧兵 剣士 / ファランクス スパルティアタイ
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `InitialCivics`: 専制政治 / 平和主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 平和主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 寛容志向

### Mercurians - マーキュリアン

- 内部名: `CIVILIZATION_MERCURIANS`
- 初期テクノロジー: 道具の作成
- 指導者: バシウム
- 代替ユニット: 戦士 / 斥候 / 弩兵 / 火縄銃兵 / 魔獣使い 御使い / 狂戦士 熾天使 / 不死者 戦乙女 / 騎士 座天使 / 狙撃手 / ファランクス 後悔の天使 / 影法師 死の天使
- 代替建造物: 宮殿 マーキュリアンの宮殿 / 土着の神殿 聖櫃
- 説明（ゲーム内ヘルプ）: 善良なユニットが死亡すると天使 を得る / [SPACE][SPACE]都市は蒼褪めたヴェール を放逐する
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_MERCURIANS
  - `ArtStyleType`: ARTSTYLE_MERCURIANS
  - `NationalUnitClassLimits`: シドおじさんの聖なる手榴弾 iLimit=12 / エレメント・デストロイヤー iLimit=3
  - `MinGameProgressPercents`: 狂暴 iGameProgressPercent=50 / ギルド iGameProgressPercent=50 / 高潔の証 iGameProgressPercent=60
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### Luchuirp - ルシュイアープ

- 内部名: `CIVILIZATION_LUCHUIRP`
- 初期テクノロジー: 道具の作成 / 漁業
- 指導者: ガリム・ギュール / ビーリ・バウル / ギズリ / キシュ・リカ / レティゴ / ベア・グイン
- 代替ユニット: 労働者 泥のゴーレム / 斧兵 木のゴーレム / 騎乗兵 猪の騎乗兵 / 勇士 鉄のゴーレム / 長弓兵 ガーゴイル / レンジャー / 弓騎兵 / 魔獣使い / 狂戦士 機械仕掛けのゴーレム / ドルイド僧 ドワーフドルイド僧 / 不死者 骨のゴーレム / 騎士 ドワーフホーンガード / 狙撃手 / ファランクス 虚無石のゴーレム / 影法師 ドワーフ影法師
- 代替建造物: 宮殿 ルシュイアープの宮殿 / 練兵場 彫刻家のアトリエ / 鍛冶屋 ゴーレムの工房 / 土着の神殿 ナントスエルタの鍛冶場
- 種族: ドワーフ
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_LUCHUIRP
  - `ArtStyleType`: ARTSTYLE_LUCHUIRP
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 不死者 iLimit=12
  - `MinGameProgressPercents`: 石工 iGameProgressPercent=15 / 建設 iGameProgressPercent=30 / 四大元素 iGameProgressPercent=35 / 工学 iGameProgressPercent=40 / 鉄器 iGameProgressPercent=50
  - `ManaWeightModifiers`: 炎のノードを展開 iModifier=70 / 太陽のノードを展開 iModifier=50 / 影のノードを展開 iModifier=30
  - `UnitDescriptions`: 弓兵 ドワーフ投石兵
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ImprovementYieldChanges`: 工房 +1[商業] / ドワーフの工房 +1[商業]
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### Kuriotates - クリオテイテ

- 内部名: `CIVILIZATION_KURIOTATES`
- 初期テクノロジー: 狩猟 / 農業
- 指導者: カーディス・ローダ / 教導官ウェルシュ / ファーヴナ / ヒュンケル / ヘルネ / シス・モー / シェロン
- 代替ユニット: 騎乗兵 ケンタウロス / 弓騎兵 ケンタウロス射手 / 戦車兵 ケンタウロス突撃兵 / 騎士 ケンタウロス槍騎兵 / 戦列の女王 飛空艇 / カタパルト ミノタウロス攻城兵
- 代替建造物: 宮殿 クリオテイテの宮殿 / 厩舎 / 土着の神殿 アマサオンの神殿
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_KURIOTATES
  - `ArtStyleType`: ARTSTYLE_KURIOTATES
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 騎士 iLimit=12
  - `MinGameProgressPercents`: 騎乗 iGameProgressPercent=15 / 数学 iGameProgressPercent=25 / 交易 iGameProgressPercent=30 / 鐙 iGameProgressPercent=35 / 重商主義 iGameProgressPercent=55 / 軍馬 iGameProgressPercent=70
  - `UnitDescriptions`: ファランクス スパルティアタイ
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ImprovementYieldChanges`: 自治区 +1[食料], +1[商業]
  - `InitialCivics`: 専制政治 / 平和主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 平和主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### Ljosalfar - リョースアールヴ

- 内部名: `CIVILIZATION_LJOSALFAR`
- 初期テクノロジー: 道具の作成 / 狩猟
- 指導者: アメランキエル / アレンデル・パイドラ / テッサ / アイベル / サウレー / エルダーウェン・アルカリン
- 代替ユニット: 長弓兵 女王の矢 / 弩兵 疾風隊 / 弓騎兵 フュルドウェル / 魔術師 幻術師 / 戦車兵 / カタパルト / 火縄銃兵 / 狂戦士 / 大砲
- 代替建造物: 錬金術ラボ / 宮殿 リョースアールヴの宮殿 / 攻城兵器工廠 / 土着の神殿 ケルヌンノスの杜 / 機械工場 / プラント
- 種族: エルフ
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_LJOSALFAR
  - `ArtStyleType`: ARTSTYLE_LJOSALFAR
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 弩兵 iLimit=12
  - `MinGameProgressPercents`: 弓術 iGameProgressPercent=15 / 深き森への道 iGameProgressPercent=25 / 複合弓 iGameProgressPercent=35 / 機械 iGameProgressPercent=70
  - `ManaWeightModifiers`: 炎のノードを展開 iModifier=70
  - `UnitDescriptions`: 斧兵 剣士 / 勇士 スケルスの監視者
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 斥候 iFreeUnits=1 / 戦士 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ImprovementYieldChanges`: 狩猟場 +1[ハンマー] / 大狩猟場 +1[ハンマー] / 炭焼き小屋 +1[商業]
  - `InitialCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 器用
  - `MaintainFeatures`: 森林 / 古代樹林 / 若き森林

### Khazad - カザード

- 内部名: `CIVILIZATION_KHAZAD`
- 初期テクノロジー: 道具の作成 / 狩猟
- 指導者: アーチュラス・ソーン / カンドロス・ファー / ニコデマス / アゼル / ビトニール / リャメラダ・バーダ
- 代替ユニット: 騎乗兵 猪の騎乗兵 / 魔術師 / 長弓兵 / レンジャー / 弓騎兵 / カタパルト トレビュシェット / 大魔道 / 魔獣使い マイコニド / ドルイド僧 ドワーフドルイド僧 / 騎士 ドワーフホーンガード / 狙撃手 / 影法師 ドワーフ影法師 / 大砲 ドワーフの大砲
- 代替建造物: 鍛冶屋 ドワーフの鍛冶場 / 宮殿 カザードの宮殿 / 土着の神殿 キルモフの洞穴
- 種族: ドワーフ
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_KHAZAD
  - `ArtStyleType`: ARTSTYLE_KHAZAD
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: ドルイド僧 iLimit=12
  - `MinGameProgressPercents`: 青銅器 iGameProgressPercent=15 / 建設 iGameProgressPercent=30 / 鉄器 iGameProgressPercent=45 / 爆薬 iGameProgressPercent=60
  - `ManaWeightModifiers`: 呪付のノードを展開 iModifier=70
  - `UnitDescriptions`: 弓兵 ドワーフ投石兵 / 勇士 ドワーフ鉄鎚兵 / ファランクス スパルティアタイ
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=2
  - `FreeBuildingClasses`: 宮殿
  - `ExtraPrereqAndTechs`: 爆薬 鉄器
  - `ExtraPrereqOrTechs`: 爆薬 工学 / 蒸気機関 工学
  - `ImprovementYieldChanges`: 鉱山 +1[商業] / 立坑鉱山 +1[商業]
  - `InitialCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 兵器改良

### Sidar - シダー

- 内部名: `CIVILIZATION_SIDAR`
- 初期テクノロジー: 狩猟 / 原初の祈り
- 指導者: サンダルフォン / シェキナ / シュムエル / ミローフ / リーシー / ラジエル
- 代替ユニット: 暗殺者 亡霊 / 狩人 魂の緒 / 労働者 影の手 / 斥候 密偵 / レンジャー 禍祓い / 魔獣使い 依巫
- 代替建造物: 宮殿 シダーの宮殿 / 土着の神殿 聖所
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_SIDAR
  - `ArtStyleType`: ARTSTYLE_SIDAR
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 不死者 iLimit=12 / 影の騎士 iLimit=12
  - `MinGameProgressPercents`: 追跡術 iGameProgressPercent=10 / 筆記 iGameProgressPercent=20 / 詐欺 iGameProgressPercent=30 / 動物の馴致 iGameProgressPercent=35 / 毒物 iGameProgressPercent=45
  - `UnitDescriptions`: ファランクス スパルティアタイ
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `InitialCivics`: 専制政治 / 平和主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 平和主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 忍足

### Lanun - ラヌーン

- 内部名: `CIVILIZATION_LANUN`
- 初期テクノロジー: 海洋志向 / 探検 / 漁業
- 指導者: ファラマー / ハンナ・ジ・イリン / フリッツ船長 / ナイアス / カジン・ラヴレス / モードモーガン
- 代替ユニット: 勇士 斬り込み隊 / 騎士 戦亀 / 私掠船 海賊船
- 代替建造物: 港 避難港 / 宮殿 ラヌーンの宮殿 / 土着の神殿 ダナリンの湧水
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_LANUN
  - `ArtStyleType`: ARTSTYLE_LANUN
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 騎士 iLimit=12
  - `MinGameProgressPercents`: 光学 iGameProgressPercent=30 / 鉄器 iGameProgressPercent=45
  - `UnitDescriptions`: 斧兵 剣士 / 鷹 オウム
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `TerrainYieldChanges`: 近海 +1[食料] / 外洋 +1[商業]
  - `ImprovementYieldChanges`: 海賊の隠れ家 +1[商業] / 海賊の港 +1[ハンマー], +2[商業] / 海賊の港町 +1[食料], +2[ハンマー], +3[商業]
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 水陸両用

### Grigori - グリゴリ

- 内部名: `CIVILIZATION_GRIGORI`
- 初期テクノロジー: 道具の作成 / 農業
- 指導者: カシエル / コウン大臣 / ゴルベーザ / メリッサ・ドリズル / グッドレオー / メネク / ゾーダロール / オーセ
- 代替ユニット: 勇士 ドラゴンスレイヤー / ドルイド僧 ルオンノタル
- 代替建造物: 土着の神殿 ダグダの記念碑 / 宮殿 グリゴリの宮殿 / 巡業サーカス 冒険者集会
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_GRIGORI
  - `ArtStyleType`: ARTSTYLE_GRIGORI
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: ドルイド僧 iLimit=12
  - `MinGameProgressPercents`: 通貨 iGameProgressPercent=30 / 製錬 iGameProgressPercent=40 / 医薬 iGameProgressPercent=50
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ExtraPrereqAndTechs`: 神々の本質 ミスリルの武具
  - `ExtraPrereqOrTechs`: 神々の本質 意志の力
  - `InitialCivics`: 専制政治 / 平和主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 平和主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### Hippus - ヒッパス

- 内部名: `CIVILIZATION_HIPPUS`
- 初期テクノロジー: 狩猟 / 農業
- 指導者: タスンケ / ロアンナ / オスタネス隊長 / ウルダンノール隊長 / セルマ / イリシリダン
- 代替ユニット: 傭兵 傭騎兵 / 火縄銃兵 / 大砲
- 代替建造物: 錬金術ラボ / 宮殿 ヒッパスの宮殿 / 土着の神殿 風の塔
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_HIPPUS
  - `ArtStyleType`: ARTSTYLE_HIPPUS
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 騎士 iLimit=12 / 傭兵 iLimit=24
  - `MinGameProgressPercents`: 騎乗 iGameProgressPercent=15 / 交易 iGameProgressPercent=25 / 建設 iGameProgressPercent=30 / 通貨 iGameProgressPercent=35 / 鐙 iGameProgressPercent=35 / 重商主義 iGameProgressPercent=50 / 軍馬 iGameProgressPercent=70
  - `UnitDescriptions`: 弓騎兵 馬賊 / 勇士 ハイウェイマン / ファランクス スパルティアタイ
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ImprovementYieldChanges`: 牧草地 +1[商業] / 大牧草地 +1[商業] / ユルト +1[食料] / ゴウム +1[食料] / アデュアル +1[食料]
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 駿馬

### Amurites - アムリテ

- 内部名: `CIVILIZATION_AMURITES`
- 初期テクノロジー: 漁業 / 原初の祈り
- 指導者: 均等なるヴァレディア / デイン・ザ・カスワラウン / ティヤ・キリ / グウィエン / バーレイン / ローレライ・コーラル
- 代替ユニット: 魔術師 ウィザード / 長弓兵 火弓隊 / 暗殺者 詠唱者
- 代替建造物: 宮殿 アムリテの宮殿 / 土着の神殿 オグマの図書館 / 裁判所 秘術法廷 / 図書館 魔導書院
- 説明（ゲーム内ヘルプ）: すべてのマナの初期配置を可視化
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_AMURITES
  - `ArtStyleType`: ARTSTYLE_AMURITES
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 大魔道 iLimit=8
  - `MinGameProgressPercents`: エーテルの知識 iGameProgressPercent=15 / 筆記 iGameProgressPercent=20 / 複合弓 iGameProgressPercent=35 / 魔術 iGameProgressPercent=40 / 秘術の伝承知識 iGameProgressPercent=50
  - `UnitDescriptions`: 勇士 エンチャンター / 斧兵 剣士
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `UnitCombatUpgradeDiscounts`: 秘術ユニット iDiscount=33
  - `CivTrait`: 血統

### Doviello - ドヴィエロ

- 内部名: `CIVILIZATION_DOVIELLO`
- 初期テクノロジー: 道具の作成 / 狩猟
- 指導者: キャラドン / マヘイラ / 半獣のデュイン男爵 / ビュグヴィル / シルバガー / エマ・ヴァルガモア
- 代替ユニット: 戦士 野蛮人 / 術使い まじない医 / 斧兵 アセナの末裔 / 弓兵 投槍兵 / 勇士 闘将 / 火縄銃兵 / 狂戦士 ウルズの円陣 / 不死者 スクルド / 騎士 野牛の騎士 / 狙撃手 / ファランクス ヴェルザンディ / 大砲 / TXT_KEY_UNIT_WORKBOAT バス船
- 代替建造物: 錬金術ラボ / 図書館 / 魔術師ギルド / 宮殿 ドヴィエロの宮殿 / 土着の神殿 狂戦士の闘技場
- 種族: 寒冷種
- 説明（ゲーム内ヘルプ）: 戦闘で敵から武器を奪い取ることが できる / [SPACE][SPACE]都市を破壊すると周辺の中立地帯を 自動で掠奪
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_DOVIELLO
  - `ArtStyleType`: ARTSTYLE_DOVIELLO
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: ファランクス iLimit=12
  - `MinGameProgressPercents`: 地図 iGameProgressPercent=10 / 青銅器 iGameProgressPercent=15 / 軍事行動 iGameProgressPercent=25 / 製錬 iGameProgressPercent=35 / 狂暴 iGameProgressPercent=50 / ミスリルの武具 iGameProgressPercent=70
  - `UnitDescriptions`: カタパルト 髑髏カタパルト / 魔術師 祈祷師 / ファランクス スパルティアタイ
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ImprovementTerrains`: 凍土
  - `TerrainYieldChanges`: 凍土 +1[ハンマー]
  - `ImprovementYieldChanges`: 狩猟場 +1[食料] / 大狩猟場 +1[食料] / 捕鯨船 +1[食料]
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `UnitCombatUpgradeDiscounts`: 白兵ユニット iDiscount=50
  - `CivTrait`: 残存

### Balseraphs - バルセラフ

- 内部名: `CIVILIZATION_BALSERAPHS`
- 初期テクノロジー: 農業 / 原初の祈り
- 指導者: パーペンタク / キーリン / ウィーヴィルとピクルとハイド / 狂気のフューリア / メリサンドラ / タリエシン / だまし絵のノヤ－ / 早業のネル
- 代替ユニット: 勇士 ものまね師 / レンジャー 道化師 / 暗殺者 奴隷監督 / 影法師 娼婦
- 代替建造物: 宮殿 バルセラフの宮殿 / 練兵場 闘技場 / 土着の神殿 マンモンの巡業サーカス
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_BALSERAPHS
  - `ArtStyleType`: ARTSTYLE_BALSERAPHS
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 幻霊 iLimit=12
  - `MinGameProgressPercents`: 祝祭 iGameProgressPercent=25 / 製錬 iGameProgressPercent=40
  - `UnitDescriptions`: 斧兵 剣士 / 戦士 陽気者 / ファランクス スパルティアタイ / 狩人 軽業師 / カタパルト 投牛機 / ガレー船 ドラゴン船 / 鷹 オウム
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `InitialCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 理不尽志向

### Clan of Embers - 残り火一族

- 内部名: `CIVILIZATION_CLAN_OF_EMBERS`
- 初期テクノロジー: 探検 / 狩猟
- 指導者: ヨナス・エンダイン / シェルバ / 追放者ハウゲン / アザン / ジー / ヘンク
- 代替ユニット: 斥候 ゴブリン / 術使い まじない医 / 戦車兵 狼の戦車兵 / 騎乗兵 狼の騎乗兵 / 狩人 リザードマン / 勇士 オーガ / 弓騎兵 / 火縄銃兵 / 不死者 オーガの親分 / 騎士 / ファランクス 石肌のオーガ / 大砲 / カタパルト 巨大コブラ
- 代替建造物: 錬金術ラボ / 図書館 / 魔術師ギルド / 宮殿 残り火一族の宮殿 / 厩舎 / 裁判所 生贄の祭壇 / 土着の神殿 バアルの篝火
- 種族: オーク
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_CLAN_OF_EMBERS
  - `ArtStyleType`: ARTSTYLE_CLAN_OF_EMBERS
  - `bPlayable`: 1
  - `UnitClassRaces`: 狂戦士 オーク / 騎乗兵 ゴブリン / 戦車兵 ゴブリン / 狩人 リザードマン / レンジャー リザードマン / 暗殺者 リザードマン / 魔獣使い リザードマン / 影法師 リザードマン / ドルイド僧 リザードマン
  - `NationalUnitClassLimits`: TXT_KEY_UNIT_HIGH_PRIEST_OF_THE_OVERLORDS iLimit=12 / TXT_KEY_UNIT_HIGH_PRIEST_OF_THE_VEIL iLimit=12 / 幻霊 iLimit=12
  - `MinGameProgressPercents`: 青銅器 iGameProgressPercent=15 / 石工 iGameProgressPercent=15 / 法律 iGameProgressPercent=20 / 追跡術 iGameProgressPercent=25 / 騎乗 iGameProgressPercent=25 / 軍事行動 iGameProgressPercent=25 / 製錬 iGameProgressPercent=40
  - `UnitDescriptions`: 鷹 渡り鴉 / 狩人 リザードマン / 魔術師 祈祷師 / 戦士 オーク
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ImprovementTerrains`: 湿地
  - `ImprovementFeatures`: 密林
  - `TerrainYieldChanges`: 湿地 +1[食料]
  - `FeatureYieldChanges`: 密林 +1[食料]
  - `InitialCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### Svartalfar - スヴァルトアールヴ

- 内部名: `CIVILIZATION_SVARTALFAR`
- 初期テクノロジー: 探検 / 狩猟
- 指導者: ファエリル・ヴィコーニア / 死霊の主リヴァンナ / ヴォランナ / マテウス / ハセイム / ウティルソ
- 代替ユニット: レンジャー ダークストーカー / 魔術師 幻術師 / 弓騎兵 ニュクスの眷属 / 戦車兵 / カタパルト / 火縄銃兵 / 狂戦士 / 大砲
- 代替建造物: 錬金術ラボ / 宮殿 スヴァルトアールヴの宮殿 / 攻城兵器工廠 / 土着の神殿 エススの隠れ家 / 機械工場 / プラント
- 種族: エルフ
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_SVARTALFAR
  - `ArtStyleType`: ARTSTYLE_SVARTALFAR
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 狙撃手 iLimit=12
  - `MinGameProgressPercents`: 詐欺 iGameProgressPercent=30 / 毒物 iGameProgressPercent=35 / 複合弓 iGameProgressPercent=40 / 鐙 iGameProgressPercent=45
  - `ManaWeightModifiers`: 炎のノードを展開 iModifier=70
  - `UnitDescriptions`: 斧兵 剣士 / 勇士 致命の刃 / ファランクス スパルティアタイ / 鷹 渡り鴉
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ImprovementYieldChanges`: 狩猟場 +1[ハンマー] / 大狩猟場 +1[ハンマー] / 炭焼き小屋 +1[商業]
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 凶刃
  - `MaintainFeatures`: 森林 / 古代樹林 / 若き森林

### Calabim - カラビム

- 内部名: `CIVILIZATION_CALABIM`
- 初期テクノロジー: 探検 / 農業
- 指導者: アレクシス / フラウロス / デキウス / 皆殺しのマホン / ネルガル / エレナ / エリヤ・アルノー / 緋のエイリメール
- 代替ユニット: 戦士 血のしもべ / 斧兵 モロイ / 勇士 ヴァンパイア / 火縄銃兵 / 狂戦士 ブルーハ / 不死者 ヴァンパイアロード / 大砲
- 代替建造物: 錬金術ラボ / 裁判所 領主邸 / 長老会議 / 宮殿 カラビムの宮殿 / 土着の神殿 屠殺穴
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_CALABIM
  - `ArtStyleType`: ARTSTYLE_CALABIM
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 近衛騎兵 iLimit=12
  - `MinGameProgressPercents`: 法律 iGameProgressPercent=15 / 暦 iGameProgressPercent=20 / 数学 iGameProgressPercent=35 / 封建制 iGameProgressPercent=35 / 狂信 iGameProgressPercent=45
  - `StackManaWeightModifiers`: 死のノードを展開 iModifier=-30
  - `UnitDescriptions`: ファランクス スパルティアタイ / 鷹 渡り鴉
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### Sheaim - シェアイム

- 内部名: `CIVILIZATION_SHEAIM`
- 初期テクノロジー: 道具の作成 / 原初の祈り
- 指導者: テブリン・アルバンディ / オズ=ガベラ / 半妖のアヴェラクス / ゴセア / マルキャヴィーク / エロンカル卿
- 代替ユニット: 斧兵 火葬のゾンビ / 勇士 / 大魔道 夢喰い / 狂戦士 / 不死者 / ファランクス / 勇士 憤怒の亡者
- 代替建造物: 宮殿 シェアイムの宮殿 / 練兵場 / 鍛冶屋 影石加工場 / 厩舎 夢魔の厩舎 / 土着の神殿 ケリドウェンの観測所 / 錬金術ラボ 屍霊術研究所
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_SHEAIM
  - `ArtStyleType`: ARTSTYLE_SHEAIM
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: リッチ iLimit=8
  - `MinGameProgressPercents`: エーテルの知識 iGameProgressPercent=15 / 青銅器 iGameProgressPercent=20 / 魂の堕落 iGameProgressPercent=35 / 魔術 iGameProgressPercent=50 / 意志の力 iGameProgressPercent=65
  - `StackManaWeightModifiers`: 死のノードを展開 iModifier=-10
  - `UnitDescriptions`: 鷹 渡り鴉
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 呪刻

### Infernal - 地獄の軍勢

- 内部名: `CIVILIZATION_INFERNAL`
- 初期テクノロジー: 道具の作成
- 指導者: ハイボレム / ジュデッカ / サロス公爵 / オウザ / メレシン / 救世主スタティウス / 嘆きの女王レテ
- 代替ユニット: 術使い インプ / 狩人 地獄の番犬 / 火縄銃兵 / 狂戦士 バロール / 騎士 死の騎士 / カタパルト 業火の精霊 / 勇士 拷問士
- 代替建造物: 水道橋 / 穀倉 / 薬草師 / 診療所 / 宮殿 地獄の軍勢の宮殿 / 公衆浴場 / 燻製場 / 土着の神殿 アガレスの門 / 厩舎 夢魔の厩舎 / 錬金術ラボ 屍霊術研究所
- 種族: 魔族
- 説明（ゲーム内ヘルプ）: 邪悪なユニットが死亡するとマネス を得る / [SPACE][SPACE]都市は特定の初期建造物と蒼褪めた ヴェールを得る / [SPACE][SPACE]都市は地獄の侵蝕を広める
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_INFERNAL
  - `ArtStyleType`: ARTSTYLE_INFERNAL
  - `NationalUnitClassLimits`: 幻霊 iLimit=12 / アガレスの魔獣 iLimit=12
  - `MinGameProgressPercents`: 宗教法 iGameProgressPercent=35 / ギルド iGameProgressPercent=45 / 悪意の企み iGameProgressPercent=55 / エーテル移動 iGameProgressPercent=60
  - `UnitDescriptions`: 斧兵 灰運び / 勇士 蝿王の眷属 / ファランクス スパルティアタイ / 不死者 悪魔貴族 / 暗殺者 処刑人 / レンジャー 狩り立てる悪魔 / 騎乗兵 墓生まれ / 鷹 渡り鴉
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `FreeBuildingClassesForAllCities`: 長老会議 / 市場 / 練兵場 / 黒曜石の門 / 鍛冶屋 / 魔術師ギルド / 悪魔の市民
  - `ImprovementFeatures`: 捩れた森林
  - `TerrainYieldChanges`: 死滅の大地 +1[ハンマー] / 灼熱の砂地 +1[ハンマー]
  - `FeatureYieldChanges`: 黒の氾濫原 +2[商業] / 悪霊の地 +1[食料], +1[ハンマー], +1[商業]
  - `InitialCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 休耕志向

### Illians - イリアン

- 内部名: `CIVILIZATION_ILLIANS`
- 初期テクノロジー: 探検 / 原初の祈り
- 指導者: オーリック・ウルヴィン / 静かなるブリーデン / デュマンニオス / リウロス / アナガンティオス / レイトロール
- 代替ユニット: 弓兵 投槍兵
- 代替建造物: 土着の神殿 御手の神殿 / 宮殿 イリアンの宮殿 / 無神論者
- 種族: 寒冷種
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_ILLIANS
  - `ArtStyleType`: ARTSTYLE_ILLIANS
  - `bPlayable`: 1
  - `MinGameProgressPercents`: 哲学 iGameProgressPercent=20 / 聖職 iGameProgressPercent=35 / 鉄器 iGameProgressPercent=45 / 全知 iGameProgressPercent=75
  - `UnitDescriptions`: 勇士 冬の訪れ / ファランクス スパルティアタイ / 鷹 渡り鴉
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ImprovementTerrains`: 凍土 / 氷原
  - `RiverYieldChanges`: 氷原 +1[商業]
  - `TerrainYieldChanges`: 氷原 +2[食料]
  - `FeatureYieldChanges`: 猛吹雪 +1[商業] / 水晶原 +1[食料], +1[商業]
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### Niraikanai - ニライカナイ

- 内部名: `CIVILIZATION_NIRAIKANAI`
- 初期テクノロジー: 探検 / 狩猟 / 獣道の発見
- 指導者: M.A. / ティナ / リーザ / センダック / 竜殺しのテリー / リーケッジ・アロー
- 代替ユニット: 斥候 楽園の森林狼 / 狩人 フレキ / 暗殺者 マーナガルム / 影法師 フェンリル / 戦士 楽園の熊兵 / 斧兵 アルカス / 勇士 カリスト / 狂戦士 ベルセルク / 不死者 ルフ / 弓兵 ヴァナラ / 長弓兵 ハヌマーン / 弩兵 ヴァーユ / 騎乗兵 グリフォン飛行隊 / 弓騎兵 オピニンクス / 騎士 ガルダ / 戦車兵 グリフォン連隊 / 近衛騎兵 グリフォン騎士隊 / 術使い ペガサス / 魔術師 ユニコーン / 大魔道 バイコーン / 火縄銃兵 / カタパルト
- 代替建造物: 宮殿 ニライカナイの宮殿 / 巡業サーカス 太陽の曲芸団 / 土着の神殿 神明神社 / 図書館 目の院 / 錬金術ラボ 鼻の院 / 鍛冶屋 手の院 / 民族叙事詩 耳の院 / 英雄叙事詩 口の院 / 攻城兵器工廠 / 練兵場 / 厩舎 / 弓術射撃場 / 魔術師ギルド / 機械工場 / プラント
- 説明（ゲーム内ヘルプ）: 捕縛した動物を有効活用できる
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_NIRAIKANAI
  - `ArtStyleType`: ARTSTYLE_ASIAN
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: TXT_KEY_UNIT_HIGH_PRIEST_OF_THE_ORDER iLimit=12 / 至天の光輝者 iLimit=12 / 緑葉の司祭長 iLimit=12
  - `MinGameProgressPercents`: 追跡術 iGameProgressPercent=10 / 祝祭 iGameProgressPercent=20 / 動物の馴致 iGameProgressPercent=30 / 野生の触れ合い iGameProgressPercent=45 / 自然との共生 iGameProgressPercent=60 / 神学 iGameProgressPercent=70
  - `ManaWeightModifiers`: 死のノードを展開 iModifier=-70 / 不可逆のノードを展開 iModifier=-70
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `FeatureYieldChanges`: 森林 +1[食料], +1[商業] / 古代樹林 +1[食料], +1[商業]
  - `ImprovementYieldChanges`: ユグドラシルの樹 +3[食料] / 巨大樹の苗 +2[食料] / 巨大樹 +5[食料], +1[商業]
  - `InitialCivics`: 専制政治 / 平和主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 平和主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 馴致

### Dark - 常闇ノ国

- 内部名: `CIVILIZATION_DARK`
- 初期テクノロジー: 道具の作成 / 原初の祈り
- 指導者: 常闇ノ魔女 / 教授 / シヴァの化身 / 猛将シュトゥルム / 偽善の扇動者 / 直観の王君
- 代替ユニット: 術使い 首狩りの術師 / 魔術師 首狩りの魔術師 / 大魔道 首狩りの大魔術師 / 聖騎士 常闇の騎士 / 斧兵 暗き剣士 / 勇士 幽々たる猛きもの / 狩人 地獄の番犬 / 狂戦士 バロール / 騎士 死の騎士 / 火縄銃兵 / 幻霊 / カタパルト
- 代替建造物: 宮殿 常闇の宮殿 / 土着の神殿 炎獄の祭壇 / 鍛冶屋 影石加工場 / 厩舎 夢魔の厩舎 / 錬金術ラボ 屍霊術研究所 / 薬草師 / 水道橋 / 診療所 / 攻城兵器工廠 / 魔術師ギルド
- 種族: 魔族
- 説明（ゲーム内ヘルプ）: アルマゲドンカウンタ50到達により 地獄の浸食が発生
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_DARK
  - `ArtStyleType`: ARTSTYLE_INFERNAL
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: アガレスの魔獣 iLimit=12
  - `MinGameProgressPercents`: エーテルの知識 iGameProgressPercent=15 / 青銅器 iGameProgressPercent=20 / 邪悪への道 iGameProgressPercent=25 / 魂の堕落 iGameProgressPercent=30 / 地獄の契約 iGameProgressPercent=35 / 聖職 iGameProgressPercent=40 / 製錬 iGameProgressPercent=45 / 毒物 iGameProgressPercent=55 / 悪意の企み iGameProgressPercent=60
  - `ManaWeightModifiers`: 死のノードを展開 iModifier=100 / 不可逆のノードを展開 iModifier=50
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `FreeBuildingClassesForAllCities`: 空亡の宝珠
  - `ImprovementFeatures`: 捩れた森林
  - `TerrainYieldChanges`: 灼熱の砂地 +1[ハンマー], +1[商業]
  - `FeatureYieldChanges`: 延焼 +1[商業] / 黒の氾濫原 +1[食料], +1[商業] / 捩れた森林 +1[ハンマー]
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `MaintainFeatures`: 延焼

### Ys - イース

- 内部名: `CIVILIZATION_YS`
- 初期テクノロジー: 探検 / 漁業
- 指導者: レア / フィーナ / フローレット / ヤール / リーゼ / 白き魔女ゲルド / オリビエ
- 代替ユニット: 斧兵 術歩兵 / 勇士 重魔装兵 / 騎乗兵 術騎兵 / 弓騎兵 魔導騎兵 / 弓兵 術弓兵 / 長弓兵 魔弓隊 / 近衛騎兵 神殿騎士 / 戦車兵 / 火縄銃兵 / カタパルト / 大砲
- 代替建造物: 宮殿 イースの宮殿 / 記念碑 ナピシュテムの匣 / 図書館 修道院 / 裁判所 枢密院 / 土着の神殿 道祖神 / 攻城兵器工廠
- 説明（ゲーム内ヘルプ）: 高速詠唱を持つ固有ユニットは 呪文昇進をランダムに習得
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_YS
  - `ArtStyleType`: ARTSTYLE_KURIOTATES
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 聖騎士 iLimit=12
  - `MinGameProgressPercents`: エーテルの知識 iGameProgressPercent=25 / 聖職 iGameProgressPercent=40
  - `ManaWeightModifiers`: 炎のノードを展開 iModifier=50 / 太陽のノードを展開 iModifier=50
  - `UnitDescriptions`: ファランクス スパルティアタイ
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `TerrainYieldChanges`: 近海 +1[商業] / 外洋 +1[商業]
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### Echigo - エチゴ

- 内部名: `CIVILIZATION_ECHIGO`
- 初期テクノロジー: 農業 / 漁業
- 指導者: 上杉謙信 / 直江山城守 / 直江景綱 / 柿崎景家 / 宇佐美駿河守定満 / 甘粕景持
- 代替ユニット: 影法師 忍者 / 戦士 足軽 / 斧兵 剣客 / 勇士 侍 / 不死者 夜叉 / 騎士 母衣武者 / 術使い 巫女 / 魔術師 僧兵 / 大魔道 僧兵長 / ドルイド僧 花魁 / 私掠船 倭寇 / 魔獣使い / 狂戦士 / ファランクス / カタパルト / 戦車兵 / 聖騎士 / 幻霊
- 代替建造物: 宮殿 エチゴの宮殿 / 土着の神殿 毘沙門天廟 / 練兵場 道場 / 英雄叙事詩 上杉謙信の玉座 / 魔術師ギルド / 錬金術ラボ / 無神論者
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_ECHIGO
  - `ArtStyleType`: ARTSTYLE_ASIAN
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 騎士 iLimit=12
  - `MinGameProgressPercents`: 青銅器 iGameProgressPercent=15 / 軍事行動 iGameProgressPercent=30 / 封建制 iGameProgressPercent=40 / 軍事戦略 iGameProgressPercent=40 / 税制 iGameProgressPercent=45 / 高潔の証 iGameProgressPercent=60
  - `UnitDescriptions`: 近衛騎兵 旗本 / 狩人 下忍 / レンジャー 般若 / 暗殺者 くのいち / ガレー船 安宅船
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ExtraPrereqOrTechs`: 蒸気機関 工学
  - `FeatureYieldChanges`: 海藻 +1[食料], +1[商業]
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 士魂

### Droaum - ドロアウム

- 内部名: `CIVILIZATION_DROAUM`
- 初期テクノロジー: 農業 / 原初の祈り
- 指導者: ソーマ・カトラ / ソーマ・テラザ / ロバート・ソーン / リチャード・ソーン / ダースク / シェーララク
- 代替ユニット: 勇士 救世主の使い / 狂戦士 サイクロプス / 火縄銃兵 / 大砲
- 代替建造物: 宮殿 ドロアウムの宮殿 / 土着の神殿 救世の神殿 / 鍛冶屋 影石加工場 / 厩舎 夢魔の厩舎 / 錬金術ラボ 屍霊術研究所 / NONE
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_RED
  - `ArtStyleType`: ARTSTYLE_SHEAIM
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 幻霊 iLimit=12
  - `MinGameProgressPercents`: エーテルの知識 iGameProgressPercent=20 / 邪悪への道 iGameProgressPercent=20 / 屍霊術 iGameProgressPercent=25 / 詐欺 iGameProgressPercent=30 / 聖職 iGameProgressPercent=40 / 鉄器 iGameProgressPercent=45
  - `UnitDescriptions`: ファランクス スパルティアタイ / 鷹 渡り鴉
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `FeatureYieldChanges`: 悪霊の地 +1[食料], +1[ハンマー], +1[商業]
  - `InitialCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### Despiel - デスピエル

- 内部名: `CIVILIZATION_DESPIEL`
- 初期テクノロジー: 探検 / 原初の祈り
- 指導者: イェノイア・ゴルゴダ / ラディバール・ド・サブレ / ヒュドール・アルギュロス / ゴリィー・ザ・ゴッドハンド / アルシン・ビスミュス / プゼヴ・ダル・ギュロス
- 代替ユニット: 術使い 骨遊び / 大魔道 黒魔導師 / 斧兵 這い出し者 / 勇士 暗黒兵 / 狂戦士 暗黒騎士 / 騎乗兵 嘲笑う者 / 弓騎兵 心を失くす者 / 騎士 名前を忘れし者 / 弩兵 腐れ矢の射手 / 狙撃手 蟇目矢の射手 / 火縄銃兵 / カタパルト / 大砲
- 代替建造物: 宮殿 デスピエルの宮殿 / 鍛冶屋 換魂所 / 図書館 汚染法書院 / 錬金術ラボ 霊魂培養所 / 裁判所 真理の館 / 土着の神殿 奉魔の祭壇 / 市場 奇妙な肉屋 / 地下牢 実験場 / 攻城兵器工廠
- 種族: 壊人
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_DESPIEL
  - `ArtStyleType`: ARTSTYLE_SCIONS
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 不死者 iLimit=12
  - `MinGameProgressPercents`: エーテルの知識 iGameProgressPercent=20 / 製錬 iGameProgressPercent=40 / 秘術の伝承知識 iGameProgressPercent=50 / 意志の力 iGameProgressPercent=55 / 神々の本質 iGameProgressPercent=70
  - `UnitDescriptions`: ファランクス 殺人狂 / 弓兵 凶弓手 / 長弓兵 人間狩り / 狩人 腐肉食い / 魔術師 ネクロフィリア / 鷹 渡り鴉
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `FreeBuildingClassesForAllCities`: デスピエルの市民
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 外法

### Lineage - リネージ

- 内部名: `CIVILIZATION_LINEAGE`
- 初期テクノロジー: 道具の作成 / 探検
- 指導者: ボールドウィン・ド・マリス / ノイシュタット・レオード / ジョリスターペン / カース / ディアナ / 山本沈愚
- 代替ユニット: 魔獣使い 盗賊 / 戦士 レギオン / 斧兵 デクリオン / 勇士 センチュリオン / ファランクス ハルムベルテ / 狂戦士 装甲兵 / 火縄銃兵 重弩兵 / 弩兵 奇環弩兵 / 狙撃手 アペイロン / 弓騎兵 ハロース / 騎士 オクスタン / 術使い 除霊師 / カタパルト 重バリスタ / 大砲 ドーラ / 不死者 / 戦車兵 / 魔術師 / 大魔道
- 代替建造物: 宮殿 リネージの宮殿 / 土着の神殿 神々の神殿 / 水道橋 帝国水道橋 / 防壁 城塞防壁 / 裁判所 総督府 / 厩舎 帝国厩舎 / 攻城兵器工廠 バリスタ工房 / 無神論者
- 説明（ゲーム内ヘルプ）: 偉人誕生時に33%の確率で偉大な指揮官 が追加される
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_LINEAGE
  - `ArtStyleType`: ARTSTYLE_BANNOR
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: ファランクス iLimit=12
  - `MinGameProgressPercents`: 法律 iGameProgressPercent=20 / 建設 iGameProgressPercent=30 / 鐙 iGameProgressPercent=35 / 軍事戦略 iGameProgressPercent=40 / 工学 iGameProgressPercent=50 / 機械 iGameProgressPercent=60 / ミスリルの武具 iGameProgressPercent=70
  - `UnitDescriptions`: 聖騎士 聖北の執行官
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ExtraPrereqAndTechs`: 爆薬 鉄器
  - `ExtraPrereqOrTechs`: 爆薬 工学 / 蒸気機関 工学
  - `InitialCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 異邦人

### Mazatl - マサトル

- 内部名: `CIVILIZATION_MAZATL`
- 初期テクノロジー: 狩猟 / 原初の祈り / 獣道の発見
- 指導者: ヒアンスローフ / クゥセット / アミンゼルフ / マルスト / サッカスローン / ラフィセルノ
- 代替ユニット: 労働者 リザードマン整形者 / 弓兵 投槍兵 / 長弓兵 吹管兵 / 弩兵 罠師 / 狙撃手 奇襲兵 / 火縄銃兵 / 騎乗兵 / 弓騎兵 / 騎士 / 戦象
- 代替建造物: 宮殿 マサトルの宮殿 / 土着の神殿 カルシェックの礼拝所 / 弓術射撃場 / 厩舎
- 種族: リザードマン
- 説明（ゲーム内ヘルプ）: 領内の森林が密林に徐々に変化 / [SPACE][SPACE]領内の密林が深い密林に徐々に変化 (要：聖職) / [SPACE][SPACE]領内の道路が獣道に徐々に変化
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_MAZATL
  - `ArtStyleType`: ARTSTYLE_LIZARD
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 奉竜の御子 iLimit=8
  - `MinGameProgressPercents`: 変成術 iGameProgressPercent=25 / 聖職 iGameProgressPercent=35 / 複合弓 iGameProgressPercent=45 / 精密射撃 iGameProgressPercent=55
  - `UnitDescriptions`: 斧兵 剣士 / 狩人 リザードマン / ファランクス スパルティアタイ
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ImprovementTerrains`: 湿地
  - `ImprovementFeatures`: 密林 / 深い密林
  - `TerrainYieldChanges`: 湿地 +1[食料], +1[商業]
  - `FeatureYieldChanges`: 密林 +1[食料], +1[商業]
  - `ImprovementYieldChanges`: 小屋 / 部落 +1[商業] / 村 +1[商業] / 町 +1[商業] / 自治区 +1[商業]
  - `InitialCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `MaintainFeatures`: 深い密林 / 密林 / 沼

### Cualli - クアリ

- 内部名: `CIVILIZATION_CUALLI`
- 初期テクノロジー: 道具の作成 / 狩猟 / 獣道の発見
- 指導者: コルセヴァン / ミファトル / グロヴァー / インベールフ / キスタオーリ / グルコァトル
- 代替ユニット: 労働者 リザードマン整形者 / 弓兵 投槍兵 / 長弓兵 吹管兵 / 暗殺者 アグルオンの尖兵 / 狩人 血の狩人 / レンジャー 虐殺者 / 魔獣使い 奴隷使い / 火縄銃兵 / 騎乗兵 / 弓騎兵 / 騎士 / 戦象
- 代替建造物: 宮殿 クアリの宮殿 / 土着の神殿 アグルオンの祭壇 / 錬金術ラボ / 裁判所 / 図書館 / 厩舎 / 劇場
- 種族: リザードマン
- 説明（ゲーム内ヘルプ）: 領内の森林が密林に徐々に変化 / [SPACE][SPACE]領内の密林が深い密林に徐々に変化 (要：聖職) / [SPACE][SPACE]領内の道路が獣道に徐々に変化
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_CUALLI
  - `ArtStyleType`: ARTSTYLE_LIZARD
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 影法師 iLimit=12
  - `MinGameProgressPercents`: 邪悪への道 iGameProgressPercent=25 / 毒物 iGameProgressPercent=35 / 聖職 iGameProgressPercent=35 / 詐欺 iGameProgressPercent=40 / 動物の馴致 iGameProgressPercent=45 / 複合弓 iGameProgressPercent=45 / ギルド iGameProgressPercent=50 / 悪意の企み iGameProgressPercent=60
  - `UnitDescriptions`: 斧兵 剣士 / ファランクス スパルティアタイ
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ImprovementTerrains`: 湿地
  - `ImprovementFeatures`: 密林 / 深い密林
  - `TerrainYieldChanges`: 湿地 +1[食料], +1[商業]
  - `FeatureYieldChanges`: 密林 +1[食料], +1[商業]
  - `ImprovementYieldChanges`: 鉱山 +1[商業] / 立坑鉱山 +1[商業]
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 奴隷志向
  - `MaintainFeatures`: 深い密林 / 密林 / 沼

### Altair - アルタイル

- 内部名: `CIVILIZATION_ALTAIR`
- 初期テクノロジー: 道具の作成 / 探検 / 獣道の発見
- 指導者: メタトロン / エル'ケブレス / 竜使いビュウ / 柱守ヤーヴェ / 有翼のアスタルテ / ゲヘナ
- 代替ユニット: 労働者 功労者 / 弓兵 投槍兵 / 長弓兵 毒針使い / 魔獣使い 竜使い / ドルイド僧 嵐に潜む者 / 弩兵 / 狙撃手 / 影法師 / カタパルト / 大砲 / 火縄銃兵 / 大魔道
- 代替建造物: 宮殿 アルタイルの宮殿 / 土着の神殿 要石 / 診療所 列石 / 弓術射撃場 / 巡業サーカス / 攻城兵器工廠 / 機械工場 / プラント / 無神論者
- 種族: 竜人
- 説明（ゲーム内ヘルプ）: 領内の地形が砂漠・湿地に変化 / [SPACE][SPACE]領内の道路が獣道に変化 / [SPACE][SPACE]-1: 氾濫原
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_ALTAIR
  - `ArtStyleType`: ARTSTYLE_CLAN_OF_EMBERS
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: ドルイド僧 iLimit=12
  - `MinGameProgressPercents`: 教育 iGameProgressPercent=10 / 地図 iGameProgressPercent=10 / 青銅器 iGameProgressPercent=15 / 四大元素 iGameProgressPercent=25 / 製錬 iGameProgressPercent=30 / 衛生設備 iGameProgressPercent=35 / 軍事戦略 iGameProgressPercent=40 / 鉄器 iGameProgressPercent=45 / 魔術 iGameProgressPercent=50 / 爆薬 iGameProgressPercent=55 / ミスリル器 iGameProgressPercent=60 / 医薬 iGameProgressPercent=65 / 自然との共生 iGameProgressPercent=70 / 神々の本質 iGameProgressPercent=70 / 意志の力 iGameProgressPercent=75 / 全知 iGameProgressPercent=75
  - `UnitDescriptions`: 斧兵 剣士 / ファランクス スパルティアタイ
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ExtraPrereqOrTechs`: 神学 自然との共生
  - `ImprovementTerrains`: 砂漠 / 湿地 / 凍土 / 氷原
  - `TerrainYieldChanges`: 砂漠 +1[食料] / 氷原 +1[食料]
  - `FeatureYieldChanges`: 氾濫原 / オアシス
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### Mechanos - メカノス

- 内部名: `CIVILIZATION_MECHANOS`
- 初期テクノロジー: 道具の作成 / 漁業
- 指導者: ヴェロッキオ / メイヤー / メタルヴォルフ / ライデン / アートマン / アマジーグ
- 代替ユニット: 勇士 機械化兵 / ファランクス 火炎放射兵 / 狂戦士 擲弾兵 / 長弓兵 拳銃兵 / 火縄銃兵 マスケット兵 / 弓騎兵 竜騎兵 / 暗殺者 魔女狩り / 術使い 精製術師 / ドルイド僧 テックプリースト / カタパルト トレビュシェット / 大砲 榴弾砲 / キャラベル船 飛行船 / 魔導艦 潜水艦 / マン・オー・ウォー 装甲艦 / 戦列の女王 ツェッペリン / 不死者 / 魔術師 / 大魔道 / 戦車兵 / 戦象
- 代替建造物: 土着の神殿 時計塔 / 鍛冶屋 製錬所 / プラント 発電所 / 宮殿 メカノスの宮殿 / マーキュリアンの門 / 錬金術ラボ / 魔術師ギルド / 黒曜石の門
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_MECHANOS
  - `ArtStyleType`: ARTSTYLE_MECHANOS
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: ドルイド僧 iLimit=12
  - `MinGameProgressPercents`: 蒸気機関 iGameProgressPercent=15 / 製錬 iGameProgressPercent=35 / 工学 iGameProgressPercent=45 / 鉄器 iGameProgressPercent=50 / 爆薬 iGameProgressPercent=55 / 天文学 iGameProgressPercent=60
  - `ManaWeightModifiers`: 精製装置を建設 iModifier=70
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ExtraPrereqAndTechs`: 爆薬 鉄器
  - `ExtraPrereqOrTechs`: 爆薬 工学 / 蒸気機関 エーテルの知識
  - `ImprovementYieldChanges`: 風車 +1[商業] / 水車 +1[商業]
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 整備士志向

### Scions of Patria - パトリアの後継者

- 内部名: `CIVILIZATION_SCIONS`
- 初期テクノロジー: 道具の作成 / ギフト
- 指導者: 上帝 / 守護者コリンナ / オフェリア / シーヴァン / ネロ / ティベリウス
- 代替ユニット: 開拓者 覚醒者 / 近衛騎兵 近衛兵 / 戦士 百卒長 / 弓兵 軽装歩兵 / 火縄銃兵 骨の大群 / 勇士 第二列歩兵 / 狩人 軽盾兵 / レンジャー 彷徨い人 / 暗殺者 パトリアの殉教者 / ドルイド僧 嫌われ者 / 魔術師 屍霊術師 / ガレアス船 五段櫂船 / 戦象 / 魔獣使い / 大砲
- 代替建造物: 宮殿 後継者の神殿 / 診療所 屍肉工房 / 劇場 契約の大広間 / 裁判所 荘厳なる鎮魂碑 / ビール醸造所 精魂所 / 図書館 カイロリンの聖廟 / 土着の神殿 ギフトの寺院 / 灯台 標のかがり火 / NONE
- 種族: 屍人
- 説明（ゲーム内ヘルプ）: 低確率で首都に再誕者 が出現
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_SCIONS
  - `ArtStyleType`: ARTSTYLE_SCIONS
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 近衛騎兵 iLimit=12
  - `MinGameProgressPercents`: 神秘主義 iGameProgressPercent=10 / エーテルの知識 iGameProgressPercent=15 / 法律 iGameProgressPercent=15 / 追跡術 iGameProgressPercent=15 / 祝祭 iGameProgressPercent=30 / 通貨 iGameProgressPercent=30 / 宗教法 iGameProgressPercent=40 / 工学 iGameProgressPercent=55
  - `ManaWeightModifiers`: 肉体のノードを展開 iModifier=70
  - `UnitDescriptions`: 斧兵 第一列歩兵 / ファランクス スパルティアタイ / 影法師 帝国暗殺者
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `FeatureYieldChanges`: 悪霊の地 +1[食料], +1[ハンマー], +1[商業]
  - `InitialCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 休耕志向
  - `MaintainFeatures`: 悪霊の地

### Nival - ニバル

- 内部名: `CIVILIZATION_NIVAL`
- 初期テクノロジー: 狩猟 / 漁業
- 指導者: エクロ / キタン / シェンガ / ネージュ / イヴェール / ジーヴル
- 代替ユニット: 労働者 雪男 / 勇士 氷の巨人 / ファランクス 雪の怪物 / 狂戦士 勇者の氷像 / 狙撃手 吹雪の化身 / 騎乗兵 狼の騎乗兵 / レンジャー 氷の牙 / 魔獣使い 氷の影 / 暗殺者 雪蜥蜴 / ドルイド僧 雪の賢者 / 影の騎士 氷の影の乗り手 / 斧兵 / 不死者 / 弩兵 / 火縄銃兵 / 弓騎兵 / 騎士 / 戦車兵 / カタパルト / 大砲
- 代替建造物: 宮殿 ニバルの宮殿 / 土着の神殿 雪洞 / 攻城兵器工廠 氷雪のアトリエ / 練兵場 / 厩舎 / 鍛冶屋 / 両替商 / 公衆浴場 / 機械工場 / プラント
- 種族: フロストリング
- 説明（ゲーム内ヘルプ）: 首都周辺の地形が氷原に変化 / [SPACE][SPACE]領内で寒冷化や猛吹雪が 発生しやすく消滅しづらい / [SPACE][SPACE]領内に進入したモッカを 味方に引き込む
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_NIVAL
  - `ArtStyleType`: ARTSTYLE_DOVIELLO
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 狙撃手 iLimit=12
  - `MinGameProgressPercents`: 祝祭 iGameProgressPercent=15 / 数学 iGameProgressPercent=25 / 動物の馴致 iGameProgressPercent=30 / 建設 iGameProgressPercent=30 / 演劇 iGameProgressPercent=35 / 毒物 iGameProgressPercent=40 / 工学 iGameProgressPercent=50 / ギルド iGameProgressPercent=60 / 動物の極意 iGameProgressPercent=65 / 機械 iGameProgressPercent=70
  - `UnitDescriptions`: 斥候 雪踏み / 狩人 氷霧の子 / 鷹 渡り鴉 / 狼の騎乗兵 フロストリング狼騎兵
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ImprovementTerrains`: 氷原
  - `RiverYieldChanges`: 氷原 +1[商業]
  - `TerrainYieldChanges`: 氷原 +2[食料]
  - `FeatureYieldChanges`: 猛吹雪 +1[商業] / 水晶原 +1[食料], +1[商業]
  - `ImprovementYieldChanges`: 雪だるま +1[食料], +1[商業] / 大きな雪だるま +1[食料], +3[商業] / 巨大な雪だるま +1[食料], +1[ハンマー], +4[商業]
  - `InitialCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `MaintainFeatures`: 猛吹雪

### Rarna - ラーナ

- 内部名: `CIVILIZATION_RARNA`
- 初期テクノロジー: 探検 / 原初の祈り
- 指導者: ラファエル / ジョルジュ・ロングヒル / マルガレーテ / オズワルド / ラスロー / イグナティウス
- 代替ユニット: 狩人 槍兵 / レンジャー 長槍兵 / ファランクス 鉾槍兵 / 不死者 魂狩り / 弓騎兵 斧騎兵 / 騎士 白の騎士 / 近衛騎兵 神殿騎士 / 火縄銃兵
- 代替建造物: 宮殿 ラーナの宮殿 / 土着の神殿 継承の神殿 / 黒曜石の門 要の祭壇
- 説明（ゲーム内ヘルプ）: 死亡した生物ユニットが転生する / [SPACE][SPACE]地獄の浸食が発生しない / [SPACE][SPACE]アルマゲドンカウンタによる一部の 悪影響を受けない
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_RARNA
  - `ArtStyleType`: ARTSTYLE_MERCURIANS
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: ダイヤモンドの騎士 iLimit=8
  - `MinGameProgressPercents`: 哲学 iGameProgressPercent=20 / 軍事行動 iGameProgressPercent=30 / 狂信 iGameProgressPercent=40 / 封建制 iGameProgressPercent=45 / 鉄器 iGameProgressPercent=50 / 秘術の伝承知識 iGameProgressPercent=55 / 神々の本質 iGameProgressPercent=70
  - `UnitDescriptions`: ファランクス スパルティアタイ
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `InitialCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### Tiger - ティーグル

- 内部名: `CIVILIZATION_TIGER`
- 初期テクノロジー: 狩猟 / 農業
- 指導者: フォックス / ハウンド / ブランフォード / コヨーテ / シュタインドルフ / スマイリー
- 代替ユニット: 傭兵 ティーグル傭兵団 / ドルイド僧 / 聖騎士 / 幻霊 / TXT_KEY_UNIT_HIGH_PRIEST_OF_KILMORPH / 緑葉の司祭長 / 至天の光輝者 / TXT_KEY_UNIT_HIGH_PRIEST_OF_THE_ORDER / TXT_KEY_UNIT_HIGH_PRIEST_OF_THE_OVERLORDS / TXT_KEY_UNIT_HIGH_PRIEST_OF_THE_VEIL
- 代替建造物: 宮殿 ティーグルの宮殿 / 土着の神殿 勝利の標 / 錬金術ラボ
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_TIGER
  - `ArtStyleType`: ARTSTYLE_GRIGORI
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 傭兵 iLimit=24
  - `MinGameProgressPercents`: 通貨 iGameProgressPercent=20 / 封建制 iGameProgressPercent=40 / 名誉 iGameProgressPercent=45 / ギルド iGameProgressPercent=50 / 医薬 iGameProgressPercent=55
  - `UnitDescriptions`: ファランクス スパルティアタイ
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 掠奪

### Xoth - ゾス

- 内部名: `CIVILIZATION_XOTH`
- 初期テクノロジー: 海洋志向 / 漁業
- 指導者: ハイドラ
- 代替ユニット: 勇士 イタカ / 狂戦士 バイアクヘー / 長弓兵 ショゴス / 弓騎兵 ティンダロスの猟犬 / マン・オー・ウォー 古のもの / 斥候 / 斧兵 / ファランクス / 火縄銃兵 / 騎乗兵 / 騎士 / 戦車兵 / カタパルト / 大砲
- 代替建造物: 宮殿 旧支配者の封印 / 土着の神殿 海底神殿 / 愉悦の塔
- 説明（ゲーム内ヘルプ）: 都市は特定の初期建造物と深海の 旧支配者を得る / [SPACE][SPACE]正気度により様々な影響を受ける
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_XOTH
  - `ArtStyleType`: ARTSTYLE_LANUN
  - `NationalUnitClassLimits`: TXT_KEY_UNIT_HIGH_PRIEST_OF_THE_OVERLORDS iLimit=12
  - `MinGameProgressPercents`: 光学 iGameProgressPercent=25 / 複合弓 iGameProgressPercent=35 / 鐙 iGameProgressPercent=40 / 海図 iGameProgressPercent=40 / 天文学 iGameProgressPercent=45 / 神学 iGameProgressPercent=60
  - `UnitDescriptions`: 鷹 渡り鴉
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `FreeBuildingClassesForAllCities`: 深海の神殿 / 精神病院 / 港 / 灯台 / 長老会議 / 黒曜石の門 / 魔術師ギルド
  - `ImprovementTerrains`: 凍土
  - `TerrainYieldChanges`: 近海 +1[食料] / 外洋 +1[ハンマー]
  - `InitialCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 水陸両用

### Baldralfar - バルドルアールヴ

- 内部名: `CIVILIZATION_BALDRALFAR`
- 初期テクノロジー: 探検 / 原初の祈り
- 指導者: イングウェ・ヴァンヤール / グレブニール・ワードナ / アルドウェン・エルゲバーン / ルーシエン・ティヌーヴィエル / フィンウェ・ノルドール / エルウェ・エル・シンゴル
- 代替ユニット: レンジャー ダークストーカー / 勇士 王の使者 / 長弓兵 フェルム / 弩兵 疾風隊 / 弓騎兵 監視者 / 魔術師 幻術師 / 狂戦士 / 火縄銃兵 / 戦車兵 / カタパルト / 大砲
- 代替建造物: 宮殿 バルドルアールヴの宮殿 / 英雄叙事詩 マンドスの館 / 土着の神殿 再生の祭壇 / 錬金術ラボ / 攻城兵器工廠 / 機械工場 / プラント
- 種族: エルフ
- 説明（ゲーム内ヘルプ）: ユニットは生まれつき変異しており 時間経過で更に進行 / [SPACE][SPACE]領内の森林・古代樹林では、 弱体化・病気が与えられることがある
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_BALDRALFAR
  - `ArtStyleType`: ARTSTYLE_LJOSALFAR
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 大魔道 iLimit=8
  - `MinGameProgressPercents`: エーテルの知識 iGameProgressPercent=25 / 複合弓 iGameProgressPercent=35 / 軍事戦略 iGameProgressPercent=40 / 動物の馴致 iGameProgressPercent=45 / 魔術 iGameProgressPercent=45 / 野生の触れ合い iGameProgressPercent=50
  - `ManaWeightModifiers`: 炎のノードを展開 iModifier=70
  - `UnitDescriptions`: 斧兵 剣士 / 勇士 スケルスの監視者
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ImprovementFeatures`: 捩れた森林
  - `FeatureYieldChanges`: 捩れた森林 +1[ハンマー], +1[商業]
  - `ImprovementYieldChanges`: 狩猟場 +1[食料] / 大狩猟場 +1[食料] / 炭焼き小屋 +1[商業]
  - `InitialCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 瘴烟
  - `MaintainFeatures`: 森林 / 古代樹林 / 若き森林 / 捩れた森林

### Nougbii - ノービアイ

- 内部名: `CIVILIZATION_NOUGBII`
- 初期テクノロジー: 道具の作成 / 農業
- 指導者: アデライズ・モーガティロド / ユスデニィ・アターカス / エピーティア・メート / エニプサー・エユティツニ / エニドゥラーシ・メーク / ティヴァーヴカ・スルーアト
- 代替ユニット: 労働者 泥のゴーレム / 影法師 ドワーフ影法師 / 魔獣使い マイコニド / 勇士 戦車のゴーレム / ファランクス 幻想機甲部隊 / 狂戦士 歩行戦車 / 火縄銃兵 クローン / 弩兵 大蜘蛛のゴーレム / 騎乗兵 猪の騎乗兵 / 騎士 ドワーフホーンガード / カタパルト トレビュシェット / 大砲 ドワーフの大砲 / 術使い 精製術師 / ドルイド僧 テックプリースト / レンジャー / 長弓兵 / 狙撃手 / 弓騎兵
- 代替建造物: 宮殿 ノービアイの宮殿 / 土着の神殿 シヴレント工房 / 鍛冶屋 製錬所 / プラント 発電所 / 穀倉 複製の竈 / 劇場 螺旋の塔 / 魔術師ギルド
- 種族: ドワーフ
- 説明（ゲーム内ヘルプ）: 都市は領内で死亡した生物を 食糧に変換する
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_NOUGBII
  - `ArtStyleType`: ARTSTYLE_KHAZAD
  - `bPlayable`: 1
  - `MinGameProgressPercents`: 暦 iGameProgressPercent=15 / 蒸気機関 iGameProgressPercent=15 / 哲学 iGameProgressPercent=20 / 建設 iGameProgressPercent=30 / 演劇 iGameProgressPercent=35 / 製錬 iGameProgressPercent=40 / 機械 iGameProgressPercent=50
  - `ManaWeightModifiers`: 精製装置を建設 iModifier=70
  - `UnitDescriptions`: 弓兵 ドワーフ投石兵 / 勇士 ドワーフ鉄鎚兵 / ファランクス スパルティアタイ
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `ExtraPrereqOrTechs`: 蒸気機関 エーテルの知識
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 整備士志向

### Aristrakh - アリストラク

- 内部名: `CIVILIZATION_ARISTRAKH`
- 初期テクノロジー: 道具の作成 / 探検
- 指導者: ニケフォロス / ナージェシュ / ナスルエル / ノーマメイア / ニュート / ノザリー / ネスグオシム / ネクロゾール
- 代替ユニット: 斥候 生ける死体 / 狩人 屍奴 / レンジャー 食屍鬼 / 魔獣使い 火竜の屍骸 / 戦士 土塚の戦士 / 斧兵 青褪めた衛士 / 勇士 弔鐘の地下守 / 狂戦士 ブルーハ / 不死者 ヴァンパイアロード / ファランクス ヴァンパイアカウント / 弓兵 土塚の弓兵 / 長弓兵 青褪めた獄吏 / 弩兵 弔鐘の墓警 / 狙撃手 求血者 / 騎乗兵 土塚の騎乗兵 / 戦車兵 弔鐘の墓騎兵 / 弓騎兵 青褪めた騎手 / 騎士 ヴァンパイアデューク / 術使い 土塚の術者 / 魔術師 青褪めた保骸士 / 大魔道 弔鐘の呪織 / 暗殺者 / 影法師 / 火縄銃兵 / 戦象 / 近衛騎兵 / 大砲 / 鷹
- 代替建造物: 宮殿 アリストラクの宮殿 / 水道橋 悪霊小路 / ビール醸造所 汚された土壌 / 巡業サーカス 屍骸の檻 / 穀倉 埋葬塚 / 鎮守の杜 寄る辺なき納骨堂 / 薬草師 死者の間 / 診療所 霊廟 / 灯台 霊安倉 / 市場 悪霊の塔 / 公衆浴場 不浄なる標 / 燻製場 暴かれた墓所 / 徴税所 魂の牢獄 / 劇場 墳墓 / 狩猟小屋
- 説明（ゲーム内ヘルプ）: 定められた上限に達するまで 都市の人口が徐々に増加
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_ARISTRAKH
  - `ArtStyleType`: ARTSTYLE_INFERNAL
  - `bPlayable`: 1
  - `MinGameProgressPercents`: エーテルの知識 iGameProgressPercent=20 / 屍霊術 iGameProgressPercent=25 / 演劇 iGameProgressPercent=35 / 魔術 iGameProgressPercent=40 / 製錬 iGameProgressPercent=40 / 軍事戦略 iGameProgressPercent=45 / 動物の極意 iGameProgressPercent=65
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `FeatureYieldChanges`: 悪霊の地 +1[食料], +1[ハンマー], +1[商業]
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 休耕志向
  - `MaintainFeatures`: 悪霊の地

### Megisus - メギスス

- 内部名: `CIVILIZATION_MEGISUS`
- 初期テクノロジー: 探検 / 原初の祈り
- 指導者: ヘルメスⅡ世 / ロージェレン・ベコニル / アルベラット・マグヌイリオン / ヘルメスⅢ世 / パラステンディ・オーレオルス / ゲベラー・アレムビシル
- 代替ユニット: 暗殺者 詠唱者 / 斧兵 生きている鎧 / 狂戦士 人造人間
- 代替建造物: 宮殿 メギススの宮殿 / 土着の神殿 ナントスエルタの神殿
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_MEGISUS
  - `ArtStyleType`: ARTSTYLE_AMURITES
  - `bPlayable`: 1
  - `NationalUnitClassLimits`: 大魔道 iLimit=8
  - `MinGameProgressPercents`: 叡智への道 iGameProgressPercent=20 / 複合弓 iGameProgressPercent=40 / 魔術 iGameProgressPercent=40 / 錬金術 iGameProgressPercent=50 / 秘術の伝承知識 iGameProgressPercent=55
  - `ManaWeightModifiers`: 肉体のノードを展開 iModifier=70
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `CivTrait`: 血統

### Letum Frigus - レートゥム・フリグス

- 内部名: `CIVILIZATION_LETUM_FRIGUS`
- 指導者: 冬の神ムルカルン / 天帝カイロリン
- 代替建造物: 宮殿 レートゥム・フリグスの宮殿
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_LETUM_FRIGUS
  - `ArtStyleType`: ARTSTYLE_ILLIANS
  - `bPlayable`: 1
  - `FreeUnitClasses`: 開拓者 iFreeUnits=1 / 戦士 iFreeUnits=1 / 斥候 iFreeUnits=1
  - `FreeBuildingClasses`: 宮殿
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### Barbarian State - 蛮族の国

- 内部名: `CIVILIZATION_BARBARIAN`
- 指導者: 蛮族
- 代替ユニット: 斥候 ゴブリン / 術使い / 戦車兵 狼の戦車兵 / 鷹 / 騎乗兵 狼の騎乗兵 / 狩人 リザードマン / 魔術師 アケロンの信奉者 / 勇士 オーガ / 弓騎兵 / カタパルト / 大魔道 業火の申し子 / 火縄銃兵 / 不死者 オーガの親分 / 騎士 / 聖騎士 / ファランクス 石肌のオーガ / 戦象 / 大砲 / 輝ける衛士 / 影法師 / 傭兵
- 代替建造物: 長老会議 / 図書館 / 魔術師ギルド / 市場 / 記念碑 / 宮殿 / 厩舎 / 無神論者
- 種族: オーク
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_BLACK
  - `ArtStyleType`: ARTSTYLE_BARBARIAN
  - `UnitClassRaces`: 狂戦士 オーク / 騎乗兵 ゴブリン / 戦車兵 ゴブリン / レンジャー リザードマン / 暗殺者 リザードマン / 魔獣使い リザードマン / ドルイド僧 リザードマン
  - `UnitDescriptions`: 狩人 リザードマン / 戦士 オーク
  - `ImprovementTerrains`: 湿地
  - `ImprovementFeatures`: 密林
  - `TerrainYieldChanges`: 湿地 +1[食料]
  - `FeatureYieldChanges`: 密林 +1[食料]
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### Wilderness Animals - 野生の動物

- 内部名: `CIVILIZATION_ANIMAL`
- 指導者: 蛮族
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_BLACK
  - `ArtStyleType`: ARTSTYLE_BARBARIAN
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### Demons - 魔族

- 内部名: `CIVILIZATION_DEMONS`
- 指導者: 蛮族
- 代替ユニット: 術使い インプ / 狩人 地獄の番犬 / 火縄銃兵 / 狂戦士 バロール / 騎士 死の騎士
- 種族: 魔族
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_INFERNAL
  - `ArtStyleType`: ARTSTYLE_INFERNAL
  - `UnitDescriptions`: 斧兵 灰運び / 勇士 蝿王の眷属 / ファランクス スパルティアタイ / 不死者 悪魔貴族 / 暗殺者 処刑人 / レンジャー 狩り立てる悪魔 / 騎乗兵 墓生まれ / 鷹 渡り鴉
  - `InitialCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### Undead - 屍人

- 内部名: `CIVILIZATION_UNDEAD`
- 指導者: 蛮族
- 種族: 屍人
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_BLACK
  - `ArtStyleType`: ARTSTYLE_BARBARIAN
  - `InitialCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 宗教主義 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### Frostling - フロストリング

- 内部名: `CIVILIZATION_FROSTLING`
- 指導者: 蛮族
- 代替ユニット: 労働者 / 斥候 フロストリング / 騎乗兵 狼の騎乗兵
- 代替建造物: 長老会議 / 図書館 / 魔術師ギルド / 市場 / 記念碑 / 宮殿 / 厩舎
- 種族: フロストリング
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_BLACK
  - `ArtStyleType`: ARTSTYLE_BARBARIAN
  - `UnitClassRaces`: 騎乗兵 フロストリング / 戦車兵 フロストリング
  - `UnitDescriptions`: 弓兵 フロストリング弓兵 / 騎乗兵 フロストリング狼騎兵 / 狼の騎乗兵 フロストリング狼騎兵
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### Pirate - 海賊

- 内部名: `CIVILIZATION_PIRATES`
- 指導者: 蛮族
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_BLACK
  - `ArtStyleType`: ARTSTYLE_LANUN
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 不偏不党 / 無所属

### @Random (by Alignment) - 属性限定

- 内部名: `CIVILIZATION_RANDOM`
- 指導者: ランダム（善良限定） / ランダム（中立限定） / ランダム（邪悪限定） / （ヴァニラの指導者） / TXT_KEY_LEADER_RANDOM_MALE / （女性の指導者） / （ドワーフ指導者） / （エルフ指導者） / TXT_KEY_LEADER_RANDOM_WINTERBORN / TXT_KEY_LEADER_RANDOM_LIZARDMAN / （無生物指導者） / TXT_KEY_LEADER_RANDOM_AGGRESSIVE / TXT_KEY_LEADER_RANDOM_SPIRITUAL / TXT_KEY_LEADER_RANDOM_INDUSTRIOUS / TXT_KEY_LEADER_RANDOM_FINANCIAL / TXT_KEY_LEADER_RANDOM_ARCANE / TXT_KEY_LEADER_RANDOM_RAIDERS / TXT_KEY_LEADER_RANDOM_DEFENDER / TXT_KEY_LEADER_RANDOM_CHARGE / TXT_KEY_LEADER_RANDOM_SPEECH / TXT_KEY_LEADER_RANDOM_NOURISH / TXT_KEY_LEADER_RANDOM_CONSTRUCTION / TXT_KEY_LEADER_RANDOM_BUILDER / TXT_KEY_LEADER_RANDOM_GENERAL / TXT_KEY_LEADER_RANDOM_AGNOSTIC / TXT_KEY_LEADER_RANDOM_BARBARIAN / TXT_KEY_LEADER_RANDOM_SPRAWLING / TXT_KEY_LEADER_RANDOM_ADAPTIVE / TXT_KEY_LEADER_RANDOM_FALLOW / （呪文の達人指導者） / （非金融志向の指導者） / （非無神論の指導者） / TXT_KEY_LEADER_RANDOM_NO_BARBARIAN / TXT_KEY_LEADER_RANDOM_NO_SPRAWLING / TXT_KEY_LEADER_RANDOM_NO_FALLOW
- その他の設定:
  - `DefaultPlayerColor`: PLAYERCOLOR_BLACK
  - `ArtStyleType`: ARTSTYLE_BARBARIAN
  - `bPlayable`: 1
  - `InitialCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 無所属
  - `AnarchyCivics`: 専制政治 / 国民国家 / 部族社会 / 地方分権 / 無所属
