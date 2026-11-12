"""OAC 0.57 の XML から各分野（ユニット・建造物など）のデータ Markdown を生成する。

テクノロジーは gen_tech.py が担当。こちらは各 Info の「既定値でない設定」を
日本語名に置き換えて機械的に列挙する（主要な項目は日本語ラベル付きで先頭に出す）。

usage: python3 gen_infos.py <Assets/XML のパス> <出力フォルダ> [ゲーム本体のTextフォルダ ...]
"""
import glob
import html
import os
import re
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict

XML, OUTDIR = sys.argv[1], sys.argv[2]

# ---------- テキスト ----------
JA, EN = {}, {}
files = sorted(glob.glob(f"{XML}/Text/*.xml"))
for extra in sys.argv[3:]:
    files += sorted(glob.glob(f"{extra}/*.xml"))
for f in files:
    t = open(f, "rb").read().decode("cp932", "replace")
    for m in re.finditer(r"<TEXT>(.*?)</TEXT>", t, re.S):
        body = m.group(1)
        tag = re.search(r"<Tag>(.*?)</Tag>", body)
        if not tag:
            continue
        key = tag.group(1).strip()

        def get(lang):
            mm = re.search(rf"<{lang}>(.*?)</{lang}>", body, re.S)
            if not mm:
                return ""
            inner = re.search(r"<Text>(.*?)</Text>", mm.group(1), re.S)
            return html.unescape((inner.group(1) if inner else mm.group(1)).strip())

        ja = get("Japanese") or get("French")
        if ja and key not in JA:
            JA[key] = ja
        en = get("English")
        if en and key not in EN:
            EN[key] = en


def strip_markup(s):
    s = re.sub(r"\[LINK=[^\]]*\]|\[\\LINK\]|\[COLOR[^\]]*\]|\[\\COLOR\]|\[ICON_[A-Z_]+\]", "", s)
    return s.replace("[NEWLINE]", " / ").replace("[PARAGRAPH:1]", " / ").replace("[TAB]", "")


def name_text(key, table):
    return strip_markup(table.get(key, EN.get(key, key))).split(":")[0].strip()


# ---------- XML ----------
def load(path):
    raw = open(f"{XML}/{path}", "rb").read().decode("latin-1")
    raw = re.sub(r'\sxmlns="[^"]+"', "", raw, count=1)
    raw = re.sub(r"<!--.*?-->", "", raw, flags=re.S)
    return ET.fromstring(raw.encode("latin-1"))


def txt(e, tag, default=""):
    c = e.find(tag)
    return c.text.strip() if c is not None and c.text and c.text.strip() else default


DESC = {}
for f in glob.glob(f"{XML}/*/*.xml"):
    if "/Text/" in f or "/Art/" in f or "/Audio/" in f or "Schema" in f:
        continue
    try:
        root = load(os.path.relpath(f, XML))
    except ET.ParseError:
        continue
    for e in root.iter():
        ty, de = e.find("Type"), e.find("Description")
        if ty is not None and de is not None and ty.text and de.text:
            DESC.setdefault(ty.text.strip(), de.text.strip())


def ja_name(type_):
    return name_text(DESC.get(type_, type_), JA)


def en_name(type_):
    return name_text(DESC.get(type_, type_), EN)


YIELD = ["食料", "ハンマー", "商業"]
COMMERCE = ["ゴールド", "研究", "文化", "諜報"]
DEFAULTS = {"", "0", "NONE", "-1", "0.0", "0.00"}
SKIP = re.compile(
    r"^(Type|Description|Civilopedia|Strategy|Pronunciation|Quote|Button|Art|ArtDefineTag|EarlyArtDefineTag|LateArtDefineTag|"
    r"MiddleArtDefineTag|UnitMeshGroups|Advisor|Sound|SoundMP|.*Sound.*|Movie.*|HotKey.*|bAltDown|bShiftDown|bCtrlDown|"
    r"bAltDownAlt|bShiftDownAlt|bCtrlDownAlt|HotKeyAlt|iHotKeyPriority.*|bGraphicalOnly|iAsset|iPower|iAdvancedStartCost.*|"
    r"Flavors|iAIWeight|iAITradeModifier|.*AI.*|iOrderPriority|iGridX|iGridY|ArtStyleTypes|UnitArtStyleType|Help|"
    r"ConstructSound|DiploMusic.*|Animation.*|.*Music.*|LeaderHead|CityNames|DerivativeCiv|AdjectiveDescription|ShortDescription|"
    r"Adjective|Plural|Gender|Civilopedia.*|FontButtonIndex|TextureBlend.*|iTextureIndex|iWorldSoundscape.*|bVisible|"
    r"CivilizationSelectionSound|ArtDefineTagAlt|DiplomacyMusic.*|MemoryAttitude.*|NoWarAttitudeProb.*|.*Attitude.*|"
    r"Unique.*Names|iBaseAttitude|iWonderConstructRand|.*Rand$|iEspionage.*|iMemory.*|iContactRand.*|.*Prob$|MovieDefineTag|Contact.*|MemoryDecays|ImprovementWeightModifiers|UnitAIWeightModifiers|bVanilla|iSomnium.*|Cities|UnitCivilopedias|.*Pedia.*)$"
)


