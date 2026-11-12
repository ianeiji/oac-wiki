"""OAC 0.57 の XML からテクノロジーデータの Markdown を生成する。

usage: python3 gen_tech.py <Assets/XML のパス> <出力ファイル> [ゲーム本体のTextフォルダ ...]
"""
import glob
import html
import re
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict

XML = sys.argv[1]
OUT = sys.argv[2]


def load(path):
    raw = open(f"{XML}/{path}", "rb").read().decode("latin-1")
    raw = re.sub(r'\sxmlns="[^"]+"', "", raw, count=1)
    raw = re.sub(r"<!--.*?-->", "", raw, flags=re.S)
    return ET.fromstring(raw.encode("latin-1"))


def txt(e, tag, default=""):
    c = e.find(tag)
    return c.text.strip() if c is not None and c.text and c.text.strip() else default


# ---- テキスト (日本語名) ----
JA, EN = {}, {}
TEXT_FILES = sorted(glob.glob(f"{XML}/Text/*.xml"))
for extra in sys.argv[3:]:  # ゲーム本体のテキスト (MOD側が優先)
    TEXT_FILES += sorted(glob.glob(f"{extra}/*.xml"))
for f in TEXT_FILES:
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
            v = mm.group(1)
            inner = re.search(r"<Text>(.*?)</Text>", v, re.S)
            return html.unescape((inner.group(1) if inner else v).strip())

        ja = get("Japanese") or get("French")
        if ja and key not in JA:
            JA[key] = ja
        en = get("English")
        if en and key not in EN:
            EN[key] = en


def clean(s):
    s = re.sub(r"\[LINK=[^\]]*\]|\[\\LINK\]|\[COLOR[^\]]*\]|\[\\COLOR\]", "", s)
    return s.split(":")[0].strip()


def ja(key):
    return clean(JA.get(key, EN.get(key, key)))


def en(key):
    return clean(EN.get(key, key))


def name_of(type_, desc_map):
    return ja(desc_map.get(type_, type_))


# ---- 各種 Info ----
def infos(path, item):
    return list(load(path).iter(item))


DESC = {}
for path, item in [
    ("Technologies/CIV4TechInfos.xml", "TechInfo"),
    ("Units/CIV4UnitInfos.xml", "UnitInfo"),
    ("Units/CIV4UnitClassInfos.xml", "UnitClassInfo"),
    ("Buildings/CIV4BuildingInfos.xml", "BuildingInfo"),
    ("Buildings/CIV4BuildingClassInfos.xml", "BuildingClassInfo"),
    ("Gameinfo/CIV4CivicInfos.xml", "CivicInfo"),
    ("Gameinfo/CIV4ProjectInfo.xml", "ProjectInfo"),
    ("Gameinfo/CIV4EraInfos.xml", "EraInfo"),
    ("Gameinfo/CIV4ReligionInfo.xml", "ReligionInfo"),
    ("Units/CIV4BuildInfos.xml", "BuildInfo"),
    ("Units/CIV4PromotionInfos.xml", "PromotionInfo"),
    ("Units/CIV4SpellInfos.xml", "SpellInfo"),
    ("Terrain/CIV4BonusInfos.xml", "BonusInfo"),
    ("Terrain/CIV4ImprovementInfos.xml", "ImprovementInfo"),
    ("Civilizations/CIV4CivilizationInfos.xml", "CivilizationInfo"),
]:
    for e in infos(path, item):
        DESC[txt(e, "Type")] = txt(e, "Description")

N = lambda t: name_of(t, DESC)  # noqa: E731

COMBAT = {
    "UNITCOMBAT_NAVAL": "海軍", "UNITCOMBAT_BEAST": "魔獣", "UNITCOMBAT_MELEE": "白兵",
    "UNITCOMBAT_ADEPT": "秘術", "UNITCOMBAT_DISCIPLE": "信奉", "UNITCOMBAT_RECON": "偵察",
    "UNITCOMBAT_MOUNTED": "騎乗", "UNITCOMBAT_ANIMAL": "動物", "UNITCOMBAT_ARCHER": "弓術",
    "UNITCOMBAT_SIEGE": "攻城兵器", "UNITCOMBAT_IDIOT": "無能",
}
YIELD = ["食料", "ハンマー", "商業"]
COMMERCE = ["ゴールド", "研究", "文化", "諜報"]
DOMAIN = {"DOMAIN_SEA": "海洋", "DOMAIN_LAND": "陸上"}

