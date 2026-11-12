# OAC/志向（0.57、XMLから生成）

- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）
- 生成元: `Civilizations/CIV4TraitInfos.xml`
- 読み方: 主要な項目は日本語ラベル付きで先頭に、それ以外の既定値でない設定は「その他の設定」にXMLのタグ名のまま列挙する。値の内部名は日本語名に置き換えている。Pythonで実装された効果はXMLにないため含まない（ゲーム内ヘルプの説明文があれば載せている）。

### TRAIT_DUMMY - TRAIT_DUMMY

- 内部名: `TRAIT_DUMMY`

### Philosophical - 哲学志向

- 内部名: `TRAIT_PHILOSOPHICAL`
- その他の設定:
  - `iGreatPeopleRateModifier`: 100
  - `bSelectable`: 1

### Aggressive - 攻撃志向

- 内部名: `TRAIT_AGGRESSIVE`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]+10%: 軍事ユニットの訓練 / [SPACE][SPACE]都市の駐留ユニットに確率で 無償の経験値+1 (上限 3)
- その他の設定:
  - `bSelectable`: 1
  - `FreePromotions`: 戦闘Ⅰ
  - `FreePromotionUnitCombats`: 秘術ユニット / 弓術ユニット / 信奉ユニット / 無能ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット

### Spiritual - 宗教志向

- 内部名: `TRAIT_SPIRITUAL`
- その他の設定:
  - `bSelectable`: 1
  - `iFreePromotionPick`: 1
  - `FreePromotions`: 潜在力
  - `FreePromotionUnitCombats`: 信奉ユニット

### Expansive - 拡張志向

- 内部名: `TRAIT_EXPANSIVE`
- その他の設定:
  - `iHealth`: 3
  - `bSelectable`: 1

### Industrious - 勤労志向

- 内部名: `TRAIT_INDUSTRIOUS`
- その他の設定:
  - `iMaxGlobalBuildingProductionModifier`: 50
  - `iMaxTeamBuildingProductionModifier`: 50
  - `iMaxPlayerBuildingProductionModifier`: 50
  - `bSelectable`: 1
  - `FreePromotions`: 機動力Ⅰ
  - `FreePromotionUnitCombats`: 労働ユニット

### Creative - 創造志向

- 内部名: `TRAIT_CREATIVE`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]文化税率から得られる幸福 2倍 / [SPACE][SPACE]次の資源から+1: 染料
- その他の設定:
  - `iCultureInfluenceModifier`: 50
  - `bSelectable`: 1
  - `CommerceChanges`: 2[文化]

### Financial - 金融志向

- 内部名: `TRAIT_FINANCIAL`
- その他の設定:
  - `bSelectable`: 1
  - `ExtraYieldThresholds`: iExtraYieldThreshold=2

### Organized - 組織志向

- 内部名: `TRAIT_ORGANIZED`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]叛乱期間を最大1ターンに短縮
- その他の設定:
  - `iUpkeepModifier`: -100
  - `bSelectable`: 1

### Charismatic - カリスマ志向

- 内部名: `TRAIT_CHARISMATIC`
- その他の設定:
  - `iHappiness`: 2
  - `iLevelExperienceModifier`: -25
  - `bSelectable`: 1

### Arcane - 秘術志向

- 内部名: `TRAIT_ARCANE`
- その他の設定:
  - `bSelectable`: 1
  - `bDoubleManaEffect`: 1
  - `FreePromotions`: 潜在力 / 秘術師
  - `FreePromotionUnitCombats`: 秘術ユニット

### Raiders - 侵掠志向

- 内部名: `TRAIT_RAIDERS`
- その他の設定:
  - `bSelectable`: 1
  - `iPillagingGold`: 100
  - `FreePromotions`: 特別奇襲
  - `FreePromotionUnitCombats`: 秘術ユニット / 弓術ユニット / 信奉ユニット / 無能ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット

### Summoner - 召喚志向

