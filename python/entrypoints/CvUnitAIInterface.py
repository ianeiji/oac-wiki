## Civilization 4 (c) 2005 Firaxis Games
##
## name     : CvUnitAIInterface.py
## author   : Denev
## date     : 2012.07.23

import CvUtil
from CvPythonExtensions import *
import CvEventInterface
import CustomFunctions
import ScenarioFunctions
import CvPythonEnums

import PyHelpers
PyPlayer = PyHelpers.PyPlayer

# globals
cf = CustomFunctions.CustomFunctions()
en = CvPythonEnums.CvPythonEnums()
gc = CyGlobalContext()
sf = ScenarioFunctions.ScenarioFunctions()

# Kaijin >>>
g_leManaTypes = [iBonus for iBonus in xrange(gc.getNumBonusInfos()) if gc.getBonusInfo(iBonus).getBonusClassType() == gc.getDefineINT('BONUSCLASS_MANA')]
# Kaijin <<<

def AI_updateDonal(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	eRecruit = gc.getInfoTypeForString('SPELL_RECRUIT')

	if pPlot.isCity():
		if pUnit.canCast(eRecruit, False):
			pUnit.cast(eRecruit)
			return 1

	elif pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_RECRUITER')):
		pPlayer = gc.getPlayer(pUnit.getOwner())
# ent >>>
	## Bug Fix - Ability can cast during the Arcane Lacuna.
		"""
		if pPlayer.getDisableSpellcasting() < 1:
#			if pUnit.getGroup().getNumUnits() > 1:
#				pUnit.getGroup().joinGroup(-1)

			if pUnit.AI_retreatToCity():
				pUnit.getGroup().pushMission(MissionTypes.MISSION_SPELL, eRecruit, -1, 0, False, False, MissionAITypes.NO_MISSIONAI, CyMap().plotByIndex(-1), pPlayer.getUnit(-1))
				return 1
		"""

		if pUnit.AI_retreatToCity():
			pUnit.getGroup().pushMission(MissionTypes.MISSION_SPELL, eRecruit, -1, 0, False, False, MissionAITypes.NO_MISSIONAI, CyMap().plotByIndex(-1), pPlayer.getUnit(-1))
			return 1
# ent <<<
	return 0

def AI_updateRantine(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	pPlayer = gc.getPlayer(pUnit.getOwner())
	pTeam = gc.getTeam(pUnit.getTeam())

	if pTeam.getAtWarCount(True) > 0:
		return 0

	if pUnit.getDamage() > 0:
		return 0
# ent >>>
	if pPlayer.AI_isFinancialTrouble():
		return 0
# ent <<<

	iRantineStrengthTimes100 = pUnit.getCombatAttackTimes100() + pUnit.getCombatDefenseTimes100()

	ltTargetCities = []
	for pyCity in PyPlayer(gc.getBARBARIAN_PLAYER()).getCityList():
		pLoopCity = pyCity.GetCy()
		if pLoopCity.isRevealed(pUnit.getTeam(), False):
			pCityPlot = pLoopCity.plot()
			for iUnitIndex in xrange(pCityPlot.getNumUnits()):
				pLoopUnit = pCityPlot.getUnit(iUnitIndex)
				if pLoopUnit.getOwner() == gc.getBARBARIAN_PLAYER():
					if pLoopUnit.getDomainType() == pUnit.getDomainType():
						if pLoopUnit.getCombatAttackTimes100() + pLoopUnit.getCombatDefenseTimes100() >= iRantineStrengthTimes100:
							break
			else:
				iPathTurns = CyMap().calculatePathDistance(pPlot, pCityPlot)
				if iPathTurns > -1:
					bDiffArea = (pCityPlot.getArea() != pPlot.getArea())
					ltTargetCities.append((bDiffArea, iPathTurns, pLoopCity))

	if len(ltTargetCities) > 0:
		eConvert = gc.getInfoTypeForString('SPELL_CONVERT_CITY_RANTINE')

		ltTargetCities.sort()
		for bDiffArea, iPathTurns, pTargetCity in ltTargetCities:
			pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, pTargetCity.getX(), pTargetCity.getY(), 0, False, False, MissionAITypes.NO_MISSIONAI, pTargetCity.plot(), gc.getPlayer(pUnit.getOwner()).getUnit(-1))
			pUnit.getGroup().pushMission(MissionTypes.MISSION_SPELL, eConvert, -1, 0, False, False, MissionAITypes.NO_MISSIONAI, CyMap().plotByIndex(-1), pPlayer.getUnit(-1))
			return 1
	return 0

def AI_updateAcheron(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()
	pCity = pPlot.getPlotCity()

	if not pUnit.isBarbarian():
		return 0

	if pCity.isNone() or pCity.getOwner() != pUnit.getOwner():
		return 0

	pPlayer = gc.getPlayer(pUnit.getOwner())

	if CyGame().getSorenRandNum(10, "Acheron Roar") < 1:
		eRoar = gc.getInfoTypeForString('SPELL_ROAR')
		if pUnit.canCast(eRoar, False):
			pUnit.getGroup().pushMission(MissionTypes.MISSION_SPELL, eRoar, -1, 0, False, False, MissionAITypes.NO_MISSIONAI, CyMap().plotByIndex(-1), pPlayer.getUnit(-1))
			return 1

	eBreath = gc.getInfoTypeForString('SPELL_BREATH_FIRE')

	if pUnit.canCast(eBreath, False):
		iX = pUnit.getX()
		iY = pUnit.getY()
		for iDX in xrange(iX-2, iX+3, 1):
			for iDY in xrange(iY-2, iY+3, 1):
				pPlot = CyMap().plot(iDX, iDY)
				if not pPlot.isNone() and pPlot.isVisibleEnemyUnit(pUnit.getOwner()):
					pPlayer.AI_setSummonTargetPlot(pPlot)
					pUnit.getGroup().pushMission(MissionTypes.MISSION_SPELL, eBreath, -1, 0, False, False, MissionAITypes.NO_MISSIONAI, CyMap().plotByIndex(-1), pPlayer.getUnit(-1))
					pPlayer.AI_setSummonTargetPlot(CyMap().plotByIndex(-1))
					break

	if pUnit.getGroup().canAnyMove():
		pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, -1, -1, 0, False, False, MissionAITypes.MISSIONAI_GUARD_CITY, pPlot, pPlayer.getUnit(-1))
		return 1

	return 0

def AI_updateSailorsDirge(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	if not pUnit.isBarbarian():
		return 0

	if pPlot.isWater():
		pWaterArea = pPlot.area()
	elif pPlot.isCoastalLand():
		pWaterArea = pPlot.waterArea()
	else:
		return 0

	if not pUnit.hasCargo():
		if CyGame().getSorenRandNum(4, "Sailors Dirge Spawn Crew") < 1:
			cf.spawnSailorsDirgeCrew(pUnit)

	if pUnit.hasCargo():
		if pPlot.isOwned() and pPlot.isAdjacentToLand():
			ltAssaultPlots = []
			for eDirection in xrange(DirectionTypes.NUM_DIRECTION_TYPES):
				pLoopPlot = plotDirection(pPlot.getX(), pPlot.getY(), DirectionTypes(eDirection))
				if not pLoopPlot.isNone():
					if pLoopPlot.isOwned() and not pLoopPlot.isWater():
						iValue = CyGame().getSorenRandNum(10000, "Sailors Dirge Assault Plot")
						if pLoopPlot.isVisibleEnemyUnit(pUnit.getOwner()):
							iValue /= 2
						ltAssaultPlots.append((iValue, pLoopPlot))
			ltAssaultPlots.sort()
			for iValue, pAssaultPlot in ltAssaultPlots:
				pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, pAssaultPlot.getX(), pAssaultPlot.getY(), 0, False, False, MissionAITypes.MISSIONAI_ASSAULT, pAssaultPlot, gc.getPlayer(pUnit.getOwner()).getUnit(-1))
				return 1

	if pUnit.hasCargo():
		ltTargetCities = []
		for ePlayer in xrange(gc.getMAX_CIV_PLAYERS()):
			if gc.getPlayer(ePlayer).isAlive():
				py = PyPlayer(ePlayer)
				for pyCity in PyPlayer(ePlayer).getCityList():
					pLoopCity = pyCity.GetCy()
					if pLoopCity.plot().isAdjacentToArea(pWaterArea):
						ltTargetCities.append((CyGame().getSorenRandNum(10000, "Sailors Dirge City Weight"), pLoopCity))
		ltTargetCities.sort()

		for iWeight, pLoopCity in ltTargetCities:
			pBestCity = pLoopCity
			break
		else:
			return 0

		ltTargetPlots = []
		for iPlotIndex in xrange(1, 37):
			pCityPlot = pBestCity.getCityIndexPlot(iPlotIndex)
			if pCityPlot.getArea() == pWaterArea.getID():
				if pCityPlot.isAdjacentToLand():
					ltTargetPlots.append((CyGame().getSorenRandNum(10000, "Sailors Dirge Plot Weight"), pCityPlot))
		ltTargetPlots.sort()

		MOVE_AVOID_ENEMY_WEIGHT_3 = 2**8	# MOVE_AVOID_ENEMY_WEIGHT_3
		for iWeight, pTargetPlot in ltTargetPlots:
			if CyMap().calculatePathDistance(pPlot, pTargetPlot) > -1:
				pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, pTargetPlot.getX(), pTargetPlot.getY(), MOVE_AVOID_ENEMY_WEIGHT_3, False, False, MissionAITypes.MISSIONAI_ASSAULT, pTargetPlot, gc.getPlayer(pUnit.getOwner()).getUnit(-1))
				return 1
	return 0