# ---- 固有ユニット・建造物の所属文明 ----
default_unit = {txt(e, "Type"): txt(e, "DefaultUnit") for e in infos("Units/CIV4UnitClassInfos.xml", "UnitClassInfo")}
default_bldg = {txt(e, "Type"): txt(e, "DefaultBuilding") for e in infos("Buildings/CIV4BuildingClassInfos.xml", "BuildingClassInfo")}
unit_civs, bldg_civs = defaultdict(list), defaultdict(list)
for c in infos("Civilizations/CIV4CivilizationInfos.xml", "CivilizationInfo"):
    cn = N(txt(c, "Type"))
    for u in c.iter("Unit"):
        if txt(u, "UnitType") not in ("", "NONE"):
            unit_civs[txt(u, "UnitType")].append(cn)
    for b in c.iter("Building"):
        if txt(b, "BuildingType") not in ("", "NONE"):
            bldg_civs[txt(b, "BuildingType")].append(cn)


def owner_note(type_, default_map, cls, civs):
    if default_map.get(cls) == type_:
        return ""
    if civs.get(type_):
        return f"（{'・'.join(sorted(set(civs[type_])))}）"
    return ""


def other_techs(e, list_tag):
    lst = e.find(list_tag)
    return [p.text.strip() for p in lst.iter("PrereqTech") if p.text and p.text.strip() not in ("", "NONE")] if lst is not None else []


UNLOCK = defaultdict(lambda: defaultdict(list))


def add_unlock(e, main_tag, kind, extra_list=None, note=""):
    t = txt(e, main_tag)
    extras = other_techs(e, extra_list) if extra_list else []
    techs = [x for x in [t] + extras if x not in ("", "NONE")]
    for tech in techs:
        others = [N(x) for x in techs if x != tech]
        s = N(txt(e, "Type")) + note
        if others:
            s += f"（{'・'.join(others)}も必要）"
        UNLOCK[tech][kind].append(s)


for e in infos("Units/CIV4UnitInfos.xml", "UnitInfo"):
    note = owner_note(txt(e, "Type"), default_unit, txt(e, "Class"), unit_civs)
    add_unlock(e, "PrereqTech", "ユニット", "TechTypes", note)
for e in infos("Buildings/CIV4BuildingInfos.xml", "BuildingInfo"):
    note = owner_note(txt(e, "Type"), default_bldg, txt(e, "BuildingClass"), bldg_civs)
    add_unlock(e, "PrereqTech", "建造物", "TechTypes", note)
for path, item, kind in [
    ("Gameinfo/CIV4CivicInfos.xml", "CivicInfo", "社会制度"),
    ("Gameinfo/CIV4ProjectInfo.xml", "ProjectInfo", "大儀式"),
    ("Units/CIV4PromotionInfos.xml", "PromotionInfo", "昇進"),
    ("Units/CIV4SpellInfos.xml", "SpellInfo", "呪文・技能"),
]:
    for e in infos(path, item):
        add_unlock(e, "TechPrereq", kind)
for e in load("Units/CIV4BuildInfos.xml").iter("BuildInfo"):
    add_unlock(e, "PrereqTech", "タイル整備・作業")

# 資源の発見・有効化、整備の産出変化
SPECIAL = defaultdict(list)
for e in infos("Terrain/CIV4BonusInfos.xml", "BonusInfo"):
    for tag, label in [("TechReveal", "資源の発見"), ("TechCityTrade", "資源の有効化")]:
        t = txt(e, tag)
        if t not in ("", "NONE"):
            SPECIAL[(t, label)].append(N(txt(e, "Type")))
    t = txt(e, "TechObsolete")
    if t not in ("", "NONE"):
        SPECIAL[(t, "資源の陳腐化")].append(N(txt(e, "Type")))