- 内部名: `TRAIT_SUMMONER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]都市にポータルが無償で与えられる
- その他の設定:
  - `iMaxProjectProductionModifier`: 50
  - `bSelectable`: 1
  - `iSummonDuration`: 1
  - `FreePromotions`: 召喚術師
  - `FreePromotionUnitCombats`: 秘術ユニット

### Defender - 防御志向

- 内部名: `TRAIT_DEFENDER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]+1 防御時の戦闘経験点
- その他の設定:
  - `bSelectable`: 1
  - `FreePromotions`: 教練Ⅰ / 母国
  - `FreePromotionUnitCombats`: 弓術ユニット / 信奉ユニット / 無能ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット

### Rapid - 迅速志向

- 内部名: `TRAIT_RAPID`
- その他の設定:
  - `bSelectable`: 1
  - `FreePromotions`: 機動力Ⅰ / 側面攻撃Ⅰ
  - `FreePromotionUnitCombats`: 弓術ユニット / 魔獣ユニット / 無能ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット

### Scientific - 探求志向

- 内部名: `TRAIT_SCIENTIFIC`
- その他の設定:
  - `bSelectable`: 1
  - `CommerceChanges`: 1[研究]
  - `CommerceModifiers`: 20[研究]
  - `FreePromotions`: 冒険者
  - `FreePromotionUnitCombats`: 偵察ユニット / 動物ユニット

### Prophet - 預言志向

- 内部名: `TRAIT_PROPHET`
- その他の設定:
  - `CommerceChanges`: 3[研究]
  - `FreePromotions`: 災厄 / 高速詠唱
  - `FreePromotionUnitCombats`: 信奉ユニット

### Charge - 突撃志向

- 内部名: `TRAIT_CHARGE`
- その他の設定:
  - `bSelectable`: 1
  - `FreePromotions`: 突撃
  - `FreePromotionUnitCombats`: 信奉ユニット / 無能ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット / 攻城兵器

### TXT_KEY_TRAIT_IMPERIALIST - TXT_KEY_TRAIT_IMPERIALIST

- 内部名: `TRAIT_IMPERIALIST`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]黄金時代の期間+25% / [SPACE][SPACE]+25%: 労働者のタイル整備速度
- その他の設定:
  - `iGreatGeneralRateModifier`: 100
  - `bSelectable`: 1

### Sacrifice the weak - 弱肉強食志向

- 内部名: `TRAIT_SACRIFICE_THE_WEAK`
- その他の設定:
  - `bSelectable`: 1
  - `iPillagingGold`: 100
  - `FreePromotions`: 強襲Ⅰ
  - `FreePromotionUnitCombats`: 弓術ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット / 攻城兵器

### Chanter - 詠唱志向

- 内部名: `TRAIT_CHANTER`
- その他の設定:
  - `bSelectable`: 1
  - `FreePromotions`: 詠唱者
  - `FreePromotionUnitCombats`: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット

### Intensification - 強化志向

- 内部名: `TRAIT_INTENSIFICATION`
- その他の設定:
  - `bSelectable`: 1
  - `iFreeXPFromCombat`: 1
  - `iUpgradeCostModifier`: -50
  - `FreePromotions`: 増幅
  - `FreePromotionUnitCombats`: 秘術ユニット

### Speech - 話術志向

- 内部名: `TRAIT_SPEECH`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]ライバル文明の指導者から+6: 外交態度
- その他の設定:
  - `bSelectable`: 1
  - `FreePromotions`: 折伏Ⅰ / 折伏Ⅱ
  - `FreePromotionUnitCombats`: 信奉ユニット / 無能ユニット / 白兵ユニット / 偵察ユニット

### Militaristic - 軍事志向

- 内部名: `TRAIT_MILITARISTIC`
- その他の設定:
  - `bSelectable`: 1
  - `FreePromotions`: 都市襲撃Ⅰ
  - `FreePromotionUnitCombats`: 弓術ユニット / 信奉ユニット / 無能ユニット / 白兵ユニット / 騎乗ユニット / 攻城兵器 / 偵察ユニット

### Hunter - 野戦志向

- 内部名: `TRAIT_HUNTER`
- その他の設定:
  - `iHealth`: 1
  - `bSelectable`: 1
  - `FreePromotions`: 野戦
  - `FreePromotionUnitCombats`: 弓術ユニット / 信奉ユニット / 騎乗ユニット / 偵察ユニット

### Patrol - 警邏志向