# Kaijin >>>
def AI_updateSlave(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	ePlayer = pUnit.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	eCiv = pPlayer.getCivilizationType()

	if eCiv == en.eCivilizationDroaum:
		if pPlayer.isIgnoreFood():
			if pPlot.isCity():
				if pUnit.canCast(gc.getInfoTypeForString('SPELL_ADD_TO_CITY_DROAUM'), False):
					pUnit.cast(gc.getInfoTypeForString('SPELL_ADD_TO_CITY_DROAUM'))
					return 1
			if pUnit.AI_retreatToCity():
				for pyCity in PyPlayer(ePlayer).getCityList():
					pCity = pyCity.GetCy()
					if pUnit.canMoveInto(pCity.plot(), False, False, False):
						if (pCity.happyLevel() - pCity.unhappyLevel(0)) >= 0 and (pCity.goodHealth() - pCity.badHealth(False)) >= 0:
							pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, True, False, MissionAITypes.NO_MISSIONAI, pPlot, pUnit)
							pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, 0, 0, 0, False, False, MissionAITypes.NO_MISSIONAI, pCity.plot(), pUnit)
							pUnit.getGroup().pushMoveToMission(pCity.getX(), pCity.getY())
							pUnit.finishMoves()
							return 1
		if not pPlayer.isFeatAccomplished(FeatTypes.FEAT_GLOBAL_SPELL) and not pPlayer.AI_isFinancialTrouble():
			if pUnit.getUnitAIType() != UnitAITypes.UNITAI_WORKER:
				pUnit.setUnitAIType(UnitAITypes.UNITAI_WORKER)
			return 0

	elif eCiv == en.eCivilizationCualli:
		if pPlot.isCity():
			if pUnit.canCast(gc.getInfoTypeForString('SPELL_SLAVE_IN_THE_PIT'), False):
				pUnit.cast(gc.getInfoTypeForString('SPELL_SLAVE_IN_THE_PIT'))
				return 1
		if pPlayer.isFeatAccomplished(FeatTypes.FEAT_GLOBAL_SPELL):
			if pUnit.AI_retreatToCity():
				eSlavePit = gc.getInfoTypeForString('BUILDING_SLAVE_PIT')
				for pyCity in PyPlayer(ePlayer).getCityList():
					pCity = pyCity.GetCy()
					if pUnit.canMoveInto(pCity.plot(), False, False, False):
						if pCity.getNumBuilding(eSlavePit) > 0:
							if pCity.getFreeSpecialistCount(en.eSpecialistCitizen) < 15:
								pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, True, False, MissionAITypes.NO_MISSIONAI, pPlot, pUnit)
								pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, 0, 0, 0, False, False, MissionAITypes.NO_MISSIONAI, pCity.plot(), pUnit)
								pUnit.getGroup().pushMoveToMission(pCity.getX(), pCity.getY())
								pUnit.finishMoves()
								return 1
		elif not pPlayer.AI_isFinancialTrouble():
			if pUnit.getUnitAIType() != UnitAITypes.UNITAI_WORKER:
				pUnit.setUnitAIType(UnitAITypes.UNITAI_WORKER)
			return 0

	elif eCiv == en.eCivilizationBalseraphs:
		if pPlot.isCity():
			if pUnit.canCast(gc.getInfoTypeForString('SPELL_ADD_TO_FREAK_SHOW'), False):
				pUnit.cast(gc.getInfoTypeForString('SPELL_ADD_TO_FREAK_SHOW'))
				return 1
		if pUnit.AI_retreatToCity():
			eRace = pUnit.getRace()
			eBuilding = gc.getInfoTypeForString('BUILDING_HUMAN_CAGE')
			if eRace == en.eRaceDwarf:
				eBuilding = gc.getInfoTypeForString('BUILDING_DWARF_CAGE')
			elif eRace in en.leRaceElf:
				eBuilding = gc.getInfoTypeForString('BUILDING_ELF_CAGE')
			elif eRace == en.eRaceOrc:
				eBuilding = gc.getInfoTypeForString('BUILDING_ORC_CAGE')
			elif eRace == en.eRaceLizardman:
				eBuilding = gc.getInfoTypeForString('BUILDING_LIZARD_CAGE')

			for pyCity in PyPlayer(ePlayer).getCityList():
				pCity = pyCity.GetCy()
				pCityPlot = pCity.plot()
				if pUnit.canMoveInto(pCityPlot, False, False, False):
					iBaseCulture = pCity.getBaseCommerceRateTimes100(CommerceTypes.COMMERCE_CULTURE)
					if iBaseCulture < 300:
						if pCity.getNumBuilding(eBuilding) == 0:
							pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, True, False, MissionAITypes.NO_MISSIONAI, pPlot, pUnit)
							pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, 0, 0, 0, False, False, MissionAITypes.NO_MISSIONAI, pCity.plot(), pUnit)
							pUnit.getGroup().pushMoveToMission(pCity.getX(), pCity.getY())
							pUnit.finishMoves()
							return 1

	if pPlot.isCity():
		if pUnit.canCast(gc.getInfoTypeForString('SPELL_SLAVE_ADD_CITY_SPECIAL'), False):
			pUnit.cast(gc.getInfoTypeForString('SPELL_SLAVE_ADD_CITY_SPECIAL'))
			return 1

	if pPlayer.getGold() > cyFlatValue(30, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False):
		if pUnit.AI_retreatToCity():
			for pyCity in PyPlayer(ePlayer).getCityList():
				pCity = pyCity.GetCy()
				if pUnit.canMoveInto(pCity.plot(), False, False, False):
					if pCity.getFreeSpecialistCount(en.eSpecialistCitizen) < 5:
						pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, True, False, MissionAITypes.NO_MISSIONAI, pPlot, pUnit)
						pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, 0, 0, 0, False, False, MissionAITypes.NO_MISSIONAI, pCity.plot(), pUnit)
						pUnit.getGroup().pushMoveToMission(pCity.getX(), pCity.getY())
						pUnit.finishMoves()
						return 1

	return 0