for e in infos("Terrain/CIV4ImprovementInfos.xml", "ImprovementInfo"):
    tyc = e.find("TechYieldChanges")
    if tyc is None:
        continue
    for ch in tyc.findall("TechYieldChange"):
        t = txt(ch, "PrereqTech")
        ys = [int(y.text) for y in ch.iter("iYield")]
        part = ", ".join(f"{v:+d}[{YIELD[i]}]" for i, v in enumerate(ys) if v)
        if t not in ("", "NONE") and part:
            SPECIAL[(t, "整備の産出")].append(f"{part}: {N(txt(e, 'Type'))}")
for e in infos("Buildings/CIV4BuildingInfos.xml", "BuildingInfo"):
    t = txt(e, "ObsoleteTech")
    if t not in ("", "NONE"):
        SPECIAL[(t, "陳腐化")].append(N(txt(e, "Type")))

# ---- テクノロジー本体 ----
techs = infos("Technologies/CIV4TechInfos.xml", "TechInfo")
LEADS = defaultdict(list)
for e in techs:
    for p in other_techs(e, "AndPreReqs") + other_techs(e, "OrPreReqs"):
        LEADS[p].append(txt(e, "Type"))

FLAG = {
    "bTechTrading": "テクノロジーの取引が可能", "bGoldTrading": "ゴールドの取引が可能",
    "bOpenBordersTrading": "相互通行条約が可能", "bDefensivePactTrading": "防衛協定が可能",
    "bPermanentAllianceTrading": "永久同盟が可能", "bVassalTrading": "属国が有効",
    "bMapTrading": "地図の取引が可能", "bBridgeBuilding": "橋の建設が可能",
    "bIrrigation": "灌漑が可能", "bIgnoreIrrigation": "灌漑なしで農場を建設可能",
    "bWaterWork": "水タイルに市民を配置できる", "bRiverTrade": "河川で交易路が可能",
    "bExtraWaterSeeFrom": "+1 水上視界", "bMapCentering": "世界地図を絶対座標化",
    "bMapVisible": "世界地図を獲得", "bTechBrokering": "テクノロジーの即時転売が可能",
    "bRepeat": "繰り返し研究可能",
}
TERRAIN_TRADE = {"TERRAIN_COAST": "近海で交易路が可能", "TERRAIN_OCEAN": "外洋で交易路が可能"}