- 内部名: `TRAIT_PATROL`
- その他の設定:
  - `bSelectable`: 1
  - `FreePromotions`: ゲリラⅠ / 森番Ⅰ / 歩哨Ⅰ
  - `FreePromotionUnitCombats`: 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 無能ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット

### Collector - 蒐集志向

- 内部名: `TRAIT_COLLECTOR`
- その他の設定:
  - `bSelectable`: 1
  - `CommerceModifiers`: 20[ゴールド]
  - `FreePromotions`: 蒐集
  - `FreePromotionUnitCombats`: 秘術ユニット / 弓術ユニット / 信奉ユニット / 無能ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット

### Nourish - 成長志向

- 内部名: `TRAIT_NOURISH`
- その他の設定:
  - `iHealth`: 1
  - `bSelectable`: 1
  - `ExtraYieldThresholds`: iExtraYieldThreshold=4

### Agricultural - 農耕志向

- 内部名: `TRAIT_AGRICULTURAL`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]都市は人口2からの開始 / [SPACE][SPACE]人口増加時に追加の
- その他の設定:
  - `iHealth`: 1
  - `bSelectable`: 1

### Wise - 賢人志向

- 内部名: `TRAIT_WISE`
- その他の設定:
  - `iGreatPeopleRateModifier`: 50
  - `bSelectable`: 1
  - `CommerceChanges`: 1[研究], 1[文化]

### Construction - 建設志向

- 内部名: `TRAIT_CONSTRUCTION`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]-20%: 建造物コスト / [SPACE][SPACE]都市に +1: 特別市民が無償で与えられる
- その他の設定:
  - `bSelectable`: 1

### Almighty - 万能志向

- 内部名: `TRAIT_ALMIGHTY`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]新規ユニットに +2: 経験ポイント / [SPACE][SPACE]都市で感謝祭がランダム発動 (とに余裕が必要)
- その他の設定:
  - `iHealth`: 1
  - `iHappiness`: 1
  - `iUpkeepModifier`: -25
  - `iGreatPeopleRateModifier`: 10
  - `bSelectable`: 1
  - `CommerceModifiers`: 5[ゴールド], 5[研究], 5[文化]

### Iron-Will - 伝道志向

- 内部名: `TRAIT_IRON_WILL`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]都市建設時に国教を布教 / [SPACE][SPACE]創始された宗教が国内に伝播 / [SPACE][SPACE]無信仰の新規ユニットは国教を信奉
- その他の設定:
  - `bSelectable`: 1
  - `CommerceModifiers`: 20[文化]
  - `FreePromotions`: 機動力Ⅰ / 異端審問
  - `FreePromotionUnitCombats`: 秘術ユニット / 信奉ユニット

### Builder - 生産志向

- 内部名: `TRAIT_BUILDER`
- その他の設定:
  - `bSelectable`: 1
  - `ExtraYieldThresholds`: iExtraYieldThreshold=3

### Riches - 商才志向

- 内部名: `TRAIT_RICHES`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]所持金に応じ都市出力上昇 / [SPACE][SPACE]外交取引のゴールド取得+50% / [SPACE][SPACE]いずれかの文明間で取引が発生 した時、取引額の10%をあなたの国庫に 加えます。
- その他の設定:
  - `bSelectable`: 1
  - `iStartingGold`: 150

### Oppress - 徴税志向

- 内部名: `TRAIT_OPPRESS`
- その他の設定:
  - `bSelectable`: 1
  - `CommerceChanges`: 4[ゴールド]
  - `CommerceModifiers`: -10[文化]

### Legend - 伝説志向

- 内部名: `TRAIT_LEGEND`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]ランダムに黄金期発動 / [SPACE][SPACE]英雄がいれば配下のユニットに +1: 経験ポイント(確率は20%/ターン)

### Trader - 交易志向

- 内部名: `TRAIT_TRADER`
- その他の設定:
  - `bSelectable`: 1
  - `TradeYieldModifiers`: +100[商業]
  - `FreePromotions`: 航海術Ⅰ
  - `FreePromotionUnitCombats`: 海軍ユニット

### General - 将官志向