def AI_updateCommander(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

# ent >>>
	"""
	ePlayer = pUnit.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	pCapital = pPlayer.getCapitalCity()
	pCapitalPlot = pCapital.plot()

	if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LINEAGE'):
		pTeam = gc.getTeam(pPlayer.getTeam())
		if not pTeam.isHasTech(gc.getInfoTypeForString('TECH_BRONZE_WORKING')):
			pUnit.getGroup().pushMission(MissionTypes.MISSION_DISCOVER, -1, -1, 0, False, False, MissionAITypes.NO_MISSIONAI, CyMap().plotByIndex(-1), pPlayer.getUnit(-1))
			return 1

		bValid = False
		if pUnit.canMoveInto(pCapitalPlot, False, False, False):
			if pPlot.isCity():
				pCity = pPlot.getPlotCity()
				if pCity.isCapital():
					if pUnit.canCast(gc.getInfoTypeForString('SPELL_ADD_TO_CITY_COMMANDER'), False):
						pUnit.cast(gc.getInfoTypeForString('SPELL_ADD_TO_CITY_COMMANDER'))
						bValid = True
						return 1
		elif pUnit.canCast(gc.getInfoTypeForString('SPELL_ADD_TO_CITY_COMMANDER'), False):
			pUnit.cast(gc.getInfoTypeForString('SPELL_ADD_TO_CITY_COMMANDER'))
			bValid = True
			return 1

		if not bValid:

			if pUnit.AI_retreatToCity():
				pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, True, False, MissionAITypes.NO_MISSIONAI, pPlot, pUnit)
				if pUnit.canMoveInto(pCapitalPlot, False, False, False):
					pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, 0, 0, 0, False, False, MissionAITypes.NO_MISSIONAI, pCapitalPlot, pUnit)
					pUnit.getGroup().pushMoveToMission(pCapital.getX(), pCapital.getY())
					pUnit.finishMoves()
					return 1
				else:
					pUnit.getGroup().pushMission(MissionTypes.MISSION_SPELL, gc.getInfoTypeForString('SPELL_RECRUIT'), -1, 0, False, False, MissionAITypes.NO_MISSIONAI, CyMap().plotByIndex(-1), pPlayer.getUnit(-1))
					return 1

	else:
		pUnit.getGroup().pushMission(MissionTypes.MISSION_DISCOVER, -1, -1, 0, False, False, MissionAITypes.NO_MISSIONAI, CyMap().plotByIndex(-1), pPlayer.getUnit(-1))
		return 1
	"""
	ePlayer = pUnit.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	pTeam = gc.getTeam(pPlayer.getTeam())

	leRecommendedTech = [	gc.getInfoTypeForString('TECH_BRONZE_WORKING'),
							gc.getInfoTypeForString('TECH_MILITARY_STRATEGY'),
							gc.getInfoTypeForString('TECH_IRON_WORKING')]
	eDiscoveryTech = pUnit.getDiscoveryTech()
	if eDiscoveryTech in leRecommendedTech:
		if (	pUnit.getDiscoverResearch(eDiscoveryTech) < pTeam.getResearchLeft(eDiscoveryTech) or		# no loss
				pUnit.getDiscoverResearch(eDiscoveryTech) * 2 > pTeam.getResearchCost(eDiscoveryTech)	):	# good job
			pUnit.getGroup().pushMission(MissionTypes.MISSION_DISCOVER, -1, -1, 0, False, False, MissionAITypes.NO_MISSIONAI, CyMap().plotByIndex(-1), pPlayer.getUnit(-1))
			return 1

	if pUnit.getUnitAIType() != UnitAITypes.UNITAI_GENERAL:
		if pTeam.getAtWarCount(True) > 0:
			ltTargetCities = []
			for pyCity in PyPlayer(ePlayer).getCityList():
				pCity = pyCity.GetCy()
				pCityPlot = pCity.plot()
				if pUnit.canMoveInto(pCityPlot, False, False, False) or pUnit.atPlot(pCityPlot):
					iPathTurns = CyMap().calculatePathDistance(pPlot, pCityPlot)
					if iPathTurns > -1:
						iPop = pCity.getPopulation()
						if iPop < 10:
							continue
						bDiffArea = (pCityPlot.getArea() != pPlot.getArea())
						ltTargetCities.append((bDiffArea, -iPop, pCity))
			if len(ltTargetCities) > 0:
				ltTargetCities.sort()
				eSpell = gc.getInfoTypeForString('SPELL_RECRUIT')
				for bDiffArea, iPopMinus, pTargetCity in ltTargetCities:
					pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, pTargetCity.getX(), pTargetCity.getY(), 0, False, False, MissionAITypes.NO_MISSIONAI, pTargetCity.plot(), pPlayer.getUnit(-1))
					pUnit.getGroup().pushMission(MissionTypes.MISSION_SPELL, eSpell, -1, 0, False, False, MissionAITypes.NO_MISSIONAI, CyMap().plotByIndex(-1), pPlayer.getUnit(-1))
					return 1
# ent <<<
	return 0


def AI_updateDefenseOfTheBase(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	ePlayer = pUnit.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	AIType = pUnit.getUnitAIType()
	iThresholdFoundValue = 1000

	if pPlayer.getCivilizationType() == en.eCivilizationLineage:

		if AIType in (UnitAITypes.UNITAI_ATTACK, UnitAITypes.UNITAI_RESERVE):
			if pPlot.getFoundValue(ePlayer) > iThresholdFoundValue:
				if pPlot.isBestAdjacentFound(ePlayer):
					iImprovement = pPlot.getImprovementType()
					if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_SUPPLY_BASE'):

						if pUnit.canCast(gc.getInfoTypeForString('SPELL_PROMOTE_SUPPLY_BASE'), False):
							pUnit.cast(gc.getInfoTypeForString('SPELL_PROMOTE_SUPPLY_BASE'))
							return 1

						lpRangedPlots = cyGetRangedPlots(pPlot, 2, False, False, TeamTypes.NO_TEAM)
						for pTargetPlot in lpRangedPlots:
							if pTargetPlot.isCity():
								break
						else:
							if pPlot.getNumUnits() == 1:
								pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, False, False, MissionAITypes.MISSIONAI_GUARD_BONUS, pUnit.plot(), pUnit)
								return 1
					elif pUnit.canBuild(pPlot, gc.getInfoTypeForString('BUILD_SUPPLY_BASE'), False):
						pUnit.getGroup().pushMission(MissionTypes.MISSION_BUILD, gc.getInfoTypeForString('BUILD_SUPPLY_BASE'), -1, 0, False, False, MissionAITypes.MISSIONAI_BUILD, pUnit.plot(), pUnit)
						return 1

	return 0