ERA_ORDER = ["ERA_ANCIENT", "ERA_CLASSICAL", "ERA_MEDIEVAL", "ERA_FUTURE", "ERA_RELIGIOUS"]
out = [
    "# OAC/テクノロジー（0.57、XMLから生成）",
    "",
    "- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）",
    "- 生成元: Technologies/CIV4TechInfos.xml ほか（ユニット・建造物・社会制度・大儀式・昇進・呪文・整備・資源の各XML）",
    "- 注意: Pythonで実装された効果や、文明固有の別ルート（代替前提）は含まない。文明固有の要素は所属文明を括弧で示す（判別できたもののみ）。",
    "",
]
for era in ERA_ORDER:
    group = [e for e in techs if txt(e, "Era") == era]
    if not group:
        continue
    out += [f"## {N(era)}", ""]
    for e in sorted(group, key=lambda x: (int(txt(x, "iGridX", "0")), int(txt(x, "iGridY", "0")))):
        T = txt(e, "Type")
        out += [f"### {en(DESC[T])} - {N(T)}", "", f"- 内部名: `{T}`"]
        if txt(e, "bDisable") == "1":
            out.append("- 研究不可")
        else:
            out.append(f"- コスト: {txt(e, 'iCost')}[研究]")
        ands = [N(x) for x in other_techs(e, "AndPreReqs")]
        ors = [N(x) for x in other_techs(e, "OrPreReqs")]
        cond = " と ".join(ands)
        if ors:
            o = " または ".join(ors)
            cond = f"{cond} と ({o})" if cond and len(ors) > 1 else (f"{cond} と {o}" if cond else o)
        rel = txt(e, "PrereqReligion")
        if rel not in ("", "NONE"):
            cond += f" かつ [国教]{N(rel)}"
        out.append(f"- 必要条件: {cond or 'なし'}")
        if LEADS[T]:
            out.append(f"- 発展: {', '.join(N(x) for x in LEADS[T])}")
        for kind in ["建造物", "ユニット", "社会制度", "大儀式", "タイル整備・作業", "昇進", "呪文・技能"]:
            items = UNLOCK[T].get(kind)
            if items:
                out.append(f"- {kind}:")
                out += [f"  - {x}" for x in items]
        sp = []
        for tag, label in FLAG.items():
            if txt(e, tag) == "1":
                sp.append(label)
        for tt in e.iter("TerrainTrade"):
            if txt(tt, "bTerrainTrade") == "1":
                sp.append(TERRAIN_TRADE.get(txt(tt, "TerrainType"), txt(tt, "TerrainType")))
        for k, label in [("iTradeRoutes", "[交易路]交易路: すべての都市"), ("iHappiness", "[幸福]: すべての都市"), ("iHealth", "[衛生]: すべての都市")]:
            v = int(txt(e, k, "0"))
            if v:
                sp.append(f"{v:+d}{label}")
        ym = e.find("YieldModifiers")
        if ym is not None:
            for i, y in enumerate(ym.iter("iYield")):
                if int(y.text):
                    sp.append(f"{int(y.text):+d}%[{YIELD[i]}]: すべての都市")
        v = int(txt(e, "iCombatStrengthModifier", "0"))
        if v:
            sp.append(f"{v:+d}%[戦闘力]: 全てのユニット")
        for d in e.iter("DomainExtraMove"):
            sp.append(f"{int(txt(d, 'iExtraMoves')):+d}[移動力]: {DOMAIN.get(txt(d, 'DomainType'), txt(d, 'DomainType'))}ユニット")
        for p in e.iter("PioneerUnitCombatModifier"):
            sp.append(f"{int(txt(p, 'iCombatStrengthModifier')):+d}%[戦闘力]: {COMBAT.get(txt(p, 'UnitCombatType'), txt(p, 'UnitCombatType'))}ユニット (先駆者ボーナス)")
        for k, label in [("iPioneerForBelieverModifier", "[国教]国教を信仰するユニット"), ("iPioneerVsHeathenModifier", "対 異教徒ユニット")]:
            v = int(txt(e, k, "0"))
            if v:
                sp.append(f"{v:+d}%[戦闘力]: {label} (先駆者ボーナス)")
        for p in e.iter("UnitCombatFreePromotionPick"):
            sp.append(f"新規の{COMBAT.get(txt(p, 'UnitCombatType'), '')}ユニットに +{txt(p, 'iFreePromotionPick')} 無償の昇進")
        f1 = txt(e, "FirstFreeUnitClass")
        if f1 not in ("", "NONE"):
            sp.append(f"一番乗りで{N(f1)}を獲得")
        f2 = txt(e, "FreeUnitClass")
        if f2 not in ("", "NONE"):
            sp.append(f"{N(f2)}を獲得")
        if int(txt(e, "iFirstFreeTechs", "0")):
            sp.append("一番乗りで無償のテクノロジーを取得")
        for label in ["資源の発見", "資源の有効化", "資源の陳腐化", "整備の産出", "陳腐化"]:
            items = SPECIAL.get((T, label))
            if not items:
                continue
            if label == "整備の産出":
                sp += items
            else:
                sp.append(f"{label}: {', '.join(items)}")
        if sp:
            out.append("- 特殊能力:")
            out += [f"  - {x}" for x in sp]
        other = []
        if txt(e, "bTrade") != "1":
            other.append("外交取引不可")
        if txt(e, "bGoodyTech") != "1":
            other.append("部族集落からの取得不可")
        if other:
            out.append(f"- その他: {', '.join(other)}")
        out.append("")

open(OUT, "w", encoding="utf-8").write("\n".join(out))
print("techs:", len(techs), "text keys:", len(JA))