- 内部名: `TRAIT_GENERAL`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]新規ユニットに無償の昇進(+1～2 任意の昇進)
- その他の設定:
  - `bSelectable`: 1
  - `FreePromotionUnitCombats`: 秘術ユニット / 弓術ユニット / 動物ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット

### Greedy - 強欲志向

- 内部名: `TRAIT_GREEDY`
- その他の設定:
  - `iMaxGlobalBuildingProductionModifier`: 20
  - `iMaxTeamBuildingProductionModifier`: 20
  - `iMaxPlayerBuildingProductionModifier`: 20
  - `bSelectable`: 1
  - `CommerceChanges`: 1[ゴールド]
  - `CommerceModifiers`: 10[ゴールド]
  - `FreePromotions`: 賞金稼ぎ
  - `FreePromotionUnitCombats`: 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット

### Magic Resistant - 魔法抵抗志向

- 内部名: `TRAIT_MAGIC_RESISTANT`
- その他の設定:
  - `FreePromotions`: 魔法抵抗
  - `FreePromotionUnitCombats`: 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット

### Agnostic - 無神論志向

- 内部名: `TRAIT_AGNOSTIC`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]ユニットは信仰を持たない
- その他の設定:
  - `iMaxProjectProductionModifier`: 50
  - `bAgnostic`: 1
  - `DisableTechs`: 魂の堕落 / 深海からの神託 / 天界からの指令 / 母なる大地への道 / 深き森への道

### Barbarian - 蛮族志向

- 内部名: `TRAIT_BARBARIAN`
- その他の設定:
  - `bBarbarianAlly`: 1
  - `CommerceModifiers`: -10[文化]

### Sprawling - 大都市志向

- 内部名: `TRAIT_SPRAWLING`
- その他の設定:
  - `iHappiness`: 3
  - `bSprawling`: 1
  - `iMaxCities`: 4
  - `CommerceChanges`: 1[ゴールド], 1[研究], 1[文化]
  - `iFreePromotionPick`: 1
  - `FreePromotionUnitCombats`: 秘術ユニット / 弓術ユニット / 動物ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット

### Ingenuity - 工夫志向

- 内部名: `TRAIT_INGENUITY`
- その他の設定:
  - `iStartingGold`: 50
  - `iUpgradeCostModifier`: -25

### Adaptive - 適応志向

- 内部名: `TRAIT_ADAPTIVE`
- その他の設定:
  - `bAdaptive`: 1

### Insane - 狂気志向

- 内部名: `TRAIT_INSANE`
- その他の設定:
  - `bInsane`: 1

### Fallow - 休耕志向

- 内部名: `TRAIT_FALLOW`
- その他の設定:
  - `bIgnoreFood`: 1

### Tolerant - 寛容志向

- 内部名: `TRAIT_TOLERANT`
- その他の設定:
  - `bAssimilation`: 1

### Dexterous - 器用

- 内部名: `TRAIT_DEXTEROUS`
- その他の設定:
  - `FreePromotions`: 器用
  - `FreePromotionUnitCombats`: 弓術ユニット

### Guardsman - 護衛

- 内部名: `TRAIT_GUARDSMAN`
- その他の設定:
  - `FreePromotions`: 護衛
  - `FreePromotionUnitCombats`: 弓術ユニット / 白兵ユニット

### Horselord - 駿馬

- 内部名: `TRAIT_HORSELORD`
- その他の設定:
  - `FreePromotions`: 駿馬
  - `FreePromotionUnitCombats`: 騎乗ユニット

### Sinister - 凶刃

- 内部名: `TRAIT_SINISTER`
- その他の設定:
  - `FreePromotions`: 凶刃
  - `FreePromotionUnitCombats`: 偵察ユニット

### Sundered - 呪刻

- 内部名: `TRAIT_SUNDERED`
- その他の設定:
  - `FreePromotions`: 呪刻
  - `FreePromotionUnitCombats`: 秘術ユニット

### Foolish - 愚鈍志向

- 内部名: `TRAIT_FOOLISH`
- その他の設定:
  - `CommerceModifiers`: -15[研究]

### Weak - 非力志向

- 内部名: `TRAIT_WEAK`
- その他の設定:
  - `FreePromotions`: 非力
  - `FreePromotionUnitCombats`: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット

### Improve - 兵器改良