def AI_updateGardener(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	ePlayer = pUnit.getOwner()
	pPlayer = gc.getPlayer(ePlayer)

	if pUnit.canCast(gc.getInfoTypeForString('SPELL_PLANT_SACRED_TREE'), False):
		pUnit.cast(gc.getInfoTypeForString('SPELL_PLANT_SACRED_TREE'))
		return 1
	if pPlot.getFeatureType() in (en.eFeatureForest, gc.getInfoTypeForString('FEATURE_FOREST_ANCIENT')):
		iImprovement = pPlot.getImprovementType()
		if iImprovement != ImprovementTypes.NO_IMPROVEMENT:
			if (iImprovement != gc.getInfoTypeForString('IMPROVEMENT_VILLAGE') 
			and iImprovement != gc.getInfoTypeForString('IMPROVEMENT_TOWN') 
			and iImprovement != gc.getInfoTypeForString('IMPROVEMENT_LEAF_VILLAGE') 
			and iImprovement != gc.getInfoTypeForString('IMPROVEMENT_LEAF_TOWN')	):
				if pUnit.canPillage(pPlot):
					pUnit.getGroup().pushMission(MissionTypes.MISSION_PILLAGE, 0, 0, 0, False, False, MissionAITypes.NO_MISSIONAI, pPlot, pUnit)
					pUnit.finishMoves()

	else:
		if pUnit.AI_retreatToCity():
			pBestPlot = -1
			for pyCity in PyPlayer(ePlayer).getCityList():
				pCity = pyCity.GetCy()
				lpRangedPlots = cyGetRangedPlots(pCity.plot(), pCity.getPlotRadius() - 1, False, False, TeamTypes.NO_TEAM)
				for pTargetPlot in lpRangedPlots:
					if pUnit.canMoveInto(pTargetPlot, False, False, False):
						iImprovement = pTargetPlot.getImprovementType()
						if iImprovement == ImprovementTypes.NO_IMPROVEMENT:
							if pTargetPlot.isFlatlands() and not pTargetPlot.isVisibleEnemyUnit(ePlayer):
								if pTargetPlot.getFeatureType() in (en.eFeatureForest, gc.getInfoTypeForString('FEATURE_FOREST_ANCIENT')):
									pBestPlot = pTargetPlot
									break

			if pBestPlot != -1:
				for pyCity in PyPlayer(ePlayer).getCityList():
					pCity = pyCity.GetCy()
					lpRangedPlots = cyGetRangedPlots(pCity.plot(), pCity.getPlotRadius() - 1, False, False, TeamTypes.NO_TEAM)
					for pTargetPlot in lpRangedPlots:
						if pUnit.canMoveInto(pTargetPlot, False, False, False):
							if pUnit.canPillage(pTargetPlot):
								iImprovement = pTargetPlot.getImprovementType()
								if (iImprovement != gc.getInfoTypeForString('IMPROVEMENT_VILLAGE') 
								and iImprovement != gc.getInfoTypeForString('IMPROVEMENT_TOWN') 
								and iImprovement != gc.getInfoTypeForString('IMPROVEMENT_LEAF_VILLAGE') 
								and iImprovement != gc.getInfoTypeForString('IMPROVEMENT_LEAF_TOWN')	):
									if pTargetPlot.isFlatlands() and not pTargetPlot.isVisibleEnemyUnit(ePlayer):
										if pTargetPlot.getFeatureType() in (en.eFeatureForest, gc.getInfoTypeForString('FEATURE_FOREST_ANCIENT')):
											pBestPlot = pTargetPlot
											break

			if pBestPlot != -1:
				pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, True, False, MissionAITypes.NO_MISSIONAI, pPlot, pUnit)
				pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, 0, 0, 0, False, False, MissionAITypes.NO_MISSIONAI, pBestPlot, pUnit)
				pUnit.getGroup().pushMoveToMission(pBestPlot.getX(), pBestPlot.getY())
				pUnit.finishMoves()
				return 1

	return 0


def AI_updateMetatoron(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	##最序盤を過ぎたら首都で隠居
	pPlayer = gc.getPlayer(pUnit.getOwner())
	iGameProgress = pPlayer.getGameProgressPercent()
	if iGameProgress <= 8:
		if pUnit.getUnitAIType() == UnitAITypes.UNITAI_RESERVE:
			pUnit.setUnitAIType(UnitAITypes.UNITAI_ATTACK)
		return 0

	if pUnit.getUnitAIType() != UnitAITypes.UNITAI_RESERVE:
		pUnit.setUnitAIType(UnitAITypes.UNITAI_RESERVE)
	if pUnit.getDamage() > 0:
		return 0

	pCapitalCity = pPlayer.getCapitalCity()
	if not pCapitalCity.isNone():
		if not pUnit.at(pCapitalCity.getX(), pCapitalCity.getY()):
			pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, pCapitalCity.getX(), pCapitalCity.getY(), 0, False, False, MissionAITypes.NO_MISSIONAI, pCapitalCity.plot(), pPlayer.getUnit(-1))
		pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, True, False, MissionAITypes.NO_MISSIONAI, pPlot, pUnit)
		return 1

	return 0


def AI_updateAdeptus(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	ePlayer = pUnit.getOwner()

	if pUnit.canBuild(pPlot, gc.getInfoTypeForString('BUILD_REFINERY'), False):
		pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, True, False, MissionAITypes.NO_MISSIONAI, pPlot, pUnit)
		pUnit.getGroup().pushMission(MissionTypes.MISSION_BUILD, gc.getInfoTypeForString('BUILD_REFINERY'), -1, 0, False, False, MissionAITypes.MISSIONAI_BUILD, pPlot, pUnit)
		return 1
	elif pUnit.canCast(gc.getInfoTypeForString('SPELL_DISPEL_MAGIC'), False):
		pUnit.cast(gc.getInfoTypeForString('SPELL_DISPEL_MAGIC'))
		return 1

	else:
		if pUnit.AI_retreatToCity():
			pBestPlot = -1
			iBestPlot = 0

			for i in xrange (CyMap().numPlots()):
				pLoopPlot = CyMap().plotByIndex(i)
				iPlot = 0
				iImprovement = pLoopPlot.getImprovementType()
				iBonus = pLoopPlot.getBonusType(TeamTypes.NO_TEAM)
				if pLoopPlot.getOwner() == ePlayer:
					if pPlot.getArea() == pLoopPlot.getArea():
						if pUnit.canMoveInto(pLoopPlot, False, False, False):
							if pLoopPlot.isVisibleEnemyUnit(ePlayer) == False:
								if iBonus == gc.getInfoTypeForString('BONUS_MANA'):
									iPlot += 1
									if iImprovement == ImprovementTypes.NO_IMPROVEMENT:
										iPlot += 5
									for iUnitIndex in xrange(pLoopPlot.getNumUnits()):
										pPlotUnit = pLoopPlot.getUnit(iUnitIndex)
										if pPlotUnit.getUnitType() in (gc.getInfoTypeForString('UNIT_ADEPTUS'), gc.getInfoTypeForString('UNIT_TECHPRIEST')):
											if iPlot > 0:
												iPlot = -1

								elif iBonus in g_leManaTypes:
									iPlot += 5
									if iImprovement != ImprovementTypes.NO_IMPROVEMENT:
										if gc.getImprovementInfo(iImprovement).isPermanent():
											iPlot -= 5
									for iUnitIndex in xrange(pLoopPlot.getNumUnits()):
										pPlotUnit = pLoopPlot.getUnit(iUnitIndex)
										if pPlotUnit.getUnitType() in (gc.getInfoTypeForString('UNIT_ADEPTUS'), gc.getInfoTypeForString('UNIT_TECHPRIEST')):
											if iPlot > 0:
												iPlot = -1

				if iPlot > iBestPlot:
					iBestPlot = iPlot
					pBestPlot = pLoopPlot

			if pBestPlot != -1:
				pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, True, False, MissionAITypes.NO_MISSIONAI, pPlot, pUnit)
				pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, 0, 0, 0, False, False, MissionAITypes.NO_MISSIONAI, pBestPlot, pUnit)
				pUnit.getGroup().pushMoveToMission(pBestPlot.getX(), pBestPlot.getY())
				pUnit.finishMoves()
				return 1

	return 0


