#Spell system and FfH specific callout python functions
#All code by Kael, all bugs by woodelf

from CvPythonExtensions import *
import CvUtil
import Popup as PyPopup
import CvScreensInterface
import sys
import PyHelpers
import CustomFunctions
import ScenarioFunctions
##--------	Enums Cache: Added by Denev	--------##
import CvPythonEnums
en = CvPythonEnums.CvPythonEnums()
##--------	Enums Cache: End Add		--------##

PyInfo = PyHelpers.PyInfo
PyPlayer = PyHelpers.PyPlayer
gc = CyGlobalContext()
cf = CustomFunctions.CustomFunctions()
sf = ScenarioFunctions.ScenarioFunctions()

##--------	Advanced Rules: Modified by Denev 2009/11/21
g_leHellTerrains = [iTerrain for iTerrain in xrange(gc.getNumTerrainInfos()) if gc.getTerrainInfo(iTerrain).getTerrainDown() != TerrainTypes.NO_TERRAIN]
g_leManaTypes = [iBonus for iBonus in xrange(gc.getNumBonusInfos()) if gc.getBonusInfo(iBonus).getBonusClassType() == gc.getDefineINT('BONUSCLASS_MANA')]
g_leVessels = [	(gc.getInfoTypeForString('UNITCLASS_ARCANE_BARGE')		, 1),
				(gc.getInfoTypeForString('UNITCLASS_CARAVEL')			, 1),
				(gc.getInfoTypeForString('UNITCLASS_GALLEY')			, 1),
				(gc.getInfoTypeForString('UNITCLASS_FRIGATE')			, 2),
				(gc.getInfoTypeForString('UNITCLASS_GALLEON')			, 2),
				(gc.getInfoTypeForString('UNITCLASS_MAN_O_WAR')			, 3),
				(gc.getInfoTypeForString('UNITCLASS_PRIVATEER')			, 1),
				(gc.getInfoTypeForString('UNITCLASS_QUEEN_OF_THE_LINE')	, 3),
				(gc.getInfoTypeForString('UNITCLASS_TRIREME')			, 1)	]
g_dGameSpeedPercent = {	"GoldenAge" : gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getGoldenAgePercent(),
						"HurryConscriptAnger" : gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getHurryConscriptAngerPercent(),
						"VictoryDelay" : gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent()	}
##--------	Advanced Rules: End Modify

def reqAddToFleshGolem(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isImmortal():
		return ReasonTypes.REASON_DISABLED_IMMORTAL_NOT_ALLOWED
	if pCaster.isImmuneToMagic():
		return ReasonTypes.REASON_DISABLED_IMMUNE_TO_MAGIC
	return True

def spellAddToFleshGolem(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	leUntransferable = [en.ePromotionChanneling1,
						en.ePromotionChanneling2,
						en.ePromotionChanneling3,
						en.ePromotionDivine	]
	ePlayer = pCaster.getOwner()

	# search most promoted golem
	pFleshGolem = -1
	iBestCount = 0
	for iUnitIndex in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(iUnitIndex)
		if pUnit.getUnitClassType() == en.eUnitClassFleshGolem:
			if pUnit.getOwner() == ePlayer:
				liPromotions = [iPromotion for iPromotion in xrange(gc.getNumPromotionInfos()) if pUnit.isHasPromotion(iPromotion)]
				if pFleshGolem == -1 or len(liPromotions) > iBestCount:
					pFleshGolem = pUnit
					iBestCount = len(liPromotions)

	if pFleshGolem != -1:
##--------	Fractional Combat Strength: Modified by Denev	--------##
		'''
		if pCaster.baseCombatStr() > pFleshGolem.baseCombatStr():
			pFleshGolem.setBaseCombatStr(pFleshGolem.baseCombatStr() + 1)
		if pCaster.baseCombatStrDefense() > pFleshGolem.baseCombatStrDefense():
			pFleshGolem.setBaseCombatStrDefense(pFleshGolem.baseCombatStrDefense() + 1)
		'''
		# caster bare strength
		iWeaponExtraAttack = 0
		iWeaponExtraDefense = 0
		eWeapon = pCaster.getWeapon()
		if eWeapon != WeaponTypes.NO_WEAPON:
			eWeaponPromotion = gc.getWeaponInfo(eWeapon).getWeaponPromotion()
			if eWeaponPromotion != PromotionTypes.NO_PROMOTION:
				iWeaponExtraAttack = gc.getPromotionInfo(eWeaponPromotion).getExtraCombatStr()
				iWeaponExtraDefense = gc.getPromotionInfo(eWeaponPromotion).getExtraCombatDefense()

		iBareCombatAttackTimes100 = pCaster.getCombatAttackTimes100() - iWeaponExtraAttack * 100
		iBareCombatDefenseTimes100 = pCaster.getCombatDefenseTimes100() - iWeaponExtraDefense * 100

		# golem bare strength
		iWeaponExtraAttack = 0
		iWeaponExtraDefense = 0
		eWeapon = pFleshGolem.getWeapon()
		if eWeapon != WeaponTypes.NO_WEAPON:
			eWeaponPromotion = gc.getWeaponInfo(eWeapon).getWeaponPromotion()
			if eWeaponPromotion != PromotionTypes.NO_PROMOTION:
				iWeaponExtraAttack = gc.getPromotionInfo(eWeaponPromotion).getExtraCombatStr()
				iWeaponExtraDefense = gc.getPromotionInfo(eWeaponPromotion).getExtraCombatDefense()

		iGolemBareCombatAttackTimes100 = pFleshGolem.getCombatAttackTimes100() - iWeaponExtraAttack * 100
		iGolemBareCombatDefenseTimes100 = pFleshGolem.getCombatDefenseTimes100() - iWeaponExtraDefense * 100

		iChangeAttackTimes100 = min(max(iBareCombatAttackTimes100 - iGolemBareCombatAttackTimes100, 0), 100)
		iChangeDefenseTimes100 = min(max(iBareCombatDefenseTimes100 - iGolemBareCombatDefenseTimes100, 0), 100)

		pFleshGolem.changeCombatAttackTimes100(iChangeAttackTimes100)
		pFleshGolem.changeCombatDefenseTimes100(iChangeDefenseTimes100)
##--------	Fractional Combat Strength: End Modify		--------##
		for iPromotion in xrange(gc.getNumPromotionInfos()):
			if pCaster.isHasPromotion(iPromotion):
				if iPromotion not in leUntransferable:
					if not gc.getPromotionInfo(iPromotion).isRace() and not gc.getPromotionInfo(iPromotion).isEquipment():
						if gc.getPromotionInfo(iPromotion).getBonusPrereq() == BonusTypes.NO_BONUS:
							siPromotionPrereqs = set([	gc.getPromotionInfo(iPromotion).getPrereqPromotion(),
														gc.getPromotionInfo(iPromotion).getPrereqOrPromotion1(),
														gc.getPromotionInfo(iPromotion).getPrereqOrPromotion2(),
														gc.getPromotionInfo(iPromotion).getPromotionPrereqAnd(),
														gc.getPromotionInfo(iPromotion).getPromotionPrereqOr3(),
														gc.getPromotionInfo(iPromotion).getPromotionPrereqOr4()])
							if len(siPromotionPrereqs & set(leUntransferable)) == 0:
								pFleshGolem.setHasPromotion(iPromotion, True)
								if iPromotion == en.ePromotionGreatCommander:
									pFleshGolem.setName(pCaster.getNameKey().split(' (')[0])
##--------	Fractional Combat Strength: Modified by Denev	--------##
#		if pFleshGolem.baseCombatStr() >= 15:
		if pFleshGolem.getCombatAttackTimes100() >= 1500:
##--------	Fractional Combat Strength: End Modify		--------##
			if pCaster.isHuman():
				szTorophyKey = 'TROPHY_FEAT_FLESH_GOLEM_15'
				if not CyGame().isHasTrophy(szTorophyKey):
					CyGame().changeTrophyValue(szTorophyKey, 1)

def reqAddToWolfPack(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	eWolfPack = gc.getSpellInfo(eSpell).getUnitInStackPrereq()
	ePlayer = pCaster.getOwner()
	iCasterID = pCaster.getID()

	for iUnitIndex in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(iUnitIndex)
		if pUnit.getUnitType() == eWolfPack:
			if pUnit.getOwner() == ePlayer:
				if pUnit.getID() != iCasterID:
					if not pUnit.isHasPromotion(en.ePromotionEmpower5):
						return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellAddToWolfPack(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	eWolfPack = gc.getSpellInfo(eSpell).getUnitInStackPrereq()
	leEmpower = [	en.ePromotionEmpower5,
					en.ePromotionEmpower4,
					en.ePromotionEmpower3,
					en.ePromotionEmpower2,
					en.ePromotionEmpower1	]
	ePlayer = pCaster.getOwner()
	iCasterID = pCaster.getID()

	# search most empowered wolf pack
	lpTargetList = []
	for iUnitIndex in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(iUnitIndex)
		if pUnit.getUnitType() == eWolfPack:
			if pUnit.getOwner() == ePlayer:
				if pUnit.getID() != iCasterID:
					if not pUnit.isHasPromotion(leEmpower[0]):
						for iLoop, iEmpower in enumerate(leEmpower):
							if pUnit.isHasPromotion(iEmpower):
								lpTargetList.append((iLoop, pUnit))
								break
							else:
								lpTargetList.append((len(leEmpower), pUnit))
	lpTargetList.sort()
	iEmpowerIndex	= lpTargetList[0][0]
	pTarget			= lpTargetList[0][1]

	pTarget.setHasPromotion(leEmpower[iEmpowerIndex - 1], True)

def reqAnnexLair(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	eImprovement = pPlot.getImprovementType()

	if eImprovement == ImprovementTypes.NO_IMPROVEMENT:
		return False

	if gc.getImprovementInfo(pPlot.getImprovementType()).getPythonExplore() == "":
		return False

	if pPlot.isOwned():
		if pPlot.getOwner() != pCaster.getOwner():
			return ReasonTypes.REASON_DISABLED_IN_RIVAL_BORDER
	else:
		return ReasonTypes.REASON_DISABLED_OUT_OF_BORDER

	if pCaster.isDuration():
		return ReasonTypes.REASON_DISABLED_WITH_DURATION

	eLairBarbarian = gc.getImprovementInfo(pPlot.getImprovementType()).getSpawnBarbarianType()
	if eLairBarbarian == BarbarianTypes.NO_BARBARIAN:
		return False

	eLairPlayer = CyGame().getBarbarianPlayer(eLairBarbarian)
	if eLairPlayer == PlayerTypes.NO_PLAYER:
		return False

	eLairTeam = gc.getPlayer(eLairPlayer).getTeam()
	if gc.getTeam(eLairTeam).isAtWar(pCaster.getTeam()):
		return ReasonTypes.REASON_DISABLED_BARBARIAN_IS_ENEMY

	return True

def spellAnnexLair(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pPlot = pCaster.plot()
##--------	Unofficial Bug Fix: Modified by ent
#	pCity = CyMap().findCity(pPlot.getX(), pPlot.getY(), pCaster.getOwner(), TeamTypes.NO_TEAM, False, False, TeamTypes.NO_TEAM, DirectionTypes.NO_DIRECTION, pPlayer.getCity(-1))
	pCity = pPlot.getWorkingCity()
	if pCity.isNone() or pCity.getOwner() != pCaster.getOwner() or pCity.isSettlement():
		pCity = CyMap().findCity(pPlot.getX(), pPlot.getY(), pCaster.getOwner(), TeamTypes.NO_TEAM, False, False, TeamTypes.NO_TEAM, DirectionTypes.NO_DIRECTION, pCity)
##--------	Unofficial Bug Fix: End Modify

	if not pCity.isNone():
		pCity.changePopulation(1)
		pPoint = pCity.plot().getPoint()
		CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_CREATION'), pPoint)
	else:
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_AXEMAN'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit.finishMoves()

	lpUnits = [pPlot.getUnit(iUnitIndex) for iUnitIndex in xrange(pPlot.getNumUnits())]

	pImprovementInfo = gc.getImprovementInfo(pPlot.getImprovementType())
	eBarbarianPlayer = pImprovementInfo.getSpawnBarbarianType() + gc.getBARBARIAN_PLAYER()
	for pUnit in lpUnits:
		if pUnit.getOwner() == eBarbarianPlayer:
			if pUnit.getUnitType() in (pImprovementInfo.getSpawnUnitType(), pImprovementInfo.getInitialSpawnUnitType()):
				pNewUnit = pPlayer.initSkeletalUnit(pUnit.getUnitType(), pUnit.getX(), pUnit.getY(), pUnit.getUnitAIType());
				pNewUnit.convert(pUnit)
				pNewUnit.finishMoves()
	pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)

def reqArcaneLacuna(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	iCount = 0
	for iBonus in g_leManaTypes:
		iCount += CyMap().getNumBonuses(iBonus)
	if iCount == 0:
		return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

	if not pCaster.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		if not pTeam.isHasTech(en.eTechSorcery):
			return False
		if pTeam.getAtWarCount(True) == 0:
			return False
	return True

def spellArcaneLacuna(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iCount = 0
	for iBonus in g_leManaTypes:
		iCount += CyMap().getNumBonuses(iBonus)

	for pUnit in PyPlayer(pCaster.getOwner()).getUnitList():
		if pUnit.getUnitCombatType() == en.eUnitCombatAdept:
			pUnit.changeExperience(iCount, -1, False, False, False)

	iDelay = cyFlatValue(20, g_dGameSpeedPercent["GoldenAge"], True)

	eTeam = gc.getPlayer(pCaster.getOwner()).getTeam()
	for eLoopPlayer in xrange(gc.getMAX_PLAYERS()):
		pLoopPlayer = gc.getPlayer(eLoopPlayer)
		if pLoopPlayer.isAlive():
			if pLoopPlayer.getTeam() != eTeam:
				pLoopPlayer.changeDisableSpellcasting(iDelay)

def reqArdor(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getGreatPeopleCreated() == 0:
		return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET
	if not pPlayer.isHuman():
		if pPlayer.getGreatPeopleCreated() < 5:
			return False
	return True

def spellArdor(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pPlayer.setGreatPeopleCreated(0)
	pPlayer.setGreatPeopleThresholdModifier(0)

def reqArenaBattle(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.getUnitCombatType() == en.eUnitCombatMelee:
		return True
	if pCaster.getUnitCombatType() == en.eUnitCombatRecon:
		return True
	if pCaster.getUnitClassType() == en.eUnitClassSlave:
		return True
	return ReasonTypes.REASON_DISABLED_INVALID_KIND_OF_UNIT

def spellArenaBattle(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pCaster.plot().getPlotCity()
	iTimer = cyFlatValue(3, g_dGameSpeedPercent["VictoryDelay"], True)
	pCity.changeHappinessTimer(iTimer)
	szButton = gc.getBuildingInfo(gc.getSpellInfo(eSpell).getBuildingPrereq()).getButton()

	iOddsModifier = (pCaster.currHitPoints() * 100) // pCaster.maxHitPoints()
	iOdds = min(90, 45 + pCaster.getLevel() * 5)
	iOdds = (iOdds * iOddsModifier) // 100
	if CyGame().getSorenRandNum(100, "Arena Battle") < iOdds:
		iRnd = CyGame().getSorenRandNum(6, 'Arena Battle') + 1
		pCaster.changeExperience(iRnd, -1, False, False, False)
		iNewDamage = min(pCaster.maxHitPoints() - 1, pCaster.getDamage() + (pCaster.currHitPoints() * iRnd) // 7)
		pCaster.setDamage(iNewDamage, pCity.getOwner())
		szSound = gc.getEraInfo(CyGame().getCurrentEra()).getAudioUnitVictoryScript()
		CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_ARENA_WIN', ()), szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCaster.getX(), pCaster.getY(), True, True)
		if pCaster.getUnitClassType() == en.eUnitClassSlave:
			pPlayer = gc.getPlayer(pCaster.getOwner())
			pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_WARRIOR'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit.convert(pCaster)
			pNewUnit.finishMoves()
	else:
		szSound = gc.getEraInfo(CyGame().getCurrentEra()).getAudioUnitDefeatScript()
		CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_ARENA_LOSE', ()), szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCaster.getX(), pCaster.getY(), True, True)
		pCaster.kill(True, PlayerTypes.NO_PLAYER)

def reqCallBlizzard(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pPlot.isSpellDetectable(pCaster.getTeam()):
		return ReasonTypes.REASON_DISABLED_PLOT_OUT_OF_SIGHT
# Kaijin OAC >>>
	"""
	iBlizzard = en.eFeatureBlizzard
	if pPlot.getFeatureType() == iBlizzard:
		return False
	if pPlot.getFeatureType() == en.eFeatureForestAncient:
		return ReasonTypes.REASON_DISABLED_IMMUNE_TO_BLIZZARD

	iRange = pCaster.getSpellRange(eSpell)
	lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, True, pCaster.getTeam())

	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.getFeatureType() == iBlizzard:
			return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET
	"""
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, True)

	bHuman = (pCaster.isHuman())
	ePlayer = pCaster.getOwner()
	bBlizzard = False
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.isCity():
			continue
		if pTargetPlot.getFeatureType() == FeatureTypes.NO_FEATURE:
			bBlizzard = True
			if not bHuman:
				if pTargetPlot.isOwned() and pTargetPlot.getOwner() == ePlayer:
					if not pTargetPlot.getTerrainType() in (en.eTerrainSnow, en.eTerrainTundra):
						return False
			if pTargetPlot.isOwned() and pTargetPlot.getOwner() != ePlayer:
				if not gc.getTeam(pCaster.getTeam()).isAtWar(pTargetPlot.getTeam()):
					return False

	if bBlizzard:
		return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET
# Kaijin OAC <<<

def spellCallBlizzard(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iBlizzard = en.eFeatureBlizzard

	pPlot = pCaster.plot()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)

# Kaijin OAC >>>
	"""
	lpBlizzardPlot = []
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.getFeatureType() == iBlizzard:
			lpBlizzardPlot.append(pTargetPlot)

	if len(lpBlizzardPlot) > 0:
		pBlizzardPlot = lpBlizzardPlot[CyGame().getSorenRandNum(len(lpBlizzardPlot), 'Select blizzard plot')]
		pBlizzardPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)

	pPlot.setFeatureType(iBlizzard, 0)
	liAlterableTerrains = [	gc.getInfoTypeForString('TERRAIN_GRASS'),
							gc.getInfoTypeForString('TERRAIN_PLAINS'),
							gc.getInfoTypeForString('TERRAIN_MARSH'),
							gc.getInfoTypeForString('TERRAIN_DESERT')	]
	if pPlot.getOriginalTerrainType() in liAlterableTerrains:
		if pPlot.getColdCounter() < 7500:
			pPlot.changeColdCounter(7500 - pPlot.getColdCounter(), 500)
	pPlot.ceilColdCounter(4500, 500)
	"""
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.isCity():
			continue
		if pTargetPlot.getFeatureType() == FeatureTypes.NO_FEATURE:
			pTargetPlot.setFeatureType(iBlizzard, 0)
			pTargetPlot.ceilColdCounter(4500, 500)
# Kaijin OAC <<<

def disabledSever(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		if pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_HIDDEN')):
			return True
		if pCaster.getUnitAIType() != UnitAITypes.UNITAI_EXPLORE:
			return True
	return False

def reqCallForm(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pPlot.isSpellDetectable(pCaster.getTeam()):
		return ReasonTypes.REASON_DISABLED_PLOT_OUT_OF_SIGHT
	if pCaster.getSummoner() == -1:
		return ReasonTypes.REASON_DISABLED_BODY_HAS_LOST
	pPlayer = gc.getPlayer(pCaster.getOwner())
	pUnit = pPlayer.getUnit(pCaster.getSummoner())
	if not pUnit.canMoveInto(pPlot, False, False, False):
		return ReasonTypes.REASON_DISABLED_BODY_CAN_NOT_MOVE_INTO
	return True

def spellCallForm(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pUnit = pPlayer.getUnit(pCaster.getSummoner())
	pPlot = pCaster.plot()
	pUnit.setXY(pPlot.getX(), pPlot.getY(), False, True, True)

def enabledCallOfTheGrave(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, True)
	for pTargetPlot in lpRangedPlots:
		eImprovement = pTargetPlot.getRevealedImprovementType(pCaster.getTeam(), False)
		if eImprovement == en.eImprovementGraveyard:
			return True
#	for iIndex in xrange(gc.getSpellInfo(eSpell).getNumSecondarySpells()):
#		eLoopSecondarySpell = gc.getSpellInfo(eSpell).getSecondarySpell(iIndex)
#		lpRangedUnits = cyGetSpellRangedUnits(pCaster, eLoopSecondarySpell, pPlot, False, True)
#		if len(lpRangedUnits) > 0:
#			return True
	return False

def spellCallOfTheGrave(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.getImprovementType() == en.eImprovementGraveyard:
			customSummonSpellData = CvCustomSummonSpellData()
			customSummonSpellData.eUnit = gc.getSpellInfo(eSpell).getCreateUnitType()
			customSummonSpellData.iNumUnits = 3
			customSummonSpellData.iSummoningPlotIndex = CyMap().plotNum(pTargetPlot.getX(), pTargetPlot.getY())
			customSummonSpellData.eEffect = gc.getInfoTypeForString('EFFECT_WRAITH_SUMMON')
			customSummonSpellData.szSound = 'AS3D_SPELL_WRAITH'
			pCaster.castCustomSummon(customSummonSpellData)
			pTargetPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)

def disabledCommanderJoin(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.canFight():
		return ReasonTypes.REASON_DISABLED_CAN_NOT_FIGHT
#	if isWorldUnitClass(pCaster.getUnitClassType()):
#		return ReasonTypes.REASON_DISABLED_WORLDUNIT_NOT_ALLOWED
	if not pCaster.isHuman():
##--------	Fractional Combat Strength: Modified by Denev	--------##
#		if pCaster.baseCombatStr() <= 5:
		if pCaster.getCombatAttackTimes100() <= 500:
##--------	Fractional Combat Strength: End Modify		--------##
			return True
# Kaijin >>> for Lineage
		if pCaster.getCivilizationType() == en.eCivilizationLineage:
			return True
# Kaijin <<<
	return False

def spellCommanderJoin(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	iCommander = gc.getInfoTypeForString('UNITCLASS_COMMANDER')
	ePlayer = pCaster.getOwner()
	pCommander = None
	for iUnitIndex in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(iUnitIndex)
		if pUnit.getOwner() == ePlayer and pUnit.getUnitClassType() == iCommander:
			pCommander = pUnit
##--------	Advanced Rules: Added by Denev 2010/07/05
			break
##--------	Advanced Rules: End Add
	if pCommander is not None:
##--------	Advanced Rules: Added by Denev 2010/07/05
		pCaster.setName(pCommander.getNameNoDesc())
		pCaster.setLeaderUnitType(pCommander.getUnitType())
##--------	Advanced Rules: End Add
		pCommander.setHasPromotion(en.eRaceGolem, True)
		pCommander.kill(False, PlayerTypes.NO_PLAYER)

def spellCommanderJoinDecius(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	iDecius = gc.getInfoTypeForString('UNIT_DECIUS')
	ePlayer = pCaster.getOwner()
	pCommander = None
	for iUnitIndex in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(iUnitIndex)
		if pUnit.getOwner() == ePlayer and pUnit.getUnitType() == iDecius:
			pCommander = pUnit
##--------	Advanced Rules: Added by Denev 2010/07/05
			break
##--------	Advanced Rules: End Add
	if pCommander is not None:
		pCaster.setScenarioCounter(iDecius)
##--------	Advanced Rules: Added by Denev 2010/07/05
#		pCaster.setName(pCommander.getNameKey().split(' (')[0])
		pCaster.setLeaderUnitType(pCommander.getUnitType())
##--------	Advanced Rules: End Add
		pCommander.setHasPromotion(en.eRaceGolem, True)
		pCommander.kill(False, PlayerTypes.NO_PLAYER)

def spellCommanderSplit(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	iCommander = gc.getInfoTypeForString('UNIT_COMMANDER')
	if pCaster.getScenarioCounter() == gc.getInfoTypeForString('UNIT_DECIUS'):
		iCommander = gc.getInfoTypeForString('UNIT_DECIUS')
		pCaster.setScenarioCounter(-1)
	pNewUnit = pPlayer.initUnit(iCommander, pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.finishMoves()
##--------	Advanced Rules: Added by Denev 2010/07/05
	if iCommander == gc.getInfoTypeForString('UNIT_COMMANDER'):
		pNewUnit.setName(pCaster.getNameNoDesc())
		pCaster.setName('')
		pCaster.setLeaderUnitType(UnitTypes.NO_UNIT)
##--------	Advanced Rules: End Add

def reqConvertCityBasium(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	if pCity.getOwner() == pCaster.getOwner():
		return ReasonTypes.REASON_DISABLED_IMMUNE_OWN_CITY
	return True

def spellConvertCityBasium(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pCaster.plot().getPlotCity()
	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	pPlayer.acquireCity(pCity, False, False)
	pCity = pCaster.plot().getPlotCity()
	iCulture = 300
	iCulture *= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(CyGame().getGameSpeedType())
	iCulture /= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(en.eGameSpeedNormal)
	pCity.changeCulture(iPlayer, iCulture, True)

def reqConvertCityRantine(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	if pCity.getOwner() == pCaster.getOwner():
		return ReasonTypes.REASON_DISABLED_IMMUNE_OWN_CITY
	elif pCity.getTeam() == pCaster.getTeam():
		return ReasonTypes.REASON_DISABLED_IMMUNE_FRIENDLY_CITY
	elif pCity.getOwner() != gc.getBARBARIAN_PLAYER():
		return ReasonTypes.REASON_DISABLED_IN_RIVAL_BORDER
##--------	Fractional Combat Strength: Modified by Denev	--------##
	iCasterStrengthTimes100 = pCaster.getCombatAttackTimes100() + pCaster.getCombatDefenseTimes100()
##--------	Fractional Combat Strength: End Modify		--------##
	eDomain = pCaster.getDomainType()
	for iUnitIndex in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(iUnitIndex)
		if pUnit.getOwner() == gc.getBARBARIAN_PLAYER():
##--------	Unofficial Bug Fix: Added by Denev	--------##
			if pUnit.getDomainType() != eDomain:
				continue
##--------	Unofficial Bug Fix: End Add			--------##
##--------	Fractional Combat Strength: Modified by Denev	--------##
#			if pUnit.baseCombatStr() + pUnit.baseCombatStrDefense() >= pCaster.baseCombatStr() + pCaster.baseCombatStrDefense():
			if pUnit.getCombatAttackTimes100() + pUnit.getCombatDefenseTimes100() >= iCasterStrengthTimes100:
##--------	Fractional Combat Strength: End Modify		--------##
				return ReasonTypes.REASON_DISABLED_NOT_STRONGEST
	return True

def spellConvertCityRantine(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())

	eHero = en.ePromotionHero
	eOrc = en.eRaceOrc
	eGoblin = en.eRaceGoblin
	eCityOwner = pCity.getOwner()

	for iUnitIndex in xrange(pPlot.getNumUnits(), 0, -1):
		pUnit = pPlot.getUnit(iUnitIndex - 1)
		if pUnit.getOwner() == eCityOwner:
			if pUnit.getUnitAIType() == UnitAITypes.UNITAI_CITY_DEFENSE:
				if pUnit.getRace() in (eOrc, eGoblin) and not pUnit.isHasPromotion(eHero):
					pNewUnit = pPlayer.initUnit(pUnit.getUnitType(), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
					pNewUnit.convert(pUnit)
	pPlayer.acquireCity(pCity, False, True)

# ent >>>
def disabledCreateBatteringRam(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pPlot.isOwned():
		if pPlot.getTeam() != pCaster.getTeam() and not gc.getTeam(pCaster.getTeam()).isAtWar(pPlot.getTeam()):
			return ReasonTypes.REASON_DISABLED_IN_RIVAL_BORDER

	if not pCaster.isHuman():
		if pPlot.getImprovementType() == en.eImprovementSmoke:
			return False
		if pPlot.isOwned():
			if pPlot.getOwner() == pCaster.getOwner():
				return True
			else:
				return False
		if pCaster.getUnitAIType() != UnitAITypes.UNITAI_ATTACK_CITY:
			return True
	return False
# ent <<<
def spellCreateBatteringRam(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]
	liSummonedUnitIDs = argsList[3]

	pPlot = pCaster.plot()
	pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)

# Kaijin >>>	patch29 expansion - Start -
"""
def disabledCreateDenBear(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_LAIRS):
		return ReasonTypes.REASON_DISABLED_GAMEOPTION_DISABLE_LAIRS

	iX = pPlot.getX()
	iY = pPlot.getY()
	iBearDen = gc.getSpellInfo(eSpell).getCreateImprovementType()

	if pCaster.getDamage() > 0:
		return ReasonTypes.REASON_DISABLED_INJURED

	if pPlot.isOwned():
		return ReasonTypes.REASON_DISABLED_IN_BORDER

	if iX == pCaster.plot().getX() and iY == pCaster.plot().getY():
		# test castability on actual pCaster's plot
		if pPlot.getNumUnits() != 1:
			return ReasonTypes.REASON_DISABLED_NOT_ALONE
	else:
		# test castability on other plot
		if pPlot.getNumUnits() != 0 or pCaster.getGroup().getNumUnits() != 1:
			return ReasonTypes.REASON_DISABLED_NOT_ALONE

	iRange = 4
	lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, False, TeamTypes.NO_TEAM)
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.getImprovementType() == iBearDen:
			return ReasonTypes.REASON_DISABLED_TOO_CLOSE_SAME_IMPROVEMENT
	return False

def spellCreateDenBear(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	iUnit = pCaster.getUnitType()
	iAnimalPlayer = cf.getCivilization(en.eCivilizationAnimal)
	if pCaster.getOwner() != iAnimalPlayer:
		bSuccess = pCaster.jumpToNearestValidPlot()
		if bSuccess:
			pPlayer = gc.getPlayer(iAnimalPlayer)
			pNewUnit = pPlayer.initUnit(iUnit, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit.convert(pCaster)
			pNewUnit.finishMoves()

def disabledCreateDenLion(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_LAIRS):
		return ReasonTypes.REASON_DISABLED_GAMEOPTION_DISABLE_LAIRS

	iX = pPlot.getX()
	iY = pPlot.getY()
	iLionDen = gc.getSpellInfo(eSpell).getCreateImprovementType()

	if pCaster.getDamage() > 0:
		return ReasonTypes.REASON_DISABLED_INJURED

	if pPlot.isOwned():
		return ReasonTypes.REASON_DISABLED_IN_BORDER

	if iX == pCaster.plot().getX() and iY == pCaster.plot().getY():
		# test castability on actual pCaster's plot
		if pPlot.getNumUnits() != 1:
			return ReasonTypes.REASON_DISABLED_NOT_ALONE
	else:
		# test castability on other plot
		if pPlot.getNumUnits() != 0 or pCaster.getGroup().getNumUnits() != 1:
			return ReasonTypes.REASON_DISABLED_NOT_ALONE

	iRange = 4
	lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, False, TeamTypes.NO_TEAM)
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.getImprovementType() == iLionDen:
			return ReasonTypes.REASON_DISABLED_TOO_CLOSE_SAME_IMPROVEMENT
	return False

def spellCreateDenLion(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	iUnit = pCaster.getUnitType()
	iAnimalPlayer = cf.getCivilization(en.eCivilizationAnimal)
	if pCaster.getOwner() != iAnimalPlayer:
		bSuccess = pCaster.jumpToNearestValidPlot()
		if bSuccess:
			pPlayer = gc.getPlayer(iAnimalPlayer)
			pNewUnit = pPlayer.initUnit(iUnit, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit.convert(pCaster)
			pNewUnit.finishMoves()
"""

def disabledCreateDen(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_LAIRS):
		return ReasonTypes.REASON_DISABLED_GAMEOPTION_DISABLE_LAIRS

	iX = pPlot.getX()
	iY = pPlot.getY()
	iDen = gc.getSpellInfo(eSpell).getCreateImprovementType()

	if pCaster.getDamage() > 0:
		return ReasonTypes.REASON_DISABLED_INJURED

	if pPlot.isOwned():
		return ReasonTypes.REASON_DISABLED_IN_BORDER

	if iX == pCaster.plot().getX() and iY == pCaster.plot().getY():
		# test castability on actual pCaster's plot
		if pPlot.getNumUnits() != 1:
			return ReasonTypes.REASON_DISABLED_NOT_ALONE
	else:
		# test castability on other plot
		if pPlot.getNumUnits() != 0 or pCaster.getGroup().getNumUnits() != 1:
			return ReasonTypes.REASON_DISABLED_NOT_ALONE

	iRange = 4
	lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, False, TeamTypes.NO_TEAM)
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.getImprovementType() == iDen:
			return ReasonTypes.REASON_DISABLED_TOO_CLOSE_SAME_IMPROVEMENT
	return False

def spellCreateDen(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	iUnit = pCaster.getUnitType()
	iAnimalPlayer = cf.getCivilization(en.eCivilizationAnimal)
	if pCaster.getOwner() != iAnimalPlayer:
		bSuccess = pCaster.jumpToNearestValidPlot()
		if bSuccess:
			pPlayer = gc.getPlayer(iAnimalPlayer)
			pNewUnit = pPlayer.initUnit(iUnit, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit.convert(pCaster)
			pNewUnit.finishMoves()
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WILDANIMAL'), True)
# Kaijin <<<	patch29 expansion - End -

def disabledCrewBuccaneers(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

# Bug Fix >>>
	if pCaster.hasCargo():
		lpPromotionChanges = [	(gc.getInfoTypeForString('PROMOTION_SKELETON_CREW')	, False),
								(gc.getInfoTypeForString('PROMOTION_LONGSHOREMEN')	, False),
								(gc.getInfoTypeForString('PROMOTION_BUCCANEERS')	, True)	]
		iCargoChange = 0
		for ePromotion, bChange in lpPromotionChanges:
			if bChange and not pCaster.isHasPromotion(ePromotion):
				iCargoChange += gc.getPromotionInfo(ePromotion).getCargoChange()
			if not bChange and pCaster.isHasPromotion(ePromotion):
				iCargoChange -= gc.getPromotionInfo(ePromotion).getCargoChange()
		if iCargoChange < 0:
			if pCaster.cargoSpaceAvailable(pCaster.specialCargo(), pCaster.domainCargo()) + iCargoChange < 0:
				return ReasonTypes.REASON_DISABLED_ALREADY_BUFFED
# Bug Fix <<<
	if pCaster.maxMoves() <= 1:
		return True
	if not pCaster.canFight():
		return ReasonTypes.REASON_DISABLED_CAN_NOT_FIGHT
	return False

def disabledCrewLongshoremen(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

# Bug Fix >>>
#	if pCaster.cargoSpaceAvailable(pCaster.specialCargo(), pCaster.domainCargo()) == 0:
	if pCaster.hasCargo():
		lpPromotionChanges = [	(gc.getInfoTypeForString('PROMOTION_SKELETON_CREW')	, False),
								(gc.getInfoTypeForString('PROMOTION_LONGSHOREMEN')	, True),
								(gc.getInfoTypeForString('PROMOTION_BUCCANEERS')	, False)	]
		iCargoChange = 0
		for ePromotion, bChange in lpPromotionChanges:
			if bChange and not pCaster.isHasPromotion(ePromotion):
				iCargoChange += gc.getPromotionInfo(ePromotion).getCargoChange()
			if not bChange and pCaster.isHasPromotion(ePromotion):
				iCargoChange -= gc.getPromotionInfo(ePromotion).getCargoChange()
		if iCargoChange < 0:
			if pCaster.cargoSpaceAvailable(pCaster.specialCargo(), pCaster.domainCargo()) + iCargoChange < 0:
				return ReasonTypes.REASON_DISABLED_ALREADY_BUFFED
# Bug Fix <<<
	if not pCaster.canFight():
		return ReasonTypes.REASON_DISABLED_CAN_NOT_FIGHT
	return False

def disabledCrewNormalCrew(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

# Bug Fix >>>
	if pCaster.hasCargo():
		lpPromotionChanges = [	(gc.getInfoTypeForString('PROMOTION_SKELETON_CREW')	, False),
								(gc.getInfoTypeForString('PROMOTION_LONGSHOREMEN')	, False),
								(gc.getInfoTypeForString('PROMOTION_BUCCANEERS')	, False)	]
		iCargoChange = 0
		for ePromotion, bChange in lpPromotionChanges:
			if bChange and not pCaster.isHasPromotion(ePromotion):
				iCargoChange += gc.getPromotionInfo(ePromotion).getCargoChange()
			if not bChange and pCaster.isHasPromotion(ePromotion):
				iCargoChange -= gc.getPromotionInfo(ePromotion).getCargoChange()
		if iCargoChange < 0:
			if pCaster.cargoSpaceAvailable(pCaster.specialCargo(), pCaster.domainCargo()) + iCargoChange < 0:
				return ReasonTypes.REASON_DISABLED_ALREADY_BUFFED
# Bug Fix <<<
	if not pCaster.canFight():
		return ReasonTypes.REASON_DISABLED_CAN_NOT_FIGHT
	return False

def disabledCrewSkeletonCrew(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

# Bug Fix >>>
	if pCaster.hasCargo():
		lpPromotionChanges = [	(gc.getInfoTypeForString('PROMOTION_SKELETON_CREW')	, True),
								(gc.getInfoTypeForString('PROMOTION_LONGSHOREMEN')	, False),
								(gc.getInfoTypeForString('PROMOTION_BUCCANEERS')	, False)	]
		iCargoChange = 0
		for ePromotion, bChange in lpPromotionChanges:
			if bChange and not pCaster.isHasPromotion(ePromotion):
				iCargoChange += gc.getPromotionInfo(ePromotion).getCargoChange()
			if not bChange and pCaster.isHasPromotion(ePromotion):
				iCargoChange -= gc.getPromotionInfo(ePromotion).getCargoChange()
		if iCargoChange < 0:
			if pCaster.cargoSpaceAvailable(pCaster.specialCargo(), pCaster.domainCargo()) + iCargoChange < 0:
				return ReasonTypes.REASON_DISABLED_ALREADY_BUFFED
# Bug Fix <<<
	if not pCaster.canFight():
		return ReasonTypes.REASON_DISABLED_CAN_NOT_FIGHT
	return False

# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
def effectCrownOfBrillance(argsList):
	pCaster = argsList[0]
	pCaster.cast(gc.getInfoTypeForString('SPELL_CROWN_OF_BRILLANCE_PER_TURN'))
"""
# Kaijin <<< End

def reqDeclareNationality(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

##--------	Unofficial Bug Fix: Added by Denev	--------##
	if gc.getUnitInfo(pCaster.getUnitType()).isHiddenNationality():
		return False
	if pCaster.hasCargo():
		return False
##--------	Unofficial Bug Fix: End Add			--------##
	if not pCaster.isHuman():
		if pCaster.getUnitAIType() in (UnitAITypes.UNITAI_PIRATE_SEA, UnitAITypes.UNITAI_ANIMAL):
			return False
		if pCaster.isHasPromotion(en.ePromotionHidden) or pCaster.isHasPromotion(en.ePromotionInvisible):
			return False
		if pCaster.isBarbarian():
			return False
	return True

# Kaijin >>> for Refined Mana and Sealed
def spellDispelMagic(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)

	eTeam = pCaster.getTeam()
	for pUnit in lpRangedUnits:
		if pUnit.getTeam() == eTeam:
			if not pUnit.isHasPromotion(en.ePromotionSealed):
				 if pUnit.getUncastableTimer() > 0:
					pUnit.setUncastableTimer(0)

def disabledDispelMagic(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	eBonus = pPlot.getBonusType(TeamTypes.NO_TEAM)

	if pPlot.getImprovementType() != ImprovementTypes.NO_IMPROVEMENT:
		eUpgradesTo = gc.getImprovementInfo(pPlot.getImprovementType()).getImprovementUpgrade()
		if eUpgradesTo != ImprovementTypes.NO_IMPROVEMENT:
			if gc.getImprovementInfo(eUpgradesTo).isUnique():
				return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET


	if not pCaster.isHuman():
		if pCaster.getUnitType() in (gc.getInfoTypeForString('UNIT_ADEPTUS'), gc.getInfoTypeForString('UNIT_TECHPRIEST')):
			if eBonus == gc.getInfoTypeForString('BONUS_REFINED_MANA'):
				return True
	return False

# Kaijin <<<
# ent >>>
"""
def reqDisrupt(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	if pCaster.getTeam() == pCity.getTeam():
		return ReasonTypes.REASON_DISABLED_IMMUNE_FRIENDLY_CITY
	if pCity.isDisorder():
		return ReasonTypes.REASON_DISABLED_CITY_IS_REVOLTING

	if not pCaster.isHuman():
		if pCity.getCulture(pCity.getOwner()) > 0:
			return False
	return True

def spellDisrupt(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()

	iCasterPlayer = pCaster.getOwner()
	iTargetPlayer = pCity.getOwner()
	pCasterPlayer = gc.getPlayer(iCasterPlayer)
	pTargetPlayer = gc.getPlayer(iTargetPlayer)

	iAngerTimer = cyFlatValue(2, g_dGameSpeedPercent["HurryConscriptAnger"], True)
	pCity.changeHurryAngerTimer(iAngerTimer)
	iNewCulture = max(0, pCity.getCulture(iTargetPlayer) - CyGame().getSorenRandNum(3, 'Disrupt'))
	pCity.setCulture(iTargetPlayer, iNewCulture, True)

	szButton = gc.getSpellInfo(gc.getInfoTypeForString('SPELL_DISRUPT')).getButton()
	szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_DISRUPT_ENEMY',(pCaster.getNameKey(), pTargetPlayer.getCivilizationAdjectiveKey(), pCity.getNameKey()))
	CyInterface().addMessage(iCasterPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
	szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_DISRUPT',(pCaster.getNameKey(), pCity.getNameKey()))
	CyInterface().addMessage(iTargetPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCity.getX(), pCity.getY(), True, True)

	if pCity.getCulture(iTargetPlayer) == 0:
		pCasterPlayer.acquireCity(pCity, False, False)
		pTargetPlayer.AI_changeAttitudeExtra(iCasterPlayer, -4)

		szMessage = CyTranslator().getText('TXT_KEY_MISC_CITY_REVOLTED_JOINED',(pCity.getNameKey(), pCasterPlayer.getCivilizationAdjectiveKey()))
		CyInterface().addMessage(iCasterPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
		szMessage = CyTranslator().getText('TXT_KEY_MISC_CITY_REVOLTED_JOINED',(pCity.getNameKey(), pCasterPlayer.getCivilizationAdjectiveKey()))
		CyInterface().addMessage(iTargetPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCity.getX(), pCity.getY(), True, True)
"""
def reqDisrupt(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	if pCaster.getTeam() == pCity.getTeam():
		return ReasonTypes.REASON_DISABLED_IMMUNE_FRIENDLY_CITY
	if pCity.isDisorder():
		return ReasonTypes.REASON_DISABLED_CITY_IS_REVOLTING

	eCasterPlayer = pCaster.getOwner()
	if not pPlot.isWithinCultureRange(eCasterPlayer):
		return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET
	if pCity.getHappinessTimer() > 0:
		return ReasonTypes.REASON_DISABLED_ALREADY_BUFFED

	if not pCaster.isHuman():
		if pCity.cultureStrength(eCasterPlayer) <= pCity.cultureGarrison(eCasterPlayer):
			return False

	return True

def spellDisrupt(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()

	eCasterPlayer = pCaster.getOwner()
	eCityOwner = pCity.getOwner()

	if pPlot.isWithinCultureRange(eCasterPlayer):
		if not pCity.doInstantRevolt(eCasterPlayer, False):
			iAngerTimer = cyFlatValue(2, g_dGameSpeedPercent["HurryConscriptAnger"], True)
			pCity.changeHurryAngerTimer(iAngerTimer)
		pPlayer = gc.getPlayer(eCasterPlayer)
		if pPlayer.getNumCities() > 0:
			pCapitalCity = pPlayer.getCapitalCity()
			if pCapitalCity.isNone():
				pCapitalCity, iterOut = pPlayer.firstCity(False)
			if not pCapitalCity.isNone():
				pCaster.setXY(pCapitalCity.getX(), pCapitalCity.getY(), False, True, True)
# ent <<<

def reqDivineRetribution(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
# ent >>>
		"""
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) < 2:
			return False
		"""
		pTeam = gc.getTeam(pCaster.getTeam())
		eUnitClassHyborem = gc.getInfoTypeForString('UNITCLASS_HYBOREM')
		if CyGame().isUnitClassMaxedOut(eUnitClassHyborem, 0):
			for eLoopPlayer in xrange(gc.getMAX_PLAYERS()):
				pLoopPlayer = gc.getPlayer(eLoopPlayer)
				if pLoopPlayer.getUnitClassCount(eUnitClassHyborem) > 0:
					py = PyPlayer(eLoopPlayer)
					pHyborem = None

					for pUnit in py.getUnitList():
						if pUnit.getUnitClassType() == eUnitClassHyborem:
							if not pUnit.isDuration() and not pUnit.isSummoned():
								pHyborem = pUnit
								break
					if pHyborem is not None:
						return (pHyborem.getDamage() > 50)
			else:
				if pTeam.getAtWarCount(True) > 1:
					return True
		if CyGame().getGlobalCounter() > 90:
			return True
		return False
# ent <<<
	return True

def reqDomination(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isAlwaysHostile(pPlot):
		return ReasonTypes.REASON_DISABLED_NATIONALITY_IS_HIDDEN

	iResistMax = 95
	if not pCaster.isHuman():
		iResistMax = 20

	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)

	eTeam = pCaster.getTeam()
	for pUnit in lpRangedUnits:
		if pUnit.isEnemy(eTeam, pUnit.plot()):
			if not isWorldUnitClass(pUnit.getUnitClassType()):
				iResist = pUnit.getResistChance(pCaster, eSpell)
				if iResist <= iResistMax:
					return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellDomination(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iX = pCaster.getX()
	iY = pCaster.getY()

	iResistMax = 95
	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.isHuman():
		iResistMax = 20

	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)

	eTeam = pCaster.getTeam()
	iBestValue = 0
	pBestUnit = -1
	for pUnit in lpRangedUnits:
		if pUnit.isEnemy(eTeam, pUnit.plot()):
			if not isWorldUnitClass(pUnit.getUnitClassType()):
				iResist = pUnit.getResistChance(pCaster, eSpell)
				if iResist <= iResistMax:
##--------	Fractional Combat Strength: Modified by Denev	--------##
#					iValue = (pUnit.baseCombatStr() + pUnit.baseCombatStrDefense()) * 5 + pUnit.getExperience()
					iValue = (pUnit.getCombatAttackTimes100() + pUnit.getCombatDefenseTimes100()) // 20 + pUnit.getExperience()
##--------	Fractional Combat Strength: End Modify		--------##
					iValue += (100 - iResist)
					if iValue > iBestValue:
						iBestValue = iValue
						pBestUnit = pUnit
	if pBestUnit != -1:
		szButton = gc.getSpellInfo(eSpell).getButton()
		if not pBestUnit.isResisted(pCaster, eSpell):
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_DOMINATION', (pBestUnit.getNameKey(), pPlayer.getCivilizationAdjectiveKey(), pCaster.getNameKey()))
			CyInterface().addMessage(pBestUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pBestUnit.getX(), pBestUnit.getY(), True, True)
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_DOMINATION_ENEMY', (pCaster.getNameKey(), gc.getPlayer(pBestUnit.getOwner()).getCivilizationAdjectiveKey(), pBestUnit.getNameKey()))
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)

			if pBestUnit.isImmuneToCapture():
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_CAPTURED_LOYALTY', (pBestUnit.getNameKey(), ))
				CyInterface().addMessage(pBestUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pBestUnit.getX(), pBestUnit.getY(), True, True)
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_CAPTURED_LOYALTY', (pBestUnit.getNameKey(), ))
				CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
				pBestUnit.kill(False, PlayerTypes.NO_PLAYER)
			else:
				pNewUnit = pPlayer.initSkeletalUnit(pBestUnit.getUnitType(), pPlot.getX(), pPlot.getY(), pBestUnit.getUnitAIType())
				pNewUnit.convert(pBestUnit)
				pNewUnit.changeImmobileTimer(1)
# Kaijin >>>
		"""
		else:
			iTimer = 1 + cyFlatValue(3, g_dGameSpeedPercent["VictoryDelay"], True)
			pCaster.changeUncastableTimer(iTimer)
			ePromotion = gc.getInfoTypeForString('PROMOTION_MIND3')
#			pCaster.setHasPromotion(ePromotion, False)
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_DOMINATION_FAILED', (pCaster.getNameKey(), gc.getSpellInfo(eSpell).getDescription()))
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getPromotionInfo(ePromotion).getButton(), en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
		"""
# Kaijin <<<

# ent >>>
def disabledDrown(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		ePlayer = pCaster.getOwner()
		iCasterID = pCaster.getID()
		for iUnitIndex in xrange(pPlot.getNumUnits()):
			pUnit = pPlot.getUnit(iUnitIndex)
			if pUnit.getOwner() == ePlayer:
				if pUnit.isMilitaryHappiness():
					if pUnit.getID() != iCasterID:
						break
		else:
			return True
	return False
# ent <<<
def disabledEarthquake(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		iTeam = pCaster.getTeam()
		pTeam = gc.getTeam(iTeam)
		lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, True)
		for pTargetPlot in lpRangedPlots:
			iRevealedOwner = pTargetPlot.getRevealedOwner(iTeam, False)
			if iRevealedOwner != PlayerTypes.NO_PLAYER:
				iTargetTeam = gc.getPlayer(iRevealedOwner).getTeam()
				if not pTeam.isAtWar(iTargetTeam):
					return True
	return False

def spellEnterPortal(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	iX = pPlot.getPortalExitX()
	iY = pPlot.getPortalExitY()
	pExitPlot = CyMap().plot(iX,iY)
	if not pPlot.isNone():
		pCaster.setXY(iX, iY, False, True, True)

def reqEntertain(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	if pCity.isDisorder():
		return ReasonTypes.REASON_DISABLED_CITY_IS_REVOLTING
# ent >>>
	if pCity.getHappinessTimer() > 0:
		return ReasonTypes.REASON_DISABLED_ALREADY_BUFFED
# ent <<<
	return True

def spellEntertain(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	iCasterPlayer = pCaster.getOwner()
	iTargetPlayer = pCity.getOwner()
	if iCasterPlayer != iTargetPlayer:
		pCasterPlayer = gc.getPlayer(iCasterPlayer)
		pTargetPlayer = gc.getPlayer(iTargetPlayer)
		iGold = pCity.getPopulation() // 2 + 1
		pCasterPlayer.changeGold(iGold)
		pTargetPlayer.changeGold(iGold * -1)

		szButton = gc.getSpellInfo(eSpell).getButton()
		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_ENTERTAIN_GOOD', (iGold, pTargetPlayer.getCivilizationAdjectiveKey(), pCity.getNameKey(), gc.getSpellInfo(eSpell).getDescription()))
		CyInterface().addMessage(iCasterPlayer,True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_ENTERTAIN_BAD', (iGold, pTargetPlayer.getCivilizationAdjectiveKey(), pCity.getNameKey(), gc.getSpellInfo(eSpell).getDescription()))
		CyInterface().addMessage(iTargetPlayer,True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCity.getX(), pCity.getY(), True, True)

# ent >>>
#	iHappinessTimer = cyFlatValue(2, g_dGameSpeedPercent["VictoryDelay"], True)
#	pCity.changeHappinessTimer(iHappinessTimer)
	iTotalCulture = 0
	for pyCity in PyPlayer(iCasterPlayer).getCityList():
		pLoopCity = pyCity.GetCy()
		iTotalCulture += pLoopCity.getCulture(iCasterPlayer)
	iTurn = CyGame().getGameTurn()
	if iTurn > 0:
		pPlot.changeCulture(iCasterPlayer, (iTotalCulture // iTurn), True)
		iHappinessTimer = cyFlatValue((iTotalCulture // iTurn), g_dGameSpeedPercent["VictoryDelay"], True)
		iHappinessTimer = 2 + CyGame().getSorenRandNum(iHappinessTimer, 'Entertain!')
		pCity.changeHappinessTimer(iHappinessTimer)
# ent <<<

def reqEscape(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isBarbarian():
		return False
	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getNumCities() < 1:
		return ReasonTypes.REASON_DISABLED_REQUIRES_CITY
	pCity = pPlayer.getCapitalCity()
	if pCity.isNone():
		pCity, iterOut = pPlayer.firstCity(False)
	if pCaster.at(pCity.getX(), pCity.getY()):
		return ReasonTypes.REASON_DISABLED_ALREADY_BUFFED
	if not pPlayer.isHuman():
		if pCaster.getDamage() < 50:
			return False
	return True

def spellEscape(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getNumCities() > 0:
		pCity = pPlayer.getCapitalCity()
		if pCity.isNone():
			pCity, iterOut = pPlayer.firstCity(False)
		if not pCity.isNone():
			pCaster.setXY(pCity.getX(), pCity.getY(), False, True, True)

def reqFeast(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	if pCity.getPopulation() < 3:
		return ReasonTypes.REASON_DISABLED_LACK_OF_POPULATION
	if not pCaster.isHuman():
		if pCity.getPopulation() < 15:
			return False
		if pCaster.getUnitAIType() != UnitAITypes.UNITAI_FEASTING:
			if pCity.unhappyLevel(0) > pCity.happyLevel():
				return False
	return True

def spellFeast(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	pCaster.changeExperience(pCity.getPopulation()-2, -1, False, False, False)
	iAngerTimer = cyFlatValue(3, g_dGameSpeedPercent["HurryConscriptAnger"], True)
	pCity.changeHurryAngerTimer(iAngerTimer)

def reqFeed(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.getDamage() == 0 and not pCaster.isMadeAttack():
		return ReasonTypes.REASON_DISABLED_FULL_STOMACH_BLOODY
	if not pCaster.isHuman():
		if pCaster.getDamage() < 20:
			return False
	return True

def spellFeed(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	eBloodpet = gc.getSpellInfo(eSpell).getUnitInStackPrereq()
	ePlayer = pCaster.getOwner()
	iCasterID = pCaster.getID()

	pVictim = -1
	for iUnitIndex in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(iUnitIndex)
		if pUnit.getOwner() == ePlayer:
			if pUnit.getUnitType() == eBloodpet:
				if pVictim == -1 or pVictim.getExperience() > pUnit.getExperience():
					if pUnit.getID() != iCasterID:
						pVictim = pUnit
	if pVictim != -1:
		pVictim.kill(False, PlayerTypes.NO_PLAYER)

def reqForTheHorde(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pTeam = gc.getTeam(pCaster.getTeam())
	iBarbarianTeam = gc.getBARBARIAN_TEAM()
	if pTeam.isAtWar(iBarbarianTeam):
		return ReasonTypes.REASON_DISABLED_BARBARIAN_IS_ENEMY

	pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
	if pBarbarianPlayer.getNumUnits() == 0:
		return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

	if not pCaster.isHuman():
# ent >>>
		"""
		if pBarbarianPlayer.getNumUnits() < 60:
			return False
		"""
		if gc.getPlayer(pCaster.getOwner()).AI_isFinancialTrouble():
			return False
		iNumUnownedLandTiles = 0
		for i in range(CyMap().getNumAreas()):
			pArea = CyMap().getArea(i)
			if not pArea.isWater():
				iNumUnownedLandTiles += pArea.getNumUnownedTiles()
		if pBarbarianPlayer.getNumUnits() < iNumUnownedLandTiles // 15:
			return False
# ent <<<
	return True

def spellForTheHorde(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	pCapital = pPlayer.getCapitalCity()
	bExistCapital = (not pCapital.isNone())
	if bExistCapital:
		pCenterPlot = pCapital.plot()
		eCapitalArea = pCenterPlot.getArea()
	else:
		pCenterPlot = pCaster.plot()
		eCapitalArea = -1
	iCenterX = pCenterPlot.getX()
	iCenterY = pCenterPlot.getY()
	eHero = en.ePromotionHero
	eOrc = en.eRaceOrc
	eGoblin = en.eRaceGoblin
	iGoblinSound = gc.getUnitInfo(gc.getInfoTypeForString('UNIT_GOBLIN')).getArtInfo(0, EraTypes.NO_ERA, UnitArtStyleTypes.NO_UNIT_ARTSTYLE).getSelectionSoundScriptId()
	iBaseDistance = int(((CyMap().getGridWidth() ** 2) + (CyMap().getGridHeight() ** 2)) ** 0.5)
	iDenominator = int(iBaseDistance ** 1.5)

	for pUnit in PyPlayer(gc.getBARBARIAN_PLAYER()).getUnitList():
		if pUnit.getRace() in (eOrc, eGoblin) and not pUnit.isHasPromotion(eHero):
			iPlotDistance = plotDistance(pUnit.getX(), pUnit.getY(), iCenterX, iCenterY)
			iNumerator = int((iBaseDistance - iPlotDistance) ** 1.5)
			if CyGame().getSorenRandNum(iDenominator, 'For the Horde!') < iNumerator:
				pPlot = pUnit.plot()
				if pPlot.getNumVisibleEnemyDefenders(pUnit) > 0:
					bJumpSuccess = pUnit.jumpToNearestValidPlot()
					if not bJumpSuccess:
						continue
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_UNIT_CONVERT', (gc.getPlayer(pUnit.getOwner()).getCivilizationAdjectiveKey(), pUnit.getNameKey()))
				iSound = pUnit.getArtInfo(0, EraTypes.NO_ERA).getSelectionSoundScriptId()
				if iSound == iGoblinSound:
					szSound = 'AS3D_GOBLIN_SELECT'
				else:
					szSound = 'AS3D_ORC_SELECT'
				CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), szMessage, szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, pUnit.getButton(), en.eColorGreen, pUnit.getX(), pUnit.getY(), True, True)

				pNewUnit = pPlayer.initSkeletalUnit(pUnit.getUnitType(), pPlot.getX(), pPlot.getY(), pUnit.getUnitAIType())
				pNewUnit.convert(pUnit)
				if not bExistCapital or pNewUnit.plot().getArea() != eCapitalArea:
					pNewUnit.setUnitAIType(UnitAITypes.UNITAI_EXPLORE)

def spellFormWolfPack(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	eWolf = gc.getSpellInfo(eSpell).getUnitInStackPrereq()
	ePlayer = pCaster.getOwner()
	iCasterID = pCaster.getID()
	lpRangedUnits = cyGetRangedUnits(pPlot, 0, False, False, TeamTypes.NO_TEAM)

	pWolf = -1
	for pUnit in lpRangedUnits:
		if pUnit.getOwner() == ePlayer:
			if pUnit.getUnitType() == eWolf:
				if pUnit.getID() != iCasterID:
					pWolf = pUnit
					break
	if pWolf != -1:
		pCaster.changeExperience(pWolf.getExperience(), -1, False, False, False)
		for iPromotion in xrange(gc.getNumPromotionInfos()):
			if pWolf.isHasPromotion(iPromotion):
				if not gc.getPromotionInfo(iPromotion).isEquipment():
					pCaster.setHasPromotion(iPromotion, True)
		pCaster.setUnitAIType(UnitAITypes.UNITAI_ATTACK_CITY)
		pWolf.kill(False, PlayerTypes.NO_PLAYER)

def reqGiftsOfNantosuelta(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getNumCities() == 0:
		return ReasonTypes.REASON_DISABLED_REQUIRES_CITY
	if not pPlayer.isHuman():
# ent >>>
#		if pPlayer.getNumCities() < gc.getWorldInfo(CyMap().getWorldSize()).getTargetNumCities():
#			return False
		if cf.AI_hasRoomForFound(pCaster.getOwner()):
			return False
# ent <<<
	return True

def spellGiftsOfNantosuelta(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	iGoldenHammer = gc.getInfoTypeForString('UNIT_GOLDEN_HAMMER')
	for pyCity in PyPlayer(iPlayer).getCityList():
		pCity = pyCity.GetCy()
		pNewUnit = pPlayer.initUnit(iGoldenHammer, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

def reqGiftVampirism(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if pUnit.getOwner() == ePlayer:
			if not pUnit.isHasPromotion(en.ePromotionVampire):
				if pUnit.getLevel() >= 6:
					return True
				if pUnit.getLevel() >= 4 and pUnit.getUnitType() == en.eUnitMoroi:
					return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellGiftVampirism(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	ePlayer = pCaster.getOwner()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, False)
	for pUnit in lpRangedUnits:
		if pUnit.getOwner() == ePlayer:
			if pUnit.getLevel() >= 6:
				pUnit.setHasPromotion(en.ePromotionVampire, True)
			if pUnit.getLevel() >= 4 and pUnit.getUnitType() == en.eUnitMoroi:
				pUnit.setHasPromotion(en.ePromotionVampire, True)

def spellGiveHammerToCraftsman(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pCaster.plot().getPlotCity()
	pCity.changeFreeSpecialistCount(gc.getInfoTypeForString('SPECIALIST_ENGINEER'), 1)

def reqHastursRazor(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	bHuman = (pCaster.isHuman())
	ePlayer = pCaster.getOwner()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if pUnit.getDamage() > 0:
			if bHuman:
				return True
			if pUnit.getOwner() == ePlayer:
				return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellHastursRazor(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	ePlayer = pCaster.getOwner()
	eTeam = pCaster.getTeam()
	kSpell = gc.getSpellInfo(eSpell)
	szButton = kSpell.getButton()
	szSpellDescription = kSpell.getDescription()
	szSound = 'AS2D_SPELL_CHARM_PERSON'
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, False)

	lpTargetUnits = [pUnit for pUnit in lpRangedUnits if pUnit.canFight()]
	liDamage = [pUnit.getDamage() for pUnit in lpRangedUnits if pUnit.canFight()]
	for pUnit in lpTargetUnits:
		iNewDamage = liDamage.pop(CyGame().getSorenRandNum(len(liDamage), 'Hasturs Razor'))
		if iNewDamage != pUnit.getDamage():
			bPositive = (iNewDamage < pUnit.getDamage())
			if bPositive:
				iColor = en.eColorGreen
			else:
				iColor = en.eColorRed
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_HASTURS_RAZOR', (szSpellDescription, pUnit.getDamage(), iNewDamage, pUnit.getNameKey()))
			CyInterface().addMessage(pUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, iColor, pUnit.getX(), pUnit.getY(), True, True)
			if pUnit.getOwner() != ePlayer:
				bPositive = (pUnit.getTeam() != eTeam) ^ (iNewDamage < pUnit.getDamage())
				if bPositive:
					iColor = en.eColorGreen
				else:
					iColor = en.eColorRed
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_HASTURS_RAZOR_ENEMY', (szSpellDescription, pUnit.getDamage(), iNewDamage, pUnit.getNameKey(), gc.getPlayer(pUnit.getOwner()).getCivilizationAdjectiveKey()))
				CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, iColor, pUnit.getX(), pUnit.getY(), True, True)
			pUnit.setDamage(iNewDamage, ePlayer)

def disabledHealingSalve(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		if pCaster.getDamage() < 25:
			return True
	return False

def disabledHellfire(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	eHellFire = gc.getSpellInfo(eSpell).getCreateImprovementType()
	iRange = 2
	lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, False, TeamTypes.NO_TEAM)
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.getImprovementType() == eHellFire:
			return ReasonTypes.REASON_DISABLED_TOO_CLOSE_SAME_IMPROVEMENT
	if not pCaster.isHuman():
		if pPlot.isOwned():
			if pPlot.getOwner() == pCaster.getOwner():
				return True
	return False

def spellHeraldsCall(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

##>>>>Advanced Kamikaze Rules: Modified by ent 2019/07/30
	"""
	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, False)
	for pUnit in lpRangedUnits:
		if pUnit.getUnitCombatType() in (en.eUnitCombatRecon, en.eUnitCombatArcher, en.eUnitCombatMounted, en.eUnitCombatMelee, en.eUnitCombatAdept, en.eUnitCombatDisciple, en.eUnitCombatAnimal, en.eUnitCombatBeast):
			pUnit.setDuration(1)
	"""
	eHeraldsCall = gc.getInfoTypeForString('PROMOTION_HERALDS_CALL')
	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, False)
	for pUnit in lpRangedUnits:
		if pUnit.isHasPromotion(eHeraldsCall):
			pUnit.setDuration(1)
##<<<<Advanced Kamikaze Rules: End Modify

def reqHireScorpionClan(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pTeam = gc.getTeam(pCaster.getTeam())
	if pTeam.isAtWar(gc.getBARBARIAN_TEAM()):
		return ReasonTypes.REASON_DISABLED_BARBARIAN_IS_ENEMY
	return True

# ent >>>
def reqHireUnits(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
		pTeam = gc.getTeam(pPlayer.getTeam())
		if pPlayer.AI_isFinancialTrouble():
			return False
		if pPlayer.getGold() < 200:
			return False
		if pTeam.getAnyWarPlanCount(True) == 0:
			return False
	return True
# ent <<<

def spellHireUnits(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	pCity = pCaster.plot().getPlotCity()
	iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(), 'EVENTTRIGGER_MAGNADINE_HIRE_UNITS')
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#	triggerData = pPlayer.initTriggeredData(iEvent, True, pCity.getID(), pCity.getX(), pCity.getY(), iPlayer, -1, -1, -1, -1, -1)
	pPlayer.triggerCustomEvent(iEvent, pCity.getID(), pCity.getX(), pCity.getY(), PlayerTypes.NO_PLAYER, -1, ReligionTypes.NO_RELIGION, CorporationTypes.NO_CORPORATION, -1, BuildingTypes.NO_BUILDING)
##--------	Unofficial Bug Fix: End Modify			--------##

def reqHyboremsWhisper(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if CyGame().isNetworkMultiPlayer():
		if not pCaster.plot().isCity():
			return ReasonTypes.REASON_DISABLED_OUT_OF_CITY
		return True
##--------	Tweaked Hyborem: Modified by Denev	--------##
	"""
	pCity = cf.getAshenVeilCity(3)
	if pCity == -1:
	"""
	lpVeilCities = cf.getAshenVeilCities(pCaster.getOwner(), pCaster.getID(), 1)
	if len(lpVeilCities) == 0:
##--------	Tweaked Hyborem: End Modify			--------##
		return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET
	return True

def spellHyboremsWhisper(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	if CyGame().isNetworkMultiPlayer():
		iNumUnits = 30
		iNumUnits *= CyGame().getGameTurn() ** 2
		iNumUnits /= CyGame().getMaxTurns() ** 2
		iNumUnits = max(1, iNumUnits)
		customSummonSpellData = CvCustomSummonSpellData()
		customSummonSpellData.eUnit = en.eUnitManes
		customSummonSpellData.iNumUnits = iNumUnits
		pCaster.castCustomSummon(customSummonSpellData)
		return

	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
##--------	Tweaked Hyborem: Modified by Denev	--------##
	"""
	iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(),'EVENTTRIGGER_HYBOREMS_WHISPER')
	triggerData = pPlayer.initTriggeredData(iEvent, True, -1, caster.getX(), caster.getY(), iPlayer, -1, -1, -1, -1, -1)
	"""
	iNumSelectableCities = 3
	iCasterID = pCaster.getID()
	lpVeilCities = cf.getAshenVeilCities(iPlayer, iCasterID, iNumSelectableCities)
	if pPlayer.isHuman():
		popupHyboremsWhisper(iPlayer, iCasterID, lpVeilCities, 0)
	else:
# ent >>>
#		pPlayer.acquireCity(lpVeilCities[0], False, True)
		pCity = lpVeilCities[0]
		pPlayer.acquireCity(pCity, False, True)
		eUnit = gc.getInfoTypeForString('UNIT_LONGBOWMAN')
		for i in xrange(gc.getDefineINT('COLONY_NUM_FREE_DEFENDERS')):
			pNewUnit = pPlayer.initUnit(eUnit, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit.changeImmobileTimer(1)
# ent <<<

def popupHyboremsWhisper(iPlayer, iCasterID, lpVeilCities, iCurrentSelected):
	popupInfo = CyPopupInfo()
	popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
	popupInfo.setText(CyTranslator().getText("TXT_KEY_EVENT_HYBOREMS_WHISPER",()))
	popupInfo.setData1(iPlayer)
	popupInfo.setData2(len(lpVeilCities))
	popupInfo.setData3(iCurrentSelected)
	popupInfo.setFlags(iCasterID)

	for pVeilCity in lpVeilCities:
		popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_POPUP_HYBOREMS_WHISPER_SELECT", (pVeilCity.getNameKey(), )), "")
		popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_CITY_WARNING_ANSWER3", ()), "")
	szButton = CyGlobalContext().getUnitInfo(CyGlobalContext().getInfoTypeForString('UNIT_HYBOREM')).getButton()
	popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_EVENT_HYBOREMS_WHISPER_HELP", (lpVeilCities[iCurrentSelected].getNameKey(), )), szButton)
	popupInfo.setOnClickedPythonCallback("applyHyboremsWhisper")
	popupInfo.setPythonModule("CvSpellInterface")
	popupInfo.addPopup(iPlayer)

def applyHyboremsWhisper(argsList):
	iButtonId, iData1, iData2, iData3, iFlags, szText, bOption1, bOption2 = argsList

	iPlayer = iData1
	iNumCities = iData2
	iCurrentSelected = iData3
	iCasterID = iFlags
	lpVeilCities = cf.getAshenVeilCities(iPlayer, iCasterID, iNumCities)

	if iButtonId == iNumCities * 2:
		pPlayer = gc.getPlayer(iPlayer)
# ent >>>
#		pPlayer.acquireCity(lpVeilCities[iCurrentSelected], False, True)
		pCity = lpVeilCities[iCurrentSelected]
		pPlayer.acquireCity(pCity, False, True)
		eUnit = gc.getInfoTypeForString('UNIT_LONGBOWMAN')
		for i in xrange(gc.getDefineINT('COLONY_NUM_FREE_DEFENDERS')):
			pNewUnit = pPlayer.initUnit(eUnit, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit.changeImmobileTimer(1)
# ent <<<
		return

	iClickedKind = iButtonId % 2
	iPickedUpIndex = iButtonId // 2
	pSelectedCity = lpVeilCities[iPickedUpIndex]
	if iPlayer == CyGame().getActivePlayer():
		CyCamera().JustLookAtPlot(pSelectedCity.plot())
	if iClickedKind == 1:
		CyInterface().selectCity(pSelectedCity, False)
	popupHyboremsWhisper(iPlayer, iCasterID, lpVeilCities, iPickedUpIndex)
##--------	Tweaked Hyborem: End Modify			--------##

def reqImpersonateLeader(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if CyGame().isOption(GameOptionTypes.GAMEOPTION_CHALLENGE_HIGH_TO_LOW):
		if CyGame().getHighToLowCounter() < 2:
			return False

	pCity = pPlot.getPlotCity()
	if pCity.getTeam() == pCaster.getTeam():
		return ReasonTypes.REASON_DISABLED_IMMUNE_OWN_CITY
	if gc.getTeam(pCity.getTeam()).isHuman():
		return False
	if gc.getPlayer(pCity.getOwner()).isBarbarian():
		return False
	if gc.getPlayer(pCity.getOwner()).getTempPlayerTimer() > 0:
		return False
	for ePlayer in xrange(gc.getMAX_CIV_PLAYERS()):
		pPlayer = gc.getPlayer(ePlayer)
		if pPlayer.isAlive():
			if pPlayer.getTempPlayerTimer() > 0:
				if pPlayer.getRealPlayer() == pCity.getOwner():
					return False
	return True

def spellImpersonateLeader(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pCaster.plot().getPlotCity()
	iNewPlayer = pCity.getOwner()
	iOldPlayer = pCaster.getOwner()
	iTimer = 5 + CyGame().getSorenRandNum(10, "Impersonate Leader")
	iTimer = cyFlatValue(iTimer, g_dGameSpeedPercent["GoldenAge"], True)
	CyGame().reassignPlayerAdvanced(iOldPlayer, iNewPlayer, iTimer)

def reqInquisition(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())
	iStateBelief = pPlayer.getStateReligion()
# ent >>>
	"""
	if iStateBelief == ReligionTypes.NO_RELIGION:
		if pCaster.getOwner() != pCity.getOwner():
			return ReasonTypes.REASON_DISABLED_REQUIRES_STATE_RELIGION
	if iStateBelief != gc.getPlayer(pCity.getOwner()).getStateReligion():
		return ReasonTypes.REASON_DISABLED_HERETIC_IS_YOU
	"""
	eCityOwner = pCity.getOwner()
	bOwnCity = (pCaster.getOwner() == eCityOwner)
	pTeam = gc.getTeam(pPlayer.getTeam())

	if iStateBelief == ReligionTypes.NO_RELIGION:
		if not bOwnCity:
			return ReasonTypes.REASON_DISABLED_REQUIRES_STATE_RELIGION
	if iStateBelief != gc.getPlayer(eCityOwner).getStateReligion():
		return ReasonTypes.REASON_DISABLED_HERETIC_IS_YOU
# ent <<<
	bHolyCity = False
	for iReligion in xrange(gc.getNumReligionInfos()):
		if iStateBelief != iReligion:
			if pCity.isHolyCityByType(iReligion):
				bHolyCity = True
				continue
			if pCity.isHasReligion(iReligion):
# ent - AI: Ignore waste work. >>>
				if not pCaster.isHuman() and bOwnCity:
					eTech = gc.getReligionInfo(iReligion).getTechPrereq()
					bHasTech = (eTech != TechTypes.NO_TECH and pPlayer.isHasTech(eTech))
					# If you have prereqTech of a religion, you must have at least 1 cities with the religion. @ CvGame::doHolyCity()
					if bHasTech and pTeam.getHasReligionCount(iReligion) == 1:
						continue
					# If religious victory is out of concern, you don't need to abandon a religion who don't hate.
					if bHasTech or gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getReligionWeightModifier(iReligion) >= 0:
						if pTeam.hasHolyCity(iReligion) or CyGame().calculateReligionPercent(iReligion) < 50:
							if iStateBelief == ReligionTypes.NO_RELIGION or not pTeam.hasHolyCity(iStateBelief) or CyGame().calculateReligionPercent(iStateBelief) < 50:
								continue
					# Cult of the Dragon
					elif iReligion == en.eReligionCultoftheDragon:
						if pPlayer.getCivilizationType() in (	en.eCivilizationKuriotates, 
																en.eCivilizationSheaim, 
																en.eCivilizationMazatl	):
							if pPlayer.getHasReligionCount(iReligion) == 1:
								return False
							continue
						elif pPlayer.getCivilizationType() in (	en.eCivilizationIllians, 
																en.eCivilizationAltair	):
							if pPlayer.hasHolyCity(iReligion):
								continue
# ent <<<
				return True
	if bHolyCity:
		return ReasonTypes.REASON_DISABLED_HERE_IS_HOLYCITY
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellInquisition(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	iStateBelief = gc.getPlayer(pCity.getOwner()).getStateReligion()

	iAngerTimer = 0
	for iReligion in xrange(gc.getNumReligionInfos()):
		if iStateBelief != iReligion and pCity.isHasReligion(iReligion) and not pCity.isHolyCityByType(iReligion):
			pCity.setHasReligion(iReligion, False, True, True)
			iAngerTimer += 2
			for iBuilding in xrange(gc.getNumBuildingInfos()):
				if gc.getBuildingInfo(iBuilding).getPrereqReligion() == iReligion:
					if pCity.getNumRealBuilding(iBuilding) > 0:
						iBuildingClass = gc.getBuildingInfo(iBuilding).getBuildingClassType()
						if not isWorldWonderClass(iBuildingClass):
							pCity.setNumRealBuilding(iBuilding, 0)
							iAngerTimer += 1
	iAngerTimer = cyFlatValue(iAngerTimer, g_dGameSpeedPercent["HurryConscriptAnger"], True)
	iAngerTimer = CyGame().getSorenRandNum(iAngerTimer, 'Inquisition') + CyGame().getSorenRandNum(iAngerTimer, 'Inquisition') + 1
	if iStateBelief == en.eReligionOrder:
		iAngerTimer //= 2
	pCity.changeHurryAngerTimer(iAngerTimer)

def reqIntoTheMist(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		if gc.getPlayer(pCaster.getOwner()).getNumUnits() < 40:
			return False
	return True

def spellIntoTheMist(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	for pUnit in PyPlayer(pCaster.getOwner()).getUnitList():
		pUnit.setHasPromotion(en.ePromotionHidden, True)

def reqKidnap(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	if pCity.isNone():
		return ReasonTypes.REASON_DISABLED_REQUIRES_CITY
	if pCity.getTeam() == pCaster.getTeam():
		return ReasonTypes.REASON_DISABLED_IMMUNE_FRIENDLY_CITY
	iGreatPerson = 0
	iGreatPerson += pCity.getFreeSpecialistCount(en.eSpecialistGreatPriest)
	iGreatPerson += pCity.getFreeSpecialistCount(en.eSpecialistGreatArtist)
	iGreatPerson += pCity.getFreeSpecialistCount(en.eSpecialistGreatMerchant)
	iGreatPerson += pCity.getFreeSpecialistCount(en.eSpecialistGreatEngineer)
	iGreatPerson += pCity.getFreeSpecialistCount(en.eSpecialistGreatScientist)
	if iGreatPerson == 0:
		return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

	if not pCaster.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.AI_getAtWarCounter(pCity.getTeam()) == 0:
			if pTeam.AI_getWarPlan(pCity.getTeam()) == 0:
				return ReasonTypes.REASON_DISABLED_IMMUNE_FRIENDLY_CITY
			if not pTeam.canDeclareWar(pCity.getTeam()):
				return ReasonTypes.REASON_DISABLED_FORCE_PEACE
# Kaijin >>>
		if pTeam.isVassal(pCity.getTeam()):
			return False
# Kaijin <<<
# ent >>>
		iChance = (pCaster.getCombatAttackTimes100() * 2) // 25
		#iChance = min(95, iChance)
		if iChance < 50:
			return False
# ent <<<
	return True

def spellKidnap(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

# Kaijin >>>
	if not pCaster.plot().isCity():
		return
# Kaijin <<<

	pCity = pCaster.plot().getPlotCity()
	liKidnappable = []
	if pCity.getFreeSpecialistCount(en.eSpecialistGreatPriest) > 0:
		liKidnappable += [(gc.getInfoTypeForString('UNIT_PROPHET'), en.eSpecialistGreatPriest)]
	if pCity.getFreeSpecialistCount(en.eSpecialistGreatArtist) > 0:
		liKidnappable += [(gc.getInfoTypeForString('UNIT_ARTIST'), en.eSpecialistGreatArtist)]
	if pCity.getFreeSpecialistCount(en.eSpecialistGreatMerchant) > 0:
		liKidnappable += [(gc.getInfoTypeForString('UNIT_MERCHANT'), en.eSpecialistGreatMerchant)]
	if pCity.getFreeSpecialistCount(en.eSpecialistGreatEngineer) > 0:
		liKidnappable += [(gc.getInfoTypeForString('UNIT_ENGINEER'), en.eSpecialistGreatEngineer)]
	if pCity.getFreeSpecialistCount(en.eSpecialistGreatScientist) > 0:
		liKidnappable += [(gc.getInfoTypeForString('UNIT_SCIENTIST'), en.eSpecialistGreatScientist)]
##--------	Fractional Combat Strength: Modified by Denev	--------##
#	iChance = pCaster.baseCombatStr() * 8
	iChance = (pCaster.getCombatAttackTimes100() * 2) // 25
##--------	Fractional Combat Strength: End Modify		--------##
	iChance = min(95, iChance)
	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCityOwner = gc.getPlayer(pCity.getOwner())
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#	if CyGame().getSorenRandNum(100, "Kidnap") <= iChance:
	if CyGame().getSorenRandNum(100, 'Kidnap Success Roll') < iChance:
##--------	Unofficial Bug Fix: End Modify			--------##
		if len(liKidnappable) > 0:
			iRnd = CyGame().getSorenRandNum(len(liKidnappable), 'Kidnap Victim Choice Roll')
			iUnit = liKidnappable[iRnd][0]
			iSpec = liKidnappable[iRnd][1]
			pNewUnit = pPlayer.initUnit(iUnit, pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
##--------	Advanced Rules: Added by Denev 2014/04/26
			pNewUnit.finishMoves()
##--------	Advanced Rules: End Add
			pCity.changeFreeSpecialistCount(iSpec, -1)
			szButton = gc.getUnitInfo(iUnit).getButton()
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_KIDNAP_SUCCEEDED', (pCaster.getNameKey(), pCityOwner.getCivilizationAdjectiveKey(), pCity.getNameKey(), gc.getUnitInfo(iUnit).getDescription()))
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_POSITIVE_DINK', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
	else:
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#		if CyGame().getSorenRandNum(100, "Kidnap") <= 50:
		if CyGame().getSorenRandNum(100, 'Kidnap Escape Roll') < 50:
##--------	Unofficial Bug Fix: End Modify			--------##
			pCaster.setXY(pPlayer.getCapitalCity().getX(), pPlayer.getCapitalCity().getY(), False, True, True)
			szButton = gc.getSpellInfo(eSpell).getButton()
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_KIDNAP_FAILED_AND_ESCAPED', (pCaster.getNameKey(), pCityOwner.getCivilizationAdjectiveKey(), pCity.getNameKey()))
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_EXPOSED', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCity.getX(), pCity.getY(), True, True)
		else:
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#			caster.kill(True, 0)
			pCaster.kill(True, PlayerTypes.NO_PLAYER)
##--------	Unofficial Bug Fix: End Modify			--------##
			szButton = gc.getSpellInfo(eSpell).getButton()
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_KIDNAP_FAILED_AND_KILLED', (pCaster.getNameKey(), pCityOwner.getCivilizationAdjectiveKey(), pCity.getNameKey()))
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_EXPOSED', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCity.getX(), pCity.getY(), True, True)
			szButton = gc.getSpellInfo(eSpell).getButton()
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_KIDNAP_INTERCEPTED', (pPlayer.getCivilizationAdjectiveKey(), pCaster.getNameKey(), pCity.getNameKey()))
			CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_EXPOSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
			pTeam = gc.getTeam(pCaster.getTeam())
			pTeam.declareWar(pCity.getTeam(), False, WarPlanTypes.WARPLAN_LIMITED)

def reqLegends(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getNumCities() == 0:
		return ReasonTypes.REASON_DISABLED_REQUIRES_CITY
	if not pPlayer.isHuman():
# ent >>>
		"""
		iMaxCities = pPlayer.getMaxCities()
		if pPlayer.getNumCities() < iMaxCities + max(2, iMaxCities - 1):
			if pPlayer.getCurrentPeriod() < CyGame().getNumPeriods() // 2:
				return False
		"""
		if cf.AI_hasRoomForFound(pCaster.getOwner()):
			return False
# ent <<<
	return True

def spellLegends(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)

	iCapitalCulture = 0
	pCapital = pPlayer.getCapitalCity()
	if not pCapital.isNone():
		iCapitalCulture = pCapital.getCulture(iPlayer)

	iCulture = max(300, iCapitalCulture//8)
	iCulture *= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(CyGame().getGameSpeedType())
	iCulture /= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(en.eGameSpeedNormal)

	for pyCity in PyPlayer(iPlayer).getCityList():
		pCity = pyCity.GetCy()
		pCity.changeCulture(iPlayer, iCulture, True)

def disabledLichdom(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.getUnitClassType() == en.eUnitClassFleshGolem:
		return ReasonTypes.REASON_DISABLED_INVALID_KIND_OF_UNIT
	if isWorldUnitClass(pCaster.getUnitClassType()):
		return ReasonTypes.REASON_DISABLED_WORLDUNIT_NOT_ALLOWED
	return False

def disabledMask(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.hasCargo():
		return True
	if pCaster.isCargo():
		return True
	return False

def reqMezmerizeAnimal(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isAlwaysHostile(pPlot):
		return ReasonTypes.REASON_DISABLED_NATIONALITY_IS_HIDDEN

	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if pUnit.getUnitCombatType() == en.eUnitCombatAnimal:
			return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellMezmerizeAnimal(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pPlayer = gc.getPlayer(pCaster.getOwner())
	szButton = gc.getSpellInfo(eSpell).getButton()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, False)
	for pUnit in lpRangedUnits:
		if pUnit.getUnitCombatType() == en.eUnitCombatAnimal:
			if not pUnit.isResisted(pCaster, eSpell):
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_MEZMERIZE_ANIMAL', (pUnit.getNameKey(), pCaster.getNameKey(), pPlayer.getCivilizationAdjectiveKey()))
				CyInterface().addMessage(pUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pUnit.getX(), pUnit.getY(), True, True)
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_MEZMERIZE_ANIMAL_ENEMY', (pCaster.getNameKey(), pUnit.getNameKey(), gc.getPlayer(pUnit.getOwner()).getCivilizationAdjectiveKey()))
				CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pUnit.getX(), pUnit.getY(), True, True)

				if pUnit.isImmuneToCapture():
					szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_CAPTURED_LOYALTY', (pUnit.getNameKey(), ))
					CyInterface().addMessage(pUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pUnit.getX(), pUnit.getY(), True, True)
					szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_CAPTURED_LOYALTY', (pUnit.getNameKey(), ))
					CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pUnit.getX(), pUnit.getY(), True, True)
					pUnit.kill(False, PlayerTypes.NO_PLAYER)
				else:
					eUnitAI = pUnit.getUnitAIType()
					if eUnitAI == UnitAITypes.UNITAI_ANIMAL:
						eUnitAI = UnitAITypes.UNITAI_ATTACK
					pNewUnit = pPlayer.initSkeletalUnit(pUnit.getUnitType(), pCaster.getX(), pCaster.getY(), eUnitAI)
					pNewUnit.convert(pUnit)
					pNewUnit.changeImmobileTimer(1)

def reqMirror(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	iPlayer = pCaster.getOwner()
	if pCaster.isImmuneToMagic():
		return ReasonTypes.REASON_DISABLED_IMMUNE_TO_MAGIC
#	if pPlot.isVisibleEnemyUnit(iPlayer):
#		return ReasonTypes.REASON_DISABLED_SUMMON_ON_TOP_OF_ENEMIES
	return True

def spellMirror(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	customSummonSpellData = CvCustomSummonSpellData()
	customSummonSpellData.eUnit = pCaster.getUnitType()
	customSummonSpellData.iDuration = gc.getDefineINT('SUMMONING_DEFAULT_DURATION_TURNS')
	customSummonSpellData.bAbility = True
	customSummonSpellData.bCopyPromotion = True
	customSummonSpellData.bCopyCaster = True
	customSummonSpellData.eDefaultPromotion = en.eRaceIllusion
	"""
	customSummonSpellData.eUnit = UnitTypes.NO_UNIT
	customSummonSpellData.iNumUnits = 1
	customSummonSpellData.iDuration = -1
	customSummonSpellData.bAbility = False
	customSummonSpellData.bCopyPromotion = False
	customSummonSpellData.bCopyCaster = False
	customSummonSpellData.eDefaultPromotion = PromotionTypes.NO_PROMOTION
	customSummonSpellData.iSummoningPlotIndex = -1
	customSummonSpellData.eUnitAI = UnitAITypes.NO_UNITAI
	customSummonSpellData.eEffect = EffectTypes.NO_EFFECT
	customSummonSpellData.szSound = ''
	"""

# Kaijin >>>
	# His real ability of Alazkan
	if pCaster.getUnitType() == gc.getInfoTypeForString('UNIT_ALAZKAN'):
		customSummonSpellData.iNumUnits += 1
# Kaijin <<<

	lpNewUnits = pCaster.castCustomSummon(customSummonSpellData)

def reqPeace(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_CHANGING_WAR_PEACE):
		return False
	pTeam = gc.getTeam(pCaster.getTeam())
	if pTeam.getAtWarCount(True) == 0:
		return False
# ent >>>
	if not pCaster.isHuman():
		iRatio = cf.AI_getWarSuccessCapitulationRatio(pCaster.getOwner())
		if iRatio > -99:
			return False
# ent <<<
	for iLoopTeam in xrange(gc.getMAX_CIV_TEAMS()):
		if pTeam.isAtWar(iLoopTeam):
			if pTeam.canChangeWarPeace(iLoopTeam):
				return True
	return False

def spellPeace(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	eTeam = pCaster.getTeam()
	pTeam = gc.getTeam(eTeam)
	for iLoopTeam in xrange(gc.getMAX_CIV_TEAMS()):
		pLoopTeam = gc.getTeam(iLoopTeam)
		if pLoopTeam.isAlive() and iLoopTeam != eTeam:
			if pTeam.isAtWar(iLoopTeam):
				if pTeam.canChangeWarPeace(iLoopTeam):
					pTeam.makePeace(iLoopTeam)
	CyGame().changeGlobalCounter(-1 * (CyGame().getGlobalCounter() / 2))

def reqPeaceSevenPines(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isBarbarian():
		return False
	if not pPlot.isPythonActive():
		return ReasonTypes.REASON_DISABLED_ONLY_ONCE_PER_GAME
	pTeam = gc.getTeam(pCaster.getTeam())
	if pTeam.getAtWarCount(True) == 0:
		return False
# ent >>>
	if not pCaster.isHuman():
		iRatio = cf.AI_getWarSuccessCapitulationRatio(pCaster.getOwner())
		if iRatio > -99:
			return False
# ent <<<
	for iLoopTeam in xrange(gc.getMAX_CIV_TEAMS()):
		if pTeam.isAtWar(iLoopTeam):
			if pTeam.canChangeWarPeace(iLoopTeam):
				return True
	return False

def spellPeaceSevenPines(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	eTeam = pCaster.getTeam()
	pTeam = gc.getTeam(eTeam)
	for iLoopTeam in xrange(gc.getMAX_CIV_TEAMS()):
		pLoopTeam = gc.getTeam(iLoopTeam)
		if pLoopTeam.isAlive() and iLoopTeam != eTeam:
			if pTeam.isAtWar(iLoopTeam):
				if pTeam.canChangeWarPeace(iLoopTeam):
					pTeam.makePeace(iLoopTeam)
	CyGame().changeGlobalCounter(-1 * (CyGame().getGlobalCounter() / 2))
	pPlot = pCaster.plot()
	pPlot.setPythonActive(False)

def reqMarchOfTheTrees(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		ePlayer = pCaster.getOwner()
		pPlayer = gc.getPlayer(ePlayer)
		eTeam = pCaster.getTeam()
		pTeam = gc.getTeam(eTeam)

# ent >>>
#		if pTeam.getAtWarCount(True) < 2:
		if pTeam.getAtWarCount(True) == 0:
			return False

		iRatio = cf.AI_getWarSuccessCapitulationRatio(ePlayer)
		if iRatio > -30:
			return False

		# 都市に迫る敵の数と防衛戦力、実行で誕生するトレントの数で制御
		iNumEnemies = 0
		iNumDefenders = 0
		iNumTrees = 0
		leAreas = []

		for pyCity in PyPlayer(ePlayer).getCityList():
			pCity = pyCity.GetCy()
			iThreat = pCity.AI_cityThreat()
			if pCity.isCapital() or iThreat > 50:
				pCityPlot = pCity.plot()
				leAreas.append(pCityPlot.getArea())
				lpRangedPlots = cyGetRangedPlots(pCityPlot, 2, True, True, eTeam)
				for pTargetPlot in lpRangedPlots:
					if pTargetPlot.getArea() not in leAreas:
						continue
					if pTargetPlot.getOwner() != ePlayer:
						continue
					for iUnitIndex in xrange(pTargetPlot.getNumUnits()):
						pUnit = pTargetPlot.getUnit(iUnitIndex)
						if pUnit.canFight():
							if pUnit.getOwner == ePlayer:
								iNumDefenders += 1
							elif pUnit.isEnemy(eTeam, pTargetPlot):
								iNumEnemies += 1
		if leAreas == []:
			return False
		if iNumEnemies < iNumDefenders:
			return False
		if iNumEnemies * CyGame().getNumPeriods() < 30 * (pPlayer.getCurrentPeriod() + 1):
			return False
		for iPlotIndex in xrange(CyMap().numPlots()):
			pLoopPlot = CyMap().plotByIndex(iPlotIndex)
			if pLoopPlot.isOwned():
				if pLoopPlot.getOwner() == ePlayer:
					if pLoopPlot.getFeatureType() in (en.eFeatureForestAncient, en.eFeatureForest):
						if not pLoopPlot.isVisibleEnemyUnit(ePlayer):
							if pLoopPlot.getArea() not in leAreas:
								continue
							iNumTrees += 1
		if iNumTrees < iNumDefenders:
			return False
		if iNumEnemies < iNumDefenders * 2:
			if iNumTrees < iNumEnemies:
				return False
# ent <<<
	return True

def spellMarchOfTheTrees(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iNewForest = en.eFeatureForestNew
	iTreant = gc.getInfoTypeForString('UNIT_TREANT')
	iDuration = cyFlatValue(5, g_dGameSpeedPercent["GoldenAge"], True)
	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	for iPlotIndex in xrange(CyMap().numPlots()):
		pPlot = CyMap().plotByIndex(iPlotIndex)
		if pPlot.isOwned():
			if pPlot.getOwner() == iPlayer:
				if pPlot.getFeatureType() in (en.eFeatureForestAncient, en.eFeatureForest):
					if not pPlot.isVisibleEnemyUnit(iPlayer):
						pNewUnit = pPlayer.initUnit(iTreant, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
						pNewUnit.setDuration(iDuration)

						pCity = pPlot.getWorkingCity()
						if pCity.isNone():
							szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_TREANT', (pNewUnit.getNameKey(), gc.getFeatureInfo(pPlot.getFeatureType()).getDescription()))
						else:
							szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_TREANT_NEAR_CITY', (pNewUnit.getNameKey(), gc.getFeatureInfo(pPlot.getFeatureType()).getDescription(), pCity.getNameKey()))
						szButton = pNewUnit.getButton()
						CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_FEATUREGROWTH', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pNewUnit.getX(), pNewUnit.getY(), True, True)

						pPlot.setFeatureType(iNewForest, 0)

def reqMotherLode(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
# Kaijin >>> Ysbegin
#		if pPlayer.getImprovementCount(gc.getInfoTypeForString('IMPROVEMENT_MINE')) < 10:
		if (pPlayer.getImprovementCount(en.eImprovementMine) + pPlayer.getImprovementCount(en.eImprovementShaftMine)) < 10:
# Kaijin >>> Ysend
			return False
	return True

def spellMotherLode(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)

	iProfitPerMine = 25
	iNumMines = pPlayer.getImprovementCount(en.eImprovementMine)
# Kaijin >>> Magic Expantion Mod
	iNumMines += pPlayer.getImprovementCount(en.eImprovementShaftMine)
# Kaijin <<< Magic Expantion Mod
	pPlayer.changeGold(((iNumMines * iProfitPerMine) * g_dGameSpeedPercent["VictoryDelay"]) // 100)

	eEffect = gc.getInfoTypeForString('EFFECT_SPELL1')
	iUpheavalOdds = 10
	iBaseDiscoverOdds = 100
	for iPlotIndex in xrange(CyMap().numPlots()):
		pPlot = CyMap().plotByIndex(iPlotIndex)
		if pPlot.getOwner() == ePlayer:
			if pPlot.isFlatlands():
				ePlotBonus = pPlot.getBonusType(TeamTypes.NO_TEAM)
				if ePlotBonus != BonusTypes.NO_BONUS:
					if gc.getBonusInfo(ePlotBonus).isFlatlands():
						continue
				if pPlot.getTerrainType() in (en.eTerrainMarsh, en.eTerrainShallows):
					continue
				if CyGame().getSorenRandNum(100, 'Mother Lode') < iUpheavalOdds:
					pPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
					if pPlot.getTerrainType() == en.eTerrainPlains:
						pPlot.setTerrainType(en.eTerrainGrass, False, True)
					elif pPlot.getTerrainType() == en.eTerrainFieldsofPerdition:
						pPlot.setTerrainType(en.eTerrainBrokenLands, False, True)
					elif pPlot.getYield(YieldTypes.YIELD_FOOD) > 0:
						if not pPlot.isCity():
							CyGame().setPlotExtraYield(pPlot.getX(), pPlot.getY(), YieldTypes.YIELD_FOOD, 1)
							CyGame().setPlotExtraYield(pPlot.getX(), pPlot.getY(), YieldTypes.YIELD_PRODUCTION, -1)
# ent: insert applyLandmarkFromEvent() at EventSigns.py >>>
							sCaptionFood = CyTranslator().getText("TXT_KEY_SIGN_FORMAT_FOOD", (1, )) + u" "
							sCaptionProd = CyTranslator().getText("TXT_KEY_SIGN_FORMAT_PROD", (-1, )) + u" "
							sCaptionComm = ""
							sCaptionDesc = CyTranslator().getText("TXT_KEY_SIGN_SPELL_MOTHER_LODE", ())

							sCaption = CyTranslator().getText("TXT_KEY_SIGN_FORMAT_OVERVIEW", (sCaptionFood, sCaptionProd, sCaptionComm, sCaptionDesc))

							for eLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
								pLoopPlayer = gc.getPlayer(eLoopPlayer)
								if pLoopPlayer.isAlive() and pLoopPlayer.isHuman():
									CyEngine().addSign(pPlot, eLoopPlayer, sCaption)
# ent <<<
					pPlot.setPlotType(PlotTypes.PLOT_HILLS, True, True)
					pPoint = pPlot.getPoint()
					CyEngine().triggerEffect(eEffect, pPoint)
			elif pPlot.isHills():
				if pPlot.getBonusType(TeamTypes.NO_TEAM) == BonusTypes.NO_BONUS:
					lePotentialBonuses = []
					for eBonus in xrange(gc.getNumBonusInfos()):
# Kaijin >>> Magic Expantion Mod
#						if gc.getImprovementInfo(en.eImprovementMine).isImprovementBonusTrade(eBonus):
						if gc.getImprovementInfo(en.eImprovementMine).isImprovementBonusTrade(eBonus) or gc.getImprovementInfo(en.eImprovementShaftMine).isImprovementBonusTrade(eBonus):
# Kaijin <<< Magic Expantion Mod
							eTechReveal = gc.getBonusInfo(eBonus).getTechReveal()
							if eTechReveal == TechTypes.NO_TECH or pPlayer.isHasTech(eTechReveal):
#								if pPlot.canHaveBonus(eBonus, False):
									lePotentialBonuses.append(eBonus)
					iRnd = CyGame().getSorenRandNum(10000, 'Mother Lode Extra Mineral')
					if iRnd < iBaseDiscoverOdds * len(lePotentialBonuses):
						eDiscoveredBonus = lePotentialBonuses[CyGame().getSorenRandNum(len(lePotentialBonuses), 'Mother Lode Extra Mineral 2')]
						pPlot.setBonusType(eDiscoveredBonus)
##--------	Unofficial Bug Fix: Modified by ent
#						pCity = CyMap().findCity(pPlot.getX(), pPlot.getY(), ePlayer, TeamTypes.NO_TEAM, False, False, TeamTypes.NO_TEAM, DirectionTypes.NO_DIRECTION, pPlayer.getCity(-1))
						pCity = pPlot.getWorkingCity()
						if pCity.isNone() or pCity.getOwner() != ePlayer:
							pCity = CyMap().findCity(pPlot.getX(), pPlot.getY(), ePlayer, TeamTypes.NO_TEAM, False, False, TeamTypes.NO_TEAM, DirectionTypes.NO_DIRECTION, pCity)
##--------	Unofficial Bug Fix: Modified by ent
						if not pCity.isNone():
							szBuffer = CyTranslator().getText("TXT_KEY_MISC_DISCOVERED_NEW_RESOURCE", (gc.getBonusInfo(eDiscoveredBonus).getTextKey(), pCity.getNameKey()))
							CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), szBuffer, 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, gc.getBonusInfo(eDiscoveredBonus).getButton(), en.eColorWhite, pPlot.getX(), pPlot.getY(), True, True)

def spellOpenChest(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)

	if CyGame().getWBMapScript():
		if not sf.openChest(pCaster, pPlot):
			return

	if CyGame().getSorenRandNum(100, 'Explore Lair') < 25:
		lTrapList = ['POISON', 'FIRE', 'SPORES']
		sTrap = lTrapList[CyGame().getSorenRandNum(len(lTrapList), 'Pick Trap')]
		pPoint = pPlot.getPoint()
		if sTrap == 'POISON':
			iPonson = gc.getInfoTypeForString('PROMOTION_POISONED')
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_TRAP_POISON', ()), 'AS2D_POSITIVE_DINK', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorGreen, pPlot.getX(), pPlot.getY(), False, False)

			pCaster.doDamage(25, 100, en.eDamagePoison)
			pCaster.setHasPromotion(iPonson, True)

		elif sTrap == 'FIRE':
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_TRAP_FIRE', ()), 'AS2D_POSITIVE_DINK', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorGreen, pPlot.getX(), pPlot.getY(), False, False)
			CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_RING_OF_FLAMES'), pPoint)
			CyAudioGame().Play3DSound('AS3D_SPELL_FIREBALL', pPoint.x, pPoint.y, pPoint.z)

			pCaster.doDamage(50, 100, en.eDamageFire)

		elif sTrap == 'SPORES':
			iTimer = cyFlatValue(3, g_dGameSpeedPercent["GoldenAge"], True)

			szButton = gc.getSpellInfo(gc.getInfoTypeForString('SPELL_SPORES')).getButton()
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_TRAP_SPORES', ()), 'AS2D_POSITIVE_DINK', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPORES'), pPoint)
			CyAudioGame().Play3DSound('AS3D_SPELL_CONTAGION', pPoint.x, pPoint.y, pPoint.z)

			pCaster.changeImmobileTimer(iTimer)

	lszGoody = ['EMPTY', 'HIGHEST_GOLD', 'ITEM_HEALING_SALVE', 'ITEM_JADE_TORC', 'ITEM_ROD_OF_WINDS', 'ITEM_TIMOR_MASK']
	if pPlayer.canReceiveGoody(pPlot, gc.getInfoTypeForString('GOODY_GRAVE_TECH'), pCaster):
		lszGoody.append('TECH')
	sGoody = lszGoody[CyGame().getSorenRandNum(len(lszGoody), 'Pick Goody')]
	iTreasure = gc.getInfoTypeForString('UNITCLASS_TREASURE')
	if sGoody == 'EMPTY':
		szButton = gc.getUnitClassInfo(iTreasure).getButton()
		CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_EXPLORE_LAIR_TREASURE_EMPTY',()), 'AS2D_POSITIVE_DINK', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pPlot.getX(), pPlot.getY(), False, False)
	elif sGoody == 'HIGHEST_GOLD':
		pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_HIGHEST_GOLD'), pCaster)
	elif sGoody == 'ITEM_HEALING_SALVE':
		pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_HEALING_SALVE'), pCaster)
	elif sGoody == 'ITEM_JADE_TORC':
		pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_JADE_TORC'), pCaster)
	elif sGoody == 'ITEM_POTION_OF_INVISIBILITY':
		pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_POTION_OF_INVISIBILITY'), pCaster)
	elif sGoody == 'ITEM_POTION_OF_RESTORATION':
		pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_POTION_OF_RESTORATION'), pCaster)
	elif sGoody == 'ITEM_ROD_OF_WINDS':
		pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_ROD_OF_WINDS'), pCaster)
	elif sGoody == 'ITEM_TIMOR_MASK':
		pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_TIMOR_MASK'), pCaster)
	elif sGoody == 'TECH':
		pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_GRAVE_TECH'), pCaster)

	for iUnitIndex in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(iUnitIndex)
		if pUnit.getUnitClassType() == iTreasure and not pUnit.isDelayedDeath():
# ent >>>
			if pUnit.getOwner() != iPlayer:
				continue
# ent <<<
			pTreasure = pUnit
			break
	pTreasure.kill(False, PlayerTypes.NO_PLAYER)

def reqPromoteSettlement(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	if not pCity.isSettlement():
		return False
	pPlayer = gc.getPlayer(pCaster.getOwner())
# Kaijin >>>
	if not pPlayer.hasTrait(en.eTraitSprawling):
		return False
# Kaijin <<<
	if pPlayer.getNumCities() - pPlayer.getNumSettlements() >= pPlayer.getMaxCities():
		return False
	return True

def spellPromoteSettlement(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	pCity.setSettlement(False)
	pCity.setPlotRadius(3)

def reqRagingSeas(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		eTeam = pCaster.getTeam()
		iCount = 0
		for iLoopTeam in xrange(gc.getMAX_CIV_TEAMS()):
			pLoopTeam = gc.getTeam(iLoopTeam)
			if pLoopTeam.isAlive():
				if pLoopTeam.isAtWar(eTeam):
					for eVessel, iPower in g_leVessels:
						iCount += pLoopTeam.getUnitClassCount(eVessel) * iPower
					if iCount > 10:
						return True
		return False
	return True

def spellRaiseSkeleton(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]
	liSummonedUnitIDs = argsList[3]

	pPlot = pCaster.plot()
	if pPlot.getImprovementType() == en.eImprovementGraveyard:
		pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
		customSummonSpellData = CvCustomSummonSpellData()
		customSummonSpellData.eUnit = gc.getSpellInfo(eSpell).getCreateUnitType()
		customSummonSpellData.iNumUnits = 2
		pCaster.castCustomSummon(customSummonSpellData)

def reqRally(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.getNumCities() < gc.getWorldInfo(CyMap().getWorldSize()).getTargetNumCities():
			return False
	return True

def spellRally(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	eDemagog = en.eUnitDemagog
	iCount = 0
	for iPlotIndex in xrange(CyMap().numPlots()):
		pPlot = CyMap().plotByIndex(iPlotIndex)
		if pPlot.getOwner() == ePlayer:
			if not pPlot.isVisibleEnemyUnit(ePlayer):
				pNewUnit = None
				if pPlot.isCity():
					pNewUnit = pPlayer.initUnit(eDemagog, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
					pPlot.getPlotCity().applyBuildEffects(pNewUnit)
					szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_UNIT_JOIN_YOUR_CAUSE', (pNewUnit.getNameKey(), pPlot.getPlotCity().getNameKey()))
				else:
					ePlotImprovement = pPlot.getImprovementType()
					if ePlotImprovement in (en.eImprovementTown, en.eImprovementEnclave):
						pNewUnit = pPlayer.initUnit(eDemagog, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
						eDowngrade = gc.getImprovementInfo(ePlotImprovement).getImprovementPillage()
						pPlot.setImprovementType(eDowngrade)

						pNearCity = pPlot.getWorkingCity()
						if pNearCity.isNone():
							szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_UNIT_JOIN_YOUR_CAUSE', (pNewUnit.getNameKey(), gc.getImprovementInfo(ePlotImprovement).getDescription()))
						else:
							szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_UNIT_JOIN_YOUR_CAUSE_NEAR_CITY', (pNewUnit.getNameKey(), gc.getImprovementInfo(ePlotImprovement).getDescription(), pNearCity.getNameKey()))
							pNearCity.applyBuildEffects(pNewUnit)

				if pNewUnit is not None:
					iStateReligion = pPlayer.getStateReligion()
					if iStateReligion != ReligionTypes.NO_RELIGION:
						if CyGame().getSorenRandNum(100, 'Religion Adoption') < gc.getDefineINT('RELIGION_ADOPTION_CHANCE'):
							pNewUnit.setReligion(pPlayer.getStateReligion())
					CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorGreen, pNewUnit.getX(), pNewUnit.getY(), True, True)

def spellReadTheGrimoire(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iRnd = CyGame().getSorenRandNum(100, 'Read the Grimoire')
	if iRnd < 20:
		pCaster.cast(gc.getInfoTypeForString('SPELL_SUMMON_SPECTRE'))
	elif iRnd < 40:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_UNHOLY_TAINT'), True)
	elif iRnd < 60:
		pCaster.cast(gc.getInfoTypeForString('SPELL_WITHER'))
	elif iRnd < 70:
		pCaster.cast(gc.getInfoTypeForString('SPELL_SUMMON_PIT_BEAST'))
	elif iRnd < 80:
		pCaster.cast(gc.getInfoTypeForString('SPELL_BURNING_BLOOD'))
	elif iRnd < 90:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)
	else:
		pCaster.cast(gc.getInfoTypeForString('SPELL_SACRIFICE_ALTAR'))

def reqRebuildBarnaxus(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	pCityPlayer = gc.getPlayer(pCity.getOwner())
	if pCaster.getUnitType() == en.eUnitBarnaxus:
		return False
	if pCityPlayer.getCivilizationType() != en.eCivilizationLuchuirp:
		return False
# ent >>>
	if not pCaster.isHuman():
		if pCaster.getOwner() != pCity.getOwner():
			if gc.getPlayer(pCaster.getOwner()).AI_getAttitude(pCity.getOwner()) < AttitudeTypes.ATTITUDE_PLEASED:
				return False
# ent <<<
	return True

def spellRebuildBarnaxus(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pCaster.plot().getPlotCity()
	ePlayer = pCaster.getOwner()
	eCityOwner = pCity.getOwner()
	pCityPlayer = gc.getPlayer(eCityOwner)
	pNewUnit = pCityPlayer.initUnit(en.eUnitBarnaxus, pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
	pNewUnit.setDamage((pNewUnit.maxHitPoints() * 3) // 4, PlayerTypes.NO_PLAYER)
	pNewUnit.changeImmobileTimer(1)
	pCity.applyBuildEffects(pNewUnit)
	if ePlayer != eCityOwner:
		pCityPlayer.AI_changeAttitudeExtra(ePlayer, 2)

def reqRecruit(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	if pCity.getPopulation() < 3:
		return ReasonTypes.REASON_DISABLED_LACK_OF_POPULATION
# ent >>>
	if not pCaster.isHuman():
		if pCaster.getUnitAIType() == UnitAITypes.UNITAI_GENERAL:
			return False
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) == 0:
			return False
		if pCity.getPopulation() < 10:
			return ReasonTypes.REASON_DISABLED_LACK_OF_POPULATION
# ent <<<
	return True

def spellRecruit(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())
	pTeam = gc.getTeam(pCaster.getTeam())
	eCivilization = pPlayer.getCivilizationType()

	lliUnitClasses = [	[	gc.getInfoTypeForString('UNITCLASS_SCOUT'),
							gc.getInfoTypeForString('UNITCLASS_HUNTER'),
							gc.getInfoTypeForString('UNITCLASS_RANGER')			],

						[	gc.getInfoTypeForString('UNITCLASS_SCOUT'),
							gc.getInfoTypeForString('UNITCLASS_HUNTER'),
							gc.getInfoTypeForString('UNITCLASS_ASSASSIN')		],

						[	gc.getInfoTypeForString('UNITCLASS_SCOUT'),
							gc.getInfoTypeForString('UNITCLASS_HORSEMAN'),
							gc.getInfoTypeForString('UNITCLASS_HORSE_ARCHER')	],

						[	gc.getInfoTypeForString('UNITCLASS_WARRIOR'),
							gc.getInfoTypeForString('UNITCLASS_AXEMAN'),
							gc.getInfoTypeForString('UNITCLASS_CHARIOT')		],

						[	gc.getInfoTypeForString('UNITCLASS_WARRIOR'),
							gc.getInfoTypeForString('UNITCLASS_AXEMAN'),
							gc.getInfoTypeForString('UNITCLASS_CHAMPION')		],

						[	gc.getInfoTypeForString('UNITCLASS_WARRIOR'),
							gc.getInfoTypeForString('UNITCLASS_ARCHER'),
							gc.getInfoTypeForString('UNITCLASS_LONGBOWMAN'),
							gc.getInfoTypeForString('UNITCLASS_ARQUEBUS')		],

						[	gc.getInfoTypeForString('UNITCLASS_ADVENTURER'),
							gc.getInfoTypeForString('UNITCLASS_WARRIOR'),
							gc.getInfoTypeForString('UNITCLASS_ADEPT'),
							gc.getInfoTypeForString('UNITCLASS_MAGE')		]	]

#	iNumUnits = max(1, pCity.getPopulation() // 3)
	iNumUnits = pCity.getPopulation()
	if isWorldUnitClass(pCaster.getUnitClassType()):
		if pCity.getNumActiveBuilding(gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_ORDER')) != 0:
			iNumUnits *= 2
		iNumUnits = max(1, iNumUnits // 3)
	for iLoop in xrange(iNumUnits):
		iPromotedPercent = 40
		iUnitLevel = 2

		# select upgrade line
		iLine = CyGame().getSorenRandNum(len(lliUnitClasses), 'Recruit')

		# select tier
		for iUnitClass in reversed(lliUnitClasses[iLine]):
			if CyGame().getSorenRandNum(2, 'Recruit: unit downgrade roll') == 0:
				iUnit = gc.getCivilizationInfo(eCivilization).getCivilizationUnits(iUnitClass)
			else:
				iUnit = gc.getUnitClassInfo(iUnitClass).getDefaultUnitIndex()
			if iUnit == UnitTypes.NO_UNIT:
				iUnitLevel += 1
				continue
			pUnitInfo = gc.getUnitInfo(iUnit)

			# pick up all required techs
			liTechPrereq = [pUnitInfo.getPrereqAndTech()]
			for iIndex in xrange(gc.getNUM_UNIT_AND_TECH_PREREQS()):
				liTechPrereq.append(pUnitInfo.getPrereqAndTechs(iIndex))

			# check required techs
			for iTechPrereq in liTechPrereq:
				if iTechPrereq != TechTypes.NO_TECH:
					if not pTeam.isHasTech(iTechPrereq):
						# if player doesn't have enough techs, downgrade tier and continue checking
						break
			else:
				# if player has enough techs, fix tier
				if CyGame().getSorenRandNum(100, 'Recruit: unit downgrade roll') < 80:
					break
				iUnitLevel += 1
		else:
			iUnit = -1

		if iUnit != -1:
			pNewUnit = pPlayer.initUnit(iUnit, pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
			pNewUnit.setHomeCivilizationType(pCity.getCivilizationType())
			if pNewUnit.getUnitArtStyleType() == UnitArtStyleTypes.NO_UNIT_ARTSTYLE:
				eUnitArtStyle = gc.getCivilizationInfo(pCity.getCivilizationType()).getUnitArtStyleType()
				pNewUnit.setUnitArtStyleType(eUnitArtStyle)
#			pCity.applyBuildEffects(pNewUnit)
			cf.setPromotionRecruitee(pNewUnit, iPromotedPercent)
			iStartingExperience = CyGame().getSorenRandNum(iUnitLevel ** 2 + 1, 'Recruit: Starting experience')
			pNewUnit.changeExperience(iStartingExperience, -1, False, False, False)
			pNewUnit.testPromotionReady()
			pNewUnit.finishMoves()

			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_UNIT_JOIN_YOUR_CAUSE', (pNewUnit.getNameKey(), pCity.getNameKey()))
			szButton = pNewUnit.getButton()
			szSound = pNewUnit.getArtInfo(0, EraTypes.NO_ERA).getTrainSound()
			CyInterface().addMessage(pCaster.getOwner(), False, gc.getEVENT_MESSAGE_TIME(), szMessage, szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)

	if not isWorldUnitClass(pCaster.getUnitClassType()):
		pCaster.kill(True, PlayerTypes.NO_PLAYER)

def reqRecruitMercenary(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
# Kaijin >>>
	if pCaster.getCivilizationType() == en.eCivilizationTiger:
		return False
	eSummonedUnit = gc.getSpellInfo(eSpell).getCreateUnitType()
	eUnitClass = gc.getUnitInfo(eSummonedUnit).getUnitClassType()

	if pPlayer.isProductionMaxedUnitClass(eUnitClass):
		return ReasonTypes.REASON_DISABLED_CLASSCOUNT_LIMIT_SUMMON

# Kaijin <<<
	if not pPlayer.isHuman():
		if pPlayer.getCivilizationType() == en.eCivilizationKhazad:
			return ReasonTypes.REASON_DISABLED_KHAZAD_HATES_MERCENARY
# Kaijin >>>
		if pPlayer.hasTrait(en.eTraitRiches):
			if pPlot.isCity():
				pCity = pPlot.getPlotCity()
				if not (pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED')) or pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED_1')) or pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED_2'))):
					return ReasonTypes.REASON_DISABLED_KHAZAD_HATES_MERCENARY
# Kaijin <<<
# ent >>>
		"""
		pTeam = gc.getTeam(pCaster.getTeam())
		lpRangedUnits = cyGetRangedUnits(pPlot, 1, False, True, pCaster.getTeam())
		for pUnit in lpRangedUnits:
			if pTeam.isAtWar(pUnit.getTeam()):
				return True
		return False
		"""
# ent <<<
	return True

def disabledRecruitMercenary(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pCaster.getCivilizationType() == en.eCivilizationTiger:
		return True

	if not pPlayer.isHuman():
		if pPlayer.getCivilizationType() == en.eCivilizationKhazad:
			return ReasonTypes.REASON_DISABLED_KHAZAD_HATES_MERCENARY
		if pPlayer.hasTrait(en.eTraitRiches):
			if pPlot.isCity():
				pCity = pPlot.getPlotCity()
				if not (pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED')) or pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED_1')) or pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED_2'))):
					return ReasonTypes.REASON_DISABLED_KHAZAD_HATES_MERCENARY

def spellRecruitMercenary(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

# ent >>>
	"""
	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCivilization = gc.getCivilizationInfo(pPlayer.getCivilizationType())
	iUnitClass = gc.getInfoTypeForString('UNITCLASS_MERCENARY')
	iUnit = pCivilization.getCivilizationUnits(iUnitClass)
	pNewUnit = pPlayer.initUnit(iUnit, pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
	pNewUnit.finishMoves()
	if pCaster.getUnitType() == gc.getInfoTypeForString('UNIT_MAGNADINE'):
		pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LOYALTY'), True)
	"""
	liSummonedUnitIDs = argsList[3]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	eSummonedUnit = gc.getSpellInfo(eSpell).getCreateUnitType()
	eUnitClass = gc.getUnitInfo(eSummonedUnit).getUnitClassType()
	pCity = pCaster.plot().getPlotCity()
	pCivilization = gc.getCivilizationInfo(pCity.getCivilizationType())
	eUnit = pCivilization.getCivilizationUnits(eUnitClass)
	eCasterType = pCaster.getUnitType()
	eMagnadine = gc.getInfoTypeForString('UNIT_MAGNADINE')

	for iSummonedUnitID in liSummonedUnitIDs:
		pUnit = pPlayer.getUnit(iSummonedUnitID)
		if not eUnit in (UnitTypes.NO_UNIT, eSummonedUnit):
			pNewUnit = pPlayer.initUnit(eUnit, pUnit.getX(), pUnit.getY(), pUnit.getUnitAIType(), pUnit.getFacingDirection())
			pNewUnit.convert(pUnit)
		else:
			pNewUnit = pUnit
		if eCasterType == eMagnadine:
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LOYALTY'), True)
# ent <<<

def disabledRegeneration(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
		for pUnit in lpRangedUnits:
			if pUnit.isHurt():
				break
		else:
			return True
	return False

def spellReleaseFromCage(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
	for iUnitIndex in xrange(pPlot.getNumUnits(), -1, -1):
		pUnit = pPlot.getUnit(iUnitIndex)
		if pUnit.isHasPromotion(en.ePromotionHeld):
			pUnit.setHasPromotion(en.ePromotionHeld, False)
			if pUnit.isDuration():
				pUnit.setDuration(-1)

def reqReligiousFervor(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	iReligion = pPlayer.getStateReligion()
	if iReligion == ReligionTypes.NO_RELIGION:
		return ReasonTypes.REASON_DISABLED_REQUIRES_STATE_RELIGION
	if not pPlayer.isHuman():
# ent >>>
		"""
		iCount = 0
		for pyCity in PyPlayer(iPlayer).getCityList():
			pCity = pyCity.GetCy()
			if pCity.isHasReligion(iReligion):
				iCount += 1
		if iCount < 5:
			return False
		"""
		if cf.AI_hasRoomForFound(iPlayer):
			return False
# ent <<<
	return True

def spellReligiousFervor(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	iReligion = pPlayer.getStateReligion()
	if iReligion == en.eReligionFellowshipofLeaves:
		liUnit = [gc.getInfoTypeForString('UNIT_PRIEST_OF_LEAVES')]
	elif iReligion == en.eReligionRunesofKilmorph:
		liUnit = [gc.getInfoTypeForString('UNIT_PRIEST_OF_KILMORPH')]
	elif iReligion == en.eReligionEmpyrean:
		liUnit = [gc.getInfoTypeForString('UNIT_PRIEST_OF_THE_EMPYREAN')]
	elif iReligion == en.eReligionOrder:
		liUnit = [gc.getInfoTypeForString('UNIT_PRIEST_OF_THE_ORDER')]
	elif iReligion == en.eReligionOctopusOverlords:
		liUnit = [gc.getInfoTypeForString('UNIT_PRIEST_OF_THE_OVERLORDS')]
	elif iReligion == en.eReligionAshenVeil:
		liUnit = [gc.getInfoTypeForString('UNIT_PRIEST_OF_THE_VEIL')]
	elif iReligion == en.eReligionCouncilofEsus:
		liUnit = [gc.getInfoTypeForString('UNIT_ASSASSIN'), gc.getInfoTypeForString('UNIT_NIGHTWATCH')]
	else:
		return

	iStartingXP = 0
	for pyCity in PyPlayer(iPlayer).getCityList():
		pCity = pyCity.GetCy()
		if pCity.isHasReligion(iReligion):
			iStartingXP += 1
	for pyCity in PyPlayer(iPlayer).getCityList():
		pCity = pyCity.GetCy()
		iUnit = liUnit[CyGame().getSorenRandNum(len(liUnit), 'Religious Fervor')]
		pNewUnit = pPlayer.initUnit(iUnit, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pCity.applyBuildEffects(pNewUnit)
		pNewUnit.changeExperience(iStartingXP, -1, False, False, False)
		pNewUnit.setReligion(iReligion)

		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_UNIT_JOIN_YOUR_CAUSE', (pNewUnit.getNameKey(), pCity.getNameKey()))
		szButton = gc.getUnitInfo(iUnit).getButton()
		CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)

def reqResurrection(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	if pPlayer.getBuriedUnit() != UnitTypes.NO_UNIT:
		return True
	if cf.getDeadHero(ePlayer) != UnitTypes.NO_UNIT:
		return True
	return ReasonTypes.REASON_DISABLED_CIV_HERO_IS_ALIVE_YET

def spellResurrection(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	eHero = cf.getDeadHero(ePlayer)

	if eHero != UnitTypes.NO_UNIT:
		eDeadUnit = eHero
		iDeadExperience = 0
		eBarnUnit = gc.getInfoTypeForString('UNIT_PIECES_OF_BARNAXUS')
		eBarnProm = gc.getInfoTypeForString('PROMOTION_PIECES_OF_BARNAXUS')
		if eHero == en.eUnitBarnaxus:
			szButton = gc.getPromotionInfo(eBarnProm).getButton()
			for eLoopPlayer in xrange(gc.getMAX_PLAYERS()):
				pLoopPlayer = gc.getPlayer(eLoopPlayer)
				if pLoopPlayer.isAlive():
					for pUnit in PyPlayer(eLoopPlayer).getUnitList():
						if pUnit.isHasPromotion(eBarnProm):
							pUnit.setHasPromotion(eBarnProm, False)
							CyInterface().addMessage(eLoopPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_PIECES_LOST', ()), 'AS2D_SPELL_CHARM_PERSON', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pUnit.getX(), pUnit.getY(), True, True)
						if pUnit.getUnitType() == eBarnUnit:
							CyInterface().addMessage(eLoopPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_PIECES_LOST', ()), 'AS2D_SPELL_CHARM_PERSON', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pUnit.getX(), pUnit.getY(), True, True)
							pUnit.kill(True, PlayerTypes.NO_PLAYER)
	else:
		eDeadUnit = pPlayer.getBuriedUnit()
		iDeadExperience = pPlayer.getBuriedUnitExperience()
		pPlayer.setBuriedUnit(UnitTypes.NO_UNIT, 0)

	if eDeadUnit != UnitTypes.NO_UNIT:
		pNewUnit = pPlayer.initUnit(eDeadUnit, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)

		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SPELL_RESURRECTED', (pCaster.getNameKey(), pNewUnit.getNameKey()))
		szButton = pNewUnit.getButton()
		CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pNewUnit.getX(), pNewUnit.getY(), True, True)

		pNewUnit.changeExperience(iDeadExperience, -1, False, False, False)
		pNewUnit.changeImmobileTimer(1)
		for ePromotion in xrange(gc.getNumPromotionInfos()):
			if pNewUnit.isHasPromotion(ePromotion):
				if gc.getPromotionInfo(ePromotion).isEquipment():
					pNewUnit.setHasPromotion(ePromotion, False)

def spellResurrectionGraveyard(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCivilization = gc.getCivilizationInfo(pPlayer.getCivilizationType())
	iUnit = pCivilization.getCivilizationUnits(gc.getInfoTypeForString('UNITCLASS_CHAMPION'))
	if iUnit == UnitTypes.NO_UNIT:
		iUnit = gc.getInfoTypeForString('UNIT_CHAMPION')
	pNewUnit = pPlayer.initUnit(iUnit, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(en.ePromotionHero, True)
	pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)

	szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SPELL_RESURRECTED', (pCaster.getNameKey(), pNewUnit.getNameKey()))
	szButton = pNewUnit.getButton()
	CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pNewUnit.getX(), pNewUnit.getY(), True, True)

def reqReveal(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isIgnoreHide():
		return ReasonTypes.REASON_DISABLED_ALREADY_BUFFED
	if pPlot.getOwner() != pCaster.getOwner():
		return False
	return True

def spellReveal(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pCaster.setIgnoreHide(True)

def reqRevelry(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.getTotalPopulation() < 25:
			return False
	return True

def spellRevelry(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pPlayer.changeGoldenAgeTurns(CyGame().goldenAgeLength() * 2)

def reqRevelation(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	return True

def spellRevelation(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		pTargetPlot.updateCenterUnit()

def reqRiverOfBlood(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getNumCities() == 0:
		return ReasonTypes.REASON_DISABLED_REQUIRES_CITY
	if not pPlayer.isHuman():
# ent >>>
#		if pPlayer.getNumCities() < gc.getWorldInfo(CyMap().getWorldSize()).getTargetNumCities():
#			return False
		if cf.AI_hasRoomForFound(pCaster.getOwner()):
			return False
# ent <<<
	return True

def spellRiverOfBlood(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	lszSounds = ['AS3D_SPELL_FEED', 'AS3D_SPELL_GIFT_VAMPIRISM', 'AS3D_SPELL_SACRIFICE']

	def getPoputationChange():
		if pPlayer.isIgnoreFood():
			iChangePopulation = 1
		else:
			iChangePopulation = max(2, cyFlatValue(max(0, pCity.getPopulation() - 2), 33, True))
		return iChangePopulation

	szButton = gc.getSpellInfo(eSpell).getButton()
	szSpellDescription = gc.getSpellInfo(eSpell).getDescription()
	iTotalExtraDrainPopulation = 0

	iPlayer = pCaster.getOwner()
	for eLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
		pPlayer = gc.getPlayer(eLoopPlayer)
		if pPlayer.isAlive():
			if eLoopPlayer != iPlayer:
				for pyCity in PyPlayer(eLoopPlayer).getCityList():
					pCity = pyCity.GetCy()
					iOldPopulation = pCity.getPopulation()
					iNewPopulation = max(1, iOldPopulation - getPoputationChange())
					iDrainPopulation = iOldPopulation - iNewPopulation
					if iDrainPopulation > 0:
						szSound = lszSounds[CyGame().getSorenRandNum(len(lszSounds), 'River of Blood')]
						szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_RIVER_OF_BLOOD', (szSpellDescription, iDrainPopulation, pCity.getNameKey()))
						CyInterface().addMessage(pCity.getOwner(), False, gc.getEVENT_MESSAGE_TIME(), szMessage, szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCity.getX(), pCity.getY(), True, True)
						pCity.setPopulation(iNewPopulation)
						iTotalExtraDrainPopulation += max(0, iDrainPopulation - 2)

	iNumPlayers = CyGame().countCivPlayersAlive()

	eCasterPlayer = pCaster.getOwner()
	pCasterPlayer = gc.getPlayer(eCasterPlayer)
	iNumRegularCities = pCasterPlayer.getNumCities() - pCasterPlayer.getNumSettlements()
	iTotalPopulation = pCasterPlayer.getTotalPopulation()
	for pyCity in PyPlayer(eCasterPlayer).getCityList():
		pCity = pyCity.GetCy()
		iChangePopulation = 2 + cyFlatValue10000(iTotalExtraDrainPopulation, 10000 // (iNumRegularCities * iNumPlayers), True)
		pCity.changePopulation(iChangePopulation)

def reqRoar(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
# ent >>>
#		if not pUnit.isImmuneToFear():
#			return True
		if pUnit.getReligion() != en.eReligionCultoftheDragon:
			if not pUnit.isImmuneToFear() and not pUnit.plot().isCity():
				return True
		else:
			return True
# ent <<<
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellRoar(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	szButton = gc.getSpellInfo(eSpell).getButton()

	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, False)
	for pUnit in lpRangedUnits:
# Kaijin CultOfTheDragon >>>
#		if not pUnit.isImmuneToFear():
# ent >>>
#		if not pUnit.isImmuneToFear() and not pUnit.getReligion() == gc.getInfoTypeForString('RELIGION_CULT_OF_THE_DRAGON'):
		if pUnit.getReligion() != en.eReligionCultoftheDragon:
			if pUnit.isImmuneToFear() or pUnit.plot().isCity():
				continue
# ent <<<
			if not pUnit.isResisted(pCaster, eSpell):
				pUnit.jumpToAdjacentValidPlotWithForbiddingPlot(pPlot)
				CyInterface().addMessage(pUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_FEAR', (pUnit.getNameKey(), )), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pUnit.getX(), pUnit.getY(), True, True)
				CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_FEAR_ENEMY', (pUnit.getNameKey(), )), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pUnit.getX(), pUnit.getY(), True, True)
# ent >>>
#		if pUnit.getReligion() == gc.getInfoTypeForString('RELIGION_CULT_OF_THE_DRAGON'):
		else:
# ent <<<
			if pUnit.isImmuneToCapture():
				pUnit.kill(True, 0)
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_ROAR_SELF_KILL', (pUnit.getNameKey(), ))
				CyInterface().addMessage(pUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art_Kaijin/Interface/Buttons/Religions/cultofthedragon.dds', en.eColorRed, pUnit.getX(), pUnit.getY(), True, True)
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_ROAR_SELF_KILL_ENEMY', (gc.getPlayer(pUnit.getOwner()).getCivilizationAdjectiveKey(), pUnit.getNameKey()))
				CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art_Kaijin/Interface/Buttons/Religions/cultofthedragon.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			else:
				pNewUnit = pPlayer.initUnit(pUnit.getUnitType(), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
				pNewUnit.convert(pUnit)
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_DOMINATION', (pUnit.getNameKey(), pPlayer.getCivilizationAdjectiveKey(), pCaster.getNameKey()))
				CyInterface().addMessage(pUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art_Kaijin/Interface/Buttons/Religions/cultofthedragon.dds', en.eColorRed, pUnit.getX(), pUnit.getY(), True, True)
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_DOMINATION_ENEMY', (pCaster.getNameKey(), gc.getPlayer(pUnit.getOwner()).getCivilizationAdjectiveKey(), pUnit.getNameKey()))
				CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art_Kaijin/Interface/Buttons/Religions/cultofthedragon.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
# Kaijin CultOfTheDragon <<<

def reqRobGrave(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pPlot.isOwned():
		if pPlot.getOwner() != pCaster.getOwner():
			return ReasonTypes.REASON_DISABLED_IN_RIVAL_BORDER
	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.getAlignment() == en.eAlignmentGood:
			return False
	return True

def spellRobGrave(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	CyGame().changeGlobalCounter(1)
	pPlot = pCaster.plot()
	pPlayer = gc.getPlayer(pCaster.getOwner())
	lszGoody = [	'GOODY_GRAVE_LOW_GOLD', 'GOODY_GRAVE_LOW_GOLD',
					'GOODY_GRAVE_HIGH_GOLD',
					'GOODY_GRAVE_SKELETONS', 'GOODY_GRAVE_SKELETONS',
					'GOODY_GRAVE_SPECTRE'	]
	if pPlayer.canReceiveGoody(pPlot, gc.getInfoTypeForString('GOODY_GRAVE_TECH'), pCaster):
		lszGoody.append('GOODY_GRAVE_TECH')
	iRnd = CyGame().getSorenRandNum(len(lszGoody), 'Pick Goody')
	iGoody = gc.getInfoTypeForString(lszGoody[iRnd])
	pPlayer.receiveGoody(pPlot, iGoody, pCaster)
	pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)

def reqSacrificeAltar(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	iTech = pPlayer.getCurrentResearch()
	if iTech == TechTypes.NO_TECH:
		return ReasonTypes.REASON_DISABLED_HAS_CAST
# Kaijin >>>	patch29 expansion - Start -
	#このターンに一度使用済みなら詠唱不可。
	if pPlayer.getGuildPlusCounter(5) != 0:
		return ReasonTypes.REASON_DISABLED_ALREADY_HAS_CAST
# Kaijin <<<	patch29 expansion - End -
	return True

def spellSacrificeAltar(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pTeam = gc.getTeam(pCaster.getTeam())
	pPlayer = gc.getPlayer(pCaster.getOwner())
	iTech = pPlayer.getCurrentResearch()

# Kaijin >>>	patch29 expansion - Start -
	"""
	iResearchBase = pCaster.getLevel() + gc.getUnitInfo(pCaster.getUnitType()).getTier() - 1
	iResearch = 10 + (iResearchBase ** 2)
	iResearch *= pPlayer.calculateResearchModifier(iTech)
	iResearch = max(1, iResearch // 100)
	"""
	#死亡したユニットの世代で基本値を設定
	iResearchBase = 0
	eUnit = gc.getUnitInfo(pCaster.getUnitType())
	if eUnit.getProductionCost() > 0:
		iResearchBase = eUnit.getProductionCost()
	else:
		if gc.getUnitInfo(unit.getUnitType()).getTier() == 1:
			iResearchBase = 25
		elif gc.getUnitInfo(unit.getUnitType()).getTier() == 2:
			iResearchBase = 60
		elif gc.getUnitInfo(unit.getUnitType()).getTier() == 3:
			iResearchBase = 120
		elif gc.getUnitInfo(unit.getUnitType()).getTier() == 4:
			iResearchBase = 180

	iResearchTimes100 = iResearchBase * 2
	iResearchTimes100 *= pPlayer.calculateResearchModifier(iTech)
	iResearchTimes100 = max(1, iResearchTimes100 // 100)
	#1ターンに一度だけ使用できるようカウンタをセット。
	pPlayer.setGuildPlusCounter(5, 1)
# Kaijin <<<	patch29 expansion - End -

	if iResearchTimes100 < pTeam.getResearchLeft(iTech):
#		pTeam.announceTechToPlayers(iTech, pCaster.getTeam(), iResearchTimes100)
		szMessage = CyTranslator().getText('TXT_KEY_MISC_PROGRESS_TOWARDS_TECH', (iResearchTimes100, gc.getTechInfo(iTech).getDescription()))
		CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorTech, -1, -1, False, False)

	pTeam.changeResearchProgress(iTech, iResearchTimes100, pCaster.getOwner())

def disabledSacrificePyre(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isSummoned():
		return True
	return False

def spellSacrificePyre(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]
	liSummonedUnitIDs = argsList[3]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pPlot = pCaster.plot()
	if pCaster.isImmortal():
##--------	Single Afterlife: Modified by Denev	--------##
#		caster.changeImmortal(-1)
		pCaster.disableImmortal()
##--------	Single Afterlife: End Modify		--------##
	lpSummonedUnits = []
	for iSummonedUnitID in liSummonedUnitIDs:
		lpSummonedUnits.append(pPlayer.getUnit(iSummonedUnitID))
	if isWorldUnitClass(pCaster.getUnitClassType()):
		for pSummonedUnit in lpSummonedUnits:
			pSummonedUnit.kill(False, PlayerTypes.NO_PLAYER)
		customSummonSpellData = CvCustomSummonSpellData()
		customSummonSpellData.eUnit = gc.getSpellInfo(eSpell).getCreateUnitType()
		customSummonSpellData.iNumUnits = 7
		customSummonSpellData.bAbility = gc.getSpellInfo(eSpell).isAbility()
		customSummonSpellData.eDefaultPromotion = en.ePromotionImmortal
		lpNewUnits = pCaster.castCustomSummon(customSummonSpellData)
	else:
#Kaijin >>>
		"""
		iBaseDuration = (pCaster.getLevel() ** 2) * 10
		iExtraDuration = (cyFlatValue(iBaseDuration, g_dGameSpeedPercent["GoldenAge"], True))
		for pSummonedUnit in lpSummonedUnits:
			pSummonedUnit.changeDuration(iExtraDuration)
		"""

		for pSummonedUnit in lpSummonedUnits:
			pSummonedUnit.setHasPromotion(en.ePromotionHeroicStrength, True)
			pSummonedUnit.setHasPromotion(en.ePromotionHeroicStrength2, True)
			pSummonedUnit.setHasPromotion(en.ePromotionHeroicDefense, True)
			pSummonedUnit.setHasPromotion(en.ePromotionHeroicDefense2, True)
			pSummonedUnit.setHasPromotion(en.ePromotionStrong, True)
#Kaijin <<<

	pPoint = pPlot.getPoint()
	CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_RING_OF_FLAMES'), pPoint)
	CyAudioGame().Play3DSound('AS3D_SPELL_FIREBALL', pPoint.x, pPoint.y, pPoint.z)

def disabledSanctify(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		if pCaster.getTeam() != pPlot.getTeam():
			return True
		if pCaster.getCivilizationType() in (en.eCivilizationInfernal, en.eCivilizationDark):
#		if pCaster.getCivilizationType() in (en.eCivilizationInfernal, gc.getInfoTypeForString('CIVILIZATION_SHEAIM')):
			return True
	return False

def enabledSanctify(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, True)
	for pTargetPlot in lpRangedPlots:
#Orbis >>
#		if pTargetPlot.getImprovementType() in (en.eImprovementCityRuins, en.eImprovementGraveyard):
		if pTargetPlot.getImprovementType() in (en.eImprovementCityRuins, en.eImprovementGraveyard, en.eImprovementHauntedRuins):
			return True
#Orbis <<
#		if CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_PLOT_COUNTER):
#			if pTargetPlot.getTerrainType() in g_leHellTerrains:
		if pTargetPlot.getOriginalTerrainType() in g_leHellTerrains:
			if pTargetPlot.getOriginalTerrainType() == pTargetPlot.getTerrainType():
				return True
#		else:
#			if pTargetPlot.getPlotCounter() > 0:
#				return True
	return False

def spellSanctify(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pPlot = pCaster.plot()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
#		if CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_PLOT_COUNTER):
#			eTerrain = pTargetPlot.getTerrainType()
#			if eTerrain in g_leHellTerrains:
#				eEarthyTerrain = gc.getTerrainInfo(eTerrain).getTerrainDown()
#				pTargetPlot.setTerrainType(eEarthyTerrain, False, True)
		if pTargetPlot.getOriginalTerrainType() in g_leHellTerrains:
			eTerrain = pTargetPlot.getTerrainType()
			if pTargetPlot.getOriginalTerrainType() == eTerrain:
				eEarthyTerrain = gc.getTerrainInfo(eTerrain).getTerrainDown()
				pTargetPlot.setOriginalTerrainType(eEarthyTerrain)
				pTargetPlot.setTerrainType(eEarthyTerrain, False, True)

		eImprovement = pTargetPlot.getImprovementType()
		if eImprovement == en.eImprovementSnakePillar:
			pTargetPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
# Kaijin >>>
#		elif eImprovement in (en.eImprovementCityRuins, en.eImprovementGraveyard):
		elif eImprovement in (en.eImprovementCityRuins, en.eImprovementGraveyard, en.eImprovementHauntedRuins):
# Kaijin <<<
			pTargetPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
			CyGame().changeGlobalCounter(-1)

			eSummonSpell = gc.getInfoTypeForString('SPELL_SUMMON_EINHERJAR')
			customSummonSpellData = CvCustomSummonSpellData()
			customSummonSpellData.eUnit = gc.getSpellInfo(eSummonSpell).getCreateUnitType()
			customSummonSpellData.iSummoningPlotIndex = CyMap().plotNum(pTargetPlot.getX(), pTargetPlot.getY())
			customSummonSpellData.bAbility = True
			customSummonSpellData.eEffect = gc.getSpellInfo(eSummonSpell).getEffect()
			customSummonSpellData.szSound = gc.getSpellInfo(eSummonSpell).getSound()
			pCaster.castCustomSummon(customSummonSpellData)

def reqSanctuary(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getNumCities() == 0:
		return ReasonTypes.REASON_DISABLED_REQUIRES_CITY
	if not pPlayer.isHuman():
# ent >>>
		iRatio = cf.AI_getWarSuccessCapitulationRatio(pCaster.getOwner())
		if iRatio < -50 and iRatio > -99:
			return True
# ent <<<
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) < 2:
			return False
	return True

def spellSanctuary(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iPlayer = pCaster.getOwner()
	iTeam = pCaster.getTeam()
	pPlayer = gc.getPlayer(iPlayer)

	iTimer = cyFlatValue(30, g_dGameSpeedPercent["GoldenAge"], True)
	pPlayer.changeSanctuaryTimer(iTimer)
	for iPlotIndex in xrange(CyMap().numPlots()):
		pPlot = CyMap().plotByIndex(iPlotIndex)
		if pPlot.isOwned():
			if pPlot.getOwner() == iPlayer:
				for iUnitIndex in xrange(pPlot.getNumUnits(), -1, -1):
					pUnit = pPlot.getUnit(iUnitIndex)
					if pUnit.getTeam() != iTeam:
						pUnit.jumpToNearestValidPlot()

						"""
def reqScorch(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	liValidTerrain = [	gc.getInfoTypeForString('TERRAIN_PLAINS'),
						gc.getInfoTypeForString('TERRAIN_FIELDS_OF_PERDITION'),
						gc.getInfoTypeForString('TERRAIN_SNOW')	]
	if pPlot.getTerrainType() not in liValidTerrain:
		return False
	if pPlot.isImpassable():
		return False
	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.isHuman():
		if pPlot.getTerrainType() in [gc.getInfoTypeForString('TERRAIN_PLAINS'), gc.getInfoTypeForString('TERRAIN_FIELDS_OF_PERDITION')]:
			if not gc.getTeam(pCaster.getTeam()).isAtWar(pPlot.getTeam()):
				return False
# Kaijin >>> Marsh and Shallow - for Lizardman
		if pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_MARSH') or pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_SHALLOWS'):
			if not gc.getTeam(pCaster.getTeam()).isAtWar(pPlot.getTeam()):
				if pPlayer.getCivilizationType() != gc.getInfoTypeForString('CIVILIZATION_MAZATL') or pPlayer.getCivilizationType() != gc.getInfoTypeForString('CIVILIZATION_CUALLI'):
					return True
# Kaijin <<<
		if pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_SNOW'):
			if pCaster.getTeam() != pPlot.getTeam():
				return False
# Kaijin >>> Blizzard
	bValid = False
	if pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_SNOW'):
		if not pPlayer.isHuman():
			if pCaster.getOwner() != pPlot.getOwner():
				return False
##			if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DOVIELLO'):
##				return False
#			pPlotOwner = gc.getPlayer(pPlot.getOwner())
#			if pPlotOwner.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ILLIANS'):
#				return False
		bValid = True
	iX = pPlot.getX()
	iY = pPlot.getY()
	for iiX in xrange(iX-1, iX+2, 1):
		for iiY in xrange(iY-1, iY+2, 1):
			pPlot = CyMap().plot(iiX,iiY)
			if not pPlot.isNone():
				iFeature = pPlot.getFeatureType()
				if iFeature == gc.getInfoTypeForString('FEATURE_BLIZZARD'):
					bValid = True
	if bValid == True:
		if not pPlayer.isHuman():
			if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ILLIANS'):
				return False
			elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_NIVAL'):
				return False
		return True
# Kaijin <<<
	return False
						"""

def enabledScorch(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

# ent >>>
	if not pCaster.isHuman() or pCaster.isAutomated():
		if pCaster.getCivilizationType() in (en.eCivilizationIllians, en.eCivilizationNival):
			return False

	if pPlot.getFeatureType() == en.eFeatureSwamp:
		return True

	ePlayer = pCaster.getOwner()
	eTeam = pCaster.getTeam()
	iRange = pCaster.getSpellRange(eSpell) + 1
	lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, True, eTeam)
# ent <<<
	for pTargetPlot in lpRangedPlots:
# ent >>>
		if pTargetPlot.isColdCounter():
			if pTargetPlot.isOwned():
				if pTargetPlot.getOwner() == ePlayer:
					return True
# ent <<<
		if pTargetPlot.getFeatureType() == en.eFeatureBlizzard:
			return True
	return False

def disabledScorch(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if gc.getPlayer(pCaster.getOwner()).isCivic(gc.getInfoTypeForString('CIVIC_PRINCIPLE_OF_THE_OLD')):
		return True

	if not pCaster.isHuman() or pCaster.isAutomated():
		pPlotOwner = gc.getPlayer(pPlot.getOwner())
		if pPlot.getTerrainType() == en.eTerrainPlains:
			if not gc.getTeam(pCaster.getTeam()).isAtWar(pPlot.getTeam()):
				return True
		elif pPlot.getTerrainType() == en.eTerrainSnow:
			if pCaster.getTeam() != pPlot.getTeam():
				return True
#			if pCaster.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DOVIELLO'):
#				return True
# Kaijin >>>
			if pPlotOwner.getCivilizationType() in (en.eCivilizationIllians, en.eCivilizationNival):
				return True
		elif pPlot.getTerrainType() == en.eTerrainMarsh or pPlot.getFeatureType() == en.eFeatureSwamp:
			if pCaster.getTeam() != pPlot.getTeam():
				return True
			if pPlotOwner.getCivilizationType() in (en.eCivilizationMazatl, en.eCivilizationCualli):
				return True
# ent: move to enabledScorch >>>
		"""
		if pCaster.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ILLIANS'):
			return True
		elif pCaster.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_NIVAL'):
			return True
		"""
# ent <<<
# Kaijin <<<
	return False

# Kaijin >>>
def spellScorch(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlot = pCaster.plot()
	if pPlot.getFeatureType() == en.eFeatureSwamp:
		pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)

	iRange = pCaster.getSpellRange(eSpell) + 1
	lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, False, TeamTypes.NO_TEAM)
	for pTargetPlot in lpRangedPlots:
# ent >>>
		if pTargetPlot.isColdCounter():
			if pTargetPlot.isOwned():
				if pTargetPlot.getOwner() == ePlayer:
					pTargetPlot.doThawColdCounter(10)
# ent <<<
		if pTargetPlot.getFeatureType() == en.eFeatureBlizzard:
			pTargetPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
# Kaijin <<<

	"""
def spellScorch(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCaster.finishMoves()
	bDeclareWar = False
	if pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_PLAINS'):
		pPlot.setTerrainType(gc.getInfoTypeForString('TERRAIN_DESERT'), True, True)
		bDeclareWar = True
	elif pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_FIELDS_OF_PERDITION'):
		pPlot.setTerrainType(gc.getInfoTypeForString('TERRAIN_BURNING_SANDS'), True, True)
		bDeclareWar = True
	elif pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_SNOW'):
		pPlot.setTerrainType(gc.getInfoTypeForString('TERRAIN_TUNDRA'), True, True)
		if pPlot.isOwned():
			pPlayer = gc.getPlayer(pPlot.getOwner())
			if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ILLIANS'):
				bDeclareWar = True
	if pPlot.isOwned():
		if pPlot.getTeam() != pCaster.getTeam():
			pTeam = gc.getTeam(pCaster.getTeam())
			pTeam.declareWar(pPlot.getTeam(), False, WarPlanTypes.WARPLAN_LIMITED)
	"""

def spellSing(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	point = pPlot.getPoint()
##--------	Unofficial Bug Fix: Modified by Denev	--------##
	"""
	iRnd = CyGame().getSorenRandNum(100, "Sing")
	szText = "AS3D_SING1"
	if iRnd > 25:
		szText = "AS3D_SING2"
	if iRnd > 50:
		szText = "AS3D_SING3"
	if iRnd > 75:
		szText = "AS3D_SING4"
	CyAudioGame().Play3DSound(szText,point.x,point.y,point.z)
	"""
	lszSound = ["AS3D_SING1", "AS3D_SING2", "AS3D_SING3", "AS3D_SING4"]
	szSound = lszSound[CyGame().getSorenRandNum(4, "Sing")]
	CyAudioGame().Play3DSound(szSound, point.x, point.y, point.z)
##--------	Unofficial Bug Fix: End Modify			--------##

def disabledSironasTouch(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.isFeatAccomplished(FeatTypes.FEAT_HEAL_UNIT_PER_TURN):
		return ReasonTypes.REASON_DISABLED_ONLY_ONCE_PER_TURN
	return False

def spellSironasTouch(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pPlayer.setFeatAccomplished(FeatTypes.FEAT_HEAL_UNIT_PER_TURN, False)

# Kaijin OAC >>> for AI
def disabledSlaveTrade(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]


	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)

	pCity = pPlot.getPlotCity()
	if pCaster.isBarbarian():
		return True
	if not pCaster.isHuman():
		if pPlayer.AI_isFinancialTrouble():
			return True
# ent >>>
		iNumCity = pPlayer.getNumCities()
		if pPlayer.getUnitClassCount(en.eUnitClassSlave) > iNumCity:
			return True

		eCiv = pCaster.getCivilizationType()
		if eCiv in (en.eCivilizationDoviello, en.eCivilizationLineage):
			pTeam = gc.getTeam(pCaster.getTeam())
			if pTeam.getAtWarCount(True) > 0:
				if pPlayer.getUnitClassCount(en.eUnitClassWarrior) < iNumCity:
					return False
		elif eCiv == en.eCivilizationBalseraphs:
			if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_HUMAN_CAGE')) == 0:
				return False
		elif eCiv == en.eCivilizationCualli:
			eSlavePit = gc.getInfoTypeForString('BUILDING_SLAVE_PIT')
			if pCity.getNumBuilding(eSlavePit) > 0:
				if pCity.getFreeSpecialistCount(en.eSpecialistCitizen) < 15:
					return False
			for pyCity in PyPlayer(ePlayer).getCityList():
				pLoopCity = pyCity.GetCy()
				if pLoopCity.getNumBuilding(eSlavePit) > 0:
					if pLoopCity.getFreeSpecialistCount(en.eSpecialistCitizen) < 15:
						return True
		elif eCiv == en.eCivilizationDroaum:
			if pPlayer.isIgnoreFood():
				if cf.doAddPopValid(pCity):
					return False
				for pyCity in PyPlayer(ePlayer).getCityList():
					pLoopCity = pyCity.GetCy()
					if cf.doAddPopValid(pLoopCity):
						return True
			pTeam = gc.getTeam(pCaster.getTeam())
			if pTeam.getAtWarCount(True) > 0:
				return False

		if pCity.getFreeSpecialistCount(en.eSpecialistCitizen) < 5:
			return False
		if pCity.getNumActiveBuilding(gc.getInfoTypeForString('BUILDING_ASYLUM')) > 0:
			pTeam = gc.getTeam(pCaster.getTeam())
			if pTeam.getAtWarCount(True) > 0:
				if pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_LUNATIC')) < iNumCity:
					return False
		return True
# ent <<<

	return False
# Kaijin OAC <<<

def spellSlaveTradeBuy(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]
	liSummonedUnitIDs = argsList[3]

	pCity = pCaster.plot().getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())
	pPlot = pCaster.plot()

	for iSlaveUnitID in liSummonedUnitIDs:
		pNewUnit = pPlayer.getUnit(iSlaveUnitID)
		iRnd = CyGame().getSorenRandNum(100, 'Slave Trade Buy')
		if iRnd > 80:
			iPromotion = gc.getInfoTypeForString('PROMOTION_ORC')
		elif iRnd > 70:
			iPromotion = gc.getInfoTypeForString('PROMOTION_ELF')
		elif iRnd > 65:
			iPromotion = gc.getInfoTypeForString('PROMOTION_DARK_ELF')
		elif iRnd > 60:
			iPromotion = gc.getInfoTypeForString('PROMOTION_DWARF')
# Kaijin OAC >>> for Lizardman
		elif iRnd > 50:
			iPromotion = gc.getInfoTypeForString('PROMOTION_LIZARDMAN')
# Kaijin OAC <<<
		else:
			continue
		pNewUnit.setHasPromotion(iPromotion, True)

def spellSnowfall(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	kSpell = gc.getSpellInfo(eSpell)

	iDamage = kSpell.getDamage()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		if not pTargetPlot.isWater():
			iColdCounter = CyGame().getSorenRandNum(600 + iDamage * 60, 'Snowfall') + 1800 + iDamage * 180
			pTargetPlot.ceilColdCounter(iColdCounter, 2000)

def disabledSpring(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if gc.getPlayer(pCaster.getOwner()).isCivic(gc.getInfoTypeForString('CIVIC_PRINCIPLE_OF_THE_OLD')):
		return True

	eSpellSpringExtinguish = gc.getInfoTypeForString('SPELL_SPRING_EXTINGUISH')
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpellSpringExtinguish, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.getImprovementType() == en.eImprovementSmoke or pTargetPlot.getFeatureType() == en.eFeatureFlames:
			return True

	leDesertFeatures = [en.eFeatureOasis, en.eFeatureFloodPlains]
	if pPlot.getFeatureType() in leDesertFeatures:
		return True
# ent >>>
	if pPlot.getTerrainType() == en.eTerrainGrass and pPlot.isHills():
		return True
# ent <<<

# Kaijin >>> Marsh
	"""
	if not pCaster.isHuman():
		if pCaster.getOwner() != pPlot.getOwner():
			return True
		if pCaster.getCivilizationType() == en.eCivilizationInfernal:
			return True
	"""
	if not pCaster.isHuman() or pCaster.isAutomated():
		if pCaster.getOwner() != pPlot.getOwner():
			return True
		if pCaster.getCivilizationType() == en.eCivilizationInfernal:
			return True
# ent >>>
		if pPlot.getTerrainType() == en.eTerrainDesert:
			if pCaster.getCivilizationType() in (en.eCivilizationMalakim, en.eCivilizationAltair):
				return True
			if pPlot.getFeatureType() == en.eFeatureScrub:
				if gc.getPlayer(pCaster.getOwner()).isOption(PlayerOptionTypes.PLAYEROPTION_LEAVE_FORESTS):
					return True
		elif pPlot.getTerrainType() == en.eTerrainGrass:
			if not pCaster.getCivilizationType() in (en.eCivilizationClanofEmbers, en.eCivilizationMazatl, en.eCivilizationCualli, en.eCivilizationBarbarian):
				return True
# ent <<<
# Kaijin <<<
	return False

def reqSpringExtinguish(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.getImprovementType() == en.eImprovementSmoke or pTargetPlot.getFeatureType() == en.eFeatureFlames:
			return True
	return False

def reqStasis(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if CyGame().getProjectCreatedCount(gc.getInfoTypeForString('PROJECT_ASCENSION')) == 0:
		return False
	"""
	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.getNumCities() < gc.getWorldInfo(CyMap().getWorldSize()).getTargetNumCities():
			return False
	"""
	return True

def spellStasis(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

# Kaijin >>>
#	iDelay = cyFlatValue(20, g_dGameSpeedPercent["GoldenAge"], True)
	iDelay = cyFlatValue(100, g_dGameSpeedPercent["GoldenAge"], True)
# Kaijin <<<
	eTeam = pCaster.getTeam()
	for eLoopPlayer in xrange(gc.getMAX_PLAYERS()):
		pLoopPlayer = gc.getPlayer(eLoopPlayer)
		if pLoopPlayer.isAlive():
			if pLoopPlayer.getTeam() != eTeam:
				pLoopPlayer.changeDisableProduction(iDelay)
				pLoopPlayer.changeDisableResearch(iDelay)

def reqSteal(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	eReason = ReasonTypes.REASON_DISABLED_HAS_NO_TARGET
	bHuman = (pCaster.isHuman())
	eTeam = pCaster.getTeam()
	pTeam = gc.getTeam(eTeam)

	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		for iProm in xrange(gc.getNumPromotionInfos()):
			if gc.getPromotionInfo(iProm).isEquipment():
				if pUnit.isHasPromotion(iProm) and not pCaster.isHasPromotion(iProm):
# Kaijin >>>
					if not bHuman:
						if pTeam.isVassal(pUnit.getTeam()):
							continue
# Kaijin <<<
					return True
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, True)
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.isCity():
			pCity = pTargetPlot.getPlotCity()
			for iBuilding in xrange(gc.getNumBuildingInfos()):
				if gc.getBuildingInfo(iBuilding).isEquipment():
					if pCity.getNumRealBuilding(iBuilding) > 0:
						if pCity.getTeam() == eTeam:
							eReason = ReasonTypes.REASON_DISABLED_IMMUNE_FRIENDLY_CITY
							continue
# Kaijin >>>
						if not bHuman:
							if pTeam.isVassal(pCity.getTeam()):
								continue
# Kaijin <<<
						return True
	return eReason

def spellSteal(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()

	ltEquipments = []
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, False)
	for pUnit in lpRangedUnits:
		for iPromotion in xrange(gc.getNumPromotionInfos()):
			if gc.getPromotionInfo(iPromotion).isEquipment():
				if pUnit.isHasPromotion(iPromotion) and not pCaster.isHasPromotion(iPromotion):
					ltEquipments.append((True, iPromotion, pUnit))
	eTeam = pCaster.getTeam()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.isCity() and pTargetPlot.getTeam() != eTeam:
			pCity = pTargetPlot.getPlotCity()
			for iBuilding in xrange(gc.getNumBuildingInfos()):
				if gc.getBuildingInfo(iBuilding).isEquipment():
					if pCity.getNumRealBuilding(iBuilding) > 0:
						ltEquipments.append((False, iBuilding, pCity))

	if len(ltEquipments) > 0:
		iRnd = CyGame().getSorenRandNum(len(ltEquipments), 'Steal Choose Target')
		bPickpocket, iEquipmentIndex, pVictim = ltEquipments[iRnd]
		iSuccessPercent = 60
		if pCaster.isInvisible(pVictim.getTeam(), False):
			iSuccessPercent += 10
		if not bPickpocket:
			for iLoopUnit in xrange(gc.getNumUnitInfos()):
				if gc.getUnitInfo(iLoopUnit).getBuildings(iEquipmentIndex):
					iBuilding = iEquipmentIndex
					iEquipmentIndex = gc.getUnitInfo(iLoopUnit).getEquipmentPromotion()
					break
		kEquipmentPromotion = gc.getPromotionInfo(iEquipmentIndex)
		iRnd = CyGame().getSorenRandNum(100, 'Steal')
		if iRnd < iSuccessPercent:
			if bPickpocket:
				pCaster.setHasPromotion(iEquipmentIndex, True)
				pVictim.setHasPromotion(iEquipmentIndex, False)
			else:
				pVictim.setNumRealBuilding(iBuilding, 0)
				pCaster.setHasPromotion(iEquipmentIndex, True)
			pCaster.finishMoves()
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_STEAL_EQUIPMENT_SUCCESS', (pCaster.getNameKey(), kEquipmentPromotion.getDescription(), gc.getPlayer(pVictim.getOwner()).getCivilizationAdjectiveKey(), pVictim.getNameKey()))
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, kEquipmentPromotion.getButton(), en.eColorGreen, pCaster.getX(), pCaster.getY(), True, True)
		else:
			iFailPercent = (100 - iSuccessPercent)
			if iRnd < iSuccessPercent + (iFailPercent // 2):
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_STEAL_EQUIPMENT_FAIL', (pCaster.getNameKey(), kEquipmentPromotion.getDescription(), gc.getPlayer(pVictim.getOwner()).getCivilizationAdjectiveKey(), pVictim.getNameKey()))
				CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, kEquipmentPromotion.getButton(), en.eColorRed, pCaster.getX(), pCaster.getY(), True, True)
				iTimer = cyFlatValue(3, g_dGameSpeedPercent["GoldenAge"], True)
				pCaster.changeImmobileTimer(iTimer)
			else:
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_STEAL_EQUIPMENT_NOTICED', (pCaster.getNameKey(), kEquipmentPromotion.getDescription(), gc.getPlayer(pVictim.getOwner()).getCivilizationAdjectiveKey(), pVictim.getNameKey()))
				CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, kEquipmentPromotion.getButton(), en.eColorRed, pCaster.getX(), pCaster.getY(), True, True)
				pCaster.kill(True, PlayerTypes.NO_PLAYER)

				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_STEAL_EQUIPMENT_NOTICE', (gc.getPlayer(pCaster.getOwner()).getCivilizationAdjectiveKey(), pCaster.getNameKey(), kEquipmentPromotion.getDescription(), pVictim.getNameKey()))
				CyInterface().addMessage(pVictim.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, kEquipmentPromotion.getButton(), en.eColorGreen, pCaster.getX(), pCaster.getY(), True, True)
				pTeam = gc.getTeam(pCaster.getTeam())
				pTeam.declareWar(pVictim.getTeam(), False, WarPlanTypes.WARPLAN_LIMITED)

def isValidUnitForSummonIllusion(pOriginalUnit, pCaster, iCasterTier, pPlot):
	if pOriginalUnit.canFight():
		if gc.getUnitInfo(pOriginalUnit.getUnitType()).getTier() <= iCasterTier:
			if not isWorldUnitClass(pOriginalUnit.getUnitClassType()):
				if pOriginalUnit.getUnitCombatType() != en.eUnitCombatSiege:
					if pOriginalUnit.getOwner() != pCaster.getOwner() or pOriginalUnit.getID() != pCaster.getID():	# can't copy itself
						if pPlot.isValidDomainForLocation(pOriginalUnit):
							return True
	return False

# ent >>>
def spellSummonAnimal(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]
	liSummonedUnitIDs = argsList[3]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	for iSummonedUnitID in liSummonedUnitIDs:
		pNewUnit = pPlayer.getUnit(iSummonedUnitID)
		if pNewUnit.getUnitAIType() == UnitAITypes.UNITAI_ANIMAL:
			pNewUnit.setUnitAIType(UnitAITypes.UNITAI_ATTACK)
# ent <<<
def disabledSummonGuardianVines(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())

	if not pPlayer.isHuman():
		if not pPlot.isCity():
			return True
		if pPlot.getTeam() != pCaster.getTeam():
			return True
	return False

def reqSummonIllusion(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	iCasterTier = gc.getUnitInfo(pCaster.getUnitType()).getTier()

	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pOriginalUnit in lpRangedUnits:
		if isValidUnitForSummonIllusion(pOriginalUnit, pCaster, iCasterTier, pPlot):
			return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellSummonIllusion(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())

	eIllusion = en.eRaceIllusion
	eHiddenNationality = en.ePromotionHiddenNationality
	pPlot = pCaster.plot()

	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)

	iCasterTier = gc.getUnitInfo(pCaster.getUnitType()).getTier()
	iNumMaxSummonedUnits = max(1, iCasterTier - 1)
	if iNumMaxSummonedUnits > 1:
		iNumTotalUnits = CyGame().getSorenRandNum(iNumMaxSummonedUnits, 'Summon Illusion: pick a unit') + 1
	else:
		iNumTotalUnits = 1

	if pCaster.isTwincast():
		iNumUnits = 1 + pCaster.getTwincast()
	else:
		iNumUnits = 1

	while iNumTotalUnits > 0 and len(lpRangedUnits) > 0:
		iIndex = CyGame().getSorenRandNum(len(lpRangedUnits), 'Summon Illusion: pick a unit')
		pOriginalUnit = lpRangedUnits.pop(iIndex)
		if isValidUnitForSummonIllusion(pOriginalUnit, pCaster, iCasterTier, pPlot):
			eUnitArtStyle = pOriginalUnit.getUnitArtStyleType()
			if eUnitArtStyle == UnitArtStyleTypes.NO_UNIT_ARTSTYLE:
				eUnitArtStyle = gc.getCivilizationInfo(pOriginalUnit.getHomeCivilizationType()).getUnitArtStyleType()
			customSummonSpellData = CvCustomSummonSpellData()
			customSummonSpellData.eUnit = pOriginalUnit.getUnitType()
			customSummonSpellData.iNumUnits = iNumUnits
			customSummonSpellData.iDuration = gc.getDefineINT('SUMMONING_DEFAULT_DURATION_TURNS') + pPlayer.getSummonDuration()
			customSummonSpellData.eDefaultPromotion = eIllusion
			lpNewUnits = pCaster.castCustomSummon(customSummonSpellData)
			for pNewUnit in lpNewUnits:
				pNewUnit.setDamage(pOriginalUnit.getDamage(), PlayerTypes.NO_PLAYER)
				pNewUnit.setLevel(pOriginalUnit.getLevel())
				pNewUnit.setExperience(pOriginalUnit.getExperience(), -1)
# ent >>>
#				pNewUnit.setHasCasted(True)
# ent <<<
				pNewUnit.changeFreePromotionPick(-pNewUnit.getFreePromotionPick())
				pNewUnit.changeFastChant(1)
				pNewUnit.setHasPromotion(eHiddenNationality, False)
				pNewUnit.setName(CyTranslator().getText('TXT_KEY_PROMOTION_ILLUSION', ()))
				pNewUnit.setHomeCivilizationType(pOriginalUnit.getHomeCivilizationType())
				pNewUnit.setUnitArtStyleType(eUnitArtStyle)
			iNumTotalUnits -= 1

def reqTargetFree(argsList):
	return True

def reqTaunt(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if pCaster.isEnemyBetweenUnits(pUnit, pPlot):
			if pUnit.canAttack():
				if pUnit.canMoveInto(pPlot, True, False, True):
					if pUnit.getResistChance(pCaster, eSpell) != 0:
						return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellTaunt(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if pUnit.canAttack():
			if pUnit.canMoveInto(pPlot, True, False, True):
				if not pUnit.isResisted(pCaster, eSpell):
					pUnit.setHasPromotion(en.ePromotionEnraged, True)
					pUnit.attack(pPlot, False)
"""
def reqTreetopDefence(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, False)
	for pUnit in lpRangedUnits:
		if not pUnit.noDefensiveBonus():
			if pUnit.getFortifyTurns() < gc.getDefineINT('MAX_FORTIFY_TURNS'):
				return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellTreetopDefence(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, False)
	for pUnit in lpRangedUnits:
		pUnit.setFortifyTurns(gc.getDefineINT('MAX_FORTIFY_TURNS'))
"""
def reqTrust(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.isFeatAccomplished(FeatTypes.FEAT_TRUST):
		return ReasonTypes.REASON_DISABLED_ONLY_ONCE_PER_GAME
	if pPlayer.isBarbarian():
		return False
	if not pPlayer.isHuman():
		if isWorldUnitClass(pCaster.getUnitClassType()):
			return ReasonTypes.REASON_DISABLED_WORLDUNIT_NOT_ALLOWED
# ent >>>
		if pCaster.isImmortal():
			return ReasonTypes.REASON_DISABLED_IMMORTAL_NOT_ALLOWED
		if pCaster.getLevel() > 6:
			return False
		bHasEquipment = False
		for ePromotion in xrange(gc.getNumPromotionInfos()):
			if pCaster.isHasPromotion(ePromotion):
				if gc.getPromotionInfo(ePromotion).isEquipment():
					bHasEquipment = True
					break
		if bHasEquipment:
			if not pPlot.isCity():
				return False
			if pPlot.getOwner() != pCaster.getOwner():
				return False
# ent <<<
	return True

def spellTrust(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pPlayer.setFeatAccomplished(FeatTypes.FEAT_TRUST, True)

def spellUnyieldingOrder(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	pCity.setOccupationTimer(0)
	pCity.changeHurryAngerTimer(min(pCity.getHurryAngerTimer(), pCity.flatHurryAngerLength()) * -1)
	pCity.changeConscriptAngerTimer(min(pCity.getConscriptAngerTimer(), pCity.flatConscriptAngerLength()) * -1)

def reqUpgradeDovielloWarrior(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isAutomated():
		return False
	if not pCaster.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) == 0:
			return False
		if pCaster.getUnitType() == en.eUnitWorker:
			pPlayer = gc.getPlayer(pCaster.getOwner())
			if pPlayer.getNumCities() >= pPlayer.getUnitClassCount(en.eUnitWorker):
				return False
#		elif pCaster.getUnitType() == gc.getInfoTypeForString('UNIT_SLAVE'):
#			if pPlayer.getStateReligion() == gc.getInfoTypeForString('RELIGION_OCTOPUS_OVERLORDS'):
#				return False
	return True

def reqVeilOfNight(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.getNumUnits() < 25:
			return False
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) > 0:
			return False
	return True

def spellVeilOfNight(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	for pUnit in PyPlayer(pCaster.getOwner()).getUnitList():
##--------	Fractional Combat Strength: Modified by Denev	--------##
#		if pUnit.baseCombatStr() > 0:
		if pUnit.getCombatAttackTimes100() > 0:
##--------	Fractional Combat Strength: End Modify		--------##
			pUnit.setHasPromotion(en.ePromotionHiddenNationality, True)
# Kaijin >>>
## 偵察ユニットをエスス信仰に変更
		if pUnit.getUnitCombatType() == en.eUnitCombatRecon:
			pUnit.setReligion(en.eReligionCouncilofEsus)
# Kaijin <<<

def plotReqVitalize(argsList):
	pPlot = argsList[0]
	eSpell = argsList[1]

	if pPlot.isWater():
		return False
	if pPlot.getTerrainType() == en.eTerrainGrass:
		if pPlot.isRiver() and not pPlot.isHills() and pPlot.getFeatureType() == FeatureTypes.NO_FEATURE:
			return False	# SPELL_VITALIZE_FLOOD_PLAINS is possible
		else:
			return ReasonTypes.REASON_DISABLED_MOST_VITAL_TERRAIN
	elif pPlot.getTerrainType() in g_leHellTerrains:
		return ReasonTypes.REASON_DISABLED_CAN_NOT_VITALIZE_HELL_TERRAIN
	if pPlot.getFeatureType() == en.eFeatureFloodPlains:
		return False
	elif pPlot.getFeatureType() == en.eFeatureOasis:
		return ReasonTypes.REASON_DISABLED_MOST_VITAL_TERRAIN
	return True

def plotReqVitalizeFloodPlains(argsList):
	pPlot = argsList[0]
	eSpell = argsList[1]

	if pPlot.isWater():
		return False
	if not pPlot.isRiver() or pPlot.isHills():
		return False
	if pPlot.getFeatureType() == en.eFeatureFloodPlains:
		return ReasonTypes.REASON_DISABLED_MOST_VITAL_TERRAIN
	elif pPlot.getFeatureType() != FeatureTypes.NO_FEATURE:
		return False
	if pPlot.getTerrainType() != en.eTerrainGrass:
		return False
	elif pPlot.getTerrainType() in g_leHellTerrains:
		return False
	if pPlot.getBonusType(pPlot.getTeam()) != BonusTypes.NO_BONUS:
		return ReasonTypes.REASON_DISABLED_BONUS_EXISTS
	return True

def spellVitalizeFloodPlains(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()

	if pPlot.getBonusType(pPlot.getTeam()) != BonusTypes.NO_BONUS:
		pPlot.setBonusType(BonusTypes.NO_BONUS)

def reqWane(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if isWorldUnitClass(pCaster.getUnitClassType()):
		return ReasonTypes.REASON_DISABLED_WORLDUNIT_NOT_ALLOWED
	if pCaster.getUnitCombatType() in (en.eUnitCombatAnimal, en.eUnitCombatBeast):
		return ReasonTypes.REASON_DISABLED_INVALID_KIND_OF_UNIT
	if pCaster.isImmortal():
		return ReasonTypes.REASON_DISABLED_IMMORTAL_NOT_ALLOWED
# Kaijin >>>
	if gc.getPlayer(pCaster.getOwner()).getGuildPlusCounter(50) <= 0:
		return False
# Kaijin <<<
# ent >>>
	if not pCaster.isHuman():
		if not pPlot.isCity():
			return False
		if pPlot.getOwner() != pCaster.getOwner():
			return False
		if pCaster.getLevel() > 4:
			return False
		if pCaster.getUnitAIType() == UnitAITypes.UNITAI_CITY_DEFENSE:
			return False
		if pPlot.getNumUnits() < 3:
			return False
		if pCaster.getUnitCombatType() in (en.eUnitCombatAdept, en.eUnitCombatDisciple):
			return False
		iRatio = cf.AI_getWarSuccessCapitulationRatio(pCaster.getOwner())
		if iRatio < -20:
			return False
# ent <<<
	return True

# Kaijin >>>
def spellWane(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pPlayer.changeGuildPlusCounter(50, -1)
# Kaijin <<<

def reqWarcry(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.getNumUnits() < 25:
			return False
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) == 0:
			return False
	return True

def spellWarcry(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iWarcry = gc.getInfoTypeForString('PROMOTION_WARCRY')
	for pUnit in PyPlayer(pCaster.getOwner()).getUnitList():
		if pUnit.getUnitCombatType() != UnitCombatTypes.NO_UNITCOMBAT:
			if pUnit.canFight():
				pUnit.setHasPromotion(iWarcry, True)

def reqWildHunt(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) == 0:
			return False
		if pPlayer.getNumUnits() < 20:
			return False
	return True

def spellWildHunt(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iWolf = gc.getSpellInfo(eSpell).getCreateUnitType()
	iWolfStr = gc.getUnitInfo(iWolf).getCombat()
	pPlayer = gc.getPlayer(pCaster.getOwner())
	for pUnit in PyPlayer(pCaster.getOwner()).getUnitList():
		if pUnit.canFight() and not pUnit.isAnimal():
			pNewUnit = pPlayer.initUnit(iWolf, pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
##--------	Fractional Combat Strength: Modified by Denev	--------##
			"""
			iExtraAtt = max(0, pUnit.baseCombatStr() - iWolfStr) // 2
#			iExtraDef = max(0, pUnit.baseCombatStrDefense() - iWolfStr) // 2
			"""
			iExtraAtt = max(0, pUnit.getCombatAttackTimes100() - iWolfStr * 100) // 200
#			iExtraDef = max(0, pUnit.getCombatDefenseTimes100() - iWolfStr * 100) // 200
##--------	Fractional Combat Strength: End Modify		--------##
			liExtraPromotions = [	en.ePromotionHeroicStrength,
									en.ePromotionHeroicStrength2,
									en.ePromotionStrong	]
			for iLoop in xrange(min(len(liExtraPromotions), iExtraAtt)):
				pNewUnit.setHasPromotion(liExtraPromotions[iLoop], True)
			pNewUnit.setUnitAIType(UnitAITypes.UNITAI_ATTACK_CITY)

def spellWonder(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iCount = CyGame().getSorenRandNum(3, 'Wonder: the number of effects') + 3
	pPlayer = gc.getPlayer(pCaster.getOwner())
	pPlot = pCaster.plot()
	bCity = pPlot.isCity()
	pPoint = pPlot.getPoint()
	iDuration = gc.getDefineINT('SUMMONING_DEFAULT_DURATION_TURNS') + pPlayer.getSummonDuration()
	leSpells = [	gc.getInfoTypeForString('SPELL_BLAZE'),
					gc.getInfoTypeForString('SPELL_BLESS'),
					gc.getInfoTypeForString('SPELL_BLINDING_LIGHT'),
					gc.getInfoTypeForString('SPELL_BLOOM'),
					gc.getInfoTypeForString('SPELL_BLUR'),
					gc.getInfoTypeForString('SPELL_CHARM_PERSON'),
					gc.getInfoTypeForString('SPELL_CONTAGION'),
					gc.getInfoTypeForString('SPELL_COURAGE'),
					gc.getInfoTypeForString('SPELL_CRUSH'),
					gc.getInfoTypeForString('SPELL_DESTROY_UNDEAD'),
					gc.getInfoTypeForString('SPELL_DISPEL_MAGIC'),
					gc.getInfoTypeForString('SPELL_EARTHQUAKE'),
					gc.getInfoTypeForString('SPELL_ENCHANTED_BLADE'),
					gc.getInfoTypeForString('SPELL_ENTANGLE'),
					gc.getInfoTypeForString('SPELL_ESCAPE'),
					gc.getInfoTypeForString('SPELL_FIREBALL'),
					gc.getInfoTypeForString('SPELL_FLAMING_ARROWS'),
					gc.getInfoTypeForString('SPELL_FLOATING_EYE'),
					gc.getInfoTypeForString('SPELL_HASTE'),
					gc.getInfoTypeForString('SPELL_HASTURS_RAZOR'),
					gc.getInfoTypeForString('SPELL_HEAL'),
					gc.getInfoTypeForString('SPELL_HIDE'),
					gc.getInfoTypeForString('SPELL_LOYALTY'),
					gc.getInfoTypeForString('SPELL_MAELSTROM'),
					gc.getInfoTypeForString('SPELL_MORALE'),
					gc.getInfoTypeForString('SPELL_MUTATION'),
					gc.getInfoTypeForString('SPELL_PILLAR_OF_FIRE'),
					gc.getInfoTypeForString('SPELL_POISONED_BLADE'),
					gc.getInfoTypeForString('SPELL_REVELATION'),
					gc.getInfoTypeForString('SPELL_RING_OF_FLAMES'),
					gc.getInfoTypeForString('SPELL_RUST'),
					gc.getInfoTypeForString('SPELL_SANCTIFY'),
					gc.getInfoTypeForString('SPELL_SCORCH'),
					gc.getInfoTypeForString('SPELL_SHADOWWALK'),
					gc.getInfoTypeForString('SPELL_SPORES'),
					gc.getInfoTypeForString('SPELL_SPRING'),
					gc.getInfoTypeForString('SPELL_STONESKIN'),
					gc.getInfoTypeForString('SPELL_SUMMON_AIR_ELEMENTAL'),
					gc.getInfoTypeForString('SPELL_SUMMON_AUREALIS'),
					gc.getInfoTypeForString('SPELL_SUMMON_BALOR'),
					gc.getInfoTypeForString('SPELL_SUMMON_DJINN'),
					gc.getInfoTypeForString('SPELL_SUMMON_EARTH_ELEMENTAL'),
					gc.getInfoTypeForString('SPELL_SUMMON_EINHERJAR'),
					gc.getInfoTypeForString('SPELL_SUMMON_FIRE_ELEMENTAL'),
					gc.getInfoTypeForString('SPELL_SUMMON_MISTFORM'),
					gc.getInfoTypeForString('SPELL_SUMMON_PIT_BEAST'),
					gc.getInfoTypeForString('SPELL_SUMMON_SAND_LION'),
					gc.getInfoTypeForString('SPELL_SUMMON_SPECTRE'),
					gc.getInfoTypeForString('SPELL_SUMMON_WATER_ELEMENTAL'),
					gc.getInfoTypeForString('SPELL_SUMMON_WRAITH'),
					gc.getInfoTypeForString('SPELL_TSUNAMI'),
					gc.getInfoTypeForString('SPELL_VALOR'),
					gc.getInfoTypeForString('SPELL_VITALIZE'),
					gc.getInfoTypeForString('SPELL_WITHER'),
					gc.getInfoTypeForString('SPELL_SLOW'),
					gc.getInfoTypeForString('SPELL_SUMMON_ICE_ELEMENTAL'),
					gc.getInfoTypeForString('SPELL_SNOWFALL')	]
	for iLoop in xrange(iCount):
		iRnd = CyGame().getSorenRandNum(len(leSpells) + 9, 'Wonder: select effect')
		if iRnd < len(leSpells):
			eSpell = leSpells[iRnd]
			pCaster.cast(eSpell)
		elif iRnd == len(leSpells) + 0:
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_SPELL_WONDER_DEFILE', ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorSpell, pPlot.getX(), pPlot.getY(), False, False)
			CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPELL1'), pPoint)
			CyAudioGame().Play3DSound('AS3D_SPELL_DEFILE', pPoint.x, pPoint.y, pPoint.z)
			iRange = 1
			lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, False, TeamTypes.NO_TEAM)
			for pTargetPlot in lpRangedPlots:
# Kaijin OAC - Hell Terrain fix
				iFeature = pTargetPlot.getFeatureType()
				iBonus = pTargetPlot.getBonusType(TeamTypes.NO_TEAM)
				pTargetPlot.setPlotCounter(100)
				if iBonus != BonusTypes.NO_BONUS:
					if gc.getImprovementInfo(en.eImprovementFarm).isImprovementBonusTrade(iBonus):
						pTargetPlot.setImprovementType(en.eImprovementSnakePillar)
				if iFeature == en.eFeatureFloodPlains:
					pTargetPlot.setFeatureType(en.eFeatureObsidianPlains, 0)
# Kaijin OAC - end
		elif iRnd == len(leSpells) + 1:
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_SPELL_WONDER_SANCTIFY_PLUS', ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorSpell, pPlot.getX(), pPlot.getY(), False, False)
			CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPELL1'), pPoint)
			CyAudioGame().Play3DSound('AS3D_SPELL_SANCTIFY', pPoint.x, pPoint.y, pPoint.z)
			iRange = 2
			lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, False, TeamTypes.NO_TEAM)
			for pTargetPlot in lpRangedPlots:
				pTargetPlot.setPlotCounter(0)
		elif iRnd == len(leSpells) + 2:
			eSpell = gc.getInfoTypeForString('SPELL_SUMMON_KRAKEN')
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), gc.getSpellInfo(eSpell).getDescription(), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getSpellInfo(eSpell).getButton(), en.eColorSpell, pPlot.getX(), pPlot.getY(), True, True)
			lpNewUnits = pCaster.castSummon(eSpell, UnitAITypes.NO_UNITAI)
			for pNewUnit in lpNewUnits:
				pNewUnit.setDuration(iDuration)
		elif iRnd == len(leSpells) + 3:
			eSpell = gc.getInfoTypeForString('SPELL_SUMMON_TIGER')
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), gc.getSpellInfo(eSpell).getDescription(), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getSpellInfo(eSpell).getButton(), en.eColorSpell, pPlot.getX(), pPlot.getY(), True, True)
			lpNewUnits = pCaster.castSummon(eSpell, UnitAITypes.NO_UNITAI)
			for pNewUnit in lpNewUnits:
				pNewUnit.setDuration(iDuration)
		elif iRnd == len(leSpells) + 4:
			eSpell = gc.getInfoTypeForString('SPELL_SUMMON_TREANT')
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), gc.getSpellInfo(eSpell).getDescription(), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getSpellInfo(eSpell).getButton(), en.eColorSpell, pPlot.getX(), pPlot.getY(), True, True)
			lpNewUnits = pCaster.castSummon(eSpell, UnitAITypes.NO_UNITAI)
			for pNewUnit in lpNewUnits:
				pNewUnit.setDuration(iDuration)
		elif iRnd == len(leSpells) + 5:
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_SPELL_WONDER_SUMMON_PENGUINS', ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorSpell, pPlot.getX(), pPlot.getY(), False, False)
			if not bCity:
				iImprovement = pPlot.getImprovementType()
				if iImprovement != ImprovementTypes.NO_IMPROVEMENT:
					if gc.getImprovementInfo(iImprovement).isPermanent():
						continue
				iPenguin = gc.getInfoTypeForString('IMPROVEMENT_PENGUINS')
				pPlot.setImprovementType(iPenguin)
				szButton = gc.getImprovementInfo(iPenguin).getButton()
				CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_WONDER_PENGUINS', ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
		elif iRnd == len(leSpells) + 6:
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_SPELL_WONDER_MUSHROOMS', ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorSpell, pPlot.getX(), pPlot.getY(), False, False)
			if not bCity:
				iImprovement = pPlot.getImprovementType()
				if iImprovement != ImprovementTypes.NO_IMPROVEMENT:
					if gc.getImprovementInfo(iImprovement).isPermanent():
						continue
# Kaijin OAC >>>
						"""
				iMushroom = gc.getInfoTypeForString('IMPROVEMENT_MUSHROOMS')
				pPlot.setImprovementType(iMushroom)
				szButton = gc.getImprovementInfo(iMushroom).getButton()
						"""
				iMushroom = gc.getInfoTypeForString('BONUS_MUSHROOMS')
				pPlot.setBonusType(iMushroom)
				szButton = gc.getBonusInfo(iMushroom).getButton()
# Kaijin OAC <<<
				CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_WONDER_MUSHROOMS', ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
		elif iRnd == len(leSpells) + 7:
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_SPELL_WONDER_TRANSFORM_BABOON', ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorSpell, pPlot.getX(), pPlot.getY(), False, False)
			for iProm in xrange(gc.getNumPromotionInfos()):
				if pCaster.isHasPromotion(iProm):
					if gc.getPromotionInfo(iProm).isRace():
						pCaster.setHasPromotion(iProm, False)
			pCaster.setUnitArtStyleType(gc.getInfoTypeForString('UNIT_ARTSTYLE_BABOON'))
			szButton = gc.getUnitInfo(gc.getInfoTypeForString('UNIT_MARGALARD')).getButton()
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_WONDER_BABOON', ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			if pPlayer.isHuman():
				szTorophyKey = 'TROPHY_FEAT_BABOON'
				if not CyGame().isHasTrophy(szTorophyKey):
					CyGame().changeTrophyValue(szTorophyKey, 1)
		elif iRnd == len(leSpells) + 8:
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_SPELL_WONDER_SUMMON_SPIDERKIN', ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorSpell, pPlot.getX(), pPlot.getY(), False, False)
			eUnit = gc.getInfoTypeForString('UNIT_SPIDERKIN')
			customSummonSpellData = CvCustomSummonSpellData()
			customSummonSpellData.eUnit = eUnit
#			customSummonSpellData.iDuration = iDuration
			pCaster.castCustomSummon(customSummonSpellData)
			szButton = gc.getUnitInfo(eUnit).getButton()
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_WONDER_SPIDERKIN', ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorGreen, pPlot.getX(), pPlot.getY(), False, False)

def reqWorldbreak(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	iCount = CyGame().getGlobalCounter()
	if iCount == 0:
		return ReasonTypes.REASON_DISABLED_REQUIRES_GLOBAL_COUNTER
	if not pCaster.isHuman():
		if iCount < 50:
			return False
	return True
"""
def spellWorldbreak(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iCounter = CyGame().getGlobalCounter()
	for iPlotIndex in xrange(CyMap().numPlots()):
		pPlot = CyMap().plotByIndex(iPlotIndex)
		if pPlot.getTeam() != pCaster.getTeam():
			if pPlot.isCity():
				continue
"""
def atRangeGuardian(argsList):
	pPlot = argsList[1]

	if pPlot.getNumUnits() == 0:
		iGraceTurns = cyFlatValue(20, g_dGameSpeedPercent["GoldenAge"], False)
		if iGraceTurns < CyGame().getElapsedGameTurns(): #fixes a problem if units spawn next to the gargoyle
			pCaster = argsList[0]
			iPlayer = pCaster.getOwner()
			pPlayer = gc.getPlayer(iPlayer)
			if not pPlayer.isBarbarian():
				pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
				for iLoop in xrange(3):
					pNewUnit = pBarbarianPlayer.initUnit(en.eUnitGargoyle, pPlot.getX(), pPlot.getY(), UnitAITypes.UNITAI_ANIMAL, DirectionTypes.DIRECTION_SOUTH)
					pNewUnit.jumpToNearestValidPlot()
##--------	Unofficial Bug Fix: Modified by ent	--------##
#				CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_GUARDIAN", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getUnitInfo(en.eUnitGargoyle).getButton(),ColorTypes(8), pPlot.getX(), pPlot.getY(), True, True)
				CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_GUARDIAN", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getUnitInfo(en.eUnitGargoyle).getButton(), en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
				pPlot.setPythonActive(False)
##--------	Unofficial Bug Fix: End Modify			--------##

def atRangeJungleAltar(argsList):
	if CyGame().getWBMapScript():
		sf.atRangeJungleAltar(argsList)

def atRangeNecrototem(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]

	if cf.doFear(pCaster, pPlot, -1, False):
		CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_FEAR", (gc.getUnitInfo(pCaster.getUnitType()).getDescription(), )), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Improvements/Necrototem.dds',en.eColorRed, pCaster.getX(), pCaster.getY(), True, True)

def atRangeAncientForest(argsList):
	pUnit = argsList[0]
	pPlot = argsList[1]
	eFeature = argsList[2]

	if not pPlot.isOwned():
		return

	pPlotOwner = gc.getPlayer(pPlot.getOwner())
	if pPlotOwner.getStateReligion() != en.eReligionFellowshipofLeaves:
		return

	pPlotTeam = gc.getTeam(pPlot.getTeam())
	if not pPlotTeam.isAtWar(pUnit.getTeam()):
		return

	if pPlot.isVisibleEnemyUnit(pPlot.getOwner()):
		return

	if not pUnit.canMoveOrAttackInto(pPlot, False):
		return

	iChance = gc.getDefineINT('TREANT_SPAWN_CHANCE')
	pCity = pPlot.getWorkingCity()
	if not pCity.isNone():
		if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_TEMPLE_OF_LEAVES')):
			iChance *= 3

	if CyGame().getSorenRandNum(100, 'Treant Spawn Chance') < iChance:
		pUnit.getGroup().clearMissionQueue()

		iDuration = 3
		pNewUnit = pPlotOwner.initUnit(gc.getInfoTypeForString('UNIT_TREANT'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit.setDuration(iDuration)

		pPlot.setFeatureType(en.eFeatureForestNew, -1)

		szButton = pNewUnit.getButton()
# ent - Treant has Invisible Animal >>>
		if not pNewUnit.isInvisible(pUnit.getTeam(), False):
			szMoveInMessage = CyTranslator().getText('TXT_KEY_MESSAGE_TREANT_ENEMY', (pNewUnit.getNameKey(), gc.getFeatureInfo(eFeature).getDescription()))
		else:
			szMoveInMessage = CyTranslator().getText('TXT_KEY_MESSAGE_UNKNOWN_ENEMY', ())
#		szMoveInMessage = CyTranslator().getText('TXT_KEY_MESSAGE_TREANT_ENEMY', (pNewUnit.getNameKey(), gc.getFeatureInfo(eFeature).getDescription()))
# ent <<<
		if pCity.isNone():
			szDefenderMessage = CyTranslator().getText('TXT_KEY_MESSAGE_TREANT', (pNewUnit.getNameKey(), gc.getFeatureInfo(eFeature).getDescription()))
		else:
			szDefenderMessage = CyTranslator().getText('TXT_KEY_MESSAGE_TREANT_NEAR_CITY', (pNewUnit.getNameKey(), gc.getFeatureInfo(eFeature).getDescription(), pCity.getNameKey()))
		CyInterface().addMessage(pUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMoveInMessage, 'AS2D_FEATUREGROWTH', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pNewUnit.getX(), pNewUnit.getY(), True, True)
		CyInterface().addMessage(pPlot.getOwner(), False, gc.getEVENT_MESSAGE_TIME(), szDefenderMessage, 'AS2D_FEATUREGROWTH', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pNewUnit.getX(), pNewUnit.getY(), True, True)
		CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_NATURE_SUMMON'), pPlot.getPoint())

def onMoveBlizzard(argsList):
	pCaster = argsList[0]
# ent: for Nival mainly (frequent messages is troublesome) >>>
#	if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_WINTERBORN')):
#		pCaster.doDamage(10, 50, gc.getInfoTypeForString('DAMAGE_COLD'))
	if not pCaster.canFight():
		return
	if pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_WINTERBORN')):
		return
	if pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COLD_RESISTANCE')):
		return
	if pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_FROSTLING')):
		return
	if pCaster.getDamageTypeResist(en.eDamageCold) == 100:
		return
	if pCaster.getDamage() > 50:
		return
	pCaster.doDamage(10, 50, en.eDamageCold)
# ent <<<

def onMoveLetumFrigus(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]

	if pCaster.isHuman():
		iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(), 'EVENTTRIGGER_LETUM_FRIGUS')
		pPlayer = gc.getPlayer(pCaster.getOwner())
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#		triggerData = pPlayer.initTriggeredData(iEvent, True, -1, pCaster.getX(), pCaster.getY(), pCaster.getOwner(), -1, -1, -1, -1, -1)
		pPlayer.triggerCustomEvent(iEvent, -1, pCaster.getX(), pCaster.getY(), PlayerTypes.NO_PLAYER, -1, ReligionTypes.NO_RELIGION, CorporationTypes.NO_CORPORATION, -1, BuildingTypes.NO_BUILDING)
##--------	Unofficial Bug Fix: End Modify			--------##
		szButton = gc.getImprovementInfo(pPlot.getImprovementType()).getButton()
		CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_LETUM_FRIGUS', ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
		pPlot.setPythonActive(False)

#More Events Mod Begins#
def onMoveBrokenSepulcher(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	if pPlayer.getGuildPlusCounter(1) == 6:
		if pCaster.isHasPromotion(en.eEquipmentGela):
			pCaster.setHasPromotion(en.eEquipmentGela, False)
			for pyCity in PyPlayer(pCaster.getOwner()).getCityList():
				pCity = pyCity.GetCy()
				if CyGame().getSorenRandNum(100, "Mane") <= 60:
					pNewUnit = pPlayer.initUnit(en.eUnitManes, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
				if pCity.getPopulation() > 2:
					pCity.changePopulation(-2)
			szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_GELA_BROKEN", ())
			szButton = gc.getImprovementInfo(pPlot.getImprovementType()).getButton()
			CyInterface().addMessage(ePlayer, True, 25, szMessage, '', 1, szButton, en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
#More Events Mod End#

def onMoveMaelstrom(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]

	szButton = gc.getImprovementInfo(pPlot.getImprovementType()).getButton()
# Kaijin >>>
	"""
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#	if CyGame().getSorenRandNum(100, "Maelstrom") <= 25:
	if CyGame().getSorenRandNum(100, 'Maelstrom') < 25:
##--------	Unofficial Bug Fix: End Modify			--------##
		CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_MAELSTROM_KILL',()), 'AS2D_FEATUREGROWTH', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
		pCaster.kill(True, PlayerTypes.NO_PLAYER)
	else:
		iOcean = gc.getInfoTypeForString('TERRAIN_OCEAN')
		iBestValue = 0
		pBestPlot = -1
		for iPlotIndex in xrange(CyMap().numPlots()):
			iValue = 0
			pTargetPlot = CyMap().plotByIndex(iPlotIndex)
			if pTargetPlot.getTerrainType() == iOcean:
				iFeature = pTargetPlot.getFeatureType()
				if iFeature != FeatureTypes.NO_FEATURE and gc.getFeatureInfo(iFeature).isImpassable():
					continue
				iValue = CyGame().getSorenRandNum(1000, 'Maelstrom')
				if not pTargetPlot.isOwned():
					iValue += 1000
				if iValue > iBestValue:
					iBestValue = iValue
					pBestPlot = pTargetPlot
		if pBestPlot != -1:
			pCaster.setXY(pBestPlot.getX(), pBestPlot.getY(), False, True, True)
			iDamage = CyGame().getSorenRandNum(100, 'Maelstrom Damage')
			pCaster.changeDamage(iDamage, PlayerTypes.NO_PLAYER)
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_MAELSTROM_MOVE',()), 'AS2D_FEATUREGROWTH', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCaster.getX(), pCaster.getY(), True, True)
	"""
#More Events Mod Begins#
	pPlayer = gc.getPlayer(pCaster.getOwner())
	'''
	## ゲラのイベントにて大渦潮が選択されていて、進入ユニットがゲラを所持している
	if pPlayer.getGuildPlusCounter(1) == 3 and pCaster.isHasPromotion(en.eEquipmentGela):
		pCaster.setHasPromotion(en.eEquipmentGela, False)
		iMobility1 = gc.getInfoTypeForString('PROMOTION_WATER_WALKING')
		iHero = gc.getInfoTypeForString('PROMOTION_HERO')
	'''
	if pPlayer.getGuildPlusCounter(1) == 3:
		pEquipedUnit = -1
		if pCaster.isHasPromotion(en.eEquipmentGela):
			pEquipedUnit = pCaster
		elif pCaster.hasCargo():
			iCasterID = pCaster.getID()
			for iUnitIndex in xrange(pPlot.getNumUnits()):
				pLoopUnit = pPlot.getUnit(iUnitIndex)
				if pLoopUnit.isCargo() and pLoopUnit.getTransportUnit().getID() == iCasterID:
					if pLoopUnit.isHasPromotion(en.eEquipmentGela):
						pEquipedUnit = pLoopUnit
						break
		if pEquipedUnit != -1:
			pEquipedUnit.setHasPromotion(en.eEquipmentGela, False)
			iMobility1 = gc.getInfoTypeForString('PROMOTION_WATER_WALKING')
			iHero = en.ePromotionHero
			## プレイヤーが深海の旧支配者を採用していればユニットが与えられる
			if  pPlayer.getStateReligion() == en.eReligionOctopusOverlords:
				pCapital = pPlayer.getCapitalCity()
				pCapitalPlot = pCapital.plot()
				pClearPlot = cf.findAdjacentClearPlot(pCaster.getOwner(), pPlot.getX(), pPlot.getY(), True, False)
				if pClearPlot is None:
					pClearPlot = pCapitalPlot
				ltStartingUnits = [	(4,	gc.getInfoTypeForString('UNIT_STYGIAN_GUARD'),				[iMobility1]		),
									(1,	gc.getInfoTypeForString('UNIT_DISCIPLE_OCTOPUS_OVERLORDS'),	[iMobility1, iHero]	)	]
				for iNumUnits, eUnit, lePromotions in ltStartingUnits:
					for iLoop in xrange(iNumUnits):
#						pNewUnit = pPlayer.initUnit(eUnit, iCapitalX, iCapitalY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
						pNewUnit = pPlayer.initUnit(eUnit, pClearPlot.getX(), pClearPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
						for ePromotions in lePromotions:
							pNewUnit.setHasPromotion(ePromotions, True)

				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_MAELSTROM_GELA_1', ())
				szColor= en.eColorGreen
			## 旧支配者を採用していなければ世界各地に蛮族が出現する
			else:
# ent >>>
				iStygianChance = 1000
				iSeaSerpentChance = 300
				pAnimalPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER() + en.eBarbarianAnimal)

				eStygian = gc.getInfoTypeForString('UNIT_STYGIAN_GUARD')
				eSerpent = gc.getInfoTypeForString('UNIT_SEA_SERPENT')
				for i in xrange (CyMap().numPlots()):
					pPlot = CyMap().plotByIndex(i)
					if pPlot.isWater():
						if pPlot.isImpassable():
							continue
						if pPlot.isLake():
							continue
						if pPlot.getNumUnits() == 0:
							"""
							if CyGame().getSorenRandNum(10000, "Stygian") <= iStygianChance:
								pNewUnit = pAnimalPlayer.initUnit(gc.getInfoTypeForString('UNIT_STYGIAN_GUARD'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
								pNewUnit.setUnitAIType(UnitAITypes.UNITAI_ANIMAL)
								pNewUnit.setHasPromotion(iMobility1, True)
							if CyGame().getSorenRandNum(10000, "SeaSerpent") <= iStygianChance:
								pNewUnit = pAnimalPlayer.initUnit(gc.getInfoTypeForString('UNIT_SEA_SERPENT'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
								pNewUnit.setUnitAIType(UnitAITypes.UNITAI_ANIMAL)
								pNewUnit.setHasPromotion(iMobility1, True)
							"""
							if pPlot.getTerrainType() == en.eTerrainCoast:
								if CyGame().getSorenRandNum(10000, "Stygian") <= iStygianChance:
									pNewUnit = pAnimalPlayer.initUnit(eStygian, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
									pNewUnit.setUnitAIType(UnitAITypes.UNITAI_ANIMAL)
									pNewUnit.setHasPromotion(iMobility1, True)
							elif pPlot.getTerrainType() == en.eTerrainOcean:
								if CyGame().getSorenRandNum(10000, "SeaSerpent") <= iSeaSerpentChance:
									pNewUnit = pAnimalPlayer.initUnit(eSerpent, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
									pNewUnit.setUnitAIType(UnitAITypes.UNITAI_ANIMAL)
									pNewUnit.setHasPromotion(iMobility1, True)
# ent <<<

				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_MAELSTROM_GELA_2', ())
				szColor= en.eColorRed
			szSound = 'AS2D_FEATUREGROWTH'
			CyInterface().addMessage(pCaster.getOwner(),True,25,szMessage,szSound,1,szButton,szColor,pCaster.getX(),pCaster.getY(),True,True)
			pCaster.kill(True, PlayerTypes.NO_PLAYER)
			return
#More Events Mod End#

	if CyGame().getSorenRandNum(100, 'Maelstrom') <= 25:
		CyInterface().addMessage(pCaster.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_MAELSTROM_KILL",()),'AS2D_FEATUREGROWTH',1,'Art/Interface/Buttons/Improvements/Maelstrom.dds',en.eColorRed,pPlot.getX(),pPlot.getY(),True,True)
		pCaster.kill(True, PlayerTypes.NO_PLAYER)
	else:
		iOcean = en.eTerrainOcean
		iBestValue = 0
		pBestPlot = -1
		for i in xrange (CyMap().numPlots()):
			iValue = 0
			pTargetPlot = CyMap().plotByIndex(i)
			if pTargetPlot.getTerrainType() == iOcean:
				iValue = CyGame().getSorenRandNum(1000, 'Maelstrom')
				if not pTargetPlot.isOwned():
					iValue += 1000
				if iValue > iBestValue:
					iBestValue = iValue
					pBestPlot = pTargetPlot
		if pBestPlot != -1:
			pCaster.setXY(pBestPlot.getX(), pBestPlot.getY(), False, True, True)
			pCaster.setDamage(25, PlayerTypes.NO_PLAYER)
			CyInterface().addMessage(pCaster.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_MAELSTROM_MOVE",()),'AS2D_FEATUREGROWTH',1,'Art/Interface/Buttons/Improvements/Maelstrom.dds',en.eColorRed,pCaster.getX(),pCaster.getY(),True,True)
# Kaijin <<<

def onMoveMirrorOfHeaven(argsList):
	if CyGame().getWBMapScript():
		sf.onMoveMirrorOfHeaven(argsList)

#More Events Mod Begins#
	pCaster = argsList[0]
	pPlot = argsList[1]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getGuildPlusCounter(1) == 7:
		if pCaster.isHasPromotion(en.eEquipmentGela):
			pCaster.setHasPromotion(en.eEquipmentGela, False)
			CyInterface().addMessage(pCaster.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_GELA_MIRROR",()),'AS2D_FEATUREGROWTH',1,'Art/Interface/Buttons/Improvements/Mirror Of Heaven.dds',en.eColorGreen,pCaster.getX(),pCaster.getY(),True,True)
			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SOL'), True)

			eChampion = gc.getInfoTypeForString('UNIT_CHAMPION')
			eInfernalPlayer = cf.getCivilization(en.eCivilizationInfernal)
			if eInfernalPlayer != PlayerTypes.NO_PLAYER:
				pDemonPlayer = gc.getPlayer(eInfernalPlayer)
			else:
				pDemonPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER() + en.eBarbarianDemons)
			eEnemyTeam = pDemonPlayer.getTeam()
			pTeam = gc.getTeam(pPlayer.getTeam())
			pTeam.declareWar(eEnemyTeam, True, WarPlanTypes.WARPLAN_TOTAL)

			iRange = 2
			lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, False, TeamTypes.NO_TEAM)
			for pTargetPlot in lpRangedPlots:
				if pTargetPlot.isWater():
					continue
				if pTargetPlot.getNumUnits() > 0:
					continue
				if pTargetPlot.isCity():
					continue
				eImprovement = pTargetPlot.getImprovementType()
				if eImprovement != ImprovementTypes.NO_IMPROVEMENT:
					if gc.getImprovementInfo(eImprovement).isPermanent():
						continue
				if pTargetPlot.isFlatlands():
					if CyGame().getSorenRandNum(500, "Hellfire") <= 400:
						pTargetPlot.setImprovementType(en.eImprovementHellfire)
						pNewUnit = pDemonPlayer.initUnit(eChampion, pTargetPlot.getX(), pTargetPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
						pNewUnit.setHasPromotion(en.eRaceDemon, True)
#More Events Mod End#

def onMovePoolOfTears(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]

	liCurePromotions = [	gc.getInfoTypeForString('PROMOTION_POISONED'),
							gc.getInfoTypeForString('PROMOTION_DISEASED'),
							gc.getInfoTypeForString('PROMOTION_PLAGUED'),
							gc.getInfoTypeForString('PROMOTION_WITHERED')	]
	lszCured = []
	for iCurePromotion in liCurePromotions:
		if pCaster.isHasPromotion(iCurePromotion):
			pCaster.setHasPromotion(iCurePromotion, False)
			lszCured.append(gc.getPromotionInfo(iCurePromotion).getDescription())
	if len(lszCured) > 0:
		iImprovement = pPlot.getImprovementType()
		szButton = gc.getImprovementInfo(iImprovement).getButton()
		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_CURED_POOL_OF_TEARS_LIST', (pCaster.getNameKey(), gc.getImprovementInfo(iImprovement).getDescription()))
		szMessage += ', '.join(lszCured)
		CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_FEATUREGROWTH', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCaster.getX(), pCaster.getY(), True, True)

#More Events Mod Begins#
	pPlayer = gc.getPlayer(pCaster.getOwner())

	## ゲラのイベントにて涙の池が選択されていて、進入ユニットがゲラを所持している
	if pPlayer.getGuildPlusCounter(1) == 2 and pCaster.isHasPromotion(en.eEquipmentGela):
		pCaster.setHasPromotion(en.eEquipmentGela, False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PIKE_OF_TEARS'), True)

		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_TEARS_GELA', ())
		iImprovement = pPlot.getImprovementType()
		szButton = gc.getImprovementInfo(iImprovement).getButton()
		szSound = 'AS2D_FEATUREGROWTH'
		CyInterface().addMessage(pCaster.getOwner(), True, 25, szMessage, szSound, 1, szButton, en.eColorGreen, pCaster.getX(), pCaster.getY(), True, True)

		## プレイヤーが緑葉の同胞を採用していれば低確率で世界各地の荒廃が起きる
		## 緑葉の同胞を採用していなければ高確率で世界各地の荒廃が起きる
		if pPlayer.getStateReligion() != en.eReligionFellowshipofLeaves or CyGame().getSorenRandNum(100, "Plague") <= 40:
			if CyGame().getSorenRandNum(100, "Plague") <= 50:
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_TEARS_GELA_PLAGUE', ())
				CyInterface().addMessage(pCaster.getOwner(), True, 25, szMessage, szSound, 1, szButton, en.eColorRed, pCaster.getX(), pCaster.getY(), True, True)
				for eLoopPlayer in xrange(gc.getMAX_PLAYERS()):
					pLoopPlayer = gc.getPlayer(eLoopPlayer)
					if pLoopPlayer.isAlive() and pLoopPlayer.getCivilizationType() != en.eCivilizationInfernal:
						py = PyPlayer(eLoopPlayer)
						for pyCity in py.getCityList():
							pCity = pyCity.GetCy()
							i = CyGame().getSorenRandNum(5, "Blight")
							i += pCity.getPopulation() - 2
							i -= pCity.totalGoodBuildingHealth()
							pCity.changeEspionageHealthCounter(i)
						for pUnit in py.getUnitList():
							if pUnit.isAlive():
								pUnit.doDamage(10, 100, en.eDamageDeath)

def onMovePyreOfTheSeraphic(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getGuildPlusCounter(1) == 5:
		if pCaster.isHasPromotion(en.eEquipmentGela):
			iImprovement = pPlot.getImprovementType()
			pCaster.setHasPromotion(en.eEquipmentGela, False)
			if CyGame().getSorenRandNum(100, "Pyre") <= 40:
				pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
				pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FROZEN_FLAME'), True)
				szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_TEARS_GELA_PYRE_1",())
			else:
				iBaseNumber = gc.getWorldInfo(CyMap().getWorldSize()).getDefaultPlayers()
				iNumBonuses = CyGame().getSorenRandNum(iBaseNumber, "Pyre of the Seraphic") + CyGame().getSorenRandNum(iBaseNumber, "Pyre of the Seraphic") + 1
				iNumBonuses = (iBaseNumber + iNumBonuses + 1) // 2
				cf.addBonus(gc.getInfoTypeForString('BONUS_MANA'), iNumBonuses)
				szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_TEARS_GELA_PYRE_2",())
			szButton = gc.getImprovementInfo(iImprovement).getButton()
			szSound = 'AS2D_FEATUREGROWTH'
			CyInterface().addMessage(pCaster.getOwner(),True,25,szMessage,szSound,1,szButton,en.eColorGreen,pCaster.getX(),pCaster.getY(),True,True)

#More Events Mod ends

def onMoveJungleAltar(argsList):
	if CyGame().getWBMapScript():
		sf.onMoveJungleAltar(argsList)

def onMovePortal(argsList):
	if CyGame().getWBMapScript():
		sf.onMovePortal(argsList)

def onMoveWarningPost(argsList):
	if CyGame().getWBMapScript():
		sf.onMoveWarningPost(argsList)

def voteFundDissidents():
	iOvercouncil = gc.getInfoTypeForString('DIPLOVOTE_OVERCOUNCIL')
	for iPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
		pPlayer = gc.getPlayer(iPlayer)
		if pPlayer.isAlive():
			if pPlayer.isFullMember(iOvercouncil):
				iBaseAnger = 3
				for pyCity in PyPlayer(iPlayer).getCityList():
					pCity = pyCity.GetCy()
					iUnitPeriod = pCity.flatDefyResolutionAngerLength()
					iAngerTimer = CyGame().getSorenRandNum(iUnitPeriod * (iBaseAnger + 1), 'Fund Dissidents')
					iAngerTimer = max(0, iAngerTimer - iUnitPeriod)
					pCity.changeDefyResolutionAngerTimer(iAngerTimer)

#Tougou Start
"""
def reqMurasamaBlade(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pNest = pPlayer.getCapitalCity()
	iNestPop = pNest.getPopulation()
	if iNestPop > 0:
		return True
	return False
"""
def spellMurasamaBlade(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	pCity = pPlayer.getCapitalCity()
	pPlayer.initUnit(gc.getInfoTypeForString('UNIT_MURAMASA_BLADE_ECHIGO'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
def effectKuruma(argsList):
	pCaster = argsList[0]

	iX = pCaster.getX()
	iY = pCaster.getY()
	pPlayer = gc.getPlayer(pCaster.getOwner())
	iTeam = pPlayer.getTeam()
	eTeam = gc.getTeam(iTeam)
	iNaoe = -1
	for iiX in xrange(iX-4, iX+5, 1):
		for iiY in xrange(iY-4, iY+5, 1):
			pPlot = CyMap().plot(iiX,iiY)
			if not pPlot.isNone():
				for i in xrange(pPlot.getNumUnits()):
					pUnit = pPlot.getUnit(i)
					if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_NAOE'):
						iNaoe = 1
						break
	if iNaoe == -1:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_KURUMA_ECHIGO'), False)
"""
# Kaijin <<< End

def reqZintoushiki(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	eSikon = gc.getInfoTypeForString('PROMOTION_SUIKOU_ECHIGO')
	eHoushi = gc.getInfoTypeForString('PROMOTION_HOUSHI_ECHIGO')
	eKikkou = gc.getInfoTypeForString('PROMOTION_KIKKOU_ECHIGO')
	eMamori = gc.getInfoTypeForString('PROMOTION_MAMORI_ECHIGO')
	eHoujutu = gc.getInfoTypeForString('PROMOTION_HOUJUTU_ECHIGO')

	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if pUnit.getLevel() >= 5:
			eUnitCombat = pUnit.getUnitCombatType()
			if eUnitCombat == en.eUnitCombatMelee:
				if not pUnit.isHasPromotion(eSikon):
					return True
			elif eUnitCombat == en.eUnitCombatMounted:
				if not pUnit.isHasPromotion(eHoushi):
					return True
			elif eUnitCombat == en.eUnitCombatArcher:
				if not pUnit.isHasPromotion(eKikkou):
					return True
			elif eUnitCombat == en.eUnitCombatDisciple:
				if not pUnit.isHasPromotion(eMamori):
					return True
			elif eUnitCombat == en.eUnitCombatSiege:
				if not pUnit.isHasPromotion(eHoujutu):
					return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellZintoushiki(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	eSikon = gc.getInfoTypeForString('PROMOTION_SUIKOU_ECHIGO')
	eHoushi = gc.getInfoTypeForString('PROMOTION_HOUSHI_ECHIGO')
	eKikkou = gc.getInfoTypeForString('PROMOTION_KIKKOU_ECHIGO')
	eMamori = gc.getInfoTypeForString('PROMOTION_MAMORI_ECHIGO')
	eHoujutu = gc.getInfoTypeForString('PROMOTION_HOUJUTU_ECHIGO')
	szButton = gc.getSpellInfo(eSpell).getButton()
	szCasterName = pCaster.getNameKey()
	ePlayer = pCaster.getOwner()

	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if pUnit.getLevel() >= 5:
			eUnitCombat = pUnit.getUnitCombatType()
			eProm = PromotionTypes.NO_PROMOTION
			if eUnitCombat == en.eUnitCombatMelee:
				if not pUnit.isHasPromotion(eSikon):
					pUnit.setHasPromotion(eSikon, True)
					eProm = eSikon
			elif eUnitCombat == en.eUnitCombatMounted:
				if not pUnit.isHasPromotion(eHoushi):
					pUnit.setHasPromotion(eHoushi, True)
					eProm = eHoushi
			elif eUnitCombat == en.eUnitCombatArcher:
				if not pUnit.isHasPromotion(eKikkou):
					pUnit.setHasPromotion(eKikkou, True)
					eProm = eKikkou
			elif eUnitCombat == en.eUnitCombatDisciple:
				if not pUnit.isHasPromotion(eMamori):
					pUnit.setHasPromotion(eMamori, True)
					eProm = eMamori
			elif eUnitCombat == en.eUnitCombatSiege:
				if not pUnit.isHasPromotion(eHoujutu):
					pUnit.setHasPromotion(eHoujutu, True)
					eProm = eHoujutu
			if eProm != PromotionTypes.NO_PROMOTION:
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_ZINTOU_ECHIGO', (szCasterName, pUnit.getNameKey(), ))
				CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pUnit.getX(), pUnit.getY(), True, True)

def reqNAIOU_ECHIGO(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isAlwaysHostile(pPlot):
		return ReasonTypes.REASON_DISABLED_NATIONALITY_IS_HIDDEN

	iResistMax = 95
	if not pCaster.isHuman():
		iResistMax = 20

	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if not isWorldUnitClass(pUnit.getUnitClassType()):
			iResist = pUnit.getResistChance(pCaster, eSpell)
			if iResist <= iResistMax:
				return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellNAIOU_ECHIGO(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	eKuruma = gc.getInfoTypeForString('PROMOTION_KURUMA_ECHIGO')
	eLoyalty = gc.getInfoTypeForString('PROMOTION_LOYALTY')
	szButton = gc.getSpellInfo(eSpell).getButton()
	szCasterName = pCaster.getNameKey()

	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if pUnit.isImmuneToCapture() or isWorldUnitClass(pUnit.getUnitClassType()):
			pUnit.setHasPromotion(eKuruma, True)
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_NAIOU_ECHIGO_ANGRY', (pUnit.getNameKey(), szCasterName, ))
			CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pUnit.getX(), pUnit.getY(), True, True)
		elif pUnit.isResisted(pCaster, eSpell):
			pUnit.setHasPromotion(eLoyalty, True)
			pUnit.setHasPromotion(eKuruma, True)
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_NAIOU_ECHIGO_ANGRY', (pUnit.getNameKey(), szCasterName, ))
			CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pUnit.getX(), pUnit.getY(), True, True)
		else:
			pNewUnit = pPlayer.initSkeletalUnit(pUnit.getUnitType(), pCaster.getX(), pCaster.getY(), pUnit.getUnitAIType())
			pNewUnit.convert(pUnit)
			pNewUnit.changeImmobileTimer(1)
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_DOMINATION', (pUnit.getNameKey(), pPlayer.getCivilizationAdjectiveKey(), szCasterName))
			CyInterface().addMessage(pUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pUnit.getX(), pUnit.getY(), True, True)
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_DOMINATION_ENEMY', (szCasterName, gc.getPlayer(pUnit.getOwner()).getCivilizationAdjectiveKey(), pUnit.getNameKey()))
			CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)

def spellHarakiri_Echigo(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	kSpell = gc.getSpellInfo(eSpell)
	iDamage = 20 + pCaster.getExperience()
	iDamageLimit = 60 + pCaster.getExperience()
	eDamageType = kSpell.getDamageType()
	szButton = kSpell.getButton()
	ePlayer = pCaster.getOwner()
	szCasterName = pCaster.getNameKey()

	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, False)
	for pUnit in lpRangedUnits:
# ent >>>
		iActualDamage = pUnit.doDamage(iDamage, iDamageLimit, eDamageType)
		if iActualDamage > 0:
			eColor = en.eColorGreen
		else:
			eColor = en.eColorRed
		if pUnit.getDamage() < 100:
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_HARAKIRI_ECHIGO', (szCasterName, pUnit.getNameKey(), iActualDamage, ))
		else:
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_HARAKIRI_ECHIGO_KILL', (szCasterName, pUnit.getNameKey(), iActualDamage, ))
		CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, eColor, pUnit.getX(), pUnit.getY(), True, True)
# ent <<<

#Droaum
def reqUndeadInSacrifice(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

# ent >>>
	"""
	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.isHuman():
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_BRONZE_WORKING')):
			return True
		elif pPlayer.getNumUnits() < 30:
			return False
	"""
	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.isHuman():
		if not cf.AI_hasRoomForFound(pCaster.getOwner()):
			return True
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_BRONZE_WORKING')) or pPlayer.isHasTech(gc.getInfoTypeForString('TECH_ARCHERY')):
			return False
		pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
		if not pBarbarianPlayer.isHasTech(gc.getInfoTypeForString('TECH_BRONZE_WORKING')) and not pBarbarianPlayer.isHasTech(gc.getInfoTypeForString('TECH_ARCHERY')):
			return False
# ent <<<
	return True

def spellUndeadInSacrifice(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	py = PyPlayer(pCaster.getOwner())
	eZonbie = gc.getInfoTypeForString('UNIT_ZOMBIE_CITIZEN')
# ent >>>
	"""
	for pUnit in py.getUnitList():
		if pUnit.canFight():
			if not pUnit.isSummoned():
				if pUnit.getUnitCombatType() == en.eUnitCombatMelee:
					iWeaponExtraAttack = 0
					eWeapon = pCaster.getWeapon()
					if eWeapon != WeaponTypes.NO_WEAPON:
						eWeaponPromotion = gc.getWeaponInfo(eWeapon).getWeaponPromotion()
						if eWeaponPromotion != PromotionTypes.NO_PROMOTION:
							iWeaponExtraAttack = gc.getPromotionInfo(eWeaponPromotion).getExtraCombatStr()

					if (pUnit.getCombatAttackTimes100() - iWeaponExtraAttack * 100) <= 500:
						if not isWorldUnitClass(pUnit.getUnitClassType()):
							if not pUnit.isDuration():
								pNewUnit = pPlayer.initUnit(eZonbie, pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
								pNewUnit.convert(pUnit)
	"""
	eSlave = gc.getInfoTypeForString('UNIT_SLAVE')
	eWeak = gc.getInfoTypeForString('PROMOTION_WEAK')
	for pUnit in py.getUnitList():
		if pUnit.getUnitType() == eSlave and not pUnit.isDuration():
			pNewUnit = pPlayer.initUnit(eZonbie, pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit.convert(pUnit)
	for pyCity in py.getCityList():
		pCity = pyCity.GetCy()
		pNewUnit = pPlayer.initUnit(eZonbie, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit.setHasPromotion(eWeak, True)
# ent <<<

def reqAddCityDroaum(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.isIgnoreFood():
		return False
	if not cf.doAddPopValid(pCity):
		return False
	return True

def reqExperimentDroaum(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	iTech = pPlayer.getCurrentResearch()
	if iTech == TechTypes.NO_TECH:
		return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET
	
	if not pCaster.isHuman():
		if pPlayer.isIgnoreFood() and pPlot.isCity() and cf.doAddPopValid(pPlot.getPlotCity()):
			return False
		if pCaster.getLevel() < 4:
			return False
	return True

def spellExperimentDroaum(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	iCasterID = pCaster.getID()
	pPlot = pCaster.plot()
	pTeam = gc.getTeam(pCaster.getTeam())
	eTech = pPlayer.getCurrentResearch()
	iNum = 1 + (pCaster.getLevel() * pCaster.getLevel())

	pTeam.changeResearchProgress(eTech, iNum, ePlayer)
	pCaster.changeExperience(1, -1, False, False, False)
	eSlave = gc.getSpellInfo(eSpell).getUnitInStackPrereq()
	pVictim = -1
	for i in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(i)
		if pUnit.getOwner() == ePlayer:
			if pUnit.getUnitType() == eSlave:
				if pVictim == -1 or pVictim.getExperience() > pUnit.getExperience():
					if pUnit.getID() != iCasterID:
						pVictim = pUnit
	if pVictim != -1:
		pVictim.kill(False, PlayerTypes.NO_PLAYER)

def reqPromotionDroaum(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		iCount = CyGame().getGlobalCounter()
		if iCount <= 30:
			return False
		if iCount < pCaster.getLevel() * 10:
			return False
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.isIgnoreFood() and pPlot.isCity() and cf.doAddPopValid(pPlot.getPlotCity()):
			return False

	return True

def spellPromotionDroaum(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iCount = CyGame().getGlobalCounter()
	iExpPoints = CyGame().getSorenRandNum(3, "Impersonate Leader")
	if iCount <= 30:
		iExpPoints += CyGame().getSorenRandNum(3, "Impersonate Leader")
	elif (iCount >= 31 and iCount <= 40):
		iExpPoints += CyGame().getSorenRandNum(6, "Impersonate Leader")
	elif (iCount >= 41 and iCount <= 50):
		iExpPoints += CyGame().getSorenRandNum(9, "Impersonate Leader")
	elif (iCount >= 51 and iCount <= 60):
		iExpPoints += CyGame().getSorenRandNum(12, "Impersonate Leader")
	elif (iCount >= 61 and iCount <= 70):
		iExpPoints += CyGame().getSorenRandNum(15, "Impersonate Leader")
	elif (iCount >= 71 and iCount <= 80):
		iExpPoints += CyGame().getSorenRandNum(18, "Impersonate Leader")
	elif (iCount >= 81 and iCount <= 90):
		iExpPoints += CyGame().getSorenRandNum(21, "Impersonate Leader")
	elif (iCount >= 91 and iCount <= 99):
		iExpPoints += CyGame().getSorenRandNum(24, "Impersonate Leader")
	else: #iCount == 100:
		iExpPoints += CyGame().getSorenRandNum(27, "Impersonate Leader")

	pCaster.changeExperience(iExpPoints, -1, False, False, False)
	
	ePlayer = pCaster.getOwner()
	iCasterID = pCaster.getID()
	eSlave = gc.getSpellInfo(eSpell).getUnitInStackPrereq()
	pVictim = -1
	pPlot = pCaster.plot()
	for i in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(i)
		if pUnit.getOwner() == ePlayer:
			if pUnit.getUnitType() == eSlave:
				if pVictim == -1 or pVictim.getExperience() > pUnit.getExperience():
					if pUnit.getID() != iCasterID:
						pVictim = pUnit
	if pVictim != -1:
		pVictim.kill(False, PlayerTypes.NO_PLAYER)

def disabledZombiepowderDroaum(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAnyWarPlanCount(True) == 0:
			if pPlot.isCity():
				return True
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.isIgnoreFood() and pPlot.isCity() and cf.doAddPopValid(pPlot.getPlotCity()):
			return True
	return False

def reqOvereatDroaum(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.getDamage() == 0:
		return ReasonTypes.REASON_DISABLED_FULL_STOMACH_BLOODY
	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.isIgnoreFood() and pPlot.isCity() and cf.doAddPopValid(pPlot.getPlotCity()):
			return False
		if pCaster.getDamage() < 40:
			return False
	return True

def spellOvereatDroaum(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	ePlayer = pCaster.getOwner()
	iCasterID = pCaster.getID()
	eSlave = gc.getSpellInfo(eSpell).getUnitInStackPrereq()
	pVictim = -1
	for iUnitIndex in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(iUnitIndex)
		if pUnit.getOwner() == ePlayer:
			if pUnit.getUnitType() == eSlave:
				if pVictim == -1 or pVictim.getExperience() > pUnit.getExperience():
					if pUnit.getID() != iCasterID:
						pVictim = pUnit
	if pVictim != -1:
		pVictim.kill(False, PlayerTypes.NO_PLAYER)

# ent >>>
def disabledDeathBreathDroaum(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	iCount = CyGame().getGlobalCounter()
	if iCount == 0:
		return ReasonTypes.REASON_DISABLED_REQUIRES_GLOBAL_COUNTER

	if not pCaster.isHuman():
		if iCount < 50:
			return True
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.isIgnoreFood() and pPlot.isCity() and cf.doAddPopValid(pPlot.getPlotCity()):
			return True
		lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, True)
		for pTargetPlot in lpRangedPlots:
			if pTargetPlot.isCity():
				if pTargetPlot.isEnemyCity(pCaster):
					break
		else:
			return True
	return False
# ent <<<
def spellDeathBreathDroaum(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	ePlayer = pCaster.getOwner()
	iCasterID = pCaster.getID()
	eSlave = gc.getSpellInfo(eSpell).getUnitInStackPrereq()
	pVictim = -1
	for iUnitIndex in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(iUnitIndex)
		if pUnit.getOwner() == ePlayer:
			if pUnit.getUnitType() == eSlave:
				if pVictim == -1 or pVictim.getExperience() > pUnit.getExperience():
					if pUnit.getID() != iCasterID:
						pVictim = pUnit
	if pVictim != -1:
		pVictim.kill(False, PlayerTypes.NO_PLAYER)

def reqDecoyHeartDroaum(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	iCount = CyGame().getGlobalCounter()
	if pCaster.getLevel() < 10 and iCount < 100:
		return False
	if pCaster.isImmortal():
		return ReasonTypes.REASON_DISABLED_ALREADY_BUFFED

	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.isIgnoreFood() and pPlot.isCity() and cf.doAddPopValid(pPlot.getPlotCity()):
			return False

	return True

def spellDecoyHeartDroaum(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	ePlayer = pCaster.getOwner()
	iCasterID = pCaster.getID()
	eSlave = gc.getSpellInfo(eSpell).getUnitInStackPrereq()
	pVictim = -1
	for iUnitIndex in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(iUnitIndex)
		if pUnit.getOwner() == ePlayer:
			if pUnit.getUnitType() == eSlave:
				if pVictim == -1 or pVictim.getExperience() > pUnit.getExperience():
					if pUnit.getID() != iCasterID:
						pVictim = pUnit
	if pVictim != -1:
		pVictim.kill(False, PlayerTypes.NO_PLAYER)

#NIRAIKANAI
def reqGenesis(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getNumCities() == 0:
		return ReasonTypes.REASON_DISABLED_REQUIRES_CITY
	if not pPlayer.isHuman():
# ent >>>
#		if pPlayer.getNumCities() < gc.getWorldInfo(CyMap().getWorldSize()).getTargetNumCities():
#			return False
		if cf.AI_hasRoomForFound(pCaster.getOwner()):
			return False
# ent <<<
	return True

def spellGenesis(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iPlayer = pCaster.getOwner()
	cf.genesis(iPlayer)

def spellOmikuzi(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	szButton = gc.getSpellInfo(eSpell).getButton()
	iRnd = CyGame().getSorenRandNum(100, "omikuzi")
	if iRnd < 45:
		lList = ['UNIT_WOLF_NIRAIKANAI', 'UNIT_LION', 'UNIT_GORILLA_NIRAIKANAI', 'UNIT_BEAR_NIRAIKANAI', 'UNIT_TIGER', 'UNIT_ELEPHANT', 'UNIT_GRIFFON_NIRAIKANAI']

		customSummonSpellData = CvCustomSummonSpellData()
		customSummonSpellData.eUnit = gc.getInfoTypeForString(lList[CyGame().getSorenRandNum(len(lList), "Summon Animal")])
		customSummonSpellData.bAbility = True
		customSummonSpellData.iNumUnits = 1
		customSummonSpellData.eEffect = gc.getInfoTypeForString('EFFECT_BLOOM')
		customSummonSpellData.szSound = 'AS3D_SPELL_BLOOM'
		lpNewUnits = pCaster.castCustomSummon(customSummonSpellData)

		CyInterface().addMessage(pCaster.getOwner(), True, 25, CyTranslator().getText("TXT_KEY_MESSAGE_SUMMON_ANIMAL", ()), '', 1, szButton, en.eColorGreen, pCaster.getX(), pCaster.getY(), True, True)

	elif iRnd < 50:
		pCaster.cast(gc.getInfoTypeForString('SPELL_REGENERATION'))
	elif iRnd < 60:
		pCaster.cast(gc.getInfoTypeForString('SPELL_SHIELD_OF_FAITH'))
	elif iRnd < 65:
		pCaster.cast(gc.getInfoTypeForString('SPELL_HEAL'))
	elif iRnd < 80:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FATIGUED'), True)
		CyInterface().addMessage(pCaster.getOwner(),True,25,CyTranslator().getText("TXT_KEY_PROMOTION_FATIGUED", ()),'',1,szButton,en.eColorRed,pCaster.getX(),pCaster.getY(),True,True)
	elif iRnd < 90:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAKEN'), True)
		CyInterface().addMessage(pCaster.getOwner(),True,25,CyTranslator().getText("TXT_KEY_PROMOTION_WEAKEN", ()),'',1,szButton,en.eColorRed,pCaster.getX(),pCaster.getY(),True,True)
	else:
		pCaster.cast(gc.getInfoTypeForString('SPELL_BLESS'))

#TOKOYAMI
def reqSoranaki(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if CyGame().getGlobalCounter() < 50:
		return False
	return True

def spellSoranaki(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	eChampion = gc.getInfoTypeForString('UNIT_CHAMPION')
	eDemon = en.eRaceDemon
	eHellfire = en.eImprovementHellfire
	iHellfireChance = gc.getDefineINT('HELLFIRE_CHANCE')

	pPlayer = gc.getPlayer(pCaster.getOwner())
	eDemonPlayer = gc.getBARBARIAN_PLAYER() + en.eBarbarianDemons
	pDemonPlayer = gc.getPlayer(eDemonPlayer)

	for iPlotIndex in xrange(CyMap().numPlots()):
		pPlot = CyMap().plotByIndex(iPlotIndex)
		if pPlot.getNumUnits() == 0:
			if pPlot.canHaveImprovement(eHellfire, PlayerTypes.NO_PLAYER, False):
				if pPlot.getBonusType(TeamTypes.NO_TEAM) == BonusTypes.NO_BONUS:
					iImprovement = pPlot.getImprovementType()
					if iImprovement == ImprovementTypes.NO_IMPROVEMENT or not gc.getImprovementInfo(iImprovement).isPermanent():
						if CyGame().getMapRandNum(5000, "Hellfire") < iHellfireChance:
							pPlot.setImprovementType(eHellfire)
							pNewUnit = pDemonPlayer.initUnit(eChampion, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
							pNewUnit.setHasPromotion(eDemon, True)

# ent >>>
def reqRessurectionDark(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pPlot.getImprovementType() in (en.eImprovementBarrow, en.eImprovementGraveyard):
		return True
	return False
# ent <<<

def spellRessurectionDark(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]
	liSummonedUnitIDs = argsList[3]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	for iSummonedUnitID in liSummonedUnitIDs:
		pNewUnit = pPlayer.getUnit(iSummonedUnitID)
		pNewUnit.changeExperience(CyGame().getSorenRandNum(15, "Ressurection Graveyard"), -1, False, False, False)
	pPlot = pCaster.plot()
	pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)

def reqGiftDemon(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if pUnit.getRace() != en.eRaceDemon:
			return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellGiftDemon(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if pUnit.getRace() != en.eRaceDemon:
			pUnit.setHasPromotion(en.eRaceDemon, True)

#ImprovementEpic
def onMoveNaturalStone(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]

	liCurePromotions = [	gc.getInfoTypeForString('PROMOTION_POISONED'),
							gc.getInfoTypeForString('PROMOTION_DISEASED'),
							gc.getInfoTypeForString('PROMOTION_PLAGUED'),
							gc.getInfoTypeForString('PROMOTION_WITHERED')	]
	lszCured = []
	for iCurePromotion in liCurePromotions:
		if pCaster.isHasPromotion(iCurePromotion):
			pCaster.setHasPromotion(iCurePromotion, False)
			lszCured.append(gc.getPromotionInfo(iCurePromotion).getDescription())
	if len(lszCured) > 0:
		iImprovement = pPlot.getImprovementType()
		szButton = gc.getImprovementInfo(iImprovement).getButton()
		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_CURED_POOL_OF_TEARS_LIST', (pCaster.getNameKey(), gc.getImprovementInfo(iImprovement).getDescription()))
		szMessage += ', '.join(lszCured)
		CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_FEATUREGROWTH', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCaster.getX(), pCaster.getY(), True, True)

#NIRAIKANAI END <<<

def onMoveDistortion(argsList):
	pCaster = argsList[0]
	pCaster.doDamage(100, 100, en.eDamageLethal)

#Magic Expansion Mod >>>
def enabledThaw(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman() or pCaster.isAutomated():
		if pCaster.getCivilizationType() in (en.eCivilizationIllians, en.eCivilizationNival):
			return False

	ePlayer = pCaster.getOwner()
	eTeam = pCaster.getTeam()
	iRange = pCaster.getSpellRange(eSpell) + 1
	lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, True, eTeam)
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.isColdCounter():
			if pTargetPlot.isOwned():
				if pTargetPlot.getOwner() == ePlayer:
					return True
	return False

def disabledThaw(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman() or pCaster.isAutomated():
		if pCaster.getOwner() != pPlot.getOwner():
			return True
		if pCaster.getCivilizationType() in (en.eCivilizationDoviello, en.eCivilizationIllians, en.eCivilizationNival):
			return True
	return False

def spellThaw(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlot = pCaster.plot()
	iRange = pCaster.getSpellRange(eSpell) + 1
	lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, False, TeamTypes.NO_TEAM)
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.isColdCounter():
			if pTargetPlot.isOwned():
				if pTargetPlot.getOwner() == ePlayer:
					pTargetPlot.doThawColdCounter(10)

"""
def disabledRent(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.isHuman() or pCaster.isAutomated():
		if pCaster.getTeam() != pPlot.getTeam():
			return True
		elif pPlayer.getCivilizationType() != en.eCivilizationInfernal and pPlayer.getCivilizationType() != gc.getInfoTypeForString('CIVILIZATION_DARK') and pPlayer.getCivilizationType() != gc.getInfoTypeForString('CIVILIZATION_DESPIEL'):
			return True
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_RARNA'):
		return True
	return False

def enabledRent(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, True)
	for pTargetPlot in lpRangedPlots:
		if CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_PLOT_COUNTER):
			if pTargetPlot.getTerrainType() in g_leHellTerrains:
				return True
	return False

def spellRent(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
# Kaijin OAC - Hell Terrain fix
#	pPlot.setPlotCounter(100)
	iFeature = pPlot.getFeatureType()
	iBonus = pPlot.getBonusType(TeamTypes.NO_TEAM)
	pPlot.setPlotCounter(100)
	if iBonus != BonusTypes.NO_BONUS:
		if gc.getImprovementInfo(en.eImprovementFarm).isImprovementBonusTrade(iBonus):
			pPlot.setImprovementType(en.eImprovementSnakePillar)
	if iFeature == en.eFeatureFloodPlains:
		pPlot.setFeatureType(en.eFeatureObsidianPlains, 0)

# Kaijin OAC - end
	if pPlot.isOwned():
		if pPlot.getTeam() != pCaster.getTeam():
			pTeam = gc.getTeam(pCaster.getTeam())
			pTeam.declareWar(pPlot.getTeam(), False, WarPlanTypes.WARPLAN_LIMITED)
"""

def reqRaiseOrthus(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCity = pPlot.getPlotCity()
	iRank = 1

	if pPlayer.getAlignment() != AlignmentTypes.ALIGNMENT_EVIL:
		return False

	iThresholdPopulation = cf.doRaiseRequest(pCity, iRank)
	if pCity.getPopulation() < iThresholdPopulation:
		return ReasonTypes.REASON_DISABLED_LACK_OF_POPULATION
	return True

def spellRaiseOrthus(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())

	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ORTHUS'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ORTHUSS_AXE'), False)
	pNewUnit.setHasPromotion(en.eRaceOrc, False)
	pNewUnit.setHasPromotion(en.eRaceUndead, True)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BLITZ'), True)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MUSOU'), True)

	activePlayer = gc.getPlayer(CyGame().getActivePlayer())
	sPlayerName = pPlayer.getName()
	sUnitName = PyInfo.UnitInfo(pNewUnit.getUnitType()).getDescription()
	sPopupText = CyTranslator().getText('TXT_KEY_POPUP_CREATED_UNIT_ORTHUS_RETURN', ())
	if gc.getTeam(pNewUnit.getTeam()).isHasMet(activePlayer.getTeam()):
		sPopupText += CyTranslator().getText('TXT_KEY_POPUP_JOIN_SOMEONE',(sPlayerName, sUnitName))
	else:
		sPopupText += CyTranslator().getText('TXT_KEY_POPUP_JOIN_UNKNOWN',(sUnitName, ))
	cf.addPopup(sPopupText, str(gc.getUnitInfo(pNewUnit.getUnitType()).getImage()))

	iRank = 1

	cf.doRaiseResult(pCity, iRank, pPlot)

def reqRaiseHyborem(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCity = pPlot.getPlotCity()
	iRank = 2

	if pPlayer.getCivilizationType() == en.eCivilizationInfernal:
		return False
	if pPlayer.getAlignment() != AlignmentTypes.ALIGNMENT_EVIL:
		return False

	iThresholdPopulation = cf.doRaiseRequest(pCity, iRank)
	if pCity.getPopulation() < iThresholdPopulation:
		return ReasonTypes.REASON_DISABLED_LACK_OF_POPULATION
	return True

def spellRaiseHyborem(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())

	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_HYBOREM'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(en.eEquipmentGela, False)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BLITZ'), True)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MUSOU'), True)

	activePlayer = gc.getPlayer(CyGame().getActivePlayer())
	sPlayerName = pPlayer.getName()
	sUnitName = PyInfo.UnitInfo(pNewUnit.getUnitType()).getDescription()
	sPopupText = CyTranslator().getText('TXT_KEY_POPUP_CREATED_UNIT_HYBOREM_RETURN', ())
	if gc.getTeam(pNewUnit.getTeam()).isHasMet(activePlayer.getTeam()):
		sPopupText += CyTranslator().getText('TXT_KEY_POPUP_JOIN_SOMEONE',(sPlayerName, sUnitName))
	else:
		sPopupText += CyTranslator().getText('TXT_KEY_POPUP_JOIN_UNKNOWN',(sUnitName, ))
	cf.addPopup(sPopupText, str(gc.getUnitInfo(pNewUnit.getUnitType()).getImage()))

	iRank = 2

	cf.doRaiseResult(pCity, iRank, pPlot)

def reqRaiseAcheron(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCity = pPlot.getPlotCity()
	iRank = 3

	if pPlayer.getAlignment() != AlignmentTypes.ALIGNMENT_EVIL:
		return False

	iThresholdPopulation = cf.doRaiseRequest(pCity, iRank)
	if pCity.getPopulation() < iThresholdPopulation:
		return ReasonTypes.REASON_DISABLED_LACK_OF_POPULATION
	return True

def spellRaiseAcheron(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())

	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ACHERON'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(en.eRaceDragon, False)
	pNewUnit.setHasPromotion(en.eRaceUndead, True)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CANNIBALIZE'), True)

	activePlayer = gc.getPlayer(CyGame().getActivePlayer())
	sPlayerName = pPlayer.getName()
	sUnitName = PyInfo.UnitInfo(pNewUnit.getUnitType()).getDescription()
	sPopupText = CyTranslator().getText('TXT_KEY_POPUP_CREATED_UNIT_ACHERON_RETURN', ())
	if gc.getTeam(pNewUnit.getTeam()).isHasMet(activePlayer.getTeam()):
		sPopupText += CyTranslator().getText('TXT_KEY_POPUP_JOIN_SOMEONE',(sPlayerName, sUnitName))
	else:
		sPopupText += CyTranslator().getText('TXT_KEY_POPUP_JOIN_UNKNOWN',(sUnitName, ))
	cf.addPopup(sPopupText, str(gc.getUnitInfo(pNewUnit.getUnitType()).getImage()))

	iRank = 3

	cf.doRaiseResult(pCity, iRank, pPlot)

def reqRaiseStephanos(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCity = pPlot.getPlotCity()
	iRank = 4

	if pPlayer.getAlignment() != AlignmentTypes.ALIGNMENT_EVIL:
		return False

	iThresholdPopulation = cf.doRaiseRequest(pCity, iRank)
	if pCity.getPopulation() < iThresholdPopulation:
		return ReasonTypes.REASON_DISABLED_LACK_OF_POPULATION
	return True

def spellRaiseStephanos(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())

	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_STEPHANOS'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CROWN_OF_COMMAND'), False)

	activePlayer = gc.getPlayer(CyGame().getActivePlayer())
	sPlayerName = pPlayer.getName()
	sUnitName = PyInfo.UnitInfo(pNewUnit.getUnitType()).getDescription()
	sPopupText = CyTranslator().getText('TXT_KEY_POPUP_CREATED_UNIT_STEPHANOS_RETURN', ())
	if gc.getTeam(pNewUnit.getTeam()).isHasMet(activePlayer.getTeam()):
		sPopupText += CyTranslator().getText('TXT_KEY_POPUP_JOIN_SOMEONE',(sPlayerName, sUnitName))
	else:
		sPopupText += CyTranslator().getText('TXT_KEY_POPUP_JOIN_UNKNOWN',(sUnitName, ))
	cf.addPopup(sPopupText, str(gc.getUnitInfo(pNewUnit.getUnitType()).getImage()))

	iRank = 4

	cf.doRaiseResult(pCity, iRank, pPlot)

def reqRaiseBuboes(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCity = pPlot.getPlotCity()
	iRank = 4

	if pPlayer.getAlignment() != AlignmentTypes.ALIGNMENT_EVIL:
		return False

	iThresholdPopulation = cf.doRaiseRequest(pCity, iRank)
	if pCity.getPopulation() < iThresholdPopulation:
		return ReasonTypes.REASON_DISABLED_LACK_OF_POPULATION
	return True

def spellRaiseBuboes(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())

	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_BUBOES'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WAR'), False)

	activePlayer = gc.getPlayer(CyGame().getActivePlayer())
	sPlayerName = pPlayer.getName()
	sUnitName = PyInfo.UnitInfo(pNewUnit.getUnitType()).getDescription()
	sPopupText = CyTranslator().getText('TXT_KEY_POPUP_CREATED_UNIT_BUBOES_RETURN', ())
	if gc.getTeam(pNewUnit.getTeam()).isHasMet(activePlayer.getTeam()):
		sPopupText += CyTranslator().getText('TXT_KEY_POPUP_JOIN_SOMEONE',(sPlayerName, sUnitName))
	else:
		sPopupText += CyTranslator().getText('TXT_KEY_POPUP_JOIN_UNKNOWN',(sUnitName, ))
	cf.addPopup(sPopupText, str(gc.getUnitInfo(pNewUnit.getUnitType()).getImage()))

	iRank = 4

	cf.doRaiseResult(pCity, iRank, pPlot)

def reqRaiseYersinia(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCity = pPlot.getPlotCity()
	iRank = 4

	if pPlayer.getAlignment() != AlignmentTypes.ALIGNMENT_EVIL:
		return False

	iThresholdPopulation = cf.doRaiseRequest(pCity, iRank)
	if pCity.getPopulation() < iThresholdPopulation:
		return ReasonTypes.REASON_DISABLED_LACK_OF_POPULATION
	return True

def spellRaiseYersinia(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())

	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_YERSINIA'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ATHAME'), False)

	activePlayer = gc.getPlayer(CyGame().getActivePlayer())
	sPlayerName = pPlayer.getName()
	sUnitName = PyInfo.UnitInfo(pNewUnit.getUnitType()).getDescription()
	sPopupText = CyTranslator().getText('TXT_KEY_POPUP_CREATED_UNIT_YERSINIA_RETURN', ())
	if gc.getTeam(pNewUnit.getTeam()).isHasMet(activePlayer.getTeam()):
		sPopupText += CyTranslator().getText('TXT_KEY_POPUP_JOIN_SOMEONE',(sPlayerName, sUnitName))
	else:
		sPopupText += CyTranslator().getText('TXT_KEY_POPUP_JOIN_UNKNOWN',(sUnitName, ))
	cf.addPopup(sPopupText, str(gc.getUnitInfo(pNewUnit.getUnitType()).getImage()))

	iRank = 4

	cf.doRaiseResult(pCity, iRank, pPlot)

def reqRaiseArs(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCity = pPlot.getPlotCity()
	iRank = 4

	if pPlayer.getAlignment() != AlignmentTypes.ALIGNMENT_EVIL:
		return False

	iThresholdPopulation = cf.doRaiseRequest(pCity, iRank)
	if pCity.getPopulation() < iThresholdPopulation:
		return ReasonTypes.REASON_DISABLED_LACK_OF_POPULATION
	return True

def spellRaiseArs(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())

	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ARS'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STAFF_OF_SOULS'), False)

	activePlayer = gc.getPlayer(CyGame().getActivePlayer())
	sPlayerName = pPlayer.getName()
	sUnitName = PyInfo.UnitInfo(pNewUnit.getUnitType()).getDescription()
	sPopupText = CyTranslator().getText('TXT_KEY_POPUP_CREATED_UNIT_ARS_RETURN', ())
	if gc.getTeam(pNewUnit.getTeam()).isHasMet(activePlayer.getTeam()):
		sPopupText += CyTranslator().getText('TXT_KEY_POPUP_JOIN_SOMEONE',(sPlayerName, sUnitName))
	else:
		sPopupText += CyTranslator().getText('TXT_KEY_POPUP_JOIN_UNKNOWN',(sUnitName, ))
	cf.addPopup(sPopupText, str(gc.getUnitInfo(pNewUnit.getUnitType()).getImage()))

	iRank = 4

	cf.doRaiseResult(pCity, iRank, pPlot)

#Magic Expansion Mod <<<

#YS mod

# ent >>>
def reqAddToFreakShow(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	eRace = pCaster.getRace()
	if eRace == en.eRaceDwarf:
		eBuilding = gc.getInfoTypeForString('BUILDING_DWARF_CAGE')
	elif eRace in en.leRaceElf:
		eBuilding = gc.getInfoTypeForString('BUILDING_ELF_CAGE')
	elif eRace == en.eRaceOrc:
		eBuilding = gc.getInfoTypeForString('BUILDING_ORC_CAGE')
	elif eRace == en.eRaceLizardman:
		eBuilding = gc.getInfoTypeForString('BUILDING_LIZARD_CAGE')
	else:
		eBuilding = gc.getInfoTypeForString('BUILDING_HUMAN_CAGE')

	if eBuilding != BuildingTypes.NO_BUILDING:
		pCity = pPlot.getPlotCity()
		if pCity.getNumBuilding(eBuilding) > 0:
			return False
		return True
	return False

def spellAddToFreakShow(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	eRace = pCaster.getRace()
	if eRace == en.eRaceDwarf:
		eBuilding = gc.getInfoTypeForString('BUILDING_DWARF_CAGE')
	elif eRace in en.leRaceElf:
		eBuilding = gc.getInfoTypeForString('BUILDING_ELF_CAGE')
	elif eRace == en.eRaceOrc:
		eBuilding = gc.getInfoTypeForString('BUILDING_ORC_CAGE')
	elif eRace == en.eRaceLizardman:
		eBuilding = gc.getInfoTypeForString('BUILDING_LIZARD_CAGE')
	else:
		eBuilding = gc.getInfoTypeForString('BUILDING_HUMAN_CAGE')

	if eBuilding != BuildingTypes.NO_BUILDING:
		pCity = pPlot.getPlotCity()
		pCity.setNumRealBuilding(eBuilding, 1)

def disabledRevivalOfOnetimeonly(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		if pCaster.canCast(gc.getInfoTypeForString('SPELL_RESURRECTION'), False):
			return True
	return False

def disabledTiltowaito(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
		for pTargetPlot in lpRangedPlots:
			if not pTargetPlot.isWater():
				if pTargetPlot.isOwned():
					if not pTeam.isAtWar(pTargetPlot.getTeam()):
						return True
	return False
# ent <<<

def spellTiltowaito(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iChance = gc.getDefineINT('FLAMES_SPREAD_CHANCE')
	pPlot = pCaster.plot()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		if not pTargetPlot.isWater():
			if CyGame().getSorenRandNum(100, "Haunted Spread") <= iChance:
				if pTargetPlot.getFeatureType() != en.eFeatureHauntedLands:
					pTargetPlot.setFeatureType(en.eFeatureHauntedLands, 0)

# ent >>>
def reqDepression(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if not pUnit.isImmuneToFear() and not pUnit.plot().isCity():
			return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET
# ent <<<

def spellDepression(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	szButton = gc.getSpellInfo(eSpell).getButton()

	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, False)
	for pUnit in lpRangedUnits:
# ent >>>
#		if not pUnit.isImmuneToFear():
		if not pUnit.isImmuneToFear() and not pUnit.plot().isCity():
# ent <<<
			if not pUnit.isResisted(pCaster, eSpell):
				pUnit.jumpToAdjacentValidPlotWithForbiddingPlot(pPlot)
				CyInterface().addMessage(pUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_FEAR', (pUnit.getNameKey(), )), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pUnit.getX(), pUnit.getY(), True, True)
				CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText('TXT_KEY_MESSAGE_FEAR_ENEMY', (pUnit.getNameKey(), )), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pUnit.getX(), pUnit.getY(), True, True)

# ent >>>
def disabledHandoftheDead(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		ePlayer = pCaster.getOwner()
		for iUnitIndex in xrange(pPlot.getNumUnits()):
			pUnit = pPlot.getUnit(iUnitIndex)
			if pUnit.getOwner() == ePlayer:
				if pUnit.getDamageTypeResist(en.eDamageDeath) < 100:
					return True
	return False
# ent <<<

def spellHandoftheDead(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pCasterPlot = pCaster.plot()
	bResist = False
	for i in xrange(pBestPlot.getNumUnits()):
		pUnit = pBestPlot.getUnit(i)
		if pUnit.isResisted(pCaster, eSpell):
			bResist = True
			for iUnitIndex in xrange(pCasterPlot.getNumUnits()):
				pLoopUnit = pCasterPlot.getUnit(iUnitIndex)
				pLoopUnit.doDamage(10, 100, en.eDamageDeath)
	if bResist and pCasterPlot.isVisibleToWatchingHuman():
		CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_ENTROPY_SUMMON'), pCasterPlot.getPoint())

def spellSealed(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, False)

	for pUnit in lpRangedUnits:
		if not pUnit.isResisted(pCaster, eSpell):
			pUnit.setHasPromotion(en.ePromotionSealed, True)
			iDelay = cyFlatValue(CyGame().getSorenRandNum(3, "Sealed") + 1, g_dGameSpeedPercent["VictoryDelay"], True)
			pUnit.changeUncastableTimer(iDelay)
		else:
			pUnit.setHasPromotion(en.ePromotionSealed, False)

# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
def effectSealed(argsList):
	pCaster = argsList[0]
	if pCaster.getUncastableTimer() <= 1:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SEALED'), False)
"""
# Kaijin <<< End

def reqPrismicMissile(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if pUnit.getResistChance(pCaster, eSpell) < 100:
			return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellPrismicMissile(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	lePromotions = [	gc.getInfoTypeForString('PROMOTION_FATIGUED'),
						gc.getInfoTypeForString('PROMOTION_WEAKEN'),
						gc.getInfoTypeForString('PROMOTION_DISEASED'),
						gc.getInfoTypeForString('PROMOTION_WITHERED'),
						gc.getInfoTypeForString('PROMOTION_BLIND'),
						gc.getInfoTypeForString('PROMOTION_SLEEP'),
						gc.getInfoTypeForString('PROMOTION_FERAL'),
						en.ePromotionSealed	]
	lDamageList = ['POISON', 'LOW', 'MIDDLE', 'HIGH', 'IMMOBILE', 'LETHAL', 'NONE']

	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	szButton = gc.getSpellInfo(eSpell).getButton()
	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if not pUnit.isResisted(pCaster, eSpell):
			leChosenPromotions = []
			for ePromotion in lePromotions:
				if not pUnit.isHasPromotion(ePromotion):
					if not pUnit.isImmuneToPromotion(ePromotion):
						leChosenPromotions.append(ePromotion)
			leChosenPromotions.sort()

			if len(leChosenPromotions) > 0:
				leSelectedPromotions = []
				for iLoop in xrange( CyGame().getSorenRandNum(len(leChosenPromotions), "Randomizer") ):
					leSelectedPromotions.append(leChosenPromotions.pop( CyGame().getSorenRandNum(len(leChosenPromotions), "Randomizer") ))
				leSelectedPromotions.sort()
				for eSelectedPromotion in leSelectedPromotions:
					pUnit.setHasPromotion(eSelectedPromotion, True)
					if eSelectedPromotion == en.ePromotionSealed:
						iDelay = cyFlatValue(CyGame().getSorenRandNum(3, "Sealed") + 1, g_dGameSpeedPercent["VictoryDelay"], True)
						pUnit.changeUncastableTimer(iDelay)

			sDamage = lDamageList[CyGame().getSorenRandNum(len(lDamageList), 'Pick Damage')]
			if sDamage == 'POISON':
				pUnit.doDamage(20, 100, en.eDamagePoison)
				pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED'), True)

			elif sDamage == 'LOW':
				pUnit.doDamage(5, 100, en.eDamagePhysical)

			elif sDamage == 'MIDDLE':
				pUnit.doDamage(10, 100, en.eDamagePhysical)

			elif sDamage == 'HIGH':
				pUnit.doDamage(20, 100, en.eDamagePhysical)

			elif sDamage == 'IMMOBILE':
				pUnit.changeImmobileTimer(1)

			elif sDamage == 'LETHAL':
				if CyGame().getSorenRandNum(100, "Lethal Chance") < 25:
					pUnit.doDamage(100, 100, en.eDamageLethal)

			pTargetPlot = pUnit.plot()
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_PRISMIC_MISSILE', (pUnit.getNameKey(), pPlayer.getCivilizationAdjectiveKey(), pCaster.getNameKey()))
			CyInterface().addMessage(pUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pUnit.getX(), pUnit.getY(), True, True)
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_PRISMIC_MISSILE_ENEMY', (pCaster.getNameKey(), gc.getPlayer(pUnit.getOwner()).getCivilizationAdjectiveKey(), pUnit.getNameKey()))
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)

def reqControl(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if pUnit.getOwner() == ePlayer:
			if pUnit.isMadeAttack():
				return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellControl(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	eSpellHeal = gc.getInfoTypeForString('SPELL_CONTROL_MOVEMENT_HEAL')
	ePlayer = pCaster.getOwner()
	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if pUnit.getOwner() == ePlayer:
			if pUnit.isMadeAttack():
				pUnit.cast(eSpellHeal)

# ent >>>
def disabledHurricane(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
		for pTargetPlot in lpRangedPlots:
			if pTargetPlot.isOwned():
				if not pTeam.isAtWar(pTargetPlot.getTeam()):
					return True
		for eDirection in xrange(DirectionTypes.NUM_DIRECTION_TYPES):
			pLoopPlot = plotDirection(pPlot.getX(), pPlot.getY(), DirectionTypes(eDirection))
			if not pLoopPlot.isNone():
				if pLoopPlot.isCity():
					if pLoopPlot.isEnemyCity(pCaster):
						break
		else:
			return True
	return False
# ent <<<

def spellHurricane(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	eEffect = gc.getInfoTypeForString('EFFECT_SNOWFALL')
	pPlot = pCaster.plot()
	iX = pPlot.getX()
	iY = pPlot.getY()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		if not pTargetPlot.at(iX, iY):
			for iUnit in xrange(pTargetPlot.getNumUnits()):
				pUnit = pTargetPlot.getUnit(iUnit)
				if pUnit.isFlying():
					pUnit.setFortifyTurns(0)
					pUnit.doDamage(70, 100, en.eDamagePhysical)
		iRnd = CyGame().getSorenRandNum(100, "Bob")
		if iRnd > 80:
			if not pTargetPlot.isCity():
				if pTargetPlot.getNumUnits() == 0:
					if pTargetPlot.isFlatlands():
						if pTargetPlot.isVisibleToWatchingHuman():
							CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())
						pTargetPlot.setBonusType(BonusTypes.NO_BONUS)
						pTargetPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
						pTargetPlot.setPlotType(PlotTypes.PLOT_OCEAN, True, True)
						pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
						pTargetPlot.clearColdCounter()
#						pTargetPlot.setTerrainType(en.eTerrainCoast, True, True)
		if iRnd > 50:
			if pTargetPlot.getTerrainType() == en.eTerrainDesert:
				if pTargetPlot.isVisibleToWatchingHuman():
					CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())
				pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
				pTargetPlot.clearColdCounter()
				pTargetPlot.setTerrainType(en.eTerrainMarsh, True, True)
		if pTargetPlot.getFeatureType() == en.eFeatureScrub:
			pTargetPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)

# ent >>>

	"""
def disabledSoilPreparation(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pPlot = pCaster.plot()
	kSpell = gc.getSpellInfo(eSpell)
	lpRangedPlots = cyGetRangedPlots(pPlot, kSpell.getRange(), False, False, TeamTypes.NO_TEAM)
	for pTargetPlot in lpRangedPlots:
		if not pTargetPlot.isPeak():
			return False
		elif pTargetPlot.getFeatureType() != gc.getInfoTypeForString('FEATURE_VOLCANO'):
			return False
	return True
	"""

def reqSoilPreparation(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		ePlayer = pCaster.getOwner()
		if pPlot.isOwned():
			if pPlot.getOwner() != ePlayer:
				return False
		else:
			return False
		pPlayer = gc.getPlayer(ePlayer)
		if pPlayer.getCivilizationType() == en.eCivilizationMazatl:
			return False
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) > 0:
			return False

		lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, True)
		for pTargetPlot in lpRangedPlots:
			if pTargetPlot.isCity():
				if pTargetPlot.isCoastalLand():
					return False

	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, True)
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.getNumUnits() == 0:
			if pTargetPlot.isPeak() or pTargetPlot.getFeatureType() == en.eFeatureVolcano:
				return True

			if pTargetPlot.isWater():
				return True
	
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET
# ent <<<

def spellSoilPreparation(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	eTeam = pCaster.getTeam()
	pPlot = pCaster.plot()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.getNumUnits() == 0:
			if pTargetPlot.isPeak():
				pTargetPlot.setPlotType(PlotTypes.PLOT_HILLS, True, True)
				pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
				pTargetPlot.clearColdCounter()
				pTargetPlot.setTerrainType(en.eTerrainDesert, True, True)
				if pTargetPlot.isOwned():
					if pTargetPlot.getTeam() != eTeam:
						pTeam = gc.getTeam(eTeam)
						pTeam.declareWar(pTargetPlot.getTeam(), False, WarPlanTypes.WARPLAN_LIMITED)

			if pTargetPlot.getFeatureType() == en.eFeatureVolcano:
				pTargetPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
				if pTargetPlot.isOwned():
					if pTargetPlot.getTeam() != eTeam:
						pTeam = gc.getTeam(eTeam)
						pTeam.declareWar(pTargetPlot.getTeam(), False, WarPlanTypes.WARPLAN_LIMITED)

			if pTargetPlot.isWater():
				iRnd = CyGame().getSorenRandNum(100, "Landfill")
				if iRnd <= 50:
					pTargetPlot.setBonusType(BonusTypes.NO_BONUS)
					pTargetPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
					pTargetPlot.setPlotType(PlotTypes.PLOT_LAND, True, True)
					if pTargetPlot.getLatitude() > 70:
						pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
						pTargetPlot.setTerrainType(en.eTerrainSnow, True, True)
						pTargetPlot.ceilColdCounter(9600 + CyGame().getSorenRandNum(2400, "Built Temple of the Hand"), 1000)
					elif pTargetPlot.getLatitude() > 50:
						pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
						pTargetPlot.clearColdCounter()
						pTargetPlot.setTerrainType(en.eTerrainTundra, True, True)
					else:
						pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
						pTargetPlot.clearColdCounter()
						pTargetPlot.setTerrainType(en.eTerrainDesert, True, True)
					if pTargetPlot.isOwned():
						if pTargetPlot.getTeam() != eTeam:
							pTeam = gc.getTeam(eTeam)
							pTeam.declareWar(pTargetPlot.getTeam(), False, WarPlanTypes.WARPLAN_LIMITED)

# YS start
def reqSpecchioDelZeme(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.isHuman():
		if pPlayer.getNumUnits() < 30:
			return False
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) == 0:
			return False
	return True

def spellSpecchioDelZeme(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	py = PyPlayer(pCaster.getOwner())
	for pUnit in py.getUnitList():
		if pUnit.canFight():
			if pUnit.getUnitCombatType() != UnitCombatTypes.NO_UNITCOMBAT:
				pUnit.changeExperience(10, -1, False, False, False)

def reqRemainStrong(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.getExperience() >= 50:
		return True
	return False

def spellRemainStrong(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]
 
	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	iCasterID = pCaster.getID()
	if pPlayer.isHuman():
		popupInfo = CyPopupInfo()
		popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
		popupInfo.setText(CyTranslator().getText("TXT_KEY_REMAINS_STRONG",()))
		popupInfo.setData1(ePlayer)
		popupInfo.setData2(iCasterID)
		popupInfo.setPythonModule("CvSpellInterface")
		popupInfo.setOnClickedPythonCallback("selectRemainStrong")
		popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_POPUP_YES", ()), "")
		popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_POPUP_NO", ()), "")
		popupInfo.addPopup(ePlayer)
	else:
		applyRemainStrong(ePlayer, iCasterID)

def selectRemainStrong(argsList):
	iButton = argsList[0]
	ePlayer = argsList[1]
	iCasterID = argsList[2]

	if iButton == 0:
		applyRemainStrong(ePlayer, iCasterID)

def applyRemainStrong(ePlayer, iCasterID):
	pPlayer = gc.getPlayer(ePlayer)
	pCaster = pPlayer.getUnit(iCasterID)
	pPlot = pCaster.plot()
	if pCaster.getUnitType() == gc.getInfoTypeForString('UNIT_ADOL1'):
		eUnit = gc.getInfoTypeForString('UNIT_ADOL2')
	elif pCaster.getUnitType() == gc.getInfoTypeForString('UNIT_ADOL2'):
		eUnit = gc.getInfoTypeForString('UNIT_ADOL3')
	CyInterface().addMessage(pCaster.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_ADOL", ()),'AS2D_REVOLTEND',1,'Art_Kaijin/REAH/adol.dds',ColorTypes(8),pCaster.getX(),pCaster.getY(),True,True)
	if pPlot.isVisibleToWatchingHuman():
		CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_PILLAR_OF_FIRE'),pPlot.getPoint())
	pNewUnit = pCaster.castReincarnate(SpellTypes.NO_SPELL, eUnit)
	pNewUnit.setLevel(1)
	pNewUnit.setExperience(0, -1)

def reqYsEventBuyWeapon(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())

	rate = (100 + pPlayer.calculateInflationRate()) / 100
	iGoldLow = 50 * rate
	iGoldMid = 200 * rate
	iGoldHigh = 1600 * rate
	iGoldNeckless = 100 * rate
	iGoldPlayer = pPlayer.getGold()

	if not pCaster.isHuman():
		if pPlayer.AI_isFinancialTrouble():
			return False
		if iGoldPlayer >= iGoldLow:
			if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSWORD3')):
				if pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_COPPER')) > 0:
					if iGoldPlayer >= iGoldHigh:
						return True
					if iGoldPlayer >= iGoldMid and not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSWORD2')):
						return True
				if (not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSWORD2'))
					and not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSWORD1'))	):
					return True
			if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSARMOR3')):
				if pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_MARBLE')) > 0:
					if iGoldPlayer >= iGoldHigh:
						return True
					if iGoldPlayer >= iGoldMid and not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSARMOR2')):
						return True
				if (not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSARMOR2'))
					and not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSARMOR1'))	):
					return True
			if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSHIELD3')):
				if pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_GOLD')) > 0:
					if iGoldPlayer >= iGoldHigh:
						return True
					if iGoldPlayer >= iGoldMid and not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSHIELD2')):
						return True
				if (not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSHIELD2'))
					and not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSHIELD1'))	):
					return True
			if (not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSNECKLESS'))
				and pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_GEMS')) > 0
				and iGoldPlayer >= iGoldNeckless											):
				return True
		return False
	return True

def spellYsEventBuyWeapon(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(), 'EVENTTRIGGER_BUY_WEAPON')
	triggerData = pPlayer.initTriggeredData(iEvent, True, -1, pCaster.getX(), pCaster.getY(), pCaster.getOwner(), -1, -1, -1, pCaster.getID(), -1)

def reqNewGame(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if CyGame().isUnitClassMaxedOut(gc.getInfoTypeForString('UNITCLASS_ADOL'), 0):
		return False
	return True

# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
def effectHoodooAsh(argsList):
	pCaster = argsList[0]

	pPlot = pCaster.plot()
	if not pPlot.isNone():
		for iUnit in xrange(pPlot.getNumUnits()):
			pUnit = pPlot.getUnit(iUnit)
			pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAKEN'), True)
			pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LOW_VITALITY'), True)
"""
# Kaijin <<< End

# YS end
# YS mod end
"""
def reqWayOfWar(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		if pCaster.getUnitClassType() in (gc.getInfoTypeForString('UNIT_ENGINEER'), gc.getInfoTypeForString('UNIT_SCIENTIST'), gc.getInfoTypeForString('UNIT_PROPHET')):
			return False
	return True
"""

def reqHyboremSmile(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isAlwaysHostile(pPlot):
		return ReasonTypes.REASON_DISABLED_NATIONALITY_IS_HIDDEN

	iResistMax = 95
	if not pCaster.isHuman():
		iResistMax = 20

	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)

	for pUnit in lpRangedUnits:
		if pUnit.getReligion() == en.eReligionAshenVeil:
			if pUnit.isAlive() or pUnit.getRace() == en.eRaceDemon:
				if not isWorldUnitClass(pUnit.getUnitClassType()):
					iResist = pUnit.getResistChance(pCaster, eSpell)
					if iResist <= iResistMax:
						return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellHyboremSmile(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iResistMax = 95
	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.isHuman():
		iResistMax = 20

	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)

	iBestValue = 0
	pBestUnit = -1
	for pUnit in lpRangedUnits:
		if pUnit.getReligion() == en.eReligionAshenVeil:
			if pUnit.isAlive() or pUnit.getRace() == en.eRaceDemon:
				if not isWorldUnitClass(pUnit.getUnitClassType()):
					iResist = pUnit.getResistChance(pCaster, eSpell)
					if iResist <= iResistMax:
						iValue = (pUnit.getCombatAttackTimes100() + pUnit.getCombatDefenseTimes100()) // 20 + pUnit.getExperience()
						iValue += (100 - iResist)
						if iValue > iBestValue:
							iBestValue = iValue
							pBestUnit = pUnit

	szButton = gc.getSpellInfo(eSpell).getButton()
	if pBestUnit != -1:
		if not pBestUnit.isResisted(pCaster, eSpell):
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_DOMINATION', (pBestUnit.getNameKey(), pPlayer.getCivilizationAdjectiveKey(), pCaster.getNameKey()))
			CyInterface().addMessage(pBestUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pBestUnit.getX(), pBestUnit.getY(), True, True)
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_DOMINATION_ENEMY', (pCaster.getNameKey(), gc.getPlayer(pBestUnit.getOwner()).getCivilizationAdjectiveKey(), pBestUnit.getNameKey()))
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)

			if pBestUnit.isImmuneToCapture():
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_CAPTURED_LOYALTY', (pBestUnit.getNameKey(), ))
				CyInterface().addMessage(pBestUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pBestUnit.getX(), pBestUnit.getY(), True, True)
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_CAPTURED_LOYALTY', (pBestUnit.getNameKey(), ))
				CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
				pBestUnit.kill(False, PlayerTypes.NO_PLAYER)
			else:
				pNewUnit = pPlayer.initSkeletalUnit(pBestUnit.getUnitType(), pPlot.getX(), pPlot.getY(), pBestUnit.getUnitAIType())
				pNewUnit.convert(pBestUnit)
				pNewUnit.changeImmobileTimer(1)
		else:
			iTimer = 1 + cyFlatValue(3, g_dGameSpeedPercent["VictoryDelay"], True)
			pCaster.changeUncastableTimer(iTimer)
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_HYBOREMS_SMILE_FAILED', ())
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)

#Tougou End

#Kaijin OAC Start
#Despiel Start
def reqDeathAndDecay(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if CyGame().getGlobalCounter() == 0:
		return ReasonTypes.REASON_DISABLED_REQUIRES_GLOBAL_COUNTER
	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.isHuman():
		if CyGame().getGlobalCounter() < 40:
			return False
	return True

def spellDeathAndDecay(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iCounter = CyGame().getGlobalCounter()
	iOwner = pCaster.getOwner()
	for iPlayer in xrange(gc.getMAX_PLAYERS()):
		pPlayer = gc.getPlayer(iPlayer)
		if pPlayer.isAlive():
			if iPlayer != iOwner and pPlayer.getCivilizationType() != en.eCivilizationInfernal:
				for pyCity in PyPlayer(iPlayer).getCityList():
					pCity = pyCity.GetCy()
					i = (iCounter / 4)
					i += pCity.getPopulation()
					i -= pCity.totalGoodBuildingHealth()
					if i > 0:
						pCity.changeEspionageHealthCounter(i)

def reqEnergyExploitationKaijin(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	if len(lpRangedUnits) > 0:
		if pCaster.isHuman():
			iCasterID = pCaster.getID()
			for pUnit in lpRangedUnits:
				if pUnit.getID() != iCasterID:
					return True
		else:
			iTotalExploitationExperience = 0
			eTeam = pCaster.getTeam()
			for pUnit in lpRangedUnits:
				if pUnit.getTeam() != eTeam:
					iExploitationExperience = min(pUnit.getExperience(), 3)
					iTotalExploitationExperience += iExploitationExperience
			if iTotalExploitationExperience > 30:
				return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellEnergyExploitationKaijin(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, False)
	iCasterID = pCaster.getID()
	iTotalExploitationExperience = 0
	for pUnit in lpRangedUnits:
		if pUnit.getID() != iCasterID:
			iExploitationExperience = min(pUnit.getExperience(), 3)
			pUnit.changeExperience(iExploitationExperience * -1, -1, False, False, False)
			iTotalExploitationExperience += iExploitationExperience

	pTeam = gc.getTeam(pCaster.getTeam())
	lpTargetUnits = [pUnit for pUnit in lpRangedUnits if pTeam.isAtWar(pUnit.getTeam())]

	listProms = []
	if len(lpTargetUnits) > 0:
		for eProm in xrange(gc.getNumPromotionInfos()):
			if not pCaster.isHasPromotion(eProm):
				if gc.getPromotionInfo(eProm).isEquipment():
					continue
				if gc.getPromotionInfo(eProm).isRace():
					continue
				if eProm in (en.ePromotionGreatCommander, en.lePromotionWeapons):
					continue
				for pUnit in lpTargetUnits:
					if pUnit.isHasPromotion(eProm):
						listProms.append(eProm)
						break

	szButton = gc.getSpellInfo(eSpell).getButton()
	if iTotalExploitationExperience > 0:
		pCaster.changeExperience(iTotalExploitationExperience, -1, False, False, False)
		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_ENERGY_EXPLOITATION_KAIJIN', (pCaster.getNameKey(), iTotalExploitationExperience))
		CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCaster.getX(), pCaster.getY(), True, True)
	if len(listProms) > 0:
		iRnd = CyGame().getSorenRandNum(len(listProms), "PromotionExploitation")
		eSelectedProm = listProms[iRnd]
		pCaster.setHasPromotion(eSelectedProm, True)
		szPromMessage = CyTranslator().getText('TXT_KEY_MESSAGE_ENERGY_EXPLOITATION_KAIJIN_PROMOTION_STOLEN', (pCaster.getNameKey(), gc.getPromotionInfo(eSelectedProm).getDescription()))
		szPromButton = gc.getPromotionInfo(eSelectedProm).getButton()
		CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szPromMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szPromButton, en.eColorGreen, pCaster.getX(), pCaster.getY(), True, True)

def reqSummonCuchumaquic(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		eTeam = pCaster.getTeam()
		pTeam = gc.getTeam(eTeam)
		if pTeam.getAtWarCount(True) == 0:
			return False
		pPlot = pCaster.plot()
		iRange = 2
		lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, False, TeamTypes.NO_TEAM)
		for pTargetPlot in lpRangedPlots:
			if pTargetPlot.isEnemyCity(pCaster):
				return True
			for iUnitIndex in xrange(pTargetPlot.getNumUnits()):
				pUnit = pTargetPlot.getUnit(iUnitIndex)
				if pUnit.isEnemy(eTeam, pUnit.plot()):
					if pUnit.canFight():
						return True
		return False

	return True

def spellSummonCuchumaquic(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]
	liSummonedUnitIDs = argsList[3]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	for iSummonedUnitID in liSummonedUnitIDs:
		pNewUnit = pPlayer.getUnit(iSummonedUnitID)
		pNewUnit.kill(False, PlayerTypes.NO_PLAYER)

	if CyGame().getSorenRandNum(100, 'Chant Failure') < max(0, 25 - pCaster.getLevel() * 5):
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_CUCHUMAQUIC'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit.convert(pCaster)
		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SUMMON_CUCHUMAQUIC_FAILED', (pCaster.getNameKey(), gc.getSpellInfo(eSpell).getDescription()))
		szButton = gc.getSpellInfo(eSpell).getButton()
		CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCaster.getX(), pCaster.getY(), True, True)

	else:
		customSummonSpellData = CvCustomSummonSpellData()
		customSummonSpellData.eUnit = gc.getInfoTypeForString('UNIT_CUCHUMAQUIC')
		customSummonSpellData.iDuration = gc.getDefineINT('SUMMONING_DEFAULT_DURATION_TURNS') + pPlayer.getSummonDuration()
		customSummonSpellData.bAbility = True
		customSummonSpellData.bCopyPromotion = True
		lpNewUnits = pCaster.castCustomSummon(customSummonSpellData)

		for pNewUnit in lpNewUnits:
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_KAIJIN_RACE'), False)
			pNewUnit.setHasPromotion(en.ePromotionChanneling3, False)
			pNewUnit.setHasCasted(True)

			# caster bare strength
			iWeaponExtraAttack = 0
			iWeaponExtraDefense = 0
			eWeapon = pCaster.getWeapon()
			if eWeapon != WeaponTypes.NO_WEAPON:
				eWeaponPromotion = gc.getWeaponInfo(eWeapon).getWeaponPromotion()
				if eWeaponPromotion != PromotionTypes.NO_PROMOTION:
					iWeaponExtraAttack = gc.getPromotionInfo(eWeaponPromotion).getExtraCombatStr()
					iWeaponExtraDefense = gc.getPromotionInfo(eWeaponPromotion).getExtraCombatDefense()

			iBareCombatAttackTimes100 = pCaster.getCombatAttackTimes100() - iWeaponExtraAttack * 100
			iBareCombatDefenseTimes100 = pCaster.getCombatDefenseTimes100() - iWeaponExtraDefense * 100

			# Cuchumaquic bare strength
			iWeaponExtraAttack = 0
			iWeaponExtraDefense = 0
			eWeapon = pNewUnit.getWeapon()
			if eWeapon != WeaponTypes.NO_WEAPON:
				eWeaponPromotion = gc.getWeaponInfo(eWeapon).getWeaponPromotion()
				if eWeaponPromotion != PromotionTypes.NO_PROMOTION:
					iWeaponExtraAttack = gc.getPromotionInfo(eWeaponPromotion).getExtraCombatStr()
					iWeaponExtraDefense = gc.getPromotionInfo(eWeaponPromotion).getExtraCombatDefense()

			iCuchumaquicBareCombatAttackTimes100 = pNewUnit.getCombatAttackTimes100() - iWeaponExtraAttack * 100
			iCuchumaquicBareCombatDefenseTimes100 = pNewUnit.getCombatDefenseTimes100() - iWeaponExtraDefense * 100

			iChangeAttackTimes100 = iBareCombatAttackTimes100 - iCuchumaquicBareCombatAttackTimes100
			iChangeDefenseTimes100 = iBareCombatDefenseTimes100 - iCuchumaquicBareCombatDefenseTimes100

			pNewUnit.changeCombatAttackTimes100(iChangeAttackTimes100)
			pNewUnit.changeCombatDefenseTimes100(iChangeDefenseTimes100)

#Despiel End
#Lineage Start
def reqBravely(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.isHuman():
		if pPlayer.getNumUnits() < 40:
			return False
# ent >>>
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) == 0:
			return False
# ent <<<
	return True

def spellBravely(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	py = PyPlayer(pCaster.getOwner())
	for pUnit in py.getUnitList():
		if pUnit.canFight():
			pUnit.changeFreePromotionPick(2)

# ent >>>
def reqUpgradeFreedmanWarrior(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isAutomated():
		return False
	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.getUnitClassCount(en.eUnitClassWarrior) > pPlayer.getNumCities():
			return False
		pTeam = gc.getTeam(pCaster.getTeam())
		if pPlot.isOwned():
			if pTeam.isAtWar(pPlot.getTeam()):
				return False
		if pTeam.getAtWarCount(True) == 0:
			return False
	return True

def reqUpgradeFreedmanWorker(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isAutomated():
		return False
	if not pCaster.isHuman():
		if pPlot.isOwned():
			if pPlot.getOwner() != pCaster.getOwner():
				return False
		else:
			return False
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.getUnitClassCount(en.eUnitWorker) * 2 > pPlayer.getNumCities() * 3:
			return False
	return True

	"""
def reqLineageHorseMounting(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) > 0:
			pPlot = pCaster.plot()
			if pPlot.isCity():
				if pPlot.getOwner() == pCaster.getOwner():
					return False

			if pCaster.getUnitCombatType() in (	gc.getInfoTypeForString('UNITCOMBAT_MELEE'), 
												gc.getInfoTypeForString('UNITCOMBAT_ARCHER'), 
												gc.getInfoTypeForString('UNITCOMBAT_DISCIPLE')	):
				iX = pCaster.getX()
				iY = pCaster.getY()
				eTeam = pCaster.getTeam()
				for iiX in xrange(iX-1, iX+2, 1):
					for iiY in xrange(iY-1, iY+2, 1):
						pPlot = CyMap().plot(iiX,iiY)
						if pPlot.isCity():
							for i in xrange(pPlot.getNumUnits()):
								pUnit = pPlot.getUnit(i)
								if pUnit.isEnemy(eTeam, pUnit.plot()):
									return False

	return True
	"""

def disabledLineageHorseMounting(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		if pPlot.isCity():
			if pPlot.getOwner() == pCaster.getOwner():
				return True
		iRange = 1
		eTeam = pCaster.getTeam()
		lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, True, eTeam)
		for pTargetPlot in lpRangedPlots:
			if pTargetPlot.isCity():
				if pTargetPlot.isEnemyCity(pCaster):
					return True
	return False
# ent <<<

def spellLineageHorseMounting(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pCaster.setUnitCombatType(en.eUnitCombatMounted)

def reqLineageHorseUnMounting(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

# ent >>>
	"""
	pPlayer = gc.getPlayer(pCaster.getOwner())
	eCasterDefaultUnit = gc.getCivilizationInfo(pPlayer.getCivilizationType()).getCivilizationUnits(pCaster.getUnitClassType())
	eDefaultUnitCombat = gc.getUnitInfo(eCasterDefaultUnit).getUnitCombatType()

	if not pCaster.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) > 0:
			pPlot = pCaster.plot()
			if pPlot.isCity():
				if pPlot.getOwner() == pCaster.getOwner():
					return True

			if eDefaultUnitCombat in (	gc.getInfoTypeForString('UNITCOMBAT_MELEE'), 
										gc.getInfoTypeForString('UNITCOMBAT_ARCHER'), 
										gc.getInfoTypeForString('UNITCOMBAT_DISCIPLE')	):
				iX = pCaster.getX()
				iY = pCaster.getY()
				eTeam = pCaster.getTeam()
				for iiX in xrange(iX-1, iX+2, 1):
					for iiY in xrange(iY-1, iY+2, 1):
						pPlot = CyMap().plot(iiX,iiY)
						if pPlot.isCity():
							for i in xrange(pPlot.getNumUnits()):
								pUnit = pPlot.getUnit(i)
								if pUnit.isEnemy(eTeam, pUnit.plot()):
									return True
		return False
	return True
	"""

	if not pCaster.isHuman():
		if pPlot.isCity():
			if pPlot.getOwner() == pCaster.getOwner():
				return True
		iRange = 1
		eTeam = pCaster.getTeam()
		lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, True, eTeam)
		for pTargetPlot in lpRangedPlots:
			if pTargetPlot.isCity():
				if pTargetPlot.isEnemyCity(pCaster):
					return True
		return False
	return True

def spellLineageHorseUnMounting(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	eCasterDefaultUnit = gc.getCivilizationInfo(pPlayer.getCivilizationType()).getCivilizationUnits(pCaster.getUnitClassType())
	eDefaultUnitCombat = gc.getUnitInfo(eCasterDefaultUnit).getUnitCombatType()
	pCaster.setUnitCombatType(eDefaultUnitCombat)

# ent >>>
def reqAddToCityCommander(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if not pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_ORGANIZED')):
			pCity = pPlot.getPlotCity()
			if pCity.getFreeSpecialistCount(gc.getInfoTypeForString('SPECIALIST_GREAT_GENERAL')) >= 3:
				if pCity.getNumActiveBuilding(gc.getInfoTypeForString('BUILDING_COMMAND_POST')) == 0:
					# 指揮所を建てさせる
					return False
	return True
# ent <<<

def spellAddToCityCommander(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	pCity.changeFreeSpecialistCount(gc.getInfoTypeForString('SPECIALIST_GREAT_GENERAL'), 1)

def reqPromoteSupplyBase(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if CyGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and gc.getPlayer(pCaster.getOwner()).isHuman():
		return False
	iRange = 2
	lpRangedPlots = cyGetRangedPlots(pPlot, iRange, True, False, TeamTypes.NO_TEAM)
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.isCity():
			return ReasonTypes.REASON_DISABLED_TOO_CLOSE_SAME_IMPROVEMENT
	return True

def spellPromoteSupplyBase(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	pPlot = pCaster.plot()
	pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)

	pNewUnit = pPlayer.initUnit(en.eUnitSettler, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
	pNewUnit.getGroup().pushMission(MissionTypes.MISSION_FOUND, 0, -1, 0, False, False, MissionAITypes.MISSIONAI_FOUND, pPlot, pNewUnit)

	pCity = pPlot.getPlotCity()
	if pCity.isNone():
		return
	pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_PALISADE'), 1)
	iCulture = 20
	iCulture *= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(CyGame().getGameSpeedType())
	iCulture /= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(en.eGameSpeedNormal)
	pCity.changeCulture(iPlayer, iCulture, True)

def reqIncubationLineage(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pPlot.getFeatureType() in (en.eFeatureForest, en.eFeatureForestAncient, en.eFeatureJungle, en.eFeatureDeepJungle, en.eFeatureScrub):
		return True
	if pPlot.getImprovementType() in en.leImprovementFortress:
		return True
	return False

# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
def effectCommanderGoze(argsList):
	pCaster = argsList[0]

	iX = pCaster.getX()
	iY = pCaster.getY()
	pPlayer = gc.getPlayer(pCaster.getOwner())
	pTeam = gc.getTeam(pPlayer.getTeam())
	for iiX in xrange(iX-3, iX+4, 1):
		for iiY in xrange(iY-3, iY+4, 1):
			pPlot = CyMap().plot(iiX,iiY)
			if not pPlot.isNone():
				for iUnit in xrange(pPlot.getNumUnits()):
					pUnit = pPlot.getUnit(iUnit)
					if not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMMANDER')):
						if not pTeam.isAtWar(pUnit.getTeam()):
							pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MILITARY_LEADERSHIP'), True)
"""
# Kaijin <<< End

# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
def effectCommandedLine(argsList):
	pCaster = argsList[0]

	iX = pCaster.getX()
	iY = pCaster.getY()
	pPlayer = gc.getPlayer(pCaster.getOwner())
	pTeam = gc.getTeam(pPlayer.getTeam())
	iCommander = 0
	for iiX in xrange(iX-3, iX+4, 1):
		for iiY in xrange(iY-3, iY+4, 1):
			pPlot = CyMap().plot(iiX,iiY)
			if not pPlot.isNone():
				for iUnit in xrange(pPlot.getNumUnits()):
					pUnit = pPlot.getUnit(iUnit)
					if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMMANDER')):
						iCommander = 1
	if iCommander == 0:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MILITARY_LEADERSHIP'), False)
"""
# Kaijin <<< End
#Linage End

#Mazatl Start
def spellMonsoon(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iPlayer = pCaster.getOwner()
	iWettedChance = 200
	pPlayer = gc.getPlayer(iPlayer)
	eTeam = pCaster.getTeam()
	eEffect = gc.getInfoTypeForString('EFFECT_WATER_SUMMON')

	for i in xrange (CyMap().numPlots()):
		pPlot = CyMap().plotByIndex(i)
		if pPlot.isOwned():
			if pPlot.getOwner() == iPlayer:
				if pPlot.getFeatureType() == en.eFeatureFlames:
					pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
				elif pPlot.getImprovementType() == en.eImprovementSmoke:
					pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
				elif pPlot.getTerrainType() == en.eTerrainGrass and pPlot.getFeatureType() in (en.eFeatureForest, en.eFeatureJungle):
					pPlot.setFeatureType(en.eFeatureDeepJungle, 0)

				elif pPlot.isFlatlands() and not pPlot.isCity():
					iChanceRnd = iWettedChance
					if pPlot.isRiver():
						iChanceRnd = iWettedChance * 3
					if CyGame().getSorenRandNum(1000, "Wetted") < iChanceRnd:
						pPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
						pPlot.clearColdCounter()
						if pPlot.getTerrainType() == en.eTerrainPlains and pPlot.getFeatureType() in (FeatureTypes.NO_FEATURE, en.eFeatureForest):
							pPlot.setTerrainType(en.eTerrainGrass, True, True)
							pPlot.setFeatureType(en.eFeatureJungle, 0)
						elif pPlot.getTerrainType() == en.eTerrainGrass and pPlot.getFeatureType() in (FeatureTypes.NO_FEATURE, en.eFeatureForestNew):
							pPlot.setFeatureType(en.eFeatureJungle, 0)
						elif pPlot.getTerrainType() == en.eTerrainDesert and pPlot.getFeatureType() in (FeatureTypes.NO_FEATURE, en.eFeatureScrub):
							pPlot.setTerrainType(en.eTerrainMarsh, True, True)
							pPlot.setFeatureType(en.eFeatureSwamp, 0)
						elif pPlot.getTerrainType() == en.eTerrainMarsh and pPlot.getFeatureType() == FeatureTypes.NO_FEATURE:
							pPlot.setFeatureType(en.eFeatureSwamp, 0)

				for iUnit in xrange(pPlot.getNumUnits()):
					pUnit = pPlot.getUnit(iUnit)
					if not pUnit.canFight():
						continue
					if pUnit.isEnemy(eTeam, pUnit.plot()):
						pUnit.doDamage(60, 80, en.eDamageLightning)
				if pPlot.isVisibleToWatchingHuman():
					CyEngine().triggerEffect(eEffect, pPlot.getPoint())

#Mazatl End
#Cualli Start
def reqSlaveDrive(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getNumCities() == 0:
		return ReasonTypes.REASON_DISABLED_REQUIRES_CITY
	if not pPlayer.isHuman():
# ent >>>
#		if pPlayer.getNumCities() < gc.getWorldInfo(CyMap().getWorldSize()).getTargetNumCities():
#			return False
		if cf.AI_hasRoomForFound(pCaster.getOwner()):
			return False
# ent <<<
	return True

def spellSlaveDrive(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	iSlaveBuilding = gc.getInfoTypeForString('BUILDING_SLAVE_PIT')
	for iCity in xrange(pPlayer.getNumCities()):
		pCity = pPlayer.getCity(iCity)
		pCity.setNumRealBuilding(iSlaveBuilding, 1)

def reqSlaveInThePit(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	if pCity.getFreeSpecialistCount(en.eSpecialistCitizen) >= 15:
		return False
	return True

def spellSlaveInThePit(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	pCity.changeFreeSpecialistCount(en.eSpecialistCitizen, 1)

"""
def reqSlaveInThePitAI(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.isHuman():
		return False
	iTeam = gc.getPlayer(pCaster.getOwner()).getTeam()
	eTeam = gc.getTeam(iTeam)
	if eTeam.getAtWarCount(True) > 0:
		return False
	pPlot = pCaster.plot()
	iOwner = pCaster.getOwner()
	bValid = False
	for pyCity in PyPlayer(iOwner).getCityList():
		if bValid == False:
			pCity = pyCity.GetCy()
			if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_SLAVE_PIT')) == 1:
				if pCity.getFreeSpecialistCount(gc.getInfoTypeForString('SPECIALIST_CITIZEN')) < 15:
					bValid = True
	if bValid == False:
		return False
	return True

def spellSlaveInThePitAI(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pPlot = pCaster.plot()
	iOwner = pCaster.getOwner()
	bValid = False
	for pyCity in PyPlayer(iOwner).getCityList():
		if bValid == False:
			pCity = pyCity.GetCy()
			if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_SLAVE_PIT')) == 1:
				if pCity.getFreeSpecialistCount(gc.getInfoTypeForString('SPECIALIST_CITIZEN')) < 15:
					bValid = True
	pCity.changeFreeSpecialistCount(gc.getInfoTypeForString('SPECIALIST_CITIZEN'), 1)
"""

# ent >>>
def disabledSacrificeAndBlessing(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) == 0:
			return True
		if pPlot.isOwned():
			if not pTeam.isAtWar(pPlot.getOwner()):
				return True
		eProm = gc.getInfoTypeForString('PROMOTION_BLOODY_BLADE')
		lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
		iNumTarget = 0
		for pUnit in lpRangedUnits:
			if pUnit.isPromotionValid(eProm):
				if not pUnit.isHasPromotion(eProm):
					iNumTarget += 1
					if iNumTarget > 5:
						return False
		return True
	return False

"""
def reqSacrificeAndBlessing(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) == 0:
			return False

	eReason = ReasonTypes.REASON_DISABLED_HAS_NO_TARGET
	eProm = gc.getInfoTypeForString('PROMOTION_BLOODY_BLADE')
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	if pCaster.isHuman():
		for pUnit in lpRangedUnits:
#			if pUnit.getUnitCombatType() in (en.eUnitCombatRecon, en.eUnitCombatArcher, en.eUnitCombatMounted, en.eUnitCombatMelee, en.eUnitCombatAdept, en.eUnitCombatDisciple):
			if pUnit.isPromotionValid(eProm):
				if not pUnit.isHasPromotion(eProm):
					return True
				else:
					eReason = ReasonTypes.REASON_DISABLED_ALREADY_BUFFED
	else:
		iNumTarget = 0
		for pUnit in lpRangedUnits:
#			if pUnit.getUnitCombatType() in (en.eUnitCombatRecon, en.eUnitCombatArcher, en.eUnitCombatMounted, en.eUnitCombatMelee, en.eUnitCombatAdept, en.eUnitCombatDisciple):
			if pUnit.isPromotionValid(eProm):
				if not pUnit.isHasPromotion(eProm):
					iNumTarget += 1
		if iNumTarget > 5:
			return True
	return eReason
"""
# ent <<<

def spellSacrificeAndBlessing(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	ePlayer = pCaster.getOwner()
	iCasterID = pCaster.getID()
	eSlave = gc.getSpellInfo(eSpell).getUnitInStackPrereq()
	pVictim = -1
	for iUnitIndex in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(iUnitIndex)
		if pUnit.getOwner() == ePlayer:
			if pUnit.getUnitType() == eSlave:
				if pVictim == -1 or pVictim.getExperience() > pUnit.getExperience():
					if pUnit.getID() != iCasterID:
						pVictim = pUnit
	if pVictim != -1:
		pVictim.kill(False, PlayerTypes.NO_PLAYER)

# ent >>>
def disabledBlessedOfAgruonn(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) == 0:
			return True
		if pPlot.isOwned():
			if not pTeam.isAtWar(pPlot.getOwner()):
				return True
		eProm = gc.getInfoTypeForString('PROMOTION_BLESSED_OF_AGRUONN')
		lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
		iNumTarget = 0
		for pUnit in lpRangedUnits:
			if pUnit.isPromotionValid(eProm):
				if not pUnit.isHasPromotion(eProm):
					iNumTarget += 1
					if iNumTarget > 5:
						return False
		return True
	return False

"""
def reqBlessedOfAgruonn(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) == 0:
			return False

	eReason = ReasonTypes.REASON_DISABLED_HAS_NO_TARGET
	eProm = gc.getInfoTypeForString('PROMOTION_BLESSED_OF_AGRUONN')
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	if pCaster.isHuman():
		for pUnit in lpRangedUnits:
#			if pUnit.getUnitCombatType() in (en.eUnitCombatRecon, en.eUnitCombatArcher, en.eUnitCombatMounted, en.eUnitCombatMelee, en.eUnitCombatAdept, en.eUnitCombatDisciple):
			if pUnit.isPromotionValid(eProm):
				if not pUnit.isHasPromotion(eProm):
					return True
				else:
					eReason = ReasonTypes.REASON_DISABLED_ALREADY_BUFFED
	else:
		iNumTarget = 0
		for pUnit in lpRangedUnits:
#			if pUnit.getUnitCombatType() in (en.eUnitCombatRecon, en.eUnitCombatArcher, en.eUnitCombatMounted, en.eUnitCombatMelee, en.eUnitCombatAdept, en.eUnitCombatDisciple):
			if pUnit.isPromotionValid(eProm):
				if not pUnit.isHasPromotion(eProm):
					iNumTarget += 1
		if iNumTarget > 5:
			return True
	return eReason
"""
# ent <<<

def reqSacrificeForAgronn(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	kSpell = gc.getSpellInfo(eSpell)
	eSlave = kSpell.getUnitPrereq()
	iNumSlave = 0
	for i in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(i)
		if pUnit.getOwner() == ePlayer and pUnit.getUnitType() == eSlave:
			iNumSlave += 1
			if iNumSlave >= 3:
				return True
	return False

def spellSacrificeForAgronn(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlot = pCaster.plot()
	kSpell = gc.getSpellInfo(eSpell)
	eSlave = kSpell.getUnitPrereq()
	iNumSlave = 0
	for i in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(i)
		if pUnit.getOwner() == ePlayer and pUnit.getUnitType() == eSlave:
			iNumSlave += 1
			pUnit.setHasCasted(True)
			pUnit.kill(True, PlayerTypes.NO_PLAYER)

	eBlessedofAgruonn = gc.getInfoTypeForString('PROMOTION_BLESSED_OF_AGRUONN')
	eBloodyBlade = gc.getInfoTypeForString('PROMOTION_BLOODY_BLADE')
	if iNumSlave >= 3 and iNumSlave < 9:
		py = PyPlayer(ePlayer)
		for pUnit in py.getUnitList():
			if pUnit.canFight():
				pUnit.setHasPromotion(eBlessedofAgruonn, True)
		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SACRIFICE_FOR_AGRUONN_1', ())
	elif iNumSlave >= 9 and iNumSlave < 15:
		py = PyPlayer(ePlayer)
		for pUnit in py.getUnitList():
			if pUnit.canFight():
				pUnit.changeExperience(4, -1, False, False, False)
				pUnit.setHasPromotion(eBlessedofAgruonn, True)
		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SACRIFICE_FOR_AGRUONN_2', ())
	elif iNumSlave >= 15:
		pPlayer = gc.getPlayer(ePlayer)
		pPlayer.changeGoldenAgeTurns(CyGame().goldenAgeLength() // 2)
		py = PyPlayer(ePlayer)
		for pUnit in py.getUnitList():
			if pUnit.canFight():
				pUnit.changeExperience(4, -1, False, False, False)
				pUnit.setHasPromotion(eBlessedofAgruonn, True)
				pUnit.setHasPromotion(eBloodyBlade, True)
				pUnit.setDamage(0, PlayerTypes.NO_PLAYER)
		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SACRIFICE_FOR_AGRUONN_3', ())
	szButton = kSpell.getButton()
	CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorWhite, pCaster.getX(), pCaster.getY(), True, True)

#Cualli End

#Altair Start
def reqBornDragonPuppy(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isAutomated():
		return False
	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.AI_isFinancialTrouble():
			return False
		eSummonedUnit = gc.getSpellInfo(eSpell).getCreateUnitType()
		eUnitClass = gc.getUnitInfo(eSummonedUnit).getUnitClassType()
		liMax = [12, 16, 20, 24, 28, 36]
		iMax = liMax[CyMap().getWorldSize()]
		if iMax <= pPlayer.getUnitClassCount(eUnitClass):
			return False
# ent >>>
		for pLoopUnit in PyPlayer(pCaster.getOwner()).getUnitList():
			if pLoopUnit.getUnitType() == eSummonedUnit:
				if pLoopUnit.hasUpgrade(False):
					return False
# ent <<<
	return True

def disabledBornDragonPuppy(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isAutomated():
		return True
	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.AI_isFinancialTrouble():
			return True
		eSummonedUnit = gc.getSpellInfo(eSpell).getCreateUnitType()
		eUnitClass = gc.getUnitInfo(eSummonedUnit).getUnitClassType()
		liMax = [12, 16, 20, 24, 28, 36]
		iMax = liMax[CyMap().getWorldSize()]
		if iMax <= pPlayer.getUnitClassCount(eUnitClass):
			return True
# ent >>>
		for pLoopUnit in PyPlayer(pCaster.getOwner()).getUnitList():
			if pLoopUnit.getUnitType() == eSummonedUnit:
				if pLoopUnit.hasUpgrade(False):
					return True
# ent <<<
	return False

# ent >>>
def spellBornDragonPuppy(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]
	liSummonedUnitIDs = argsList[3]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCity = pCaster.plot().getPlotCity()
	if not pCity.isNone():
		for iSummonedUnitID in liSummonedUnitIDs:
			pNewUnit = pPlayer.getUnit(iSummonedUnitID)
			pCity.applyBuildEffects(pNewUnit)

def disabledDragonGrow(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.AI_isFinancialTrouble():
			return True
		if pCaster.hasUpgrade(False):
			return True
		if gc.getUnitInfo(pCaster.getUnitType()).getTier() < 2:
			return True
		if pPlayer.isFeatAccomplished(FeatTypes.FEAT_GLOBAL_SPELL):
			return True
	return False

def disabledDragonScale(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.AI_isFinancialTrouble():
			return True
		if pCaster.hasUpgrade(False):
			return True
		if gc.getUnitInfo(pCaster.getUnitType()).getTier() < 3:
			return True
	return False
# ent <<<

def reqAnimalEatenPuppy(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.getExperience() >= 17:
		return False

	ePlayer = pCaster.getOwner()
	iCasterID = pCaster.getID()
	for i in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(i)
		if pUnit.getOwner() == ePlayer:
			if pUnit.isAlive() and pUnit.getUnitCombatType() == en.eUnitCombatAnimal:
				if pUnit.getID() != iCasterID:
					return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellAnimalEatenPuppy(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	ePlayer = pCaster.getOwner()
	iCasterID = pCaster.getID()
	for iUnitIndex in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(iUnitIndex)
		if pUnit.getOwner() == ePlayer:
			if pUnit.isAlive() and pUnit.getUnitCombatType() == en.eUnitCombatAnimal:
				if pUnit.getID() != iCasterID:
					pCaster.changeExperience(pUnit.getExperience()+2, -1, False, False, False)
					pUnit.kill(True, PlayerTypes.NO_PLAYER)

def reqPredation(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.getRace() in (en.eRaceDragon, en.eRaceDragonling):
		return False
	
	if pCaster.getDamage() == 0:
		if not pCaster.isMadeAttack() or not pCaster.isFastChant():
			leCurePromotions = [	gc.getInfoTypeForString('PROMOTION_DISEASED'),
									gc.getInfoTypeForString('PROMOTION_PLAGUED'),
									gc.getInfoTypeForString('PROMOTION_WITHERED'),
									gc.getInfoTypeForString('PROMOTION_PEST')	]
			for i in xrange(len(leCurePromotions)):
				if pCaster.isHasPromotion(leCurePromotions[i]):
					break
			else:
				return ReasonTypes.REASON_DISABLED_FULL_STOMACH_BLOODY
#	if not pCaster.isHuman():
#		if pCaster.getDamage() < 20:
#			return False
	ePlayer = pCaster.getOwner()
	iCasterID = pCaster.getID()
	lpRangedUnits = cyGetRangedUnits(pPlot, 0, False, False, TeamTypes.NO_TEAM)
	for pUnit in lpRangedUnits:
		if pUnit.getOwner() == ePlayer:
			if pUnit.isAlive() and not pUnit.getRace() in (en.eRaceDragon, en.eRaceDragonling):
				if pUnit.getID() != iCasterID:
					return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellPredation(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	iCasterID = pCaster.getID()
	pPlot = pCaster.plot()
	lpRangedUnits = cyGetRangedUnits(pPlot, 0, False, False, TeamTypes.NO_TEAM)
	pVictim = -1
	iBestValue = 0
	for pUnit in lpRangedUnits:
		if pUnit.getOwner() == ePlayer:
			if pUnit.isAlive() and not pUnit.getRace() in (en.eRaceDragon, en.eRaceDragonling):
				if pUnit.getID() != iCasterID:
					iValue = (pUnit.getCombatAttackTimes100() + pUnit.getCombatDefenseTimes100()) // 20 + pUnit.getExperience()
					if pVictim == -1 or iValue > iBestValue:
						pVictim = pUnit
						iBestValue = iValue
	if pVictim != -1:
		pVictim.kill(False, PlayerTypes.NO_PLAYER)

def reqAwakening(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.isHuman():
		if pPlayer.getNumUnits() < 50:
			return False
		if not pPlayer.isHasTech(gc.getInfoTypeForString('TECH_MITHRIL_WORKING')):
			return False
#		if not pPlayer.isHasTech(gc.getInfoTypeForString('TECH_OMNISCIENCE')):
#			return False
	return True

def spellAwakening(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	eLesserDragon = gc.getInfoTypeForString('PROMOTION_LESSER_DRAGON')
	eElderDragon = gc.getInfoTypeForString('PROMOTION_ELDER_DRAGON')
	eGreaterDragon = gc.getInfoTypeForString('PROMOTION_GREATER_DRAGON')
	eAncientDragon = gc.getInfoTypeForString('PROMOTION_ANCIENT_DRAGON')

	py = PyPlayer(pCaster.getOwner())
	for pUnit in py.getUnitList():
		if pUnit.isAlive():
			if not pUnit.isHasPromotion(eAncientDragon):
				if pUnit.getRace() in (en.eRaceDragon, en.eRaceDragonling):
					pUnit.setHasPromotion(eAncientDragon, True)
					pUnit.setHasPromotion(eLesserDragon, False)
					pUnit.setHasPromotion(eElderDragon, False)
					pUnit.setHasPromotion(eGreaterDragon, False)
					if CyGame().getSorenRandNum(100, "Enraged") < 50:
						pUnit.setHasPromotion(en.ePromotionEnraged, False)
	pPlayer = gc.getPlayer(pCaster.getOwner())
	for eTrait in xrange(gc.getNumTraitInfos()):
		if pPlayer.hasTrait(eTrait):
			if eTrait != en.eTraitAgnostic:
				pPlayer.setHasTrait(eTrait, False)
	pPlayer.changeNoDiplomacyWithEnemies(1)
	eTeam = pPlayer.getTeam()
	pTeam = gc.getTeam(eTeam)
	for eLoopTeam in xrange(gc.getMAX_CIV_TEAMS()):
		if eLoopTeam != eTeam:
			pLoopTeam = gc.getTeam(eLoopTeam)
			if pLoopTeam.isAlive() and not pLoopTeam.isAVassal():
				pTeam.declareWar(eLoopTeam, False, WarPlanTypes.WARPLAN_TOTAL)

"""
def reqBrazeAltair(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	iX = pCaster.getX()
	iY = pCaster.getY()
	pPlayer = gc.getPlayer(pCaster.getOwner())
	iTeam = pPlayer.getTeam()
	eTeam = gc.getTeam(iTeam)
	for iiX in xrange(iX-1, iX+2, 1):
		for iiY in xrange(iY-1, iY+2, 1):
			pPlot = CyMap().plot(iiX,iiY)
			bEnemy = False
			bNeutral = False
			for i in xrange(pPlot.getNumUnits()):
				pUnit = pPlot.getUnit(i)
				if eTeam.isAtWar(pUnit.getTeam()):
					bEnemy = True
				else:
					bNeutral = True
			if (bEnemy and bNeutral == False):
				return True
	return False
"""

def spellCrimsonNote(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	eEffect = gc.getInfoTypeForString('EFFECT_PILLAR_OF_FIRE')
	pPlot = pCaster.plot()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		if not pTargetPlot.isWater():
			if pTargetPlot.getFeatureType() != en.eFeatureFlames:
				iRnd = CyGame().getSorenRandNum(100, "Bob")
				if iRnd < 25:
					pTargetPlot.setFeatureType(en.eFeatureFlames, 0)
					if pTargetPlot.getImprovementType() == en.eImprovementSmoke:
						pTargetPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
					pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
					pTargetPlot.clearColdCounter()
					if pTargetPlot.getTerrainType() in (en.eTerrainGrass, en.eTerrainPlains, en.eTerrainMarsh):
						pTargetPlot.setTerrainType(en.eTerrainDesert, True, True)
					elif pTargetPlot.getTerrainType() == en.eTerrainSnow:
						pTargetPlot.setTerrainType(en.eTerrainTundra, True, True)
					if pTargetPlot.isVisibleToWatchingHuman():
						CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())

def spellEvilDead(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	eEffect = gc.getInfoTypeForString('EFFECT_RESURRECTION')
	pPlot = pCaster.plot()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.isCity():
			pCity = pTargetPlot.getPlotCity()
			if not gc.getPlayer(pCity.getOwner()).isIgnoreFood() and pCity.getCivilizationType() != en.eCivilizationAltair:
				if pTargetPlot.isVisibleToWatchingHuman():
					CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())
				i = CyGame().getSorenRandNum(5, "EvilDead")
				i += pCity.getPopulation()
				i -= pCity.totalGoodBuildingHealth()
				if i > 0:
					pCity.changeEspionageHealthCounter(i)
		else:
			if pTargetPlot.isFlatlands() or pTargetPlot.isHills():
				if pTargetPlot.getFeatureType() != en.eFeatureHauntedLands:
					iRnd = CyGame().getSorenRandNum(100, "Bob")
					if iRnd < 25:
						if pTargetPlot.isVisibleToWatchingHuman():
							CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())
						pTargetPlot.setFeatureType(en.eFeatureHauntedLands, 0)

def spellRadiantGale(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	eEffect = gc.getInfoTypeForString('EFFECT_SNOWFALL')
	pPlot = pCaster.plot()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		iRnd = CyGame().getSorenRandNum(100, "Bob")
		if iRnd < 20:
			if not pTargetPlot.isCity():
				if pTargetPlot.getNumUnits() == 0:
					if pTargetPlot.isFlatlands():
						if pTargetPlot.isVisibleToWatchingHuman():
							CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())
						pTargetPlot.setBonusType(BonusTypes.NO_BONUS)
						pTargetPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
						pTargetPlot.setPlotType(PlotTypes.PLOT_OCEAN, True, True)
						pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
						pTargetPlot.clearColdCounter()
		if iRnd < 50:
			if pTargetPlot.getTerrainType() == en.eTerrainDesert:
				if pTargetPlot.isVisibleToWatchingHuman():
					CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())
				pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
				pTargetPlot.clearColdCounter()
				pTargetPlot.setTerrainType(en.eTerrainMarsh, True, True)

def spellEarthquakeZahhak(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	eEffect = gc.getInfoTypeForString('EFFECT_SNOWFALL')
	pPlot = pCaster.plot()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		if not pTargetPlot.isCity():
			iRnd = CyGame().getSorenRandNum(100, "Bob")
			if iRnd < 50:

				if pTargetPlot.isFlatlands():
					if pTargetPlot.isVisibleToWatchingHuman():
						CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())
					if iRnd < 30:
						pTargetPlot.setPlotType(PlotTypes.PLOT_HILLS, True, True)
						if pTargetPlot.getTerrainType() == en.eTerrainPlains:
							pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
							pTargetPlot.clearColdCounter()
							if pTargetPlot.getLatitude() > 60:
								pTargetPlot.setTerrainType(en.eTerrainSnow, True, True)
							elif pTargetPlot.getLatitude() > 40:
								pTargetPlot.setTerrainType(en.eTerrainTundra, True, True)
							elif pTargetPlot.getLatitude() <= 10:
								pTargetPlot.setTerrainType(en.eTerrainDesert, True, True)
					elif pTargetPlot.getNumUnits() == 0:
						if not pTargetPlot.isRiver():
							pTargetPlot.setBonusType(BonusTypes.NO_BONUS)
							pTargetPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
							pTargetPlot.setPlotType(PlotTypes.PLOT_OCEAN, True, True)
							pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
							pTargetPlot.clearColdCounter()

				elif pTargetPlot.isPeak() and pTargetPlot.getNumUnits() == 0:
					if pTargetPlot.isVisibleToWatchingHuman():
						CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())
					pTargetPlot.setPlotType(PlotTypes.PLOT_HILLS, True, True)
					pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
					pTargetPlot.clearColdCounter()
					if pTargetPlot.getLatitude() > 60:
						pTargetPlot.setTerrainType(en.eTerrainSnow, True, True)
					elif pTargetPlot.getLatitude() > 40:
						pTargetPlot.setTerrainType(en.eTerrainTundra, True, True)
					elif pTargetPlot.getLatitude() <= 10:
						pTargetPlot.setTerrainType(en.eTerrainDesert, True, True)

				elif pTargetPlot.isWater() and pTargetPlot.getNumUnits() == 0:
					if not pTargetPlot.isRiver():
						if pTargetPlot.isVisibleToWatchingHuman():
							CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())
						pTargetPlot.setBonusType(BonusTypes.NO_BONUS)
						pTargetPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
						pTargetPlot.setPlotType(PlotTypes.PLOT_LAND, True, True)

						pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
						pTargetPlot.clearColdCounter()
						if pTargetPlot.getLatitude() > 60:
							pTargetPlot.setTerrainType(en.eTerrainSnow, True, True)
						elif pTargetPlot.getLatitude() > 40:
							pTargetPlot.setTerrainType(en.eTerrainTundra, True, True)
						else:
							pTargetPlot.setTerrainType(en.eTerrainMarsh, True, True)

				elif pTargetPlot.isHills():
					if iRnd < 30:
						if pTargetPlot.isVisibleToWatchingHuman():
							CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())
						pTargetPlot.setPlotType(PlotTypes.PLOT_LAND, True, True)
					elif pTargetPlot.getNumUnits() == 0:
						if pTargetPlot.isVisibleToWatchingHuman():
							CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())
						pTargetPlot.setPlotType(PlotTypes.PLOT_PEAK, True, True)
						pTargetPlot.setBonusType(BonusTypes.NO_BONUS)
						pTargetPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
						iImprovement = pTargetPlot.getImprovementType()
						if iImprovement != ImprovementTypes.NO_IMPROVEMENT:
							if not gc.getImprovementInfo(iImprovement).isPermanent():
								pTargetPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)

				if pTargetPlot.getFeatureType() == en.eFeatureVolcano:
					pTargetPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
					if pTargetPlot.isOwned():
						if pTargetPlot.getTeam() != eTeam:
							pTeam = gc.getTeam(eTeam)
							pTeam.declareWar(pTargetPlot.getTeam(), False, WarPlanTypes.WARPLAN_LIMITED)

# ent >>>
def spellFreezingBreath(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_SEVERED_SOUL'), pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setName(pCaster.getNameKey())
	pNewUnit.cast(gc.getInfoTypeForString('SPELL_FREEZING_BREATH_SECONDARY'))
	pNewUnit.kill(False, PlayerTypes.NO_PLAYER)

def spellFreezingBreathSecondary(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	kSpell = gc.getSpellInfo(eSpell)
	iDamage = kSpell.getDamage()
	eEffect = gc.getInfoTypeForString('EFFECT_SNOWFALL')
	pPlot = pCaster.plot()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		if not pTargetPlot.isWater():
			if pTargetPlot.isVisibleToWatchingHuman():
				CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())
			iColdCounter = CyGame().getSorenRandNum(600 + iDamage * 60, 'Snowfall') + 1800 + iDamage * 180
			pTargetPlot.ceilColdCounter(iColdCounter, 2000)
# ent <<<

def spellFreezingBreathGreator(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	kSpell = gc.getSpellInfo(eSpell)
	iDamage = kSpell.getDamage()
	eEffect = gc.getInfoTypeForString('EFFECT_SNOWFALL')
	pPlot = pCaster.plot()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		if not pTargetPlot.isWater():
			if pTargetPlot.isVisibleToWatchingHuman():
				CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())
			iColdCounter = CyGame().getSorenRandNum(600 + iDamage * 60, 'Snowfall') + 1800 + iDamage * 180
			pTargetPlot.ceilColdCounter(iColdCounter, 2000)

def reqGiftAncientDragon(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.isFeatAccomplished(FeatTypes.FEAT_GLOBAL_SPELL):
		return False
	eAncientDragon = gc.getInfoTypeForString('PROMOTION_ANCIENT_DRAGON')
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if not pUnit.isHasPromotion(eAncientDragon):
			if pUnit.getRace() in (en.eRaceDragon, en.eRaceDragonling):
				return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellGiftAncientDragon(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	eAncientDragon = gc.getInfoTypeForString('PROMOTION_ANCIENT_DRAGON')
	eLesserDragon = gc.getInfoTypeForString('PROMOTION_LESSER_DRAGON')
	eElderDragon = gc.getInfoTypeForString('PROMOTION_ELDER_DRAGON')
	eGreaterDragon = gc.getInfoTypeForString('PROMOTION_GREATER_DRAGON')

	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if not pUnit.isHasPromotion(eAncientDragon):
			if pUnit.getRace() in (en.eRaceDragon, en.eRaceDragonling):
				pUnit.setHasPromotion(eAncientDragon, True)
				pUnit.setHasPromotion(eLesserDragon, False)
				pUnit.setHasPromotion(eElderDragon, False)
				pUnit.setHasPromotion(eGreaterDragon, False)

def reqAddToDragonMaster(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	iCasterID = pCaster.getID()
	eDragonMaster = gc.getSpellInfo(eSpell).getUnitInStackPrereq()
	for iUnitIndex in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(iUnitIndex)
		if pUnit.getUnitType() == eDragonMaster:
			if pUnit.getOwner() == ePlayer:
				if pUnit.getID() != iCasterID:
					if not pUnit.isHasPromotion(en.ePromotionEmpower5):
						return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellAddToDragonMaster(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	ePlayer = pCaster.getOwner()
	iCasterID = pCaster.getID()
	eDragonMaster = gc.getSpellInfo(eSpell).getUnitInStackPrereq()
	leEmpower = [	en.ePromotionEmpower5,
					en.ePromotionEmpower4,
					en.ePromotionEmpower3,
					en.ePromotionEmpower2,
					en.ePromotionEmpower1	]

	lpTargetList = []
	for iUnitIndex in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(iUnitIndex)
		if pUnit.getUnitType() == eDragonMaster:
			if pUnit.getOwner() == ePlayer:
				if pUnit.getID() != iCasterID:
					if not pUnit.isHasPromotion(leEmpower[0]):
						for iLoop, iEmpower in enumerate(leEmpower):
							if pUnit.isHasPromotion(iEmpower):
								lpTargetList.append((iLoop, pUnit))
								break
							else:
								lpTargetList.append((len(leEmpower), pUnit))
	lpTargetList.sort()
	iEmpowerIndex	= lpTargetList[0][0]
	pTarget			= lpTargetList[0][1]

	pTarget.setHasPromotion(leEmpower[iEmpowerIndex - 1], True)

#Altair End
#Mechanos Start

def reqSteamworks(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getCurrentResearch() == TechTypes.NO_TECH:
		return False

	if not pCaster.isHuman():
		pCity = pPlot.getPlotCity()
		if not pCity.isCapital():
			return False
#		if pPlayer.getImprovementCount(gc.getInfoTypeForString('IMPROVEMENT_WORKSHOP')) < 5:
#			return False
	return True

def spellSteamworks(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	pTeam = gc.getTeam(pCaster.getTeam())
	eTech = pPlayer.getCurrentResearch()
	iNum = 20
	iNum += pPlayer.getImprovementCount(gc.getInfoTypeForString('IMPROVEMENT_WORKSHOP')) * 60
	iNum += pPlayer.getImprovementCount(gc.getInfoTypeForString('IMPROVEMENT_WATERMILL')) * 50
	iNum += pPlayer.getImprovementCount(gc.getInfoTypeForString('IMPROVEMENT_WINDMILL')) * 50
	pTeam.changeResearchProgress(eTech, iNum, ePlayer)

#Mechanos End

#Scions Start
# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
def effectCheckBurrs(argsList):
	pCaster = argsList[0]

	pPlot = pCaster.plot()
	if CyGame().getSorenRandNum(10, "BurrsHatching") < 3:
#		if (pCaster.getLevel() >= 6 or pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_HERO'))):
		if pCaster.getDamage() < 80:
			CyInterface().addMessage(pCaster.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_BURRS_SURVIVED", ()),'',1,'Art_Kaijin/Interface/Buttons/Promotions/Burrs.dds',en.eColorRed,pPlot.getX(),pPlot.getY(),True,True)
			pCaster.setDamage(20, PlayerTypes.NO_PLAYER)
		else:
			CyInterface().addMessage(pCaster.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_BURRS_DESTROYED", ()),'',1,'Art_Kaijin/Interface/Buttons/Promotions/Burrs.dds',en.eColorRed,pPlot.getX(),pPlot.getY(),True,True)
			pCaster.kill(True, PlayerTypes.NO_PLAYER)
			if not pPlot.isCity():
				pNewUnit = gc.getPlayer(gc.getANIMAL_PLAYER()).initUnit(gc.getInfoTypeForString('UNIT_CREEPER'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
				pNewUnit.changeExperience(pCaster.getExperience() / 2, -1, False, False, False)
"""
# Kaijin <<< End

# Spell for Awakened and Reborn
def reqScionsAddPopuration(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		# Control in PythonSpecificAI
		if pCaster.getUnitAIType() != UnitAITypes.UNITAI_CITY_SPECIAL:
			return False
	if pPlot.isCity():
		pCity = pPlot.getPlotCity()
		if cf.doAddPopValid(pCity):
			return True

	return False

#Thaumaturge's Keep
def reqThaumaturge(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())

	if pPlayer.getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_THAUMATURGE_KEEP')) > 0:
		return ReasonTypes.REASON_DISABLED_BUILDING_ALREADY_EXISTS
	if pCity.isCapital():
		if not (CyGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and pPlayer.isHuman()):
			return False
	if not pPlayer.isHuman():
		if pCity.getBaseCommerceRateTimes100(CommerceTypes.COMMERCE_CULTURE) < 200:
			return False

	return True

# Sets up the Thaumaturge's Keep campus.
def spellThaumaturge(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())

	leKeepNode = [	gc.getInfoTypeForString('BUILDING_KEEP_BODY'),
					gc.getInfoTypeForString('BUILDING_KEEP_LAW'),
					gc.getInfoTypeForString('BUILDING_KEEP_ENCHANTMENT'),
					gc.getInfoTypeForString('BUILDING_KEEP_EARTH'),
					gc.getInfoTypeForString('BUILDING_KEEP_ENTROPY'),
					gc.getInfoTypeForString('BUILDING_KEEP_MIND'),
					gc.getInfoTypeForString('BUILDING_KEEP_ICE'),
					gc.getInfoTypeForString('BUILDING_KEEP_SHADOW'),
					gc.getInfoTypeForString('BUILDING_KEEP_CHAOS')				]

	leKeepAnother = [	gc.getInfoTypeForString('BUILDING_MILITARY_ABATTOIR'),
						gc.getInfoTypeForString('BUILDING_KEEP_ALCHEMIST'),
						gc.getInfoTypeForString('BUILDING_SCHOLA_FURIO'),
						gc.getInfoTypeForString('BUILDING_ALCINUS_TROVE')		]

	leChosenKeep = []
	for iLoop in xrange(2):
		leChosenKeep.append(leKeepNode.pop( CyGame().getSorenRandNum(len(leKeepNode), "keep node") ))
	for iLoop in xrange(2):
		leChosenKeep.append(leKeepAnother.pop( CyGame().getSorenRandNum(len(leKeepAnother), "keep another") ))
	leChosenKeep.sort()

	for eChosenKeep in leChosenKeep:
		pCity.setNumRealBuilding(eChosenKeep, 1)

def reqSuccor(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
		# Control in PythonSpecificAI
		if pCaster.getUnitAIType() != UnitAITypes.UNITAI_CITY_SPECIAL:
			return False
	if pPlot.isCity():
		pCity = pPlot.getPlotCity()
		if pCity.getOwner() == pCaster.getOwner():
			return ReasonTypes.REASON_DISABLED_IMMUNE_OWN_CITY

	return True

def spellSuccor(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCapital = pPlayer.getCapitalCity()

	if pCity.isNone():
		return
	eReborn = gc.getInfoTypeForString('UNIT_REBORN')
	for iLoop in xrange(max(1, pCity.getPopulation() // 5)):
		pNewUnit = pPlayer.initUnit(eReborn, pCapital.getX(), pCapital.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
		pNewUnit.finishMoves()

		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_UNIT_JOIN_YOUR_CAUSE', (pNewUnit.getNameKey(), pCity.getNameKey()))
		szButton = pNewUnit.getButton()
		szSound = pNewUnit.getArtInfo(0, EraTypes.NO_ERA).getTrainSound()
		CyInterface().addMessage(pCaster.getOwner(), False, gc.getEVENT_MESSAGE_TIME(), szMessage, szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)

def reqDarkCouncil(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	ePelemoc = gc.getInfoTypeForString('UNIT_PELEMOC')
	eThemoch = gc.getInfoTypeForString('UNIT_THEMOCH')
	eAlcinus = gc.getInfoTypeForString('UNIT_ALCINUS')
	bPelemocPresent = False
	bThemochPresent = False
	bAlcinusPresent = False

	for i in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(i)
		eUnitType = pUnit.getUnitType()
		if eUnitType == ePelemoc:
			bPelemocPresent = True
		elif eUnitType == eThemoch:
			bThemochPresent = True
		elif eUnitType == eAlcinus:
			bAlcinusPresent = True
	if bPelemocPresent and bThemochPresent and bAlcinusPresent:
		return True
	return False

# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
def effectGrandWard(argsList):
	pCaster = argsList[0]

	pCaster.cast(gc.getInfoTypeForString('SPELL_GRAND_WARD'))
"""
# Kaijin <<< End

# Req for Give Gift spell. 
def reqEmbraceGift(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isHasPromotion(en.ePromotionHero):
		return ReasonTypes.REASON_DISABLED_INVALID_KIND_OF_UNIT
	if pCaster.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_KORRINA'):
		return ReasonTypes.REASON_DISABLED_INVALID_KIND_OF_UNIT
	return True

#Scions End
#Nival Start
def reqTricksNival(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getNumCities() == 0:
		return ReasonTypes.REASON_DISABLED_REQUIRES_CITY
	if not pPlayer.isHuman():
# ent >>>
#		if pPlayer.getNumCities() < gc.getWorldInfo(CyMap().getWorldSize()).getTargetNumCities():
#			return False
		if cf.AI_hasRoomForFound(pCaster.getOwner()):
			return False
# ent <<<
	return True

def spellTricksNival(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iChangeCulture = 200
	iChangeCulture *= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(CyGame().getGameSpeedType())
	iChangeCulture /= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(en.eGameSpeedNormal)
	iGuaranteedCulture = gc.getCultureLevelInfo(gc.getInfoTypeForString('CULTURELEVEL_FLEDGLING')).getSpeedThreshold(CyGame().getGameSpeedType())

	szButton = gc.getSpellInfo(eSpell).getButton()
	ePlayer = pCaster.getOwner()
	for eLoopPlayer in xrange(gc.getMAX_PLAYERS()):
		pLoopPlayer = gc.getPlayer(eLoopPlayer)
		if pLoopPlayer.isAlive():
			if eLoopPlayer != ePlayer:
				for pyCity in PyPlayer(eLoopPlayer).getCityList():
					pCity = pyCity.GetCy()
					iOldCulture = pCity.getCulture(eLoopPlayer)
					iNewCulture = min(max(iGuaranteedCulture, iOldCulture - iChangeCulture), iOldCulture)
					pCity.setCulture(eLoopPlayer, iNewCulture, True)
					iDecreaseCulture = iOldCulture - iNewCulture
					if iDecreaseCulture > 0:
						CyInterface().addMessage(eLoopPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_TRICK_NIVAL", (pCity.getNameKey(), iDecreaseCulture, )), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCity.getX(), pCity.getY(), True, True)
			else:
				for pyCity in PyPlayer(eLoopPlayer).getCityList():
					pCity = pyCity.GetCy()
					pCity.changeCulture(eLoopPlayer, iChangeCulture, True)

def reqPrankNival(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)

	if pPlot.isOwned():
		if pPlot.getOwner() == ePlayer:
			return ReasonTypes.REASON_DISABLED_IN_BORDER
	iRange = 1
	lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, True, pCaster.getTeam())
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.isOwned():
			if pTargetPlot.getOwner() == ePlayer:
				return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellPrankNival(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

# Kaijin >>>	patch29 expansion - Start -
	"""
	pPlot = pCaster.plot()
	iCulture = CyGame().getSorenRandNum(10, "Prank") +1
	iCulture *= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(CyGame().getGameSpeedType())
	iCulture /= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(en.eGameSpeedNormal)
	pPlot.changeCulture(pCaster.getOwner(), iCulture, True)
	"""
	pPlayer = gc.getPlayer(pCaster.getOwner())
	pPlot = pCaster.plot()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		iCulture = CyGame().getSorenRandNum(50, "Prank") +5
		iCulture *= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(CyGame().getGameSpeedType())
		iCulture /= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(en.eGameSpeedNormal)
		pTargetPlot.changeCulture(pCaster.getOwner(), iCulture, True)
# Kaijin <<<	patch29 expansion - End -

# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
def effectIceRoad(argsList):
	pCaster = argsList[0]

	iX = pCaster.getX()
	iY = pCaster.getY()
	iFlames = gc.getInfoTypeForString('FEATURE_FLAMES')
	iSmoke = gc.getInfoTypeForString('IMPROVEMENT_SMOKE')
	iSnow = gc.getInfoTypeForString('TERRAIN_SNOW')
	iTundra = gc.getInfoTypeForString('TERRAIN_TUNDRA')
	for iiX in xrange(iX-1, iX+2, 1):
		for iiY in xrange(iY-1, iY+2, 1):
			pPlot = CyMap().plot(iiX,iiY)
			if not pPlot.isNone() and not pPlot.isWater():
				if pPlot.getTerrainType() != iSnow:
					if pPlot.isOwned() and gc.getPlayer(pPlot.getOwner()).getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_NIVAL'):
						pPlot.setTerrainType(iSnow, True, True)
					elif pPlot.getColdCounter() < 5000 or CyGame().getSorenRandNum(100, "Iceroad") < 33:
						iColdCounter = CyGame().getSorenRandNum(1000, 'Snowfall') + 3000
						if CyGame().getSorenRandNum(1000, "Snow") >= 666:
							iColdCounter = iColdCounter // 2
						pPlot.ceilColdCounter(iColdCounter, 2000)
					if pPlot.getFeatureType() == iFlames:
						pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
					if pPlot.getImprovementType() == iSmoke:
						pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
"""
# Kaijin <<< End

# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
def effectSnowstormAvatar(argsList):
	pCaster = argsList[0]

	iX = pCaster.getX()
	iY = pCaster.getY()
	iSnow = gc.getInfoTypeForString('TERRAIN_SNOW')
	iTundra = gc.getInfoTypeForString('TERRAIN_TUNDRA')
	iBlizzard = gc.getInfoTypeForString('FEATURE_BLIZZARD')
	for iiX in xrange(iX-1, iX+2, 1):
		for iiY in xrange(iY-1, iY+2, 1):
			pPlot = CyMap().plot(iiX,iiY)
			if not pPlot.isNone():
				if pPlot.isFlatlands():
					if (pPlot.getTerrainType() == iSnow or pPlot.getTerrainType() == iTundra) and pPlot.getFeatureType() == -1:
						if CyGame().getSorenRandNum(100, "Blizzard") < 33:
							pPlot.setFeatureType(iBlizzard, 0)
"""
# Kaijin <<< End

def spellCombatBlizzard(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

# ent >>>
	"""
	pPlot = pCaster.plot()
	kSpell = gc.getSpellInfo(eSpell)
	iDamage = kSpell.getDamage()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		if not pTargetPlot.isWater():
			iColdCounter = CyGame().getSorenRandNum(600 + iDamage * 60, 'Snowfall') + 1800 + iDamage * 180
			pTargetPlot.ceilColdCounter(iColdCounter, 2000)
			if pTargetPlot.getFeatureType() == FeatureTypes.NO_FEATURE:
				if CyGame().getSorenRandNum(100, "Blizzard") < 75:
					pTargetPlot.setFeatureType(en.eFeatureBlizzard, 0)
	"""
	iCulture = gc.getUnitInfo(pCaster.getUnitType()).getPowerValue()
	iCulture *= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(CyGame().getGameSpeedType())
	iCulture /= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(en.eGameSpeedNormal)

	pPlot = pCaster.plot()
	ePlayer = pCaster.getOwner()
	if ePlayer == gc.getBARBARIAN_PLAYER() + en.eBarbarianFrostling:
		if pPlot.isOwned() and gc.getPlayer(pPlot.getOwner()).getCivilizationType() == en.eCivilizationNival:
			ePlayer = pPlot.getOwner()
		else:
			ePlayer = cf.getCivilization(en.eCivilizationNival)
		iCulture /= 2
	if ePlayer == PlayerTypes.NO_PLAYER:
		return

	pCity = pPlot.getWorkingCity()
	if not pCity.isNone() and pCity.getOwner() == ePlayer:
		pCity.changeWeLoveTheKingDayProbability(90)
	else:
		pCity = CyMap().findCity(pPlot.getX(), pPlot.getY(), ePlayer, TeamTypes.NO_TEAM, False, False, TeamTypes.NO_TEAM, DirectionTypes.NO_DIRECTION, pCity)
		iPlotDistance = plotDistance(pPlot.getX(), pPlot.getY(), pCity.getX(), pCity.getY())
		if iPlotDistance > 0:
			iCulture /= iPlotDistance
	if not pCity.isNone():
		pCity.changeCulture(ePlayer, iCulture, True)
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		pTargetPlot.changeCulture(ePlayer, iCulture, True)
# ent <<<

#Nival End
#Rarna Start
def reqPatheticFire(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.isHuman():
# ent >>>
		iRatio = cf.AI_getWarSuccessCapitulationRatio(pCaster.getOwner())
		if iRatio < -50 and iRatio > -99:
			return True
# ent <<<
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) < 2:
			return False
	return True

def spellPatheticFire(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	szButton = gc.getSpellInfo(eSpell).getButton()
	szSound = 'AS3D_UN_CATAPULT_HIT'
	eEffect = gc.getInfoTypeForString('EFFECT_PILLAR_OF_FIRE')
#Advanced Rules: Add by ent
	bFireInheritance = False
	if CyGame().getProjectCreatedCount(gc.getInfoTypeForString('PROJECT_FIRE_INHERITANCE')) > 0:
		bFireInheritance = True
#Advanced Rules: End Add
	for iPlotIndex in xrange(CyMap().numPlots()):
		pPlot = CyMap().plotByIndex(iPlotIndex)
		bEffect = False
		if pPlot.getNumUnits() > 0:
			for iUnitIndex in xrange(pPlot.getNumUnits()):
				pUnit = pPlot.getUnit(iUnitIndex)
				if pUnit.canFight():
					pUnit.doDamage(50, 90, en.eDamageFire)
			bEffect = True
		if pPlot.isCity():
			pCity = pPlot.getPlotCity()
#Advanced Rules: Add by ent
			if bFireInheritance and gc.getPlayer(pCity.getOwner()).getCivilizationType() == en.eCivilizationRarna:
				continue
#Advanced Rules: End Add
			if pCity.getDefenseModifier(False) > 0:
				pCity.changeDefenseDamage(gc.getMAX_CITY_DEFENSE_DAMAGE() - pCity.getDefenseDamage())
				bEffect = True
				CyInterface().addMessage(pCity.getOwner(), True, 25, CyTranslator().getText("TXT_KEY_MESSAGE_PATHETIC_FIRE", (pCity.getNameKey(), )), szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCity.getX(), pCity.getY(), True, True)
		if bEffect and pPlot.isVisibleToWatchingHuman():
			CyEngine().triggerEffect(eEffect, pPlot.getPoint())

def disabledBhavaagra(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
#Advanced Rules: Add by ent
		if CyGame().getProjectCreatedCount(gc.getInfoTypeForString('PROJECT_FIRE_INHERITANCE')) > 0:
			return False
#Advanced Rules: End Add
		ePlayer = pCaster.getOwner()
		lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, True)
		for pTargetPlot in lpRangedPlots:
			if pTargetPlot.isCity():
				if pTargetPlot.getOwner() == ePlayer:
					return True
	return False

def enabledBhavaagra(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

#Advanced Rules: Add by ent
	bFireInheritance = False
	if CyGame().getProjectCreatedCount(gc.getInfoTypeForString('PROJECT_FIRE_INHERITANCE')) > 0:
		bFireInheritance = True
#Advanced Rules: End Add

	ePlayer = pCaster.getOwner()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, True)
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.isCity():
			pCity = pTargetPlot.getPlotCity()
#Advanced Rules: Add by ent
			if bFireInheritance and gc.getPlayer(pCity.getOwner()).getCivilizationType() == en.eCivilizationRarna:
				continue
#Advanced Rules: End Add
			if pCity.getDefenseModifier(False) > 0:
				return True
	return False

def spellBhavaagra(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	szButton = gc.getSpellInfo(eSpell).getButton()
	szSound = 'AS3D_UN_CATAPULT_HIT'
	eEffect = gc.getInfoTypeForString('EFFECT_ARTILLERY_SHELL_EXPLODE')
#Advanced Rules: Add by ent
	bFireInheritance = False
	if CyGame().getProjectCreatedCount(gc.getInfoTypeForString('PROJECT_FIRE_INHERITANCE')) > 0:
		bFireInheritance = True
#Advanced Rules: End Add

	ePlayer = pCaster.getOwner()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, False)
	for pTargetPlot in lpRangedPlots:
		if pTargetPlot.isCity():
			pCity = pTargetPlot.getPlotCity()
#Advanced Rules: Add by ent
			if bFireInheritance and gc.getPlayer(pCity.getOwner()).getCivilizationType() == en.eCivilizationRarna:
				continue
#Advanced Rules: End Add
			if pCity.getDefenseModifier(False) > 0:
				iRemainDefense = gc.getMAX_CITY_DEFENSE_DAMAGE() - pCity.getDefenseDamage()
				iDefenseDamage = CyGame().getSorenRandNum(iRemainDefense +1, "Bhavaagra")
				pCity.changeDefenseDamage(iDefenseDamage)
				if pCity.getOwner() != ePlayer:
					CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_SCARLET_VIRTUAL_HEAVEN",(pCity.getNameKey(), iDefenseDamage, )), szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
				CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_SCARLET_VIRTUAL_HEAVEN_ENEMY",(pCity.getNameKey(), iDefenseDamage, )), szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCity.getX(), pCity.getY(), True, True)
				if pTargetPlot.isVisibleToWatchingHuman():
					CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())

def reqWedgeofReturn(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isBarbarian():
		return False
	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getNumCities() < 1:
		return ReasonTypes.REASON_DISABLED_REQUIRES_CITY
	pCity = pPlayer.getCapitalCity()
	if pCity.isNone():
		pCity, iterOut = pPlayer.firstCity(False)
	if pCaster.at(pCity.getX(), pCity.getY()):
		return ReasonTypes.REASON_DISABLED_ALREADY_BUFFED
	if not pPlayer.isHuman():
		if pCaster.getDamage() < 50:
			return False
		if pPlot.isCity():
			return False
	if pCaster.getExperience < 2:
		return False
	return True

def spellWedgeofReturn(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCaster.changeExperience(-1, -1, False, False, False)
	if pPlayer.getNumCities() > 0:
		pCity = pPlayer.getCapitalCity()
		if pCity.isNone():
			pCity, iterOut = pPlayer.firstCity(False)
		if not pCity.isNone():
			pCaster.setXY(pCity.getX(), pCity.getY(), False, True, True)

def reqSoulDepletion(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())

	if not pCaster.canFight():
		return ReasonTypes.REASON_DISABLED_CAN_NOT_FIGHT
	if not cf.doAddPopValid(pCity):
		return False
	if pCity.foodDifference(True) < 0:
		return False
	if pCaster.getExperience < 2:
		return False
	if CyGame().getProjectCreatedCount(en.eProjectSpreadCorruption) == 0:
		return False
	if not pCaster.isHuman():
		if pCaster.getUnitType() != gc.getInfoTypeForString('UNIT_SOUL_HUNTER'):
			if pCaster.getExperience() > 10:
				return False
			if isWorldUnitClass(pCaster.getUnitClassType()):
				return False
	return True

def spellSoulDepletion(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCaster.changeExperience(-2, -1, False, False, False)

def disabledSoulSucker(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if CyGame().getProjectCreatedCount(en.eProjectSpreadCorruption) == 0:
		return True
	return False

def spellSoulSucker(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCaster.changeExperience(2, -1, False, False, False)
	if pCaster.getDamage() > 0:
		pCaster.setDamage(0, PlayerTypes.NO_PLAYER)

# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
def effectSoulHunger(argsList):
	pCaster = argsList[0]

	if pCaster.getUnitType() != gc.getInfoTypeForString('UNIT_SOUL_HUNTER'):
		if CyGame().getSorenRandNum(100, "Soul Hunger") < 3:
			szButton = gc.getSpellInfo(gc.getInfoTypeForString('PROMOTION_SOUL_HUNGER')).getButton()
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SOUL_HUNGER_UNIT_KILLED', (pCaster.getNameKey(), ))
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCaster.getX(), pCaster.getY(), True, True)
			pCaster.kill(True, PlayerTypes.NO_PLAYER)
"""
# Kaijin <<< End

#Rarna End
#Tiger Start
def reqFame(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	if pPlayer.getNumCities() == 0:
		return ReasonTypes.REASON_DISABLED_REQUIRES_CITY
	if not pCaster.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) == 0:
			return False
		iTotalCreate = 0
		for pyCity in PyPlayer(ePlayer).getCityList():
			pCity = pyCity.GetCy()
			iTotalCreate += 2 * (pCity.getPopulation() // 5 + 1)
		if iTotalCreate < 3 * gc.getWorldInfo(CyMap().getWorldSize()).getTargetNumCities():
			return False
	return True

def spellFame(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	pCivilization = gc.getCivilizationInfo(pPlayer.getCivilizationType())
	iUnit = pCivilization.getCivilizationUnits(en.eUnitClassMercenary)
	if iUnit != UnitTypes.NO_UNIT:
		for pyCity in PyPlayer(iPlayer).getCityList():
			pCity = pyCity.GetCy()
			iLoop = (pCity.getPopulation() // 5) + 1
			for i in xrange(iLoop * 2):
				pNewUnit = pPlayer.initUnit(iUnit, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
				pNewUnit.changeImmobileTimer(1)

def reqOutbreakContracts(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)

	bContracted = bool(pPlayer.getGuildPlusCounter(50))
	if bContracted:
		return False

	ePlayerTeam = pPlayer.getTeam()
	pPlayerTeam = gc.getTeam(ePlayerTeam)
	if pPlayerTeam.isAVassal():
		return False

	eContractor = pCity.getOwner()
	pContractor = gc.getPlayer(eContractor)
	eContractorTeam = pContractor.getTeam()
	pContractorTeam = gc.getTeam(eContractorTeam)

	if eContractorTeam == ePlayerTeam:
		return ReasonTypes.REASON_DISABLED_IMMUNE_FRIENDLY_CITY
	if pContractorTeam.isAVassal():
		return False
	if pContractor.AI_getAttitude(ePlayer) < AttitudeTypes.ATTITUDE_CAUTIOUS:
		return False
	if not pPlayer.isHuman():
		#「今は、手一杯の状態だ。」
		if pPlayerTeam.getAtWarCount(True) > 0:
			return False
		#「貴国とはそこまでの関係を築いてはおらぬ。」
		if pPlayer.AI_getAttitude(eContractor) < AttitudeTypes.ATTITUDE_PLEASED:
			return False
		iEnemyPower = 0
		for eOtherTeam in xrange(gc.getMAX_CIV_TEAMS()):
			pOtherTeam = gc.getTeam(eOtherTeam)
			if pOtherTeam.isAlive() and not eOtherTeam in (ePlayerTeam, eContractorTeam):
				if pContractorTeam.isAtWar(eOtherTeam) and not pPlayerTeam.isAtWar(eOtherTeam):
					for eLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
						pLoopPlayer = gc.getPlayer(eLoopPlayer)
						if pLoopPlayer.isAlive() and pLoopPlayer.getTeam() == eOtherTeam:
							#「親友はどうしても裏切れないのだ！」
							if pPlayer.AI_getAttitude(eLoopPlayer) == AttitudeTypes.ATTITUDE_FRIENDLY:
								return False
							iEnemyPower += pLoopPlayer.getPower()
		iPowerRatio = pContractorTeam.getPower(True) + 2 * pPlayerTeam.getPower(True) - 2 * iEnemyPower
		#「奴らの軍事力には脅威を感じる。」
		if iPowerRatio < 0:
			return False
	for eOtherTeam in xrange(gc.getMAX_CIV_TEAMS()):
		pOtherTeam = gc.getTeam(eOtherTeam)
		if pOtherTeam.isAlive() and not eOtherTeam in (ePlayerTeam, eContractorTeam):
			if pContractorTeam.isAtWar(eOtherTeam) and not pPlayerTeam.isAtWar(eOtherTeam):
				return True

	return False

def spellOutbreakContracts(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iCasterID = pCaster.getID()
	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	if pPlayer.isHuman():
		popupInfo = CyPopupInfo()
		popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
		popupInfo.setText(CyTranslator().getText("TXT_KEY_CONTRACT",()))
		popupInfo.setData1(ePlayer)
		popupInfo.setData2(iCasterID)
		popupInfo.setPythonModule("CvSpellInterface")
		popupInfo.setOnClickedPythonCallback("selectContract")
		popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_POPUP_YES", ()), "")
		popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_POPUP_NO", ()), "")
		popupInfo.addPopup(ePlayer)
	else:
		applyContract(ePlayer, iCasterID)
 
def selectContract(argsList):
	iButton = argsList[0]
	ePlayer = argsList[1]
	iCasterID = argsList[2]

	if iButton == 0:
		applyContract(ePlayer, iCasterID)

def applyContract(ePlayer, iCasterID):
	pPlayer = gc.getPlayer(ePlayer)
	pCaster = pPlayer.getUnit(iCasterID)
	pCity = pCaster.plot().getPlotCity()
	eContractor = pCity.getOwner()
	pContractor = gc.getPlayer(eContractor)
	ePlayerTeam = pPlayer.getTeam()
	pPlayerTeam = gc.getTeam(ePlayerTeam)
	eContractorTeam = pContractor.getTeam()
	pContractorTeam = gc.getTeam(eContractorTeam)

	iStartTurn = CyGame().getGameTurnYear()
	iIndex = 60
	iNum = 0
	iRequire = 0

	#契約判定変数 0 → 1
	pPlayer.setGuildPlusCounter(50, 1)
	#契約開始ターン記録
	pPlayer.setGuildPlusCounter(51, iStartTurn)
	#契約文明情報記録
	pPlayer.setGuildPlusCounter(52, eContractor)
	#撃破数初期化
	pPlayer.setGuildPlusCounter(53, 0)
	#予定報酬初期化
	pPlayer.setGuildPlusCounter(54, 0)
	#対象文明に宣戦布告 & 対象文明情報記録（index 60～）
	for eOtherTeam in xrange(gc.getMAX_CIV_TEAMS()):
		pOtherTeam = gc.getTeam(eOtherTeam)
		if pOtherTeam.isAlive() and not eOtherTeam in (ePlayerTeam, eContractorTeam):
			if pContractorTeam.isAtWar(eOtherTeam) and not pPlayerTeam.isAtWar(eOtherTeam):
				if not pOtherTeam.isAVassal():
					pPlayerTeam.declareWar(eOtherTeam, False, WarPlanTypes.WARPLAN_CONTRACT)
					for eLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
						pLoopPlayer = gc.getPlayer(eLoopPlayer)
						if pLoopPlayer.isAlive():
							eLoopTeam = pLoopPlayer.getTeam()
							pLoopTeam = gc.getTeam(eLoopTeam)
							if eLoopTeam == eOtherTeam or pLoopTeam.isVassal(eOtherTeam):
								pPlayer.setGuildPlusCounter(iIndex, eLoopPlayer)
								iNum += 1
								iRequire += gc.getPlayer(eLoopPlayer).getNumUnits()
								iIndex += 1

	#対象文明数記録
	pPlayer.setGuildPlusCounter(59, iNum)
	#撃破目標数記録
	pPlayer.setGuildPlusCounter(55, iRequire)

	cf.addPlayerPopup(CyTranslator().getText('TXT_KEY_CONTRACT_APPROVE',()), ePlayer)
	
	for eLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
		pLoopPlayer = gc.getPlayer(eLoopPlayer)
		if pLoopPlayer.isAlive() and eLoopPlayer != ePlayer:
			eSpell = gc.getInfoTypeForString('SPELL_OUTBREAK_CONTRACTS')
			szButton = gc.getSpellInfo(eSpell).getButton()
			szSound = 'AS3D_SPELL_HOPE'
			siSpellDesc = gc.getSpellInfo(eSpell).getDescription()
			spPlayerCivDesc = gc.getCivilizationInfo(pPlayer.getCivilizationType()).getDescription()
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_CONTRACT_COMMON_KNOWLEDGE', (siSpellDesc, spPlayerCivDesc))
			CyInterface().addMessage(eLoopPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCity.getX(), pCity.getY(), True, True)

def reqContractOut(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	bContract = bool(pPlayer.getGuildPlusCounter(50))
	if not bContract:
		return False
	pPlayerTeam = gc.getTeam(pCaster.getTeam())
	if pPlayerTeam.isAVassal():
		return False
	iTurn = CyGame().getGameTurnYear()
	iStartTurn = pPlayer.getGuildPlusCounter(51)
	if iStartTurn + 10 > iTurn:
		return False

	if not pPlayer.isHuman():
		iRatio = cf.AI_getWarSuccessCapitulationRatio(ePlayer)
		if iRatio > -30:
			return False

	iNum = pPlayer.getGuildPlusCounter(59)
	for iIndex in xrange(iNum):
		eEnemy = pPlayer.getGuildPlusCounter(60 + iIndex)
		if eEnemy != -1:
			pEnemy = gc.getPlayer(eEnemy)
			if pEnemy.isAlive():
				eEnemyTeam = pEnemy.getTeam()
				pEnemyTeam = gc.getTeam(eEnemyTeam)
				if not pEnemyTeam.isAVassal():
					return True

	return False

def spellContractOut(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	iKill = pPlayer.getGuildPlusCounter(53)
	iRequire = pPlayer.getGuildPlusCounter(55)
	if iRequire < iKill * 2:#最低限の仕事をしたかどうか判定
		sText = 'TXT_KEY_CONTRACT_OUT'
	else:
		sText = 'TXT_KEY_CONTRACT_OUT2'

	if pPlayer.isHuman():
		popupInfo = CyPopupInfo()
		popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
		popupInfo.setText(CyTranslator().getText(sText,()))
		popupInfo.setData1(ePlayer)
		popupInfo.setPythonModule("CvSpellInterface")
		popupInfo.setOnClickedPythonCallback("selectContractOut")
		popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_POPUP_YES", ()), "")
		popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_POPUP_NO", ()), "")
		popupInfo.addPopup(ePlayer)
	else:
		applyContractOut(ePlayer)
 
def selectContractOut(argsList):
	iButton = argsList[0]
	ePlayer = argsList[1]

	if iButton == 0:
		applyContractOut(ePlayer)

def applyContractOut(ePlayer):
	pPlayer = gc.getPlayer(ePlayer)
	ePlayerTeam = pPlayer.getTeam()
	pPlayerTeam = gc.getTeam(ePlayerTeam)

	iNum = pPlayer.getGuildPlusCounter(59)
	for iIndex in xrange(iNum):
		eEnemy = pPlayer.getGuildPlusCounter(60 + iIndex)
		if eEnemy != -1:
			pEnemy = gc.getPlayer(eEnemy)
			if pEnemy.isAlive():
				eEnemyTeam = pEnemy.getTeam()
				pEnemyTeam = gc.getTeam(eEnemyTeam)
				if not pEnemyTeam.isAVassal() and pPlayerTeam.isAtWar(eEnemyTeam):
					pPlayerTeam.makePeace(eEnemyTeam)

	iKill = pPlayer.getGuildPlusCounter(53)
	iRequire = pPlayer.getGuildPlusCounter(55)
	if iRequire < iKill * 2:#最低限の仕事をしたかどうか判定
		cf.RewardContract(ePlayer, 1, 'TXT_KEY_CONTRACT_OUT_APPROVE')
	else:
		cf.addPlayerPopup(CyTranslator().getText('TXT_KEY_CONTRACT_BREACH_4',()), ePlayer)
	cf.InitializeContract(pPlayer)

# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
def effectMercenariesCommander(argsList):
	pCaster = argsList[0]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	iTeam = pPlayer.getTeam()
	eTeam = gc.getTeam(iTeam)
	pPlot = pCaster.plot()
	if not pPlot.isNone():
		for iUnit in xrange(pPlot.getNumUnits()):
			pUnit = pPlot.getUnit(iUnit)
			if not eTeam.isAtWar(pUnit.getTeam()):
				pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MORALE'), True)
"""
# Kaijin <<< End

def spellMercenariesRecruit(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	pPlayer = gc.getPlayer(pCaster.getOwner())
	iLoop = (pCity.getPopulation() / 3) + 4

	pCivilization = gc.getCivilizationInfo(pPlayer.getCivilizationType())
	iUnitClass = gc.getInfoTypeForString('UNITCLASS_MERCENARY')
	iUnit = pCivilization.getCivilizationUnits(iUnitClass)
	if iUnit != UnitTypes.NO_UNIT:
		for i in xrange(iLoop):
			pNewUnit = pPlayer.initUnit(iUnit, pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
			pNewUnit.changeImmobileTimer(1)
#	pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MERCENARIES_RECRUITER'), False)

def reqRecruitMercenaryFuneral(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.isHuman():
		if pPlayer.hasTrait(en.eTraitRiches):
			if pPlot.isCity():
				pCity = pPlot.getPlotCity()
				if not (pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED')) or pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED_1')) or pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED_2'))):
					return ReasonTypes.REASON_DISABLED_KHAZAD_HATES_MERCENARY
	"""
		pTeam = gc.getTeam(pCaster.getTeam())
		lpRangedUnits = cyGetRangedUnits(pPlot, 1, False, True, pCaster.getTeam())
		for pUnit in lpRangedUnits:
			if pTeam.isAtWar(pUnit.getTeam()):
				return True
		return False
	"""
	return True

"""
def spellRecruitMercenaryFuneral(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCivilization = gc.getCivilizationInfo(pPlayer.getCivilizationType())
	iUnitClass = gc.getInfoTypeForString('UNITCLASS_FUNERAL_MERCENARY')
	iUnit = pCivilization.getCivilizationUnits(iUnitClass)
	for i in xrange(4):
		pNewUnit = pPlayer.initUnit(iUnit, pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
		pNewUnit.changeImmobileTimer(1)
"""

def reqMercenariesBribe(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)

	#契約戦争中か
	bContracted = bool(pPlayer.getGuildPlusCounter(50))
	if not bContracted:
		return False

	eContractor = pPlayer.getGuildPlusCounter(52)
	pContractor = gc.getPlayer(eContractor)
	eContractorTeam = pContractor.getTeam()
	pContractorTeam = gc.getTeam(eContractorTeam)

	for eDirection in xrange(DirectionTypes.NUM_DIRECTION_TYPES):
		pAdjacentPlot = plotDirection(pPlot.getX(), pPlot.getY(), DirectionTypes(eDirection))
		if not pAdjacentPlot.isNone():
			pCity = pAdjacentPlot.getPlotCity()
			if not pCity.isNone():
				iNum = pPlayer.getGuildPlusCounter(59)
				for iIndex in xrange(iNum):
					eEnemy = pPlayer.getGuildPlusCounter(60 + iIndex)
					if eEnemy != -1:
						pEnemy = gc.getPlayer(eEnemy)
						if pEnemy.isAlive() and eEnemy == pCity.getOwner():
							eEnemyTeam = pEnemy.getTeam()
							pEnemyTeam = gc.getTeam(eEnemyTeam)
							if not pEnemyTeam.isAVassal() and pContractorTeam.isAtWar(eEnemyTeam):
								#AI: 基本はCvUnitAIInterfaceで制御するが、制御前にスタックに組み込まれた場合の対策
								if not pCaster.isHuman():
									iRatio = cf.AI_getWarSuccessCapitulationRatio(eContractor)
									iCityNum = pContractor.getNumCities()
									if iRatio < -50 or iCityNum < 2:
										return True
									#戦況が著しく悪化している場合は緊急発動
									iRatio = cf.AI_getWarSuccessCapitulationRatio(ePlayer)
									if iRatio < -50:
										return True
								else:
									return True

	return False

def spellMercenariesBribe(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	pPlot = pCaster.plot()

	eTarget = -1
	for eDirection in xrange(DirectionTypes.NUM_DIRECTION_TYPES):
		pAdjacentPlot = plotDirection(pPlot.getX(), pPlot.getY(), DirectionTypes(eDirection))
		if not pAdjacentPlot.isNone():
			pCity = pAdjacentPlot.getPlotCity()
			if not pCity.isNone():
				eTarget = pCity.getOwner()
				break

	if eTarget != -1:
		pTarget = gc.getPlayer(eTarget)
		eTargetTeam = pTarget.getTeam()
		eContractor = pPlayer.getGuildPlusCounter(52)
		pContractor = gc.getPlayer(eContractor)
		eContractorTeam = pContractor.getTeam()
		pContractorTeam = gc.getTeam(eContractorTeam)

		if pContractorTeam.isAtWar(eTargetTeam):
			pContractorTeam.makePeace(eTargetTeam)

		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_MERCENARIES_BRIBE', (pCaster.getNameKey(), pContractor.getCivilizationAdjectiveKey(), pTarget.getCivilizationAdjectiveKey()))
		szButton = gc.getSpellInfo(eSpell).getButton()
		CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_BUILD_BANK', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCaster.getX(), pCaster.getY(), True, True)
		pContractor.AI_changeAttitudeExtra(ePlayer, 2)

def reqMercenariesIncitement(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	pCity = pPlot.getPlotCity()
	eTarget = pCity.getOwner()
	pTarget = gc.getPlayer(eTarget)

	if pTarget.isBarbarian():
		return False
	#契約戦争中か
	bContracted = bool(pPlayer.getGuildPlusCounter(50))
	if not bContracted:
		return False

	ePlayerTeam = pPlayer.getTeam()
	eTargetTeam = pTarget.getTeam()
	pTargetTeam = gc.getTeam(eTargetTeam)
	eContractor = pPlayer.getGuildPlusCounter(52)
	pContractor = gc.getPlayer(eContractor)
	eContractorTeam = pContractor.getTeam()

	if eTargetTeam in (ePlayerTeam, eContractorTeam):
		return ReasonTypes.REASON_DISABLED_IMMUNE_FRIENDLY_CITY
	if pTargetTeam.isAtWar(eContractorTeam):
		return False
	if pTargetTeam.isAVassal():
		return False

	#都市保有文明のプレイヤーは、契約対象プレイヤーに宣戦できるか
	if not pTargetTeam.canDeclareWar(eContractorTeam):
		return ReasonTypes.REASON_DISABLED_FORCE_PEACE

	return True

def spellMercenariesIncitement(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	eTarget = pCity.getOwner()
	pTarget = gc.getPlayer(eTarget)
	eTargetTeam = pTarget.getTeam()
	pTargetTeam = gc.getTeam(eTargetTeam)
	eContractor = pPlayer.getGuildPlusCounter(52)
	pContractor = gc.getPlayer(eContractor)
	eContractorTeam = pContractor.getTeam()

	if not pTargetTeam.isAtWar(eContractorTeam):
		pTargetTeam.declareWar(eContractorTeam, True, WarPlanTypes.WARPLAN_LIMITED)
		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_MERCENARIES_INCITEMENT', (pCaster.getNameKey(), pContractor.getCivilizationAdjectiveKey(), pTarget.getCivilizationAdjectiveKey()))
		szButton = gc.getSpellInfo(eSpell).getButton()
		CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_BUILD_BANK', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCaster.getX(), pCaster.getY(), True, True)
		pContractor.AI_changeAttitudeExtra(ePlayer, -6)

def reqYell(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	eYell5 = gc.getInfoTypeForString('PROMOTION_YELL5')
	for i in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(i)
		if (pUnit.isAlive() and pUnit.canFight() and pUnit.getOwner() == ePlayer):
			if not pUnit.isHasPromotion(eYell5):
				return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellYell(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	leYell = [	gc.getInfoTypeForString('PROMOTION_YELL1'),
				gc.getInfoTypeForString('PROMOTION_YELL2'),
				gc.getInfoTypeForString('PROMOTION_YELL3'),
				gc.getInfoTypeForString('PROMOTION_YELL4'),
				gc.getInfoTypeForString('PROMOTION_YELL5')	]

	ePlayer = pCaster.getOwner()
	pPlot = pCaster.plot()
	for iUnitIndex in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(iUnitIndex)
		if (pUnit.isAlive() and pUnit.canFight() and pUnit.getOwner() == ePlayer):
			for iRank in xrange(len(leYell)):
				eYell = leYell[iRank]
				if not pUnit.isHasPromotion(eYell):
					pUnit.setHasPromotion(eYell, True)
					break

# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
def effectYell(argsList):
	pCaster = argsList[0]

	if pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL5')) and CyGame().getSorenRandNum(100, "Yell") < 50:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL5'), False)
	elif pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL4')) and CyGame().getSorenRandNum(100, "Yell") < 40:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL4'), False)
	elif pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL3')) and CyGame().getSorenRandNum(100, "Yell") < 30:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL3'), False)
	elif pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL2')) and CyGame().getSorenRandNum(100, "Yell") < 20:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL2'), False)
	elif pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL1')) and CyGame().getSorenRandNum(100, "Yell") < 10:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL1'), False)
"""
# Kaijin <<< End

def reqRecruitMercenaryTiger(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	eSummonedUnit = gc.getSpellInfo(eSpell).getCreateUnitType()
	eUnitClass = gc.getUnitInfo(eSummonedUnit).getUnitClassType()

	if pPlayer.isProductionMaxedUnitClass(eUnitClass):
		return ReasonTypes.REASON_DISABLED_CLASSCOUNT_LIMIT_SUMMON
	if not pPlayer.isHuman():

		if pPlayer.hasTrait(en.eTraitRiches):
			if pPlot.isCity():
				pCity = pPlot.getPlotCity()
				if not (pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED')) or pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED_1')) or pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED_2'))):
					return ReasonTypes.REASON_DISABLED_KHAZAD_HATES_MERCENARY
		"""
		pTeam = gc.getTeam(pCaster.getTeam())
		lpRangedUnits = cyGetRangedUnits(pPlot, 1, False, True, pCaster.getTeam())
		for pUnit in lpRangedUnits:
			if pTeam.isAtWar(pUnit.getTeam()):
				return True
		return False
		"""
	return True

def disabledRecruitMercenaryTiger(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())

	if not pPlayer.isHuman():
		if pPlayer.hasTrait(en.eTraitRiches):
			if pPlot.isCity():
				pCity = pPlot.getPlotCity()
				if not (pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED')) or pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED_1')) or pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED_2'))):
					return ReasonTypes.REASON_DISABLED_KHAZAD_HATES_MERCENARY

def spellRecruitMercenaryTiger(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]
	liSummonedUnitIDs = argsList[3]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	eSummonedUnit = gc.getSpellInfo(eSpell).getCreateUnitType()
	eUnitClass = gc.getUnitInfo(eSummonedUnit).getUnitClassType()
	pCity = pCaster.plot().getPlotCity()
	pCivilization = gc.getCivilizationInfo(pCity.getCivilizationType())
	eUnit = pCivilization.getCivilizationUnits(eUnitClass)
	eCasterType = pCaster.getUnitType()
	eMagnadine = gc.getInfoTypeForString('UNIT_MAGNADINE')

	for iSummonedUnitID in liSummonedUnitIDs:
		pUnit = pPlayer.getUnit(iSummonedUnitID)
		if not eUnit in (UnitTypes.NO_UNIT, eSummonedUnit):
			pNewUnit = pPlayer.initUnit(eUnit, pUnit.getX(), pUnit.getY(), pUnit.getUnitAIType(), pUnit.getFacingDirection())
			pNewUnit.convert(pUnit)
		else:
			pNewUnit = pUnit
		if eCasterType == eMagnadine:
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LOYALTY'), True)

	if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_TAVERN')):
		pPlayer.changeGold( cyFlatValue(20, g_dGameSpeedPercent["VictoryDelay"], False))

#Tiger End

#Xoth Start
"""
def reqCallofOverlords(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	return True
"""

def spellCallofOverlords(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	lszSounds = ['AS3D_SPELL_KRAKEN', 'AS3D_SPELL_HYBOREMS_WHISPER', 'AS3D_SPELL_DEFILE']
	szButton = gc.getSpellInfo(eSpell).getButton()
	sDescription = gc.getSpellInfo(eSpell).getDescription()
	eKraken = gc.getInfoTypeForString('UNIT_KRAKEN')
	eDrown = gc.getInfoTypeForString('UNIT_DROWN')

	iPlayer = pCaster.getOwner()
	for eLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
		pPlayer = gc.getPlayer(eLoopPlayer)
		py = PyPlayer(eLoopPlayer)
		if pPlayer.isAlive():
			for pyCity in py.getCityList():
				pCity = pyCity.GetCy()
				if pCity.isHasReligion(en.eReligionOctopusOverlords):
					pCity.changeWeLoveTheKingDayProbability(90)
					szSound = lszSounds[CyGame().getSorenRandNum(len(lszSounds), 'Call of Overlords')]
					szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_CALL_OF_OVERLORDS', (sDescription, pCity.getNameKey()))
					CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
				if (pCity.plot()).isCoastalLand():
					if eLoopPlayer == iPlayer:
						pNewUnit = pPlayer.initUnit(eKraken, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

		for pUnit in py.getUnitList():
			if pUnit.isAlive():
				if not isWorldUnitClass(pUnit.getUnitClassType()):
					if pUnit.getReligion() == en.eReligionOctopusOverlords:
						pUnit.setHasPromotion(en.ePromotionEnraged, True)
						if CyGame().getSorenRandNum(100, "Deep one") < 10:
							pNewUnit = pPlayer.initUnit(eDrown, pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
							pNewUnit.convert(pUnit)
					else:
						if CyGame().getSorenRandNum(100, "Sanity") < 25:
							pUnit.setHasPromotion(en.ePromotionEnraged, True)

	pPlayer = gc.getPlayer(iPlayer)
	if pPlayer.getGuildPlusCounter(50) < 30:
		pPlayer.setGuildPlusCounter(50, 0)
	else:
		pPlayer.changeGuildPlusCounter(50, -30)

def disabledDistorting(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) == 0:
			return True
		if not pTeam.isAtWar(pPlot.getOwner()):
			return True
		if not pPlayer.getGuildPlusCounter(50) < 60:
			return True
		if not pPlayer.getGuildPlusCounter(50) >= 20:
			return True
	return False

def spellDistorting(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pPlayer.changeGuildPlusCounter(50, 1)
	if pPlayer.getGuildPlusCounter(50) > 70:
		pPlayer.setGuildPlusCounter(50, 70)
	szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_XOTH_SANITY_POINT_INCREASE', ('1', ))
	szButton = gc.getCivilizationInfo(en.eCivilizationXoth).getButton()
	CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCaster.getX(), pCaster.getY(), True, True)

def disabledEnergyDrain(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.getGuildPlusCounter(50) < 40:
		return True
	if not pPlayer.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		if pCaster.getDamage < 50:
			return True
		if pTeam.getAtWarCount(True) == 0:
			return True
		if CyGame().getSorenRandNum(100, "Sanity") > (pPlayer.getGuildPlusCounter(50) / 2):
			return True
	return False

def spellEnergyDrain(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pCaster.changeDamage(-50, PlayerTypes.NO_PLAYER)
	pCaster.changeExperience(CyGame().getSorenRandNum(11, "Experience"), -1, False, False, False)

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pPlayer.changeGuildPlusCounter(50, 3)
	if pPlayer.getGuildPlusCounter(50) > 70:
		pPlayer.setGuildPlusCounter(50, 70)
	szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_XOTH_SANITY_POINT_INCREASE', ('3', ))
	szButton = gc.getCivilizationInfo(en.eCivilizationXoth).getButton()
	CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCaster.getX(), pCaster.getY(), True, True)

def disabledCrazyEyes(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.getGuildPlusCounter(50) < 20:
		return True
	if not pPlayer.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) == 0:
			return True
		if CyGame().getSorenRandNum(100, "Sanity") > (pPlayer.getGuildPlusCounter(50) / 2):
			return True
# ent >>>
		lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
		lpTargetUnits = [pUnit for pUnit in lpRangedUnits if pUnit.canFight()]
		if len(lpTargetUnits) < 10:
			return True
# ent <<<
	return False

def spellCrazyEyes(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pPlayer.changeGuildPlusCounter(50, 5)
	if pPlayer.getGuildPlusCounter(50) > 70:
		pPlayer.setGuildPlusCounter(50, 70)
	szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_XOTH_SANITY_POINT_INCREASE', ('5', ))
	szButton = gc.getCivilizationInfo(en.eCivilizationXoth).getButton()
	CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCaster.getX(), pCaster.getY(), True, True)

def reqCityEmerge(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)

	if CyGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and pPlayer.isHuman():
		return False
	if not pPlayer.getGuildPlusCounter(50) < 60:
		return False
	if pPlayer.getGuildPlusCounter(52) == 0:
		return False

	if not pPlayer.isHuman():
		liCanFoundCityNum = [3, 5, 7, 10, 13, 16]
		iCanFoundCityNum = liCanFoundCityNum[CyMap().getWorldSize()]
		if pPlayer.getNumCities() > iCanFoundCityNum:
			return False

	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, True)
	for pTargetPlot in lpRangedPlots:
		if not pTargetPlot.isWater():
			continue
		if pTargetPlot.isLake():
			continue
		if pTargetPlot.isOwned():
			if pTargetPlot.getOwner() != ePlayer:
				continue
		if pTargetPlot.getNumUnits() > 0:
			continue
		if pTargetPlot.isImpassable():
			continue
		if pTargetPlot.getImprovementType() != ImprovementTypes.NO_IMPROVEMENT:
			continue
		if pTargetPlot.getBonusType(TeamTypes.NO_TEAM) != BonusTypes.NO_BONUS:
			continue
		bCannotConstruct = False
		lpAroundTargetPlots = cyGetRangedPlots(pTargetPlot, 2, True, False, TeamTypes.NO_TEAM)
		for pAroundTargetPlot in lpAroundTargetPlots:
			if pAroundTargetPlot.isCity():
				bCannotConstruct = True
				break
		if bCannotConstruct:
			continue
		return True

	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellCityEmerge(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)

	iBestValue = 0
	pBestPlot = -1
	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	lpRangedPlots = cyGetSpellRangedPlots(pCaster, eSpell, pPlot, False, True)
	for pTargetPlot in lpRangedPlots:
		# 都市建設可能か否か
		if not pTargetPlot.isWater():
			continue
		if pTargetPlot.isLake():
			continue
		if pTargetPlot.isOwned():
			if pTargetPlot.getOwner() != ePlayer:
				continue
		if pTargetPlot.getNumUnits() > 0:
			continue
		if pTargetPlot.isImpassable():
			continue
		if pTargetPlot.getImprovementType() != ImprovementTypes.NO_IMPROVEMENT:
			continue
		if pTargetPlot.getBonusType(TeamTypes.NO_TEAM) != BonusTypes.NO_BONUS:
			continue
		bCannotConstruct = False
		lpAroundTargetPlots = cyGetRangedPlots(pTargetPlot, 2, True, False, TeamTypes.NO_TEAM)
		for pAroundTargetPlot in lpAroundTargetPlots:
			if pAroundTargetPlot.isCity():
				bCannotConstruct = True
				break
		if bCannotConstruct:
			continue
		# 乱数を用いて都市建設タイルを決定
		iPlotDistance = plotDistance(pPlot.getX(), pPlot.getY(), pTargetPlot.getX(), pTargetPlot.getY())
		if iPlotDistance > 4:
			if pCity.isCapital():
				iValue = 2000 + CyGame().getSorenRandNum(1000, "City Emerge")
			else:
				iValue = 1000 + CyGame().getSorenRandNum(500, "City Emerge")
		else:
			iValue = 500 + CyGame().getSorenRandNum(250, "City Emerge")
		if pTargetPlot.getTerrainType() == en.eTerrainOcean:
			iValue += 500
		if pTargetPlot.getLatitude() < 30:
			iValue += 1500
		elif pTargetPlot.getLatitude() < 60:
			iValue += 1000
		for pAroundTargetPlot in lpAroundTargetPlots:
			if pAroundTargetPlot.isWater():
				iValue += 60
			if pAroundTargetPlot.isOwned():
				if pAroundTargetPlot.getOwner() == ePlayer:
					iValue += 30
			else:
				iValue += 60
			if pAroundTargetPlot.getBonusType(TeamTypes.NO_TEAM) != BonusTypes.NO_BONUS:
				iValue += 30
		if iBestValue < iValue:
			iBestValue = iValue
			pBestPlot = pTargetPlot

	if pBestPlot != -1:
		iX = pBestPlot.getX()
		iY = pBestPlot.getY()

		pBestPlot.setPlotType(PlotTypes.PLOT_LAND, True, True)
		pBestPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
		pBestPlot.clearColdCounter()
		pBestPlot.setTerrainType(en.eTerrainPlains, True, True)

		# 都市近傍の陸地数を調整
		iWaterCount = 0
		lpAdjacentPlots = cyGetRangedPlots(pBestPlot, 1, True, False, TeamTypes.NO_TEAM)
		for pAdjacentPlot in lpAdjacentPlots:
			if pAdjacentPlot.at(iX, iY):
				continue
			if pAdjacentPlot.isWater():
				iWaterCount += 1
		if iWaterCount >= 4:
			for pAdjacentPlot in lpAdjacentPlots:
				if pAdjacentPlot.at(iX, iY):
					continue
				if pAdjacentPlot.isOwned():
					if pAdjacentPlot.getOwner() != ePlayer:
						continue
				if pAdjacentPlot.getNumUnits() > 0:
					continue
				if pAdjacentPlot.getImprovementType() != ImprovementTypes.NO_IMPROVEMENT:
					continue
				if pAdjacentPlot.getBonusType(TeamTypes.NO_TEAM) != BonusTypes.NO_BONUS:
					continue
				if CyGame().getSorenRandNum(1000, "NotWaterPlot") < 500:
					if pAdjacentPlot.isWater():
						pAdjacentPlot.setPlotType(PlotTypes.PLOT_LAND, True, True)
						pAdjacentPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
						pAdjacentPlot.clearColdCounter()
						pAdjacentPlot.setTerrainType(en.eTerrainTundra, True, True)
		else:
			for pAdjacentPlot in lpAdjacentPlots:
				if pAdjacentPlot.at(iX, iY):
					continue
				if pAdjacentPlot.isOwned():
					if pAdjacentPlot.getOwner() != ePlayer:
						continue
				if pAdjacentPlot.getNumUnits() > 0:
					continue
				if pAdjacentPlot.getImprovementType() != ImprovementTypes.NO_IMPROVEMENT:
					continue
				if pAdjacentPlot.getBonusType(TeamTypes.NO_TEAM) != BonusTypes.NO_BONUS:
					continue
				if CyGame().getSorenRandNum(1000, "WaterPlot") < 500:
					if not pAdjacentPlot.isWater():
						pAdjacentPlot.setPlotType(PlotTypes.PLOT_OCEAN, True, True)
						pAdjacentPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
						pAdjacentPlot.clearColdCounter()
		if not pBestPlot.isCoastalLand():
			for iter in xrange(10):
				iDirection = CyGame().getSorenRandNum(DirectionTypes.NUM_DIRECTION_TYPES, "CoastalLand")
				pPassPlot = plotDirection(iX, iY, DirectionTypes(iDirection))
				if not pPassPlot.isNone():
					pPassPlot.setPlotType(PlotTypes.PLOT_OCEAN, True, True)
					pPassPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
					pPassPlot.clearColdCounter()
					break

		# 都市周辺を肥沃化
		eEffect = gc.getInfoTypeForString('EFFECT_SPRING')
		lszWaterBonus = [	'BONUS_CLAM', 'BONUS_CRAB', 'BONUS_FISH', 'BONUS_PEARL', 'BONUS_SHRIMP', 'BONUS_JADE', 'BONUS_WHALE'	]
		lpWorkingPlots = cyGetRangedPlots(pBestPlot, 2, False, False, TeamTypes.NO_TEAM)
		for pWorkingPlot in lpWorkingPlots:
			if pWorkingPlot.at(iX, iY):
				continue
			if pWorkingPlot.isVisibleToWatchingHuman():
				CyEngine().triggerEffect(eEffect, pWorkingPlot.getPoint())
			if pWorkingPlot.isWater():
				if pWorkingPlot.getImprovementType() != ImprovementTypes.NO_IMPROVEMENT:
					continue
				if pWorkingPlot.getFeatureType() == en.eFeatureIce:
					pWorkingPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
				if CyGame().getSorenRandNum(1000, "Generate Kelp") < 333:
					pWorkingPlot.setFeatureType(en.eFeatureKelp, 0)
				if pWorkingPlot.getBonusType(TeamTypes.NO_TEAM) == BonusTypes.NO_BONUS:
					if CyGame().getSorenRandNum(1000, "Generate Bonus") < 200:
						szNewBonus = lszWaterBonus[CyGame().getSorenRandNum(len(lszWaterBonus), "Bonuses Select")]
						if szNewBonus == 'BONUS_WHALE' and pWorkingPlot.getTerrainType() == en.eTerrainCoast:
							szNewBonus = 'BONUS_PEARL'
						pWorkingPlot.setBonusType(gc.getInfoTypeForString(szNewBonus))

		# 都市建設
		pCity = pPlayer.initCity(iX, iY)
		pCity.setPopulation(3)
		iCulture = gc.getCultureLevelInfo(gc.getInfoTypeForString('CULTURELEVEL_FLEDGLING')).getSpeedThreshold(CyGame().getGameSpeedType())
		pCity.setCulture(ePlayer, iCulture, True)
		pCity.setHasReligion(en.eReligionOctopusOverlords, True, True, True)
		pNewUnit1 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_SHOGGOTH'), iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit1.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MOBILITY1'), True)
		pNewUnit2 = pPlayer.initUnit(en.eUnitWorker, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit3 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_GREATRACE'), iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit4 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ITHAQUA'), iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

		pPlayer.changeGuildPlusCounter(50, 5)
		if pPlayer.getGuildPlusCounter(50) > 70:
			pPlayer.setGuildPlusCounter(50, 70)
		pPlayer.changeGuildPlusCounter(52, -1)
		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_XOTH_SANITY_POINT_INCREASE', ('5', ))
		szButton = gc.getCivilizationInfo(en.eCivilizationXoth).getButton()
		CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCaster.getX(), pCaster.getY(), True, True)

def reqBodysnatch(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	if not pPlayer.getGuildPlusCounter(50) < 60:
		return False

	if pCaster.isAlwaysHostile(pPlot):
		return ReasonTypes.REASON_DISABLED_NATIONALITY_IS_HIDDEN

	iResistMax = 95
	if not pPlayer.isHuman():
		iResistMax = 20

	iTeam = pPlayer.getTeam()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	for pUnit in lpRangedUnits:
		if pUnit.isEnemy(iTeam, pUnit.plot()):
			if not isWorldUnitClass(pUnit.getUnitClassType()):
				iResist = pUnit.getResistChance(pCaster, eSpell)
				if iResist <= iResistMax:
					return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellBodysnatch(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pPlayer.changeGuildPlusCounter(50, 3)
	if pPlayer.getGuildPlusCounter(50) > 70:
		pPlayer.setGuildPlusCounter(50, 70)
	szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_XOTH_SANITY_POINT_INCREASE', ('3', ))
	szButton = gc.getCivilizationInfo(gc.getInfoTypeForString('CIVILIZATION_XOTH')).getButton()
	CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCaster.getX(), pCaster.getY(), True, True)

	iResistMax = 95
	if not pPlayer.isHuman():
		iResistMax = 20

	eTeam = pCaster.getTeam()
	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)

	iBestValue = 0
	pBestUnit = -1
	for pUnit in lpRangedUnits:
		if pUnit.isEnemy(eTeam, pUnit.plot()):
			if not isWorldUnitClass(pUnit.getUnitClassType()):
				iResist = pUnit.getResistChance(pCaster, eSpell)
				if iResist <= iResistMax:
					iValue = (pUnit.getCombatAttackTimes100() + pUnit.getCombatDefenseTimes100()) // 20 + pUnit.getExperience()
					iValue += (100 - iResist)
					if iValue > iBestValue:
						iBestValue = iValue
						pBestUnit = pUnit
	if pBestUnit != -1:
		szButton = gc.getSpellInfo(eSpell).getButton()
		bValid = False
		if not pBestUnit.isResisted(pCaster, eSpell):
			bValid = True
		if CyGame().getSorenRandNum(100, "Resistable") <= (70 - pPlayer.getGuildPlusCounter(50)):
			bValid = True
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_IMMUNE_RESISTANCE', (pBestUnit.getNameKey(), pPlayer.getCivilizationAdjectiveKey(), pCaster.getNameKey()))
			CyInterface().addMessage(pBestUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pBestUnit.getX(), pBestUnit.getY(), True, True)
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_IMMUNE_RESISTANCE_ENEMY', (pCaster.getNameKey(), gc.getPlayer(pBestUnit.getOwner()).getCivilizationAdjectiveKey(), pBestUnit.getNameKey()))
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
		if bValid:
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_BODYSNATCH', (pBestUnit.getNameKey(), pPlayer.getCivilizationAdjectiveKey(), pCaster.getNameKey()))
			CyInterface().addMessage(pBestUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pBestUnit.getX(), pBestUnit.getY(), True, True)
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_BODYSNATCH_ENEMY', (pCaster.getNameKey(), gc.getPlayer(pBestUnit.getOwner()).getCivilizationAdjectiveKey(), pBestUnit.getNameKey()))
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)

			for eProm in xrange(gc.getNumPromotionInfos()):
				if not pCaster.isHasPromotion(eProm):
					if pBestUnit.isHasPromotion(eProm):
						if not gc.getPromotionInfo(eProm).isEquipment():
							if not eProm in (en.lePromotionWeapons, en.ePromotionGreatCommander):
								if not gc.getPromotionInfo(eProm).isRace():
									pCaster.setHasPromotion(eProm, True)

			pNewUnit = pPlayer.initUnit(pBestUnit.getUnitType(), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit.convert(pCaster)
			pNewUnit.changeImmobileTimer(1)
			pBestUnit.kill(False, PlayerTypes.NO_PLAYER)
			pBestUnit.setAfterlife(AfterlifeTypes.AFTERLIFE_PREYED)
		else:
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_BODYSNATCH_FAILED', (pCaster.getNameKey(), gc.getSpellInfo(eSpell).getDescription()))
			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			pCaster.kill(True, PlayerTypes.NO_PLAYER)

#Xoth End
#Baldralfar Start
def reqWindunsayable(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getNumCities() == 0:
		return ReasonTypes.REASON_DISABLED_REQUIRES_CITY
	if not pPlayer.isHuman():
# ent >>>
		iRatio = cf.AI_getWarSuccessCapitulationRatio(pCaster.getOwner())
		if iRatio < -50 and iRatio > -99:
			return True
# ent <<<
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) < 2:
			return False
	return True

def spellWindunsayable(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	liVariantProm = [	gc.getInfoTypeForString('PROMOTION_AMPHIBIOUS'),
			gc.getInfoTypeForString('PROMOTION_COLD_RESISTANCE'),
			gc.getInfoTypeForString('PROMOTION_COMMAND1'),
			gc.getInfoTypeForString('PROMOTION_CRAZED'),
			gc.getInfoTypeForString('PROMOTION_DRILL1'),
			gc.getInfoTypeForString('PROMOTION_FEAR'),
			gc.getInfoTypeForString('PROMOTION_FIRE_RESISTANCE'),
			gc.getInfoTypeForString('PROMOTION_FLYING'),
			gc.getInfoTypeForString('PROMOTION_HEAVY'),
			gc.getInfoTypeForString('PROMOTION_LIGHT'),
			gc.getInfoTypeForString('PROMOTION_LIGHTNING_RESISTANCE'),
			gc.getInfoTypeForString('PROMOTION_MAGIC_IMMUNE'),
			gc.getInfoTypeForString('PROMOTION_MEDIC1'),
			gc.getInfoTypeForString('PROMOTION_MUTATED'),
			gc.getInfoTypeForString('PROMOTION_NOMAD'),
			gc.getInfoTypeForString('PROMOTION_PERFECT_SIGHT'),
			gc.getInfoTypeForString('PROMOTION_POISON_RESISTANCE'),
			gc.getInfoTypeForString('PROMOTION_PROPHECY_MARK'),
			gc.getInfoTypeForString('PROMOTION_SPIRIT_GUIDE'),
			gc.getInfoTypeForString('PROMOTION_STIGMATA'),
			gc.getInfoTypeForString('PROMOTION_STONESKIN'),
			gc.getInfoTypeForString('PROMOTION_UNHOLY_TAINT'),
			gc.getInfoTypeForString('PROMOTION_VILE_TOUCH'),
			gc.getInfoTypeForString('PROMOTION_VULNERABLE_TO_FIRE'),
			gc.getInfoTypeForString('PROMOTION_WINTERBORN'),
			gc.getInfoTypeForString('PROMOTION_DARK_MAGIC1'),
			gc.getInfoTypeForString('PROMOTION_STRANGER'),
			gc.getInfoTypeForString('PROMOTION_MARK_OF_THE_WARDEN'),
			gc.getInfoTypeForString('PROMOTION_ADVENTURER')	]
	eVariant = gc.getInfoTypeForString('PROMOTION_VARIANT')

	for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
		pLoopPlayer = gc.getPlayer(iLoopPlayer)
		if pLoopPlayer.isAlive():
			liPromotions = []
			eStateReligion = pLoopPlayer.getStateReligion()
			if eStateReligion != ReligionTypes.NO_RELIGION and gc.getReligionInfo(eStateReligion).getAlignment() == en.eAlignmentEvil:
				liPromotions += [	gc.getInfoTypeForString('PROMOTION_DISEASED'),
							gc.getInfoTypeForString('PROMOTION_FEAR'),
							gc.getInfoTypeForString('PROMOTION_FIRE_RESISTANCE'),
							gc.getInfoTypeForString('PROMOTION_FLYING'),
							gc.getInfoTypeForString('PROMOTION_LIGHT'),
							gc.getInfoTypeForString('PROMOTION_MAGIC_IMMUNE'),
							gc.getInfoTypeForString('PROMOTION_MUTATED'),
							gc.getInfoTypeForString('PROMOTION_POISON_RESISTANCE'),
							gc.getInfoTypeForString('PROMOTION_PLAGUED'),
							gc.getInfoTypeForString('PROMOTION_PROPHECY_MARK'),
							gc.getInfoTypeForString('PROMOTION_STIGMATA'),
							gc.getInfoTypeForString('PROMOTION_STONESKIN'),
							gc.getInfoTypeForString('PROMOTION_UNHOLY_TAINT'),
							gc.getInfoTypeForString('PROMOTION_VILE_TOUCH'),
							gc.getInfoTypeForString('PROMOTION_VULNERABLE_TO_FIRE'),
							gc.getInfoTypeForString('PROMOTION_WINTERBORN'),
							gc.getInfoTypeForString('PROMOTION_WITHERED'),
							gc.getInfoTypeForString('PROMOTION_DARK_MAGIC1'),
							gc.getInfoTypeForString('PROMOTION_STRANGER'),
							gc.getInfoTypeForString('PROMOTION_GRAVITATION'),
							gc.getInfoTypeForString('PROMOTION_HOOF'),
							gc.getInfoTypeForString('PROMOTION_FOUR_EYE'),
							gc.getInfoTypeForString('PROMOTION_SLAUGHTER_IMPULSER'),
							gc.getInfoTypeForString('PROMOTION_SHELL'),
							gc.getInfoTypeForString('PROMOTION_HAND_OF_THE_POISON')	]
			elif eStateReligion == en.eReligionFellowshipofLeaves:
				liPromotions += [	gc.getInfoTypeForString('PROMOTION_AMPHIBIOUS'),
							gc.getInfoTypeForString('PROMOTION_COLD_RESISTANCE'),
							gc.getInfoTypeForString('PROMOTION_COMMAND1'),
							gc.getInfoTypeForString('PROMOTION_DRILL1'),
							gc.getInfoTypeForString('PROMOTION_FEAR'),
							gc.getInfoTypeForString('PROMOTION_FIRE_RESISTANCE'),
							gc.getInfoTypeForString('PROMOTION_FLYING'),
							gc.getInfoTypeForString('PROMOTION_LIGHT'),
							gc.getInfoTypeForString('PROMOTION_LIGHTNING_RESISTANCE'),
							gc.getInfoTypeForString('PROMOTION_MAGIC_IMMUNE'),
							gc.getInfoTypeForString('PROMOTION_MEDIC1'),
							gc.getInfoTypeForString('PROMOTION_MUTATED'),
							gc.getInfoTypeForString('PROMOTION_NOMAD'),
							gc.getInfoTypeForString('PROMOTION_PERFECT_SIGHT'),
							gc.getInfoTypeForString('PROMOTION_POISON_RESISTANCE'),
							gc.getInfoTypeForString('PROMOTION_PROPHECY_MARK'),
							gc.getInfoTypeForString('PROMOTION_SPIRIT_GUIDE'),
							gc.getInfoTypeForString('PROMOTION_STIGMATA'),
							gc.getInfoTypeForString('PROMOTION_STONESKIN'),
							gc.getInfoTypeForString('PROMOTION_UNHOLY_TAINT'),
							gc.getInfoTypeForString('PROMOTION_VILE_TOUCH'),
							gc.getInfoTypeForString('PROMOTION_VULNERABLE_TO_FIRE'),
							gc.getInfoTypeForString('PROMOTION_WINTERBORN'),
							gc.getInfoTypeForString('PROMOTION_DARK_MAGIC1'),
							gc.getInfoTypeForString('PROMOTION_STRANGER'),
							gc.getInfoTypeForString('PROMOTION_MARK_OF_THE_WARDEN'),
							gc.getInfoTypeForString('PROMOTION_ADVENTURER'),
							gc.getInfoTypeForString('PROMOTION_GRAVITATION'),
							gc.getInfoTypeForString('PROMOTION_HOOF'),
							gc.getInfoTypeForString('PROMOTION_FOUR_EYE'),
							gc.getInfoTypeForString('PROMOTION_SLAUGHTER_IMPULSER'),
							gc.getInfoTypeForString('PROMOTION_SHELL'),
							gc.getInfoTypeForString('PROMOTION_HAND_OF_THE_POISON')	]
			else:
				liPromotions += [	gc.getInfoTypeForString('PROMOTION_DISEASED'),
							gc.getInfoTypeForString('PROMOTION_DRILL1'),
							gc.getInfoTypeForString('PROMOTION_LIGHT'),
							gc.getInfoTypeForString('PROMOTION_MUTATED'),
							gc.getInfoTypeForString('PROMOTION_POISON_RESISTANCE'),
							gc.getInfoTypeForString('PROMOTION_SPIRIT_GUIDE'),
							gc.getInfoTypeForString('PROMOTION_STONESKIN'),
							gc.getInfoTypeForString('PROMOTION_VULNERABLE_TO_FIRE'),
							gc.getInfoTypeForString('PROMOTION_STRANGER'),
							gc.getInfoTypeForString('PROMOTION_GRAVITATION'),
							gc.getInfoTypeForString('PROMOTION_HOOF'),
							gc.getInfoTypeForString('PROMOTION_FOUR_EYE'),
							gc.getInfoTypeForString('PROMOTION_SLAUGHTER_IMPULSER'),
							gc.getInfoTypeForString('PROMOTION_SHELL'),
							gc.getInfoTypeForString('PROMOTION_HAND_OF_THE_POISON')	]

			apUnitList = PyPlayer(iLoopPlayer).getUnitList()
			bBaldralfar = (pLoopPlayer.getCivilizationType() == en.eCivilizationBaldralfar)
			liVariantPromotions = liPromotions + liVariantProm
			for pUnit in apUnitList:
				if pUnit.isAlive():
					pUnit.doDamage(15, 100, en.eDamageDeath)
					if pUnit.isHasPromotion(eVariant):
						liSelectablePromotions = liVariantPromotions
					else:
						liSelectablePromotions = liPromotions
					if len(liSelectablePromotions) > 0:
						if CyGame().getSorenRandNum(100, "Winds of Miasma") < 20 or bBaldralfar:
							iCount = CyGame().getSorenRandNum(2, 'the number of effects') + 1
							liMiasmaPromotions = [iPromotion for iPromotion in liSelectablePromotions if not pUnit.isHasPromotion(iPromotion)]

							if len(liMiasmaPromotions) < iCount:
								iCount = len(liMiasmaPromotions)
							liChosenPromotion = []
							for iLoop in range(iCount):
								liChosenPromotion.append(liMiasmaPromotions.pop( CyGame().getSorenRandNum(len(liMiasmaPromotions), "Variant") ))

							liChosenPromotion.sort()
							for iChosenPromotion in liChosenPromotion:
								pUnit.setHasPromotion(iChosenPromotion, True)

def spellTutorialOfMeal(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	ePlayer = pCaster.getOwner()
	iCasterID = pCaster.getID()
	eSlave = gc.getSpellInfo(eSpell).getUnitInStackPrereq()
	pVictim = -1
	for iUnitIndex in xrange(pPlot.getNumUnits()):
		pUnit = pPlot.getUnit(iUnitIndex)
		if pUnit.getOwner() == ePlayer:
			if pUnit.getUnitType() == eSlave:
				if pVictim == -1 or pVictim.getExperience() > pUnit.getExperience():
					if pUnit.getID() != iCasterID:
						pVictim = pUnit
	if pVictim != -1:
		pVictim.kill(False, PlayerTypes.NO_PLAYER)

def reqHandsOfDimension(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

#	if not pCaster.isHuman():
#		if pCaster.getFortifyTurns() < 5:
#			return False

	iResistMax = 95

	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	pBestUnit = -1
	iBestValue = 0
	for pUnit in lpRangedUnits:
		if pUnit.canAttack():
			iResist = pUnit.getResistChance(pCaster, eSpell)
			if iResist <= iResistMax:
				iValue = pUnit.getFortifyTurns()
				iValue += (100 - iResist)
				if iBestValue < iValue:
					iBestValue = iValue
					pBestUnit = pUnit

	if pBestUnit != -1:
		iRange = 1
		lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, False, TeamTypes.NO_TEAM)
		for pTargetPlot in lpRangedPlots:
			if pTargetPlot.getNumUnits() == 0:
				if pBestUnit.canMoveInto(pTargetPlot, False, False, False):
					return True

	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellHandsOfDimension(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	iResistMax = 95

	pPlot = pCaster.plot()
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	pBestUnit = -1
	iBestValue = 0
	for pUnit in lpRangedUnits:
		if pUnit.canAttack():
			iResist = pUnit.getResistChance(pCaster, eSpell)
			if iResist <= iResistMax:
				iValue = pUnit.getFortifyTurns()
				iValue += (100 - iResist)
				if iBestValue < iValue:
					iBestValue = iValue
					pBestUnit = pUnit

	if pBestUnit != -1:
		if not pBestUnit.isResisted(pCaster, eSpell):
			iRange = 1
			lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, False, TeamTypes.NO_TEAM)
			lpTransferPlots = []
			for pTargetPlot in lpRangedPlots:
				if pTargetPlot.getNumUnits() == 0:
					if pBestUnit.canMoveInto(pTargetPlot, False, False, False):
						lpTransferPlots.append(pTargetPlot)

			if len(lpTransferPlots) > 0:
				pTransferPlot = lpTransferPlots[CyGame().getSorenRandNum(len(lpTransferPlots), "Hands of Dimension")]
				iX = pTransferPlot.getX()
				iY = pTransferPlot.getY()

				szButton = gc.getSpellInfo(eSpell).getButton()
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_HANDS_OF_DIMENSION', (pCaster.getNameKey(), pBestUnit.getNameKey(), ))
				CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, iX, iY, True, True)
				szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_HANDS_OF_DIMENSION_ENEMY', (pBestUnit.getNameKey(), ))
				CyInterface().addMessage(pBestUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, iX, iY, True, True)

				pBestUnit.setXY(iX, iY, False, True, True)
				pBestUnit.setFortifyTurns(0)

def spellBreeding(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pPlot.setFeatureType(en.eFeatureForestNew, 0)

# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
def effectVariant(argsList):
	pCaster = argsList[0]

	iPlayer = pCaster.getOwner()
	if CyGame().getSorenRandNum(10000, "Variant num") < 150:
		iCount = CyGame().getSorenRandNum(1, 'the number of effects') + 1
		liPromotion = [	gc.getInfoTypeForString('PROMOTION_AMPHIBIOUS'),
					gc.getInfoTypeForString('PROMOTION_COLD_RESISTANCE'),
					gc.getInfoTypeForString('PROMOTION_COMMAND1'),
					gc.getInfoTypeForString('PROMOTION_DRILL1'),
					gc.getInfoTypeForString('PROMOTION_FEAR'),
					gc.getInfoTypeForString('PROMOTION_FIRE_RESISTANCE'),
					gc.getInfoTypeForString('PROMOTION_FLYING'),
					gc.getInfoTypeForString('PROMOTION_LIGHT'),
					gc.getInfoTypeForString('PROMOTION_LIGHTNING_RESISTANCE'),
					gc.getInfoTypeForString('PROMOTION_MAGIC_IMMUNE'),
					gc.getInfoTypeForString('PROMOTION_MEDIC1'),
					gc.getInfoTypeForString('PROMOTION_MUTATED'),
					gc.getInfoTypeForString('PROMOTION_NOMAD'),
					gc.getInfoTypeForString('PROMOTION_PERFECT_SIGHT'),
					gc.getInfoTypeForString('PROMOTION_POISON_RESISTANCE'),
					gc.getInfoTypeForString('PROMOTION_PROPHECY_MARK'),
					gc.getInfoTypeForString('PROMOTION_SPIRIT_GUIDE'),
					gc.getInfoTypeForString('PROMOTION_STIGMATA'),
					gc.getInfoTypeForString('PROMOTION_STONESKIN'),
					gc.getInfoTypeForString('PROMOTION_UNHOLY_TAINT'),
					gc.getInfoTypeForString('PROMOTION_VILE_TOUCH'),
					gc.getInfoTypeForString('PROMOTION_VULNERABLE_TO_FIRE'),
					gc.getInfoTypeForString('PROMOTION_WINTERBORN'),
					gc.getInfoTypeForString('PROMOTION_DARK_MAGIC1'),
					gc.getInfoTypeForString('PROMOTION_STRANGER'),
					gc.getInfoTypeForString('PROMOTION_MARK_OF_THE_WARDEN'),
					gc.getInfoTypeForString('PROMOTION_ADVENTURER'),
					gc.getInfoTypeForString('PROMOTION_GRAVITATION'),
					gc.getInfoTypeForString('PROMOTION_HOOF'),
					gc.getInfoTypeForString('PROMOTION_FOUR_EYE'),
					gc.getInfoTypeForString('PROMOTION_SLAUGHTER_IMPULSER'),
					gc.getInfoTypeForString('PROMOTION_SHELL'),
					gc.getInfoTypeForString('PROMOTION_HAND_OF_THE_POISON')	]

		liChosenPromotion = []
		iChosenCount = 0
		for iPromotion in liPromotion:
			if pCaster.isHasPromotion(iPromotion):
				iChosenCount += 1
			else:
				liChosenPromotion.append(iPromotion)
		liChosenPromotion.sort()

		if len(liChosenPromotion) > 0:
			liSelectedPromotion = []
			for iLoop in xrange(iCount):
				liSelectedPromotion.append(liChosenPromotion.pop( CyGame().getSorenRandNum(len(liChosenPromotion), "Variant") ))
			liSelectedPromotion.sort()
			for iSelectedPromotion in liSelectedPromotion:
				pCaster.setHasPromotion(iSelectedPromotion, True)
				if pCaster.isHasPromotion(iSelectedPromotion):
					szButton = gc.getPromotionInfo(iSelectedPromotion).getButton()
					CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EFFECT_VARIANT", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed,pCaster.getX(),pCaster.getY(), True, True)
"""
# Kaijin <<< End

#Baldralfar End

#Nougbii Start
def reqReconstruction(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	leBonusTypes = [eBonus for eBonus in xrange(gc.getNumBonusInfos())]

	iCount = 0
	for eBonus in leBonusTypes:
		iCount += CyMap().getNumBonuses(eBonus)
	if iCount == 0:
		return False

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if not pPlayer.isHuman():
# ent >>>
#		if pPlayer.getNumCities() < (gc.getWorldInfo(CyMap().getWorldSize()).getTargetNumCities() // 2) + 1:
#			return False
		if cf.AI_hasRoomForFound(pCaster.getOwner()):
			return False
# ent <<<
	return True

def spellReconstruction(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	# 資源リストを作成
	lePlaceableBonuses = []
	#iNumBonusClass = gc.getNumBonusClassInfos()
	iNumBonusClass = 8
	leConvertibleBonusClasses = []
	for eBonusClass in xrange(iNumBonusClass):
		leConvertibleBonusClasses.append([])
	lszExcludeBonuses = [	'BONUS_CLAM', 'BONUS_CRAB', 'BONUS_FISH', 'BONUS_PEARL', 'BONUS_SHRIMP', 'BONUS_JADE', 'BONUS_WHALE', 
							'BONUS_NIGHTMARE', 'BONUS_SHEUT_STONE', 'BONUS_TOAD', 'BONUS_GULAGARM', 'BONUS_RAZORWEED', 
							'BONUS_FRUIT_OF_YGGDRASIL', 'BONUS_ALE', 'BONUS_BOOK', 'BONUS_DRAGONMETAL', 
							'BONUS_MANA_ICE', 'BONUS_MANA_DIMENSIONAL', 'BONUS_PATRIAN_ARTIFACTS'									]
	leExcludeBonuses = []
	for szExcludeBonus in lszExcludeBonuses:
		leExcludeBonuses.append(gc.getInfoTypeForString(szExcludeBonus))
	leExcludeBonuses.sort()

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)

	for eBonus in xrange(gc.getNumBonusInfos()):
		if eBonus in leExcludeBonuses:
			continue
		eTechReveal = gc.getBonusInfo(eBonus).getTechReveal()
		if eTechReveal != TechTypes.NO_TECH:
			if not pPlayer.isHasTech(eTechReveal):
				continue
		if pPlayer.countOwnedBonuses(eBonus) > 0:
			continue
		eBonusClass = gc.getBonusInfo(eBonus).getBonusClassType()
		leConvertibleBonusClasses[eBonusClass].append(eBonus)
		if not eBonus in g_leManaTypes:
			lePlaceableBonuses.append(eBonus)

	# 資源の生成
	eTeam = pPlayer.getTeam()
	iNewBonusOdds = 4
	eEffect = gc.getInfoTypeForString('EFFECT_CREATION')
	for iPlotIndex in xrange(CyMap().numPlots()):
		pPlot = CyMap().plotByIndex(iPlotIndex)
		if pPlot.getOwner() == ePlayer:
			if pPlot.isWater():
				continue
			if pPlot.isImpassable():
				continue
			if pPlot.isCity():
				continue
			eImprovement = pPlot.getImprovementType()
			if eImprovement != ImprovementTypes.NO_IMPROVEMENT:
				if gc.getImprovementInfo(eImprovement).isPermanent():
					continue
			eBonus = pPlot.getBonusType(eTeam)
			if eBonus != BonusTypes.NO_BONUS:
				if pPlayer.countOwnedBonuses(eBonus) > 1 and not eBonus in leExcludeBonuses:
					# 資源の置き換え
					leReplaceBonusTypes = leConvertibleBonusClasses[gc.getBonusInfo(eBonus).getBonusClassType()]
					if len(leReplaceBonusTypes) > 0:
						eReplaceBonus = leReplaceBonusTypes[CyGame().getSorenRandNum(len(leReplaceBonusTypes), "Bonuses Select")]
						pPlot.setBonusType(eReplaceBonus)
						lePlaceableBonuses.remove(eReplaceBonus)
						leConvertibleBonusClasses[gc.getBonusInfo(eReplaceBonus).getBonusClassType()].remove(eReplaceBonus)

						if eImprovement != ImprovementTypes.NO_IMPROVEMENT:
							if not pPlot.canHaveImprovement(eImprovement, ePlayer, False):
								pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)

						if pPlot.isVisibleToWatchingHuman():
							CyEngine().triggerEffect(eEffect, pPlot.getPoint())
			else:
				# 新たな資源の配置
				if CyGame().getSorenRandNum(100, 'New Bonus') < iNewBonusOdds:
					if len(lePlaceableBonuses) > 0:
						eNewBonus = lePlaceableBonuses[CyGame().getSorenRandNum(len(lePlaceableBonuses), "Bonuses Select")]
						pPlot.setBonusType(eNewBonus)
						lePlaceableBonuses.remove(eNewBonus)
						leConvertibleBonusClasses[gc.getBonusInfo(eNewBonus).getBonusClassType()].remove(eNewBonus)

						if pPlot.isVisibleToWatchingHuman():
							CyEngine().triggerEffect(eEffect, pPlot.getPoint())

def reqFoodDistribution(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	if pCity.getPopulation() < 3:
		return ReasonTypes.REASON_DISABLED_LACK_OF_POPULATION
	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getNumCities() < 2:
		return False
	if not pPlayer.isHuman():
		if pCity.getPopulation() < 15:
			return False
		if pCity.unhappyLevel(0) <= pCity.happyLevel():
			return False
# ent >>>
#		if pPlayer.getNumCities() < gc.getWorldInfo(CyMap().getWorldSize()).getTargetNumCities():
#			return False
		if cf.AI_hasRoomForFound(pCaster.getOwner()):
			return False
# ent <<<
	return True

def spellFoodDistribution(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	iAngerTimer = cyFlatValue(3, g_dGameSpeedPercent["HurryConscriptAnger"], True)
	pCity.changeHurryAngerTimer(iAngerTimer)

	eCasterPlayer = pCaster.getOwner()
	pCasterPlayer = gc.getPlayer(eCasterPlayer)
	iNumRegularCities = pCasterPlayer.getNumCities() - pCasterPlayer.getNumSettlements()
	iFoodStrage = (10 + pCity.getPopulation() * 2) // iNumRegularCities
	szButton = 'Art/Interface/Symbols/Food/food05.dds'
	szSound = 'AS2D_DISCOVERBONUS'
	for pyCity in PyPlayer(eCasterPlayer).getCityList():
		pLoopCity = pyCity.GetCy()
		pLoopCity.changeFood(+iFoodStrage)
		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_FOOD_DISTRIBUTION', (pCity.getNameKey(), pLoopCity.getNameKey()))
		CyInterface().addMessage(eCasterPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pLoopCity.getX(), pLoopCity.getY(), True, True)

def disableTransplant(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pPlot.getPlotCity()
	if pCity.getPopulation() <= 1:
		return ReasonTypes.REASON_DISABLED_LACK_OF_POPULATION
	if not pCaster.canFight():
		return ReasonTypes.REASON_DISABLED_CAN_NOT_FIGHT

	if not pCaster.isHuman():
		if pCity.getPopulation() <= 10:
			return True
		if (pCity.happyLevel() - pCity.unhappyLevel(0)) < 0:
			return True
	return False

def spellTransplant(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	iAngerTimer = cyFlatValue(3, g_dGameSpeedPercent["HurryConscriptAnger"], True)
	pCity.changeHurryAngerTimer(iAngerTimer)
	
# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
def effectMuppet(argsList):
	pCaster = argsList[0]

	pCaster.setExperience(0, -1)
"""
# Kaijin <<< End

#Nougbii End

#Aristrakh Start
def reqDeathMarch(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if not pCaster.isHuman():
##--------	Advanced DeathMarch: Modified by ent
		"""
		pPlayer = gc.getPlayer(pCaster.getOwner())
		if pPlayer.getNumUnits() < 25:
			return False
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.getAtWarCount(True) == 0:
			return False
		"""
		ePlayer = pCaster.getOwner()
		pPlayer = gc.getPlayer(ePlayer)
		iTotalUnhealthRate = 0
		for pyCity in PyPlayer(ePlayer).getCityList():
			pCity = pyCity.GetCy()
			iTotalUnhealthRate -= pCity.healthRate(False, 0)
		pTeam = gc.getTeam(pPlayer.getTeam())
		eDeathRitual = gc.getInfoTypeForString('PROJECT_DEATH_RITUAL')
		if iTotalUnhealthRate < pPlayer.getNumCities() * 2 and not pTeam.isProjectMaxedOut(eDeathRitual, 0):
			if pPlayer.getNumUnits() < 25:
				return False
			pTeam = gc.getTeam(pCaster.getTeam())
			if pTeam.getAtWarCount(True) == 0:
				return False

		if cf.AI_hasRoomForFound(ePlayer):
			return False
##--------	Advanced DeathMarch: End Modify
	return True

def spellDeathMarch(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	eDeathMarch = gc.getInfoTypeForString('PROMOTION_DEATH_MARCH')
	for pUnit in PyPlayer(ePlayer).getUnitList():
		if not pUnit.isSummoned():
			if pUnit.canFight():
				if pUnit.getRace() == en.eRaceUndead:
					pUnit.setHasPromotion(eDeathMarch, True)
					
##--------	Advanced DeathMarch: Added by ent
	eUndeadCity = gc.getInfoTypeForString('BUILDING_UNDEAD_CITY')
	for pyCity in PyPlayer(ePlayer).getCityList():
		pCity = pyCity.GetCy()
		pCity.setNumRealBuilding(eUndeadCity, 1)
##--------	Advanced DeathMarch: End Add

#Aristrakh End

#Megisus Start
def spellOuroboros(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	leTrait = [eTrait for eTrait in range(gc.getNumTraitInfos()) if gc.getTraitInfo(eTrait).isSelectable() and not pPlayer.hasTrait(eTrait)]
	liChosenTrait = []
	liChosenTrait.append(leTrait.pop( CyGame().getSorenRandNum(len(leTrait), "Ouroboros") ))
	liChosenTrait.sort()
	for iChosenTrait in liChosenTrait:
		pPlayer.setHasTraitWithSource(iChosenTrait, True, TraitSourceTypes.TRAITSOURCE_RANDOM_EVENT)

def disabledIncubation(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getUnitClassCountPlusMaking(gc.getInfoTypeForString('UNITCLASS_FIGURE')) >= 1:
		return True
	return False

def spellIncubation(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]
	liSummonedUnitIDs = argsList[3]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getGuildPlusCounter(50) < 5:
		pPlayer.changeGuildPlusCounter(50, 1)
		
	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()
	iAngerTimer = cyFlatValue(3, g_dGameSpeedPercent["HurryConscriptAnger"], True)
	pCity.changeHurryAngerTimer(iAngerTimer)

	lpSummonedUnits = []
	for iSummonedUnitID in liSummonedUnitIDs:
		lpSummonedUnits.append(pPlayer.getUnit(iSummonedUnitID))

		iBaseDuration = 20
		iExtraDuration = (cyFlatValue(iBaseDuration, g_dGameSpeedPercent["GoldenAge"], True))
		for pSummonedUnit in lpSummonedUnits:
			pSummonedUnit.changeDuration(iExtraDuration)

			if  pPlayer.getGuildPlusCounter(50) == 1:
				pSummonedUnit.setName(CyTranslator().getText('TXT_KEY_UNIT_FIGURE_NUMBERING_1', ()))
			if  pPlayer.getGuildPlusCounter(50) == 2:
				pSummonedUnit.setName(CyTranslator().getText('TXT_KEY_UNIT_FIGURE_NUMBERING_2', ()))
			if  pPlayer.getGuildPlusCounter(50) == 3:
				pSummonedUnit.setName(CyTranslator().getText('TXT_KEY_UNIT_FIGURE_NUMBERING_3', ()))
			if  pPlayer.getGuildPlusCounter(50) == 4:
				pSummonedUnit.setName(CyTranslator().getText('TXT_KEY_UNIT_FIGURE_NUMBERING_4', ()))
			if  pPlayer.getGuildPlusCounter(50) >= 5:
				pSummonedUnit.setName(CyTranslator().getText('TXT_KEY_UNIT_FIGURE_NUMBERING_5', ()))

def spellDrillingHomunculus(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]
	liSummonedUnitIDs = argsList[3]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_FORNACE_OF_MIDAS')) > 0:
		customSummonSpellData = CvCustomSummonSpellData()
		customSummonSpellData.eUnit = gc.getSpellInfo(eSpell).getCreateUnitType()
		customSummonSpellData.iNumUnits = 1
		pCaster.castCustomSummon(customSummonSpellData)

#Megisus End

#Dimensional Spells Start
def reqTransfer(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	iResistMax = 95
	if not pPlayer.isHuman():
		if isWorldUnitClass(pCaster.getUnitClassType()):
			return ReasonTypes.REASON_DISABLED_WORLDUNIT_NOT_ALLOWED
		iResistMax = 20
	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	lpTargetUnits = [pUnit for pUnit in lpRangedUnits if pUnit.canFight()]
	for pUnit in lpTargetUnits:
		iResist = pUnit.getResistChance(pCaster, eSpell)
		if iResist <= iResistMax:
			return True
	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellTransfer(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	pPlot = pCaster.plot()
	kSpell = gc.getSpellInfo(eSpell)

	szButton = kSpell.getButton()

	## Specifies the transition tile
	def getTransitionTile():
		iBestValue = 0
		pBestPlot = -1
		for iPlotNum in xrange (CyMap().numPlots()):
			iValue = 0
			pPlot = CyMap().plotByIndex(iPlotNum)
			if pPlot.getNumUnits() > 0:
				continue
			if pPlot.isOwned():
				continue
			if pPlot.isCity():
				continue
			if pPlot.getFeatureType() == en.eFeatureIce:
				continue
			iValue = CyGame().getSorenRandNum(1000, "Transfer")
			if not pPlot.isImpassable():
				if bDomainSea == pPlot.isWater():
					iValue += 250
			if iValue > iBestValue:
				iBestValue = iValue
				pBestPlot = pPlot
		return pBestPlot

	lpRangedUnits = cyGetSpellRangedUnits(pCaster, eSpell, pPlot, False, True)
	lpTargetUnits = [pUnit for pUnit in lpRangedUnits if pUnit.canFight()]

#	iTargetCounts = kSpell.getTargetLimitPerPlot()
	iTargetCounts = 6
	if iTargetCounts > len(lpTargetUnits):
		iTargetCounts = len(lpTargetUnits)

	if iTargetCounts > 0:
		lpSelectedTargets = []
		for iLoop in xrange(iTargetCounts):
			lpSelectedTargets.append(lpTargetUnits.pop( CyGame().getSorenRandNum(len(lpTargetUnits), "Transfer") ))
		lpSelectedTargets.sort()

		iCasterX = pCaster.getX()
		iCasterY = pCaster.getY()

		for pUnit in lpSelectedTargets:
			## Success
			if not pUnit.isResisted(pCaster, eSpell):
				bDomainSea = (pUnit.getDomainType() == DomainTypes.DOMAIN_SEA)
				pBestPlot = getTransitionTile()
				if pBestPlot != -1:
					iBestX = pBestPlot.getX()
					iBestY = pBestPlot.getY()
					eEnemy = pUnit.getOwner()
					szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SPELL_TRANSFER_CASTER_TRUE', (pCaster.getNameKey(), pUnit.getNameKey(), ))
					CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, iCasterX, iCasterY, True, True)
					szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SPELL_TRANSFER_ENEMY', (pUnit.getNameKey(), ))
					CyInterface().addMessage(eEnemy, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, iBestX, iBestY, True, True)
					if pUnit.canMoveInto(pBestPlot, False, False, False):
						pUnit.setXY(iBestX, iBestY, False, True, True)
					else:
						pUnit.kill(True, ePlayer)
						if pBestPlot.isPeak():
							szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SPELL_TRANSFER_BURYING', (pUnit.getNameKey(), ))
						elif pBestPlot.isWater() and not bDomainSea:
							szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SPELL_DROWNING', (pUnit.getNameKey(), ))
						elif not pBestPlot.isWater() and bDomainSea:
							szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SPELL_DESTRUCTION', (pUnit.getNameKey(), ))
						else:
							szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SPELL_DEATH', (pUnit.getNameKey(), ))
						CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorWhite, iCasterX, iCasterY, True, True)
						CyInterface().addMessage(eEnemy, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorWhite, iBestX, iBestY, True, True)

			## Reaction
			elif CyGame().getSorenRandNum(1000, "Reaction") < 50:
				bDomainSea = (pCaster.getDomainType() == DomainTypes.DOMAIN_SEA)
				pBestPlot = getTransitionTile()
				if pBestPlot != -1:
					iBestX = pBestPlot.getX()
					iBestY = pBestPlot.getY()
					szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SPELL_TRANSFER_CASTER_FALSE', (pCaster.getNameKey(), ))
					CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, iBestX, iBestY, True, True)
					if pCaster.canMoveInto(pBestPlot, False, False, False):
						pCaster.setXY(iBestX, iBestY, False, True, True)
					else:
						pCaster.kill(True, PlayerTypes.NO_PLAYER)
						if pBestPlot.isPeak():
							szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SPELL_TRANSFER_BURYING', (pCaster.getNameKey(), ))
						elif pBestPlot.isWater() and not bDomainSea:
							szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SPELL_DROWNING', (pCaster.getNameKey(), ))
						elif not pBestPlot.isWater() and bDomainSea:
							szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SPELL_DESTRUCTION', (pCaster.getNameKey(), ))
						else:
							szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SPELL_DEATH', (pCaster.getNameKey(), ))
						CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorWhite, iBestX, iBestY, True, True)

#Dimensional Spells End

#Orbis Equipment Start
"""
def reqMutationPotion(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	return True
"""

def spellMutationPotion(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	listProms = []
	for eProm in xrange(gc.getNumPromotionInfos()):
		if not pCaster.isHasPromotion(eProm):
			if not gc.getPromotionInfo(eProm).isEquipment():
				if not gc.getPromotionInfo(eProm).isRace():
					if gc.getPromotionInfo(eProm).getMinLevel() >= 0:
						listProms.append(eProm)
	if len(listProms) > 0:
		iRnd = CyGame().getSorenRandNum(len(listProms), "Mutation Potion")
		pCaster.setHasPromotion(listProms[iRnd], True)
	if CyGame().getSorenRandNum(100, "Mutation Potion") >= 30:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MUTATION_POTION'), False)

#Orbis Equipment End

#OAC Addition Spells - START
def reqSlaveAddCitySpecial(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isAutomated():
		return False
	pCity = pPlot.getPlotCity()
	if pCity.getFreeSpecialistCount(en.eSpecialistCitizen) >= 5:
		return False
	if pCaster.getCivilizationType() == en.eCivilizationCualli:
		if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_SLAVE_PIT')) > 0:
			return False
	if not pCaster.isHuman():
		pPlayer = gc.getPlayer(pCaster.getOwner())
		eCiv = pCaster.getCivilizationType()
		if eCiv == en.eCivilizationDroaum and pPlayer.isIgnoreFood():
			return False
	return True

#OAC Addition Spells End

#OAC FFH2 Civs Unique Spells - START
# ent >>>
"""
def reqTheft(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCity = pCaster.plot().getPlotCity()
	pTarget = gc.getPlayer(pCity.getOwner())
	if pCity.isNone():
		return False
	if not pTarget.isAlive():
		return False
	if pTarget.isBarbarian():
		return False
	if pTarget.getTeam() == pCaster.getTeam():
		return False
	if not pPlayer.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.isVassal(pCity.getTeam()):
			return False
		iChance = (pCaster.getCombatAttackTimes100() // 100 + pCaster.getLevel()) * 5
		if iChance <= 40:
			return False
	return True
"""

def reqTheftTech(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCity = pPlot.getPlotCity()
	if pCity.isNone():
		return False
	pTarget = gc.getPlayer(pCity.getOwner())
	if pTarget.isBarbarian():
		return False
	if pTarget.getTeam() == pCaster.getTeam():
		return ReasonTypes.REASON_DISABLED_IMMUNE_FRIENDLY_CITY
	pTeam = gc.getTeam(pCaster.getTeam())
	eBestTech = TechTypes.NO_TECH
	iBestValue = 0
	for eTech in xrange(gc.getNumTechInfos()):
		if pTarget.isHasTech(eTech):
			if not pPlayer.isHasTech(eTech):
				if pPlayer.canResearch(eTech, False):
					iValue = pTeam.getResearchLeft(eTech)
					if iBestValue < iValue:
						iBestValue = iValue
						eBestTech = eTech
	if eBestTech == TechTypes.NO_TECH:
		return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET
	if not pPlayer.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.isVassal(pCity.getTeam()):
			return False
		iChance = (pCaster.getCombatAttackTimes100() // 100 + pCaster.getLevel()) * 5
		if iChance <= 40:
			return False
	return True
# ent <<<

def spellTheftTech(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pCaster.plot().getPlotCity()
	if pCity.isNone():
		return
	iChance = (pCaster.getCombatAttackTimes100() // 100 + pCaster.getLevel()) * 5
	if iChance > 95:
		iChance = 95

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	eTeam = pPlayer.getTeam()
	pTeam = gc.getTeam(eTeam)

	eTarget = pCity.getOwner()
	pTarget = gc.getPlayer(eTarget)
	if CyGame().getSorenRandNum(100, "Theft") < iChance:
		ltTargetTechs = []
		for eTech in xrange(gc.getNumTechInfos()):
			if pTarget.isHasTech(eTech):
				if not pPlayer.isHasTech(eTech):
					if pPlayer.canResearch(eTech, False):
						iResearchLeft = pTeam.getResearchLeft(eTech)
						ltTargetTechs.append((iResearchLeft, eTech))
		if len(ltTargetTechs) > 0:
			ltTargetTechs.sort()
			ltTargetTechs.reverse()
			eTheftTech = ltTargetTechs[0][1]
			pTeam.setHasTech(eTheftTech, True, ePlayer, False, True)
			szButton = gc.getSpellInfo(eSpell).getButton()
			szBuffer = CyTranslator().getText("TXT_KEY_MESSAGE_THEFT_TECH_GOOD", ())
			CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), szBuffer,'', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton,en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
			szBuffer = CyTranslator().getText("TXT_KEY_MESSAGE_THEFT_TECH_BAD", ())
			CyInterface().addMessage(eTarget, True, gc.getEVENT_MESSAGE_TIME(), szBuffer,'', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton,en.eColorRed, pCity.getX(), pCity.getY(), True, True)
	else:
		if CyGame().getSorenRandNum(100, "Theft") < 50:
			pCaster.setXY(pPlayer.getCapitalCity().getX(), pPlayer.getCapitalCity().getY(), False, True, True)
		else:
			pCaster.kill(True, PlayerTypes.NO_PLAYER)
		if pTarget.getTeam() != eTeam:
			pTeam.declareWar(pTarget.getTeam(), False, WarPlanTypes.WARPLAN_LIMITED)

def reqTheftGold(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	pCity = pPlot.getPlotCity()
	if pCity.isNone():
		return False
	pTarget = gc.getPlayer(pCity.getOwner())
	if pTarget.isBarbarian():
		return False
	if pTarget.getTeam() == pCaster.getTeam():
		return ReasonTypes.REASON_DISABLED_IMMUNE_FRIENDLY_CITY
	if pTarget.getGold() <= 0:
		return ReasonTypes.REASON_DISABLED_LACK_OF_WEALTH
	if not pPlayer.isHuman():
		pTeam = gc.getTeam(pCaster.getTeam())
		if pTeam.isVassal(pCity.getTeam()):
			return False
		iChance = (pCaster.getCombatAttackTimes100() // 100 + pCaster.getLevel()) * 5
		if iChance <= 40:
			return False
		iGold = pCity.getPopulation() * 5
		if iGold < 100:
			return False
	return True

def spellTheftGold(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pCity = pCaster.plot().getPlotCity()
	if pCity.isNone():
		return
	iChance = (pCaster.getCombatAttackTimes100() // 100 + pCaster.getLevel()) * 5
	if iChance > 95:
		iChance = 95

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	eTeam = pPlayer.getTeam()
	pTeam = gc.getTeam(eTeam)

	eTarget = pCity.getOwner()
	pTarget = gc.getPlayer(eTarget)
	if CyGame().getSorenRandNum(100, "Theft") < iChance:
		iGold = pCity.getPopulation() * 5
		if iGold > (pTarget.getGold() // 2):
			iGold = pTarget.getGold() // 2

		szButton = gc.getSpellInfo(eSpell).getButton()

		pPlayer.changeGold(iGold)
		szBuffer = CyTranslator().getText("TXT_KEY_MESSAGE_THEFT_GOLD_GOOD", (iGold, ))
		CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), szBuffer,'', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton,en.eColorGreen, pCity.getX(), pCity.getY(), True, True)

		iGold = iGold * -1
		pTarget.changeGold(iGold)
		szBuffer = CyTranslator().getText("TXT_KEY_MESSAGE_THEFT_GOLD_BAD", (iGold, ))
		CyInterface().addMessage(eTarget, True, gc.getEVENT_MESSAGE_TIME(), szBuffer,'', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton,en.eColorRed, pCity.getX(), pCity.getY(), True, True)
	else:
		pCaster.setXY(pPlayer.getCapitalCity().getX(), pPlayer.getCapitalCity().getY(), False, True, True)
		if pTarget.getTeam() != eTeam:
			pTeam.declareWar(pTarget.getTeam(), False, WarPlanTypes.WARPLAN_LIMITED)

# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
def effectIntensification(argsList):
	pCaster = argsList[0]

	iX = pCaster.getX()
	iY = pCaster.getY()
	pPlayer = gc.getPlayer(pCaster.getOwner())
	iTeam = pPlayer.getTeam()
	eTeam = gc.getTeam(iTeam)
	for iiX in xrange(iX-1, iX+2, 1):
		for iiY in xrange(iY-1, iY+2, 1):
			pPlot = CyMap().plot(iiX,iiY)
			if not pPlot.isNone():
				for iUnit in xrange(pPlot.getNumUnits()):
					pUnit = pPlot.getUnit(iUnit)
					if not eTeam.isAtWar(pUnit.getTeam()):
						if not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_1')):
							pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_1'), True)
"""
# Kaijin <<< End

# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
def effectIntensified(argsList):
	pCaster = argsList[0]

	iX = pCaster.getX()
	iY = pCaster.getY()
	pPlayer = gc.getPlayer(pCaster.getOwner())
	iTeam = pPlayer.getTeam()
	eTeam = gc.getTeam(iTeam)
	iIntensify = 0
	for iiX in xrange(iX-1, iX+2, 1):
		for iiY in xrange(iY-1, iY+2, 1):
			pPlot = CyMap().plot(iiX,iiY)
			if not pPlot.isNone():
				for iUnit in xrange(pPlot.getNumUnits()):
					pUnit = pPlot.getUnit(iUnit)
					if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFICATION')) and iIntensify <=5:
						iIntensify += 1
	if iIntensify >= 5:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_5'), True)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_4'), True)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_3'), True)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_2'), True)
	elif iIntensify == 4:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_5'), False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_4'), True)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_3'), True)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_2'), True)
	elif iIntensify == 3:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_5'), False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_4'), False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_3'), True)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_2'), True)
	elif iIntensify == 2:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_5'), False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_4'), False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_3'), False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_2'), True)
	elif iIntensify == 1:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_5'), False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_4'), False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_3'), False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_2'), False)
	elif iIntensify == 0:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_5'), False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_4'), False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_3'), False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_2'), False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_1'), False)
"""

#OAC Unique Barbarian Spell Start
def disabledSummonKOD(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	"""
	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getUnitClassCountPlusMaking(gc.getInfoTypeForString('UNITCLASS_DIAMOND_KNIGHT')) >= 3:
		return True
	"""
	if not pCaster.isHuman():
		if pCaster.movesLeft() != 0:
			return True

	return False

def spellSummonKOD(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]
	liSummonedUnitIDs = argsList[3]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	for iSummonedUnitID in liSummonedUnitIDs:
		pNewUnit = pPlayer.getUnit(iSummonedUnitID)
		pNewUnit.kill(False, PlayerTypes.NO_PLAYER)

	customSummonSpellData = CvCustomSummonSpellData()
	customSummonSpellData.eUnit = gc.getInfoTypeForString('UNIT_DIAMOND_KNIGHT')
	customSummonSpellData.iNumUnits = 3
	customSummonSpellData.iDuration = 2
	customSummonSpellData.bAbility = True
	lpNewUnits = pCaster.castCustomSummon(customSummonSpellData)
	for pNewUnit in lpNewUnits:
		pNewUnit.setLevel(12)
		pNewUnit.changeCombatStr(2800)
		pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HERO'), True)
		pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FLYING'), True)
		pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_GUARDSMAN'), True)
		pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SKIRMISHER'), True)

		pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_REGENERATION'), True)
		pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STONESKIN'), True)
		pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENCHANTED_BLADE'), True)
		pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_COURAGE'), True)
		pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LOYALTY'), True)

#OAC Unique Barbarian Spell End
# Kaijin <<< End

#OAC FFH2 Civs Unique Spells - END

#OAC Special Spells - Start
## ent >>>
def reqOfferGela(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pPlayer.getGuildPlusCounter(1) == 4:
		return True
	return False

def spellOfferGela(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	pPlot = pCaster.plot()

	pCaster.setHasPromotion(en.eEquipmentGela, False)
	pNewUnit = pPlayer.initUnit(en.eUnitAngel, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(en.ePromotionHero, True) 
	szButton = gc.getSpellInfo(eSpell).getButton()
	CyInterface().addMessage(ePlayer, True, 25, CyTranslator().getText("TXT_KEY_MESSAGE_BASIUM_GELA", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
	CyGame().changeGlobalCounter(-10)
## ent <<<
#OAC Special Spells - End

#OAC Unique - General - Start
def reqConversion(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]
 
	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	eCasterReligion = pCaster.getReligion()

	if not pCaster.isHuman():
		if eCasterReligion != ReligionTypes.NO_RELIGION:
			if CyGame().getSorenRandNum(100, "Conversion") < 95:
				return False

	for eReligion in xrange(gc.getNumReligionInfos()):
		if eReligion != eCasterReligion:
			for pyCity in PyPlayer(ePlayer).getCityList():
				pLoopCity = pyCity.GetCy()
				if pLoopCity.isHasReligion(eReligion):
					return True

	return ReasonTypes.REASON_DISABLED_HAS_NO_TARGET

def spellConversion(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	ePlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	"""
	eStateReligion = pPlayer.getStateReligion()

	if not pCaster.isHuman():
		eStateReligion = pPlayer.getStateReligion()
		if pPlayer.getNumCities() > 0 and eStateReligion != ReligionTypes.NO_RELIGION:
			if pCaster.getReligion() != eStateReligion:
				pCaster.setReligion(eStateReligion)

	else:
		iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(), 'EVENTTRIGGER_SPELL_CONVERSION')
		triggerData = pPlayer.initTriggeredData(iEvent, True, -1, pCaster.getX(), pCaster.getY(), ePlayer, -1, -1, -1, pCaster.getID(), -1)
	"""
	iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(), 'EVENTTRIGGER_SPELL_CONVERSION')
	triggerData = pPlayer.initTriggeredData(iEvent, True, -1, pCaster.getX(), pCaster.getY(), ePlayer, -1, -1, -1, pCaster.getID(), -1)
	
def reqHospitable(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	eTeam = pCaster.getTeam()
	pCity = pPlot.getPlotCity()
	if eTeam == pCity.getTeam():
		return ReasonTypes.REASON_DISABLED_IMMUNE_FRIENDLY_CITY
	if pCity.isDisorder():
		return ReasonTypes.REASON_DISABLED_CITY_IS_REVOLTING

	if not pCaster.isHuman():
		pTeam = gc.getTeam(eTeam)
		if pTeam.getAnyWarPlanCount(True) > 0:
			return False
		if gc.getPlayer(pCity.getOwner()).AI_getAttitude(pCaster.getOwner()) == AttitudeTypes.ATTITUDE_FRIENDLY:
			return False

	return True

def spellHospitable(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()
	pCity = pPlot.getPlotCity()

	iCasterPlayer = pCaster.getOwner()
	iTargetPlayer = pCity.getOwner()
	pCasterPlayer = gc.getPlayer(iCasterPlayer)
	pTargetPlayer = gc.getPlayer(iTargetPlayer)

	szButton = gc.getSpellInfo(eSpell).getButton()
	szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SPELL_HOSPITABLE',())
	CyInterface().addMessage(iCasterPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
	CyInterface().addMessage(iTargetPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCity.getX(), pCity.getY(), True, True)

	pTargetPlayer.AI_changeAttitudeExtra(iCasterPlayer, 2)
"""
def disabledArmedFishingBoats(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	eImprovement = gc.getSpellInfo(eSpell).getCreateImprovementType()

	if pPlot.canHaveImprovement(eImprovement, iPlayer, False):
		if pPlayer.canBuild(pPlot, gc.getInfoTypeForString('BUILD_FISHING_BOATS'), False, False):
			return False
	return True

def disabledArmedWhalingBoats(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	eImprovement = gc.getSpellInfo(eSpell).getCreateImprovementType()

	if pPlot.canHaveImprovement(eImprovement, iPlayer, False):
		if pPlayer.canBuild(pPlot, gc.getInfoTypeForString('BUILD_WHALING_BOATS'), False, False):
			return False
	return True

def spellArmedFishingBoats(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	pPlot = pCaster.plot()

	if pPlot.getFeatureType() == en.eFeatureKelp:
		pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
	pCaster.setUnitAIType(UnitAITypes.UNITAI_UNKNOWN)
	pCaster.getGroup().pushMission(MissionTypes.MISSION_SEAPATROL, 0, 0, 0, False, False, MissionAITypes.NO_MISSIONAI, pPlot, pCaster)
"""
#OAC Unique - General - End

#Naval - Organize the Landing crew.
def disabledOrganizeTheLandingCrew(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isSummoned():
		return True
	return False

#Bug Ba Curry - Start
def spellEatBugDaRake(argsList):
	pCaster = argsList[0]
	pBestPlot = argsList[1]
	eSpell = argsList[2]

	cf.addPopup(CyTranslator().getText("TXT_KEY_MESSAGE_EAT_BUG_DA_RAKE",()),'Art_Kaijin/Interface/Popups/YamamotoPop.dds')
	pCaster.doDamage(25, 100, en.eDamagePoison)
	pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED'), True)

	"""
	iUnitID = cf.getUnitPlayerID(pCaster)
	pPlayer = gc.getPlayer(pCaster.getOwner())
	iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(), 'EVENTTRIGGER_SHARP_ARTILLERY')
	pPlayer.triggerCustomEvent(iEvent, -1, pCaster.getX(), pCaster.getY(), PlayerTypes.NO_PLAYER, -1, ReligionTypes.NO_RELIGION, CorporationTypes.NO_CORPORATION, iUnitID, BuildingTypes.NO_BUILDING)
	"""
#Bug Ba Curry - End

# Kaijin >>> Moved to CvEventManager.py "EndPlayerTurn"
"""
#Kod's items - Start
def effectKodsItems(argsList):
	pCaster = argsList[0]

	if CyGame().getSorenRandNum(100, "Tiltowaito") < 20:
		lpRangedUnits = cyGetSpellRangedUnits(pCaster, gc.getInfoTypeForString('SPELL_TILTOWAITO'), pCaster.plot(), False, True)
		eTeam = pCaster.getTeam()
		for pUnit in lpRangedUnits:
			if pUnit.isEnemy(eTeam, pUnit.plot()):
				pCaster.cast(gc.getInfoTypeForString('SPELL_TILTOWAITO'))
				break
#Kod's items - End
"""
# Kaijin <<< End

"""
#Summon Permanent
def disabledSummonPermanent(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]
	liSummonedUnitIDs = argsList[3]

	pPlayer = gc.getPlayer(pCaster.getOwner())

	return True
"""

#Dummy Enabled
def enabledDummy(argsList):
	pCaster = argsList[0]
	pPlot = argsList[1]
	eSpell = argsList[2]

	if pCaster.isHuman():
		return True
	else:
		return False
#Kaijin OAC End