UPKEEP = {"UPKEEP_NONE": "なし", "UPKEEP_LOW": "低額", "UPKEEP_MEDIUM": "中程度", "UPKEEP_HIGH": "高額"}


def render_val(v):
    if v in UPKEEP:
        return UPKEEP[v]
    if v.startswith("TXT_KEY_") and (v in JA or v in EN):
        return name_text(v, JA)
    return ja_name(v) if v in DESC else v


def render_children(e):
    kids = list(e)
    if not kids:
        return None
    tags = {k.tag for k in kids}
    vals = [(k.text or "").strip() for k in kids]
    if tags <= {"iYield"} and len(kids) <= 3:
        parts = [f"{int(v):+d}[{YIELD[i]}]" for i, v in enumerate(vals) if v not in DEFAULTS]
        return ", ".join(parts) or None
    if tags <= {"iCommerce", "iCommerceChange", "iCommerceModifier", "bFlexible"} and len(kids) <= 4:
        parts = [f"{v}[{COMMERCE[i]}]" for i, v in enumerate(vals) if v not in DEFAULTS]
        return ", ".join(parts) or None
    items = []
    for k in kids:
        if len(k) == 0:
            v = (k.text or "").strip()
            if v not in DEFAULTS:
                items.append(render_val(v) if k.tag in ("Type",) or v in DESC else f"{k.tag}={v}" if not v.isupper() else render_val(v))
            continue
        pairs = []
        for leaf in k.iter():
            if len(leaf) == 0 and leaf is not k:
                v = (leaf.text or "").strip()
                if v in DEFAULTS:
                    continue
                if v in DESC or v.startswith("TXT_KEY_"):
                    pairs.append(render_val(v))
                elif leaf.tag in ("iYield", "iCommerce"):
                    continue  # 産出の配列はコンテナ側でまとめて表示する
                else:
                    pairs.append(f"{leaf.tag}={v}" if not v.isupper() else v)
            elif len(leaf) and leaf is not k and leaf.tag in ("YieldChanges", "Yields", "TechYields", "CommerceChanges"):
                r = render_children(leaf)
                if r:
                    pairs.append(r)
        if len(pairs) > 1:
            pairs = [x for x in pairs if not re.fullmatch(r"b[A-Za-z]+=1", x)]
        if pairs and not (len(pairs) == 1 and pairs[0] in ("bTerrainTrade=1",)):
            items.append(" ".join(dict.fromkeys(pairs)))
    return " / ".join(items) or None


def help_text(e):
    key = txt(e, "Help")
    if key and key in JA:
        return strip_markup(JA[key]).strip()
    return ""


def describe(e, labels, skip_extra=()):
    lines = []
    used = set(skip_extra)
    for tag, label in labels:
        used.add(tag)
        c = e.find(tag)
        if c is None:
            continue
        if len(c):
            r = render_children(c)
            if r:
                lines.append(f"- {label}: {r}")
        else:
            v = (c.text or "").strip()
            if v not in DEFAULTS:
                lines.append(f"- {label}: {render_val(v)}")
    h = help_text(e)
    if h:
        lines.append(f"- 説明（ゲーム内ヘルプ）: {h}")
    other = []
    for c in e:
        if c.tag in used or SKIP.match(c.tag):
            continue
        if len(c):
            r = render_children(c)
            if r:
                other.append(f"  - `{c.tag}`: {r}")
        else:
            v = (c.text or "").strip()
            if v not in DEFAULTS:
                other.append(f"  - `{c.tag}`: {render_val(v)}")
    if other:
        lines.append("- その他の設定:")
        lines += other
    return lines


# ---------- 文明固有の判定 ----------
def build_owner():
    default = {}
    for path, item, key in [("Units/CIV4UnitClassInfos.xml", "UnitClassInfo", "DefaultUnit"),
                            ("Buildings/CIV4BuildingClassInfos.xml", "BuildingClassInfo", "DefaultBuilding")]:
        for e in load(path).iter(item):
            default[txt(e, "Type")] = txt(e, key)
    owners = defaultdict(set)
    for c in load("Civilizations/CIV4CivilizationInfos.xml").iter("CivilizationInfo"):
        cn = ja_name(txt(c, "Type"))
        for u in c.iter("Unit"):
            owners[txt(u, "UnitType")].add(cn)
        for b in c.iter("Building"):
            owners[txt(b, "BuildingType")].add(cn)
    return default, owners