def AI_updateAwakened(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	ePlayer = pUnit.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	iCasterID = pUnit.getID()
	eSpell = gc.getInfoTypeForString('SPELL_SCIONS_ADD_POPULATION')
	iNumCities = pPlayer.getNumCities()

	# 定住可能な都市への割り振り
	def doAllocation():
		# 人口が一定未満の都市に優先して定住
		iWorstPop = 6
		pWorstCity = -1
		for pyCity in PyPlayer(ePlayer).getCityList():
			pCity = pyCity.GetCy()
			if cf.doAddPopValid(pCity):
				pCityPlot = pCity.plot()
				if pUnit.canMoveInto(pCityPlot, False, False, False) or pUnit.atPlot(pCityPlot):
					iPop = pCity.getPopulation()
					iPathTurns = CyMap().calculatePathDistance(pPlot, pCityPlot)
					if iPathTurns > -1:
						if iPop < iWorstPop:
							iWorstPop = iPop
							pWorstCity = pCity
		if pWorstCity != -1:
			if cf.doMovePlotAndCastSpell(pUnit, pWorstCity.plot() , eSpell):
				return True

		# 今いる都市に定住
		if pPlot.isCity():
			pCity = pPlot.getPlotCity()
			if cf.doAddPopValid(pCity):
				if cf.doMovePlotAndCastSpell(pUnit, pCity.plot(), eSpell):
					return True

		# 定住可能な都市にID順に向かう
		for pyCity in PyPlayer(ePlayer).getCityList():
			pCity = pyCity.GetCy()
			if cf.doAddPopValid(pCity):
				pCityPlot = pCity.plot()
				if pUnit.canMoveInto(pCityPlot, False, False, False) or pUnit.atPlot(pCityPlot):
					if cf.doMovePlotAndCastSpell(pUnit, pCity.plot(), eSpell):
						return True

		return False

	# 産み出す都市には優先して定住
	if pPlot.isCity():
		pCity = pPlot.getPlotCity()
		if cf.doAddPopValid(pCity):
			if pCity.getPopulation() < iNumCities * 2 and CyGame().getSorenRandNum(100, "Priority") < 60:
				if cf.doMovePlotAndCastSpell(pUnit, pCity.plot(), eSpell):
					return 1

	# 都市がある程度揃ったら平均人口が一定以上になるまでは定住優先
	# 開拓者のコストは都市数に応じて上昇（マップサイズが大きいほど緩やかに上昇）するため
	iTargetCities = pPlayer.getMaxCities()
	if iTargetCities == -1:
		iTargetCities = gc.getWorldInfo(CyMap().getWorldSize()).getTargetNumCities()
	if ((iNumCities >= iTargetCities     and pPlayer.getAveragePopulation() < 10) or
		(iNumCities >= iTargetCities / 2 and pPlayer.getAveragePopulation() < 6)):
		if doAllocation():
			return 1

	# 覚醒者は都市出しを目的に生産されることを想定して基本的に「開拓者」として行動
	if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_AWAKENED'):
		for iUnitIndex in xrange(pPlot.getNumUnits()):
			pLoopUnit = pPlot.getUnit(iUnitIndex)
			if pLoopUnit.getOwner() == ePlayer:
				if pLoopUnit.getID() != iCasterID:
					if pLoopUnit.getUnitAIType() == UnitAITypes.UNITAI_SETTLE:
						break
		else:
			return 0
	else:
	# 再誕者も護衛の受け皿となるユニットが存在するなら「開拓者」として行動
		bValid = False
		for iUnitIndex in xrange(pPlot.getNumUnits()):
			pLoopUnit = pPlot.getUnit(iUnitIndex)
			if pLoopUnit.getOwner() == ePlayer:
				if pLoopUnit.getID() != iCasterID:
					if pLoopUnit.getUnitAIType() == UnitAITypes.UNITAI_SETTLE:
						bValid = False
						break
					if pLoopUnit.getUnitAIType() == UnitAITypes.UNITAI_ESCORT:
						bValid = True
		if bValid:
			return 0

	if doAllocation():
		return 1

	return 0


	"""
def AI_updatePelemoc(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	ePlayer = pUnit.getOwner()
	pPlayer = gc.getPlayer(ePlayer)

	if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SCIONS'):
		if pUnit.canCast(gc.getInfoTypeForString('SPELL_SCIONS_SUCCOR'), False):
			pUnit.cast(gc.getInfoTypeForString('SPELL_SCIONS_SUCCOR'))
			return 1

		else:

			if pUnit.AI_retreatToCity():
				for eLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
					pLoopPlayer = gc.getPlayer(eLoopPlayer)
					if pLoopPlayer.isAlive():
						if eLoopPlayer != ePlayer:
							for pyCity in PyPlayer(eLoopPlayer).getCityList():
								pCity = pyCity.GetCy()
								if pUnit.canMoveInto(pCity.plot(), False, False, False):
									if not pCity.goodHealth() - pCity.badHealth(False) > -2:
										pTeam = gc.getTeam(pUnit.getTeam())
										if not pTeam.isAtWar(pCity.getTeam()):
											pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, True, False, MissionAITypes.NO_MISSIONAI, pPlot, pUnit)
											pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, 0, 0, 0, False, False, MissionAITypes.NO_MISSIONAI, pCity.plot(), pUnit)
											pUnit.getGroup().pushMoveToMission(pCity.getX(), pCity.getY())
											pUnit.finishMoves()
											return 1

	return 0
	"""


def AI_updateEin(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	eRecruit = gc.getInfoTypeForString('SPELL_MERCENARIES_RECRUIT')
	if pPlot.isCity():
		if pUnit.canCast(eRecruit, False):
			pUnit.cast(eRecruit)
			return 1

	if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MERCENARIES_RECRUITER')):
		pPlayer = gc.getPlayer(pUnit.getOwner())
		if pPlayer.getGold() > cyFlatValue(500, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False):
			if pUnit.AI_retreatToCity():
				pUnit.getGroup().pushMission(MissionTypes.MISSION_SPELL, eRecruit, -1, 0, False, False, MissionAITypes.NO_MISSIONAI, CyMap().plotByIndex(-1), pPlayer.getUnit(-1))
				return 1

	return 0


def AI_updateElementDestroyer(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	ePlayer = pUnit.getOwner()
	pPlayer = gc.getPlayer(ePlayer)

	pBestPlot = -1
	iBestPlot = 0

	for iPlotIndex in xrange(CyMap().numPlots()):
		pLoopPlot = CyMap().plotByIndex(iPlotIndex)
		iPlot = 0

		if pPlot.getX() == pLoopPlot.getX() and pPlot.getY() == pLoopPlot.getY():
			continue

		if pLoopPlot.getOwner() == ePlayer:
			iPlot -= 500

		if pPlot.getArea() != pLoopPlot.getArea():
			iPlot += 50

		lpRangedPlots = cyGetRangedPlots(pLoopPlot, pUnit.nukeRange(), False, False, TeamTypes.NO_TEAM)
		for pTargetPlot in lpRangedPlots:
			if pPlot.getX() == pTargetPlot.getX() and pPlot.getY() == pTargetPlot.getY():
				iPlot = 0
				break

			if pTargetPlot.getOwner() != ePlayer:
				iPlot += 5
				if pTargetPlot.isCity():
					iPlot += 45
					pCity = pTargetPlot.getPlotCity()
					iPlot += (int(pCity.getPopulation()) * 3)
			else:
				if pTargetPlot.isCity():
					iPlot -= 50
					pCity = pTargetPlot.getPlotCity()
					iPlot -= (int(pCity.getPopulation()) * 5)
					if pCity.isCapital():
						iPlot = 0
						break
			if pTargetPlot.isVisibleEnemyUnit(ePlayer):
				for iUnitIndex in xrange(pTargetPlot.getNumUnits()):
					pPlotUnit = pTargetPlot.getUnit(iUnitIndex)
					if pPlotUnit.getOwner() != ePlayer:
						iPlot += 1
						if isWorldUnitClass(pPlotUnit.getUnitClassType()):
							iPlot += 5
					else:
						iPlot -= 1

		if iPlot > iBestPlot:
			iBestPlot = iPlot
			pBestPlot = pLoopPlot

	if pBestPlot != -1:
		eTeam = pPlayer.getTeam()
		pTeam = gc.getTeam(eTeam)
		for eLoopTeam in xrange(gc.getMAX_CIV_TEAMS()):
			if eLoopTeam != eTeam:
				pLoopTeam = gc.getTeam(eLoopTeam)
				if pLoopTeam.isAlive() and not pLoopTeam.isAVassal():
					pTeam.declareWar(eLoopTeam, False, WarPlanTypes.WARPLAN_TOTAL)
		pUnit.getGroup().pushMission(MissionTypes.MISSION_NUKE, pBestPlot.getX(), pBestPlot.getY(), 0, False, False, MissionAITypes.NO_MISSIONAI, pBestPlot, pPlayer.getUnit(-1))
		return 1

	return 0


def AI_updateBasque(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

#	ePlayer = pUnit.getOwner()
#	pPlayer = gc.getPlayer(ePlayer)

	if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BASQUE')):
		pUnit.setUnitAIType(UnitAITypes.UNITAI_UNKNOWN)
		pUnit.getGroup().pushMission(MissionTypes.MISSION_SEAPATROL, 0, 0, 0, False, False, MissionAITypes.NO_MISSIONAI, pPlot, pUnit)
		return 1
	"""
	if pUnit.canCast(gc.getInfoTypeForString('SPELL_ARMED_FISHING_BOATS'), False):
		pUnit.cast(gc.getInfoTypeForString('SPELL_ARMED_FISHING_BOATS'))
		return 1
	if pUnit.canCast(gc.getInfoTypeForString('SPELL_ARMED_WHALING_BOATS'), False):
		pUnit.cast(gc.getInfoTypeForString('SPELL_ARMED_WHALING_BOATS'))
		return 1

	pBestPlot = None
	for pyCity in PyPlayer(ePlayer).getCityList():
		pCity = pyCity.GetCy()
		lpRangedPlots = cyGetRangedPlots(pPlot, pCity.getPlotRadius(), False, False, TeamTypes.NO_TEAM)
		for pTargetPlot in lpRangedPlots:
			if pTargetPlot.isWater() and not pTargetPlot.isVisibleEnemyUnit(ePlayer):
				if pUnit.canMoveInto(pTargetPlot, False, False, False):
					bValid = False
					if pTargetPlot.canHaveImprovement(gc.getInfoTypeForString('IMPROVEMENT_FISHING_BOATS'), ePlayer, False):
						if pPlayer.canBuild(pTargetPlot, gc.getInfoTypeForString('BUILD_FISHING_BOATS'), False, False):
							bValid = True
					if pTargetPlot.canHaveImprovement(gc.getInfoTypeForString('IMPROVEMENT_WHALING_BOATS'), ePlayer, False):
						if pPlayer.canBuild(pTargetPlot, gc.getInfoTypeForString('BUILD_WHALING_BOATS'), False, False):
							bValid = True
					if bValid:
						if pTargetPlot.getImprovementType() == ImprovementTypes.NO_IMPROVEMENT:
							iArmedBoats = 0
							for iUnitIndex in xrange(pTargetPlot.getNumUnits()):
								pPlotUnit = pTargetPlot.getUnit(iUnitIndex)
								if pPlotUnit.getUnitType() == gc.getInfoTypeForString('UNIT_BASQUE'):
									iArmedBoats += 1
							if iArmedBoats == 0:
								pBestPlot = pTargetPlot
								break
	if pBestPlot is not None:
		pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, True, False, MissionAITypes.NO_MISSIONAI, pPlot, pUnit)
		pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, 0, 0, 0, False, False, MissionAITypes.NO_MISSIONAI, pBestPlot, pUnit)
		pUnit.getGroup().pushMoveToMission(pBestPlot.getX(), pBestPlot.getY())
		pUnit.finishMoves()
		return 1
	"""
	return 0

# Kaijin <<<
# ent OAC >>>
def AI_updateFalamar(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	ePlayer = pUnit.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	eTeam = pUnit.getTeam()
	pTeam = gc.getTeam(eTeam)

	if pUnit.getDelayedSpell() != SpellTypes.NO_SPELL:
		return 0
	if pTeam.getAnyWarPlanCount(True) > 0:
		return 0
	if pUnit.getDamage() > 0:
		return 0
	if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_FATIGUED2')):
		return 0
	
	ltTargetCities = []
	for eLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
		pLoopPlayer = gc.getPlayer(eLoopPlayer)
		if pLoopPlayer.isAlive() and eTeam != pLoopPlayer.getTeam():
			if pLoopPlayer.AI_getAttitude(ePlayer) == AttitudeTypes.ATTITUDE_FRIENDLY:
				continue
			for pyCity in PyPlayer(eLoopPlayer).getCityList():
				pLoopCity = pyCity.GetCy()
				if pLoopCity.isRevealed(eTeam, False):
					pCityPlot = pLoopCity.plot()
					if pUnit.canMoveInto(pCityPlot, False, False, False):
						iPathTurns = CyMap().calculatePathDistance(pPlot, pCityPlot)
						if iPathTurns > -1:
							ltTargetCities.append((iPathTurns, pLoopCity))
	if len(ltTargetCities) > 0:
		ltTargetCities.sort()
		eSpell = gc.getInfoTypeForString('SPELL_HOSPITABLE')
		for iPathTurns, pTargetCity in ltTargetCities:
			pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, pTargetCity.getX(), pTargetCity.getY(), 0, False, False, MissionAITypes.NO_MISSIONAI, pTargetCity.plot(), pPlayer.getUnit(-1))
			pUnit.getGroup().pushMission(MissionTypes.MISSION_SPELL, eSpell, -1, 0, False, False, MissionAITypes.NO_MISSIONAI, CyMap().plotByIndex(-1), pPlayer.getUnit(-1))
			return 1

	return 0


def AI_updateBarnaxus(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	##昇進したら首都で隠居
	if not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT3')):
		if pUnit.getUnitAIType() == UnitAITypes.UNITAI_RESERVE:
			pUnit.setUnitAIType(UnitAITypes.UNITAI_ATTACK)
		return 0
	if pUnit.getUnitAIType() != UnitAITypes.UNITAI_RESERVE:
		pUnit.setUnitAIType(UnitAITypes.UNITAI_RESERVE)
	if pUnit.getDamage() > 0:
		return 0
	pPlayer = gc.getPlayer(pUnit.getOwner())
	pCapitalCity = pPlayer.getCapitalCity()
	if not pCapitalCity.isNone():
		if not pUnit.at(pCapitalCity.getX(), pCapitalCity.getY()):
			pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, pCapitalCity.getX(), pCapitalCity.getY(), 0, False, False, MissionAITypes.NO_MISSIONAI, pCapitalCity.plot(), pPlayer.getUnit(-1))
		pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, True, False, MissionAITypes.NO_MISSIONAI, pPlot, pUnit)
		return 1

	return 0


def AI_updateDamien(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	if not pUnit.isImmortal():
		return 0

	eUnitAI = pUnit.getUnitAIType()
	pTeam = gc.getTeam(pUnit.getTeam())
	
	if pTeam.getAnyWarPlanCount(True) > 0:
		if eUnitAI == UnitAITypes.UNITAI_EXPLORE:
			pUnit.setUnitAIType(UnitAITypes.UNITAI_ATTACK_CITY)
		return 0

	if eUnitAI != UnitAITypes.UNITAI_EXPLORE:
		pUnit.setUnitAIType(UnitAITypes.UNITAI_EXPLORE)

	return 0


def AI_updateCouncilor(argsList):
#Melante, Pelemoc, Themoch and Alcinus
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	ePlayer = pUnit.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	eTeam = pUnit.getTeam()
	pTeam = gc.getTeam(eTeam)
	eUnitType = pUnit.getUnitType()
	ePelemoc = gc.getInfoTypeForString('UNIT_PELEMOC')
	eThemoch = gc.getInfoTypeForString('UNIT_THEMOCH')
	eAlcinus = gc.getInfoTypeForString('UNIT_ALCINUS')
	eMelante = gc.getInfoTypeForString('UNIT_MELANTE')

	if eUnitType == eMelante:
		if pPlayer.isFeatAccomplished(FeatTypes.FEAT_GLOBAL_SPELL):
			return 0
		if pPlot.isCity():
			eSpell = gc.getInfoTypeForString('SPELL_MELANTE_RESIDENCE')
			if pUnit.canCast(eSpell, False):
				pUnit.cast(eSpell)
				return 1
		pCapital = pPlayer.getCapitalCity()
		pUnit.getGroup().pushMoveToMission(pCapital.getX(), pCapital.getY())
		return 1
	elif eUnitType == eAlcinus:
		if pPlot.isCity():
			eSpell = gc.getInfoTypeForString('SPELL_THAUMATURGE_KEEP')
			if pUnit.canCast(eSpell, False):
				pUnit.cast(eSpell)
				return 1
		if pTeam.getAtWarCount(True) > 0:
			return 0

	if not pPlayer.isFeatAccomplished(FeatTypes.FEAT_GLOBAL_SPELL):
		bPelemocPresent = False
		bThemochPresent = False
		bAlcinusPresent = False
		bMelantePresent = False
		pMelantePlot = -1
		for pLoopUnit in PyPlayer(ePlayer).getUnitList():
			eLoopUnitType = pLoopUnit.getUnitType()
			if eLoopUnitType == ePelemoc:
				if pLoopUnit.getDelayedSpell() == SpellTypes.NO_SPELL:
					bPelemocPresent = True
			elif eLoopUnitType == eThemoch:
				bThemochPresent = True
			elif eLoopUnitType == eAlcinus:
				bAlcinusPresent = True
			elif eLoopUnitType == eMelante:
				bMelantePresent = True
				pMelantePlot = pLoopUnit.plot()
		if bPelemocPresent and bThemochPresent and bAlcinusPresent and bMelantePresent and pMelantePlot != -1:
			pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, pMelantePlot.getX(), pMelantePlot.getY(), 0, False, False, MissionAITypes.NO_MISSIONAI, pMelantePlot, pPlayer.getUnit(-1))
			return 1

	if eUnitType == ePelemoc:
		if pUnit.getDelayedSpell() != SpellTypes.NO_SPELL:
			return 0
		eSpell = gc.getInfoTypeForString('SPELL_SCIONS_SUCCOR')
		ltTargetCities = []
		for eLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
			pLoopPlayer = gc.getPlayer(eLoopPlayer)
			if pLoopPlayer.isAlive() and ePlayer != eLoopPlayer:
				for pyCity in PyPlayer(eLoopPlayer).getCityList():
					pLoopCity = pyCity.GetCy()
					if pLoopCity.isRevealed(eTeam, False):
						pCityPlot = pLoopCity.plot()
						if pUnit.canMoveInto(pCityPlot, False, False, False) or pUnit.atPlot(pCityPlot):
							iPathTurns = CyMap().calculatePathDistance(pPlot, pCityPlot)
							if iPathTurns > -1:
								bSameArea = (pCityPlot.getArea() == pPlot.getArea())
								iGetPopulation = max(1, pLoopCity.getPopulation() // 5)
								iGetPopulation = iGetPopulation * 10 - iPathTurns
								ltTargetCities.append((bSameArea, iGetPopulation, pLoopCity))
		if len(ltTargetCities) > 0:
			ltTargetCities.sort()
			ltTargetCities.reverse()
			for bSameArea, iGetPopulation, pTargetCity in ltTargetCities:
				if cf.doMovePlotAndCastSpell(pUnit, pTargetCity.plot(), eSpell):
					return 1

	return 0


def AI_updateContractWar(argsList):
#Louisa, Steindorf, Smiley
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	ePlayer = pUnit.getOwner()
	pPlayer = gc.getPlayer(ePlayer)
	ePlayerTeam = pPlayer.getTeam()
	pPlayerTeam = gc.getTeam(ePlayerTeam)
	eUnitType = pUnit.getUnitType()
	eLouisa = gc.getInfoTypeForString('UNIT_LOUISA')

	if pPlayer.getCivilizationType() != gc.getInfoTypeForString('CIVILIZATION_TIGER'):
		return 0

	#契約戦争中のルイーザ
	if pPlayer.getGuildPlusCounter(50):
		if eUnitType != eLouisa:
			return 0
		eContractor = pPlayer.getGuildPlusCounter(52)
		pContractor = gc.getPlayer(eContractor)
		eContractorTeam = pContractor.getTeam()
		pContractorTeam = gc.getTeam(eContractorTeam)
		iGold = pPlayer.getGold()
		rate = gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent()

		if pUnit.getDamage() > 0:
			return 0

		#雇い国が負けすぎているなら最大の敵に賄賂 (自国がやばい場合は契約の破棄で対応)
		eSpell = gc.getInfoTypeForString('SPELL_MERCENARIES_BRIBE')
		iCost =  cyFlatValue(200, rate, False)
		iRatio = cf.AI_getWarSuccessCapitulationRatio(eContractor)
		if iGold >= iCost and iRatio < -50:
			#最大の敵を検索
			eWorstEnemyTeam = -1
			iWorstSuccessRatio = 0
			iNum = pPlayer.getGuildPlusCounter(59)
			for iIndex in xrange(iNum):
				eEnemy = pPlayer.getGuildPlusCounter(60 + iIndex)
				if eEnemy != -1:
					pEnemy = gc.getPlayer(eEnemy)
					if pEnemy.isAlive():
						eEnemyTeam = pEnemy.getTeam()
						pEnemyTeam = gc.getTeam(eEnemyTeam)
						if not pEnemyTeam.isAVassal() and pEnemyTeam.isAtWar(eContractorTeam):
							iSuccessRatio = pContractorTeam.AI_getWarSuccess(eEnemyTeam) - pEnemyTeam.AI_getWarSuccess(eContractorTeam)
							if iSuccessRatio < iWorstSuccessRatio:
								iWorstSuccessRatio = iSuccessRatio
								eWorstEnemyTeam = eEnemyTeam

			if eWorstEnemyTeam != -1:
				#実行に適したタイルを検索
				ltTargetPlots = []
				for eWorstEnemy in xrange(gc.getMAX_CIV_PLAYERS()):
					pWorstEnemy = gc.getPlayer(eWorstEnemy)
					if pWorstEnemy.isAlive() and pWorstEnemy.getTeam() == eWorstEnemyTeam:
						for pyCity in PyPlayer(eWorstEnemy).getCityList():
							pLoopCity = pyCity.GetCy()
							if pLoopCity.isRevealed(ePlayerTeam, False):
								pCityPlot = pLoopCity.plot()
								for eDirection in xrange(DirectionTypes.NUM_DIRECTION_TYPES):
									pAdjacentCityPlot = plotDirection(pCityPlot.getX(), pCityPlot.getY(), DirectionTypes(eDirection))
									if not pAdjacentCityPlot.isNone():
										if pUnit.canMoveInto(pAdjacentCityPlot, False, False, False):
											iPathTurns = CyMap().calculatePathDistance(pPlot, pAdjacentCityPlot)
											if iPathTurns > -1:
												bDiffArea = (pAdjacentCityPlot.getArea() != pPlot.getArea())
												ltTargetPlots.append((bDiffArea, iPathTurns, pAdjacentCityPlot))
				#実行のために移動
				if len(ltTargetPlots) > 0:
					ltTargetPlots.sort()
					for bDiffArea, iPathTurns, pTargetPlot in ltTargetPlots:
						pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, pTargetPlot.getX(), pTargetPlot.getY(), 0, False, False, MissionAITypes.NO_MISSIONAI, pTargetPlot, pPlayer.getUnit(-1))
						pUnit.getGroup().pushMission(MissionTypes.MISSION_SPELL, eSpell, -1, 0, False, False, MissionAITypes.NO_MISSIONAI, CyMap().plotByIndex(-1), pPlayer.getUnit(-1))
						return 1

		#雇い主が勝ちすぎているなら第3国をけしかける
		eSpell = gc.getInfoTypeForString('SPELL_MERCENARIES_INCITEMENT')
		iCost =  cyFlatValue(500, rate, False)
		iRatio = cf.AI_getWarSuccessCapitulationRatio(eContractor)
		if iGold >= iCost and iRatio > 50:
			ltTargetCities = []
			for eOtherPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
				pOtherPlayer = gc.getPlayer(eOtherPlayer)
				if pOtherPlayer.isAlive():
					eOtherTeam = pOtherPlayer.getTeam()
					pOtherTeam = gc.getTeam(eOtherTeam)
					if eOtherTeam in (ePlayerTeam, eContractorTeam):
						continue
					if pOtherTeam.isAtWar(eContractorTeam) or pOtherTeam.isAtWar(ePlayerTeam):
						continue
					if pOtherTeam.isAVassal():
						continue
					if not pOtherTeam.canDeclareWar(eContractorTeam):
						continue
					for pyCity in PyPlayer(eOtherPlayer).getCityList():
						pLoopCity = pyCity.GetCy()
						if pLoopCity.isRevealed(ePlayerTeam, False):
							pCityPlot = pLoopCity.plot()
							if pUnit.canMoveInto(pCityPlot, False, False, False) or pUnit.atPlot(pCityPlot):
								iPathTurns = CyMap().calculatePathDistance(pPlot, pCityPlot)
								if iPathTurns > -1:
									bDiffArea = (pCityPlot.getArea() != pPlot.getArea())
									ltTargetCities.append((bDiffArea, iPathTurns, pLoopCity))

			if len(ltTargetCities) > 0:
				ltTargetCities.sort()
				for bDiffArea, iPathTurns, pTargetCity in ltTargetCities:
					pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, pTargetCity.getX(), pTargetCity.getY(), 0, False, False, MissionAITypes.NO_MISSIONAI, pTargetCity.plot(), pPlayer.getUnit(-1))
					pUnit.getGroup().pushMission(MissionTypes.MISSION_SPELL, eSpell, -1, 0, False, False, MissionAITypes.NO_MISSIONAI, CyMap().plotByIndex(-1), pPlayer.getUnit(-1))
					return 1

		#首都で待機
		pCapitalCity = pPlayer.getCapitalCity()
		if not pCapitalCity.isNone():
			if not pUnit.at(pCapitalCity.getX(), pCapitalCity.getY()):
				pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, pCapitalCity.getX(), pCapitalCity.getY(), 0, False, False, MissionAITypes.NO_MISSIONAI, pCapitalCity.plot(), pPlayer.getUnit(-1))
			return 1
		return 0

	if not pPlayerTeam.isHasTech(gc.getInfoTypeForString('TECH_CURRENCY')):
		return 0
	if pPlayerTeam.getAtWarCount(True) > 0:
		return 0
	if pPlayerTeam.isAVassal():
		return 0
	#ルイーザ優先
	if eUnitType != eLouisa:
		bLouisaPresent = False
		for pLoopUnit in PyPlayer(ePlayer).getUnitList():
			eLoopUnitType = pLoopUnit.getUnitType()
			if eLoopUnitType == eLouisa:
				bLouisaPresent = True
				break
		if bLouisaPresent:
			return 0

	#契約開戦
	eSpell = gc.getInfoTypeForString('SPELL_OUTBREAK_CONTRACTS')
	ltTargetCities = []
	for eContractor in xrange(gc.getMAX_CIV_PLAYERS()):
		pContractor = gc.getPlayer(eContractor)
		if not pContractor.isAlive():
			continue
		eContractorTeam = pContractor.getTeam()
		if eContractorTeam == ePlayerTeam:
			continue
		pContractorTeam = gc.getTeam(eContractorTeam)
		if pContractorTeam.getAtWarCount(True) == 0:
			continue
		if pContractorTeam.isAVassal():
			continue
		if pContractor.AI_getAttitude(ePlayer) < AttitudeTypes.ATTITUDE_CAUTIOUS:
			continue
		if pPlayer.AI_getAttitude(eContractor) < AttitudeTypes.ATTITUDE_PLEASED:
			continue

		iEnemyPower = 0
		bValid = False
		for eOtherTeam in xrange(gc.getMAX_CIV_TEAMS()):
			pOtherTeam = gc.getTeam(eOtherTeam)
			if pOtherTeam.isAlive() and not eOtherTeam in (ePlayerTeam, eContractorTeam):
				if pContractorTeam.isAtWar(eOtherTeam) and not pPlayerTeam.isAtWar(eOtherTeam):
					for eLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
						pLoopPlayer = gc.getPlayer(eLoopPlayer)
						if pLoopPlayer.isAlive() and pLoopPlayer.getTeam() == eOtherTeam:
							if pPlayer.AI_getAttitude(eLoopPlayer) == AttitudeTypes.ATTITUDE_FRIENDLY:
								bValid = True
								break
							iEnemyPower += pLoopPlayer.getPower()

		if bValid:
			continue
		iPowerRatio = pContractorTeam.getPower(True) + 2 * pPlayerTeam.getPower(True) - 2 * iEnemyPower
		if iPowerRatio < 0:
			continue
		pCapitalCity = pContractor.getCapitalCity()
		if pCapitalCity.isRevealed(ePlayerTeam, False):
			pCapitalPlot = pCapitalCity.plot()
			if pUnit.canMoveInto(pCapitalPlot, False, False, False) or pUnit.atPlot(pCapitalPlot):
				iPathTurns = CyMap().calculatePathDistance(pPlot, pCapitalPlot)
				if iPathTurns > -1:
					bDiffArea = (pCapitalPlot.getArea() != pPlot.getArea())
					ltTargetCities.append((bDiffArea, -iPowerRatio, iPathTurns, pCapitalCity))

	if len(ltTargetCities) > 0:
		ltTargetCities.sort()
		for bDiffArea, iPowerRatio, iPathTurns, pTargetCity in ltTargetCities:
			pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, pTargetCity.getX(), pTargetCity.getY(), 0, False, False, MissionAITypes.NO_MISSIONAI, pTargetCity.plot(), pPlayer.getUnit(-1))
			pUnit.getGroup().pushMission(MissionTypes.MISSION_SPELL, eSpell, -1, 0, False, False, MissionAITypes.NO_MISSIONAI, CyMap().plotByIndex(-1), pPlayer.getUnit(-1))
			return 1

	return 0