- 内部名: `TRAIT_IMPROVE`
- その他の設定:
  - `FreePromotions`: 機動力Ⅰ / 行軍 / 水陸両用 / 電撃戦 / 特別奇襲
  - `FreePromotionUnitCombats`: 攻城兵器

### Animal - 馴致

- 内部名: `TRAIT_ANIMAL`
- その他の設定:
  - `FreePromotions`: 動物調教
  - `FreePromotionUnitCombats`: 偵察ユニット / 動物ユニット

### Samurai Soul - 士魂

- 内部名: `TRAIT_SAMURAI_SOUL`
- その他の設定:
  - `iFreePromotionPick`: 1
  - `FreePromotionUnitCombats`: 秘術ユニット / 弓術ユニット / 動物ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 偵察ユニット

### Indomitable - 不屈

- 内部名: `TRAIT_INDOMITABLE`
- その他の設定:
  - `FreePromotions`: 病気無効
  - `FreePromotionUnitCombats`: 秘術ユニット / 弓術ユニット / 動物ユニット / 魔獣ユニット / 信奉ユニット / 無能ユニット / 白兵ユニット / 騎乗ユニット / 海軍ユニット / 攻城兵器 / 偵察ユニット

### Unreasonable - 理不尽志向

- 内部名: `TRAIT_UNREASONABLE`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]黄金時代がランダムに発動 / [SPACE][SPACE]黄金時代がランダムに短縮 / [SPACE][SPACE]新規ユニットはランダムに +1:任意の無償の昇進 / [SPACE][SPACE]無償の昇進を得られる新規ユニットは ランダムに-1:任意の無償の昇進

### Pillage - 掠奪

- 内部名: `TRAIT_PILLAGE`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]都市戦闘に勝利するとを獲得

### Great People - 不世出志向

- 内部名: `TRAIT_GREAT_PEOPLE`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]都市に不世出の偉人が無償で 与えられる

### Undead - 屍人志向

- 内部名: `TRAIT_UNDEAD`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]配下のユニットは屍人になる / [SPACE][SPACE]配下のユニットに病原巣が与えられる

### Black-Magic - 外法

- 内部名: `TRAIT_BLACK_MAGIC`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]新規ユニットに世代に応じた暗黒魔法 の昇進を与える(20%)
- その他の設定:
  - `iSummonDuration`: 1
  - `CommerceModifiers`: -10[文化]
  - `FreePromotions`: 烙印
  - `FreePromotionUnitCombats`: 秘術ユニット / 信奉ユニット

### Stranger - 異邦人

- 内部名: `TRAIT_STRANGER`
- その他の設定:
  - `FreePromotions`: 異邦人
  - `FreePromotionUnitCombats`: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット

### Brain-Muscular - 脳筋志向

- 内部名: `TRAIT_BRAIN_MUSCULAR`
- その他の設定:
  - `CommerceModifiers`: -10[ゴールド], -10[研究], -50[文化]
  - `iFreePromotionPick`: 1
  - `FreePromotions`: 電撃戦 / 行軍 / 勇気 / 武勇
  - `FreePromotionUnitCombats`: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット / 海軍ユニット / 攻城兵器

### Slaver - 奴隷志向

