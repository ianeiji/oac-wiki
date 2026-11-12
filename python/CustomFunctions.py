## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005

from CvPythonExtensions import *
import CvUtil
import Popup as PyPopup
import PyHelpers
import CvScreenEnums
import CvCameraControls
##--------	Enums Cache: Added by Denev	--------##
import CvPythonEnums
en = CvPythonEnums.CvPythonEnums()
##--------	Enums Cache: End Add		--------##
##--------	Advanced Rules: Added by Denev	--------##
import sys
##--------	Advanced Rules: End Add			--------##

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer

class CustomFunctions:
##--------	Advanced Rules: Added by Denev	--------##
	def __init__(self):
		self.ltThresholds = [	(10, 'BUILDING_DWARVEN_VAULT_OVERFLOWING'),
								(6, 'BUILDING_DWARVEN_VAULT_FULL'),
								(4, 'BUILDING_DWARVEN_VAULT_ABUNDANT'),
								(3, 'BUILDING_DWARVEN_VAULT_STOCKED'),
								(2, 'BUILDING_DWARVEN_VAULT'),
								(1, 'BUILDING_DWARVEN_VAULT_LOW'),
								(0, 'BUILDING_DWARVEN_VAULT_EMPTY')	]

		self.mUnitaryThreshold = {}
		self.iMaxNumCities = 6	# 7th or greater city increases threshold linearly, not exponentially.

#Kaijin OAC - Trait Riches
		self.RichesltThresholds = [	(10, 'BUILDING_RICHS_STUCKED_2'),
								(6, 'BUILDING_RICHS_STUCKED_1'),
								(4, 'BUILDING_RICHS_STUCKED'),
								(3, 'BUILDING_RICHS_SAVED'),
								(2, 'BUILDING_RICHS_SMALL'),
								(1, 'BUILDING_RICHS_NONE'),
								(0, 'BUILDING_RICHS_EMPTY')	]

		self.mRichesUnitaryThreshold = {}
		self.iRichesMaxNumCities = 6	# 7th or greater city increases threshold linearly, not exponentially.