DEFAULT_OF, OWNERS = build_owner()


def owner_line(e, class_tag):
    ty, cls = txt(e, "Type"), txt(e, class_tag)
    if DEFAULT_OF.get(cls) == ty:
        return []
    o = OWNERS.get(ty) - {""} if OWNERS.get(ty) else set()
    if o:
        return [f"- 固有: {'・'.join(sorted(o))}（{ja_name(DEFAULT_OF.get(cls, ''))} の代替）" if DEFAULT_OF.get(cls) not in ("", "NONE", None)
                else f"- 固有: {'・'.join(sorted(o))}"]
    return []


# ---------- 分野ごとの設定 ----------
U = [("Class", "ユニットクラス"), ("Combat", "兵科"), ("iCost", "コスト[ハンマー]"), ("iCombat", "攻撃力"),
     ("iCombatDefense", "防御力"), ("iMoves", "移動力"), ("iTier", "世代"), ("PrereqTech", "必要テクノロジー"),
     ("TechTypes", "追加で必要なテクノロジー"), ("PrereqBuilding", "必要な建造物"), ("BonusType", "必要な資源"),
     ("PrereqBonuses", "必要な資源（いずれか）"), ("PrereqReligion", "必要な宗教"), ("PrereqCiv", "必要な文明"),
     ("PrereqAlignment", "必要な属性"), ("FreePromotions", "初期昇進"), ("UnitClassUpgrades", "昇格先"),
     ("Upgrades", "昇格先"), ("UnitCombatType", "兵科"), ("DamageType", "攻撃属性"), ("iCombatLimit", "ダメージ上限"),
     ("iAirCombat", "間接攻撃力"), ("iAirRange", "間接攻撃の射程"), ("iWithdrawalProb", "退却率"),
     ("iFirstStrikes", "先制攻撃"), ("iChanceFirstStrikes", "先制攻撃のチャンス"), ("iCollateralDamage", "巻き添え被害"),
     ("iCargo", "積載量"), ("iWeaponTier", "武器の段階"), ("iMinLevel", "必要レベル")]
B = [("BuildingClass", "建造物クラス"), ("iCost", "コスト[ハンマー]"), ("PrereqTech", "必要テクノロジー"),
     ("TechTypes", "追加で必要なテクノロジー"), ("ObsoleteTech", "陳腐化"), ("PrereqReligion", "必要な宗教"),
     ("StateReligion", "必要な国教"), ("PrereqCiv", "必要な文明"), ("Bonus", "必要な資源"),
     ("PrereqBonuses", "必要な資源（いずれか）"), ("BuildingClassNeededs", "必要な建造物"), ("PrereqTrait", "必要な志向"),
     ("iHappiness", "[幸福]"), ("iHealth", "[衛生]"), ("YieldChanges", "産出"), ("YieldModifiers", "産出[%]"),
     ("CommerceChanges", "産出(商業系)"), ("CommerceModifiers", "産出(商業系)[%]"), ("FreePromotion", "新規ユニットに昇進"),
     ("iFreeExperience", "新規ユニットに経験値"), ("SpecialistCounts", "専門家枠"), ("FreeSpecialistCounts", "無償の専門家"),
     ("iDefense", "[都市防御]"), ("FreeBonus", "供給する資源"), ("iNumFreeBonuses", "供給数"), ("ProductionTraits", "倍速の志向"),
     ("BonusProductionModifiers", "倍速の資源")]