- 内部名: `TRAIT_SLAVER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]捕縛ユニットが奴隷に変化
- その他の設定:
  - `iMaxAnarchy`: 1

### Mechanic - 整備士志向

- 内部名: `TRAIT_MECHANIC`
- その他の設定:
  - `FreePromotions`: 機械
  - `FreePromotionUnitCombats`: 攻城兵器

### Faith - 信仰志向

- 内部名: `TRAIT_FAITH`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]宗教創始により黄金期を開始 / [SPACE][SPACE]国教の聖都獲得により黄金期を開始 (ただし期間の延長はしない)

### Starvation - 飢餓志向

- 内部名: `TRAIT_STARVATION`
- その他の設定:
  - `iHealth`: -2
  - `FreePromotions`: 人食い
  - `FreePromotionUnitCombats`: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット

### Oshitari - 忍足

- 内部名: `TRAIT_OSHITARI`
- その他の設定:
  - `FreePromotions`: 身隠し / 忍足
  - `FreePromotionUnitCombats`: 偵察ユニット

### Amphibious - 水陸両用

- 内部名: `TRAIT_AMPHIBIOUS`
- その他の設定:
  - `FreePromotions`: 水陸両用
  - `FreePromotionUnitCombats`: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット

### Pedigree - 血統

- 内部名: `TRAIT_PEDIGREE`
- その他の設定:
  - `FreePromotions`: 血統
  - `FreePromotionUnitCombats`: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット

### Survival - 残存

- 内部名: `TRAIT_SURVIVAL`
- その他の設定:
  - `FreePromotions`: 残存
  - `FreePromotionUnitCombats`: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット

### Temperamental - 悋気志向

- 内部名: `TRAIT_TEMPERAMENTAL`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]属性が無作為に変化

### Unenlightened - 暗愚志向

- 内部名: `TRAIT_UNENLIGHTENED`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]ランダムに性能変化
- その他の設定:
  - `iGreatPeopleRateModifier`: -25
  - `iMaxGlobalBuildingProductionModifier`: -25
  - `iMaxTeamBuildingProductionModifier`: -25
  - `iMaxPlayerBuildingProductionModifier`: -25
  - `iMaxProjectProductionModifier`: -25
  - `bAdaptive`: 1

### Diverse - 多様志向

- 内部名: `TRAIT_DIVERSE`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]ユニットはランダムな種族で生まれる

### Illusionist - 幻術志向

- 内部名: `TRAIT_ILLUSIONIST`
- その他の設定:
  - `FreePromotions`: 幻術士
  - `FreePromotionUnitCombats`: 秘術ユニット

### Redeeming - 挽回志向

- 内部名: `TRAIT_REDEEMING`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]戦闘勝利により黄金時代を開始

### Deathtouched - 触死志向

- 内部名: `TRAIT_DEATHTOUCHED`
- その他の設定:
  - `FreePromotions`: 屍霊術
  - `FreePromotionUnitCombats`: 秘術ユニット / 信奉ユニット

### Variant - 瘴烟

- 内部名: `TRAIT_VARIANT`
- その他の設定:
  - `FreePromotions`: 瘴烟
  - `FreePromotionUnitCombats`: 秘術ユニット / 動物ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット / 労働ユニット

### Demon Slaying - 退魔志向

- 内部名: `TRAIT_DEMON_SLAYING`
- その他の設定:
  - `FreePromotions`: 魔族狩り
  - `FreePromotionUnitCombats`: 信奉ユニット / 白兵ユニット

### Martyrdom - 殉死志向

- 内部名: `TRAIT_MARTYRDOM`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]-20%: 厭戦感情
- その他の設定:
  - `FreePromotions`: 忠誠
  - `FreePromotionUnitCombats`: 秘術ユニット / 弓術ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット

### Revenger - 復讐志向

- 内部名: `TRAIT_REVENGER`
- その他の設定:
  - `FreePromotions`: 復讐
  - `FreePromotionUnitCombats`: 信奉ユニット / 白兵ユニット

### Precocious - 早熟志向

- 内部名: `TRAIT_PRECOCIOUS`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]テクノロジー開発の進捗度が30%以上 になると、この志向の補正値の正負が 反転する
- その他の設定:
  - `iGreatPeopleRateModifier`: 10
  - `CommerceModifiers`: 10[ゴールド], 10[研究], 10[文化]

### Precocious - 早熟志向

- 内部名: `TRAIT_PRECOCIOUS_NERF`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]テクノロジー開発の進捗度が30%以上 になると、この志向の補正値の正負が 反転する
- その他の設定:
  - `iGreatPeopleRateModifier`: -10
  - `CommerceModifiers`: -10[ゴールド], -10[研究], -10[文化]

### Fanatic - 狂信志向

- 内部名: `TRAIT_FANATIC`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]自動的に国教が領内に広まる / [SPACE][SPACE]異教は自動的に排除される / [SPACE][SPACE]異教徒に宣戦
- その他の設定:
  - `iFreePromotionPick`: 1
  - `FreePromotions`: 怪力 / 召喚術師 / 散兵
  - `FreePromotionUnitCombats`: 信奉ユニット

### Inorganic - 無機質志向

- 内部名: `TRAIT_INORGANIC`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]ゴーレムは自爆装置を持つことがある
- その他の設定:
  - `FreePromotions`: ゴーレム
  - `FreePromotionUnitCombats`: 動物ユニット / 弓術ユニット / 魔獣ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット / 海軍ユニット / 攻城兵器 / 労働ユニット

### Warmonkey - 戦争狂志向

- 内部名: `TRAIT_WARMONKEY`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]オルタス出現ターン(速度普通であれば 75ターン経過後)以降に戦争可能になる と既知の文明へ自動的に宣戦布告 （和平交渉は可能） / [SPACE][SPACE]厭戦感情をに変換
- その他の設定:
  - `FreePromotions`: 戦闘Ⅱ / 教練Ⅱ
  - `FreePromotionUnitCombats`: 秘術ユニット / 弓術ユニット / 魔獣ユニット / 信奉ユニット / 白兵ユニット / 騎乗ユニット / 偵察ユニット / 海軍ユニット / 攻城兵器

### Crazy-by-Worldheritage - 遺産狂志向

- 内部名: `TRAIT_CRAZY_BY_WORLDHERITAGE`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]都市に遺産狂が無償で与えられる / [SPACE][SPACE]世界遺産を完成させると黄金時代を 開始または延長 / [SPACE][SPACE]他国が遺産を完成させると怒りの 宣戦布告と一時断交 黄金期中ならば期間短縮の上で、 各都市が20%で叛乱を起こす （マーキュリアンの門と聖都建造物 （祭殿＋固有装備品）は対象外）
- その他の設定:
  - `iUpkeepModifier`: 100

### Air Magic Master - 大気の達人

- 内部名: `TRAIT_AIR_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた大気の昇進を無償で与える