#Kaijin OAC - End
##--------	Advanced Rules: End Add			--------##

	def addBonus(self, iBonus, iNum):
		lpPlots = []
		for iPlotIndex in xrange(CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(iPlotIndex)
			if pPlot.canHaveBonus(iBonus, True) and pPlot.getBonusType(TeamTypes.NO_TEAM) == BonusTypes.NO_BONUS and not pPlot.isCity():
				lpPlots.append(pPlot)
		if len(lpPlots) > 0:
			for iLoop in xrange(iNum):
				iRnd = CyGame().getSorenRandNum(len(lpPlots), "Add Bonus")
				pPlot = lpPlots.pop(iRnd)
				pPlot.setBonusType(iBonus)
				for ePlayer in xrange(gc.getMAX_CIV_PLAYERS()):
					pPlayer = gc.getPlayer(ePlayer)
					if pPlayer.isAlive():
						eTeam = gc.getPlayer(ePlayer).getTeam()
						if pPlot.isRevealed(eTeam, False):
							pCity = pPlayer.getCity(-1)
							if ePlayer == pPlot.getOwner():
								pCity = CyMap().findCity(pPlot.getX(), pPlot.getY(), ePlayer, TeamTypes.NO_TEAM, False, False, TeamTypes.NO_TEAM, DirectionTypes.NO_DIRECTION, pCity)
							elif ePlayer == CyGame().getActivePlayer():
								pCity = CyMap().findCity(pPlot.getX(), pPlot.getY(), PlayerTypes.NO_PLAYER, TeamTypes.NO_TEAM, False, False, TeamTypes.NO_TEAM, DirectionTypes.NO_DIRECTION, pCity)
							if not pCity.isNone():
								szMessage = CyTranslator().getText("TXT_KEY_MISC_DISCOVERED_NEW_RESOURCE", (gc.getBonusInfo(iBonus).getDescription(), pCity.getNameKey()))
								pCity = CyMap().findCity(pPlot.getX(), pPlot.getY(), PlayerTypes.NO_PLAYER, TeamTypes.NO_TEAM, False, False, TeamTypes.NO_TEAM, DirectionTypes.NO_DIRECTION, pPlayer.getCity(-1))
								CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, gc.getBonusInfo(iBonus).getButton(), en.eColorWhite, pPlot.getX(), pPlot.getY(), True, True)

	def addPopup(self, szText, sDDS):
		szTitle = CyGameTextMgr().getTimeStr(CyGame().getGameTurn(), False)
		popup = PyPopup.PyPopup(-1)
		popup.addDDS(sDDS, 0, 0, 128, 384)
		popup.addSeparator()
		popup.setHeaderString(szTitle)
		popup.setBodyString(szText)
		popup.launch(True, PopupStates.POPUPSTATE_IMMEDIATE)

	def addPlayerPopup(self, szText, iPlayer):
		popupInfo = CyPopupInfo()
		popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
		popupInfo.setText(szText)
		popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_POPUP_CLOSE", ()), "")
		popupInfo.addPopup(iPlayer)

	def addBarbarianUnit(self, eUnit, eBarbarianType):
		pBestPlot = None
		iBestValue = -1
		eBarbarianPlayer = eBarbarianType + gc.getBARBARIAN_PLAYER()
		for iPlotIndex in xrange(CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(iPlotIndex)
			iValue = -1
			if not pPlot.isWater():
				if pPlot.getNumUnits() == 0:
					if not pPlot.isCity():
						if not pPlot.isImpassable():
							iValue = CyGame().getSorenRandNum(500, "Add Unit")
#							iValue = iValue + (pPlot.area().getNumTiles() * 10)
							iValue -= max(0, 25 - pPlot.area().getNumTiles()) * 20
							if pPlot.isBarbarian():
								iValue += 200
							if pPlot.isOwned():
								iValue /= 2
							if (pPlot.area().getNumCities() - pPlot.area().getCitiesPerPlayer(eBarbarianPlayer)) < 2:
								iValue /= 8
							if iValue > iBestValue:
								iBestValue = iValue
								pBestPlot = pPlot
		if pBestPlot is not None:
			pBarbarianPlayer = gc.getPlayer(eBarbarianPlayer)
			pNewUnit = pBarbarianPlayer.initUnit(eUnit, pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
			return pNewUnit
		return None

	def addUnitFixed(self, pCaster, iUnit):
		pPlot = pCaster.plot()
		pNewPlot = self.findClearPlot(-1, pPlot)
		if pNewPlot != -1:
			pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
			pNewUnit = pBarbarianPlayer.initUnit(iUnit, pNewPlot.getX(), pNewPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			return pNewUnit
		return None

	def doCrusade(self, iPlayer):
		iCrusadeChance = gc.getDefineINT('CRUSADE_SPAWN_CHANCE')
		leImprovements = [en.eImprovementEnclave, en.eImprovementTown]
		pPlayer = gc.getPlayer(iPlayer)
##--------	Unofficial Bug Fix: Added by Denev	--------##
		iDenominator = gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getTrainPercent()
##--------	Unofficial Bug Fix: End Add			--------##
		for iPlotIndex in xrange(CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(iPlotIndex)
			if pPlot.getOwner() == iPlayer:
				ePlotImprovement = pPlot.getImprovementType()
				if ePlotImprovement in leImprovements:
##--------	Unofficial Bug Fix: Added by Denev	--------##
# To prevent spawning demagog in the same tile with his enemy unit.
					if not pPlot.isVisibleEnemyUnit(iPlayer):
##--------	Unofficial Bug Fix: End Add			--------##
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#						if CyGame().getSorenRandNum(100, "Crusade") < iCrusadeChance:
						if CyGame().getSorenRandNum(iDenominator, "Crusade") < iCrusadeChance:
##--------	Unofficial Bug Fix: End Modify			--------##
							pNewUnit = pPlayer.initUnit(en.eUnitDemagog, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
							iStateReligion = pPlayer.getStateReligion()
							if iStateReligion != ReligionTypes.NO_RELIGION:
								if CyGame().getSorenRandNum(100, "Religion Adoption") < gc.getDefineINT("RELIGION_ADOPTION_CHANCE"):
									pNewUnit.setReligion(pPlayer.getStateReligion())

							pNearCity = pPlot.getWorkingCity()
							if pNearCity.isNone():
								szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_UNIT_JOIN_YOUR_CAUSE", (pNewUnit.getNameKey(), gc.getImprovementInfo(ePlotImprovement).getDescription()))
							else:
								pNearCity.applyBuildEffects(pNewUnit)
								szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_UNIT_JOIN_YOUR_CAUSE_NEAR_CITY", (pNewUnit.getNameKey(), gc.getImprovementInfo(ePlotImprovement).getDescription(), pNearCity.getNameKey()))
							szSound = pNewUnit.getArtInfo(0, EraTypes.NO_ERA).getTrainSound()
							CyInterface().addMessage(iPlayer, False, gc.getEVENT_MESSAGE_TIME(), szMessage, szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorGreen, pNewUnit.getX(), pNewUnit.getY(), True, True)

							iDowngrade = gc.getImprovementInfo(ePlotImprovement).getImprovementPillage()
							pPlot.setImprovementType(iDowngrade)

#--------	Expanded Spell Engine: Deleted by Denev 2009/12/26
	"""
	def doFear(self, pVictim, pPlot, pCaster, bResistable):
		if pVictim.isImmuneToFear():
			return False
		if bResistable:
			if CyGame().getSorenRandNum(100, "Crusade") < pVictim.getResistChance(pCaster, gc.getInfoTypeForString('SPELL_ROAR')):
				return False
		iX = pVictim.getX()
		iY = pVictim.getY()
		pBestPlot = -1
		iBestPlot = 0
		for iiX in xrange(iX-1, iX+2, 1):
			for iiY in xrange(iY-1, iY+2, 1):
				pLoopPlot = CyMap().plot(iiX,iiY)
				if not pLoopPlot.isNone():
					if not pLoopPlot.isVisibleEnemyUnit(pVictim.getOwner()):
						if pVictim.canMoveOrAttackInto(pLoopPlot, False):
							if (abs(pLoopPlot.getX() - pPlot.getX())>1) or (abs(pLoopPlot.getY() - pPlot.getY())>1):
								iRnd = CyGame().getSorenRandNum(500, "Fear")
								if iRnd > iBestPlot:
									iBestPlot = iRnd
									pBestPlot = pLoopPlot
		if pBestPlot != -1:
			pVictim.setXY(pBestPlot.getX(), pBestPlot.getY(), False, True, True)
			return True
		return False
	"""
#--------	Expanded Spell Engine: End Delete

# ent >>>
	'''
	def exploreLairBigBad(self, pCaster):
		iPlayer = pCaster.getOwner()
		pPlot = pCaster.plot()
		pPlayer = gc.getPlayer(pCaster.getOwner())
		pLairInfo = gc.getImprovementInfo(pPlot.getImprovementType())

		iPeriod = CyGame().getCurrentPeriod()
		iNumCities = CyGame().getNumCivCities()
		iNumPlayers = CyGame().countCivPlayersAlive()

		liMonsters	= []
		liHenchmans	= []
		iNumHenchmans = 3
		iWeaponTier = min(2, iPeriod)

		liForcePromotions = [	gc.getInfoTypeForString('PROMOTION_BLITZ'),
								gc.getInfoTypeForString('PROMOTION_COMMAND1'),
								gc.getInfoTypeForString('PROMOTION_HEROIC_DEFENSE'),
								gc.getInfoTypeForString('PROMOTION_MAGIC_IMMUNE'),
								gc.getInfoTypeForString('PROMOTION_SCOURGE'),
								gc.getInfoTypeForString('PROMOTION_STONESKIN'),
								gc.getInfoTypeForString('PROMOTION_VALOR'),
								gc.getInfoTypeForString('PROMOTION_VILE_TOUCH')	]
		liPromotions = []
		if pPlot.getFeatureType() == en.eFeatureForest:
			liPromotions += [	gc.getInfoTypeForString('PROMOTION_WOODSMAN1')	]
		if pPlot.isHills():
			liPromotions += [	gc.getInfoTypeForString('PROMOTION_GUERILLA1')	]

		if iPeriod == 0 and iNumCities < iNumPlayers + 1 and not pPlot.isWater():
			liMonsters	= [	(gc.getInfoTypeForString('UNIT_WARRIOR')	, (	gc.getInfoTypeForString('PROMOTION_ENCHANTED_BLADE'),)),
							(gc.getInfoTypeForString('UNIT_AXEMAN')		, (	gc.getInfoTypeForString('PROMOTION_RUSTED')			,)),
							(gc.getInfoTypeForString('UNIT_HUNTER')		, (	gc.getInfoTypeForString('PROMOTION_LIZARDMAN')		,
																			gc.getInfoTypeForString('PROMOTION_WEAK')			 )),
							(gc.getInfoTypeForString('UNIT_WOLF_PACK')	, (	gc.getInfoTypeForString('PROMOTION_EMPOWER1')		,))	]
			liHenchmans	= [	(gc.getInfoTypeForString('UNIT_GOBLIN')	, ()),
							(gc.getInfoTypeForString('UNIT_WARRIOR'), (gc.getInfoTypeForString('PROMOTION_WITHERED'),)),
							(gc.getInfoTypeForString('UNIT_WOLF')	, ())	]
			if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_BARROW'):
				liMonsters	+= [	(gc.getInfoTypeForString('UNIT_SPECTRE')	, (gc.getInfoTypeForString('PROMOTION_WEAK'),)),
									(gc.getInfoTypeForString('UNIT_SKELETON')	, ()),
									(gc.getInfoTypeForString('UNIT_SKELETON')	, ())	]
				liHenchmans	+= [	(gc.getInfoTypeForString('UNIT_SKELETON')	, (gc.getInfoTypeForString('PROMOTION_WEAK'),)),
									(gc.getInfoTypeForString('UNIT_SKELETON')	, (gc.getInfoTypeForString('PROMOTION_WEAK'),))	]
			elif pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_RUINS'):
				liMonsters	+= [	(gc.getInfoTypeForString('UNIT_HUNTER')	, (	gc.getInfoTypeForString('PROMOTION_LIZARDMAN'),
																				gc.getInfoTypeForString('PROMOTION_DISEASED')	))	]
			if pPlot.getTerrainType() in (en.eTerrainSnow, en.eTerrainTundra):
				liMonsters	+= [	(gc.getInfoTypeForString('UNIT_FROSTLING')	, ()),
									(gc.getInfoTypeForString('UNIT_FROSTLING')	, ()),
									(gc.getInfoTypeForString('UNIT_FROSTLING')	, ())	]
				liHenchmans	+= [	(gc.getInfoTypeForString('UNIT_SCOUT')	, (gc.getInfoTypeForString('PROMOTION_FROSTLING'),)),
									(gc.getInfoTypeForString('UNIT_SCOUT')	, (gc.getInfoTypeForString('PROMOTION_FROSTLING'),))	]
			if pPlot.getFeatureType() == en.eFeatureForest:
				liMonsters		= [	(gc.getInfoTypeForString('UNIT_FAWN'), (gc.getInfoTypeForString('PROMOTION_WEAK')		,)),
									(gc.getInfoTypeForString('UNIT_FAWN'), (gc.getInfoTypeForString('PROMOTION_DISEASED')	,))	]
		else:
			iNumHenchmans += 1
			liForcePromotions += [	gc.getInfoTypeForString('PROMOTION_CANNIBALIZE'),
									gc.getInfoTypeForString('PROMOTION_HEROIC_STRENGTH'),
									gc.getInfoTypeForString('PROMOTION_MOBILITY1'),
									gc.getInfoTypeForString('PROMOTION_STRONG')	]
			liPromotions += [	gc.getInfoTypeForString('PROMOTION_ENCHANTED_BLADE'),
								gc.getInfoTypeForString('PROMOTION_FLAMING_ARROWS'),
								gc.getInfoTypeForString('PROMOTION_MUTATED')	]
			if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_RUINS'):
				liPromotions += [	gc.getInfoTypeForString('PROMOTION_POISONED_BLADE')	]
			if pPlot.getFeatureType() == en.eFeatureForest:
				liPromotions += [	gc.getInfoTypeForString('PROMOTION_WOODSMAN1')	]

			if not pPlot.isWater():
				if iPeriod == 0:
					liMonsters	= [	(gc.getInfoTypeForString('UNIT_ARCHER')			, (gc.getInfoTypeForString('PROMOTION_DEXTEROUS'),)),
									(gc.getInfoTypeForString('UNIT_AXEMAN')			, ()),
									(gc.getInfoTypeForString('UNIT_BEAR')			, ()),
									(gc.getInfoTypeForString('UNIT_CHAOS_MARAUDER')	, ()),
									(gc.getInfoTypeForString('UNIT_GIANT_SPIDER')	, ()),
									(gc.getInfoTypeForString('UNIT_GRIFFON')		, ()),
									(gc.getInfoTypeForString('UNIT_HUNTER')			, (gc.getInfoTypeForString('PROMOTION_LIZARDMAN'),)),
									(gc.getInfoTypeForString('UNIT_LION_PRIDE')		, ()),
									(gc.getInfoTypeForString('UNIT_TIGER')			, ()),
									(gc.getInfoTypeForString('UNIT_WOLF_RIDER')		, ()),
									(gc.getInfoTypeForString('UNIT_WOLF_CHARIOT')	, ())	]
					liHenchmans	= [	(gc.getInfoTypeForString('UNIT_BABY_SPIDER')			, ()),
									(gc.getInfoTypeForString('UNIT_GOBLIN')					, (gc.getInfoTypeForString('PROMOTION_POISONED_BLADE'),)),
									(gc.getInfoTypeForString('UNIT_LION')					, ()),
									(gc.getInfoTypeForString('UNIT_LIGHTNING_ELEMENTAL')	, ()),
									(gc.getInfoTypeForString('UNIT_WARRIOR')				, ()),
									(gc.getInfoTypeForString('UNIT_WOLF')					, (gc.getInfoTypeForString('PROMOTION_EMPOWER1'),))	]
					if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_BARROW'):
						liBarrowMonsters	= [	(gc.getInfoTypeForString('UNIT_DISEASED_CORPSE'), ()),
												(gc.getInfoTypeForString('UNIT_PYRE_ZOMBIE')	, ()),
												(gc.getInfoTypeForString('UNIT_SPECTRE')		, ())	]
						liBarrowHenchmans	= [	(gc.getInfoTypeForString('UNIT_SKELETON')		, ())	]
						for iLoop in xrange(3):
							liMonsters	+= liBarrowMonsters
							liHenchmans	+= liBarrowHenchmans
					elif pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_RUINS'):
						liMonsters	= [	(gc.getInfoTypeForString('UNIT_GORILLA'), ()),
										(gc.getInfoTypeForString('UNIT_HUNTER')	, (gc.getInfoTypeForString('PROMOTION_LIZARDMAN'),)),
										(gc.getInfoTypeForString('UNIT_HUNTER')	, (gc.getInfoTypeForString('PROMOTION_LIZARDMAN'),))	]
					if pPlot.getTerrainType() in (en.eTerrainSnow, en.eTerrainTundra):
						liWinterMonsters	= [	(gc.getInfoTypeForString('UNIT_ICE_ELEMENTAL')	, ()),
												(gc.getInfoTypeForString('UNIT_POLAR_BEAR')		, ()),
												(gc.getInfoTypeForString('UNIT_ARCHER')			, (gc.getInfoTypeForString('PROMOTION_FROSTLING'),)),
												(gc.getInfoTypeForString('UNIT_WOLF_RIDER')		, (gc.getInfoTypeForString('PROMOTION_FROSTLING'),))	]
						liWinterHenchmans	= [	(gc.getInfoTypeForString('UNIT_FROSTLING')		, ())	]
						for iLoop in xrange(3):
							liMonsters	+= liWinterMonsters
							liHenchmans	+= liWinterHenchmans
					elif pPlot.getTerrainType() == en.eTerrainDesert:
						liMonsters += [	(gc.getInfoTypeForString('UNIT_SAND_LION')	, ()),
										(gc.getInfoTypeForString('UNIT_SCORPION')	, ()),
										(gc.getInfoTypeForString('UNIT_SCORPION')	, ()),
										(gc.getInfoTypeForString('UNIT_SCORPION')	, ())	]
					if pPlot.getFeatureType() == en.eFeatureForest:
						liMonsters += [	(gc.getInfoTypeForString('UNIT_FAWN'), ()),
										(gc.getInfoTypeForString('UNIT_FAWN'), ()),
										(gc.getInfoTypeForString('UNIT_FAWN'), ())	]
				else:
					iNumHenchmans += 1
					liMonsters	= [	(gc.getInfoTypeForString('UNIT_ASSASSIN')			, (gc.getInfoTypeForString('PROMOTION_LIZARDMAN'),)),
									(gc.getInfoTypeForString('UNIT_AZER')				, ()),
									(gc.getInfoTypeForString('UNIT_HILL_GIANT')			, ()),
									(gc.getInfoTypeForString('UNIT_LONGBOWMAN')			, (gc.getInfoTypeForString('PROMOTION_DEXTEROUS'),)),
									(gc.getInfoTypeForString('UNIT_LUNATIC')			, ()),
									(gc.getInfoTypeForString('UNIT_MISTFORM')			, ()),
									(gc.getInfoTypeForString('UNIT_OGRE')				, ()),
									(gc.getInfoTypeForString('UNIT_RANGER')				, (gc.getInfoTypeForString('PROMOTION_LIZARDMAN'),)),
									(gc.getInfoTypeForString('UNIT_RAVENOUS_WEREWOLF')	, ()),
									(gc.getInfoTypeForString('UNIT_VAMPIRE')			, ())	]
					liHenchmans	= [	(gc.getInfoTypeForString('UNIT_ARCHER')			, (gc.getInfoTypeForString('PROMOTION_DEXTEROUS'),)),
									(gc.getInfoTypeForString('UNIT_AXEMAN')			, ()),
									(gc.getInfoTypeForString('UNIT_BEAR')			, ()),
									(gc.getInfoTypeForString('UNIT_CHAOS_MARAUDER')	, ()),
									(gc.getInfoTypeForString('UNIT_GIANT_SPIDER')	, ()),
									(gc.getInfoTypeForString('UNIT_GRIFFON')		, ()),
									(gc.getInfoTypeForString('UNIT_HUNTER')			, (gc.getInfoTypeForString('PROMOTION_LIZARDMAN'),)),
									(gc.getInfoTypeForString('UNIT_LION_PRIDE')		, ()),
									(gc.getInfoTypeForString('UNIT_SCORPION')		, ()),
									(gc.getInfoTypeForString('UNIT_TIGER')			, ()),
									(gc.getInfoTypeForString('UNIT_WOLF_RIDER')		, ()),
									(gc.getInfoTypeForString('UNIT_WOLF_CHARIOT')	, ())	]
					if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_BARROW'):
						liBarrowMonsters	= [	(gc.getInfoTypeForString('UNIT_LICH'), ())	]
						liBarrowHenchmans	= [	(gc.getInfoTypeForString('UNIT_DISEASED_CORPSE'), ()),
												(gc.getInfoTypeForString('UNIT_PYRE_ZOMBIE')	, ()),
												(gc.getInfoTypeForString('UNIT_SPECTRE')		, ())	]
						for iLoop in xrange(3):
							liMonsters	+= liBarrowMonsters
							liHenchmans	+= liBarrowHenchmans
					elif pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_RUINS'):
						liMonsters	+= [	(gc.getInfoTypeForString('UNIT_RANGER')	, (gc.getInfoTypeForString('PROMOTION_LIZARDMAN'),))	]
						liHenchmans	+= [	(gc.getInfoTypeForString('UNIT_GORILLA'), ()),
											(gc.getInfoTypeForString('UNIT_HUNTER')	, (gc.getInfoTypeForString('PROMOTION_LIZARDMAN'),))	]
					if pPlot.getTerrainType() in (en.eTerrainSnow, en.eTerrainTundra):
						liWinterMonsters	= []
						liWinterHenchmans	= [	(gc.getInfoTypeForString('UNIT_ICE_ELEMENTAL')	, ()),
												(gc.getInfoTypeForString('UNIT_POLAR_BEAR')		, ()),
												(gc.getInfoTypeForString('UNIT_ARCHER')			, (gc.getInfoTypeForString('PROMOTION_FROSTLING'),)),
												(gc.getInfoTypeForString('UNIT_WOLF_RIDER')		, (gc.getInfoTypeForString('PROMOTION_FROSTLING'),))	]
						for iLoop in xrange(3):
							liMonsters	+= liWinterMonsters
							liHenchmans	+= liWinterHenchmans
					elif pPlot.getTerrainType() == en.eTerrainDesert:
						liMonsters	+= [	(gc.getInfoTypeForString('UNIT_HILL_GIANT'), ())	]
						liHenchmans	+= [	(gc.getInfoTypeForString('UNIT_SAND_LION'), ()),
											(gc.getInfoTypeForString('UNIT_SAND_LION'), ()),
											(gc.getInfoTypeForString('UNIT_SAND_LION'), ()),
											(gc.getInfoTypeForString('UNIT_SCORPION'), ())	]
					if pPlot.getFeatureType() == en.eFeatureForest:
						liMonsters	+= [	(gc.getInfoTypeForString('UNIT_SATYR'), ())	]
						liHenchmans	+= [	(gc.getInfoTypeForString('UNIT_FAWN'), ()),
											(gc.getInfoTypeForString('UNIT_FAWN'), ()),
											(gc.getInfoTypeForString('UNIT_FAWN'), ())	]

					if CyGame().getGlobalCounter() > 20:
						liHenchmans += [	(gc.getInfoTypeForString('UNIT_IMP')		, ()),
											(gc.getInfoTypeForString('UNIT_HELLHOUND')	, ()),
											(gc.getInfoTypeForString('UNIT_PIT_BEAST')	, ())	]
						liPromotions += [gc.getInfoTypeForString('PROMOTION_ENTROPY1')]
					if CyGame().getGlobalCounter() > 40:
						liMonsters	+= [	(gc.getInfoTypeForString('UNIT_DEATH_KNIGHT')	, ()),
											(gc.getInfoTypeForString('UNIT_BALOR')			, ())	]
						liHenchmans	+= [	(gc.getInfoTypeForString('UNIT_SUCCUBUS')		, ()),
											(gc.getInfoTypeForString('UNIT_TAR_DEMON')		, ())	]
						liForcePromotions += [gc.getInfoTypeForString('PROMOTION_FEAR')]

					if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_BARROW'):
						liForcePromotions += [	gc.getInfoTypeForString('PROMOTION_DEATH2')	]

					if iPeriod > 1:
						iNumHenchmans += 1
						liMonsters	+= [	(gc.getInfoTypeForString('UNIT_BERSERKER')			, ()),
											(gc.getInfoTypeForString('UNIT_CROSSBOWMAN')		, (gc.getInfoTypeForString('PROMOTION_DEXTEROUS'),)),
											(gc.getInfoTypeForString('UNIT_DRUID')				, (gc.getInfoTypeForString('PROMOTION_LIZARDMAN'),)),
											(gc.getInfoTypeForString('UNIT_EARTH_ELEMENTAL')	, ()),
											(gc.getInfoTypeForString('UNIT_EIDOLON')			, ()),
											(gc.getInfoTypeForString('UNIT_FIRE_ELEMENTAL')		, ()),
											(gc.getInfoTypeForString('UNIT_GARGOYLE')			, ()),
											(gc.getInfoTypeForString('UNIT_GREATER_WEREWOLF')	, ()),
											(gc.getInfoTypeForString('UNIT_MINOTAUR')			, ()),
											(gc.getInfoTypeForString('UNIT_MYCONID')			, ()),
											(gc.getInfoTypeForString('UNIT_OGRE')				, (gc.getInfoTypeForString('PROMOTION_MITHRIL_WEAPONS'),)),
											(gc.getInfoTypeForString('UNIT_STONESKIN_OGRE')		, ()),
											(gc.getInfoTypeForString('UNIT_WEREWOLF')			, ())	]
						liHenchmans	+= [	(gc.getInfoTypeForString('UNIT_ASSASSIN')			, (gc.getInfoTypeForString('PROMOTION_LIZARDMAN'),)),
											(gc.getInfoTypeForString('UNIT_AZER')				, ()),
											(gc.getInfoTypeForString('UNIT_HILL_GIANT')			, ()),
											(gc.getInfoTypeForString('UNIT_LONGBOWMAN')			, (gc.getInfoTypeForString('PROMOTION_DEXTEROUS'),)),
											(gc.getInfoTypeForString('UNIT_LUNATIC')			, ()),
											(gc.getInfoTypeForString('UNIT_MISTFORM')			, ()),
											(gc.getInfoTypeForString('UNIT_OGRE')				, ()),
											(gc.getInfoTypeForString('UNIT_RANGER')				, (gc.getInfoTypeForString('PROMOTION_LIZARDMAN'),)),
											(gc.getInfoTypeForString('UNIT_RAVENOUS_WEREWOLF')	, ()),
											(gc.getInfoTypeForString('UNIT_VAMPIRE')			, ())	]
						if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_BARROW'):
							liMonsters	+= [	(gc.getInfoTypeForString('UNIT_LICH')	, (gc.getInfoTypeForString('PROMOTION_FIRE2'),)),
												(gc.getInfoTypeForString('UNIT_WRAITH')	, ()),
												(gc.getInfoTypeForString('UNIT_WRAITH')	, ())	]
						elif pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_RUINS'):
							liMonsters	+= [	gc.getInfoTypeForString('UNIT_MANTICORE')	]
						if pPlot.getTerrainType() == en.eTerrainDesert:
							liDesertMonsters	= []
							liDesertiHenchmans	= [	(gc.getInfoTypeForString('UNIT_HILL_GIANT')	, ()),
													(gc.getInfoTypeForString('UNIT_SAND_LION')	, ())	]
							for iLoop in xrange(2):
								liMonsters	+= liDesertMonsters
								liHenchmans	+= liDesertiHenchmans
						if pPlot.getFeatureType() == en.eFeatureForest:
							liForestMonsters	= [	(gc.getInfoTypeForString('UNIT_TREANT'), ())	]
							liForestHenchmans	= [	(gc.getInfoTypeForString('UNIT_SATYR'), ())	]
							for iLoop in xrange(3):
								liMonsters	+= liForestMonsters
								liHenchmans	+= liForestHenchmans
						liForcePromotions += [	gc.getInfoTypeForString('PROMOTION_AIR2'),
												gc.getInfoTypeForString('PROMOTION_FIRE2'),
												gc.getInfoTypeForString('PROMOTION_HERO')	]
						liPromotions += [	gc.getInfoTypeForString('PROMOTION_MARKSMAN'),
											gc.getInfoTypeForString('PROMOTION_SHADOWWALK')	]
			else:
				liMonsters	= [	(gc.getInfoTypeForString('UNIT_GIANT_TORTOISE')	, ()),
								(gc.getInfoTypeForString('UNIT_SEA_SERPENT')	, ())	]
				liHenchmans	= [	(gc.getInfoTypeForString('UNIT_DROWN')	, ()),
								(gc.getInfoTypeForString('UNIT_GRIFFON'), ())	]
				if iPeriod == 0:
					liMonsters	+= [(gc.getInfoTypeForString('UNIT_DROWN')	, ()),
									(gc.getInfoTypeForString('UNIT_GRIFFON'), ())	]
				if iPeriod > 0:
					iNumHenchmans += 1
					liMonsters	+= [(gc.getInfoTypeForString('UNIT_AZER')			, ()),
									(gc.getInfoTypeForString('UNIT_STYGIAN_GUARD')	, ())	]
					liHenchmans	= [	(gc.getInfoTypeForString('UNIT_GIANT_TORTOISE')	, ()),
									(gc.getInfoTypeForString('UNIT_SEA_SERPENT')	, ())	]
				if iPeriod > 1:
					iNumHenchmans += 1
					liMonsters	+= [	(gc.getInfoTypeForString('UNIT_AIR_ELEMENTAL')	, ()),
										(gc.getInfoTypeForString('UNIT_KRAKEN')			, ()),
										(gc.getInfoTypeForString('UNIT_MANTICORE')		, ()),
										(gc.getInfoTypeForString('UNIT_WATER_ELEMENTAL'), ())	]
					liHenchmans	+= [(gc.getInfoTypeForString('UNIT_AZER')			, ()),
									(gc.getInfoTypeForString('UNIT_PIRATE')			, ()),
									(gc.getInfoTypeForString('UNIT_STYGIAN_GUARD')	, ())	]

		iMonsterUnit, liMonsterPromotions	= liMonsters[CyGame().getSorenRandNum(len(liMonsters), "Pick Monster")]
		iHenchmanUnit, liHenchmanPromotions	= liHenchmans[CyGame().getSorenRandNum(len(liHenchmans), "Pick Henchman")]

		pNewUnit = self.addUnitFixed(pCaster, iMonsterUnit)

		if pNewUnit is not None:
			# apply default promotions
			for iDefaultPromotion in liMonsterPromotions:
				pNewUnit.setHasPromotion(iDefaultPromotion, True)

			# create extra promotion table
			liValidPromotions = [iPromotion for iPromotion in liPromotions if gc.getPromotionInfo(iPromotion).getMinLevel() == -1]
			if pNewUnit.getUnitCombatType() != UnitCombatTypes.NO_UNITCOMBAT:
				liValidPromotions += [iPromotion for iPromotion in liPromotions if gc.getPromotionInfo(iPromotion).getUnitCombat(pNewUnit.getUnitCombatType())]
			liValidPromotions += liForcePromotions
			liValidPromotions += [iPromotion for iPromotion in liValidPromotions if not pNewUnit.isHasPromotion(iPromotion)]

			# apply extra promotions
			iProbability = 80
			for iLoop in xrange(10):
				if CyGame().getSorenRandNum(100, "Pick Promotion") < iProbability:
					iPromotion = liValidPromotions.pop(CyGame().getSorenRandNum(len(liValidPromotions), "Pick Promotion Type"))
					pNewUnit.setHasPromotion(iPromotion, True)
					iProbability //= 2
				else:
					break

			# apply weapon
			iWeaponTierCap = min(gc.getUnitInfo(pNewUnit.getUnitType()).getWeaponTier(), iWeaponTier)
			if iWeaponTierCap > 0:
				iRandomTier = CyGame().getSorenRandNum(gc.getNumWeaponInfos() + 1, "Pick Weapon Type")
				if 0 < iRandomTier <= iWeaponTierCap:
					for iWeapon in xrange(gc.getNumWeaponInfos()):
						if gc.getWeaponInfo(iWeapon).getWeaponTier() == iRandomTier:
							pNewUnit.setHasPromotion(gc.getWeaponInfo(iWeapon).getWeaponPromotion(), True)
							break

			pNewUnit.setName(self.MarnokNameGenerator(pNewUnit))
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BIGBAD",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorRed, pNewUnit.getX(), pNewUnit.getY(), True, True)

			eBarbarianPlayer = pLairInfo.getSpawnBarbarianType()
			if eBarbarianPlayer == BarbarianTypes.NO_BARBARIAN:
				pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
			else:
				pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER() + eBarbarianPlayer)
			iNumHenchmans = CyGame().getSorenRandNum(iNumHenchmans, "Pick the Number of Henchmen")
			for iLoop in xrange(iNumHenchmans):
				pNewHenchmanUnit = pBarbarianPlayer.initUnit(iHenchmanUnit, pNewUnit.getX(), pNewUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
				for iDefaultPromotion in liHenchmanPromotions:
					pNewHenchmanUnit.setHasPromotion(iDefaultPromotion, True)
		else:
			pCaster.kill(True, PlayerTypes.NO_PLAYER)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_DEATH", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pLairInfo.getButton(), en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
		"""
		liPromotions = [	gc.getInfoTypeForString('PROMOTION_MUTATED'),
							gc.getInfoTypeForString('PROMOTION_CANNIBALIZE'),
							gc.getInfoTypeForString('PROMOTION_MOBILITY1'),
							gc.getInfoTypeForString('PROMOTION_STRONG'),
							gc.getInfoTypeForString('PROMOTION_BLITZ'),
							gc.getInfoTypeForString('PROMOTION_COMMAND1'),
							gc.getInfoTypeForString('PROMOTION_HEROIC_STRENGTH'),
							gc.getInfoTypeForString('PROMOTION_HEROIC_DEFENSE'),
							gc.getInfoTypeForString('PROMOTION_MAGIC_IMMUNE'),
							gc.getInfoTypeForString('PROMOTION_STONESKIN'),
							gc.getInfoTypeForString('PROMOTION_VALOR'),
							gc.getInfoTypeForString('PROMOTION_VILE_TOUCH')	]

		liMonsters	= [	gc.getInfoTypeForString('UNIT_AZER')	]
		liHenchmans	= [	gc.getInfoTypeForString('UNIT_AZER'),
						gc.getInfoTypeForString('UNIT_GRIFFON')	]
		if not self.grace():
			liMonsters += [gc.getInfoTypeForString('UNIT_AIR_ELEMENTAL')]

		if pPlot.isWater():
			liMonsters	+= [	gc.getInfoTypeForString('UNIT_SEA_SERPENT'),
								gc.getInfoTypeForString('UNIT_STYGIAN_GUARD'),
								gc.getInfoTypeForString('UNIT_PIRATE')	]
			liHenchmans	+= [	gc.getInfoTypeForString('UNIT_DROWN')	]
			if not self.grace():
				liMonsters += [	gc.getInfoTypeForString('UNIT_WATER_ELEMENTAL'),
								gc.getInfoTypeForString('UNIT_KRAKEN')	]
		else:
			liMonsters	+= [	gc.getInfoTypeForString('UNIT_ASSASSIN'),
								gc.getInfoTypeForString('UNIT_OGRE'),
								gc.getInfoTypeForString('UNIT_GIANT_SPIDER'),
								gc.getInfoTypeForString('UNIT_HILL_GIANT')	]
			liHenchmans += [	gc.getInfoTypeForString('UNIT_AXEMAN'),
								gc.getInfoTypeForString('UNIT_WOLF'),
								gc.getInfoTypeForString('UNIT_CHAOS_MARAUDER'),
								gc.getInfoTypeForString('UNIT_WOLF_RIDER'),
								gc.getInfoTypeForString('UNIT_MISTFORM'),
								gc.getInfoTypeForString('UNIT_LION'),
								gc.getInfoTypeForString('UNIT_TIGER'),
								gc.getInfoTypeForString('UNIT_BABY_SPIDER'),
								gc.getInfoTypeForString('UNIT_FAWN')	]
			if not self.grace():
				liMonsters	+= [	gc.getInfoTypeForString('UNIT_EARTH_ELEMENTAL'),
									gc.getInfoTypeForString('UNIT_FIRE_ELEMENTAL'),
									gc.getInfoTypeForString('UNIT_GARGOYLE'),
									gc.getInfoTypeForString('UNIT_VAMPIRE'),
									gc.getInfoTypeForString('UNIT_MYCONID'),
									gc.getInfoTypeForString('UNIT_EIDOLON'),
									gc.getInfoTypeForString('UNIT_LICH'),
									gc.getInfoTypeForString('UNIT_OGRE_WARCHIEF'),
									gc.getInfoTypeForString('UNIT_SATYR'),
									gc.getInfoTypeForString('UNIT_WEREWOLF')	]
				liHenchmans	+= [	gc.getInfoTypeForString('UNIT_OGRE')	]
				liPromotions += [	gc.getInfoTypeForString('PROMOTION_FIRE2'),
									gc.getInfoTypeForString('PROMOTION_AIR2'),
									gc.getInfoTypeForString('PROMOTION_HERO'),
									gc.getInfoTypeForString('PROMOTION_MARKSMAN'),
									gc.getInfoTypeForString('PROMOTION_SHADOWWALK')	]

				if pPlot.getFeatureType() == gc.getInfoTypeForString('FEATURE_FOREST'):
					liMonsters += [	gc.getInfoTypeForString('UNIT_TREANT')	]

			if pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_SNOW'):
				liHenchmans	+= [	gc.getInfoTypeForString('UNIT_FROSTLING_ARCHER'),
									gc.getInfoTypeForString('UNIT_FROSTLING_WOLF_RIDER'),
									gc.getInfoTypeForString('UNIT_POLAR_BEAR')	]

			if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_BARROW'):
				liMonsters	+= [	gc.getInfoTypeForString('UNIT_SPECTRE')	]
				liHenchmans	+= [	gc.getInfoTypeForString('UNIT_SKELETON'),
									gc.getInfoTypeForString('UNIT_PYRE_ZOMBIE')	]
				liPromotions += [	gc.getInfoTypeForString('PROMOTION_DEATH2')	]
				if not self.grace():
					liMonsters += [	gc.getInfoTypeForString('UNIT_WRAITH')	]
			elif pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_RUINS'):
				liHenchmans	+= [	gc.getInfoTypeForString('UNIT_LIZARDMAN'),
									gc.getInfoTypeForString('UNIT_GORILLA')	]
				liPromotions += [	gc.getInfoTypeForString('PROMOTION_POISONED_BLADE')	]
				if not self.grace():
					liMonsters += [	gc.getInfoTypeForString('UNIT_MANTICORE')	]

			if CyGame().getGlobalCounter() > 40:
				liMonsters	+= [	gc.getInfoTypeForString('UNIT_PIT_BEAST'),
									gc.getInfoTypeForString('UNIT_DEATH_KNIGHT'),
									gc.getInfoTypeForString('UNIT_BALOR')	]
				liHenchmans += [	gc.getInfoTypeForString('UNIT_IMP'),
									gc.getInfoTypeForString('UNIT_HELLHOUND')	]
				liPromotions += [gc.getInfoTypeForString('PROMOTION_FEAR')]

		iMonster = liMonsters[CyGame().getSorenRandNum(len(liMonsters), "Pick Monster")]
		iHenchman = liHenchmans[CyGame().getSorenRandNum(len(liHenchmans), "Pick Henchman")]
		pNewUnit = self.addUnitFixed(pCaster, iMonster)
		if pNewUnit != -1:
			iProbability = 80
			for iLoop in xrange(10):
				if CyGame().getSorenRandNum(100, "Pick Promotion") < iProbability:
					iPromotion = liPromotions.pop(CyGame().getSorenRandNum(len(liPromotions), "Pick Promotion Type"))
					pNewUnit.setHasPromotion(iPromotion, True)
					iProbability //= 2
				else:
					break
			pNewUnit.setName(self.MarnokNameGenerator(pNewUnit))
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BIGBAD",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getUnitInfo(iMonster).getButton(), en.eColorRed, pNewUnit.getX(), pNewUnit.getY(), True, True)
			pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
			for iLoop in xrange(CyGame().getSorenRandNum(5, "Pick the Number of Henchmen")):
				pBarbarianPlayer.initUnit(iHenchman, pNewUnit.getX(), pNewUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		"""
		return 0
	'''

	def exploreLairBigBad(self, pCaster):
		iPlayer = pCaster.getOwner()
		pPlot = pCaster.plot()
		pPlayer = gc.getPlayer(pCaster.getOwner())
		pLairInfo = gc.getImprovementInfo(pPlot.getImprovementType())

		bWater = (pPlot.isWater())
		bHills = (pPlot.isHills())
		eFeature = pPlot.getFeatureType()
		eTerrain = pPlot.getTerrainType()
		iCounter = CyGame().getGlobalCounter()
		iOctopusLevel = CyGame().calculateReligionPercent(en.eReligionOctopusOverlords)

		eOrc = en.eBarbarianOrc
		eAnimal = en.eBarbarianAnimal
		eDemons = en.eBarbarianDemons
		eUndead = en.eBarbarianUndead
		eFrostling = en.eBarbarianFrostling
		ePirates = en.eBarbarianPirates

		# 脅威レベルとお供の数
		iPeriod = CyGame().getCurrentPeriod() #[0-6]
		iNumCities = CyGame().getNumCivCities()
		iNumPlayers = CyGame().countCivPlayersAlive()
		iWeaponTier = min(2, iPeriod)
		iThreat = 1
		iNumHenchmans = 3
		if iPeriod > 0 or iNumCities > iNumPlayers:
			iThreat += (iPeriod // 2) + 1
			iNumHenchmans += (iPeriod + 1) // 2

		def doCasterKill():
			pCaster.kill(True, PlayerTypes.NO_PLAYER)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_DEATH", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pLairInfo.getButton(), en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
			return

		# 蛮族の所属候補 (蛮族IDリスト)
		eBarbarianPlayer = pLairInfo.getSpawnBarbarianType()
		if eBarbarianPlayer != BarbarianTypes.NO_BARBARIAN:
			leEnemyBarbarian = [eBarbarianPlayer]
		else:
			leEnemyBarbarian = []
			pTeam = gc.getTeam(pPlayer.getTeam())
			pBarbarianOrc = gc.getPlayer(gc.getBARBARIAN_PLAYER() + eOrc)
			if pTeam.isAtWar(pBarbarianOrc.getTeam()):
				leEnemyBarbarian.append(eOrc)
			pBarbarianAnimal = gc.getPlayer(gc.getBARBARIAN_PLAYER() + eAnimal)
			if pTeam.isAtWar(pBarbarianAnimal.getTeam()):
				leEnemyBarbarian.append(eAnimal)
			pBarbarianDemons = gc.getPlayer(gc.getBARBARIAN_PLAYER() + eDemons)
			if pTeam.isAtWar(pBarbarianDemons.getTeam()):
				leEnemyBarbarian.append(eDemons)
			pBarbarianUndead = gc.getPlayer(gc.getBARBARIAN_PLAYER() + eUndead)
			if pTeam.isAtWar(pBarbarianUndead.getTeam()):
				leEnemyBarbarian.append(eUndead)
			if not bWater:
				pBarbarianFrostling = gc.getPlayer(gc.getBARBARIAN_PLAYER() + eFrostling)
				if pTeam.isAtWar(pBarbarianFrostling.getTeam()):
					leEnemyBarbarian.append(eFrostling)
			if bWater:
				pBarbarianPirates = gc.getPlayer(gc.getBARBARIAN_PLAYER() + ePirates)
				if pTeam.isAtWar(pBarbarianPirates.getTeam()):
					leEnemyBarbarian.append(ePirates)
		if len(leEnemyBarbarian) == 0:
			doCasterKill()
			return

		# ユニット候補 (所属, 世代, ユニット, 初期昇進)
		if bWater:
			ltEnemies = [	(eOrc,		0,	gc.getInfoTypeForString('UNIT_AIR_ELEMENTAL'),		(gc.getInfoTypeForString('PROMOTION_WEAK'),)),
							(eOrc,		1,	gc.getInfoTypeForString('UNIT_AIR_ELEMENTAL'),		()),
							(eOrc,		2,	gc.getInfoTypeForString('UNIT_AZER'),				()),
							(eOrc,		3,	gc.getInfoTypeForString('UNIT_PRIVATEER'),			()),
							(eOrc,		4,	gc.getInfoTypeForString('UNIT_HELLFIRE_ELEMENTAL'),	()),
							(eAnimal,	0,	gc.getInfoTypeForString('UNIT_GREATRACE'),			(gc.getInfoTypeForString('PROMOTION_WEAK'),)),
							(eAnimal,	1,	gc.getInfoTypeForString('UNIT_GREATRACE'),			()),
							(eAnimal,	2,	gc.getInfoTypeForString('UNIT_GIANT_TORTOISE'),		()),
							(eAnimal,	3,	gc.getInfoTypeForString('UNIT_SEA_SERPENT'),		()),
							(eAnimal,	4,	gc.getInfoTypeForString('UNIT_KRAKEN'),				()),
							(eAnimal,	5,	gc.getInfoTypeForString('UNIT_DRAGON_QUETZALCOATL'),()),
							(ePirates,	2,	gc.getInfoTypeForString('UNIT_CARAVEL'),			()),
							(ePirates,	3,	gc.getInfoTypeForString('UNIT_PIRATE'),				()),
							(ePirates,	4,	gc.getInfoTypeForString('UNIT_FRIGATE'),			()),
							(ePirates,	5,	gc.getInfoTypeForString('UNIT_MAN_O_WAR'),			())]
			if iCounter > 20:
				ltEnemies += [	(eDemons,	2,	gc.getInfoTypeForString('UNIT_MARCHOSIAS'),			()),
								(eDemons,	4,	gc.getInfoTypeForString('UNIT_MANTICORE'),			()),
								(eDemons,	5,	gc.getInfoTypeForString('UNIT_IRA'),				())]
			if iOctopusLevel > 20:
				ltEnemies += [	(eDemons,	0,	gc.getInfoTypeForString('UNIT_GREATRACE'),			(gc.getInfoTypeForString('PROMOTION_WEAK'),)),
								(eDemons,	1,	gc.getInfoTypeForString('UNIT_GREATRACE'),			()),
								(eDemons,	3,	gc.getInfoTypeForString('UNIT_ITHAQUA'),			()),
								(eDemons,	3,	gc.getInfoTypeForString('UNIT_ITHAQUA'),			()),
								(eDemons,	4,	gc.getInfoTypeForString('UNIT_BYAKHEE'),			()),
								(eDemons,	4,	gc.getInfoTypeForString('UNIT_BYAKHEE'),			()),
								(eDemons,	5,	gc.getInfoTypeForString('UNIT_ELDERTHING'),			()),
								(eDemons,	5,	gc.getInfoTypeForString('UNIT_ELDERTHING'),			())]

			if eTerrain == en.eTerrainCoast:
				ltEnemies += [	(eOrc,		0,	gc.getInfoTypeForString('UNIT_WATER_ELEMENTAL'),		(gc.getInfoTypeForString('PROMOTION_WEAK'),)),
								(eOrc,		1,	gc.getInfoTypeForString('UNIT_WATER_ELEMENTAL'),		()),
								(eOrc,		3,	gc.getInfoTypeForString('UNIT_PRIEST_OF_THE_OVERLORDS'),()),
								(eOrc,		5,	gc.getInfoTypeForString('UNIT_WAR_TORTOISE'),			()),
								(eAnimal,	0,	gc.getInfoTypeForString('UNIT_GRIFFON'),				(gc.getInfoTypeForString('PROMOTION_WEAK'),)),
								(eAnimal,	1,	gc.getInfoTypeForString('UNIT_GRIFFON'),				()),
								(eAnimal,	3,	gc.getInfoTypeForString('UNIT_HIPPOGRIFF'),				()),
								(eUndead,	0,	gc.getInfoTypeForString('UNIT_DROWN'),					(gc.getInfoTypeForString('PROMOTION_RUSTED'),)),
								(eUndead,	1,	gc.getInfoTypeForString('UNIT_DROWN'),					()),
								(eUndead,	2,	gc.getInfoTypeForString('UNIT_DROWN'),					(gc.getInfoTypeForString('PROMOTION_STRONG'),
																										 gc.getInfoTypeForString('PROMOTION_MUSOU'),)),
								(ePirates,	1,	gc.getInfoTypeForString('UNIT_GALLEY'),					()),
								(ePirates,	2,	gc.getInfoTypeForString('UNIT_TRIREME'),				()),
								(ePirates,	3,	gc.getInfoTypeForString('UNIT_BOARDING_PARTY'),			()),
								(ePirates,	4,	gc.getInfoTypeForString('UNIT_TRANSITION_SAILOR'),		())]
				if iOctopusLevel > 20:
					ltEnemies += [	(eDemons,	3,	gc.getInfoTypeForString('UNIT_TINDALOS'),			()),
									(eDemons,	3,	gc.getInfoTypeForString('UNIT_STYGIAN_GUARD'),		()),
									(eDemons,	3,	gc.getInfoTypeForString('UNIT_STYGIAN_GUARD'),		()),
									(eDemons,	3,	gc.getInfoTypeForString('UNIT_SHOGGOTH'),			()),
									(eDemons,	3,	gc.getInfoTypeForString('UNIT_SHOGGOTH'),			())]

		else:
			ltEnemies = [	(eOrc,		0,	gc.getInfoTypeForString('UNIT_GOBLIN'),				()),
							(eOrc,		1,	gc.getInfoTypeForString('UNIT_GOBLIN'),				(gc.getInfoTypeForString('PROMOTION_SCORPION_CLAN'),)),
							(eOrc,		1,	gc.getInfoTypeForString('UNIT_WARRIOR'),			()),
							(eOrc,		2,	gc.getInfoTypeForString('UNIT_AXEMAN'),				()),
							(eOrc,		2,	gc.getInfoTypeForString('UNIT_ARCHER'),				()),
							(eOrc,		2,	gc.getInfoTypeForString('UNIT_ARCHER'),				(gc.getInfoTypeForString('PROMOTION_GOBLIN'),
																								 gc.getInfoTypeForString('PROMOTION_SCORPION_CLAN'),)),
							(eOrc,		2,	gc.getInfoTypeForString('UNIT_HUNTER'),				(gc.getInfoTypeForString('PROMOTION_LIZARDMAN'),)),
							(eOrc,		2,	gc.getInfoTypeForString('UNIT_WOLF_RIDER'),			(gc.getInfoTypeForString('PROMOTION_GOBLIN'),)),
							(eOrc,		2,	gc.getInfoTypeForString('UNIT_DISCIPLE_OF_ACHERON'),()),
							(eOrc,		2,	gc.getInfoTypeForString('UNIT_FIRE_ELEMENTAL'),		(gc.getInfoTypeForString('PROMOTION_STRONG'),)),
							(eOrc,		3,	gc.getInfoTypeForString('UNIT_EARTH_ELEMENTAL'),	(gc.getInfoTypeForString('PROMOTION_STRONG'),
																								 gc.getInfoTypeForString('PROMOTION_HEROIC_DEFENSE'),
																								 gc.getInfoTypeForString('PROMOTION_HEROIC_DEFENSE2'),
																								 gc.getInfoTypeForString('PROMOTION_HEROIC_STRENGTH'),
																								 gc.getInfoTypeForString('PROMOTION_HEROIC_STRENGTH2'),)),
							(eOrc,		3,	gc.getInfoTypeForString('UNIT_OGRE'),				()),
							(eOrc,		3,	gc.getInfoTypeForString('UNIT_LONGBOWMAN'),			()),
							(eOrc,		3,	gc.getInfoTypeForString('UNIT_RANGER'),				(gc.getInfoTypeForString('PROMOTION_LIZARDMAN'),)),
							(eOrc,		3,	gc.getInfoTypeForString('UNIT_GIANT_COBRA'),		()),
							(eOrc,		3,	gc.getInfoTypeForString('UNIT_WOLF_CHARIOT'),		(gc.getInfoTypeForString('PROMOTION_GOBLIN'),)),
							(eOrc,		3,	gc.getInfoTypeForString('UNIT_SON_OF_THE_INFERNO'),	()),
							(eOrc,		4,	gc.getInfoTypeForString('UNIT_STONESKIN_OGRE'),		()),
							(eOrc,		4,	gc.getInfoTypeForString('UNIT_CROSSBOWMAN'),		()),
							(eOrc,		4,	gc.getInfoTypeForString('UNIT_BEASTMASTER'),		(gc.getInfoTypeForString('PROMOTION_LIZARDMAN'),)),
							(eOrc,		4,	gc.getInfoTypeForString('UNIT_SON_OF_THE_INFERNO'),	(gc.getInfoTypeForString('PROMOTION_TWINCAST'),
																								 gc.getInfoTypeForString('PROMOTION_SUMMONER'),)),
							(eOrc,		5,	gc.getInfoTypeForString('UNIT_DIAMOND_KNIGHT'),		()),
							(eAnimal,	0,	gc.getInfoTypeForString('UNIT_WOLF'),				()),
							(eAnimal,	1,	gc.getInfoTypeForString('UNIT_WOLF_PACK'),			(gc.getInfoTypeForString('PROMOTION_EMPOWER1'),
																								 gc.getInfoTypeForString('PROMOTION_EMPOWER2'),)),
							(eAnimal,	1,	gc.getInfoTypeForString('UNIT_LION'),				()),
							(eAnimal,	2,	gc.getInfoTypeForString('UNIT_SABERTIGER'),			(gc.getInfoTypeForString('PROMOTION_STRONG'),)),
							(eAnimal,	2,	gc.getInfoTypeForString('UNIT_GIANT_SPIDER'),		()),
							(eAnimal,	2,	gc.getInfoTypeForString('UNIT_RAVENOUS_WEREWOLF'),	()),
							(eAnimal,	3,	gc.getInfoTypeForString('UNIT_WEREWOLF'),			()),
							(eAnimal,	4,	gc.getInfoTypeForString('UNIT_GREATER_WEREWOLF'),	()),
							(eAnimal,	5,	gc.getInfoTypeForString('UNIT_GREATER_WEREWOLF'),	(gc.getInfoTypeForString('PROMOTION_STRONG'),
																								 gc.getInfoTypeForString('PROMOTION_MUSOU'),
																								 gc.getInfoTypeForString('PROMOTION_MARCH'),)),
							(eUndead,	0,	gc.getInfoTypeForString('UNIT_SKELETON'),			(gc.getInfoTypeForString('PROMOTION_WEAK'),)),
							(eUndead,	1,	gc.getInfoTypeForString('UNIT_SKELETON'),			()),
							(eUndead,	1,	gc.getInfoTypeForString('UNIT_PYRE_ZOMBIE'),		(gc.getInfoTypeForString('PROMOTION_WEAK'),)),
							(eUndead,	2,	gc.getInfoTypeForString('UNIT_SPECTRE'),			()),
							(eUndead,	2,	gc.getInfoTypeForString('UNIT_DISEASED_CORPSE'),	()),
							(eUndead,	3,	gc.getInfoTypeForString('UNIT_LICH'),				(gc.getInfoTypeForString('PROMOTION_DEATH1'),
																								 gc.getInfoTypeForString('PROMOTION_BODY1'),
																								 gc.getInfoTypeForString('PROMOTION_NECROMANCY'),
																								 gc.getInfoTypeForString('PROMOTION_FAST_CHANT'),)),
							(eUndead,	3,	gc.getInfoTypeForString('UNIT_LICH'),				(gc.getInfoTypeForString('PROMOTION_DEATH2'),)),
							(eUndead,	4,	gc.getInfoTypeForString('UNIT_WRAITH'),				(gc.getInfoTypeForString('PROMOTION_CANNIBALIZE'),)),
							(eUndead,	5,	gc.getInfoTypeForString('UNIT_LICH'),				(gc.getInfoTypeForString('PROMOTION_DEATH3'),
																								 gc.getInfoTypeForString('PROMOTION_NECROMANCY'),
																								 gc.getInfoTypeForString('PROMOTION_FAST_CHANT'),
																								 gc.getInfoTypeForString('PROMOTION_BODY1'),
																								 gc.getInfoTypeForString('PROMOTION_BODY2'),
																								 gc.getInfoTypeForString('PROMOTION_BODY3'),)),
							(eUndead,	5,	gc.getInfoTypeForString('UNIT_DRAGONLICHE'),		(gc.getInfoTypeForString('PROMOTION_FAST_CHANT'),))]

			if bHills:
				ltEnemies += [	(eOrc,		2,	gc.getInfoTypeForString('UNIT_HUNTER'),			(gc.getInfoTypeForString('PROMOTION_LIZARDMAN'),
																								 gc.getInfoTypeForString('PROMOTION_GUERILLA1'),)),
								(eAnimal,	2,	gc.getInfoTypeForString('UNIT_HILL_GIANT'),		(gc.getInfoTypeForString('PROMOTION_GUERILLA1'),
																								 gc.getInfoTypeForString('PROMOTION_STRONG'),)),
								(eAnimal,	2,	gc.getInfoTypeForString('UNIT_HILL_GIANT'),		(gc.getInfoTypeForString('PROMOTION_GUERILLA2'),
																								 gc.getInfoTypeForString('PROMOTION_STRONG'),))]

			if eFeature in (en.eFeatureForest, en.eFeatureForestAncient):
				ltEnemies += [	(eAnimal,	2,	gc.getInfoTypeForString('UNIT_FAWN'),			()),
								(eAnimal,	2,	gc.getInfoTypeForString('UNIT_FAWN'),			(gc.getInfoTypeForString('PROMOTION_TRACKING'),)),
								(eAnimal,	3,	gc.getInfoTypeForString('UNIT_SATYR'),			()),
								(eAnimal,	3,	gc.getInfoTypeForString('UNIT_TREANT'),			())]
			elif eFeature in (en.eFeatureJungle, en.eFeatureDeepJungle):
				ltEnemies += [	(eOrc,		2,	gc.getInfoTypeForString('UNIT_HUNTER'),			(gc.getInfoTypeForString('PROMOTION_LIZARDMAN'),
																								 gc.getInfoTypeForString('PROMOTION_POISONED_BLADE'),
																								 gc.getInfoTypeForString('PROMOTION_WOODSMAN1'),)),
								(eAnimal,	0,	gc.getInfoTypeForString('UNIT_BABY_SPIDER'),	()),
								(eAnimal,	1,	gc.getInfoTypeForString('UNIT_TIGER'),			()),
								(eAnimal,	1,	gc.getInfoTypeForString('UNIT_GORILLA'),		())]
			elif eFeature == en.eFeatureHauntedLands:
				ltEnemies += [	(eAnimal,	0,	gc.getInfoTypeForString('UNIT_CREEPER'),		(gc.getInfoTypeForString('PROMOTION_FED_CREEPER'),)),
								(eAnimal,	0,	gc.getInfoTypeForString('UNIT_CREEPER'),		(gc.getInfoTypeForString('PROMOTION_FED_CREEPER'),))]

			if eTerrain in (en.eTerrainSnow, en.eTerrainTundra):
				ltEnemies += [	(eFrostling,0,	gc.getInfoTypeForString('UNIT_SCOUT'),					(gc.getInfoTypeForString('PROMOTION_FROSTLING'),)),
								(eFrostling,0,	gc.getInfoTypeForString('UNIT_ICE_ELEMENTAL'),			()),
								(eFrostling,1,	gc.getInfoTypeForString('UNIT_ICE_ELEMENTAL'),			(gc.getInfoTypeForString('PROMOTION_MUSOU'),)),
								(eFrostling,1,	gc.getInfoTypeForString('UNIT_FROSTLING'),				()),
								(eFrostling,2,	gc.getInfoTypeForString('UNIT_ARCHER'),					(gc.getInfoTypeForString('PROMOTION_FROSTLING'),)),
								(eFrostling,2,	gc.getInfoTypeForString('UNIT_HUNTER'),					(gc.getInfoTypeForString('PROMOTION_FROSTLING'),)),
								(eFrostling,2,	gc.getInfoTypeForString('UNIT_WOLF_RIDER'),				(gc.getInfoTypeForString('PROMOTION_FROSTLING'),)),
								(eFrostling,2,	gc.getInfoTypeForString('UNIT_WOLF_RIDER'),				(gc.getInfoTypeForString('PROMOTION_FROSTLING'),)),
								(eFrostling,3,	gc.getInfoTypeForString('UNIT_FROST_GIANT'),			()),
								(eFrostling,3,	gc.getInfoTypeForString('UNIT_WHITE_FANG'),				()),
								(eFrostling,3,	gc.getInfoTypeForString('UNIT_WHITE_FANG'),				()),
								(eFrostling,3,	gc.getInfoTypeForString('UNIT_SNOW_LIZARD'),			()),
								(eFrostling,3,	gc.getInfoTypeForString('UNIT_DRUID_FROSTLING_NIVAL'),	()),
								(eFrostling,3,	gc.getInfoTypeForString('UNIT_SHADOWS_OF_ICE'),			()),
								(eFrostling,4,	gc.getInfoTypeForString('UNIT_ICE_STATUE'),				()),
								(eFrostling,4,	gc.getInfoTypeForString('UNIT_SNOWSTORM_AVATAR'),		()),
								(eFrostling,5,	gc.getInfoTypeForString('UNIT_SNOW_MONSTROSITY'),		())]
			elif eTerrain == en.eTerrainDesert:
				ltEnemies += [	(eAnimal,	1,	gc.getInfoTypeForString('UNIT_SCORPION'),		()),
								(eAnimal,	1,	gc.getInfoTypeForString('UNIT_SCORPION'),		(gc.getInfoTypeForString('PROMOTION_NOMAD'),)),
								(eAnimal,	2,	gc.getInfoTypeForString('UNIT_SAND_LION'),		()),
								(eAnimal,	2,	gc.getInfoTypeForString('UNIT_SAND_LION'),		()),
								(eOrc,		4,	gc.getInfoTypeForString('UNIT_AUREALIS'),		(gc.getInfoTypeForString('PROMOTION_SUN2'),))]
			elif eTerrain == en.eTerrainMarsh:
				ltEnemies += [	(eAnimal,	0,	gc.getInfoTypeForString('UNIT_TROLL'),			()),
								(eAnimal,	1,	gc.getInfoTypeForString('UNIT_TROLL'),			(gc.getInfoTypeForString('PROMOTION_GUERILLA2'),))]
			elif eTerrain in (en.eTerrainBurningSands, en.eTerrainBrokenLands, en.eTerrainFieldsofPerdition):
				ltEnemies += [	(eDemons,	4,	gc.getInfoTypeForString('UNIT_AHALPUH'),		(gc.getInfoTypeForString('PROMOTION_ENTROPY1'),
																								 gc.getInfoTypeForString('PROMOTION_SUMMONER'),
																								 gc.getInfoTypeForString('PROMOTION_TWINCAST'),)),
								(eDemons,	4,	gc.getInfoTypeForString('UNIT_AHALPUH'),		(gc.getInfoTypeForString('PROMOTION_FEAR'),)),
								(eDemons,	4,	gc.getInfoTypeForString('UNIT_AHALPUH'),		(gc.getInfoTypeForString('PROMOTION_ENTROPY2'),))]

			if iCounter > 20:
				ltEnemies += [	(eDemons,	0,	gc.getInfoTypeForString('UNIT_PIT_BEAST'),		()),
								(eDemons,	1,	gc.getInfoTypeForString('UNIT_IMP'),			(gc.getInfoTypeForString('PROMOTION_ENTROPY1'),)),
								(eDemons,	1,	gc.getInfoTypeForString('UNIT_IMP'),			(gc.getInfoTypeForString('PROMOTION_DEATH1'),)),
								(eDemons,	2,	gc.getInfoTypeForString('UNIT_MARCHOSIAS'),		()),
								(eDemons,	2,	gc.getInfoTypeForString('UNIT_MARCHOSIAS'),		()),
								(eDemons,	2,	gc.getInfoTypeForString('UNIT_MARCHOSIAS'),		(gc.getInfoTypeForString('PROMOTION_FORMATION'),)),
								(eDemons,	2,	gc.getInfoTypeForString('UNIT_TAR_DEMON'),		(gc.getInfoTypeForString('PROMOTION_EARTH1'),)),
								(eDemons,	2,	gc.getInfoTypeForString('UNIT_HELLHOUND'),		()),
								(eDemons,	2,	gc.getInfoTypeForString('UNIT_HELLHOUND'),		()),
								(eDemons,	3,	gc.getInfoTypeForString('UNIT_CHAOS_MARAUDER'),	(gc.getInfoTypeForString('PROMOTION_CHARGE'),)),
								(eDemons,	3,	gc.getInfoTypeForString('UNIT_CHAOS_MARAUDER'),	(gc.getInfoTypeForString('PROMOTION_STRONG'),)),
								(eDemons,	3,	gc.getInfoTypeForString('UNIT_CHAOS_MARAUDER'),	(gc.getInfoTypeForString('PROMOTION_SHOCK'),)),
								(eDemons,	3,	gc.getInfoTypeForString('UNIT_SUCCUBUS'),		())]
			if iCounter > 40:
				ltEnemies += [	(eDemons,	4,	gc.getInfoTypeForString('UNIT_BALOR'),			()),
								(eDemons,	4,	gc.getInfoTypeForString('UNIT_BALOR'),			(gc.getInfoTypeForString('PROMOTION_FEAR'),)),
								(eDemons,	4,	gc.getInfoTypeForString('UNIT_BALOR'),			(gc.getInfoTypeForString('PROMOTION_ENTROPY1'),)),
								(eDemons,	4,	gc.getInfoTypeForString('UNIT_DEATH_KNIGHT'),	()),
								(eDemons,	4,	gc.getInfoTypeForString('UNIT_EIDOLON'),		()),
								(eDemons,	5,	gc.getInfoTypeForString('UNIT_BEAST_OF_AGARES'),()),
								(eDemons,	5,	gc.getInfoTypeForString('UNIT_BEAST_OF_AGARES'),(gc.getInfoTypeForString('PROMOTION_SCOURGE'),
																								 gc.getInfoTypeForString('PROMOTION_STIGMATA'),
																								 gc.getInfoTypeForString('PROMOTION_MARCH'),)),
								(eDemons,	5,	gc.getInfoTypeForString('UNIT_BEAST_OF_AGARES'),(gc.getInfoTypeForString('PROMOTION_ENTROPY3'),))]

		# 追加昇進候補 (Forceが付かない方は兵科による取得制限を受け付ける)
		leForcePromotions = [	gc.getInfoTypeForString('PROMOTION_BLITZ'				),
								gc.getInfoTypeForString('PROMOTION_COMMAND1'			),
								gc.getInfoTypeForString('PROMOTION_HEROIC_DEFENSE'		),
								gc.getInfoTypeForString('PROMOTION_MAGIC_IMMUNE'		),
								gc.getInfoTypeForString('PROMOTION_SCOURGE'				),
								gc.getInfoTypeForString('PROMOTION_SKIRMISHER'			),
								gc.getInfoTypeForString('PROMOTION_STONESKIN'			),
								gc.getInfoTypeForString('PROMOTION_VALOR'				),
								gc.getInfoTypeForString('PROMOTION_VILE_TOUCH'			)	]
		lePromotions = []

		if iThreat > 1:
			leForcePromotions += [	gc.getInfoTypeForString('PROMOTION_CANNIBALIZE'		),
									gc.getInfoTypeForString('PROMOTION_HEROIC_STRENGTH'	),
									gc.getInfoTypeForString('PROMOTION_MOBILITY1'		),
									gc.getInfoTypeForString('PROMOTION_STRONG'			)	]
			lePromotions += [		gc.getInfoTypeForString('PROMOTION_ENCHANTED_BLADE'	),
									gc.getInfoTypeForString('PROMOTION_FLAMING_ARROWS'	),
									gc.getInfoTypeForString('PROMOTION_MUTATED'			),
									gc.getInfoTypeForString('PROMOTION_DUSKWOOD'		),
									gc.getInfoTypeForString('PROMOTION_DRAGONMETAL'		),
									gc.getInfoTypeForString('PROMOTION_KEEN_SIGHT'		),
									gc.getInfoTypeForString('PROMOTION_LONGRANGE'		),
									gc.getInfoTypeForString('PROMOTION_BARRAGE1'		),
									gc.getInfoTypeForString('PROMOTION_WILDANIMAL'		),
									gc.getInfoTypeForString('PROMOTION_EXTENSION1'		),
									gc.getInfoTypeForString('PROMOTION_POISONED_BLADE'	)	]
		if iThreat > 2:
			leForcePromotions += [	gc.getInfoTypeForString('PROMOTION_COLLECTOR'		),
									gc.getInfoTypeForString('PROMOTION_HERO'			),
									gc.getInfoTypeForString('PROMOTION_AIR2'			),
									gc.getInfoTypeForString('PROMOTION_FIRE2'			),
									gc.getInfoTypeForString('PROMOTION_IMPLACABLE'		)	]
			lePromotions += [		gc.getInfoTypeForString('PROMOTION_CHARGE'			),
									gc.getInfoTypeForString('PROMOTION_MARKSMAN'		),
									gc.getInfoTypeForString('PROMOTION_SHEUT_STONE'		),
									gc.getInfoTypeForString('PROMOTION_NIGHTMARE'		),
									gc.getInfoTypeForString('PROMOTION_SPELLSTAFF'		),
									gc.getInfoTypeForString('PROMOTION_ILLUSIONIST'		),
									gc.getInfoTypeForString('PROMOTION_INTENSIFICATION'	),
									gc.getInfoTypeForString('PROMOTION_BUFFALO'			),
									gc.getInfoTypeForString('PROMOTION_SERPENT'			),
									gc.getInfoTypeForString('PROMOTION_MOLE'			),
									gc.getInfoTypeForString('PROMOTION_BUTTERFLY'		)	]
		if iThreat > 4:
			leForcePromotions += [	gc.getInfoTypeForString('PROMOTION_DARK_MAGIC4'		),
									gc.getInfoTypeForString('PROMOTION_KODS_ITEMS'		),
									gc.getInfoTypeForString('PROMOTION_MUSOU'			)	]
			lePromotions += [		gc.getInfoTypeForString('PROMOTION_DEATH3'			),
									gc.getInfoTypeForString('PROMOTION_METAMAGIC3'		)	]

		if bWater:
			leForcePromotions += [	gc.getInfoTypeForString('PROMOTION_WATER_WALKING'	)	]
		if bHills:
			lePromotions += [		gc.getInfoTypeForString('PROMOTION_GUERILLA1'		)	]
		if eFeature in (en.eFeatureForest, en.eFeatureForestAncient, en.eFeatureJungle, en.eFeatureDeepJungle):
			lePromotions += [		gc.getInfoTypeForString('PROMOTION_WOODSMAN1'		)	]
		elif eFeature == en.eFeatureHauntedLands:
			lePromotions += [		gc.getInfoTypeForString('PROMOTION_DEATH1'			)	]
		elif eFeature == en.eFeatureSwamp:
			lePromotions += [		gc.getInfoTypeForString('PROMOTION_GUERILLA1'		)	]
		if eTerrain in (en.eTerrainSnow, en.eTerrainTundra):
			leForcePromotions += [	gc.getInfoTypeForString('PROMOTION_COLD_RESISTANCE'	)	]
		elif eTerrain == en.eTerrainDesert:
			leForcePromotions += [	gc.getInfoTypeForString('PROMOTION_FIRE_RESISTANCE'	)	]
		elif eTerrain in (en.eTerrainBurningSands, en.eTerrainBrokenLands, en.eTerrainFieldsofPerdition, en.eTerrainShallows):
			leForcePromotions += [	gc.getInfoTypeForString('PROMOTION_DARK_MAGIC1'		)	]
		if iCounter > 20:
			leForcePromotions += [	gc.getInfoTypeForString('PROMOTION_STIGMATA'		)	]
		if iCounter > 40:
			leForcePromotions += [	gc.getInfoTypeForString('PROMOTION_FEAR'			)	]

		# 強大な敵と取り巻きのユニットを決定
		leMonsters	= []
		leHenchmans	= []
		for eBarbarianPlayer, iTier, eUnitType, leDefaultPromotions in ltEnemies:
			if eBarbarianPlayer in leEnemyBarbarian:
				if iTier == iThreat:
					leMonsters.append((eBarbarianPlayer, iTier, eUnitType, leDefaultPromotions))
		if len(leMonsters) > 0:
			# 強大な敵
			eMonsterPlayer, iMonsterTier, eMonsterUnit, leMonsterPromotions = leMonsters[CyGame().getSorenRandNum(len(leMonsters), "Pick Monster")]
		else:
			doCasterKill()
			return

		for eBarbarianPlayer, iTier, eUnitType, leDefaultPromotions in ltEnemies:
			if eBarbarianPlayer == eMonsterPlayer:
				if iTier < iThreat:
					leHenchmans.append((eBarbarianPlayer, iTier, eUnitType, leDefaultPromotions))
		if len(leHenchmans) > 0:
			# 取り巻き
			eHenchmanPlayer, iHenchmanTier, eHenchmanUnit, leHenchmanPromotions = leHenchmans[CyGame().getSorenRandNum(len(leHenchmans), "Pick Monster")]
			iNumHenchmans += ((iMonsterTier - iHenchmanTier) * 3) // 2
		else:
			iNumHenchmans = 0

		# 強大な敵の生成
		pNewPlot = self.findClearPlot(-1, pPlot)
		if pNewPlot != -1:
			pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER() + eMonsterPlayer)
			pNewUnit = pBarbarianPlayer.initUnit(eMonsterUnit, pNewPlot.getX(), pNewPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		else:
			doCasterKill()
			return

		if pNewUnit is not None:
			# 以下、強大な敵へのテコ入れ
			if pNewUnit.getUnitAIType() in (UnitAITypes.UNITAI_ANIMAL, UnitAITypes.UNITAI_EXPLORE):
				pNewUnit.setUnitAIType(UnitAITypes.UNITAI_ATTACK)
			# apply default promotions
			for eDefaultPromotion in leMonsterPromotions:
				pNewUnit.setHasPromotion(eDefaultPromotion, True)

			# create extra promotion table
			leValidPromotions = []
			if pNewUnit.getUnitCombatType() != UnitCombatTypes.NO_UNITCOMBAT:
				leValidPromotions += [ePromotion for ePromotion in lePromotions if gc.getPromotionInfo(ePromotion).getUnitCombat(pNewUnit.getUnitCombatType())]
			leValidPromotions += leForcePromotions
			for ePromotion in leValidPromotions:
				if pNewUnit.isHasPromotion(ePromotion):
					leValidPromotions.remove(ePromotion)

			# apply extra promotions
			iProbability = 80 + iThreat * 20
			for iLoop in xrange(10):
				if CyGame().getSorenRandNum(100, "Pick Promotion") < iProbability:
					ePromotion = leValidPromotions.pop(CyGame().getSorenRandNum(len(leValidPromotions), "Pick Promotion Type"))
					pNewUnit.setHasPromotion(ePromotion, True)
					iProbability //= 2
				else:
					break
			if pNewUnit.getCombatAttackTimes100() + pNewUnit.getCombatDefenseTimes100() <= 700:
				pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STRONG'), True)

			# apply weapon
			iWeaponTierCap = min(gc.getUnitInfo(pNewUnit.getUnitType()).getWeaponTier(), iWeaponTier)
			if iWeaponTierCap > 0:
				iRandomTier = CyGame().getSorenRandNum(gc.getNumWeaponInfos() + 1, "Pick Weapon Type")
				if 0 < iRandomTier <= iWeaponTierCap:
					for iWeapon in xrange(gc.getNumWeaponInfos()):
						if gc.getWeaponInfo(iWeapon).getWeaponTier() == iRandomTier:
							pNewUnit.setHasPromotion(gc.getWeaponInfo(iWeapon).getWeaponPromotion(), True)
							break

			pNewUnit.setName(self.MarnokNameGenerator(pNewUnit))
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BIGBAD",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorRed, pNewUnit.getX(), pNewUnit.getY(), True, True)

			# 取り巻きの生成
			iNumHenchmans = CyGame().getSorenRandNum(iNumHenchmans, "Pick the Number of Henchmen")
			for iLoop in xrange(iNumHenchmans):
				pNewHenchmanUnit = pBarbarianPlayer.initUnit(eHenchmanUnit, pNewUnit.getX(), pNewUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
				for eDefaultPromotion in leHenchmanPromotions:
					pNewHenchmanUnit.setHasPromotion(eDefaultPromotion, True)
			return

		doCasterKill()
		return
# ent <<<

	def exploreLairBad(self, pCaster):
		iPlayer = pCaster.getOwner()
		pPlot = pCaster.plot()
		pPlayer = gc.getPlayer(iPlayer)
		pLairInfo = gc.getImprovementInfo(pPlot.getImprovementType())

# ent >>>
		pTeam = gc.getTeam(pPlayer.getTeam())
		pBarbarianOrc = gc.getPlayer(gc.getBARBARIAN_PLAYER() + en.eBarbarianOrc)
		bAtWarWithOrc = (pTeam.isAtWar(pBarbarianOrc.getTeam()))
		pBarbarianAnimal = gc.getPlayer(gc.getBARBARIAN_PLAYER() + en.eBarbarianAnimal)
		bAtWarWithAnimal = (pTeam.isAtWar(pBarbarianAnimal.getTeam()))
		pBarbarianUndead = gc.getPlayer(gc.getBARBARIAN_PLAYER() + en.eBarbarianUndead)
		bAtWarWithUndead = (pTeam.isAtWar(pBarbarianUndead.getTeam()))
		pBarbarianFrostling = gc.getPlayer(gc.getBARBARIAN_PLAYER() + en.eBarbarianFrostling)
		bAtWarWithFrostling = (pTeam.isAtWar(pBarbarianFrostling.getTeam()))

		lList = ['COLLAPSE']
		if pCaster.getLevel() == 1:
			lList += ['DEATH']
		if pCaster.isAlive():
			lList += ['CRAZED', 'DEMONIC_POSSESSION', 'DISEASED', 'ENRAGED', 'PLAGUED', 'POISONED', 'WITHERED']
		if pCaster.getUnitCombatType() == en.eUnitCombatMelee:
			lList += ['RUSTED']
		if pPlot.isWater():
#			lList += ['SPAWN_DROWN', 'SPAWN_SEA_SERPENT']
			if bAtWarWithAnimal:
				lList += ['SPAWN_SEA_SERPENT']
			if bAtWarWithUndead:
				lList += ['SPAWN_DROWN']
			"""
		if not pPlot.isWater():
#			lList += ['SPAWN_SPIDER', 'SPAWN_SPECTRE']
			if bAtWarWithAnimal:
				lList += ['SPAWN_SPIDER']
			if bAtWarWithUndead:
				lList += ['SPAWN_SPECTRE']
		if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_GOBLIN_FORT'):
#			lList += ['SPAWN_SCORPION_BAD', 'SPAWN_SCORPION_BAD', 'SPAWN_SCORPION_BAD']
			if bAtWarWithAnimal:
				lList += ['SPAWN_SCORPION_BAD', 'SPAWN_SCORPION_BAD', 'SPAWN_SCORPION_BAD']
			"""
		else:
			if bAtWarWithOrc:
				lList += ['SPAWN_LIZARDMAN']
			if bAtWarWithAnimal:
				lList += ['SPAWN_SPIDER', 'SPAWN_SCORPION']
				if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_GOBLIN_FORT'):
					lList += ['SPAWN_SCORPION_BAD']
			if bAtWarWithUndead:
				lList += ['SPAWN_SKELETON', 'SPAWN_SPECTRE']
			if pPlot.getTerrainType() == en.eTerrainSnow:
				if bAtWarWithFrostling:
					lList += ['SPAWN_FROSTLING']
# ent <<<
		sGoody = lList[CyGame().getSorenRandNum(len(lList), "Pick Goody")]
		if sGoody == 'DEATH':
			pCaster.kill(True, PlayerTypes.NO_PLAYER)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_DEATH", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pLairInfo.getButton(), en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
			return 0
		elif sGoody == 'COLLAPSE':
			pCaster.doDamage(50, 90, gc.getInfoTypeForString('DAMAGE_PHYSICAL'))
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_COLLAPSE", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pLairInfo.getButton(), en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'CRAZED':
			iPromotion = gc.getInfoTypeForString('PROMOTION_CRAZED')
			pCaster.setHasPromotion(iPromotion, True)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_CRAZED", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getPromotionInfo(iPromotion).getButton(), en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
			return 80
		elif sGoody == 'DEMONIC_POSSESSION':
# ent >>>
#			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENRAGED'), True)
#			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CRAZED'), True)
			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FERAL'), True)
			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INSTABILITY'), True)
# ent <<<
			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_POSSESSED", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Units/UCDemon.dds', en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
			return 80
		elif sGoody == 'DISEASED':
			iPromotion = gc.getInfoTypeForString('PROMOTION_DISEASED')
			pCaster.setHasPromotion(iPromotion, True)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_DISEASED", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getPromotionInfo(iPromotion).getButton(), en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
			return 80
		elif sGoody == 'ENRAGED':
			iPromotion = gc.getInfoTypeForString('PROMOTION_ENRAGED')
			pCaster.setHasPromotion(iPromotion, True)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_ENRAGED", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getPromotionInfo(iPromotion).getButton(), en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
			return 80
		elif sGoody == 'PLAGUED':
			iPromotion = gc.getInfoTypeForString('PROMOTION_PLAGUED')
			pCaster.setHasPromotion(iPromotion, True)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_PLAGUED", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getPromotionInfo(iPromotion).getButton(), en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
			return 80
		elif sGoody == 'POISONED':
			iPromotion = gc.getInfoTypeForString('PROMOTION_POISONED')
			pCaster.setHasPromotion(iPromotion, True)
			pCaster.doDamage(25, 90, gc.getInfoTypeForString('DAMAGE_POISON'))
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_POISONED", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getPromotionInfo(iPromotion).getButton(), en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
			return 80
		elif sGoody == 'WITHERED':
			iPromotion = gc.getInfoTypeForString('PROMOTION_WITHERED')
			pCaster.setHasPromotion(iPromotion, True)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_WITHERED", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getPromotionInfo(iPromotion).getButton(), en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
			return 80
		elif sGoody == 'RUSTED':
			iPromotion = gc.getInfoTypeForString('PROMOTION_RUSTED')
			pCaster.setHasPromotion(iPromotion, True)
			for iWeapon in xrange(gc.getNumWeaponInfos()):
				pCaster.setHasPromotion(gc.getWeaponInfo(iWeapon).getWeaponPromotion(), False)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_RUSTED", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getPromotionInfo(iPromotion).getButton(), en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
			return 80
		elif sGoody == 'SPAWN_DROWN':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_DROWN'), pCaster)
			return 50
		elif sGoody == 'SPAWN_SCORPION_BAD':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_SCORPION_BAD'), pCaster)
			return 50
		elif sGoody == 'SPAWN_SEA_SERPENT':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_SEA_SERPENT'), pCaster)
			return 50
		elif sGoody == 'SPAWN_SPECTRE':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_GRAVE_SPECTRE'), pCaster)
			return 50
		elif sGoody == 'SPAWN_SPIDER':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_SPIDER'), pCaster)
			return 50
# ent >>>
		elif sGoody == 'SPAWN_LIZARDMAN':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_LIZARDMAN'), pCaster)
			return 50
		elif sGoody == 'SPAWN_SCORPION':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_SCORPION'), pCaster)
			return 50
		elif sGoody == 'SPAWN_SKELETON':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_SKELETON'), pCaster)
			return 50
		elif sGoody == 'SPAWN_FROSTLING':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_FROSTLING'), pCaster)
			return 50
# ent <<<
		return 100

	def exploreLairNeutral(self, pCaster):
		iPlayer = pCaster.getOwner()
		pPlot = pCaster.plot()
		pPlayer = gc.getPlayer(iPlayer)
		pLairInfo = gc.getImprovementInfo(pPlot.getImprovementType())

# ent >>>
		pTeam = gc.getTeam(pPlayer.getTeam())
		pBarbarianOrc = gc.getPlayer(gc.getBARBARIAN_PLAYER() + en.eBarbarianOrc)
		bAtWarWithOrc = (pTeam.isAtWar(pBarbarianOrc.getTeam()))
		pBarbarianAnimal = gc.getPlayer(gc.getBARBARIAN_PLAYER() + en.eBarbarianAnimal)
		bAtWarWithAnimal = (pTeam.isAtWar(pBarbarianAnimal.getTeam()))
		pBarbarianUndead = gc.getPlayer(gc.getBARBARIAN_PLAYER() + en.eBarbarianUndead)
		bAtWarWithUndead = (pTeam.isAtWar(pBarbarianUndead.getTeam()))
		pBarbarianFrostling = gc.getPlayer(gc.getBARBARIAN_PLAYER() + en.eBarbarianFrostling)
		bAtWarWithFrostling = (pTeam.isAtWar(pBarbarianFrostling.getTeam()))

		lList = ['NOTHING']
		"""
		if not pPlot.isWater():
#			lList += ['SPAWN_SKELETON', 'SPAWN_LIZARDMAN', 'SPAWN_SPIDER', 'PORTAL', 'DEPTHS', 'DWARF_VS_LIZARDMEN', 'CAGE']
			lList += ['PORTAL', 'DEPTHS', 'CAGE']
			if bAtWarWithOrc:
				lList += ['SPAWN_LIZARDMAN', 'DWARF_VS_LIZARDMEN']
			if bAtWarWithAnimal:
				lList += ['SPAWN_SPIDER']
			if bAtWarWithUndead:
				lList += ['SPAWN_SKELETON']
			if pPlot.getTerrainType() == en.eTerrainSnow:
#				lList += ['SPAWN_FROSTLING']
				if bAtWarWithFrostling:
					lList += ['SPAWN_FROSTLING']
			if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_BARROW'):
#				lList += ['SPAWN_SKELETON', 'SPAWN_SKELETON']
				if bAtWarWithUndead:
					lList += ['SPAWN_SKELETON', 'SPAWN_SKELETON']
			if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_RUINS'):
#				lList += ['SPAWN_LIZARDMAN', 'SPAWN_LIZARDMAN']
				if bAtWarWithOrc:
					lList += ['SPAWN_LIZARDMAN', 'SPAWN_LIZARDMAN']
			if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_GOBLIN_FORT'):
#				lList += ['SPAWN_SCORPION', 'SPAWN_SCORPION', 'SPAWN_SCORPION']
				if bAtWarWithAnimal:
					lList += ['SPAWN_SCORPION', 'SPAWN_SCORPION', 'SPAWN_SCORPION']
		if pPlot.isWater():
#			lList += ['SPAWN_DROWN']
			if bAtWarWithUndead:
				lList += ['SPAWN_DROWN']
		"""
		if not pPlot.isWater():
			lList += ['PORTAL', 'DEPTHS']
			if bAtWarWithOrc:
				lList += ['DWARF_VS_LIZARDMEN']
# ent <<<
		if pCaster.isAlive():
			if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MUTATED')):
				lList += ['MUTATED']

		sGoody = lList[CyGame().getSorenRandNum(len(lList), "Pick Goody")]
		"""
		if sGoody == 'CAGE':
			iCage = gc.getInfoTypeForString('IMPROVEMENT_CAGE')
			pPlot.setImprovementType(iCage)
			for iUnitIndex in xrange(pPlot.getNumUnits(), -1, -1):
				pUnit = pPlot.getUnit(iUnitIndex)
				if pUnit.isDuration():
					pUnit.disableImmortal()
					pUnit.kill(False, PlayerTypes.NO_PLAYER)
				else:
					iDuration = cyFlatValue(24, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
					pUnit.setDuration(iDuration)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HELD'), True)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_CAGE",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getImprovementInfo(iCage).getButton(), en.eColorRed,pCaster.getX(),pCaster.getY(), True, True)
			return 0
		"""
		if sGoody == 'DEPTHS':
			iUnitID = self.getUnitPlayerID(pCaster)
			if iUnitID != -1:
				iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(), 'EVENTTRIGGER_EXPLORE_LAIR_DEPTHS')
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#				triggerData = pPlayer.initTriggeredData(iEvent, True, -1, pCaster.getX(), pCaster.getY(), PlayerTypes.NO_PLAYER, -1, ReligionTypes.NO_RELIGION, CorporationTypes.NO_CORPORATION, iUnitID, BuildingTypes.NO_BUILDING)
				pPlayer.triggerCustomEvent(iEvent, -1, pCaster.getX(), pCaster.getY(), PlayerTypes.NO_PLAYER, -1, ReligionTypes.NO_RELIGION, CorporationTypes.NO_CORPORATION, iUnitID, BuildingTypes.NO_BUILDING)
##--------	Unofficial Bug Fix: End Modify			--------##
			return 0	# must not destroy dungeon before exploring depth !!
		elif sGoody == 'DWARF_VS_LIZARDMEN':
			iUnitID = self.getUnitPlayerID(pCaster)
			if iUnitID != -1:
				iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(), 'EVENTTRIGGER_EXPLORE_LAIR_DWARF_VS_LIZARDMEN')
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#				triggerData = pPlayer.initTriggeredData(iEvent, True, -1, pCaster.getX(), pCaster.getY(), PlayerTypes.NO_PLAYER, -1, ReligionTypes.NO_RELIGION, CorporationTypes.NO_CORPORATION, iUnitID, BuildingTypes.NO_BUILDING)
				pPlayer.triggerCustomEvent(iEvent, -1, pCaster.getX(), pCaster.getY(), PlayerTypes.NO_PLAYER, -1, ReligionTypes.NO_RELIGION, CorporationTypes.NO_CORPORATION, iUnitID, BuildingTypes.NO_BUILDING)
##--------	Unofficial Bug Fix: End Modify			--------##
			return 100
		elif sGoody == 'MUTATED':
			iPromotion = gc.getInfoTypeForString('PROMOTION_MUTATED')
			pCaster.setHasPromotion(iPromotion, True)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_MUTATED",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getPromotionInfo(iPromotion).getButton(), en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
			return 50
		elif sGoody == 'NOTHING':
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_NOTHING",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pLairInfo.getButton(), en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'PORTAL':
			iUnitID = self.getUnitPlayerID(pCaster)
			if iUnitID != -1:
				iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(), 'EVENTTRIGGER_EXPLORE_LAIR_PORTAL')
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#				triggerData = pPlayer.initTriggeredData(iEvent, True, -1, pCaster.getX(), pCaster.getY(), PlayerTypes.NO_PLAYER, -1, ReligionTypes.NO_RELIGION, CorporationTypes.NO_CORPORATION, iUnitID, BuildingTypes.NO_BUILDING)
				pPlayer.triggerCustomEvent(iEvent, -1, pCaster.getX(), pCaster.getY(), PlayerTypes.NO_PLAYER, -1, ReligionTypes.NO_RELIGION, CorporationTypes.NO_CORPORATION, iUnitID, BuildingTypes.NO_BUILDING)
##--------	Unofficial Bug Fix: End Modify			--------##
			return 0
		"""
		elif sGoody == 'SPAWN_DROWN':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_DROWN'), pCaster)
			return 50
		elif sGoody == 'SPAWN_FROSTLING':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_FROSTLING'), pCaster)
			return 50
		elif sGoody == 'SPAWN_LIZARDMAN':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_LIZARDMAN'), pCaster)
			return 50
		elif sGoody == 'SPAWN_SCORPION':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_SCORPION'), pCaster)
			return 50
		elif sGoody == 'SPAWN_SKELETON':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_SKELETON'), pCaster)
			return 50
		elif sGoody == 'SPAWN_SPIDER':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SPAWN_SPIDER'), pCaster)
			return 50
		"""
		return 100

	def exploreLairGood(self, pCaster):
		iPlayer = pCaster.getOwner()
		pPlot = pCaster.plot()
		pPlayer = gc.getPlayer(iPlayer)
#		lList = ['HIGH_GOLD', 'TREASURE', 'EXPERIENCE']
		lList = ['HIGH_GOLD', 'EXPERIENCE']
		if pCaster.isAlive():
			if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SPIRIT_GUIDE')):
				lList += ['SPIRIT_GUIDE']
		if not pPlot.isWater():
			lList += ['ITEM_HEALING_SALVE', 'SUPPLIES']
			if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_MYSTICISM')):
#				lList += ['PRISONER_DISCIPLE_ASHEN', 'PRISONER_DISCIPLE_EMPYREAN', 'PRISONER_DISCIPLE_LEAVES', 'PRISONER_DISCIPLE_OVERLORDS', 'PRISONER_DISCIPLE_RUNES', 'PRISONER_DISCIPLE_ORDER']
				if CyGame().isReligionFounded(en.eReligionAshenVeil):
					lList += ['PRISONER_DISCIPLE_ASHEN']
				if CyGame().isReligionFounded(en.eReligionEmpyrean):
					lList += ['PRISONER_DISCIPLE_EMPYREAN']
				if CyGame().isReligionFounded(en.eReligionFellowshipofLeaves):
					lList += ['PRISONER_DISCIPLE_LEAVES']
				if CyGame().isReligionFounded(en.eReligionOctopusOverlords):
					lList += ['PRISONER_DISCIPLE_OVERLORDS']
				if CyGame().isReligionFounded(en.eReligionRunesofKilmorph):
					lList += ['PRISONER_DISCIPLE_RUNES']
				if CyGame().isReligionFounded(en.eReligionOrder):
					lList += ['PRISONER_DISCIPLE_ORDER']
		if pCaster.getUnitCombatType() == en.eUnitCombatMelee:
			if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ENCHANTED_BLADE')):
				lList += ['ENCHANTED_BLADE']
		elif pCaster.getUnitCombatType() == en.eUnitCombatAdept:
			if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SPELLSTAFF')):
				lList += ['SPELLSTAFF']
		elif pCaster.getUnitCombatType() == en.eUnitCombatRecon:
			if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED_BLADE')):
				lList += ['POISONED_BLADE']
		elif pCaster.getUnitCombatType() == en.eUnitCombatArcher:
			if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_FLAMING_ARROWS')):
				lList += ['FLAMING_ARROWS']
		elif pCaster.getUnitCombatType() == en.eUnitCombatDisciple:
			if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SHIELD_OF_FAITH')):
				lList += ['SHIELD_OF_FAITH']
		if gc.getUnitInfo(pCaster.getUnitType()).getWeaponTier() >= 1:
			if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MITHRIL_WEAPONS')):
				if (gc.getUnitInfo(pCaster.getUnitType()).getWeaponTier() >= 3 and pPlayer.isHasTech(gc.getInfoTypeForString('TECH_IRON_WORKING'))):
					lList += ['MITHRIL_WEAPONS']
				if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS')):
					if (gc.getUnitInfo(pCaster.getUnitType()).getWeaponTier() >= 2 and pPlayer.isHasTech(gc.getInfoTypeForString('TECH_BRONZE_WORKING'))):
						lList += ['IRON_WEAPONS']
					if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS')):
						lList += ['BRONZE_WEAPONS']

		sGoody = lList[CyGame().getSorenRandNum(len(lList), "Pick Goody")]
		if sGoody == 'HIGH_GOLD':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_HIGH_GOLD'), pCaster)
			return 90
		elif sGoody == 'SUPPLIES':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_SUPPLIES'), pCaster)
			return 100
			"""
		elif sGoody == 'TREASURE':
#			self.placeTreasure(iPlayer, gc.getInfoTypeForString('EQUIPMENT_TREASURE'))
			self.placeTreasure(iPlayer, gc.getInfoTypeForString('UNIT_TREASURE'))
			return 80
			"""
		elif sGoody == 'EXPERIENCE':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_EXPERIENCE'), pCaster)
			return 100
		elif sGoody == 'SPIRIT_GUIDE':
			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SPIRIT_GUIDE'), True)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_SPIRIT_GUIDE",()), 'AS2D_POSITIVE_DINK', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Promotions/SpiritGuide.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 80
		elif sGoody == 'ITEM_HEALING_SALVE':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_HEALING_SALVE'), pCaster)
			return 100
		elif sGoody == 'ITEM_POTION_OF_INVISIBILITY':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_POTION_OF_INVISIBILITY'), pCaster)
			return 100
		elif sGoody == 'ITEM_POTION_OF_RESTORATION':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_POTION_OF_RESTORATION'), pCaster)
			return 100
		elif sGoody == 'ENCHANTED_BLADE':
			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENCHANTED_BLADE'), True)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_ENCHANTED_BLADE",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Promotions/EnchantedBlade.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'SPELLSTAFF':
			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SPELLSTAFF'), True)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_SPELLSTAFF",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Promotions/Spellstaff.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'POISONED_BLADE':
			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED_BLADE'), True)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_POISONED_BLADE",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Promotions/PoisonedBlade.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'FLAMING_ARROWS':
			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FLAMING_ARROWS'), True)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_FLAMING_ARROWS",()), 'AS2D_POSITIVE_DINK', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Promotions/FlamingArrows.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'PRISONER_DISCIPLE_ASHEN':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_DISCIPLE_ASHEN'), pCaster)
			return 100
		elif sGoody == 'PRISONER_DISCIPLE_EMPYREAN':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_DISCIPLE_EMPYREAN'), pCaster)
			return 100
		elif sGoody == 'PRISONER_DISCIPLE_LEAVES':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_DISCIPLE_LEAVES'), pCaster)
			return 100
		elif sGoody == 'PRISONER_DISCIPLE_OVERLORDS':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_DISCIPLE_OVERLORDS'), pCaster)
			return 100
		elif sGoody == 'PRISONER_DISCIPLE_RUNES':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_DISCIPLE_RUNES'), pCaster)
			return 100
		elif sGoody == 'PRISONER_DISCIPLE_ORDER':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_DISCIPLE_ORDER'), pCaster)
			return 100
		elif sGoody == 'SHIELD_OF_FAITH':
			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SHIELD_OF_FAITH'), True)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_SHIELD_OF_FAITH",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Promotions/ShieldOfFaith.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'BRONZE_WEAPONS':
			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_RUSTED'), False)
			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS'), True)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BRONZE_WEAPONS",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Promotions/BronzeWeapons.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'IRON_WEAPONS':
			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_RUSTED'), False)
			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS'), True)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_IRON_WEAPONS",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Promotions/IronWeapons.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'MITHRIL_WEAPONS':
			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_RUSTED'), False)
			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MITHRIL_WEAPONS'), True)
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_MITHRIL_WEAPONS",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Promotions/MithrilWeapons.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		return 100

	def exploreLairBigGood(self, pCaster):
		iPlayer = pCaster.getOwner()
		pPlot = pCaster.plot()
		pPlayer = gc.getPlayer(iPlayer)
		pLairInfo = gc.getImprovementInfo(pPlot.getImprovementType())

# Kaijin >>> Orbis Equipments
#		lList = ['TREASURE_VAULT', 'GOLDEN_AGE']
		lList = [	'TREASURE_VAULT', 
					'GOLDEN_AGE', 
					'ITEM_MUTATION_POTION', 
					'ITEM_HEART_AMULET', 
					'ITEM_SWIFT_BOOTS', 
					'ITEM_TRAVELLERS_CLOAK', 
					'ITEM_RING_OF_PERCEPTION', 
					'ITEM_RING_OF_STRIKING', 
					'ITEM_COMPELLING_JEWEL', 
					'ITEM_CURSED_TOKEN_OF_RAGNAROK', 
					'ITEM_STARVATION_HELM', 
					'ITEM_HAUBERK_OF_ABJURATION', 
					'ITEM_BUG_DA_RAKE'				]
# Kaijin<<<
		if pPlayer.canReceiveGoody(pPlot, gc.getInfoTypeForString('GOODY_GRAVE_TECH'), pCaster):
			lList += ['TECH']
		if not pPlot.isWater():
			lList += ['ITEM_JADE_TORC', 'ITEM_ROD_OF_WINDS', 'ITEM_TIMOR_MASK', 'PRISONER_ADVENTURER', 'PRISONER_ARTIST', 'PRISONER_COMMANDER', 'PRISONER_ENGINEER', 'PRISONER_MERCHANT', 'PRISONER_PROPHET', 'PRISONER_SCIENTIST']
			if pPlot.getBonusType(TeamTypes.NO_TEAM) == BonusTypes.NO_BONUS:
				lList += ['BONUS_MANA']
				lList += ['BONUS_GEMS', 'BONUS_GOLD']
				if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_MINING')):
					lList += ['BONUS_COPPER']
				if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_SMELTING')):
					lList += ['BONUS_IRON']
		if pPlot.isWater():
			lList += ['PRISONER_SEA_SERPENT']
			if pPlot.getBonusType(TeamTypes.NO_TEAM) == BonusTypes.NO_BONUS:
				lList += ['BONUS_CLAM', 'BONUS_CRAB', 'BONUS_FISH']
		if not self.grace():
			lList += ['PRISONER_ANGEL', 'PRISONER_MONK', 'PRISONER_ASSASSIN', 'PRISONER_CHAMPION', 'PRISONER_MAGE']
		sGoody = lList[CyGame().getSorenRandNum(len(lList), "Pick Goody")]

		if sGoody == 'TREASURE_VAULT':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_TREASURE_VAULT'), pCaster)
			return 100
# Kaijin >>> Orbis Equipments
		elif sGoody == 'ITEM_MUTATION_POTION':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_MUTATION_POTION'), pCaster)
			return 100
		elif sGoody == 'ITEM_HEART_AMULET':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_HEART_AMULET'), pCaster)
			return 100
		elif sGoody == 'ITEM_SWIFT_BOOTS':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_SWIFT_BOOTS'), pCaster)
			return 100
		elif sGoody == 'ITEM_TRAVELLERS_CLOAK':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_TRAVELLERS_CLOAK'), pCaster)
			return 100
		elif sGoody == 'ITEM_RING_OF_PERCEPTION':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_RING_OF_PERCEPTION'), pCaster)
			return 100
		elif sGoody == 'ITEM_RING_OF_STRIKING':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_RING_OF_STRIKING'), pCaster)
			return 100
		elif sGoody == 'ITEM_COMPELLING_JEWEL':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_COMPELLING_JEWEL'), pCaster)
			return 100
		elif sGoody == 'ITEM_CURSED_TOKEN_OF_RAGNAROK':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_CURSED_TOKEN_OF_RAGNAROK'), pCaster)
			return 100
		elif sGoody == 'ITEM_STARVATION_HELM':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_STARVATION_HELM'), pCaster)
			return 100
		elif sGoody == 'ITEM_HAUBERK_OF_ABJURATION':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_HAUBERK_OF_ABJURATION'), pCaster)
			return 100
		elif sGoody == 'ITEM_BUG_DA_RAKE':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_BUG_DA_RAKE'), pCaster)
			return 100
# Kaijin <<<
		elif sGoody == 'BONUS_CLAM':
			pPlot.setBonusType(gc.getInfoTypeForString('BONUS_CLAM'))
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BONUS_CLAM",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/WorldBuilder/Clam.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'BONUS_COPPER':
			pPlot.setBonusType(gc.getInfoTypeForString('BONUS_COPPER'))
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BONUS_COPPER",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/WorldBuilder/Copper.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'BONUS_CRAB':
			pPlot.setBonusType(gc.getInfoTypeForString('BONUS_CRAB'))
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BONUS_CRAB",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/WorldBuilder/Crab.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'BONUS_FISH':
			pPlot.setBonusType(gc.getInfoTypeForString('BONUS_FISH'))
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BONUS_FISH",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/WorldBuilder/Fish.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'BONUS_GOLD':
			pPlot.setBonusType(gc.getInfoTypeForString('BONUS_GOLD'))
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BONUS_GOLD",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/WorldBuilder/Gold.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'BONUS_GEMS':
			pPlot.setBonusType(gc.getInfoTypeForString('BONUS_GEMS'))
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BONUS_GEMS",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/WorldBuilder/Gems.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'BONUS_IRON':
			pPlot.setBonusType(gc.getInfoTypeForString('BONUS_IRON'))
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BONUS_IRON",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/WorldBuilder/Iron.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'BONUS_MANA':
			pPlot.setBonusType(gc.getInfoTypeForString('BONUS_MANA'))
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_BONUS_MANA",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/WorldBuilder/mana_button.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'GOLDEN_AGE':
			pPlayer.changeGoldenAgeTurns(CyGame().goldenAgeLength())
			CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_GOLDEN_AGE",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pLairInfo.getButton(), en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			return 100
		elif sGoody == 'ITEM_JADE_TORC':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_JADE_TORC'), pCaster)
			return 100
		elif sGoody == 'ITEM_ROD_OF_WINDS':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_ROD_OF_WINDS'), pCaster)
			return 100
		elif sGoody == 'ITEM_TIMOR_MASK':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_ITEM_TIMOR_MASK'), pCaster)
			return 100
		elif sGoody == 'PRISONER_ADVENTURER':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_ADVENTURER'), pCaster)
			return 100
		elif sGoody == 'PRISONER_ANGEL':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_ANGEL'), pCaster)
			return 100
		elif sGoody == 'PRISONER_ARTIST':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_ARTIST'), pCaster)
			return 100
		elif sGoody == 'PRISONER_ASSASSIN':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_ASSASSIN'), pCaster)
			return 100
		elif sGoody == 'PRISONER_CHAMPION':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_CHAMPION'), pCaster)
			return 100
		elif sGoody == 'PRISONER_COMMANDER':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_COMMANDER'), pCaster)
			return 100
		elif sGoody == 'PRISONER_ENGINEER':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_ENGINEER'), pCaster)
			return 100
		elif sGoody == 'PRISONER_MAGE':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_MAGE'), pCaster)
			return 100
		elif sGoody == 'PRISONER_MERCHANT':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_MERCHANT'), pCaster)
			return 100
		elif sGoody == 'PRISONER_MONK':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_MONK'), pCaster)
			return 100
		elif sGoody == 'PRISONER_PROPHET':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_PROPHET'), pCaster)
			return 100
		elif sGoody == 'PRISONER_SEA_SERPENT':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_SEA_SERPENT'), pCaster)
			return 100
		elif sGoody == 'PRISONER_SCIENTIST':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_EXPLORE_LAIR_PRISONER_SCIENTIST'), pCaster)
			return 100
		elif sGoody == 'TECH':
			pPlayer.receiveGoody(pPlot, gc.getInfoTypeForString('GOODY_GRAVE_TECH'), pCaster)
			return 100
		return 100

	def formEmpire(self, iCiv, iLeader, eTeam, pCity, eAlignment, pFromPlayer):
		iPlayer = pFromPlayer.initNewEmpire(iLeader, iCiv)
		if iPlayer != PlayerTypes.NO_PLAYER:
			pPlot = pCity.plot()
			for iUnitIndex in xrange(pPlot.getNumUnits(), -1, -1):
				pUnit = pPlot.getUnit(iUnitIndex)
				pUnit.jumpToNearestValidPlot()

			pPlayer = gc.getPlayer(iPlayer)

			if eTeam != TeamTypes.NO_TEAM:
				if eTeam < pPlayer.getTeam():
					gc.getTeam(eTeam).addTeam(pPlayer.getTeam())
				else:
					gc.getTeam(pPlayer.getTeam()).addTeam(eTeam)

			pPlayer.acquireCity(pCity, False, True)

			eArcher = gc.getCivilizationInfo(pPlayer.getCivilizationType()).getCivilizationUnits(gc.getInfoTypeForString('UNITCLASS_ARCHER'))
			eWorker = gc.getCivilizationInfo(pPlayer.getCivilizationType()).getCivilizationUnits(gc.getInfoTypeForString('UNITCLASS_WORKER'))
			if eArcher != UnitTypes.NO_UNIT:
				for iArcherIndex in xrange(4):
					pPlayer.initUnit(eArcher, pPlot.getX(), pPlot.getY(), UnitAITypes.UNITAI_CITY_DEFENSE, DirectionTypes.DIRECTION_SOUTH)
			if eWorker != UnitTypes.NO_UNIT:
				pPlayer.initUnit(eWorker, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

			if eAlignment != AlignmentTypes.NO_ALIGNMENT:
				pPlayer.setAlignment(eAlignment)

		return pPlayer

	def grace(self):
		iGrace = cyFlatValue(20, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
		iDiff = gc.getNumHandicapInfos() + 1 - int(CyGame().getHandicapType())
		iGrace = iGrace * iDiff
		iGrace = CyGame().getSorenRandNum(iGrace, "grace") + iGrace
		if iGrace > CyGame().getGameTurn():
			return True
		return False

	def doCityFire(self, pCity):
		iCount = 0
		for iBuilding in xrange(gc.getNumBuildingInfos()):
			if pCity.getNumRealBuilding(iBuilding) > 0:
				if gc.getBuildingInfo(iBuilding).getConquestProbability() != 100:
					eBuildingClass = gc.getBuildingInfo(iBuilding).getBuildingClassType()
					if not isLimitedWonderClass(eBuildingClass):
						if CyGame().getSorenRandNum(100, "City Fire") < 10:
							pCity.setNumRealBuilding(iBuilding, 0)
							CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_CITY_FIRE",(gc.getBuildingInfo(iBuilding).getDescription(), )), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getBuildingInfo(iBuilding).getButton(), en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
							iCount += 1
		if iCount == 0:
			CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_CITY_FIRE_NO_DAMAGE",()), 'AS2D_SPELL_FIRE_ELEMENTAL', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Fire.dds', en.eColorGreen, pCity.getX(), pCity.getY(), True, True)

##--------	Unofficial Bug Fix: Modified by Denev	--------##
	def doHellTerrain(self):
		iFlamesSpreadChance = gc.getDefineINT('FLAMES_SPREAD_CHANCE')
		iThreshold = 18 * 100 // gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getBuildPercent()
#Kaijin >>> OAC addition
		iDark = gc.getInfoTypeForString('CIVILIZATION_DARK')
		iRarna = gc.getInfoTypeForString('CIVILIZATION_RARNA')

#Kaijin <<<
		iCount = CyGame().getGlobalCounter()
		for iPlotIndex in xrange(CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(iPlotIndex)
			if pPlot.getTerrainType() == en.eTerrainBurningSands:
				if not pPlot.isCity():
					if not pPlot.isPeak():
						if pPlot.getFeatureType() == FeatureTypes.NO_FEATURE:
							if CyGame().getSorenRandNum(100, "Flames") < iFlamesSpreadChance:
								pPlot.setFeatureType(en.eFeatureFlames, 0)
			bValid = False
			if pPlot.isOwned():
				pPlayer = gc.getPlayer(pPlot.getOwner())
				if pPlayer.getCivilizationType() == en.eCivilizationInfernal:
					pPlot.setPlotCounter(100)
					continue
#Kaijin >>>
## Tokoyami - Hell terrain
				elif (pPlayer.getCivilizationType() == iDark and iCount > 50):
					pPlot.setPlotCounter(100)
					continue
## Rarna - Auto sanctify
				elif pPlayer.getCivilizationType() == iRarna and pPlot.getPlotCounter() > 0:
					pPlot.setPlotCounter(0)
					continue
#Kaijin <<<
				if pPlayer.getStateReligion() == en.eReligionAshenVeil:
					bValid = True
				elif iCount >= 75:
					bValid = True
				elif iCount >= 50:
					if pPlayer.getAlignment() != en.eAlignmentGood:
						bValid = True
				elif iCount >= 25:
					if pPlayer.getAlignment() == en.eAlignmentEvil:
						bValid = True
			else:
				if iCount >= 25:
					bValid = True
			if bValid:
				iCountDiff = cyGetPlotCounterDiff(pPlot, iThreshold)
				if iCountDiff > 0:
					pPlot.changePlotCounter(iCountDiff)
			else:
				if pPlot.getPlotCounter() > 0:
					pPlot.changePlotCounter(-1)
##--------	Unofficial Bug Fix: End Modify			--------##
#Kaijin >>>
		iHellGrassland = gc.getInfoTypeForString('TERRAIN_BROKEN_LANDS')
		iHellPlains = gc.getInfoTypeForString('TERRAIN_FIELDS_OF_PERDITION')
		iHellDesert = gc.getInfoTypeForString('TERRAIN_BURNING_SANDS')
		iShallows = gc.getInfoTypeForString('TERRAIN_SHALLOWS')
	## Occurrence of ObsidianPlain
		if CyGame().isOption(gc.getInfoTypeForString('GAMEOPTION_MODDER_4')):
			for i in xrange (CyMap().numPlots()):
				pPlot = CyMap().plotByIndex(i)
				iBonus = pPlot.getBonusType(-1)
				iFeature = pPlot.getFeatureType()
				iHellFlood = gc.getInfoTypeForString('FEATURE_OBSIDIAN_PLAINS')
				iTerrain = pPlot.getTerrainType()
				if (iTerrain == iHellDesert and pPlot.isRiver() and pPlot.isFlatlands() and pPlot.getBonusType(-1) == -1):
					if CyGame().getSorenRandNum(100, "Flood") <= 24:
						pPlot.setFeatureType(iHellFlood, -1)
				if iFeature == iHellFlood:
					pPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
					pPlot.clearColdCounter()
					pPlot.setTerrainType(iHellDesert, True, True)
#Kaijin <<<

#Kaijin >>>
#	def doTurnKhazad(self, iPlayer):
	def doTurnKhazad(self, iPlayer, pCity):
		pPlayer = gc.getPlayer(iPlayer)
		iNumCities = pPlayer.getNumCities()
		"""
		if iNumCities > 0:
			eNewVault, iHighThreshold, iLowThreshold = self.getDwarvenVault(pPlayer.getGold(), iNumCities)
			for pyCity in PyPlayer(iPlayer).getCityList():
				pCity = pyCity.GetCy()
				for iMultiplier, szLoopVault in self.ltThresholds:
					pCity.setNumRealBuilding(gc.getInfoTypeForString(szLoopVault), 0)
				pCity.setNumRealBuilding(eNewVault, 1)
		"""
		eNewVault, iHighThreshold, iLowThreshold = self.getDwarvenVault(pPlayer.getGold(), iNumCities)
		for iMultiplier, szLoopVault in self.ltThresholds:
			pCity.setNumRealBuilding(gc.getInfoTypeForString(szLoopVault), 0)
		pCity.setNumRealBuilding(eNewVault, 1)
#Kaijin <<<

	def getDwarvenVault(self, iGold, iNumCities):
		fUnitaryThreshold = self.getDwarvenVaultUnitaryThreshold(iNumCities)

		iHighThreshold = sys.maxint
		for iMultiplier, szLoopVault in self.ltThresholds:
			iCurrentThreshold = round(iMultiplier * fUnitaryThreshold, -1)
			if iGold >= iCurrentThreshold:
				eNewVault = gc.getInfoTypeForString(szLoopVault)
				if iMultiplier == self.ltThresholds[-1][0]:	# bottom
					iLowThreshold = -sys.maxint - 1
				else:
					iLowThreshold = iCurrentThreshold - 1
				break
			iHighThreshold = iCurrentThreshold
		else:
			raise

		return eNewVault, iHighThreshold, iLowThreshold

	def getDwarvenVaultUnitaryThreshold(self, iNumCities):
		if iNumCities in self.mUnitaryThreshold:
			return self.mUnitaryThreshold[iNumCities]

		fPowerIndex = 1.0 + (min(self.iMaxNumCities, iNumCities) - 1) / 10.0
		iBaseThreshold = 50
		fUnitaryThreshold = float(iBaseThreshold ** fPowerIndex)
		if iNumCities > self.iMaxNumCities:
			fUnitaryThreshold = (fUnitaryThreshold * iNumCities) / self.iMaxNumCities
		self.mUnitaryThreshold[iNumCities] = fUnitaryThreshold

		return fUnitaryThreshold

	def getDwarvenVaultRequired(self, iNumCities, iVaultLevel):
		fUnitaryThreshold = self.getDwarvenVaultUnitaryThreshold(iNumCities)

		iVaultLevel = min(iVaultLevel, len(self.ltThresholds))

		iMultiplier = self.ltThresholds[-iVaultLevel][0]
		iCurrentThreshold = int(round(iMultiplier * fUnitaryThreshold, -1))

		return iCurrentThreshold

	def doTurnLuchuirp(self, ePlayer):
		eBarnaxusClass = gc.getInfoTypeForString('UNITCLASS_BARNAXUS')
		if CyGame().getUnitClassCreatedCount(eBarnaxusClass) > 0:
			py = PyPlayer(ePlayer)
			pBarnaxus = None
			lpGolems = []
			for pUnit in py.getUnitList():
				if pUnit.getUnitClassType() == eBarnaxusClass:
					pBarnaxus = pUnit
				elif pUnit.isHasPromotion(en.eRaceGolem):
					lpGolems.append(pUnit)
			if len(lpGolems) > 0:
				lePromotionCombats = [en.ePromotionCombat1, en.ePromotionCombat2, en.ePromotionCombat3, en.ePromotionCombat4, en.ePromotionCombat5]
				for pUnit in lpGolems:
					for ePromotionCombat in lePromotionCombats:
						ePromotionEmpower = gc.getPromotionInfo(ePromotionCombat).getPromotionSummonPerk()
						bEmpower = (pBarnaxus is not None) and pBarnaxus.isHasPromotion(ePromotionCombat)
						pUnit.setHasPromotion(ePromotionEmpower, bEmpower)

	def doTurnAmurites(self, ePlayer):
		if gc.getPlayer(ePlayer).getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_GOVANNON')) > 0:
			py = PyPlayer(ePlayer)
			pGovannon = None
			eGovannon = gc.getInfoTypeForString('UNITCLASS_GOVANNON')
			eChanneling1 = gc.getInfoTypeForString('PROMOTION_CHANNELING1')

			lpStudents = []
			for pUnit in py.getUnitList():
				if pUnit.getUnitClassType() == eGovannon:
					if not pUnit.isDuration() and not pUnit.isSummoned():
						pGovannon = pUnit
				if pUnit.isAlive():
					if pUnit.getUnitCombatType() != gc.getInfoTypeForString('UNITCOMBAT_ANIMAL'):
						if pUnit.getSpecialUnitType() != gc.getInfoTypeForString('SPECIALUNIT_BIRD'):
							if pUnit.getUnitCombatType() != UnitCombatTypes.NO_UNITCOMBAT:
								lpStudents.append(pUnit)
			if pGovannon is not None:
				leTeachPromotions = []
				for ePromotion in xrange(gc.getNumPromotionInfos()):
					if pGovannon.isHasPromotion(ePromotion):
						eBonusPrereq = gc.getPromotionInfo(ePromotion).getBonusPrereq()
						if eBonusPrereq != BonusTypes.NO_BONUS:
							if gc.getBonusInfo(eBonusPrereq).isMana():
								leTeachPromotions.append(ePromotion)

#				iLearningProbability = 24
#				iDenominator = gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getTrainPercent()

				for pStudents in lpStudents:
#					if CyGame().getSorenRandNum(iDenominator, "Govannon Drill") < iLearningProbability:
						pStudents.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING1'), True)
						for ePromotion in leTeachPromotions:
							pStudents.setHasPromotion(ePromotion, True)

#Kaijin >>> 
##パンドラの箱判定
	def doTurnDROAUM(self, iPlayer, pCity):
		iVault1 = gc.getInfoTypeForString('BUILDING_PANDORA_BOX_DROAUM_EMPTY')
		iVault2 = gc.getInfoTypeForString('BUILDING_PANDORA_BOX_DROAUM_LOW')
		iVault3 = gc.getInfoTypeForString('BUILDING_PANDORA_BOX_DROAUM_MIDDLE')
		iVault4 = gc.getInfoTypeForString('BUILDING_PANDORA_BOX_DROAUM')
		iVault5 = gc.getInfoTypeForString('BUILDING_PANDORA_BOX_DROAUM_STOCKED')
		iVault6 = gc.getInfoTypeForString('BUILDING_PANDORA_BOX_DROAUM_ABUNDANT')
		iVault7 = gc.getInfoTypeForString('BUILDING_PANDORA_BOX_DROAUM_FULL')
		iVault8 = gc.getInfoTypeForString('BUILDING_PANDORA_BOX_DROAUM_OVERFLOWING')
		iCount = CyGame().getGlobalCounter()
		if iCount <= 10:
			iNewVault = iVault1
		elif (iCount > 10 and iCount <= 25):
			iNewVault = iVault2
		elif (iCount > 25 and iCount <= 35):
			iNewVault = iVault3
		elif (iCount > 35 and iCount <= 50):
			iNewVault = iVault4
		elif (iCount > 50 and iCount <= 65):
			iNewVault = iVault5
		elif (iCount > 65 and iCount <= 75):
			iNewVault = iVault6
		elif (iCount > 75 and iCount <= 90):
			iNewVault = iVault7
		else:
			iNewVault = iVault8
		pCity.setNumRealBuilding(iVault1, 0)
		pCity.setNumRealBuilding(iVault2, 0)
		pCity.setNumRealBuilding(iVault3, 0)
		pCity.setNumRealBuilding(iVault4, 0)
		pCity.setNumRealBuilding(iVault5, 0)
		pCity.setNumRealBuilding(iVault6, 0)
		pCity.setNumRealBuilding(iVault7, 0)
		pCity.setNumRealBuilding(iVault8, 0)
		pCity.setNumRealBuilding(iNewVault, 1)

##商才志向の支部設置
	def doTurnRiches(self, iPlayer, pCity):
		pPlayer = gc.getPlayer(iPlayer)
		iNumCities = pPlayer.getNumCities()
		eNewVault, iHighThreshold, iLowThreshold = self.getRichesVault(pPlayer, pPlayer.getGold(), iNumCities)
		for iMultiplier, szLoopVault in self.RichesltThresholds:
			pCity.setNumRealBuilding(gc.getInfoTypeForString(szLoopVault), 0)
		pCity.setNumRealBuilding(eNewVault, 1)

	def getRichesVault(self, pPlayer, iGold, iNumCities):
		fUnitaryThreshold = self.getRichesVaultUnitaryThreshold(iNumCities)

		iHighThreshold = sys.maxint
		for iMultiplier, szLoopVault in self.RichesltThresholds:
			iCurrentThreshold = round(iMultiplier * fUnitaryThreshold, -1)
			iTotalProperty = iGold + self.getRichesBonus(pPlayer)
			if iTotalProperty >= iCurrentThreshold:
				eNewVault = gc.getInfoTypeForString(szLoopVault)
				if iMultiplier == self.RichesltThresholds[-1][0]:	# bottom
					iLowThreshold = -sys.maxint - 1
				else:
					iLowThreshold = iCurrentThreshold - 1
				break
			iHighThreshold = iCurrentThreshold
		else:
			raise

		return eNewVault, iHighThreshold, iLowThreshold

	def getRichesVaultUnitaryThreshold(self, iNumCities):
		if iNumCities in self.mRichesUnitaryThreshold:
			return self.mRichesUnitaryThreshold[iNumCities]

		fPowerIndex = 1.0 + (min(self.iRichesMaxNumCities, iNumCities) - 1) / 10.0
		iBaseThreshold = 100
		fUnitaryThreshold = float(iBaseThreshold ** fPowerIndex)
		if iNumCities > self.iRichesMaxNumCities:
			fUnitaryThreshold = (fUnitaryThreshold * iNumCities) / self.iRichesMaxNumCities
		self.mRichesUnitaryThreshold[iNumCities] = fUnitaryThreshold

		return fUnitaryThreshold

	def getRichesVaultRequired(self, iNumCities, iVaultLevel):
		fUnitaryThreshold = self.getRichesVaultUnitaryThreshold(iNumCities)

		iVaultLevel = min(iVaultLevel, len(self.RichesltThresholds))

		iMultiplier = self.RichesltThresholds[-iVaultLevel][0]
		iCurrentThreshold = int(round(iMultiplier * fUnitaryThreshold, -1))

		return iCurrentThreshold

	def getRichesBonus(self, pPlayer):
		iCamp = pPlayer.getImprovementCount(gc.getInfoTypeForString('IMPROVEMENT_CAMP'))
		iGreatCamp = pPlayer.getImprovementCount(gc.getInfoTypeForString('IMPROVEMENT_HUNTING_GROUNDS'))
		iFishingBoats = pPlayer.getImprovementCount(gc.getInfoTypeForString('IMPROVEMENT_FISHING_BOATS'))
		iPasture = pPlayer.getImprovementCount(gc.getInfoTypeForString('IMPROVEMENT_PASTURE'))
		iGreatPasture = pPlayer.getImprovementCount(gc.getInfoTypeForString('IMPROVEMENT_GREATER_PASTURE'))
		iPlantation = pPlayer.getImprovementCount(gc.getInfoTypeForString('IMPROVEMENT_PLANTATION'))
		iQuarry = pPlayer.getImprovementCount(gc.getInfoTypeForString('IMPROVEMENT_QUARRY'))
		iWhalingBoats = pPlayer.getImprovementCount(gc.getInfoTypeForString('IMPROVEMENT_WHALING_BOATS'))
		iWinery = pPlayer.getImprovementCount(gc.getInfoTypeForString('IMPROVEMENT_WINERY'))
		iBonus = iCamp * 20 + iGreatCamp * 30 + iFishingBoats * 20 + iPasture * 20 + iGreatPasture * 30 + iPlantation * 20 + iQuarry * 20 + iWhalingBoats * 20 + iWinery * 20
		lBonusList=[	'BONUS_GOLD','BONUS_INCENSE','BONUS_IVORY','BONUS_WHALE',
				'BONUS_COTTON','BONUS_GEMS','BONUS_FUR','BONUS_PEARL','BONUS_SILK','BONUS_WINE',
				'BONUS_DYE','BONUS_SUGAR','BONUS_TEA','BONUS_COFFEE','BONUS_JADE',
				'BONUS_RAZORWEED']
		lValueList=[	300,300,300,300,
				150,150,150,150,150,150,
				100,100,100,100,100,
				50]
		for iCount in xrange(len(lBonusList)):
			iNum = (pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString(lBonusList[iCount])) - 1)
			if iNum > 0:
				iBonus = iBonus + lValueList[iCount] * iNum
		return iBonus
#Kaijin <<<

	def findClearPlot(self, pUnit, plot):
		BestPlot = -1
		iBestPlot = 0
		if pUnit == -1:
			iX = plot.getX()
			iY = plot.getY()
			for iiX in xrange(iX-1, iX+2, 1):
				for iiY in xrange(iY-1, iY+2, 1):
					iCurrentPlot = 0
					pPlot = CyMap().plot(iiX,iiY)
					if not pPlot.isNone():
						if pPlot.getNumUnits() == 0:
							if pPlot.isWater() == plot.isWater() and not pPlot.isPeak() and not pPlot.isCity():
								iCurrentPlot = iCurrentPlot + 5
						if iCurrentPlot >= 1:
							iCurrentPlot = iCurrentPlot + CyGame().getSorenRandNum(5, "FindClearPlot")
							if iCurrentPlot >= iBestPlot:
								BestPlot = pPlot
								iBestPlot = iCurrentPlot
			return BestPlot
		iX = pUnit.getX()
		iY = pUnit.getY()
		for iiX in xrange(iX-1, iX+2, 1):
			for iiY in xrange(iY-1, iY+2, 1):
				iCurrentPlot = 0
				pPlot = CyMap().plot(iiX,iiY)
				if not pPlot.isNone():
					if pPlot.getNumUnits() == 0:
						if pUnit.canMoveOrAttackInto(pPlot, False):
							iCurrentPlot = iCurrentPlot + 5
					for i in xrange(pPlot.getNumUnits()):
						if pPlot.getUnit(i).getOwner() == pUnit.getOwner():
							if pUnit.canMoveOrAttackInto(pPlot, False):
								iCurrentPlot = iCurrentPlot + 15
					if pPlot.isCity():
						if pPlot.getPlotCity().getOwner() == pUnit.getOwner():
							iCurrentPlot = iCurrentPlot + 50
					if (iX == iiX and iY == iiY):
						iCurrentPlot = 0
					if iCurrentPlot >= 1:
						iCurrentPlot = iCurrentPlot + CyGame().getSorenRandNum(5, "FindClearPlot")
						if iCurrentPlot >= iBestPlot:
							BestPlot = pPlot
							iBestPlot = iCurrentPlot
		return BestPlot

	def genesis(self, iPlayer):
		liDesertFeatures = [en.eFeatureFloodPlains, en.eFeatureOasis]
		iBurntForest = gc.getDefineINT('FLAMES_EXPIRE_EFFECT')
		iNewForest = gc.getInfoTypeForString('FEATURE_FOREST_NEW')
		for iPlotIndex in xrange(CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(iPlotIndex)
			if pPlot.getOwner() == iPlayer:
				pPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
				pPlot.setPlotCounter(0)
# Kaijin OAC >>>
#				pPlot.clearColdCounter()
# Kaijin OAC <<<
				iFeature = pPlot.getFeatureType()
				if pPlot.getTerrainType() == en.eTerrainSnow:
#					pPlot.setTerrainType(en.eTerrainTundra, True, True)
					pPlot.setTerrainType(en.eTerrainTundra, False, True)
				elif pPlot.getTerrainType() == en.eTerrainTundra:
#					pPlot.setTerrainType(en.eTerrainPlains, True, True)
					pPlot.setTerrainType(en.eTerrainPlains, False, True)
				elif pPlot.getTerrainType() == en.eTerrainDesert:
					if iFeature not in liDesertFeatures:
#						pPlot.setTerrainType(en.eTerrainPlains, True, True)
						pPlot.setTerrainType(en.eTerrainPlains, False, True)
				elif pPlot.getTerrainType() == en.eTerrainPlains:
#					pPlot.setTerrainType(en.eTerrainGrass, True, True)
					pPlot.setTerrainType(en.eTerrainGrass, False, True)
				elif pPlot.getTerrainType() == en.eTerrainGrass:
					if iFeature == FeatureTypes.NO_FEATURE:
						if pPlot.canHaveFeatureOnImprovement(iNewForest):
							pPlot.setFeatureType(iNewForest, 0)
# Kaijin OAC >>>
				elif pPlot.getTerrainType() == en.eTerrainMarsh:
					pPlot.setTerrainType(en.eTerrainGrass, False, True)
# Kaijin OAC <<<
				if iFeature == en.eFeatureJungle:
					pPlot.setFeatureType(en.eFeatureForest, 0)
				elif iFeature == en.eFeatureFlames:
					pPlot.setFeatureType(iBurntForest, 0)
# Kaijin OAC >>>
				elif iFeature == en.eFeatureSwamp:
					pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
				elif iFeature == en.eFeatureBlizzard:
					pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
# Kaijin OAC <<<
				elif iFeature != FeatureTypes.NO_FEATURE:
					iUpgrade = gc.getFeatureInfo(iFeature).getFeatureUpgrade()
					if iUpgrade != FeatureTypes.NO_FEATURE:
						iStateReligion = gc.getFeatureInfo(iUpgrade).getPrereqStateReligion()
						if iStateReligion in (ReligionTypes.NO_RELIGION, gc.getPlayer(iPlayer).getStateReligion()):
							pPlot.setFeatureType(iUpgrade, 0)
				if pPlot.getImprovementType() == gc.getDefineINT('FLAMES_SPREAD_EFFECT'):
					pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
#				if iFeature != FeatureTypes.NO_FEATURE:
#					if not gc.getFeatureInfo(iFeature).isTerrain(pPlot.getTerrainType()):
#						pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)

##--------		Tweaked Hyborem: Added by Denev	--------##
		"""
	def getAshenVeilCity(self, iNum):
		iInfernal = gc.getInfoTypeForString('CIVILIZATION_INFERNAL')
		iVeil = gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL')
		iBestValue1 = 0
		iBestValue2 = 0
		iBestValue3 = 0
		pBestCity1 = -1
		pBestCity2 = -1
		pBestCity3 = -1
		for iPlayer in xrange(gc.getMAX_PLAYERS()):
			pPlayer = gc.getPlayer(iPlayer)
			if (pPlayer.isAlive() and pPlayer.getCivilizationType() != iInfernal):
				for pyCity in PyPlayer(iPlayer).getCityList():
					pCity = pyCity.GetCy()
					if (pCity.isHasReligion(iVeil) and pCity.isCapital() == False):
						bValid = True
						iValue = pCity.getPopulation() * 100
						iValue += pCity.getCulture(iPlayer) / 3
						iValue += pCity.getNumBuildings() * 10
						iValue += pCity.getNumWorldWonders() * 100
						iValue += pCity.countNumImprovedPlots()
						if iValue > iBestValue1:
							iBestValue3 = iBestValue2
							pBestCity3 = pBestCity2
							iBestValue2 = iBestValue1
							pBestCity2 = pBestCity1
							iBestValue1 = iValue
							pBestCity1 = pCity
							bValid = False
						if (bValid and iValue > iBestValue2):
							iBestValue3 = iBestValue2
							pBestCity3 = pBestCity2
							iBestValue2 = iValue
							pBestCity2 = pCity
							bValid = False
						if (bValid and iValue > iBestValue3):
							iBestValue3 = iValue
							pBestCity3 = pCity
		if iNum == 1:
			return pBestCity1
		if iNum == 2:
			return pBestCity2
		if iNum == 3:
			return pBestCity3
		return -1
		"""
	def getAshenVeilCities(self, iCasterPlayer, iCasterID, iNum):
		pCasterPlayer = gc.getPlayer(iCasterPlayer)
		pCaster = pCasterPlayer.getUnit(iCasterID)

		ltVeilCities = []

		for ePlayer in xrange(gc.getMAX_PLAYERS()):
			pTargetPlayer = gc.getPlayer(ePlayer)

			if not pTargetPlayer.isAlive():
				continue

			if pTargetPlayer.getTeam() == pCasterPlayer.getTeam():
				continue

			iBaseModifier = 100
			if pTargetPlayer.getStateReligion() == en.eReligionAshenVeil:
				iBaseModifier -= 20
			if pTargetPlayer.getAlignment() == en.eAlignmentEvil:
				iBaseModifier -= 10

			for pyCity in PyPlayer(ePlayer).getCityList():
				pTargetCity = pyCity.GetCy()
				if pTargetCity.isHasReligion(en.eReligionAshenVeil) and not pTargetCity.isCapital():
					iValue = pTargetCity.getPopulation() * 100
					iValue += pTargetCity.getCulture(ePlayer) / 3
					iValue += pTargetCity.getNumBuildings() * 10
					iValue += pTargetCity.getNumWorldWonders() * 100
					iValue += pTargetCity.countNumImprovedPlots()

					iModifier = iBaseModifier
					pCasterCapital = pCasterPlayer.getCapitalCity()
					if not pCasterCapital.isNone() and pTargetCity.area().getID() == pCasterCapital.area().getID():
						iModifier += 10
					if pTargetCity.area().getCitiesPerPlayer(iCasterPlayer) > 0:
						iModifier += 10

					if pCasterPlayer.getNumCities() > 0:
						iMinDistance = -1
						for pyCity in PyPlayer(iCasterPlayer).getCityList():
							pLoopCity = pyCity.GetCy()
							if pLoopCity.getID() == pTargetCity.getID():
								continue
							iDistance = stepDistance(pLoopCity.getX(), pLoopCity.getY(), pTargetCity.getX(), pTargetCity.getY())
							if iMinDistance == -1 or iMinDistance > iDistance:
								iMinDistance = iDistance
						if iMinDistance != -1:
							iModifier -= iMinDistance

					iModifier = max(0, iModifier)
					iValue = (iValue * iModifier) // 100

					ltVeilCities.append((iValue, pTargetCity))

		ltVeilCities.sort()
		ltVeilCities.reverse()
		lpVeilCities = []
		if len(ltVeilCities) > 0:
			ltVeilCities = ltVeilCities[0:min(iNum, len(ltVeilCities))]
			lpVeilCities = [pCity for iValue, pCity in ltVeilCities]
		return lpVeilCities
##--------		Tweaked Hyborem: End Modify			--------##

##--------	Unofficial Bug Fix: Deleted by Denev	--------##
	"""
	def getCivilization(self, iCiv):
		i = -1
		for iPlayer in xrange(gc.getMAX_PLAYERS()):
			pPlayer = gc.getPlayer(iPlayer)
			if pPlayer.getCivilizationType() == iCiv:
				i = iPlayer
		return i

	def getLeader(self, iLeader):
		i = -1
		for iPlayer in xrange(gc.getMAX_PLAYERS()):
			pPlayer = gc.getPlayer(iPlayer)
			if pPlayer.getLeaderType() == iLeader:
				i = iPlayer
		return i
	"""
	def getCivilization(self, iCivilization):
		iPlayer = PlayerTypes.NO_PLAYER
		for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
			pPlayer = gc.getPlayer(iLoopPlayer)
			if pPlayer.isAlive():
				if pPlayer.getCivilizationType() == iCivilization:
					iPlayer = iLoopPlayer
					break
		return iPlayer

	def getLeader(self, iLeader):
		iPlayer = PlayerTypes.NO_PLAYER
		for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
			pPlayer = gc.getPlayer(iLoopPlayer)
			if pPlayer.isAlive():
				if pPlayer.getLeaderType() == iLeader:
					iPlayer = iLoopPlayer
					break
		return iPlayer
##--------	Unofficial Bug Fix: End Delete		--------##

##--------	Unofficial Bug Fix: Deleted by Denev	--------##
	"Moved to DLL"
	"""
	def getOpenPlayer(self):
		i = -1
		for iPlayer in xrange(gc.getMAX_PLAYERS()):
			pPlayer = gc.getPlayer(iPlayer)
			if (pPlayer.isEverAlive() == False and i == -1):
				i = iPlayer
		return i
	"""
##--------	Unofficial Bug Fix: End Delete			--------##

	def getUnholyVersion(self, pUnit):
		iUnit = -1
		if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ADEPT'):
			if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 2:
				iUnit = gc.getInfoTypeForString('UNIT_IMP')
			elif gc.getUnitInfo(pUnit.getUnitType()).getTier() == 3:
				iUnit = gc.getInfoTypeForString('UNIT_MAGE')
			elif gc.getUnitInfo(pUnit.getUnitType()).getTier() == 4:
				iUnit = gc.getInfoTypeForString('UNIT_LICH')
		elif pUnit.getUnitCombatType() in (gc.getInfoTypeForString('UNITCOMBAT_ANIMAL'), gc.getInfoTypeForString('UNITCOMBAT_BEAST')):
			if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 1:
				iUnit = gc.getInfoTypeForString('UNIT_SCOUT')
			elif gc.getUnitInfo(pUnit.getUnitType()).getTier() == 2:
				iUnit = gc.getInfoTypeForString('UNIT_HELLHOUND')
			elif gc.getUnitInfo(pUnit.getUnitType()).getTier() == 3:
				iUnit = gc.getInfoTypeForString('UNIT_ASSASSIN')
			elif gc.getUnitInfo(pUnit.getUnitType()).getTier() == 4:
				iUnit = gc.getInfoTypeForString('UNIT_BEAST_OF_AGARES')
		elif pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ARCHER'):
			if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 2:
				iUnit = gc.getInfoTypeForString('UNIT_ARCHER')
			elif gc.getUnitInfo(pUnit.getUnitType()).getTier() == 3:
				iUnit = gc.getInfoTypeForString('UNIT_LONGBOWMAN')
			elif gc.getUnitInfo(pUnit.getUnitType()).getTier() == 4:
				iUnit = gc.getInfoTypeForString('UNIT_CROSSBOWMAN')
		elif pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_DISCIPLE'):
			if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 2:
				iUnit = gc.getInfoTypeForString('UNIT_DISCIPLE_THE_ASHEN_VEIL')
			elif gc.getUnitInfo(pUnit.getUnitType()).getTier() == 3:
				iUnit = gc.getInfoTypeForString('UNIT_PRIEST_OF_THE_VEIL')
			elif gc.getUnitInfo(pUnit.getUnitType()).getTier() == 4:
				iUnit = gc.getInfoTypeForString('UNIT_EIDOLON')
		elif pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_MELEE'):
			if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 1:
				iUnit = gc.getInfoTypeForString('UNIT_SKELETON')
			elif gc.getUnitInfo(pUnit.getUnitType()).getTier() == 2:
				iUnit = gc.getInfoTypeForString('UNIT_DISEASED_CORPSE')
			elif gc.getUnitInfo(pUnit.getUnitType()).getTier() == 3:
				iUnit = gc.getInfoTypeForString('UNIT_CHAMPION')
			elif gc.getUnitInfo(pUnit.getUnitType()).getTier() == 4:
				iUnit = gc.getInfoTypeForString('UNIT_BALOR')
		elif pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_MOUNTED'):
			if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 2:
				iUnit = gc.getInfoTypeForString('UNIT_HORSEMAN')
			elif gc.getUnitInfo(pUnit.getUnitType()).getTier() == 3:
				iUnit = gc.getInfoTypeForString('UNIT_CHARIOT')
			elif gc.getUnitInfo(pUnit.getUnitType()).getTier() == 4:
				iUnit = gc.getInfoTypeForString('UNIT_DEATH_KNIGHT')
		elif pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_RECON'):
			if gc.getUnitInfo(pUnit.getUnitType()).getTier() == 1:
				iUnit = gc.getInfoTypeForString('UNIT_SCOUT')
			elif gc.getUnitInfo(pUnit.getUnitType()).getTier() == 2:
				iUnit = gc.getInfoTypeForString('UNIT_HELLHOUND')
			elif gc.getUnitInfo(pUnit.getUnitType()).getTier() == 3:
				iUnit = gc.getInfoTypeForString('UNIT_ASSASSIN')
			elif gc.getUnitInfo(pUnit.getUnitType()).getTier() == 4:
				iUnit = gc.getInfoTypeForString('UNIT_BEASTMASTER')
		return iUnit

	def getUnitPlayerID(self, pUnit):
		pPlayer = gc.getPlayer(pUnit.getOwner())
		iID = pUnit.getID()
		iUnitID = -1
		for iUnit in xrange(pPlayer.getNumUnits()):
			pLoopUnit = pPlayer.getUnit(iUnit)
			if pLoopUnit.getID() == iID:
				iUnitID = iUnit
		return iUnitID

##--------		Single Afterlife: Added by Denev	--------##
	def doAfterLife(self, bRise, iNumUnits, pFromPlot, pDeadUnit, pRazedCity, iXP):
		if iNumUnits <= 0:
			return None

		pNewUnit = None

		iChance = 100 + iXP - (CyGame().countCivPlayersAlive() * 3)
		if bRise:
			eUnit = en.eUnitAngel
			eCivilization = en.eCivilizationMercurians
			iChance = (iChance * 4) // 5
		else:
			eUnit = en.eUnitManes
			eCivilization = en.eCivilizationInfernal
		iChance = max(5, min(95, iChance))
		if CyGame().getSorenRandNum(100, "Afterlife Rise or Fall") < iChance:
			lpCities = []
			for ePlayer in xrange(gc.getMAX_CIV_PLAYERS()):
				pPlayer = gc.getPlayer(ePlayer)
				if pPlayer.isAlive():
					if pPlayer.getCivilizationType() == eCivilization:
						lpCities.extend(PyPlayer(ePlayer).getCityList())
			if len(lpCities) > 0:
				iRnd = CyGame().getSorenRandNum(len(lpCities), "Afterlife Rise or Fall")
				pCity = lpCities[iRnd]
				ePlayer = pCity.getOwner()
				pPlayer = gc.getPlayer(ePlayer)
				for iLoop in xrange(iNumUnits):
					pNewUnit = pPlayer.initUnit(eUnit, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
					pNewUnit.changeExperience(iXP, -1, False, False, False)
					if pDeadUnit is not None:
						pNewUnit.setReligion(pDeadUnit.getReligion())
# Kaijin >>>
					if not bRise:
						if pPlayer.getCivilizationType() == eCivilization:
							liAdditionalUnits = [ 'UNIT_WARRIOR',
													'UNIT_WARRIOR',
													'UNIT_SCOUT',
													'UNIT_SCOUT',
													'UNIT_IMP',
													'UNIT_DISCIPLE_THE_ASHEN_VEIL' 	]
							iAdditionalUnit = gc.getInfoTypeForString(liAdditionalUnits[CyGame().getSorenRandNum(len(liAdditionalUnits), "Select Unit")])
							pAdditionalNewUnit = pPlayer.initUnit(iAdditionalUnit, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
# Kaijin <<<
				pPoint = pFromPlot.getPoint()
				if bRise:
					if pFromPlot.isVisibleToWatchingHuman():
						CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_BANISH_ANGEL'), pPoint)
					szSound = 'AS2D_UNIT_RISES'
				else:
					if pFromPlot.isVisibleToWatchingHuman():
						CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_BANISH_DEMON'), pPoint)
					szSound = 'AS2D_UNIT_FALLS'

				szText = CyTranslator().getText("TXT_KEY_MESSAGE_ADD_ANGEL_OR_MANES",(pNewUnit.getNameKey(), ))
				CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), szText, szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
				if pDeadUnit is not None:
					eFromPlayer = pDeadUnit.getOwner()
					szText = CyTranslator().getText("TXT_KEY_MESSAGE_UNIT_RISES_OR_FALLS",(pNewUnit.getNameKey(), gc.getCivilizationInfo(eCivilization).getDescription(), pDeadUnit.getNameKey()))
				else:
					eFromPlayer = pRazedCity.getPreviousOwner()
					szText = CyTranslator().getText("TXT_KEY_MESSAGE_CITY_RISES_OR_FALLS",(pNewUnit.getNameKey(), gc.getCivilizationInfo(eCivilization).getDescription(), pRazedCity.getNameKey()))
				CyInterface().addMessage(eFromPlayer, True, gc.getEVENT_MESSAGE_TIME(), szText, szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorRed, pFromPlot.getX(), pFromPlot.getY(), True, True)

				if not pPlayer.isHuman():
					if pNewUnit.canCast(en.eSpellAddToCity, False):
						if CyGame().getSorenRandNum(100, "Add to City") < 100 - pCity.getPopulation() * 5:
							pNewUnit.cast(en.eSpellAddToCity)
		return pNewUnit

# Kaijin >>>
	## Rarna
	def doAfterLifeRarna(self, pFromUnit, pFromPlot, iFromPlayer, iXP):
		pFromPlayer = gc.getPlayer(iFromPlayer)
		pNewUnit = -1
		liUnits = []

		if gc.getUnitInfo(pFromUnit.getUnitType()).getTier() >= 4:
			if isNationalUnitClass(pFromUnit.getUnitClassType()):
				liUnits = [ 'UNIT_HALBERD_RARNA',
							'UNIT_WHITE_KNIGHT_RARNA',
							'UNIT_MARKSMAN',
							'UNIT_CROSSBOWMAN' 	]
			else:
				liUnits = [ 'UNIT_BERSERKER',
							'UNIT_BEASTMASTER',	]
		if gc.getUnitInfo(pFromUnit.getUnitType()).getTier() == 3:
			liUnits = [ 'UNIT_CHAMPION',
						'UNIT_LONGBOWMAN',
						'UNIT_HORSE_AXEMAN_RARNA',
						'UNIT_PIKEMAN_RARNA' 	]
		if gc.getUnitInfo(pFromUnit.getUnitType()).getTier() == 2:
			liUnits = [ 'UNIT_AXEMAN',
						'UNIT_ARCHER',
						'UNIT_HORSEMAN',
						'UNIT_SPEARMAN_RARNA' 	]
		if gc.getUnitInfo(pFromUnit.getUnitType()).getTier() <= 1:
			liUnits = [ 'UNIT_WARRIOR',
						'UNIT_SCOUT' 	]

		iUnit = gc.getInfoTypeForString(liUnits[CyGame().getSorenRandNum(len(liUnits), "Select Unit")])

		iRace = gc.getInfoTypeForString('PROMOTION_ANGEL')
		szFromPlayerMessage = CyTranslator().getText("TXT_KEY_MESSAGE_ADD_RARNA_ANGEL",())

		if CyGame().getProjectCreatedCount(gc.getInfoTypeForString('PROJECT_FIRE_INHERITANCE')) > 0:
			iRace = gc.getInfoTypeForString('PROMOTION_UNDEAD')
			szFromPlayerMessage = CyTranslator().getText("TXT_KEY_MESSAGE_ADD_RARNA_UNDEAD",())

		elif CyGame().getProjectCreatedCount(gc.getInfoTypeForString('PROJECT_SPREAD_CORRUPTION')) > 0:
			iRace = gc.getInfoTypeForString('PROMOTION_DEMON')
			szFromPlayerMessage = CyTranslator().getText("TXT_KEY_MESSAGE_ADD_RARNA_DEMON",())

		pCity = pFromPlayer.getCapitalCity()
		pNewUnit = pFromPlayer.initUnit(iUnit, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		if pNewUnit is not None:
			pNewUnit.changeExperience(iXP, -1, False, False, False)
			pNewUnit.setHasPromotion(iRace, True)
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MAGIC_IMMUNE'), True)
			pNewUnit.changeFreePromotionPick(pFromPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_TOWER_OF_MOBIUS')))

			CyInterface().addMessage(iFromPlayer, True, gc.getEVENT_MESSAGE_TIME(), szFromPlayerMessage, 'AS2D_UNIT_RISES', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorWhite, pFromPlot.getX(), pFromPlot.getY(), True, True)

		return pNewUnit

	## Baldralfar
	def doAfterLifeBaldralfar(self, bRise, pFromPlot, iFromPlayer, iXP):
		pNewUnit = -1
		iChance = 100 + iXP - (CyGame().countCivPlayersAlive() * 3)
		iChance = max(5, min(95, iChance))
		if CyGame().getSorenRandNum(100, "Afterlife Rise or Fall") < iChance:
			iUnit = gc.getInfoTypeForString('UNIT_DRYAS')
			iCivilization = gc.getInfoTypeForString('CIVILIZATION_BALDRALFAR')
			lpCities = []
			for iPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
				pPlayer = gc.getPlayer(iPlayer)
				if pPlayer.isAlive():
					if pPlayer.getCivilizationType() == iCivilization:
						if pPlayer.countNumBuildings(gc.getInfoTypeForString('BUILDING_MANDOS_PALACE')) > 0:
							lpCities.extend(PyPlayer(iPlayer).getCityList())
			if len(lpCities) > 0:
				iRnd = CyGame().getSorenRandNum(len(lpCities), "Afterlife Rise or Fall")
				pCity = lpCities[iRnd]
				pPlayer = gc.getPlayer(pCity.getOwner())
				pNewUnit = pPlayer.initUnit(iUnit, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
				CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_UNIT_MANDOS",()), 'AS2D_UNIT_RISES', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorRed, pCity.getX(), pCity.getY(), True, True)
				CyInterface().addMessage(iFromPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_UNIT_MANDOS",()), 'AS2D_UNIT_RISES', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorRed, pFromPlot.getX(), pFromPlot.getY(), True, True)
		return pNewUnit
# Kaijin <<<
##--------		Single Afterlife: End Add		--------##

	def giftUnit(self, ePlayer, iUnit, iXP):
		pPlot = -1
		pNewUnit = -1
		py = PyPlayer(ePlayer)
		pPlayer = gc.getPlayer(ePlayer)
		if py.getNumCities() > 0:
			iRnd = CyGame().getSorenRandNum(py.getNumCities(), "Gift Unit")
			pPlot = py.getCityList()[iRnd].plot()
		elif py.getNumUnits() > 0:
			iRnd = CyGame().getSorenRandNum(py.getNumUnits(), "Gift Unit")
			pPlot = py.getUnitList()[iRnd].plot()
		if pPlot != -1:
			pNewUnit = pPlayer.initUnit(iUnit, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit.changeExperience(iXP, -1, False, False, False)
		return pNewUnit

	def placeTreasure(self, ePlayer, iUnit):
		pPlayer = gc.getPlayer(ePlayer)
		pBestPlot = -1
		iBestPlot = -1
		for iPlotIndex in xrange(CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(iPlotIndex)
			iPlot = -1
			if not pPlot.isWater():
				if pPlot.getNumUnits() == 0:
					if not pPlot.isCity():
						if not pPlot.isImpassable():
							iPlot = CyGame().getSorenRandNum(1000, "Add Unit")
							if pPlot.area().getNumTiles() < 8:
								iPlot += 1000
							if not pPlot.isOwned():
								iPlot += 1000
							if iPlot > iBestPlot:
								iBestPlot = iPlot
								pBestPlot = pPlot
		if iBestPlot != -1:
			pNewUnit = pPlayer.initUnit(iUnit, pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_TREASURE",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Equipment/Treasure.dds', en.eColorGreen, pNewUnit.getX(), pNewUnit.getY(), True, True)
			if ePlayer == CyGame().getActivePlayer():
				CyCamera().JustLookAtPlot(pBestPlot)

	def showUniqueImprovements(self, ePlayer):
		pPlayer = gc.getPlayer(ePlayer)
		eTeam = pPlayer.getTeam()
		for iPlotIndex in xrange(CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(iPlotIndex)
			if pPlot.getImprovementType() != ImprovementTypes.NO_IMPROVEMENT:
				if gc.getImprovementInfo(pPlot.getImprovementType()).isUnique():
					pPlot.setRevealed(eTeam, True, False, TeamTypes.NO_TEAM)

# Kaijin >>> Amurite - Show All Raw Manas
	def showRawManas(self, ePlayer):
		pPlayer = gc.getPlayer(ePlayer)
		eTeam = pPlayer.getTeam()
		eMana = gc.getInfoTypeForString('BONUS_MANA')
		for iPlotIndex in xrange(CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(iPlotIndex)
			if pPlot.getBonusType(eTeam) == eMana:
				pPlot.setRevealed(eTeam, True, False, TeamTypes.NO_TEAM)
# Kaijin <<<

	def warScript(self, ePlayer):
		if gc.getPlayer(ePlayer).isBarbarian():
			return

		pPlayer = gc.getPlayer(ePlayer)
		pTeam = gc.getTeam(pPlayer.getTeam())
		eOurCivilization = pPlayer.getCivilizationType()
		if not pTeam.isAVassal():
#			iBestEnemy = -1
			leOldFoes = [en.eCivilizationSvartalfar, en.eCivilizationLjosalfar]
			leWarMongers = [en.eCivilizationInfernal, en.eCivilizationDoviello]
			leVictimTeams = []
			for iRivalPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
				pRivalPlayer = gc.getPlayer(iRivalPlayer)
				if pRivalPlayer.isAlive():
					iRivalTeam = gc.getPlayer(iRivalPlayer).getTeam()
#					if pTeam.isAtWar(iRivalTeam):
#						if CyGame().getSorenRandNum(100, "War Script") < 5:
#							self.dogpile(ePlayer, iRivalPlayer)
					if self.warScriptAllow(ePlayer, iRivalPlayer):
						# breaking the compact
						if eOurCivilization == en.eCivilizationMercurians:
							if pRivalPlayer.getStateReligion() == en.eReligionAshenVeil:
								pTeam.declareWar(iRivalTeam, False, WarPlanTypes.WARPLAN_TOTAL)
								continue

						if pTeam.getAtWarCount(True) == 0:
							# warmonger bites the best player
#							if pPlayer.getAlignment() == gc.getInfoTypeForString('ALIGNMENT_EVIL'):
#								if (CyGame().getGlobalCounter() > 40) or (eOurCivilization in leWarMongers):
#									if CyGame().getPlayerRank(iRivalPlayer) > CyGame().getPlayerRank(ePlayer):
#										if (iBestEnemy == -1 or CyGame().getPlayerRank(iRivalPlayer) > CyGame().getPlayerRank(iBestEnemy)):
#											iBestEnemy = iRivalPlayer

							# interrupt winning
							if pRivalPlayer.getBuildingClassMaking(gc.getInfoTypeForString('BUILDINGCLASS_TOWER_OF_MASTERY')) > 0:
								leVictimTeams.append(iRivalTeam)
								continue
							if pRivalPlayer.getBuildingClassMaking(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_FINAL')) > 0:
								if pPlayer.getAlignment() == en.eAlignmentEvil:
									leVictimTeams.append(iRivalTeam)
									continue
# ent >>>
							if gc.getTeam(iRivalTeam).getProjectMaking(gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_CORE')) > 0:
								leVictimTeams.append(iRivalTeam)
								continue
							if gc.getTeam(iRivalTeam).getProjectMaking(gc.getInfoTypeForString('PROJECT_LED_TO_THE_END')) > 0:
								if pPlayer.getAlignment() != en.eAlignmentEvil:
									leVictimTeams.append(iRivalTeam)
									continue
# ent <<<
							# splitted palaces
							if CyGame().getGlobalCounter() > 20:
								eRivalCivilization = pRivalPlayer.getCivilizationType()
								if (eOurCivilization in leOldFoes) and (eRivalCivilization in leOldFoes):
									if eOurCivilization != eRivalCivilization:
										if CyGame().getPlayerRank(ePlayer) > CyGame().getPlayerRank(iRivalPlayer):
											leVictimTeams.append(iRivalTeam)
											continue

			for eVictimTeam in leVictimTeams:
				pTeam.declareWar(eVictimTeam, False, WarPlanTypes.WARPLAN_TOTAL)

#			if iBestEnemy != -1:
#				if CyGame().getPlayerRank(ePlayer) > CyGame().getPlayerRank(iBestEnemy):
#					self.startWar(ePlayer, iBestEnemy, WarPlanTypes.WARPLAN_TOTAL)

	def warScriptAllow(self, ePlayer, ePlayer2):
		pPlayer = gc.getPlayer(ePlayer)
		pPlayer2 = gc.getPlayer(ePlayer2)
		eTeam = gc.getPlayer(ePlayer).getTeam()
		eTeam2 = gc.getPlayer(ePlayer2).getTeam()
		pTeam = gc.getTeam(eTeam)
		if not pTeam.canDeclareWar(eTeam2):
			return False
		if gc.getPlayer(ePlayer).isBarbarian():
			return False
		if pTeam.AI_getAtPeaceCounter(eTeam2) < 20:
			return False
#		if pPlayer.AI_getAttitude(ePlayer2) <= gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getDeclareWarRefuseAttitudeThreshold():
#			return False
		if pPlayer.getCivilizationType() == en.eCivilizationInfernal:
			if pPlayer2.getStateReligion() == en.eReligionAshenVeil:
				return False
		return True

	def dogpile(self, ePlayer, eVictim):
		pPlayer = gc.getPlayer(ePlayer)
		for ePlayer2 in xrange(gc.getMAX_CIV_PLAYERS()):
			pPlayer2 = gc.getPlayer(ePlayer2)
			iChance = -1
			if pPlayer2.isAlive():
				if (self.dogPileAllow(ePlayer, ePlayer2) and self.warScriptAllow(ePlayer2, eVictim)):
					iChance = pPlayer2.AI_getAttitude(ePlayer) * 5
					if iChance > 0:
						iChance = iChance - (pPlayer2.AI_getAttitude(eVictim) * 5) - 10
						if not CyGame().isOption(GameOptionTypes.GAMEOPTION_AGGRESSIVE_AI):
							iChance = iChance - 10
						if iChance > 0:
							iChance = iChance + (CyGame().getGlobalCounter() / 3)
							if pPlayer2.getCivilizationType() == en.eCivilizationBalseraphs:
								iChance = CyGame().getSorenRandNum(50, "Dogpile")
							if CyGame().getSorenRandNum(100, "Dogpile") < iChance:
#								self.startWar(ePlayer2, eVictim, WarPlanTypes.WARPLAN_DOGPILE)
								pTeam2 = gc.getTeam(pPlayer2.getTeam())
								eVictimTeam = gc.getPlayer(eVictim).getTeam()
								pTeam2.declareWar(eVictimTeam, False, WarPlanTypes.WARPLAN_DOGPILE)

	def dogPileAllow(self, ePlayer, ePlayer2):
		pPlayer = gc.getPlayer(ePlayer)
		pPlayer2 = gc.getPlayer(ePlayer2)
		eTeam = gc.getPlayer(ePlayer).getTeam()
		eTeam2 = gc.getPlayer(ePlayer2).getTeam()
		if ePlayer == ePlayer2:
			return False
		if eTeam == eTeam2:
			return False
		if pPlayer2.isHuman():
			return False
		if pPlayer2.getCivilizationType() == en.eCivilizationElohim:
			return False
		if gc.getTeam(eTeam2).isAVassal():
			return False
		return True

	def warn(self, ePlayer, szText, pPlot):
		pPlayer = gc.getPlayer(ePlayer)
		for ePlayer2 in xrange(gc.getMAX_PLAYERS()):
			pPlayer2 = gc.getPlayer(ePlayer2)
			if (pPlayer2.isAlive() and ePlayer != ePlayer2):
				if pPlayer2.isHuman():
					popupInfo = CyPopupInfo()
					popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
					popupInfo.setText(szText)
					popupInfo.setOnClickedPythonCallback("selectWarn")
					popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_MAIN_MENU_OK",()), "")
					popupInfo.addPopup(ePlayer2)
				if pPlot != -1:
					CyInterface().addMessage(ePlayer2, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_ALTAR_OF_THE_LUONNOTAR",()), 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Buildings/AltaroftheLuonnotar.dds', en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)

	def MarnokNameGenerator(self, unit):
		pPlayer = gc.getPlayer(unit.getOwner())
		pCiv = pPlayer.getCivilizationType()
		pReligion = pPlayer.getStateReligion()
		pAlign = pPlayer.getAlignment()

		lPre=["ta", "go", "da", "bar", "arc", "ken", "an", "ad", "mi", "kon", "kar", "mar", "wal", "he", "ha", "re", "ar", "bal", "bel", "bo", "bri", "car", "dag", "dan", "ma", "ja", "co", "be", "ga", "qui", "sa"]
		lMid=["ad", "z", "the", "and", "tha", "ent", "ion", "tio", "for", "tis", "oft", "che", "gan", "an", "en", "wen", "on", "d", "n", "g", "t", "ow", "dal"]
		lEnd=["ar", "sta", "na", "is", "el", "es", "ie", "us", "un", "th", "er", "on", "an", "re", "in", "ed", "nd", "at", "en", "le", "man", "ck", "ton", "nok", "git", "us", "or", "a", "da", "u", "cha", "ir"]

		lEpithet=["red", "blue", "black", "grey", "white", "strong", "brave", "old", "young", "great", "slayer", "hunter", "seeker"]
		lNoun=["spirit", "soul", "boon", "born", "staff", "rod", "shield", "autumn", "winter", "spring", "summer", "wit", "horn", "tusk", "glory", "claw", "tooth", "head", "heart", "blood", "breath", "blade", "hand", "lover", "bringer", "maker", "taker", "river", "stream", "moon", "star", "face", "foot", "half", "one", "hundred", "thousand"]
		lSchema=["CPME", "CPMESCPME", "CPESCPE", "CPE", "CPMME", "CPMDCME", "CPMAME", "KCPMESCUM", "CPMME[ the ]CX", "CPMESCXN", "CPMME[ of ]CPMME", "CNNSCXN"]

		if pAlign == en.eAlignmentEvil:
			lNoun = lNoun + ["fear", "terror", "reign", "brood", "snare", "war", "strife", "pain", "hate", "evil", "hell", "misery", "murder", "anger", "fury", "rage", "spawn", "sly", "blood", "bone", "scythe", "slave", "bound", "ooze", "scum"]
			lEpithet=["dark", "black", "white", "cruel", "foul"]

		if pReligion == en.eReligionAshenVeil:
			lEpithet = lEpithet + ["fallen", "diseased", "infernal", "profane", "corrupt"]
			lSchema = lSchema + ["CPME[ the ]CX"]
		if pReligion == gc.getInfoTypeForString('RELIGION_OCTOPUS_OVERLORDS'):
			lPre = lPre + ["cth", "cht", "shu", "az", "ts", "dag", "hy", "gla", "gh", "rh", "x", "ll"]
			lMid = lMid + ["ul", "tha", "on", "ug", "st", "oi"]
			lEnd = lEnd + ["hu", "on", "ha", "ua", "oa", "uth", "oth", "ath", "thua", "thoa", "ur", "ll", "og", "hua"]
			lEpithet = lEpithet + ["nameless", "webbed", "deep", "watery"]
			lNoun = lNoun + ["tentacle", "wind", "wave", "sea", "ocean", "dark", "crab", "abyss", "island"]
			lSchema = lSchema + ["CPMME", "CPDMME", "CPAMAME", "CPMAME", "CPAMAMEDCPAMAE"]
		if pReligion == gc.getInfoTypeForString('RELIGION_THE_ORDER'):
			lPre = lPre + ["ph", "v", "j"]
			lMid = lMid + ["an", "al", "un"]
			lEnd = lEnd + ["uel", "in", "il"]
			lEpithet = lEpithet + ["confessor", "crusader", "faithful", "obedient", "good"]
			lNoun = lNoun + ["order", "faith", "heaven", "law"]
			lSchema = lSchema + ["CPESCPME", "CPMESCPE", "CPMESCPME", "CPESCPE"]
		if pReligion == gc.getInfoTypeForString('RELIGION_FELLOWSHIP_OF_LEAVES'):
			lPre = lPre + ["ki", "ky", "yv"]
			lMid = lMid + ["th", "ri"]
			lEnd = lEnd + ["ra", "el", "ain"]
			lEpithet = lEpithet + ["green"]
			lNoun = lNoun + ["tree", "bush", "wood", "berry", "elm", "willow", "oak", "leaf", "flower", "blossom"]
			lSchema = lSchema + ["CPESCN", "CPMESCNN", "CPMESCXN"]
		if pReligion == gc.getInfoTypeForString('RELIGION_RUNES_OF_KILMORPH'):
			lPre = lPre + ["bam", "ar", "khel", "ki"]
			lMid = lMid + ["th", "b", "en"]
			lEnd = lEnd + ["ur", "dain", "ain", "don"]
			lEpithet = lEpithet + ["deep", "guard", "miner"]
			lNoun = lNoun + ["rune", "flint", "slate", "stone", "rock", "iron", "copper", "mithril", "thane", "umber"]
			lSchema = lSchema + ["CPME", "CPMME"]
		if pReligion == gc.getInfoTypeForString('RELIGION_THE_EMPYREAN'):
			lEpithet = lEpithet + ["radiant", "holy"]
			lNoun = lNoun + ["honor"]
		if pReligion == gc.getInfoTypeForString('RELIGION_COUNCIL_OF_ESUS'):
			lEpithet = lEpithet + ["hidden", "dark"]
			lNoun = lNoun + ["cloak", "shadow", "mask"]
			lSchema = lSchema + ["CPME", "CPMME"]

		if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ENRAGED')):
			# I have left this as a copy of the Barbarian, see how it goes, this might do the trick. I plan to use it when there is a chance a unit will go Barbarian anyway.
			lPre = lPre + ["gru", "bra", "no", "os", "dir", "ka", "z"]
			lMid = lMid + ["g", "ck", "gg", "sh", "b", "bh", "aa"]
			lEnd = lEnd + ["al", "e", "ek", "esh", "ol", "olg", "alg"]
			lNoun = lNoun + ["death", "hate", "rage", "mad", "insane", "berserk"]
			lEpithet = lEpithet + ["smasher", "breaker", "mangle", "monger"]

		if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CRAZED')):
			# might want to tone this down, because I plan to use it as possession/driven to madness, less than madcap zaniness.
			lPre = lPre + ["mad", "pim", "zi", "zo", "fli", "mum", "dum", "odd", "slur"]
			lMid = lMid + ["bl", "pl", "gg", "ug", "bl", "b", "zz", "abb", "odd"]
			lEnd = lEnd + ["ad", "ap", "izzle", "onk", "ing", "er", "po", "eep", "oggle", "y"]

		if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_VAMPIRE')):
			lPre = lPre + ["dra", "al", "nos", "vam", "vla", "tep", "bat", "bar", "cor", "lil", "ray", "zar", "stra", "le"]
			lMid = lMid + ["cul", "u", "car", "fer", "pir", "or", "na", "ov", "sta"]
			lEnd = lEnd + ["a", "d", "u", "e", "es", "y", "bas", "vin", "ith", "ne", "ak", "ich", "hd", "t"]

		if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON')):
			lPre = lPre + ["aa", "ab", "adr", "ah", "al", "de", "ba", "cro", "da", "be", "eu", "el", "ha", "ib", "me", "she", "sth", "z"]
			lMid = lMid + ["rax", "lia", "ri", "al", "as", "b", "bh", "aa", "al", "ze", "phi", "sto", "phe", "cc", "ee"]
			lEnd = lEnd + ["tor", "tan", "ept", "lu", "res", "ah", "mon", "gon", "bul", "gul", "lis", "les", "uz"]
			lSchema = ["CPMMME", "CPMACME", "CPKMAUAPUE", "CPMMME[ the ]CNX"]

		if unit.getUnitType() == gc.getInfoTypeForString('UNIT_HILL_GIANT'):
			lPre = lPre + ["gor", "gra", "gar", "gi", "gol"]
			lMid = lMid + ["gan", "li", "ri", "go"]
			lEnd = lEnd + ["tus", "tan", "ath", "tha"]
			lSchema = lSchema +["CXNSCNN", "CPESCNE", "CPMME[ the ]CX"]
			lEpithet = lEpithet + ["large", "huge", "collossal", "brutal", "basher", "smasher", "crasher", "crusher"]
			lNoun = lNoun + ["fist", "tor", "hill", "brute", "stomp"]

		if unit.getUnitType() == gc.getInfoTypeForString('UNIT_LIZARDMAN'):
			lPre = lPre + ["ss", "s", "th", "sth", "hss"]
			lEnd = lEnd + ["ess", "iss", "ath", "tha"]
			lEpithet = lEpithet + ["cold"]
			lNoun = lNoun + ["hiss", "tongue", "slither", "scale", "tail", "ruin"]
			lSchema = lSchema + ["CPAECPAE", "CPAKECPAU", "CPAMMAE"]
		if unit.getUnitType() == gc.getInfoTypeForString('UNIT_FIRE_ELEMENTAL') or unit.getUnitType() == gc.getInfoTypeForString('UNIT_AZER'):
			lPre = lPre + ["ss", "cra", "th", "sth", "hss", "roa"]
			lMid = lMid + ["ss", "ck", "rr", "oa", "iss", "tt"]
			lEnd = lEnd + ["le", "iss", "st", "r", "er"]
			lNoun = lNoun + ["hot", "burn", "scald", "roast", "flame", "scorch", "char", "sear", "singe", "fire", "spit"]
			lSchema = ["CNN", "CNX", "CPME", "CPME[ the ]CNX", "CPMME", "CNNSCPME"]
		if unit.getUnitType() == gc.getInfoTypeForString('UNIT_WATER_ELEMENTAL'):
			lPre = lPre + ["who", "spl", "dr", "sl", "spr", "sw", "b"]
			lMid = lMid + ["o", "a", "i", "ub", "ib"]
			lEnd = lEnd + ["sh", "p", "ter", "ble"]
			lNoun = lNoun + ["wave", "lap", "sea", "lake", "water", "tide", "surf", "spray", "wet", "damp", "soak", "gurgle", "bubble"]
			lSchema = ["CNN", "CNX", "CPME", "CPME[ the ]CNX", "CPMME", "CNNSCPME"]
		if unit.getUnitType() == gc.getInfoTypeForString('UNIT_AIR_ELEMENTAL'):
			lPre = lPre + ["ff", "ph", "th", "ff", "ph", "th"]
			lMid = lMid + ["oo", "aa", "ee", "ah", "oh"]
			lEnd = lEnd + ["ff", "ph", "th", "ff", "ph", "th"]
			lNoun = lNoun + ["wind", "air", "zephyr", "breeze", "gust", "blast", "blow"]
			lSchema = ["CNN", "CNX", "CPME", "CPME[ the ]CNX", "CPMME", "CNNSCPME"]
		if unit.getUnitType() == gc.getInfoTypeForString('UNIT_EARTH_ELEMENTAL'):
			lPre = lPre + ["gra", "gro", "kro", "ff", "ph", "th"]
			lMid = lMid + ["o", "a", "u"]
			lEnd = lEnd + ["ck", "g", "k"]
			lNoun = lNoun + ["rock", "stone", "boulder", "slate", "granite", "rumble", "quake"]
			lSchema = ["CNN", "CNX", "CPME", "CPME[ the ]CNX", "CPMME", "CNNSCPME"]

		# SEA BASED
		# Check for ships - special schemas
		if unit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_NAVAL'):
			lEnd = lEnd + ["ton", "town", "port"]
			lNoun = lNoun + ["lady", "jolly", "keel", "bow", "stern", "mast", "sail", "deck", "hull", "reef", "wave"]
			lEpithet = lEpithet + ["sea", "red", "blue", "grand", "barnacle", "gull"]
			lSchema = ["[The ]CNN", "[The ]CXN", "[The ]CNX", "[The ]CNSCN", "[The ]CNSCX", "CPME['s ]CN", "[The ]CPME", "[The ]CNX", "CNX", "CN['s ]CN"]

		# # #
		# Pick a Schema
		sSchema = lSchema[CyGame().getSorenRandNum(len(lSchema), "Name Gen")]
		sFull = ""
		sKeep = ""
		iUpper = 0
		iKeep = 0
		iSkip = 0

		# Run through each character in schema to generate name
		for iCount in xrange(0,len(sSchema)):
			sAdd=""
			iDone = 0
			sAction = sSchema[iCount]
			if iSkip == 1:
				if sAction == "]":
					iSkip = 0
				else:
					sAdd = sAction
					iDone = 1
			else:					# MAIN SECTION
				if sAction == "P": 	# Pre 	: beginnings of names
					sAdd = lPre[CyGame().getSorenRandNum(len(lPre), "Name Gen")]
					iDone = 1
				if sAction == "M":	# Mid 	: middle syllables
					sAdd = lMid[CyGame().getSorenRandNum(len(lMid), "Name Gen")]
					iDone = 1
				if sAction == "E":	# End	: end of names
					sAdd = lEnd[CyGame().getSorenRandNum(len(lEnd), "Name Gen")]
					iDone = 1
				if sAction == "X":	# Epithet	: epithet word part
					#epithets ("e" was taken!)
					sAdd = lEpithet[CyGame().getSorenRandNum(len(lEpithet), "Name Gen")]
					iDone = 1
				if sAction == "N":	# Noun	: noun word part
					#noun
					sAdd = lNoun[CyGame().getSorenRandNum(len(lNoun), "Name Gen")]
					iDone = 1
				if sAction == "S":	# Space	: a space character. (Introduced before [ ] was possible )
					sAdd =  " "
					iDone = 1
				if sAction == "D":	# Dash	: a - character. Thought to be common and useful enough to warrant inclusion : Introduced before [-] was possible
					sAdd =  "-"
					iDone = 1
				if sAction == "A":	# '		: a ' character - as for -, introduced early
					sAdd = "'"
					iDone = 1
				if sAction == "C":	# Caps	: capitalizes first letter of next phrase generated. No effect on non-letters.
					iUpper = 1
				if sAction == "K":	# Keep	: stores the next phrase generated for re-use with U
					iKeep = 1
				if sAction == "U":	# Use	: re-uses a stored phrase.
					sAdd = sKeep
					iDone = 1
				if sAction == "[":	# Print	: anything between [] is added to the final phrase "as is". Useful for [ the ] and [ of ] among others.
					iSkip = 1
			# capitalizes phrase once.
			if iUpper == 1 and iDone == 1:
				sAdd = sAdd.capitalize()
				iUpper = 0
			# stores the next phrase generated.
			if iKeep == 1 and iDone == 1:
				sKeep = sAdd
				iKeep = 0
			# only adds the phrase if a new bit was actally created.
			if iDone == 1:
				sFull = sFull + sAdd

		# trim name length
		if len(sFull) > 25:
			sFull = sFull[:25]
		#CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), "NAME : "+sFull, 'AS2D_POSITIVE_DINK', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Spells/Rob Grave.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)

		return sFull

	def setArcanePromotionFromRedundantManas(self, pUnit):
		pPlayer = gc.getPlayer(pUnit.getOwner())
		szPrefix = 'PROMOTION_'
		szPrefixTrait = 'TRAIT_'
		for eMana in en.leAllManas:
			iNum = pPlayer.getNumAvailableBonuses(eMana)
			szManaType = gc.getBonusInfo(eMana).getType()[11:]	# remove 'BONUS_MANA_'
#			if iNum > 1:
			if iNum > 1 or pPlayer.hasTrait(gc.getInfoTypeForString(szPrefixTrait + szManaType + '_MAGIC_MASTER')):
#				szManaType = gc.getBonusInfo(eMana).getType()[11:]	# remove 'BONUS_MANA_'
				pUnit.setHasPromotion(gc.getInfoTypeForString(szPrefix + szManaType + '1'), True)
#				if (iNum > 2 and unit.isHasPromotion(en.ePromotionChanneling2)):
				if (( iNum > 2 or pPlayer.hasTrait(gc.getInfoTypeForString(szPrefixTrait + szManaType + '_MAGIC_MASTER')) ) and pUnit.isHasPromotion(en.ePromotionChanneling2)):
					pUnit.setHasPromotion(gc.getInfoTypeForString(szPrefix + szManaType + '2'), True)
#					if (iNum > 3 and unit.isHasPromotion(en.ePromotionChanneling3)):
					if (( iNum > 3 or pPlayer.hasTrait(gc.getInfoTypeForString(szPrefixTrait + szManaType + '_MAGIC_MASTER')) ) and pUnit.isHasPromotion(en.ePromotionChanneling3)):
						pUnit.setHasPromotion(gc.getInfoTypeForString(szPrefix + szManaType + '3'), True)

	def removeTemporaryTraits(self, ePlayer, eTraitSource):
		pPlayer = gc.getPlayer(ePlayer)
		for eTrait in xrange(gc.getNumTraitInfos()):
			if pPlayer.hasTrait(eTrait):
				pPlayer.setHasTraitWithSource(eTrait, False, eTraitSource)

##--------	Expanded Spell Engine: Added by Denev 2009/12/13
	def setPromotionRecruitee(self, pUnit, iPromotedPercent):
		iUnitCombat = pUnit.getUnitCombatType()
		if iUnitCombat == UnitCombatTypes.NO_UNITCOMBAT:
			if pUnit.getRace() == en.eRaceGolem:
				pCity = pUnit.plot().getPlotCity()
				pCity.applyBuildEffects(pUnit)
			return
		liStartingPromotions = [	gc.getInfoTypeForString('PROMOTION_AMPHIBIOUS'),
									gc.getInfoTypeForString('PROMOTION_BLESSED'),
									gc.getInfoTypeForString('PROMOTION_BLITZ'),
									gc.getInfoTypeForString('PROMOTION_BOUNTY_HUNTER'),
									gc.getInfoTypeForString('PROMOTION_COMBAT1'),
									gc.getInfoTypeForString('PROMOTION_COMBAT1'),
									gc.getInfoTypeForString('PROMOTION_COVER'),
									gc.getInfoTypeForString('PROMOTION_COURAGE'),
									gc.getInfoTypeForString('PROMOTION_DRILL1'),
									gc.getInfoTypeForString('PROMOTION_FORMATION'),
									gc.getInfoTypeForString('PROMOTION_HEROIC_DEFENSE'),
									gc.getInfoTypeForString('PROMOTION_HEROIC_STRENGTH'),
									gc.getInfoTypeForString('PROMOTION_LOYALTY'),
									gc.getInfoTypeForString('PROMOTION_MAGIC_RESISTANCE'),
									gc.getInfoTypeForString('PROMOTION_MOBILITY1'),
									gc.getInfoTypeForString('PROMOTION_MORALE'),
									gc.getInfoTypeForString('PROMOTION_COLD_RESISTANCE'),
									gc.getInfoTypeForString('PROMOTION_FIRE_RESISTANCE'),
									gc.getInfoTypeForString('PROMOTION_LIGHTNING_RESISTANCE'),
									gc.getInfoTypeForString('PROMOTION_POISON_RESISTANCE'),
									gc.getInfoTypeForString('PROMOTION_SENTRY'),
									gc.getInfoTypeForString('PROMOTION_SHIELD_OF_FAITH'),
									gc.getInfoTypeForString('PROMOTION_SHOCK'),
									gc.getInfoTypeForString('PROMOTION_SPIRIT_GUIDE'),
									gc.getInfoTypeForString('PROMOTION_STRONG'),
									gc.getInfoTypeForString('PROMOTION_VALOR')	]
		liStartingPromotions = [	iStartingPromotion
									for iStartingPromotion in liStartingPromotions
									if gc.getPromotionInfo(iStartingPromotion).getUnitCombat(iUnitCombat) or gc.getPromotionInfo(iStartingPromotion).getMinLevel() == -1	]
		if iUnitCombat == gc.getInfoTypeForString('UNITCOMBAT_RECON'):
			liStartingPromotions += [	gc.getInfoTypeForString('PROMOTION_FLANKING1'),
										gc.getInfoTypeForString('PROMOTION_SUBDUE_ANIMAL'),
										gc.getInfoTypeForString('PROMOTION_SUBDUE_ANIMAL'),
										gc.getInfoTypeForString('PROMOTION_SUBDUE_ANIMAL'),
										gc.getInfoTypeForString('PROMOTION_GUERILLA1'),
										gc.getInfoTypeForString('PROMOTION_POISONED_BLADE'),
										gc.getInfoTypeForString('PROMOTION_WOODSMAN1'),
										gc.getInfoTypeForString('PROMOTION_MARKSMAN')	]
		elif iUnitCombat == gc.getInfoTypeForString('UNITCOMBAT_ARCHER'):
			liStartingPromotions += [	gc.getInfoTypeForString('PROMOTION_CITY_GARRISON1'),
										gc.getInfoTypeForString('PROMOTION_CITY_GARRISON1'),
										gc.getInfoTypeForString('PROMOTION_CITY_GARRISON1'),
										gc.getInfoTypeForString('PROMOTION_DEFENSIVE'),
										gc.getInfoTypeForString('PROMOTION_DRILL1'),
										gc.getInfoTypeForString('PROMOTION_FLAMING_ARROWS'),
										gc.getInfoTypeForString('PROMOTION_GUERILLA1'),
										gc.getInfoTypeForString('PROMOTION_KEEN_SIGHT')	]
		elif iUnitCombat == gc.getInfoTypeForString('UNITCOMBAT_MOUNTED'):
			liStartingPromotions += [	gc.getInfoTypeForString('PROMOTION_FLANKING1'),
										gc.getInfoTypeForString('PROMOTION_FLANKING1'),
										gc.getInfoTypeForString('PROMOTION_FLANKING1'),
										gc.getInfoTypeForString('PROMOTION_FLANKING2'),
										gc.getInfoTypeForString('PROMOTION_FLANKING3'),
										gc.getInfoTypeForString('PROMOTION_MOBILITY1'),
										gc.getInfoTypeForString('PROMOTION_COMMANDO'),
										gc.getInfoTypeForString('PROMOTION_NIGHTMARE')	]
		elif iUnitCombat == gc.getInfoTypeForString('UNITCOMBAT_MELEE'):
			liStartingPromotions += [	gc.getInfoTypeForString('PROMOTION_CITY_RAIDER1'),
										gc.getInfoTypeForString('PROMOTION_CITY_RAIDER1'),
										gc.getInfoTypeForString('PROMOTION_CITY_RAIDER1'),
										gc.getInfoTypeForString('PROMOTION_DEFENSIVE'),
										gc.getInfoTypeForString('PROMOTION_ENCHANTED_BLADE'),
										gc.getInfoTypeForString('PROMOTION_GUERILLA1'),
										gc.getInfoTypeForString('PROMOTION_WOODSMAN1'),
										gc.getInfoTypeForString('PROMOTION_GUARDSMAN')	]
		elif iUnitCombat == gc.getInfoTypeForString('UNITCOMBAT_ADEPT'):
			liStartingPromotions += [	gc.getInfoTypeForString('PROMOTION_POTENCY'),
										gc.getInfoTypeForString('PROMOTION_AIR1'),
										gc.getInfoTypeForString('PROMOTION_BODY1'),
										gc.getInfoTypeForString('PROMOTION_CHAOS1'),
										gc.getInfoTypeForString('PROMOTION_DEATH1'),
										gc.getInfoTypeForString('PROMOTION_EARTH1'),
										gc.getInfoTypeForString('PROMOTION_ENCHANTMENT1'),
										gc.getInfoTypeForString('PROMOTION_ENTROPY1'),
										gc.getInfoTypeForString('PROMOTION_FIRE1'),
										gc.getInfoTypeForString('PROMOTION_ICE1'),
										gc.getInfoTypeForString('PROMOTION_LAW1'),
										gc.getInfoTypeForString('PROMOTION_LIFE1'),
										gc.getInfoTypeForString('PROMOTION_METAMAGIC1'),
										gc.getInfoTypeForString('PROMOTION_MIND1'),
										gc.getInfoTypeForString('PROMOTION_NATURE1'),
										gc.getInfoTypeForString('PROMOTION_SHADOW1'),
										gc.getInfoTypeForString('PROMOTION_SPIRIT1'),
										gc.getInfoTypeForString('PROMOTION_SUN1'),
										gc.getInfoTypeForString('PROMOTION_WATER1')	]
		liStartingPromotions = [iPromotion for iPromotion in liStartingPromotions if not pUnit.isHasPromotion(iPromotion)]
		for iLoop in xrange(10):
			if CyGame().getSorenRandNum(100, 'Recruit: starting promotion roll') < iPromotedPercent:
				iRnd = CyGame().getSorenRandNum(len(liStartingPromotions), 'Recruit: starting promotion kind')
				iPromotion = liStartingPromotions.pop(iRnd)
				pUnit.setHasPromotion(iPromotion, True)
				iPromotedPercent //= 2
				liStartingPromotions = [iStartingPromotion for iStartingPromotion in liStartingPromotions if iStartingPromotion != iPromotion]
			else:
				break
##--------	Expanded Spell Engine: End Modify

##--------	Advanced Rules: Added by Denev
	def spawnSailorsDirgeCrew(self, pSailorsDirgeUnit):
		pUndeadPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER() + gc.getInfoTypeForString('BARBARIAN_UNDEAD'))

		iGameProgress = (CyGame().getCurrentPeriod() * 100) // CyGame().getNumPeriods()
		if iGameProgress < 20:	# Period 0~1
			iNumUnits = 4
			lszUndeads = ['UNIT_SKELETON', 'UNIT_SPECTRE', 'UNIT_DROWN']
		elif iGameProgress < 40:	# Period ~2
			iNumUnits = 5
			lszUndeads = ['UNIT_SPECTRE', 'UNIT_DROWN', 'UNIT_DISEASED_CORPSE']
		elif iGameProgress < 55:	# Period ~3
			iNumUnits = 6
			lszUndeads = ['UNIT_SPECTRE', 'UNIT_DROWN', 'UNIT_DISEASED_CORPSE', 'UNIT_WRAITH']
		elif iGameProgress < 70:	# Period ~4
			iNumUnits = 7
			lszUndeads = ['UNIT_DISEASED_CORPSE', 'UNIT_WRAITH', 'UNIT_LICH']
		else:						# Period 5~7
			iNumUnits = 8
			lszUndeads = ['UNIT_WRAITH', 'UNIT_LICH']

		lszExtraPromotions = ['PROMOTION_HEROIC_STRENGTH', 'PROMOTION_HEROIC_STRENGTH', 'PROMOTION_HEROIC_DEFENSE', 'PROMOTION_COMBAT1', 'PROMOTION_EMPOWER1']
		for iIndex in xrange(iNumUnits):
			eUndeadUnit = gc.getInfoTypeForString(lszUndeads[CyGame().getSorenRandNum(len(lszUndeads), "Sailor's Dirge Crew")])
			pCrewUnit = pUndeadPlayer.initUnit(eUndeadUnit, pSailorsDirgeUnit.getX(), pSailorsDirgeUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			if CyGame().getSorenRandNum(100, "Sailor's Dirge Crew Promotion 1") < iGameProgress:
				eExtraPromotion = gc.getInfoTypeForString(lszExtraPromotions[CyGame().getSorenRandNum(len(lszExtraPromotions), "Sailor's Dirge Crew Promotion 2")])
				pCrewUnit.setHasPromotion(eExtraPromotion, True)
			if eUndeadUnit == gc.getInfoTypeForString('UNIT_LICH'):
				if CyGame().getSorenRandNum(2, "Sailor's Dirge Crew Lich") < 1:
					pCrewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WATER1'), True)
					pCrewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WATER2'), True)
					pCrewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WATER3'), True)
				else:
					pCrewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_AIR1'), True)
					pCrewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_AIR2'), True)
					pCrewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_AIR3'), True)
			if pSailorsDirgeUnit.isFull():
				break
##--------	Advanced Rules: End Add

##--------	Multiple Civilization Heroes: Added by Denev 2011/12/11
	def getDeadHero(self, ePlayer):
		pPlayer = gc.getPlayer(ePlayer)
		eCivilization = pPlayer.getCivilizationType()
		iNumCivilizationHeroes = gc.getCivilizationInfo(eCivilization).getNumCivilizationHeroes()
		for iIndex in xrange(iNumCivilizationHeroes):
			eHero = gc.getCivilizationInfo(eCivilization).getCivilizationHero(iIndex)
			eHeroClass = gc.getUnitInfo(eHero).getUnitClassType()
			if CyGame().isUnitClassMaxedOut(eHeroClass, 0):
				for eLoopPlayer in xrange(gc.getMAX_PLAYERS()):
					pLoopPlayer = gc.getPlayer(eLoopPlayer)
					if pLoopPlayer.getUnitClassCount(eHeroClass) > 0:
						break
				else:
					return eHero
		return UnitTypes.NO_UNIT
##--------	Multiple Civilization Heroes: End Add

#Kaijin >>>
#ORBI START
#ゲーム開始時：沼と沼地の設置
	"""
	def doWetland(self):
		for i in xrange (CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(i)
			if pPlot.getImprovementType() == ImprovementTypes.NO_IMPROVEMENT:
				if pPlot.getFeatureType() == gc.getInfoTypeForString('FEATURE_SWAMP'):
					pPlot.setTerrainType(gc.getInfoTypeForString('TERRAIN_MARSH'),True,True)
					if not gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_LAIRS):
						if CyGame().getSorenRandNum(100, "Bob") < 20:
							pPlot.setImprovementType(gc.getInfoTypeForString('IMPROVEMENT_TROLL_CAVE'))
			if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_MOUNT_KALSHEKK'):
				pPlot.setFeatureType(gc.getInfoTypeForString('FEATURE_DEEP_JUNGLE'), 0)
#ゲーム開始時：巣窟の設置
	def doPutLair(self):
		for i in xrange (CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(i)
			if pPlot.getImprovementType() == ImprovementTypes.NO_IMPROVEMENT:
				if pPlot.getFeatureType() == en.eFeatureJungle:
					if pPlot.isFlatlands():
						if pPlot.getBonusType(TeamTypes.NO_TEAM) == BonusTypes.NO_BONUS:
							if not gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_LAIRS):
								if CyGame().getSorenRandNum(100, "Bob") < 5:
									pPlot.setImprovementType(gc.getInfoTypeForString('IMPROVEMENT_RUINS'))
#ゲーム開始時：水晶原の設置
	def doCrystalplain(self):
		iCrystal = gc.getInfoTypeForString('FEATURE_CRYSTAL_PLAINS')
		for i in xrange (CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(i)
			iFeature = pPlot.getFeatureType()
			iTerrain = pPlot.getTerrainType()
			if iFeature == FeatureTypes.NO_FEATURE and pPlot.isRiver() and pPlot.isFlatlands() and pPlot.getBonusType(-1) == -1:
				if iTerrain in (en.eTerrainSnow, en.eTerrainTundra):
					pPlot.setFeatureType(iCrystal, 0)
	"""

#巣窟なし: 追加巣窟の撤去
	"""
	def doNoLairsOAC(self):
		for i in xrange (CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(i)
			if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_TROLL_CAVE'):
				pPlot.setImprovementType(-1)
			elif pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_HILLGIANT_STEADING'):
				pPlot.setImprovementType(-1)
			elif pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_GRIFFIN_NEST'):
				pPlot.setImprovementType(-1)
			elif pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_DEN_WOLF'):
				pPlot.setImprovementType(-1)
			elif pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_DEN_GORILLA'):
				pPlot.setImprovementType(-1)
			elif pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_DEN_TIGER'):
				pPlot.setImprovementType(-1)
			elif pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_HAUNTED_RUINS'):
				pPlot.setImprovementType(-1)
			elif pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_DEN_SPIDER'):
				pPlot.setImprovementType(-1)
	"""

#巣窟なし: 巣窟の追加設置
	def doMoreLairsOAC(self):
		"""
		for i in xrange (CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(i)
			if pPlot.getImprovementType() == ImprovementTypes.NO_IMPROVEMENT and pPlot.getNumUnits() == 0 and (pPlot.isFlatlands() or pPlot.isHills()) and pPlot.getBonusType(-1) == -1:
				if CyGame().getSorenRandNum(100, "Bob") < 16:
					iFeature = pPlot.getFeatureType()
					liLairs = [	gc.getInfoTypeForString('IMPROVEMENT_DUNGEON')	]
					#Swamp
					if iFeature == gc.getInfoTypeForString('FEATURE_SWAMP'):
						liLairs += [	gc.getInfoTypeForString('IMPROVEMENT_DEN_SPIDER')	]
						if pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_MARSH'):
							liLairs += [	gc.getInfoTypeForString('IMPROVEMENT_TROLL_CAVE')	]
					#Forest
					elif iFeature == gc.getInfoTypeForString('FEATURE_FOREST'):
						liLairs += [	gc.getInfoTypeForString('IMPROVEMENT_DEN_TIGER')	]
						if pPlot.getTerrainType() == en.eTerrainTundra:
							liLairs += [	gc.getInfoTypeForString('IMPROVEMENT_DEN_WOLF')	]
					#Jungle
					elif iFeature == en.eFeatureJungle:
						liLairs += [	gc.getInfoTypeForString('IMPROVEMENT_DEN_GORILLA'),
								gc.getInfoTypeForString('IMPROVEMENT_DEN_SPIDER')	]
						if pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_GRASS'):
							liLairs += [	gc.getInfoTypeForString('IMPROVEMENT_RUINS')	]
						elif pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_PLAINS'):
							liLairs += [	gc.getInfoTypeForString('IMPROVEMENT_RUINS')	]
						elif pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_MARSH'):
							liLairs += [	gc.getInfoTypeForString('IMPROVEMENT_RUINS')	]
					#Desert
					if pPlot.getTerrainType() == en.eTerrainDesert:
						liLairs += [	gc.getInfoTypeForString('IMPROVEMENT_BARROW'),
								gc.getInfoTypeForString('IMPROVEMENT_HAUNTED_RUINS')	]
					#Grass
					elif pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_GRASS'):
						liLairs += [	gc.getInfoTypeForString('IMPROVEMENT_GOBLIN_FORT')	]
					#Plains
					elif pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_PLAINS'):
						liLairs += [	gc.getInfoTypeForString('IMPROVEMENT_GOBLIN_FORT'),
								gc.getInfoTypeForString('IMPROVEMENT_LION_DEN')	]
					#Marsh
					elif pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_MARSH'):
						liLairs += [	gc.getInfoTypeForString('IMPROVEMENT_GOBLIN_FORT')	]
					#Tundra
					elif pPlot.getTerrainType() == en.eTerrainTundra:
						liLairs += [	gc.getInfoTypeForString('IMPROVEMENT_GOBLIN_FORT')	]
					#Hills
					if pPlot.isHills():
						liLairs += [	gc.getInfoTypeForString('IMPROVEMENT_GRIFFIN_NEST')	]
						if pPlot.getTerrainType() == en.eTerrainDesert:
							liLairs += [	gc.getInfoTypeForString('IMPROVEMENT_HILLGIANT_STEADING')	]
						if pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_GRASS'):
							liLairs += [	gc.getInfoTypeForString('IMPROVEMENT_HILLGIANT_STEADING')	]
						if pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_PLAINS'):
							liLairs += [	gc.getInfoTypeForString('IMPROVEMENT_HILLGIANT_STEADING')	]

					iLairImprovement = liLairs[CyGame().getSorenRandNum(len(liLairs), "Pick Lair")]
					pPlot.setImprovementType(iLairImprovement)
		"""
		leAllLairs = []
		for eImprovement in xrange(gc.getNumImprovementInfos()):
			kImprovement = gc.getImprovementInfo(eImprovement)
			if not kImprovement.isUnique():
				if kImprovement.getPythonExplore() != "":
					leAllLairs += [eImprovement]

		for i in xrange (CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(i)
			if pPlot.getImprovementType() == ImprovementTypes.NO_IMPROVEMENT and pPlot.getNumUnits() == 0 and pPlot.getBonusType(-1) == -1:
				if CyGame().getSorenRandNum(100, "Bob") < 16:
					leLairs = [eLair for eLair in leAllLairs if pPlot.canHaveImprovement(eLair, PlayerTypes.NO_PLAYER, 0)]
					if len(leLairs) > 0:
						eLairImprovement = leLairs[CyGame().getSorenRandNum(len(leLairs), "Pick Lair")]
						pPlot.setImprovementType(eLairImprovement)

#Placement of the HauntedLand
	"""
	def doHauntedLand(self):
		for i in xrange (CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(i)
			if pPlot.getImprovementType() in (gc.getInfoTypeForString('IMPROVEMENT_BARROW'), gc.getInfoTypeForString('IMPROVEMENT_HAUNTED_RUINS')):
				pPlot.setFeatureType(gc.getInfoTypeForString('FEATURE_HAUNTED_LANDS'), -1)
	"""

# マサトル/クアリ/アルタイルでの獣道化とそれ以外の文明での道路化
	def doTrail(self):
		eAltair = gc.getInfoTypeForString('CIVILIZATION_ALTAIR')
		eMazatl = gc.getInfoTypeForString('CIVILIZATION_MAZATL')
		eCualli = gc.getInfoTypeForString('CIVILIZATION_CUALLI')
		eRoad = gc.getInfoTypeForString('ROUTE_ROAD')
		eTrail = gc.getInfoTypeForString('ROUTE_TRAIL')

		for i in xrange (CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(i)
			if pPlot.isOwned():
				if gc.getPlayer(pPlot.getOwner()).getCivilizationType() in (eAltair, eMazatl, eCualli):
					if pPlot.getRouteType() == eRoad:
						if CyGame().getSorenRandNum(100, "Trail") < 20:
							pPlot.setRouteType(eTrail)
				else:
					if pPlot.getRouteType() == eTrail:
						if CyGame().getSorenRandNum(100, "Road") < 30:
							pPlot.setRouteType(eRoad)

#マサトル/クアリのジャングル発生
	def doDeepJungle(self, iPlayer, pPlot):
		"""
		iAncientForest = gc.getInfoTypeForString('FEATURE_FOREST_ANCIENT')
		iLizJungle = gc.getInfoTypeForString('FEATURE_DEEP_JUNGLE')
		iVolcano = gc.getInfoTypeForString('FEATURE_VOLCANO')
		iGrassland = gc.getInfoTypeForString('TERRAIN_GRASS')
		iPlains = gc.getInfoTypeForString('TERRAIN_PLAINS')
		iMarsh = gc.getInfoTypeForString('TERRAIN_MARSH')
		iPlainsChance = 2
		iJungleChance = 10
		iBonus = pPlot.getBonusType(-1)
		iFeature = pPlot.getFeatureType()
		iImprovement = pPlot.getImprovementType()
		iTerrain = pPlot.getTerrainType()

		pPlayer = gc.getPlayer(iPlayer)
		if pPlot.getFeatureType() in (iAncientForest, en.eFeatureForest):
			if CyGame().getSorenRandNum(50, "Jungle") < iJungleChance:
				pPlot.setFeatureType(en.eFeatureJungle, 0)
				iFeature = pPlot.getFeatureType()
		if iFeature == en.eFeatureJungle:
			if CyGame().getSorenRandNum(50, "LizJungle") < iJungleChance:
				pPlot.setFeatureType(iLizJungle, 0)
		if iTerrain == iPlains and not pPlot.isHills():
			iChance = iPlainsChance
			if pPlot.isRiver():
				iChance = iPlainsChance * 5
			if CyGame().getSorenRandNum(1000, "Plains") < iChance:
				pPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
				pPlot.clearColdCounter()
				pPlot.setTerrainType(iGrassland, True, True)
		if pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_ECONOMY')) == gc.getInfoTypeForString('CIVIC_LOST_LANDS'):
			if iTerrain == iGrassland and not pPlot.isHills():
				if CyGame().getSorenRandNum(1000, "Marsh") < 100:
					pPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
					pPlot.clearColdCounter()
					pPlot.setTerrainType(iMarsh, True, True)
					point = pPlot.getPoint()
					if pPlot.isVisibleToWatchingHuman():
						CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPRING'), point)

			if pPlot.isPeak():
				if CyGame().getSorenRandNum(1000, "Volcano") < 50:
					pPlot.setPlotType(PlotTypes.PLOT_LAND, True, True)
					pPlot.setFeatureType(iVolcano, 0)
					point = pPlot.getPoint()
					if pPlot.isVisibleToWatchingHuman():
						CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_ARTILLERY_SHELL_EXPLODE'), point)
						CyAudioGame().Play3DSound("AS3D_UN_GRENADE_EXPLODE", point.x, point.y, point.z)
		"""
		pPlayer = gc.getPlayer(iPlayer)
		eTerrain = pPlot.getTerrainType()
		eFeature = pPlot.getFeatureType()
		if eFeature == en.eFeatureForest:
			if eTerrain == en.eTerrainGrass:
				if CyGame().getSorenRandNum(1000, "Jungle") < 100:
					pPlot.setFeatureType(en.eFeatureJungle, 0)
			elif eTerrain == en.eTerrainPlains:
				if CyGame().getSorenRandNum(1000, "Grass") < 10:
					pPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
					pPlot.clearColdCounter()
					pPlot.setTerrainType(en.eTerrainGrass, True, True)
		elif eFeature == en.eFeatureJungle:
			if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_PRIESTHOOD')):
				if CyGame().getSorenRandNum(1000, "DeepJungle") < 50:
					pPlot.setFeatureType(en.eFeatureDeepJungle, 0)
		if pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_ECONOMY')) == gc.getInfoTypeForString('CIVIC_LOST_LANDS'):
			if pPlot.isPeak():
				if CyGame().getSorenRandNum(1000, "Volcano") < 50:
					pPlot.setPlotType(PlotTypes.PLOT_LAND, True, True)
					pPlot.setFeatureType(en.eFeatureVolcano, 0)

#ORBI END

#Artail Start アルタイルの砂漠化＆沼地化
	def doDesert(self, iPlayer, pPlot):
		"""
		iAncientForest = gc.getInfoTypeForString('FEATURE_FOREST_ANCIENT')
		iLizJungle = gc.getInfoTypeForString('FEATURE_DEEP_JUNGLE')
		iMarsh = gc.getInfoTypeForString('TERRAIN_MARSH')

		iDesertChance = 0
		iMarshChance = 0

		pPlayer = gc.getPlayer(iPlayer)
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_EDUCATION')):
			iDesertChance += 1
			iMarshChance += 1
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_SANITATION')):
			iDesertChance += 1
			iMarshChance += 1
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_MILITARY_STRATEGY')):
			iDesertChance += 2
			iMarshChance += 2
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_BRONZE_WORKING')):
			iDesertChance += 2
			iMarshChance += 2
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_SMELTING')):
			iDesertChance += 8
			iMarshChance += 8
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_IRON_WORKING')):
			iDesertChance += 2
			iMarshChance += 2
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_MITHRIL_WORKING')):
			iDesertChance += 8
			iMarshChance += 8
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_STIRRUPS')):
			iDesertChance += 2
			iMarshChance += 2
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_ELEMENTALISM')):
			iDesertChance += 8
			iMarshChance += 8
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_NECROMANCY')):
			iDesertChance += 2
			iMarshChance += 2
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_SORCERY')):
			iDesertChance += 2
			iMarshChance += 2
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_ANIMAL_HANDLING')):
			iDesertChance -= 2
			iMarshChance -= 2
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_ANIMAL_MASTERY')):
			iDesertChance -= 2
			iMarshChance -= 2
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_FERAL_BOND')):
			iDesertChance -= 2
			iMarshChance -= 2
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_COMMUNE_WITH_NATURE')):
			iDesertChance -= 2
			iMarshChance -= 2
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_PRIESTHOOD')):
			iDesertChance -= 2
			iMarshChance -= 2
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_RELIGIOUS_LAW')):
			iDesertChance -= 2
			iMarshChance -= 2
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_THEOLOGY')):
			iDesertChance -= 2
			iMarshChance -= 2
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_DIVINE_ESSENCE')):
			iDesertChance -= 2
			iMarshChance -= 2
		if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_OMNISCIENCE')):
			iDesertChance += 50
			iMarshChance += 50

		iBonus = pPlot.getBonusType(TeamTypes.NO_TEAM)
		iFeature = pPlot.getFeatureType()
		iImprovement = pPlot.getImprovementType()
		iTerrain = pPlot.getTerrainType()
		eHellGrassland = gc.getInfoTypeForString('TERRAIN_BROKEN_LANDS')
		eHellPlains = gc.getInfoTypeForString('TERRAIN_FIELDS_OF_PERDITION')
		eHellDesert = gc.getInfoTypeForString('TERRAIN_BURNING_SANDS')
		eShallows = gc.getInfoTypeForString('TERRAIN_SHALLOWS')
		if iTerrain in (en.eTerrainGrass, en.eTerrainPlains, eHellPlains, eHellGrassland):
			iChance = iDesertChance
			if pPlot.isRiver():
				if not pPlot.isFlatlands():
					iChance *= 15
			if iTerrain in (en.eTerrainGrass, eHellGrassland):
				if CyGame().getSorenRandNum(1000, "Marsh") < iMarshChance:
					if pPlot.isFreshWater() and pPlot.isFlatlands():
						if not pPlot.isRiver():
							if iBonus == BonusTypes.NO_BONUS:
								pPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
								pPlot.clearColdCounter()
								pPlot.setTerrainType(iMarsh, True, True)
								if pPlot.isVisibleToWatchingHuman():
									CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SNOWFALL'), pPlot.getPoint())
			elif iTerrain != iMarsh:
				if CyGame().getSorenRandNum(1000, "Desert") < iChance:
					if iBonus == BonusTypes.NO_BONUS:
						pPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
						pPlot.clearColdCounter()
						pPlot.setTerrainType(en.eTerrainDesert, True, True)
						if pPlot.isVisibleToWatchingHuman():
							CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SCORCH'), pPlot.getPoint())
			elif (	(iTerrain != en.eTerrainDesert and iFeature == en.eFeatureFloodPlains)
				and (iTerrain != eHellDesert and iFeature == gc.getInfoTypeForString('FEATURE_OBSIDIAN_PLAINS'))	):
				pPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
				pPlot.clearColdCounter()
				pPlot.setTerrainType(en.eTerrainDesert, True, True)
				if pPlot.isVisibleToWatchingHuman():
					CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SCORCH'), pPlot.getPoint())
		if iTerrain in (en.eTerrainDesert, eHellDesert):
			if iFeature in (en.eFeatureForest, en.eFeatureJungle, en.eFeatureScrub, iAncientForest, iLizJungle):
				pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
		"""
		eTerrain = pPlot.getTerrainType()
		eFeature = pPlot.getFeatureType()
		eBonus = pPlot.getBonusType(TeamTypes.NO_TEAM)
		eImprovement = pPlot.getImprovementType()
		pPlayer = gc.getPlayer(iPlayer)

		if pPlot.isPeak():
			return
		if pPlot.isWater():
			return
		if eBonus != BonusTypes.NO_BONUS:
			return
		if eImprovement != ImprovementTypes.NO_IMPROVEMENT and gc.getImprovementInfo(eImprovement).isUnique():
			return

		iChance = 0
		if pPlayer.isCivic(gc.getInfoTypeForString('CIVIC_PRINCIPLE_OF_THE_OLD')):
			iChance += 10
		if pPlayer.isFeatAccomplished(FeatTypes.FEAT_GLOBAL_SPELL):
			iChance += 50

		if iChance > 0 and eTerrain in (en.eTerrainGrass, en.eTerrainPlains, en.eTerrainBrokenLands, en.eTerrainFieldsofPerdition):

			if eFeature == FeatureTypes.NO_FEATURE:
				iChance += 5
			if eImprovement == ImprovementTypes.NO_IMPROVEMENT:
				iChance += 5
			pCity = pPlot.getWorkingCity()
			if pCity.isNone() or pCity.getOwner() != iPlayer or pCity.isSettlement():
				iChance *= 3
				pCity = CyMap().findCity(pPlot.getX(), pPlot.getY(), iPlayer, TeamTypes.NO_TEAM, False, False, TeamTypes.NO_TEAM, DirectionTypes.NO_DIRECTION, pCity)
			elif not pCity.isDisorder() and not pCity.isWorkingPlot(pPlot):
				iChance *= 2

			bChange = False
			iFood = pPlot.getYield(YieldTypes.YIELD_FOOD)
			iProduction = pPlot.getYield(YieldTypes.YIELD_PRODUCTION)
			iCommerce = pPlot.getYield(YieldTypes.YIELD_COMMERCE)
			iGameSpeedPercent = gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent()

			if not (pPlot.isFlatlands() and pPlot.isRiver()):
				if CyGame().getSorenRandNum(cyFlatValue(1000, iGameSpeedPercent, False), "Desert") < iChance:
					pPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
					pPlot.clearColdCounter()
					pPlot.setTerrainType(en.eTerrainDesert, True, True)
					if not pPlot.canHaveFeature(eFeature):
						pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
					if pPlot.isVisibleToWatchingHuman():
						CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SCORCH'), pPlot.getPoint())
					bChange = True
			if not bChange and pPlot.isFlatlands():
				if CyGame().getSorenRandNum(cyFlatValue(1000, iGameSpeedPercent, False), "Marsh") < iChance:
					pPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
					pPlot.clearColdCounter()
					pPlot.setTerrainType(en.eTerrainMarsh, True, True)
					if not pPlot.canHaveFeature(eFeature):
						pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
					if pPlot.isVisibleToWatchingHuman():
						CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SNOWFALL'), pPlot.getPoint())
					bChange = True

			if bChange and not pCity.isNone():
				szBotton = gc.getTerrainInfo(pPlot.getTerrainType()).getButton()
				if pPlot.getYield(YieldTypes.YIELD_FOOD) < iFood:
					iChangeFood = 20 * (iFood - pPlot.getYield(YieldTypes.YIELD_FOOD))
					iChangeFood = cyFlatValue(iChangeFood, iGameSpeedPercent, False)
					pCity.changeFood(iChangeFood)
					szText = CyTranslator().getText("TXT_KEY_MESSAGE_DO_DESERT_FOOD", (pCity.getNameKey(), iChangeFood, ))
					CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szText, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szBotton, en.eColorWhite, pPlot.getX(), pPlot.getY(), True, True)
				if pPlot.getYield(YieldTypes.YIELD_PRODUCTION) < iProduction:
					iChangeProduction = 30 * (iProduction - pPlot.getYield(YieldTypes.YIELD_PRODUCTION))
					iChangeProduction = cyFlatValue(iChangeProduction, iGameSpeedPercent, False)
					pCity.setFeatureProduction(pCity.getFeatureProduction() + iChangeProduction)
					szText = CyTranslator().getText("TXT_KEY_MESSAGE_DO_DESERT_PRODUCTION", (pCity.getNameKey(), iChangeProduction, ))
					CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szText, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szBotton, en.eColorWhite, pPlot.getX(), pPlot.getY(), True, True)
				if pPlot.getYield(YieldTypes.YIELD_COMMERCE) < iCommerce:
					iChangeCommerce = 50 * (iCommerce - pPlot.getYield(YieldTypes.YIELD_COMMERCE))
					iChangeCommerce = cyFlatValue(iChangeCommerce, iGameSpeedPercent, False)
					pPlayer.changeGold(iChangeCommerce)
					szText = CyTranslator().getText("TXT_KEY_MESSAGE_DO_DESERT_GOLD", (iChangeCommerce, ))
					CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szText, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szBotton, en.eColorWhite, pPlot.getX(), pPlot.getY(), True, True)
#Altair End

#Nival Start
	def doNival(self, iPlayer, pPlot):
		pPlayer = gc.getPlayer(iPlayer)
		iFrostlingPlayer = gc.getInfoTypeForString('BARBARIAN_FROSTLING') + gc.getBARBARIAN_PLAYER()
		pFrostlingPlayer = gc.getPlayer(iFrostlingPlayer)

		# Snowman - Frostling Spawn
		if not gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_BARBARIANS):
			if CyGame().getSorenRandNum(100, "Barbarian Frostling") < 5:
				if pPlot.getImprovementType() in (	gc.getInfoTypeForString('IMPROVEMENT_SNOWMAN'), 
													gc.getInfoTypeForString('IMPROVEMENT_GIANT_SNOWMAN'), 
													gc.getInfoTypeForString('IMPROVEMENT_GREATER_SNOWMAN')	):

					if not pPlot.isVisibleEnemyUnit(iFrostlingPlayer):
						if not pPlayer.isHasTech(gc.getInfoTypeForString('TECH_COMMUNE_WITH_NATURE')):
							liUnits = [ 	gc.getInfoTypeForString('UNIT_WHITE_FANG'), 
											gc.getInfoTypeForString('UNIT_SNOW_LIZARD'), 
											gc.getInfoTypeForString('UNIT_FROST_GIANT') 	]
						else:
							liUnits = [ 	gc.getInfoTypeForString('UNIT_SHADOWS_OF_ICE'), 
											gc.getInfoTypeForString('UNIT_SNOWSTORM_AVATAR'), 
											gc.getInfoTypeForString('UNIT_ICE_STATUE') 	]

						iNewSpawnUnit = liUnits[CyGame().getSorenRandNum(len(liUnits), "SpawnUnit Select")]
						pNewSpawnUnit = pFrostlingPlayer.initUnit(iNewSpawnUnit, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
						if pNewSpawnUnit.getUnitAIType() != gc.getInfoTypeForString('UNITAI_ATTACK'):
							pNewSpawnUnit.setUnitAIType(gc.getInfoTypeForString('UNITAI_ATTACK'))

						if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_GIANT_SNOWMAN'):
							pNewSpawnUnit.changeExperience(2, -1, False, False, False)
						elif pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_GREATER_SNOWMAN'):
							pNewSpawnUnit.changeExperience(5, -1, False, False, False)
		""" Move to CvUnitAIInterface
		# Barbarian Frostling
		for iUnitIndex in xrange(pPlot.getNumUnits() -1, -1, -1):
			pUnit = pPlot.getUnit(iUnitIndex)
			if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_MOKKA'):
				if pUnit.getOwner() == iFrostlingPlayer:
					pNewUnit = pPlayer.initUnit(pUnit.getUnitType(), pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
					pNewUnit.convert(pUnit)
					pNewUnit.changeImmobileTimer(1)
		"""

	def doBuildingColdEffects(self, pPlot):
		if pPlot.getImprovementType() == en.eImprovementSmoke:
			pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)

		eFeature = pPlot.getFeatureType()
		if eFeature in (en.eFeatureForest, en.eFeatureJungle, en.eFeatureDeepJungle):
			pPlot.setFeatureType(en.eFeatureForest, 2)
		elif eFeature in (en.eFeatureFlames, en.eFeatureScrub):
			pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)

#Nival End

#Baldralfar Start
	def doBaldralfar(self, iPlayer):
		pPlayer = gc.getPlayer(iPlayer)
		iAncientForest = gc.getInfoTypeForString('FEATURE_FOREST_ANCIENT')
		iForestNew = gc.getInfoTypeForString('FEATURE_FOREST_NEW')
		eDiseased = gc.getInfoTypeForString('PROMOTION_DISEASED')
		eWeaken = gc.getInfoTypeForString('PROMOTION_WEAKEN')
		for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
			pLoopPlayer = gc.getPlayer(iLoopPlayer)
			if pLoopPlayer.isAlive():
				apUnitList = PyPlayer(iLoopPlayer).getUnitList()
				for pUnit in apUnitList:
					pPlot = pUnit.plot()
					iFeature = pPlot.getFeatureType()
					if pPlot.isOwned():
						if pPlot.getOwner() == iPlayer:
							if iFeature in (iAncientForest, en.eFeatureForest, iForestNew):
								if pUnit.isAlive():
									if CyGame().getSorenRandNum(100, "Miasma Diseased") < 3:
										pUnit.setHasPromotion(eDiseased, True)
										if pUnit.isHasPromotion(eDiseased):
											CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_BALDRALFAR_MIASMA_DISEASED", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Promotions/Diseased.dds', en.eColorRed,pUnit.getX(),pUnit.getY(), True, True)
									if CyGame().getSorenRandNum(100, "Miasma Weaken") < 10:
										pUnit.setHasPromotion(eWeaken, True)
										if pUnit.isHasPromotion(eWeaken):
											CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_BALDRALFAR_MIASMA_WEAKEN", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Promotions/Weak.dds', en.eColorRed,pUnit.getX(),pUnit.getY(), True, True)
#Baldralfar End

#Aristrakh Start
	def doTurnAristrakh(self, iPlayer, pCity):
##--------	Advanced Convert Life Force: Modified by ent
		"""
		pPlayer = gc.getPlayer(iPlayer)

		#Initialise Turn Mod
		iCounterMod = 1
		iCounterMod += CyGame().getGlobalCounter()

		#gamespeed adjustments
		iSpeedMod = 1
		estiEnd = CyGame().getEstimateEndTurn()
		if ( estiEnd >= 1500 ):
			iSpeedMod = 2.0
		elif ( estiEnd >= 750 ):
			iSpeedMod = 1.5
		elif ( estiEnd >= 500 ):
			iSpeedMod = 1.0
		elif ( estiEnd >= 330 ):
			iSpeedMod = 0.67
		else:
			iSpeedMod = iSpeedMod

		#city number modifier
		iCNrMod = 0
		for pyCity in PyPlayer(iPlayer).getCityList():
			iCNrMod += 100

		#multiple cities increase growth rate slightly
		iCNrMod = 100 + 15 * iCNrMod
	
		#Dark Ritual modifier
		iDRMod = 10
		RitualCount = gc.getTeam(pPlayer.getTeam()).getProjectCount(gc.getInfoTypeForString('PROJECT_DEATH_RITUAL'))
		if RitualCount > 0:
			iDRMod += (2 * RitualCount)

		iBuildingBonus = 2
		#get max population modifier
		if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_PALACE_ARISTRAKH')):
			iBuildingBonus += 2
		if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_HAUNTED_ROADS')):
			iBuildingBonus += 2
		if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_CORRUPTED_SOIL')):
			iBuildingBonus += 1
		if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_BONE_CAGE')):
			iBuildingBonus += 1
		if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_BURIAL_MOUND')):
			iBuildingBonus += 1
		if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_FORLORN_VAULT')):
			iBuildingBonus += 2
		if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_HALLS_OF_THE_DEAD')):
			iBuildingBonus += 1
		if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_MAUSOLEUM')):
			iBuildingBonus += 2
		if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_MORTUARY_ENCLOSURE')):
			iBuildingBonus += 1
		if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_HAUNTED_TOWER')):
			iBuildingBonus += 1
		if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_UNHOLY_GLYPHS')):
			iBuildingBonus += 2
		if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_UNEARTHED_GRAVES')):
			iBuildingBonus += 1
		if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_SOUL_PRISON')):
			iBuildingBonus += 2
		if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_CATACOMBS')):
			iBuildingBonus += 2
		iMaxPop = iBuildingBonus

		#current population modifier
		iPop = pCity.getPopulation()

		# Difficulty level modifier
		iAImod = 1
		if not pPlayer.isHuman():
			iDifficulty = int(gc.getGame().getHandicapType())
			iAImod = 0.7 + (iDifficulty * 0.1)

		if not self.getFertileTerrain(pCity):
			#only cities below the max population can growth
			if iPop < iMaxPop:
				#checks if city should growth
				iChance = CyGame().getSorenRandNum(100, "Population growth")
				if iChance * iAImod < 20:
					if iDRMod * iCounterMod // (iSpeedMod * iAImod) > ((3 * iPop) - iMaxPop) // iCNrMod:
						self.ConvertLifeForce(pCity)
		"""
		if pCity.isDisorder():
			return
		if pCity.healthRate(False, 0) < 0:
			return
		if self.getFertileTerrain(pCity):
			return

		ltBuildingBonuses = [	#eBuilding												#iBonus
								(gc.getInfoTypeForString('BUILDING_PALACE_ARISTRAKH'),	2),
								(gc.getInfoTypeForString('BUILDING_HAUNTED_ROADS'),		2),
								(gc.getInfoTypeForString('BUILDING_CORRUPTED_SOIL'),	1),
								(gc.getInfoTypeForString('BUILDING_BONE_CAGE'),			1),
								(gc.getInfoTypeForString('BUILDING_BURIAL_MOUND'),		1),
								(gc.getInfoTypeForString('BUILDING_FORLORN_VAULT'),		2),
								(gc.getInfoTypeForString('BUILDING_HALLS_OF_THE_DEAD'),	1),
								(gc.getInfoTypeForString('BUILDING_MAUSOLEUM'),			3),
								(gc.getInfoTypeForString('BUILDING_MORTUARY_ENCLOSURE'),2),
								(gc.getInfoTypeForString('BUILDING_HAUNTED_TOWER'),		2),
								(gc.getInfoTypeForString('BUILDING_UNHOLY_GLYPHS'),		2),
								(gc.getInfoTypeForString('BUILDING_UNEARTHED_GRAVES'),	1),
								(gc.getInfoTypeForString('BUILDING_SOUL_PRISON'),		2),
								(gc.getInfoTypeForString('BUILDING_CATACOMBS'),			3)	]
		pPlayer = gc.getPlayer(iPlayer)
		iRitualCount = gc.getTeam(pPlayer.getTeam()).getProjectCount(gc.getInfoTypeForString('PROJECT_DEATH_RITUAL'))
		iMaxPop = 2 + iRitualCount
		for eBuilding, iBonus in ltBuildingBonuses:
			if pCity.isHasActiveBuilding(eBuilding):
				iMaxPop += iBonus
		iMaxPop = min(iMaxPop, 25)
		iPop = pCity.getPopulation()
		if iPop >= iMaxPop:
			return

		iChance = 20
		iChance = cyFlatValue(iChance, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getGrowthPercent(), False)
		iChance = cyFlatValue(iChance, gc.getEraInfo(CyGame().getStartEra()).getGrowthPercent(), False)
		iChance *= 100 + (10 * iRitualCount)
		iChance /= 100
		iRnd = 100
		if not pPlayer.isHuman() and not pPlayer.isBarbarian():
			iRnd = gc.getHandicapInfo(CyGame().getHandicapType()).getAIGrowthPercent()
		if CyGame().getSorenRandNum(iRnd, "Population growth") < iChance:
			self.ConvertLifeForce(pCity)

##--------	Advanced Convert Life Force: End Modify

##--------	Bug Fix: Modified by ent
	"""
	def getFertileTerrain(self, pCity):
		bValid = True

		pPlot = pCity.plot()
		lpRangedPlots = cyGetRangedPlots(pPlot, pCity.getPlotRadius(), False, False, TeamTypes.NO_TEAM)
		for pTargetPlot in lpRangedPlots:
			pWorkingCity = pTargetPlot.getWorkingCity()
			if pWorkingCity.getOwner() == pCity.getOwner() and pWorkingCity.getID() == pCity.getID():
				if pTargetPlot.getImprovementType() != ImprovementTypes.NO_IMPROVEMENT:
					if gc.getImprovementInfo(pTargetPlot.getImprovementType()).isUnique():
						continue
				if pTargetPlot.isImpassable():
					continue
				if pTargetPlot.isCity():
					continue
				if pTargetPlot.isWater():
					continue
				if pTargetPlot.getFeatureType() != gc.getInfoTypeForString('FEATURE_HAUNTED_LANDS'):
					bValid = False
					break

		return bValid

	def ConvertLifeForce(self, pCity):
		pCity.changePopulation(1)

		pPlot = pCity.plot()
		iThreshold = 18 * 100 // gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getBuildPercent()
		pBestPlot = None
		iBestValue = -1
		lpRangedPlots = cyGetRangedPlots(pPlot, pCity.getPlotRadius(), False, False, TeamTypes.NO_TEAM)
		for pTargetPlot in lpRangedPlots:
			pWorkingCity = pTargetPlot.getWorkingCity()
			if pWorkingCity.getOwner() == pCity.getOwner() and pWorkingCity.getID() == pCity.getID():
				if pTargetPlot.getImprovementType() != ImprovementTypes.NO_IMPROVEMENT:
					if gc.getImprovementInfo(pTargetPlot.getImprovementType()).isUnique():
						continue
				if pTargetPlot.isCity():
					continue
				if pTargetPlot.isImpassable():
					continue
				if pTargetPlot.isWater():
					continue
				iCountDiff = cyGetPlotCounterDiff(pTargetPlot, iThreshold)
				if not iCountDiff > 0:
					if pTargetPlot.getFeatureType() != gc.getInfoTypeForString('FEATURE_HAUNTED_LANDS'):
						iValue = CyGame().getSorenRandNum(500, "Select Plot")
						if iValue > iBestValue:
							iBestValue = iValue
							pBestPlot = pTargetPlot

		if pBestPlot is not None:
			pBestPlot.setFeatureType(gc.getInfoTypeForString('FEATURE_HAUNTED_LANDS'), -1)
			if pBestPlot.isVisibleToWatchingHuman():
				CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_PIT_BEAST_SUMMON'), pBestPlot.getPoint())
	"""

	def getFertileTerrain(self, pCity):
		pPlot = pCity.plot()
		ePlayer = pCity.getOwner()
		iCityID = pCity.getID()
		eHauntedLands = gc.getInfoTypeForString('FEATURE_HAUNTED_LANDS')
		lpRangedPlots = cyGetRangedPlots(pPlot, pCity.getPlotRadius(), False, False, TeamTypes.NO_TEAM)
		for pTargetPlot in lpRangedPlots:
			pWorkingCity = pTargetPlot.getWorkingCity()
			# 都市圏が重なる別の都市での望まぬ自動消費を回避可能
			if pWorkingCity.getOwner() == ePlayer and pWorkingCity.getID() == iCityID:
				if pTargetPlot.isWater():
					continue
				if pTargetPlot.isCity():
					continue
				if pTargetPlot.isImpassable():
					continue
				if pTargetPlot.getImprovementType() != ImprovementTypes.NO_IMPROVEMENT:
					if gc.getImprovementInfo(pTargetPlot.getImprovementType()).isUnique():
						continue
				if pTargetPlot.getFeatureType() != eHauntedLands:
					return False
		return True

	def ConvertLifeForce(self, pCity):
		pCity.changePopulation(1)

		pPlot = pCity.plot()
		ePlayer = pCity.getOwner()
		iCityID = pCity.getID()
		eHauntedLands = gc.getInfoTypeForString('FEATURE_HAUNTED_LANDS')
		pBestPlot = None
		iBestValue = -1
		lpRangedPlots = cyGetRangedPlots(pPlot, pCity.getPlotRadius(), False, False, TeamTypes.NO_TEAM)
		for pTargetPlot in lpRangedPlots:
			# 都市圏の重なる都市に労働タイルを譲渡しても盟約での消費は回避不可
			if pTargetPlot.getOwner() == ePlayer:
				if pTargetPlot.isWater():
					continue
				if pTargetPlot.isCity():
					continue
				if pTargetPlot.isImpassable():
					continue
				if pTargetPlot.getImprovementType() != ImprovementTypes.NO_IMPROVEMENT:
					if gc.getImprovementInfo(pTargetPlot.getImprovementType()).isUnique():
						continue
				if pTargetPlot.getFeatureType() != eHauntedLands:
					iValue = CyGame().getSorenRandNum(200, "Select Plot")
					pWorkingCity = pTargetPlot.getWorkingCity()
					# 労働タイルを優先
					if pWorkingCity.getOwner() == ePlayer and pWorkingCity.getID() == iCityID:
						iValue += 200
					if iValue > iBestValue:
						iBestValue = iValue
						pBestPlot = pTargetPlot

		if pBestPlot is not None:
			pBestPlot.setFeatureType(eHauntedLands, -1)
			if pBestPlot.isVisibleToWatchingHuman():
				CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_PIT_BEAST_SUMMON'), pBestPlot.getPoint())
##--------Bug Fix: End Modify
#Aristrakh End

	"""
# doBarbarianPirates Start 海賊のランダム出現
	def doBarbarianPirates(self, iGameTurn):
		iPiratesTurn = cyFlatValue(100, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), True)
		if iGameTurn >= iPiratesTurn:
			pBestPlot = -1
			iBestPlot = -1
			for i in xrange (CyMap().numPlots()):
				pPlot = CyMap().plotByIndex(i)
				iPlot = -1
				if pPlot.isWater() and not pPlot.getFeatureType() == gc.getInfoTypeForString('FEATURE_ICE'):
					if pPlot.getNumUnits() == 0:
						iPlot = CyGame().getSorenRandNum(500, "Barbarian Pirates")
						iPlot = iPlot + (pPlot.area().getNumTiles() * 10)
						if not pPlot.isOwned() and iPlot > iBestPlot:
							iBestPlot = iPlot
							pBestPlot = pPlot
			liNavalTechs = [	gc.getInfoTypeForString('TECH_ASTRONOMY'),
								gc.getInfoTypeForString('TECH_OPTICS'),
								gc.getInfoTypeForString('TECH_NAVIGATION')	]
			liWeapTechs = [	gc.getInfoTypeForString('TECH_IRON_WORKING'),
								gc.getInfoTypeForString('TECH_BRONZE_WORKING')	]
			if iBestPlot > 500:
				pPiratesBarbarian = gc.getPlayer(gc.getInfoTypeForString('BARBARIAN_PIRATES') + gc.getBARBARIAN_PLAYER())
				iPirateRank = 1
				iPirate = gc.getInfoTypeForString('UNIT_GALLEY')
				iBoarding = gc.getInfoTypeForString('UNIT_TRANSITION_SAILOR')
				iWeaponRank = 1
				iWeapon = -1
				# Pirate Rank
				for iTech in liNavalTechs:
					iCount = 0
					for iLoopTeam in xrange(gc.getMAX_CIV_TEAMS()):
						pLoopTeam = gc.getTeam(iLoopTeam)
						if pLoopTeam.isHasTech(iTech):
							iCount += 1
						if iCount >= 3:
							if iTech == gc.getInfoTypeForString('TECH_ASTRONOMY'):
								if CyGame().getSorenRandNum(100, "Pirates Naval") < 50:
									iPirate = gc.getInfoTypeForString('UNIT_GALLEON')
								else:
									iPirate = gc.getInfoTypeForString('UNIT_FRIGATE')
								iBoarding = gc.getInfoTypeForString('UNIT_BOARDING_PARTY')
								iPirateRank = 4
							elif iTech == gc.getInfoTypeForString('TECH_OPTICS') and iPirateRank < 3:
								if CyGame().getSorenRandNum(100, "Pirates Naval") < 50:
									iPirate = gc.getInfoTypeForString('UNIT_PIRATE')
								else:
									iPirate = gc.getInfoTypeForString('UNIT_CARAVEL')
								iBoarding = gc.getInfoTypeForString('UNIT_BOARDING_PARTY')
								iPirateRank = 3
							elif iTech == gc.getInfoTypeForString('TECH_NAVIGATION') and iPirateRank < 2:
								iPirate = gc.getInfoTypeForString('UNIT_TRIREME')
								iBoarding = gc.getInfoTypeForString('UNIT_TRANSITION_SAILOR')
								iPirateRank = 2
				# Weapon Rank
				for iTech in liWeapTechs:
					iCount = 0
					for iLoopTeam in xrange(gc.getMAX_CIV_TEAMS()):
						pLoopTeam = gc.getTeam(iLoopTeam)
						if pLoopTeam.isHasTech(iTech):
							iCount += 1
						if iCount >= 3:
							if iTech == gc.getInfoTypeForString('TECH_IRON_WORKING'):
								iWeapon = gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS')
								iWeaponRank = 3
							elif iTech == gc.getInfoTypeForString('TECH_BRONZE_WORKING') and iWeaponRank < 2:
								iWeapon = gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS')
								iWeaponRank = 2
				if not (pBestPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_OCEAN') and iPirateRank < 3):
					newPirate = pPiratesBarbarian.initUnit(iPirate, pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
					newPirate.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HIDDEN_NATIONALITY'), False)
					if newPirate.getUnitAIType() != gc.getInfoTypeForString('UNITAI_PIRATE_SEA'):
						newPirate.setUnitAIType(gc.getInfoTypeForString('UNITAI_PIRATE_SEA'))
					if newPirate.cargoSpaceAvailable(newPirate.specialCargo(), newPirate.domainCargo()) >= 1:
						iSpaceAvailable = newPirate.cargoSpaceAvailable(newPirate.specialCargo(), newPirate.domainCargo())
						if iSpaceAvailable > 2:
							iSpaceAvailable = iSpaceAvailable / 2 + 1
						for iCardo in xrange(iSpaceAvailable):
							newBoarding = pPiratesBarbarian.initUnit(iBoarding, newPirate.getX(), newPirate.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
							if iWeapon != -1:
								newBoarding.setHasPromotion(iWeapon, True)
							if newBoarding.getUnitAIType() != gc.getInfoTypeForString('UNITAI_PILLAGE'):
								newBoarding.setUnitAIType(gc.getInfoTypeForString('UNITAI_PILLAGE'))

# doBarbarianPirates End 
	"""

# doBarbarianAnimals Start - 野生動物のランダム出現
	def doBarbarianAnimals(self):
		iAliveTeam = CyGame().countCivTeamsEverAlive()
		pAnimalPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER() + en.eBarbarianAnimal)

		# Kraken
		if (CyGame().countKnownTechNumTeams(gc.getInfoTypeForString('TECH_ASTRONOMY')) * 100 // iAliveTeam) > 20:
			pBestPlot = -1
			iBestValue = 0
			for i in range (CyMap().numPlots()):
				pPlot = CyMap().plotByIndex(i)
				if pPlot.getNumUnits() == 0:
					if pPlot.isWater() and not pPlot.isImpassable():
						iValue = CyGame().getSorenRandNum(500, "Barbarian Animals")
						iValue += pPlot.area().getNumTiles() * 10
						if pPlot.isOwned():
							iValue = iValue // 2
						if iValue > iBestValue:
							iBestValue = iValue
							pBestPlot = pPlot

			if pBestPlot != -1:
				pNewUnit = pAnimalPlayer.initUnit(gc.getInfoTypeForString('UNIT_KRAKEN'), pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ANIMAL, DirectionTypes.DIRECTION_SOUTH)
				pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HIDDEN_NATIONALITY'), False)
				pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAK'), True)
				pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WITHERED'), True)

		# Hippogriff
		eFeatureVoid = gc.getInfoTypeForString('FEATURE_VOID')
		eFeatureDistortion = gc.getInfoTypeForString('FEATURE_DISTORTION')
		if (CyGame().countKnownTechNumTeams(gc.getInfoTypeForString('TECH_FERAL_BOND')) * 100 // iAliveTeam) > 20:
			pBestPlot = -1
			iBestValue = 0
			for i in range (CyMap().numPlots()):
				pPlot = CyMap().plotByIndex(i)
				if pPlot.getNumUnits() == 0:
					if pPlot.getTerrainType() != en.eTerrainOcean and not pPlot.getFeatureType() in (eFeatureVoid, eFeatureDistortion):
						iValue = CyGame().getSorenRandNum(500, "Barbarian Animals")
						iValue += not pPlot.isWater() * 10
						if pPlot.isOwned():
							iValue = iValue // 2
						if iValue > iBestValue:
							iBestValue = iValue
							pBestPlot = pPlot

			if pBestPlot != -1:
				pNewUnit = pAnimalPlayer.initUnit(gc.getInfoTypeForString('UNIT_HIPPOGRIFF'), pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
# doBarbarianAnimals End 

#Scions Start
	def doTurnScions(self, iPlayer, pCity):
		pPlayer = gc.getPlayer(iPlayer)
		py = PyPlayer(iPlayer)

		if pCity.isCapital():
			bSpawnValid = self.doChanceAwakenedSpawn(iPlayer)
			if bSpawnValid:
				pSpawnUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_REBORN'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

		pPlot = pCity.plot()
		if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_GIFT')):
			lpRangedPlots = cyGetRangedPlots(pPlot, pCity.getPlotRadius() - 1, False, False, TeamTypes.NO_TEAM)
			for pTargetPlot in lpRangedPlots:
				pWorkingCity = pTargetPlot.getWorkingCity()
				if pWorkingCity.getOwner() == pCity.getOwner() and pWorkingCity.getID() == pCity.getID():
					if not pTargetPlot.isCity():
						if not pTargetPlot.isWater() and not pTargetPlot.isImpassable():
							if pTargetPlot.getFeatureType() != en.eFeatureHauntedLands:
								pTargetPlot.setFeatureType(en.eFeatureHauntedLands, -1)

	## Awakend
	def doChanceAwakenedSpawn(self, iPlayer):
		if iPlayer == -1:
			pPlayer = gc.getPlayer(gc.getGame().getActivePlayer())
		else:
			pPlayer = gc.getPlayer(iPlayer)

		bSpawnValid = False
		iSpawnChance = pPlayer.getGuildPlusCounter(51) + 1
		iSpawnChanceBaseValue = 1
		iSpawnChanceMod = 100


	# Chance the awakened spawn.

		pCapital = pPlayer.getCapitalCity()
		if pPlayer.getNumCities() == 1 and pCapital.getPopulation() == 1:
			pCapital.changePopulation(1)
		elif pPlayer.getGuildPlusCounter(51) == 99:
			bSpawnValid = True
			pPlayer.setGuildPlusCounter(51, pPlayer.getGuildPlusCounter(52))
			pPlayer.setGuildPlusCounter(52, 0)
			iSpawnChance = pPlayer.getGuildPlusCounter(51) + 1
		elif pPlayer.getGuildPlusCounter(51) > CyGame().getSorenRandNum(100, "ChanceAwakenedSpawn"):
			bSpawnValid = True
			pPlayer.setGuildPlusCounter(51, 0)
			iSpawnChance = 0


		# Turn elapsed modifiers.
		iGameTurn = gc.getGame().getGameTurn()
		iThresholdTurn = cyFlatValue(150, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
		iTurnValue = 1
		if iThresholdTurn > iGameTurn * 15:
			iTurnValue = 10
		elif iThresholdTurn > iGameTurn * 5:
			iTurnValue = 3
		elif iThresholdTurn > iGameTurn:
			iTurnValue = 2
		iSpawnChanceBaseValue = iTurnValue


	# Various modifiers.

		# Total popuration modifiers.
		pCapital = pPlayer.getCapitalCity()
		iSpawnChanceMod += pPlayer.getTotalPopulation()

		# Buildings modifiers.
		iSpawnChanceMod += pPlayer.countNumBuildings(gc.getInfoTypeForString('BUILDING_SHRINE_TO_KYLORIN')) * 2
		iSpawnChanceMod += pPlayer.countNumBuildings(gc.getInfoTypeForString('BUILDING_IMPERIAL_CENOTAPH')) * 4
		iSpawnChanceMod += pPlayer.countNumBuildings(gc.getInfoTypeForString('BUILDING_HALL_OF_THE_COVENANT')) * 7
		iSpawnChanceMod += pPlayer.countNumBuildings(gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_GIFT')) * 4

		# Luxury modifiers.
		iSpawnChanceMod += pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_INCENSE')) * 5
		iSpawnChanceMod += pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_FUR')) * 5
		iSpawnChanceMod += pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_SILK')) * 7
		iSpawnChanceMod += pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_GOLD')) * 5
		iSpawnChanceMod += pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_GEMS')) * 5
		iSpawnChanceMod += pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_IVORY')) * 7
		iSpawnChanceMod += pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_DYE')) * 3
		iSpawnChanceMod += pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_COTTON')) * 3

		# The Body-mana bonus given by the Flesh Studio.
		iFleshStudio = pPlayer.countNumBuildings(gc.getInfoTypeForString('BUILDING_FLESH_STUDIO'))
		iBodyMana = pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_MANA_BODY'))
		iSpawnChanceMod += iFleshStudio * iBodyMana * 15

		# Resource Patrian Artifact modifier.
		iArtifacts = pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_PATRIAN_ARTIFACTS'))
		iSpawnChanceMod += iArtifacts * 10

		# Total LandPlots modifier.
		iSpawnChanceMod += (int(CyMap().getLandPlots()) // 40) + 6

		# Godking gives a xx% mod.
		if pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_GOVERNMENT')) == gc.getInfoTypeForString('CIVIC_GOD_KING'):
			iSpawnChanceMod += 25

		# Trait-Expansive gives a xx% mod.
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_EXPANSIVE')):
			iSpawnChanceMod += 15

		# Difficulty level modifier
		iModifierValue = int(gc.getGame().getHandicapType()) * 3

		if not pPlayer.isHuman() and iModifierValue > 0:
			iSpawnChanceMod += iModifierValue


	# Result.
		iSpawnChance += int((iSpawnChanceBaseValue * iSpawnChanceMod) // 100)

		if iSpawnChance >= 100:
			iSpawnChance -= 100
			pPlayer.setGuildPlusCounter(51, 99)
			pPlayer.setGuildPlusCounter(52, (iSpawnChance - 1))
		else:
			pPlayer.setGuildPlusCounter(51, (iSpawnChance - 1))

		if bSpawnValid:
			return bSpawnValid

	def doAddPopValid(self, pCity):
		if not pCity.isHuman():
			if pCity.isSettlement():
				return False
		if pCity.happyLevel() - pCity.unhappyLevel(0) > 0:
			if pCity.goodHealth() - pCity.badHealth(False) > 0:
				return True
		return False
#Scions End

#Megisus Start
	def doForestEclipse(self, iPlayer):
		pPlayer = gc.getPlayer(iPlayer)
		iBonusChance = 40
		iBonusChance += pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_MANA_EARTH')) * 20

		iGameSpeed = gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getGoldenAgePercent()
		iThreshold = 100
		iMod = (iThreshold * iGameSpeed) // 10

		leBonusTypes = [		gc.getInfoTypeForString('BONUS_SILK'),
								gc.getInfoTypeForString('BONUS_COFFEE'),
								gc.getInfoTypeForString('BONUS_TEA')		]

		liWatersideBonuses = [	gc.getInfoTypeForString('BONUS_COW'),
								gc.getInfoTypeForString('BONUS_PIG'),
								gc.getInfoTypeForString('BONUS_SHEEP'),
								gc.getInfoTypeForString('BONUS_WINE'),
								gc.getInfoTypeForString('BONUS_SALT')		]

		liHillBonuses = [		gc.getInfoTypeForString('BONUS_COPPER'),
								gc.getInfoTypeForString('BONUS_GEMS'),
								gc.getInfoTypeForString('BONUS_AMBER')		]

		liForestBonuses = [		gc.getInfoTypeForString('BONUS_DEER'),
								gc.getInfoTypeForString('BONUS_FUR'),
								gc.getInfoTypeForString('BONUS_MUSHROOMS')	]

		liJungleBonuses = [		gc.getInfoTypeForString('BONUS_BANANA'),
								gc.getInfoTypeForString('BONUS_COTTON'),
								gc.getInfoTypeForString('BONUS_DYE'),
								gc.getInfoTypeForString('BONUS_ORANGE'),
								gc.getInfoTypeForString('BONUS_LEMON')		]

		if CyGame().getSorenRandNum(iMod, "Bonus PopUp Chance") < iBonusChance:
			pBestPlot = -1
			iBestPlot = -1
			iForestAncient = gc.getInfoTypeForString('FEATURE_FOREST_ANCIENT')
			iDeepJungle = gc.getInfoTypeForString('FEATURE_DEEP_JUNGLE')

			for iPlotIndex in range (CyMap().numPlots()):
				pPlot = CyMap().plotByIndex(iPlotIndex)
				iPlot = -1
				if pPlot.isOwned():
					if pPlot.getOwner() == iPlayer:
						if not pPlot.isWater():
							if pPlot.getBonusType(TeamTypes.NO_TEAM) == BonusTypes.NO_BONUS:
								if pPlot.isRiver():
									iPlot += CyGame().getSorenRandNum(500, "Place Bonus")
								if pPlot.isFreshWater():
									iPlot += CyGame().getSorenRandNum(500, "Place Bonus")
								if pPlot.isHills():
									iPlot += CyGame().getSorenRandNum(500, "Place Bonus")
								if pPlot.getFeatureType() in (en.eFeatureForest, iForestAncient):
									iPlot += CyGame().getSorenRandNum(500, "Place Bonus")
								if pPlot.getFeatureType() in (en.eFeatureJungle, iDeepJungle):
									iPlot += CyGame().getSorenRandNum(500, "Place Bonus")
				if iPlot > iBestPlot:
					iBestPlot = iPlot
					pBestPlot = pPlot

			if pBestPlot != -1:
				if pBestPlot.isFreshWater():
					leBonusTypes += liWatersideBonuses
				if pBestPlot.isHills():
					leBonusTypes += liHillBonuses
				if pBestPlot.getFeatureType() in (en.eFeatureForest, iForestAncient):
					leBonusTypes += liForestBonuses
				if pBestPlot.getFeatureType() in (en.eFeatureJungle, iDeepJungle):
					leBonusTypes += liJungleBonuses
				leBonusTypes.sort()

				eNewBonus = -1
				eNewBonus = leBonusTypes[CyGame().getSorenRandNum(len(leBonusTypes), "Bonuses Select")]

				if eNewBonus != -1:
					pBestPlot.setBonusType(eNewBonus)
					szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_BUILDING_FOREST_ECLIPSE', ())
					szButton = gc.getBonusInfo(eNewBonus).getButton()
					CyInterface().addMessage(iPlayer, False, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS3D_SPELL_INSPIRATION', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pBestPlot.getX(), pBestPlot.getY(), True, True)

					if pBestPlot.isVisibleToWatchingHuman():
						CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_CREATION'), pBestPlot.getPoint())

#Megisus End

# doFlood Start 氾濫原の発生と消失
	def doFlood(self):
		iCrystal = gc.getInfoTypeForString('FEATURE_CRYSTAL_PLAINS')
		iRnd = 0
		for i in xrange (CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(i)
			iBonus = pPlot.getBonusType(-1)
			iFeature = pPlot.getFeatureType()
			iTerrain = pPlot.getTerrainType()
			if iFeature == FeatureTypes.NO_FEATURE and pPlot.isRiver() and pPlot.isFlatlands() and iBonus == -1:
				if iTerrain == en.eTerrainDesert:
					if CyGame().getSorenRandNum(100, "Flood") < 24:
						pPlot.setFeatureType(en.eFeatureFloodPlains, 0)
				elif iTerrain in (en.eTerrainSnow, en.eTerrainTundra):
					if CyGame().getSorenRandNum(100, "Flood") < 24:
						pPlot.setFeatureType(iCrystal, 0)
			elif iFeature == en.eFeatureBlizzard and pPlot.isRiver() and pPlot.isFlatlands() and iBonus == -1:
				if iTerrain in (en.eTerrainSnow, en.eTerrainTundra):
					if CyGame().getSorenRandNum(100, "Flood") < 24:
						pPlot.setFeatureType(iCrystal, 0)
			elif iTerrain != en.eTerrainDesert and iFeature == en.eFeatureFloodPlains:
				pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
			elif (iTerrain != en.eTerrainSnow and iTerrain != en.eTerrainTundra) and iFeature == iCrystal:
				pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
# doFlood End

# 猛吹雪の発生と消失
	def doBlizzard(self):
##--------	Advanced Winter Projects: Modified by ent
		"""
		iNival = gc.getInfoTypeForString('CIVILIZATION_NIVAL')
		for i in xrange (CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(i)
			iFeature = pPlot.getFeatureType()
			iTerrain = pPlot.getTerrainType()
			if pPlot.isOwned():
				pPlayer = gc.getPlayer(pPlot.getOwner())
				if not pPlot.isPeak() and not pPlot.isCity():
					if iTerrain == en.eTerrainSnow and iFeature == FeatureTypes.NO_FEATURE:
						if pPlayer.getCivilizationType() == iNival:
							if CyGame().getSorenRandNum(100, "Blizzard") < 9:
								pPlot.setFeatureType(en.eFeatureBlizzard, 0)
						else:
							if CyGame().getSorenRandNum(100, "Blizzard") < 3:
								pPlot.setFeatureType(en.eFeatureBlizzard, 0)
					elif iTerrain == en.eTerrainSnow and iFeature == en.eFeatureBlizzard:
						if pPlayer.getCivilizationType() == iNival:
							if CyGame().getSorenRandNum(100, "Blizzard") < 9:
								pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
						else:
							if CyGame().getSorenRandNum(100, "Blizzard") < 15:
								pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)

			if pPlot.isPeak() or pPlot.isCity():
				if iFeature == en.eFeatureBlizzard:
					pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
			elif iTerrain in (en.eTerrainTundra, en.eTerrainSnow):
				if iFeature == en.eFeatureBlizzard:
					if CyGame().getSorenRandNum(100, "Blizzard") < 30:
						pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
			elif iTerrain != en.eTerrainSnow and iTerrain != en.eTerrainTundra:
				if iFeature == en.eFeatureBlizzard:
					pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
		"""
		def isNival(pPlot):
			if pPlot.isOwned():
				if gc.getPlayer(pPlot.getOwner()).getCivilizationType() == en.eCivilizationNival:
					return True
			return False
		bDeepening = gc.getGame().isProjectMaxedOut(gc.getInfoTypeForString('PROJECT_THE_DEEPENING'), 0)

		for i in xrange (CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(i)
			iFeature = pPlot.getFeatureType()
			iTerrain = pPlot.getTerrainType()
			if pPlot.isPeak() or pPlot.isCity() or pPlot.isWater():
				if iFeature == en.eFeatureBlizzard:
					pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
			elif iTerrain == en.eTerrainSnow:
				if iFeature == FeatureTypes.NO_FEATURE:
					if isNival(pPlot) or bDeepening:
						if CyGame().getSorenRandNum(100, "Blizzard") < 9:
							pPlot.setFeatureType(en.eFeatureBlizzard, 0)
					else:
						if CyGame().getSorenRandNum(100, "Blizzard") < 3:
							pPlot.setFeatureType(en.eFeatureBlizzard, 0)
				elif iFeature == en.eFeatureBlizzard:
					if isNival(pPlot) or bDeepening:
						if CyGame().getSorenRandNum(100, "Blizzard") < 9:
							pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
					else:
						if CyGame().getSorenRandNum(100, "Blizzard") < 15:
							pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
			elif iTerrain == en.eTerrainTundra:
				if iFeature == FeatureTypes.NO_FEATURE:
					if bDeepening:
						if CyGame().getSorenRandNum(100, "Blizzard") < 3:
							pPlot.setFeatureType(en.eFeatureBlizzard, 0)
				elif iFeature == en.eFeatureBlizzard:
					if CyGame().getSorenRandNum(100, "Blizzard") < 30:
						pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
			else:
				if iFeature == en.eFeatureBlizzard:
					pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
##--------	Advanced Winter Projects: End Modify

#Tiger Start
	## Steindorf and Smiley
	def doTigerSteindorfAndSmiley(self, iPlayer):
		pPlayer = gc.getPlayer(iPlayer)
		iTeam = pPlayer.getTeam()
		pTeam = gc.getTeam(iTeam)
		iSteindorf = gc.getInfoTypeForString('UNITCLASS_STEINDORF')
		iSmiley = gc.getInfoTypeForString('UNITCLASS_SMILEY')
		pCity = pPlayer.getCapitalCity()
		pCapitalCityPlot = pCity.plot()
		py = PyPlayer(iPlayer)

		bSmileyUnitValid = False
		if CyGame().isUnitClassMaxedOut(iSmiley, 0):
			bSmileyUnitValid = True

		if pTeam.isHasTech(gc.getInfoTypeForString('TECH_CURRENCY')):
			if not CyGame().isUnitClassMaxedOut(iSteindorf, 0):
				newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_STEINDORF'), pCapitalCityPlot.getX(), pCapitalCityPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

			##Steindorf assassination, and Smiley arrival.
			elif CyGame().isUnitClassMaxedOut(iSteindorf, 0) and not CyGame().isUnitClassMaxedOut(iSmiley, 0):
				bSteindorfValid = False
				for pLoopUnit in py.getUnitList():
					if pLoopUnit.getUnitType() == gc.getInfoTypeForString('UNIT_STEINDORF'):
						bSteindorfValid = True

				if bSteindorfValid == True:
					for pLoopUnit in py.getUnitList():
						if pLoopUnit.getUnitClassType() == iSteindorf:
							pLoopUnit.kill(True, iPlayer)
							newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_SMILEY'), pLoopUnit.getX(), pLoopUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
							newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_FUNERAL_MERCENARY'), pLoopUnit.getX(), pLoopUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
							newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_FUNERAL_MERCENARY'), pLoopUnit.getX(), pLoopUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
							CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_SMILEY_KILLING_STEINDORF",()), 'AS2D_UNIT_RISES', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pLoopUnit.getButton(), en.eColorRed, pLoopUnit.getX(), pLoopUnit.getY(), True, True)
							if( CyGame().getAIAutoPlay() == 0 ):
								self.addPopup(CyTranslator().getText("TXT_KEY_POPUP_SMILEY_KILLING_STEINDORF",()), str(gc.getUnitInfo(gc.getInfoTypeForString('UNIT_SMILEY')).getImage()))
				else:
					newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_SMILEY'), pCapitalCityPlot.getX(), pCapitalCityPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
					newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_FUNERAL_MERCENARY'), pCapitalCityPlot.getX(), pCapitalCityPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
					newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_FUNERAL_MERCENARY'), pCapitalCityPlot.getX(), pCapitalCityPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
					if( CyGame().getAIAutoPlay() == 0 ):
						self.addPopup(CyTranslator().getText("TXT_KEY_POPUP_CREATED_UNIT_SMILEY",()), str(gc.getUnitInfo(gc.getInfoTypeForString('UNIT_SMILEY')).getImage()))

			##Smiley estrangement
			elif pPlayer.getNumCities() >= 2 and CyGame().isUnitClassMaxedOut(iSmiley, 0) and pPlayer.getLeaderType() != gc.getInfoTypeForString('LEADER_SMILEY'):
				bSmileyUnitValid = False
				for pLoopUnit in py.getUnitList():
					if pLoopUnit.getUnitType() == gc.getInfoTypeForString('UNIT_SMILEY'):
						bSmileyUnitValid = True

				if bSmileyUnitValid:
					bIndependentValid = False
					for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
						iRand = CyGame().getSorenRandNum(100, "Smiley Independent")
						if gc.getPlayer(iLoopPlayer).getPlayersKilled() > 0 and CyGame().countCivPlayersAlive() <= 4:
							bIndependentValid = True
						elif gc.getPlayer(iLoopPlayer).getPlayersKilled() > 0 and CyGame().countCivPlayersAlive() <= 5:
							if iRand > 96:
								bIndependentValid = True
						elif gc.getPlayer(iLoopPlayer).getPlayersKilled() > 0 and CyGame().countCivPlayersAlive() <= 6:
							if iRand > 97:
								bIndependentValid = True
						elif gc.getPlayer(iLoopPlayer).getPlayersKilled() > 0 and CyGame().countCivPlayersAlive() <= 7:
							if iRand > 98:
								bIndependentValid = True

					if bIndependentValid == True:
						#Smiley Independent
						iSmileyPlayer = pPlayer.initNewEmpire(gc.getInfoTypeForString('LEADER_SMILEY'), gc.getInfoTypeForString('CIVILIZATION_TIGER'))
						if iSmileyPlayer != PlayerTypes.NO_PLAYER:
							pSmileyPlayer = gc.getPlayer(iSmileyPlayer)
							iFounderTeam = gc.getPlayer(iPlayer).getTeam()
							pFounderTeam = gc.getTeam(iFounderTeam)
							iSmileyTeam = gc.getPlayer(iSmileyPlayer).getTeam()
							pSmileyTeam = gc.getTeam(iSmileyTeam)

							#Globalcounter initialization
							self.doGlobalcounterInitialization(iSmileyPlayer)

							#SignOpenBorders
							pFounderTeam.signOpenBorders(iSmileyTeam)
							pSmileyTeam.signOpenBorders(iFounderTeam)
							for iPlotIndex in xrange(CyMap().numPlots()):
								pLoopPlot = CyMap().plotByIndex(iPlotIndex)
								if pLoopPlot.isRevealed(iFounderTeam, False):
									pLoopPlot.setRevealed(iSmileyTeam, True, False, iFounderTeam)
								if pLoopPlot.isRevealed(iSmileyTeam, False):
									pLoopPlot.setRevealed(iFounderTeam, True, False, iSmileyTeam)
							#CityAssignment
							pWorstCulture = -1
							pBestCulture = -1
							for pyCity in PyPlayer(iPlayer).getCityList():
								pAssignmentCity = pyCity.GetCy()
								if pWorstCulture == -1:
									pWorstCulture = pAssignmentCity.getCulture(iPlayer)
									pCityWorstCulture = pAssignmentCity
								elif pAssignmentCity.getCulture(iPlayer) <= pWorstCulture and pAssignmentCity != pCity:
									pWorstCulture = pAssignmentCity.getCulture(iPlayer)
									pCityWorstCulture = pAssignmentCity
								if pAssignmentCity.getCulture(iPlayer) > pBestCulture:
									pBestCulture = pAssignmentCity.getCulture(iPlayer)
							pCityWorstCulturePlot = pCityWorstCulture.plot()
							pSmileyPlayer.acquireCity(pCityWorstCulture, False, False)
							p2CityWorstCulture = pCityWorstCulturePlot.getPlotCity()
							p2CityWorstCulture.setCulture(iSmileyPlayer, pBestCulture, True)
							pSmileyPlayer.changeGold(1500)
							#Smiley & Funeral Mercenaries : Convert
							for pLoopUnit in py.getUnitList():
								pPlot = pLoopUnit.plot()
								if pLoopUnit.getOwner() == iPlayer:
									if pLoopUnit.getUnitType() == gc.getInfoTypeForString('UNIT_SMILEY') or pLoopUnit.getUnitType() == gc.getInfoTypeForString('UNIT_FUNERAL_MERCENARY') or pLoopUnit.getUnitType() == gc.getInfoTypeForString('UNIT_UNDEAD_MERCENARY'):
										newUnit = pSmileyPlayer.initUnit(pLoopUnit.getUnitType(), pCityWorstCulturePlot.getX(), pCityWorstCulturePlot.getY(), UnitAITypes.UNITAI_HERO, DirectionTypes.DIRECTION_SOUTH)
										newUnit.convert(pLoopUnit)
										newUnit.setHasCasted(True)
										if pLoopUnit.getUnitType() == gc.getInfoTypeForString('UNIT_SMILEY'):
											newUnit.setAvatarOfCivLeader(True)
											newUnit.changeCombatStr(2)
											if newUnit.getExperience() < 100:
												newUnit.setExperience(100, -1)
											newSettlerUnit1 = pSmileyPlayer.initUnit(gc.getInfoTypeForString('UNIT_SETTLER'), pCityWorstCulturePlot.getX(), pCityWorstCulturePlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
											newSettlerUnit2 = pSmileyPlayer.initUnit(gc.getInfoTypeForString('UNIT_SETTLER'), pCityWorstCulturePlot.getX(), pCityWorstCulturePlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
											newWorkerUnit1 = pSmileyPlayer.initUnit(gc.getInfoTypeForString('UNIT_WORKER'), pCityWorstCulturePlot.getX(), pCityWorstCulturePlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
											newWorkerUnit2 = pSmileyPlayer.initUnit(gc.getInfoTypeForString('UNIT_WORKER'), pCityWorstCulturePlot.getX(), pCityWorstCulturePlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
											newWorkerUnit3 = pSmileyPlayer.initUnit(gc.getInfoTypeForString('UNIT_WORKER'), pCityWorstCulturePlot.getX(), pCityWorstCulturePlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
											newWorkerUnit4 = pSmileyPlayer.initUnit(gc.getInfoTypeForString('UNIT_WORKER'), pCityWorstCulturePlot.getX(), pCityWorstCulturePlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
											newDefenseUnit1 = pSmileyPlayer.initUnit(gc.getInfoTypeForString('UNIT_LONGBOWMAN'), pCityWorstCulturePlot.getX(), pCityWorstCulturePlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
											newDefenseUnit2 = pSmileyPlayer.initUnit(gc.getInfoTypeForString('UNIT_LONGBOWMAN'), pCityWorstCulturePlot.getX(), pCityWorstCulturePlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
											newDefenseUnit3 = pSmileyPlayer.initUnit(gc.getInfoTypeForString('UNIT_LONGBOWMAN'), pCityWorstCulturePlot.getX(), pCityWorstCulturePlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
											newDefenseUnit4 = pSmileyPlayer.initUnit(gc.getInfoTypeForString('UNIT_LONGBOWMAN'), pCityWorstCulturePlot.getX(), pCityWorstCulturePlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
											newDefenseUnit5 = pSmileyPlayer.initUnit(gc.getInfoTypeForString('UNIT_LONGBOWMAN'), pCityWorstCulturePlot.getX(), pCityWorstCulturePlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
											newDefenseUnit6 = pSmileyPlayer.initUnit(gc.getInfoTypeForString('UNIT_LONGBOWMAN'), pCityWorstCulturePlot.getX(), pCityWorstCulturePlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
											iFuneralNum = pPlayer.getNumCities() * 4
											for iLoop in xrange(iFuneralNum):
												newFuneralUnit = pSmileyPlayer.initUnit(gc.getInfoTypeForString('UNIT_FUNERAL_MERCENARY'), pCityWorstCulturePlot.getX(), pCityWorstCulturePlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
											if( CyGame().getAIAutoPlay() == 0 ):
												CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_SMILEY_BETRAY",()), 'AS2D_UNIT_FALLS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pLoopUnit.getButton(), en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)
												self.addPopup(CyTranslator().getText("TXT_KEY_POPUP_SMILEY_BETRAY",()), str(gc.getUnitInfo(gc.getInfoTypeForString('UNIT_SMILEY')).getImage()))

	## 契約戦争
	def doTurnContract(self, ePlayer):
		pPlayer = gc.getPlayer(ePlayer)
		ePlayerTeam = pPlayer.getTeam()
		pPlayerTeam = gc.getTeam(ePlayerTeam)
		eContractor = pPlayer.getGuildPlusCounter(52)
		pContractor = gc.getPlayer(eContractor)
		eContractorTeam = pContractor.getTeam()
		pContractorTeam = gc.getTeam(eContractorTeam)

		if not pContractor.isAlive() or pContractorTeam.isAVassal():
			self.InitializeContract(pPlayer)
			self.addPlayerPopup(CyTranslator().getText('TXT_KEY_CONTRACT_BREACH_1',()), ePlayer)
			return
		if pPlayerTeam.isAtWar(eContractorTeam):
			self.InitializeContract(pPlayer)
			self.addPlayerPopup(CyTranslator().getText('TXT_KEY_CONTRACT_BREACH_2',()), ePlayer)
			return
		if pPlayerTeam.isAVassal():
			self.InitializeContract(pPlayer)
			return

		def getContractStatus():
		##記録された文明との間の契約状態
		# 契約を既に終えている:2、契約を正常に終了:1、契約を続行中:0、契約違反により終了:-1
			if eEnemy == -1:
				return 2
			pEnemy = gc.getPlayer(eEnemy)
			if not pEnemy.isAlive():
				return 1
			eEnemyTeam = pEnemy.getTeam()
			pEnemyTeam = gc.getTeam(eEnemyTeam)
			if pEnemyTeam.isAVassal():
				return 1
			pContractor = gc.getPlayer(eContractor)
			eContractorTeam = pContractor.getTeam()
			pContractorTeam = gc.getTeam(eContractorTeam)
			if not pContractorTeam.isAtWar(eEnemyTeam):
				return 1
			ePlayerTeam = pPlayer.getTeam()
			pPlayerTeam = gc.getTeam(ePlayerTeam)
			if not pPlayerTeam.isAtWar(eEnemyTeam):
				return -1
			return 0

		iNum = pPlayer.getGuildPlusCounter(59)
		iSuccess = 0
		for iIndex in xrange(iNum):
			eEnemy = pPlayer.getGuildPlusCounter(60 + iIndex)
			iContract = getContractStatus()
			if iContract == 2:
				iSuccess += 1
			elif iContract == 1:
				iSuccess += 1
				pPlayer.setGuildPlusCounter(60 + iIndex, -1)
				pEnemy = gc.getPlayer(eEnemy)
				eEnemyTeam = pEnemy.getTeam()
				pEnemyTeam = gc.getTeam(eEnemyTeam)
				if pEnemy.isAlive() and pPlayerTeam.isAtWar(eEnemyTeam) and not pEnemyTeam.isAVassal():
					pPlayerTeam.makePeace(eEnemyTeam)
					sEnemyName = gc.getCivilizationInfo(pEnemy.getCivilizationType()).getDescription()
					self.addPlayerPopup(CyTranslator().getText('TXT_KEY_CONTRACT_SUCCESS',(sEnemyName, )), ePlayer)
			elif iContract == -1:
				self.InitializeContract(pPlayer)
				self.addPlayerPopup(CyTranslator().getText('TXT_KEY_CONTRACT_BREACH_3',()), ePlayer)
				return

		#契約満了
		if iSuccess >= iNum:
			iKill = pPlayer.getGuildPlusCounter(53)
			iRequire = pPlayer.getGuildPlusCounter(55)
			if iRequire < iKill * 2:#最低限の仕事をしたかどうか判定
				self.RewardContract(ePlayer, 2, 'TXT_KEY_CONTRACT_EXPIRATION')
			else:
				self.addPlayerPopup(CyTranslator().getText('TXT_KEY_CONTRACT_BREACH_4',()), ePlayer)
			self.InitializeContract(pPlayer)

	##関連カウンタの初期化
	def InitializeContract(self, pPlayer):
		pPlayer.setGuildPlusCounter(50, 0)
		pPlayer.setGuildPlusCounter(51, -1)
		pPlayer.setGuildPlusCounter(52, -1)
		pPlayer.setGuildPlusCounter(53, 0)
		pPlayer.setGuildPlusCounter(54, 0)
		pPlayer.setGuildPlusCounter(55, 0)
		iNum = pPlayer.getGuildPlusCounter(59)
		for iIndex in xrange(iNum):
			pPlayer.setGuildPlusCounter(60 + iIndex, -1)
		pPlayer.setGuildPlusCounter(59, 0)

	##報酬の支払い
	def RewardContract(self, ePlayer, iCorrect, sText):
		pPlayer = gc.getPlayer(ePlayer)
		iKill =	pPlayer.getGuildPlusCounter(53)
		iReward = pPlayer.getGuildPlusCounter(54)
		iRequire = pPlayer.getGuildPlusCounter(55)
		iGold = iReward * iKill / iRequire * iCorrect / 2
		pPlayer.changeGold(iGold)
		self.addPlayerPopup(CyTranslator().getText(sText,(iGold,)), ePlayer)

#Tiger End

#Trait Fool
	def doTraitFool(self, iPlayer):
		pPlayer = gc.getPlayer(iPlayer)
		for eTrait in xrange(gc.getNumTraitInfos()):
			if pPlayer.hasTrait(eTrait):
				if (gc.getTraitInfo(eTrait).isSelectable()):
					pPlayer.setHasTraitWithSource(eTrait, False, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
		leTrait = [eTrait for eTrait in xrange(gc.getNumTraitInfos()) if gc.getTraitInfo(eTrait).isSelectable()]
		liChosenTrait = []
		for iLoop in xrange(2):
			liChosenTrait.append(leTrait.pop( CyGame().getSorenRandNum(len(leTrait), "Fool") ))
#		liChosenTrait.append(leTrait.pop( CyGame().getSorenRandNum(len(leTrait), "Fool") ))
		liChosenTrait.sort()
		for iChosenTrait in liChosenTrait:
			pPlayer.setHasTraitWithSource(iChosenTrait, True, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
		pPlayer.setHasTraitWithSource(iChosenTrait, True, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)

		if pPlayer.isHuman() and (gc.getGame().getElapsedGameTurns() > 0):
			popupInfo = CyPopupInfo()
			popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
			popupInfo.setText(CyTranslator().getText('TXT_KEY_EVENTTRIGGER_TRAIT_UNENLIGHTENED',()))
			popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_EVENT_TRAIT_UNENLIGHTENED",()), gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getButton())
			popupInfo.addPopup(iPlayer)

#Globalcounter initialization
	def doGlobalcounterInitialization(self, ePlayer):
		pPlayer = gc.getPlayer(ePlayer)

		## Sidar - Management of the number of uses of Wane.
		if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SIDAR'):
			pPlayer.setGuildPlusCounter(50, 6)

		## Scions - The probability of the awaken is born.
		elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SCIONS'):
			pPlayer.setGuildPlusCounter(50, 0)
			pPlayer.setGuildPlusCounter(51, 9)
			pPlayer.setGuildPlusCounter(52, 0)

		## Tiger - Guildplus Contract War
		elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_TIGER'):
			pPlayer.setGuildPlusCounter(50, 0)
			pPlayer.setGuildPlusCounter(53, 0)
			pPlayer.setGuildPlusCounter(54, 0)
			pPlayer.setGuildPlusCounter(55, 0)
			pPlayer.setGuildPlusCounter(59, 0)

		## Xoth
		elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_XOTH'):
			## Sanity Point - Initial value.
			pPlayer.setGuildPlusCounter(50, 60)
			## Sanity Point - Threshold of decreasing value.
			pPlayer.setGuildPlusCounter(51, cyFlatValue(10, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False))
			## Limit of the city emerged.
			iCanEmerge = 6
			if CyMap().getWorldSize() == gc.getInfoTypeForString('WORLDSIZE_DUEL'):
				iCanEmerge = 2
			elif CyMap().getWorldSize() == gc.getInfoTypeForString('WORLDSIZE_TINY'):
				iCanEmerge = 3
			elif CyMap().getWorldSize() == gc.getInfoTypeForString('WORLDSIZE_SMALL'):
				iCanEmerge = 5
			elif CyMap().getWorldSize() == gc.getInfoTypeForString('WORLDSIZE_LARGE'):
				iCanEmerge = 7
			elif CyMap().getWorldSize() == gc.getInfoTypeForString('WORLDSIZE_HUGE'):
				iCanEmerge = 9
			pPlayer.setGuildPlusCounter(52, iCanEmerge)

		## Megisus - The threshold at which the figure is complete.
		elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MEGISUS'):
			pPlayer.setGuildPlusCounter(50, 0)

		## Another
		if not pPlayer.isBarbarian():
			## Random Event - Apply Gela
			pPlayer.setGuildPlusCounter(1, 0)
			## Victory Conditions Switch
			pPlayer.setGuildPlusCounter(2, 0)
			## Trait Speech - Threshold for changing the diplomatic attitude.
			if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_SPEECH')):
				pPlayer.setGuildPlusCounter(3, 1)
			else:
				pPlayer.setGuildPlusCounter(3, 0)
			## Trait CrazyByWorldheritage - Heritage insanity is unscrupulous.
			if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_CRAZY_BY_WORLDHERITAGE')):
				# Use Counter from 5 to 5 + MAX_CIV_TEAMS(43) - 1
				CRAZY_OFFSET = 5
				for i in xrange(gc.getMAX_CIV_TEAMS()):
					pPlayer.setGuildPlusCounter(CRAZY_OFFSET + i, 0)

#Raise Heroes Spell - Request
	def doRaiseRequest(self, pCity, iRank):
		liThresholdPopuration = [3, 5, 8, 12]
		if pCity.isCapital():
			liThresholdPopuration = [7, 9, 12, 16]
		elif pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_PLANAR_GATE')):
			liThresholdPopuration = [3, 3, 5, 8]

		return liThresholdPopuration[iRank - 1]

#Raise Heroes Spell - Result
	def doRaiseResult(self, pCity, iRank, pPlot):
		liIncreaseBadhealth = [3, 7, 10, 15]
		liDecreasePopuration = [-3, -7, -10, -15]
		if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_DEMONS_ALTAR')):
			liDecreasePopuration = [-3, -3, -7, -10]
			liIncreaseBadhealth = [3, 3, 7, 10]
		iPopulation = pCity.getPopulation() + liDecreasePopuration[iRank - 1]
		iRadius = pCity.getPlotRadius() - 1
		if iPopulation > 0:
			pCity.changePopulation(liDecreasePopuration[iRank - 1])
			pCity.changeEspionageHealthCounter(liIncreaseBadhealth[iRank - 1])
		else:
			pCity.kill()

		if not gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_PLOT_COUNTER):
			lpRangedPlots = cyGetRangedPlots(pPlot, iRadius, False, False, TeamTypes.NO_TEAM)
			for pTargetPlot in lpRangedPlots:
				iFeature = pTargetPlot.getFeatureType()
				iBonus = pTargetPlot.getBonusType(TeamTypes.NO_TEAM)
				pTargetPlot.setPlotCounter(100)
				if iBonus != BonusTypes.NO_BONUS:
					if gc.getImprovementInfo(en.eImprovementFarm).isImprovementBonusTrade(iBonus):
						pTargetPlot.setImprovementType(en.eImprovementSnakePillar)
				if iFeature == en.eFeatureFloodPlains:
					pTargetPlot.setFeatureType(en.eFeatureObsidianPlains, 0)

#Dungeon Explorer - Remove Epic Lair
	def doRemoveEpicLair(self, pPlot):
		iLair = pPlot.getImprovementType()
		iReplace = -1
		if iLair == gc.getInfoTypeForString("IMPROVEMENT_AIFON_ISLE"):
			iReplace = gc.getInfoTypeForString("IMPROVEMENT_AIFON_ISLE_EXPLORED")
		if iLair == gc.getInfoTypeForString("IMPROVEMENT_BRADELINES_WELL"):
			iReplace = gc.getInfoTypeForString("IMPROVEMENT_BRADELINES_WELL_EXPLORED")
		if iLair == gc.getInfoTypeForString("IMPROVEMENT_BROKEN_SEPULCHER"):
			iReplace = gc.getInfoTypeForString("IMPROVEMENT_BROKEN_SEPULCHER_EXPLORED")
		if iLair == gc.getInfoTypeForString("IMPROVEMENT_PYRE_OF_THE_SERAPHIC"):
			iReplace = gc.getInfoTypeForString("IMPROVEMENT_PYRE_OF_THE_SERAPHIC_EXPLORED")
		if iLair == gc.getInfoTypeForString("IMPROVEMENT_EYE_OF_HASTUR"):
			iReplace = gc.getInfoTypeForString("IMPROVEMENT_EYE_OF_HASTUR_EXPLORED")
		pPlot.setImprovementType(iReplace)

# ent >>>
	def findAdjacentClearPlot(self, iPlayer, iX, iY, bWater, bAllowStay):
		pPlot = CyMap().plot(iX, iY)
		if bAllowStay:
			if iPlayer == PlayerTypes.NO_PLAYER:
				if pPlot.getNumUnits() == 0:
					return pPlot
			else:
				if not pPlot.isVisibleEnemyUnit(iPlayer):
					return pPlot

		iBestValue = -1
		pBestPlot = None
		for iDirection in xrange(DirectionTypes.NUM_DIRECTION_TYPES):
			pAdjacentPlot = plotDirection(iX, iY, DirectionTypes(iDirection))
			if pAdjacentPlot.isNone():
				continue
			if iPlayer == PlayerTypes.NO_PLAYER:
				if pAdjacentPlot.getNumUnits() > 0:
					continue
			else:
				if pAdjacentPlot.isVisibleEnemyUnit(iPlayer):
					continue
			if pAdjacentPlot.isImpassable():
				continue
			if pAdjacentPlot.isCity():
				continue
			if (bWater != pAdjacentPlot.isWater()):
				continue
			iValue = CyGame().getSorenRandNum(1000, "FindAdjacentClearPlot")
			if iBestValue < iValue:
				pBestPlot = pAdjacentPlot
				iBestValue = iValue
		return pBestPlot

	def AI_getWarSuccessCapitulationRatio(self, ePlayer):
		pPlayer = gc.getPlayer(ePlayer)
		eTeam = pPlayer.getTeam()
		pTeam = gc.getTeam(eTeam)

		iSumWarSuccess = 0
		for eLoopTeam in xrange(gc.getMAX_CIV_TEAMS()):
			if pTeam.isAtWar(eLoopTeam):
				pLoopTeam = gc.getTeam(eLoopTeam)
				iSumWarSuccess += pTeam.AI_getWarSuccess(eLoopTeam)
				iSumWarSuccess -= pLoopTeam.AI_getWarSuccess(eTeam)
		iDivisor = max(25, min(pPlayer.getNumCities(), 4) * 10)
		return iSumWarSuccess * 100 // iDivisor

	def doMovePlotAndCastSpell(self, pUnit, pPlot, eSpell):
	# 指定ユニットの特定タイルへの移動と呪文詠唱の実行プログラム
	# スペルを実行可能な UnitAI を UNITAI_CITY_SPECIAL に限定 (at CvSpellInterface.py) して PythonSpecificAI で操作するためのもの
		iX = pPlot.getX()
		iY = pPlot.getY()
		if pUnit.canMoveInto(pPlot, False, False, False):
			pUnit.getGroup().pushMoveToMission(iX, iY)
		if pUnit.at(iX, iY):
			pUnit.setUnitAIType(UnitAITypes.UNITAI_CITY_SPECIAL)
			if pUnit.canCast(eSpell, False):
				pUnit.cast(eSpell)
				pUnit.setUnitAIType(gc.getUnitInfo(pUnit.getUnitType()).getDefaultUnitAIType())
				return True
			pUnit.setUnitAIType(gc.getUnitInfo(pUnit.getUnitType()).getDefaultUnitAIType())
		return False

	def AI_hasRoomForFound(self, ePlayer):
		pPlayer = gc.getPlayer(ePlayer)
		iTurn = gc.getGame().getElapsedGameTurns()
		if iTurn < 20:
			return True

		iNumCities = pPlayer.getNumCities()
		iTargetCities = pPlayer.getMaxCities()
		if iTargetCities == -1:
			iTargetCities = gc.getWorldInfo(CyMap().getWorldSize()).getTargetNumCities()
		if iNumCities > iTargetCities:
			iThreshold = 2000 * iNumCities // iTargetCities
		elif iNumCities > iTargetCities * 2 // 3:
			iThreshold = 1500
		else:
			iThreshold = 800
		iThreshold += iTurn * 5
		pTeam = gc.getTeam(pPlayer.getTeam())
		if pTeam.getWarPlanCount(WarPlanTypes.WARPLAN_TOTAL, True) > 0:
			iThreshold *= 3
		elif pTeam.getAnyWarPlanCount(True) > 0:
			iThreshold *= 2
		iBestFoundValue = pPlayer.findBestFoundValue()
		if iBestFoundValue > iThreshold:
			return True
		elif iBestFoundValue > iThreshold // 2:
			for pUnit in PyPlayer(ePlayer).getUnitList():
				if pUnit.getUnitType() == en.eUnitSettler:
					return True
			for pyCity in PyPlayer(ePlayer).getCityList():
				pCity = pyCity.GetCy()
				if pCity.getProductionUnit() == en.eUnitSettler:
					return True

		if pPlayer.getCivilizationType() == en.eCivilizationXoth:
			if pPlayer.getGuildPlusCounter(52) > 0:
				liCanFoundCityNum = [3, 5, 7, 10, 13, 16]
				iCanFoundCityNum = liCanFoundCityNum[CyMap().getWorldSize()]
				if iNumCities <= iCanFoundCityNum:
					return True

		return False

	def initFreeHeros(self, ePlayer, pPlot):
		if ePlayer == PlayerTypes.NO_PLAYER:
			return False
		pPlayer = gc.getPlayer(ePlayer)
		if not pPlayer.isAlive():
			return False
		eCiv = pPlayer.getCivilizationType()
		pTeam = gc.getTeam(pPlayer.getTeam())

		if pPlot.isNone():
			pCapital = pPlayer.getCapitalCity()
			if not pCapital.isNone():
				pPlot = pCapital.plot()
			elif pPlayer.getNumCities() > 0:
				for pyCity in PyPlayer(ePlayer).getCityList():
					pCity = pyCity.GetCy()
					if not pCity.isNone():
						pPlot = pCity.plot()
						break
			elif pPlayer.getNumUnits() > 0:
				for pUnit in PyPlayer(ePlayer).getUnitList():
					pPlot = pUnit.plot()
					break
			else:
				return False

		leHeros = []
		if eCiv == en.eCivilizationDoviello:
			leHeros += [gc.getInfoTypeForString('UNIT_LUCIAN')]
		elif eCiv == en.eCivilizationNiraikanai:
			leHeros += [gc.getInfoTypeForString('UNIT_BRAGGART')]
		elif eCiv == en.eCivilizationYs:
			leHeros += [gc.getInfoTypeForString('UNIT_YUNICA')]
		elif eCiv == en.eCivilizationAltair:
			if pTeam.isHasTech(gc.getInfoTypeForString('TECH_DIVINE_ESSENCE')):
				leHeros += [gc.getInfoTypeForString('UNIT_METATORON4')]
			elif pTeam.isHasTech(gc.getInfoTypeForString('TECH_IRON_WORKING')):
				leHeros += [gc.getInfoTypeForString('UNIT_METATORON3')]
			elif pTeam.isHasTech(gc.getInfoTypeForString('TECH_BRONZE_WORKING')):
				leHeros += [gc.getInfoTypeForString('UNIT_METATORON2')]
			else:
				leHeros += [gc.getInfoTypeForString('UNIT_METATORON1')]
		elif eCiv == en.eCivilizationScions:
			eHero = gc.getInfoTypeForString('UNIT_KORRINA')
			pNewUnit = pPlayer.initUnit(eHero, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			if pTeam.isHasTech(gc.getInfoTypeForString('TECH_BRONZE_WORKING')) or pTeam.isHasTech(gc.getInfoTypeForString('TECH_TRACKING')):
				pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HELD'), False)

			if pTeam.isHasTech(gc.getInfoTypeForString('TECH_CURRENCY')):
				leHeros += [gc.getInfoTypeForString('UNIT_PELEMOC')]
			if pTeam.isHasTech(gc.getInfoTypeForString('TECH_CODE_OF_LAWS')):
				leHeros += [gc.getInfoTypeForString('UNIT_MELANTE')]
			if pTeam.isHasTech(gc.getInfoTypeForString('TECH_KNOWLEDGE_OF_THE_ETHER')):
				leHeros += [gc.getInfoTypeForString('UNIT_ALCINUS')]
			if pTeam.isHasTech(gc.getInfoTypeForString('TECH_TRACKING')):
				leHeros += [gc.getInfoTypeForString('UNIT_THEMOCH')]
		elif eCiv == en.eCivilizationMercurians:
			leHeros += [gc.getInfoTypeForString('UNIT_BASIUM')]
		elif eCiv == en.eCivilizationInfernal:
			leHeros += [gc.getInfoTypeForString('UNIT_HYBOREM')]
		elif eCiv == en.eCivilizationXoth:
			leHeros += [gc.getInfoTypeForString('UNIT_MYNOGHRA')]

		if len(leHeros) > 0:
			for eHero in leHeros:
				eHeroClass = gc.getUnitInfo(eHero).getUnitClassType()
				if not CyGame().isUnitClassMaxedOut(eHeroClass, 0):
					pNewUnit = pPlayer.initUnit(eHero, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

		return True

# ent <<<
#Game Progress Percent - Substitute Module
	"""
	def doGameProgressPercent(self, iPlayer):
		liTechs = [	iTech	for iTech in xrange(gc.getNumTechInfos())
							if not gc.getTechInfo(iTech).isDisable()
							and gc.getTechInfo(iTech).getResearchCost() >= 0	]
		pTeam = gc.getTeam(gc.getPlayer(iPlayer).getTeam())
		iNumAcquiredTechs = 0
		iNumTotalTechs = len(liTechs)
		for iTech in liTechs:
			if pTeam.isHasTech(iTech):
				iNumAcquiredTechs += 1

		return (iNumAcquiredTechs * 100) // iNumTotalTechs
	"""

# Kaijin <<<

#anonymous 2/20/2010
#各種生産警告 + ターン数表示あり
	def doAlert(self, iPlayer):
		pPlayer = gc.getPlayer(iPlayer)
#アケロン
#		for pyCity in PyPlayer(gc.getBARBARIAN_PLAYER()).getCityList():
#			pLoopCity = pyCity.GetCy()
#			if pLoopCity.getProductionUnit() == gc.getInfoTypeForString('UNIT_ACHERON'):
#				for i in xrange(20):
#					if (1 < i < 12):
#						if pLoopCity.getProductionTurnsLeft() == i:
#							CyInterface().addMessage(iPlayer,True,25,CyTranslator().getText("TXT_KEY_MESSAGE_START_PRODUCTION_ACHERON", (pLoopCity.getName(), i-1)),'',1,'',ColorTypes(11),pLoopCity.getX(),pLoopCity.getY(),True,True)
#
#
#AI勝利条件達成警告
		for iPlayer2 in xrange(gc.getMAX_PLAYERS()):
			pPlayer2 = gc.getPlayer(iPlayer2)
			if pPlayer2.isAlive() and pPlayer != pPlayer2:
				for pyCity in PyPlayer(iPlayer2).getCityList():
					pLoopCity = pyCity.GetCy()
					if pLoopCity.getOwner() != iPlayer:
						iTurnsLeft = pLoopCity.getProductionTurnsLeft()
						if 1 < iTurnsLeft < 12 or iTurnsLeft in (21, 31, 41):
							if pLoopCity.getProductionBuilding() == gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_FINAL'):
								szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_START_PRODUCTION_LUONNOTAR", (pLoopCity.getName(), ))
								szButton = gc.getBuildingInfo(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_FINAL')).getButton()
								CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pLoopCity.getX(), pLoopCity.getY(), True, True)

							if pLoopCity.getProductionBuilding() == gc.getInfoTypeForString('BUILDING_TOWER_OF_MASTERY'):
								szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_START_PRODUCTION_TOWER", (pLoopCity.getName(), ))
								szButton = gc.getBuildingInfo(gc.getInfoTypeForString('BUILDING_TOWER_OF_MASTERY')).getButton()
								CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pLoopCity.getX(), pLoopCity.getY(), True, True)

							if pLoopCity.getProductionProject() == gc.getInfoTypeForString('PROJECT_LED_TO_THE_END'):
								szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_START_PRODUCTION_LED_TO_THE_END", (pLoopCity.getName(), ))
								szButton = gc.getProjectInfo(gc.getInfoTypeForString('PROJECT_LED_TO_THE_END')).getButton()
								CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pLoopCity.getX(), pLoopCity.getY(), True, True)

							if pLoopCity.getProductionProject() == gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_CORE'):
								szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_START_PRODUCTION_STATUE_OF_LUXURY_CORE", (pLoopCity.getName(), ))
								szButton = gc.getProjectInfo(gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_CORE')).getButton()
								CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pLoopCity.getX(), pLoopCity.getY(), True, True)

# Kaijin >>>	patch29 expansion - Start -
	## ボンブールの銘板により資源を発見する
	def doTabletsOfBambur(self, iPlayer):
		pPlayer = gc.getPlayer(iPlayer)

		leBonusTypes = [		gc.getInfoTypeForString('BONUS_COPPER'),
								gc.getInfoTypeForString('BONUS_GEMS'),
								gc.getInfoTypeForString('BONUS_AMBER')		]

		liWatersideBonuses = [	gc.getInfoTypeForString('BONUS_COW'),
								gc.getInfoTypeForString('BONUS_PIG'),
								gc.getInfoTypeForString('BONUS_SHEEP'),
								gc.getInfoTypeForString('BONUS_WINE'),
								gc.getInfoTypeForString('BONUS_SALT')		]

		"""
		iBonusChance = 40
		iBonusChance += pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_MANA_EARTH')) * 20
		iGameSpeed = gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getGoldenAgePercent()
		iThreshold = 100
		iMod = (iThreshold * iGameSpeed) // 10
		if CyGame().getSorenRandNum(iMod, "Bonus PopUp Chance") < iBonusChance:
		"""

		iBaseDiscoverOdds = 100
		lePotentialBonuses = []
		for eBonus in xrange(gc.getNumBonusInfos()):
			eTechReveal = gc.getBonusInfo(eBonus).getTechReveal()
			if eTechReveal == TechTypes.NO_TECH or pPlayer.isHasTech(eTechReveal):
				lePotentialBonuses.append(eBonus)
		iRnd = CyGame().getSorenRandNum(25000, 'Bonus PopUp Chance')
		if iRnd < iBaseDiscoverOdds * len(lePotentialBonuses):
			pBestPlot = -1
			iBestPlot = -1

			for iPlotIndex in range (CyMap().numPlots()):
				pPlot = CyMap().plotByIndex(iPlotIndex)
				iPlot = -1
				if pPlot.isOwned():
					if pPlot.getOwner() == iPlayer:
						if not pPlot.isWater():
							if pPlot.getBonusType(TeamTypes.NO_TEAM) == BonusTypes.NO_BONUS:
								if pPlot.isFreshWater():
									iPlot += CyGame().getSorenRandNum(500, "Place Bonus")
								if pPlot.isHills():
									iPlot += CyGame().getSorenRandNum(500, "Place Bonus")
				if iPlot > iBestPlot:
					iBestPlot = iPlot
					pBestPlot = pPlot

			if pBestPlot != -1:
				if pBestPlot.isFreshWater():
					leBonusTypes += liWatersideBonuses
				leBonusTypes.sort()

				eNewBonus = -1
				eNewBonus = leBonusTypes[CyGame().getSorenRandNum(len(leBonusTypes), "Bonuses Select")]

				if eNewBonus != -1:
					pBestPlot.setBonusType(eNewBonus)
					szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_BUILDING_FOREST_ECLIPSE', ())
					szButton = gc.getBonusInfo(eNewBonus).getButton()
					CyInterface().addMessage(iPlayer, False, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS3D_SPELL_INSPIRATION', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pBestPlot.getX(), pBestPlot.getY(), True, True)

					if pBestPlot.isVisibleToWatchingHuman():
						CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_CREATION'), pBestPlot.getPoint())
# Kaijin <<<	patch29 expansion - End -