def AI_updateMokka(argsList):
	pUnit = argsList[0]
	pPlot = pUnit.plot()

	if pUnit.getCivilizationType() == en.eCivilizationFrostling:
		if pPlot.isOwned():
			pOwner = gc.getPlayer(pPlot.getOwner())
			if pOwner.getCivilizationType() == en.eCivilizationNival:
				eTeam = pPlot.getTeam()
				if not pUnit.isEnemy(eTeam, pPlot):
					pNewUnit = pOwner.initSkeletalUnit(pUnit.getUnitType(), pUnit.getX(), pUnit.getY(), pUnit.getUnitAIType());
					pNewUnit.convert(pUnit)
					pNewUnit.changeImmobileTimer(1)
					return 1

	return 0


def AI_updateBarbarian(argsList):
# Lizardman and WolfRider
	pUnit = argsList[0]

	if pUnit.isBarbarian():
		eUnitType = pUnit.getUnitType()
		eUnitAI = pUnit.getUnitAIType()
		iGameTurn = CyGame().getGameTurn()
		iOrthusTurn = cyFlatValue(75, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
		if iGameTurn < iOrthusTurn:
			if eUnitAI != UnitAITypes.UNITAI_ANIMAL:
				pUnit.setUnitAIType(UnitAITypes.UNITAI_ANIMAL)
		else:
			if eUnitAI == UnitAITypes.UNITAI_ANIMAL:
				pUnit.setUnitAIType(gc.getUnitInfo(eUnitType).getDefaultUnitAIType())

	return 0


def AI_updateAnimal(argsList):
# Animals that can Construct Building
	pUnit = argsList[0]

	if pUnit.isBarbarian():
		return 0
	if pUnit.getUnitAIType() == UnitAITypes.UNITAI_ATTACK:
		if pUnit.getDamage() > 0:
			return 0
		pPlot = pUnit.plot()
		if pPlot.isOwned():
			if pPlot.getOwner() != pUnit.getOwner():
				return 0
		else:
			return 0
		pTeam = gc.getTeam(pUnit.getTeam())
		if pTeam.getAtWarCount(True) > 0:
			return 0
		pUnit.setUnitAIType(UnitAITypes.UNITAI_ANIMAL)

	elif pUnit.getUnitAIType() == UnitAITypes.UNITAI_ANIMAL:
		bValid = False
		if pUnit.getDamage() > 0:
			bValid = True
		pPlot = pUnit.plot()
		if pPlot.isOwned():
			if pPlot.getOwner() != pUnit.getOwner():
				bValid = True
		else:
			bValid = True
		pTeam = gc.getTeam(pUnit.getTeam())
		if pTeam.getAtWarCount(True) > 0:
			bValid = True
		if bValid:
			pUnit.setUnitAIType(UnitAITypes.UNITAI_ATTACK)

	return 0
# ent <<<