DOMAINS = [
    ("Units/CIV4UnitInfos.xml", "UnitInfo", "UnitData", "ユニット", U, "Combat", "Class"),
    ("Buildings/CIV4BuildingInfos.xml", "BuildingInfo", "BuildingData", "建造物・文化遺産", B, None, "BuildingClass"),
    ("Gameinfo/CIV4CivicInfos.xml", "CivicInfo", "CivicData", "社会制度",
     [("CivicOptionType", "分類"), ("TechPrereq", "必要テクノロジー"), ("Upkeep", "維持費")], "CivicOptionType", None),
    ("Gameinfo/CIV4ProjectInfo.xml", "ProjectInfo", "ProjectData", "大儀式",
     [("TechPrereq", "必要テクノロジー"), ("iCost", "コスト[ハンマー]"), ("PrereqCivilization", "必要な文明")], None, None),
    ("Units/CIV4PromotionInfos.xml", "PromotionInfo", "PromotionData", "昇進",
     [("PromotionPrereq", "前提昇進"), ("PromotionPrereqOr1", "前提昇進(いずれか)"), ("PromotionPrereqOr2", "前提昇進(いずれか)"),
      ("TechPrereq", "必要テクノロジー"), ("UnitCombats", "対象の兵科"), ("iCombatPercent", "+%[戦闘力]")], None, None),
    ("Units/CIV4SpellInfos.xml", "SpellInfo", "SpellData", "呪文・特殊技能",
     [("PromotionPrereq1", "必要な昇進"), ("PromotionPrereq2", "必要な昇進(2)"), ("TechPrereq", "必要テクノロジー"),
      ("UnitPrereq", "実行ユニット"), ("UnitClassPrereq", "実行ユニットクラス"), ("CivilizationPrereq", "実行文明"),
      ("ReligionPrereq", "必要な宗教"), ("iRange", "射程")], None, None),
    ("Gameinfo/CIV4ReligionInfo.xml", "ReligionInfo", "ReligionData", "宗教", [("TechPrereq", "創始テクノロジー")], None, None),
    ("Civilizations/CIV4TraitInfos.xml", "TraitInfo", "TraitData", "志向", [], None, None),
    ("Civilizations/CIV4CivilizationInfos.xml", "CivilizationInfo", "CivData", "文明",
     [("Alignment", "属性"), ("FreeTechs", "初期テクノロジー"), ("CivicDefaults", "初期社会制度"), ("Leaders", "指導者"),
      ("Units", "代替ユニット"), ("Buildings", "代替建造物"), ("DefaultRace", "種族")], None, None),
    ("Civilizations/CIV4LeaderHeadInfos.xml", "LeaderHeadInfo", "LeaderData", "指導者",
     [("Alignment", "属性"), ("Traits", "志向"), ("FavoriteCivic", "好む社会制度"), ("FavoriteWonder", "好む遺産"),
      ("FavoriteReligion", "お気に入りの宗教"), ("ReligionWeightModifiers", "宗教の重視度")], None, None),
    ("Terrain/CIV4BonusInfos.xml", "BonusInfo", "BonusData", "資源",
     [("BonusClassType", "分類"), ("TechReveal", "発見テクノロジー"), ("TechCityTrade", "有効化テクノロジー"),
      ("TechObsolete", "陳腐化"), ("YieldChanges", "産出"), ("iHappiness", "[幸福]"), ("iHealth", "[衛生]")], None, None),
    ("Terrain/CIV4ImprovementInfos.xml", "ImprovementInfo", "ImprovementData", "地形改善・名所旧跡",
     [("PrereqTech", "必要テクノロジー"), ("Yields", "産出"), ("ImprovementUpgrade", "昇格先"), ("iUpgradeTime", "昇格ターン"),
      ("BonusTypeStructs", "対応資源"), ("TechYieldChanges", "テクノロジーによる産出変化")], None, None),
    ("Terrain/CIV4TerrainInfos.xml", "TerrainInfo", "TerrainData", "地形", [("Yields", "産出")], None, None),
    ("Terrain/CIV4FeatureInfos.xml", "FeatureInfo", "FeatureData", "地物", [("YieldChanges", "産出の変化")], None, None),
    ("Gameinfo/CIV4SpecialistInfos.xml", "SpecialistInfo", "SpecialistData", "専門家",
     [("Yields", "産出"), ("Commerces", "産出(商業系)"), ("GreatPeopleUnitClass", "偉人"), ("iGreatPeopleRateChange", "偉人ポイント")], None, None),
    ("Gameinfo/CIV4EquipmentInfos.xml", "EquipmentInfo", "EquipmentData", "装備品", [], None, None),
    ("Misc/CIV4EffectInfos.xml", "EffectInfo", "EffectData", "効果", [], None, None),
]

os.makedirs(OUTDIR, exist_ok=True)
summary = []
for path, item, slug, title, labels, group, cls in DOMAINS:
    entries = list(load(path).iter(item))
    groups = defaultdict(list)
    for e in entries:
        groups[ja_name(txt(e, group)) if group else ""].append(e)
    out = [f"# OAC/{title}（0.57、XMLから生成）", "",
           "- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）",
           f"- 生成元: `{path}`",
           "- 読み方: 主要な項目は日本語ラベル付きで先頭に、それ以外の既定値でない設定は「その他の設定」にXMLのタグ名のまま列挙する。"
           "値の内部名は日本語名に置き換えている。Pythonで実装された効果はXMLにないため含まない（ゲーム内ヘルプの説明文があれば載せている）。",
           ""]
    for g in sorted(groups):
        if g:
            out += [f"## {g}", ""]
        for e in groups[g]:
            ty = txt(e, "Type")
            out += [f"### {en_name(ty)} - {ja_name(ty)}", "", f"- 内部名: `{ty}`"]
            if cls:
                out += owner_line(e, cls)
            out += describe(e, labels)
            out.append("")
    fn = f"{OUTDIR}/OAC-057_{slug}.md"
    open(fn, "w", encoding="utf-8").write("\n".join(out))
    summary.append((fn, len(entries)))
for fn, n in summary:
    print(n, fn)