### Body Magic Master - 肉体の達人

- 内部名: `TRAIT_BODY_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた肉体の昇進を無償で与える

### Chaos Magic Master - 混沌の達人

- 内部名: `TRAIT_CHAOS_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた混沌の昇進を無償で与える

### Death Magic Master - 死の達人

- 内部名: `TRAIT_DEATH_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた死の昇進を無償で与える

### Earth Magic Master - 大地の達人

- 内部名: `TRAIT_EARTH_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた大地の昇進を無償で与える

### Enchantment Magic Master - 呪付の達人

- 内部名: `TRAIT_ENCHANTMENT_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた呪付の昇進を無償で与える

### Entropy Magic Master - 不可逆の達人

- 内部名: `TRAIT_ENTROPY_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた不可逆の昇進を無償で与える

### Fire Magic Master - 炎の達人

- 内部名: `TRAIT_FIRE_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた炎の昇進を無償で与える

### Ice Magic Master - 氷の達人

- 内部名: `TRAIT_ICE_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた氷の昇進を無償で与える

### Law Magic Master - 法の達人

- 内部名: `TRAIT_LAW_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた法の昇進を無償で与える

### Life Magic Master - 生命の達人

- 内部名: `TRAIT_LIFE_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた生命の昇進を無償で与える

### Metamagic Magic Master - 超魔術の達人

- 内部名: `TRAIT_METAMAGIC_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた超魔術の昇進を無償で与える

### Mind Magic Master - 精神の達人

- 内部名: `TRAIT_MIND_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた精神の昇進を無償で与える

### Nature Magic Master - 自然の達人

- 内部名: `TRAIT_NATURE_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた自然の昇進を無償で与える

### Shadow Magic Master - 影の達人

- 内部名: `TRAIT_SHADOW_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた影の昇進を無償で与える

### Spirit Magic Master - 魂の達人

- 内部名: `TRAIT_SPIRIT_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた魂の昇進を無償で与える

### Sun Magic Master - 太陽の達人

- 内部名: `TRAIT_SUN_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた太陽の昇進を無償で与える

### Water Magic Master - 水の達人

- 内部名: `TRAIT_WATER_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた水の昇進を無償で与える

### Dimensional Magic Master - 次元の達人

- 内部名: `TRAIT_DIMENSIONAL_MAGIC_MASTER`
- 説明（ゲーム内ヘルプ）: / [SPACE][SPACE]秘術ユニットの精神集中のランクに 応じた次元の昇進を無償で与える
