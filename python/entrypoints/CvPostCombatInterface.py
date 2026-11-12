## Sid Meier's Civilization 4
## Copyright 2011 Denev's Advanced Rules modmod
from CvPythonExtensions import *
import CvPythonEnums

gc = CyGlobalContext()
en = CvPythonEnums.CvPythonEnums()

def postCombatBeastOfAgares(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.getUnitClassType() == gc.getInfoTypeForString("UNITCLASS_PALADIN"):
		pCaster.setDamage(0, PlayerTypes.NO_PLAYER)
##--------		Single Afterlife: Added by Denev	--------##
		pOpponent.setAfterlife(AfterlifeTypes.AFTERLIFE_PREYED)
##--------		Single Afterlife: End Add			--------##
##--------		Single Afterlife: Modified by Denev	--------##
#		CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_CONSUME_PALADIN", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Units/Beast of Agares.dds',ColorTypes(8), pCaster.getX(), pCaster.getY(), True, True)
		szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_CONSUME_FRESH_MEAT", (pCaster.getNameKey(), pOpponent.getNameKey()))
		szButton = gc.getPromotionInfo(gc.getInfoTypeForString('PROMOTION_CANNIBALIZE')).getButton()
		CyGame().pushGameMessage(pCaster.getOwner(), True, szMessage, '', szButton, en.eColorGreen, pCaster.getX(), pCaster.getY(), True, True)
##--------		Single Afterlife: End Modify		--------##

def postCombatDonal(argsList):
	pCaster, pOpponent = argsList
	liOldFoeRace = [	gc.getInfoTypeForString('PROMOTION_DEMON'),
						gc.getInfoTypeForString('PROMOTION_UNDEAD')	]
	if pOpponent.getRace() in liOldFoeRace:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_RECRUITER'), True)

def postCombatHeal50(argsList):
	pCaster, pOpponent = argsList
	if pCaster.getDamage() > 0:
		pCaster.setDamage(pCaster.getDamage() // 2, PlayerTypes.NO_PLAYER)

def postCombatIra(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isAlive():
##--------	Fractional Combat Strength: Modified by Denev	--------##
		"""
		if pCaster.baseCombatStr() < 32:
##--------		Unofficial Bug Fix: Modified by Denev	--------##
			'''
			pCaster.setBaseCombatStr(pCaster.baseCombatStr() - 3)
			pCaster.setBaseCombatStrDefense(pCaster.baseCombatStrDefense() - 3)
			'''
			pCaster.setBaseCombatStr(pCaster.baseCombatStr() - pCaster.getTotalDamageTypeCombat() + 1)
			pCaster.setBaseCombatStrDefense(pCaster.baseCombatStrDefense() - pCaster.getTotalDamageTypeCombat() + 1)
##--------		Unofficial Bug Fix: End Modify			--------##
		"""
		if pCaster.getCombatAttackTimes100() < 3200:
			pCaster.changeCombatStr(1)
##--------	Fractional Combat Strength: End Modify		--------##

def postCombatMimic(argsList):
	pCaster, pOpponent = argsList
	"""
	iBronze = gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS')
	iChanneling3 = gc.getInfoTypeForString('PROMOTION_CHANNELING3')
	iDivine = gc.getInfoTypeForString('PROMOTION_DIVINE')
	iGreatCommander = gc.getInfoTypeForString('PROMOTION_GREAT_COMMANDER')
	iIron = gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS')
	iMithril = gc.getInfoTypeForString('PROMOTION_MITHRIL_WEAPONS')
	listProms = []
	iCount = 0
	for iProm in xrange(gc.getNumPromotionInfos()):
		if pCaster.isHasPromotion(iProm):
			iCount += 1
		else:
			if (pOpponent.isHasPromotion(iProm)):
				if not gc.getPromotionInfo(iProm).isEquipment():
					if (iProm != iChanneling3 and iProm != iDivine and iProm != iBronze and iProm != iIron and iProm != iMithril and iProm != iGreatCommander):
						if not gc.getPromotionInfo(iProm).isRace():
							listProms.append(iProm)
	"""
	listProms = []
	iCount = 0
	for iProm in xrange(gc.getNumPromotionInfos()):
		if pCaster.isHasPromotion(iProm):
			iCount += 1
		else:
			if (pOpponent.isHasPromotion(iProm)):
				if not gc.getPromotionInfo(iProm).isEquipment():
					if not gc.getPromotionInfo(iProm).isRace():
						if gc.getPromotionInfo(iProm).getMinLevel() >= 0:
							listProms.append(iProm)
	if len(listProms) > 0:
		iCount += 1
		iRnd = CyGame().getSorenRandNum(len(listProms), "Mimic")
		pCaster.setHasPromotion(listProms[iRnd], True)
##--------		Single Afterlife: Modified by Denev	--------##
#		CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_PROMOTION_STOLEN", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getPromotionInfo(listProms[iRnd]).getButton(),ColorTypes(8), pCaster.getX(), pCaster.getY(), True, True)
		szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_PROMOTION_STOLEN', (pCaster.getNameKey(), pOpponent.getNameKey(), gc.getPromotionInfo(listProms[iRnd]).getDescription()))
		szButton = gc.getPromotionInfo(listProms[iRnd]).getButton()
		CyGame().pushGameMessage(pCaster.getOwner(), True, szMessage, '', szButton, en.eColorGreen, pCaster.getX(), pCaster.getY(), True, True)
##--------		Single Afterlife: End Modify		--------##
	if iCount >= 20:
		if pCaster.isHuman():
			szTorophyKey = 'TROPHY_FEAT_MIMIC_20'
			if not CyGame().isHasTrophy(szTorophyKey):
				CyGame().changeTrophyValue(szTorophyKey, 1)

##--------		Single Afterlife: Added by Denev	--------##
def postCombatRavenousWerewolf(argsList):
	pCaster, pOpponent = argsList
##--------		Single Afterlife: Modified by ent	--------##
##	if pOpponent.isEdible():
	if pOpponent.isEdible() and pOpponent.getDamage() == 100 and not pOpponent.getAfterlife() in (AfterlifeTypes.AFTERLIFE_CAPTURED, AfterlifeTypes.AFTERLIFE_ENSLAVED):
##--------		Single Afterlife: End Modify		--------##
		if pCaster.getDamage() > 0:
			pCaster.setDamage(pCaster.getDamage() // 2, PlayerTypes.NO_PLAYER)
##>>>>Advanced Rules: Modified by ent 2019/05/10
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENRAGED'), False)
#	else:
#		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENRAGED'), True)
##<<<<Advanced Rules: End Modify
##--------		Single Afterlife: End Add			--------##

def postCombatAcheron(argsList):
	pCaster, pOpponent = argsList
	pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STONESKIN'), True)
	if pOpponent.isHuman():
		szTorophyKey = 'TROPHY_DEFEATED_ACHERON'
		if not CyGame().isHasTrophy(szTorophyKey):
			CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatArs(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isHuman():
		szTorophyKey = 'TROPHY_DEFEATED_ARS'
		if not CyGame().isHasTrophy(szTorophyKey):
			CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatAuricAscendedLost(argsList):
	pCaster, pOpponent = argsList
#Unoji Revise >>>
	if pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ILLUSION')):
		return
#Unoji Revise<<<
	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
##--------		Unofficial Bug Fix: Deleted by Denev	--------##
	"Duplicated Auric doesn't cause losing traits. This process is moved to DLL."
	"""
	for iTrait in xrange(gc.getNumTraitInfos()):
		if pPlayer.hasTrait(iTrait):
			pPlayer.setHasTrait(iTrait, False)
	"""
##--------		Unofficial Bug Fix: End Delete			--------##

# ent >>>
	for eLoopPlayer in xrange(gc.getMAX_PLAYERS()):
		pLoopPlayer = gc.getPlayer(eLoopPlayer)
		if pLoopPlayer.isAlive():
			if pLoopPlayer.getDisableProduction() > 0:
				pLoopPlayer.changeDisableProduction(-1 * pLoopPlayer.getDisableProduction())
			if pLoopPlayer.getDisableResearch() > 0:
				pLoopPlayer.changeDisableResearch(-1 * pLoopPlayer.getDisableResearch())
# ent <<<

	if pOpponent.isHasPromotion(gc.getInfoTypeForString('PROMOTION_GODSLAYER')):
		if pOpponent.isHuman():
			szTorophyKey = 'TROPHY_FEAT_GODSLAYER'
			if not CyGame().isHasTrophy(szTorophyKey):
				CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatAuricAscendedWon(argsList):
	pCaster, pOpponent = argsList
#Unoji Revise >>>
	if pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ILLUSION')):
		return
#Unoji Revise<<<
	if pOpponent.isHasPromotion(gc.getInfoTypeForString('PROMOTION_GODSLAYER')):
		iPlayer = pCaster.getOwner()
		pPlayer = gc.getPlayer(iPlayer)
##--------		Unofficial Bug Fix: Deleted by Denev	--------##
		"Duplicated Auric doesn't cause losing traits. This process is moved to DLL."
		"""
		for iTrait in xrange(gc.getNumTraitInfos()):
			if pPlayer.hasTrait(iTrait):
				pPlayer.setHasTrait(iTrait, False)
		"""
##--------		Unofficial Bug Fix: End Delete			--------##
		pCaster.kill(True, pOpponent.getOwner())
		if pOpponent.isHuman():
			szTorophyKey = 'TROPHY_FEAT_GODSLAYER'
			if not CyGame().isHasTrophy(szTorophyKey):
				CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatBasium(argsList):
	pCaster, pOpponent = argsList
#Unoji Revise >>>
	if pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ILLUSION')):
		return
#Unoji Revise<<<
	if not pCaster.isImmortal():
		iPlayer = pCaster.getOwner()
		pPlayer = gc.getPlayer(iPlayer)
##--------		Unofficial Bug Fix: Deleted by Denev	--------##
		"Duplicated Basium doesn't cause losing traits. This process is moved to DLL."
		"""
		for iTrait in xrange(gc.getNumTraitInfos()):
			if pPlayer.hasTrait(iTrait):
				pPlayer.setHasTrait(iTrait, False)
		"""
##--------		Unofficial Bug Fix: End Delete			--------##
		if pOpponent.isHuman():
			szTorophyKey = 'TROPHY_DEFEATED_BASIUM'
			if not CyGame().isHasTrophy(szTorophyKey):
				CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatBrigitHeld(argsList):
	pCaster, pOpponent = argsList
	pPlot = pCaster.plot()
	if pPlot.getImprovementType() == gc.getInfoTypeForString('IMPROVEMENT_RING_OF_CARCER'):
		pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
	if pOpponent.isHuman():
		szTorophyKey = 'TROPHY_FEAT_RESCUE_BRIGIT'
		if not CyGame().isHasTrophy(szTorophyKey):
			CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatBuboes(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isHuman():
		szTorophyKey = 'TROPHY_DEFEATED_BUBOES'
		if not CyGame().isHasTrophy(szTorophyKey):
			CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatHyborem(argsList):
	pCaster, pOpponent = argsList
#Unoji Revise >>>
	if pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ILLUSION')):
		return
#Unoji Revise<<<
	if not pCaster.isImmortal():
		iPlayer = pCaster.getOwner()
		pPlayer = gc.getPlayer(iPlayer)
##--------		Unofficial Bug Fix: Deleted by Denev	--------##
		"Duplicated Hyborem doesn't cause losing traits. This process is moved to DLL."
		"""
		for iTrait in xrange(gc.getNumTraitInfos()):
			if iTrait != gc.getInfoTypeForString('TRAIT_FALLOW'):
				if pPlayer.hasTrait(iTrait):
					pPlayer.setHasTrait(iTrait, False)
		"""
##--------		Unofficial Bug Fix: End Delete			--------##
		if pOpponent.isHuman():
			szTorophyKey = 'TROPHY_DEFEATED_HYBOREM'
			if not CyGame().isHasTrophy(szTorophyKey):
				CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatLeviathan(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isHuman():
		szTorophyKey = 'TROPHY_DEFEATED_LEVIATHAN'
		if not CyGame().isHasTrophy(szTorophyKey):
			CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatOrthus(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isHuman():
		szTorophyKey = 'TROPHY_DEFEATED_ORTHUS'
		if not CyGame().isHasTrophy(szTorophyKey):
			CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatStephanos(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isHuman():
		szTorophyKey = 'TROPHY_DEFEATED_STEPHANOS'
		if not CyGame().isHasTrophy(szTorophyKey):
			CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatTreant(argsList):
	pCaster, pOpponent = argsList
	pPlot = pCaster.plot()
##--------	Advanced Rules: Modified by Denev 2010/01/29
	"""
	if pPlot.getFeatureType() == -1:
		if pPlot.canHaveFeature(gc.getInfoTypeForString('FEATURE_FOREST_NEW')):
			pPlot.setFeatureType(gc.getInfoTypeForString('FEATURE_FOREST_NEW'), 0)
	"""
	iNewForest = gc.getInfoTypeForString('FEATURE_FOREST_NEW')
	if pPlot.canHaveFeatureOnImprovement(iNewForest):
		pPlot.setFeatureType(iNewForest, 0)
##--------	Advanced Rules: End Modify

def postCombatYersinia(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isHuman():
		szTorophyKey = 'TROPHY_DEFEATED_YERSINIA'
		if not CyGame().isHasTrophy(szTorophyKey):
			CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatReduceCombat1(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isAlive():
##--------		Unofficial Bug Fix: Modified by Denev	--------##
		"""
		if pCaster.baseCombatStr() > 5:
			pCaster.setBaseCombatStr(pCaster.baseCombatStr() - 5)
			pCaster.setBaseCombatStrDefense(pCaster.baseCombatStrDefense() - 5)
			CyInterface().addMessage(pCaster.getOwner(), True,25,CyTranslator().getText("TXT_KEY_MESSAGE_STRENGTH_REDUCED", ()),'',1,'Art/Interface/Buttons/Units/Repentant Angel.dds',ColorTypes(7),pCaster.getX(),pCaster.getY(), True, True)
		"""
##--------	Fractional Combat Strength: Modified by Denev	--------##
		'''
		if pCaster.baseCombatStr() > pCaster.getTotalDamageTypeCombat():
			pCaster.setBaseCombatStr(pCaster.baseCombatStr() - pCaster.getTotalDamageTypeCombat() - 1)
			pCaster.setBaseCombatStrDefense(pCaster.baseCombatStrDefense() - pCaster.getTotalDamageTypeCombat() - 1)
		'''
		if pCaster.getCombatAttackTimes100() > pCaster.getTotalDamageTypeCombatTimes100():
			pCaster.changeCombatStr(-1)
##--------	Fractional Combat Strength: End Modify		--------##
##--------		Single Afterlife: Modified by Denev	--------##
#			CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_STRENGTH_REDUCED", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pCaster.getButton(), en.eColorRed, pCaster.getX(), pCaster.getY(), True, True)
			szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_STRENGTH_REDUCED", (pCaster.getNameKey(), ))
			CyGame().pushGameMessage(pCaster.getOwner(), True, szMessage, '', '', en.eColorRed, pCaster.getX(), pCaster.getY(), False, False)
##--------		Single Afterlife: End Modify		--------##
##--------		Unofficial Bug Fix: End Modify			--------##

def postCombatReducePopulation(argsList):
	pCaster, pOpponent = argsList
	pPlot = pOpponent.plot()
	if pPlot.isCity():
		pCity = pPlot.getPlotCity()
		if pCity.getPopulation() > 1:
			pCity.changePopulation(-1)
##--------		Single Afterlife: Modified by Denev	--------##
#			CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_POPULATION_REDUCED", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Units/Angel of Death.dds',ColorTypes(7), pCity.getX(), pCity.getY(), True, True)
			szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_POPULATION_REDUCED", ())
			szButton = gc.getUnitInfo(gc.getInfoTypeForString('UNIT_ANGEL_OF_DEATH')).getButton()
			CyGame().pushGameMessage(pCity.getOwner(), True, szMessage, '', szButton, en.eColorRed, pCaster.getX(), pCaster.getY(), True, True)
##--------		Single Afterlife: End Modify		--------##

def postCombatLostSailorsDirge(argsList):
	pCaster, pOpponent = argsList
	iPlayer = pOpponent.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
###--------		宝箱はバグの素: Deleted by ent	--------##
	"""
	iEvent = gc.getInfoTypeForString('EVENTTRIGGER_SAILORS_DIRGE_DEFEATED')
##--------		Unofficial Bug Fix: Modified by Denev	--------##
#	triggerData = pPlayer.initTriggeredData(iEvent, True, -1, pCaster.getX(), pCaster.getY(), iPlayer, -1, -1, -1, -1, -1)
	pPlayer.triggerCustomEvent(iEvent, -1, pCaster.getX(), pCaster.getY(), PlayerTypes.NO_PLAYER, -1, ReligionTypes.NO_RELIGION, CorporationTypes.NO_CORPORATION, -1, BuildingTypes.NO_BUILDING)
##--------		Unofficial Bug Fix: End Modify			--------##
	"""
##--------		宝箱はバグの素: End Delete			--------##

"""
def postCombatSkeleton(argsList):
	pCaster, pOpponent = argsList
	if pCaster.isBarbarian():
		if pCaster.getLevel() > 2:
			pCaster.setReincarnateUnit(gc.getInfoTypeForString('UNIT_SPECTRE'))

def postCombatSpectre(argsList):
	pCaster, pOpponent = argsList
	if pCaster.isBarbarian():
		if pCaster.getLevel() > 4:
			pCaster.setReincarnateUnit(gc.getInfoTypeForString('UNIT_WRAITH'))
"""

def postCombatSplit(argsList):
	pCaster, pOpponent = argsList
# Kaijin >>>
	pPlayer = gc.getPlayer(pCaster.getOwner())
# Kaijin <<<
	if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAK')):
		customSummonSpellData = CvCustomSummonSpellData()
		customSummonSpellData.eUnit = pCaster.getUnitType()
		customSummonSpellData.iNumUnits = 2
		customSummonSpellData.iDuration = pCaster.getDuration()
# Kaijin >>>
		if pCaster.isSummoned():
			customSummonSpellData.iDuration = gc.getDefineINT('SUMMONING_DEFAULT_DURATION_TURNS') + pPlayer.getSummonDuration()
# Kaijin <<<
		customSummonSpellData.bAbility = True
		lpNewUnits = pCaster.castCustomSummon(customSummonSpellData)
		for pNewUnit in lpNewUnits:
			pNewUnit.setDamage(pNewUnit.maxHitPoints() // 4, PlayerTypes.NO_PLAYER)
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STRONG'), False)
			if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_STRONG')):
				pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAK'), True)
##--------		Single Afterlife: Modified by Denev	--------##
#		CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_SPLIT", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getUnitInfo(eUnit).getButton(),ColorTypes(7), pCaster.getX(), pCaster.getY(), True, True)
		szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_SPLIT", (pCaster.getNameKey(), ))
		CyGame().pushGameMessage(pOpponent.getOwner(), True, szMessage, '', '', en.eColorRed, pCaster.getX(), pCaster.getY(), False, False)
##--------		Single Afterlife: End Modify		--------##

def postCombatWolfRider(argsList):
	pCaster, pOpponent = argsList
##--------		Single Afterlife: Modified by Denev	--------##
	"""
	if (pOpponent.getUnitType() == gc.getInfoTypeForString('UNIT_WOLF') or pOpponent.getUnitType() == gc.getInfoTypeForString('UNIT_WOLF_PACK')):
		CyInterface().addMessage(pCaster.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_WOLF_RIDER", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Units/Wolf Rider.dds',ColorTypes(8), pCaster.getX(), pCaster.getY(), True, True)
		pPlayer = gc.getPlayer(pCaster.getOwner())
		newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_WOLF_RIDER'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		newUnit.convert(pCaster)
	"""
	liRidableUnits = [	gc.getInfoTypeForString('UNIT_WOLF'),
						gc.getInfoTypeForString('UNIT_WOLF_PACK')	]
	if pOpponent.getUnitType() in liRidableUnits:
# ent >>>
		"""
		pCaster.setReincarnateUnit(gc.getInfoTypeForString('UNIT_WOLF_RIDER'))
		pOpponent.setAfterlife(AfterlifeTypes.AFTERLIFE_MOUNTED)
		"""
		if gc.getPlayer(pCaster.getOwner()).isHasTech(gc.getInfoTypeForString('TECH_HORSEBACK_RIDING')):
			pCaster.setReincarnateUnit(gc.getInfoTypeForString('UNIT_WOLF_RIDER'))
			pOpponent.setAfterlife(AfterlifeTypes.AFTERLIFE_MOUNTED)
# ent <<<
##--------		Single Afterlife: End Modify			--------##


# Kaijin >>>

## Echigo
def postCombatSeisyou(argsList):
	pCaster, pOpponent = argsList
	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pCaster.getLevel() >= 10 and pPlayer.isHasTech(gc.getInfoTypeForString('TECH_IRON_WORKING')):
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_KENSHIN2'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit.convert(pCaster)

def postCombatGunshin(argsList):
	pCaster, pOpponent = argsList
	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pCaster.getLevel() >= 15 and pPlayer.isHasTech(gc.getInfoTypeForString('TECH_WARHORSES')):
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_KENSHIN3'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit.convert(pCaster)

def postCombatBisyamonten(argsList):
	pCaster, pOpponent = argsList
	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pCaster.getLevel() >= 30:
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_KENSHIN4'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit.convert(pCaster)

## Droaum
def postCombatDamienDroaum(argsList):
	pCaster, pOpponent = argsList
	if not pOpponent.isBarbarian():
		CyGame().changeGlobalCounter(2)
	if not pOpponent.isHasPromotion(gc.getInfoTypeForString('PROMOTION_HERO')):
		pOpponent.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MENTAL_DERANGEMENT_DROAUM'), True)

def postCombatMaenyaDroaum(argsList):
	pCaster, pOpponent = argsList
	pPlayer = gc.getPlayer(pCaster.getOwner())
	if pOpponent.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DRAGON')):
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DRAGON_SCALE_DROAUM'), True)
	if pOpponent.isHasPromotion(gc.getInfoTypeForString('PROMOTION_HERO')):
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HERO_SKULL_DROAUM'), True)

def postCombatApostleDroaum(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isAlive() and not gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_GLOBAL_COUNTER):
		if CyGame().getSorenRandNum(100, "Apostle") < 20:
			CyGame().changeGlobalCounter(1)
	else:
		if CyGame().getSorenRandNum(100, "Apostle") < 10:
			pCaster.setDamage(0, PlayerTypes.NO_PLAYER)
			pOpponent.setAfterlife(AfterlifeTypes.AFTERLIFE_PREYED)
			szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_CONSUME_FRESH_MEAT", (pCaster.getNameKey(), pOpponent.getNameKey()))
			szButton = gc.getPromotionInfo(gc.getInfoTypeForString('PROMOTION_CANNIBALIZE')).getButton()
			CyGame().pushGameMessage(pCaster.getOwner(), True, szMessage, '', szButton, en.eColorGreen, pCaster.getX(), pCaster.getY(), True, True)

## Dark
def postCombatTokoyami(argsList):
	pCaster, pOpponent = argsList
#Unoji Revise >>>
	if pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ILLUSION')):
		return
#Unoji Revise<<<
	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	for iTrait in xrange(gc.getNumTraitInfos()):
		if pPlayer.hasTrait(iTrait):
			pPlayer.setHasTrait(iTrait, False)

# Ffh2
## Religion
def postCombatCrusaderWon(argsList):
	pCaster, pOpponent = argsList
	if	(	(pOpponent.getReligion() != ReligionTypes.NO_RELIGION and gc.getReligionInfo(pOpponent.getReligion()).getAlignment() == gc.getInfoTypeForString('ALIGNMENT_EVIL'))
		or	pOpponent.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ENTROPY1'))
		or	pOpponent.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DEATH1'))		):
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BLESSED'), True)

def postCombatDrownLost(argsList):
	pCaster, pOpponent = argsList
	if  CyGame().getSorenRandNum(100, "Enrage") < 20:
		if pOpponent.isAlive():
			if pOpponent.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENRAGED'), True):
				szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_BRING_MADNESS", ())
				szButton = gc.getPromotionInfo(gc.getInfoTypeForString('PROMOTION_ENRAGED')).getButton()
				CyGame().pushGameMessage(pOpponent.getOwner(), True, szMessage, '', szButton, en.eColorRed, pOpponent.getX(), pOpponent.getY(), True, True)

def postCombatDiseasedCorpseWon(argsList):
	pCaster, pOpponent = argsList
	pPlot = pOpponent.plot()
	if pPlot.isOwned():
		ePlotOwner = pPlot.getOwner()
		pPlotOwner = gc.getPlayer(ePlotOwner)
		if pPlotOwner.isAlive():
			if ePlotOwner != pCaster.getOwner():
				pTeam = gc.getTeam(pCaster.getTeam())
				if pTeam.isAtWar(pPlot.getTeam()):
					if pPlot.isCity():
						pCity = pPlot.getPlotCity()
						pCity.changeEspionageHealthCounter(1)
						szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_BLIGHT", ())
						szButton = gc.getUnitInfo(gc.getInfoTypeForString('UNIT_DISEASED_CORPSE')).getButton()
						CyGame().pushGameMessage(pCity.getOwner(), True, szMessage, '', szButton, en.eColorRed, pCaster.getX(), pCaster.getY(), True, True)
					else:
						if not pPlot.isWater():
							if pPlot.getFeatureType() == FeatureTypes.NO_FEATURE:
								iRnd = CyGame().getSorenRandNum(100, "Haunted Lands")
								if	(	( iRnd < 25 and CyGame().getGlobalCounter() < 30 )
									or	( iRnd < 50 and CyGame().getGlobalCounter() >= 30 )
									or	CyGame().getGlobalCounter() >= 70				):
									pPlot.setFeatureType(en.eFeatureHauntedLands, 0)

## Barbarian
def postCombatAvatarOfWrathWon(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isAlive():
		if not pOpponent.isImmortal():
			CyGame().changeGlobalCounter(1)

## Magic Expansion Mod
def postCombatOrthusReturnWon(argsList):
	pCaster, pOpponent = argsList
	pPlayer = gc.getPlayer(pCaster.getOwner())
	lList= []

	if not pCaster.isBarbarian():

		#デュインの可能性
		iWerewolf = gc.getInfoTypeForString('PROMOTION_WEREWOLF')
		if not pCaster.isHasPromotion(iWerewolf):
			if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_FERAL_BOND')):
				if CyGame().getSorenRandNum(100, "OrthusR Duin") < 20:
					lList = lList + ['DUIN']
		else:
			#狼人間誕生チェック
			if CyGame().getSorenRandNum(100, "Werewolf") < 60:
				pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_RAVENOUS_WEREWOLF'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

		#ロシャの可能性
		iVampire = gc.getInfoTypeForString('PROMOTION_VAMPIRE')
		iImmortal= gc.getInfoTypeForString('PROMOTION_IMMORTAL')
		if not pCaster.isHasPromotion(iVampire):
			if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_FANATICISM')):
				if CyGame().getSorenRandNum(100, "OrthusR Losha") < 20:
					lList = lList + ['LOSHA']
		else:
			#不死身チェック
			if not pCaster.isHasPromotion(iImmortal) and pOpponent.isAlive():
				pCaster.setHasPromotion(iImmortal,True)

		#マグナダインの可能性
		iHorselord = gc.getInfoTypeForString('PROMOTION_HORSELORD')
		if not pCaster.isHasPromotion(iHorselord):
			if pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MOBILITY1')):
				if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_WARHORSES')):
					if CyGame().getSorenRandNum(100, "OrthusR Magnadine") < 20:
						lList = lList + ['MAGNADINE']

		#ガイブラシの可能性
		iGuybrush = gc.getInfoTypeForString('PROMOTION_BOARDING')
		if not pCaster.isHasPromotion(iGuybrush):
			if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_OPTICS')):
				if CyGame().getSorenRandNum(100, "OrthusR Guybrush") < 20:
					lList = lList + ['GUYBRUSH']

		#ドラゴンの可能性
		iDragon = gc.getInfoTypeForString('PROMOTION_SUBDUE_BEASTS')
		if not pCaster.isHasPromotion(iDragon):
			if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_ANIMAL_MASTERY')):
				if CyGame().getSorenRandNum(100, "OrthusR Magnadine") < 20:
					lList = lList + ['DRAGON']

		#ギルデンの可能性
		iGilden = gc.getInfoTypeForString('PROMOTION_DEXTEROUS')
		if not pCaster.isHasPromotion(iGilden):
			if pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DRILL4')):
				if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_ARCHERY')):
					if CyGame().getSorenRandNum(100, "OrthusR Gilden") < 20:
						lList = lList + ['GILDEN']

		#アルゼンデインの可能性
		iArthendain = gc.getInfoTypeForString('PROMOTION_MEDIC2')
		if not pCaster.isHasPromotion(iArthendain):
			if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_MEDICINE')):
				if CyGame().getSorenRandNum(100, "OrthusR Arthendain") < 20:
					lList = lList + ['ARTHENDAIN']

		#無名の英雄の可能性
		iNamelessHero = gc.getInfoTypeForString('PROMOTION_STRONG')
		if not pCaster.isHasPromotion(iNamelessHero):
			if CyGame().getSorenRandNum(100, "OrthusR NamelessHero") < 3:
					lList = lList + ['NAMELESS']

		if len(lList) > 0:
			sName = lList[CyGame().getSorenRandNum(len(lList),"Orthus gains promotion")-1]
			if sName == 'DUIN':
				#デュイン男爵の記憶
				pCaster.setHasPromotion(iWerewolf, True)
			elif sName == 'LOSHA':
				#ロシャの記憶
				pCaster.setHasPromotion(iVampire, True)
			elif sName == 'MAGNADINE':
				#マグナダインの記憶
				pCaster.setHasPromotion(iHorselord, True)
			elif sName == 'GUYBRUSH':
				#ガイブラシの記憶
				pCaster.setHasPromotion(iGuybrush, True)
			elif sName == 'DRAGON':
				#ドラゴンの記憶
				pCaster.setHasPromotion(iDragon, True)
				pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FIRE2'), True)
				pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FEAR'), True)
			elif sName == 'GILDEN':
				#ギルデンの記憶
				pCaster.setHasPromotion(iGilden, True)
				pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WOODSMAN2'), True)
			elif sName == 'ARTHENDAIN':
				#アルゼンデインの記憶
				pCaster.setHasPromotion(iArthendain, True)
				pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MEDIC1'), True)
				pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IMMUNE_DISEASE'), True)
			elif sName == 'NAMELESS':
				#無名の英雄の記憶
				pCaster.setHasPromotion(iNamelessHero, True)
				pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_VALOR'), True)

			sTextKey = "TXT_KEY_POPUP_ORTHUS_RETURN_"+sName
			sPopupText = CyTranslator().getText(sTextKey,())
			cf.addPopup(sPopupText, "Art/Interface/Popups/Orthus.dds")

## Despiel
def postCombatDespielTransmigration(argsList):
	pCaster, pOpponent = argsList
	pPlayer = gc.getPlayer(pCaster.getOwner())
	iUnit = pOpponent.getUnitType()
	iAnimal = gc.getInfoTypeForString('UNITCOMBAT_ANIMAL')
	iBeast = gc.getInfoTypeForString('UNITCOMBAT_BEAST')
	iSiege = gc.getInfoTypeForString('UNITCOMBAT_SIEGE')
	iNaval = gc.getInfoTypeForString('UNITCOMBAT_NAVAL')
	iBronze = gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS')
	iChanneling3 = gc.getInfoTypeForString('PROMOTION_CHANNELING3')
	iDivine = gc.getInfoTypeForString('PROMOTION_DIVINE')
	iGreatCommander = gc.getInfoTypeForString('PROMOTION_GREAT_COMMANDER')
	iIron = gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS')
	iMithril = gc.getInfoTypeForString('PROMOTION_MITHRIL_WEAPONS')
	iWild = gc.getInfoTypeForString('PROMOTION_WILDANIMAL')
	iCount = 0
	if pOpponent.isAlive() and pOpponent.getUnitCombatType() != iAnimal and pOpponent.getUnitCombatType() != iSiege and pOpponent.getUnitCombatType() != iNaval:
		if pOpponent.getUnitCombatType() != iBeast or iUnit == gc.getInfoTypeForString('UNIT_DUIN'):
			iTransmigration = CyGame().getSorenRandNum(100, "Transmigration")
			if iTransmigration < 20 :
				pNewUnit = pPlayer.initUnit(iUnit, pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
				pNewUnit.setLevel(pOpponent.getLevel())
				pNewUnit.changeExperience(pOpponent.getExperience(), -1, False, False, False)
				pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_KAIJIN_RACE'), True)
				pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WITHERED'), False)
				pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAK'), False)
				pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DISEASED'), False)
				pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUED'), False)
				pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PEST'), False)
				pNewUnit.setDamage(25, PlayerTypes.NO_PLAYER)
				CyInterface().addMessage(pCaster.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_DESPIEL_TRANSMIGRATION", ()),'',1,gc.getUnitInfo(iUnit).getButton(),ColorTypes(8),pCaster.getX(),pCaster.getY(),True,True)
				for iProm in xrange(gc.getNumPromotionInfos()):
					if pNewUnit.isHasPromotion(iProm):
						iCount += 1
					else:
						if (pOpponent.isHasPromotion(iProm)):
							if not gc.getPromotionInfo(iProm).isEquipment():
								if (iProm != iChanneling3 and iProm != iDivine and iProm != iBronze and iProm != iIron and iProm != iMithril and iProm != iGreatCommander and iProm != iWild):
									if not gc.getPromotionInfo(iProm).isRace():
										pNewUnit.setHasPromotion(iProm, True)
				pNewUnit.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_DESPIEL'))

			else:
				iNizarCuchumaquic = CyGame().getSorenRandNum(100, "NizarCuchumaquic")
				if pCaster.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_NIZAR') and iNizarCuchumaquic < 40:
					if pOpponent.isAlive():
						pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_CUCHUMAQUIC'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
						pNewUnit.setLevel(pOpponent.getLevel())
						pNewUnit.changeExperience(pOpponent.getExperience(), -1, False, False, False)

						# caster bare strength
						iWeaponExtraAttack = 0
						iWeaponExtraDefense = 0
						eWeapon = pOpponent.getWeapon()
						if eWeapon != WeaponTypes.NO_WEAPON:
							eWeaponPromotion = gc.getWeaponInfo(eWeapon).getWeaponPromotion()
							if eWeaponPromotion != PromotionTypes.NO_PROMOTION:
								iWeaponExtraAttack = gc.getPromotionInfo(eWeaponPromotion).getExtraCombatStr()
								iWeaponExtraDefense = gc.getPromotionInfo(eWeaponPromotion).getExtraCombatDefense()

						iBareCombatAttackTimes100 = pOpponent.getCombatAttackTimes100() - iWeaponExtraAttack * 100
						iBareCombatDefenseTimes100 = pOpponent.getCombatDefenseTimes100() - iWeaponExtraDefense * 100

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

						if iBareCombatAttackTimes100 <= 400:
							pNewUnit.changeCombatAttack(1)
						else:
							pNewUnit.changeCombatAttackTimes100(iChangeAttackTimes100)
						if iBareCombatDefenseTimes100 <= 400:
							pNewUnit.changeCombatDefense(1)
						else:
							pNewUnit.changeCombatDefenseTimes100(iChangeDefenseTimes100)
						for iProm in xrange(gc.getNumPromotionInfos()):
							if pNewUnit.isHasPromotion(iProm):
								iCount += 1
							else:
								if (pOpponent.isHasPromotion(iProm)):
									if not gc.getPromotionInfo(iProm).isEquipment():
										if (iProm != iChanneling3 and iProm != iDivine and iProm != iBronze and iProm != iIron and iProm != iMithril and iProm != iGreatCommander and iProm != iWild):
											if not gc.getPromotionInfo(iProm).isRace():
												pNewUnit.setHasPromotion(iProm, True)

				elif pCaster.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_PULUFRAUS'):
					pNewUnit = pPlayer.initUnit(pOpponent.getUnitType(), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
					for i in xrange(gc.getNumPromotionInfos()):
						pNewUnit.setHasPromotion(i, pOpponent.isHasPromotion(i))
						if gc.getPromotionInfo(i).isEquipment():
							pNewUnit.setHasPromotion(i, False)
					pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ILLUSION'), True)
					pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IMMORTAL'), False)
					if pNewUnit.isImmortal():
						pNewUnit.disableImmortal()
					pNewUnit.setLevel(pOpponent.getLevel())
					pNewUnit.setExperience(pOpponent.getExperience(), -1)
					pNewUnit.setHasCasted(False)
					pNewUnit.setDuration(1)
					for iProm in xrange(gc.getNumPromotionInfos()):
						if pNewUnit.isHasPromotion(iProm):
							iCount += 1
						else:
							if (pOpponent.isHasPromotion(iProm)):
								if not gc.getPromotionInfo(iProm).isEquipment():
									if (iProm != iChanneling3 and iProm != iDivine and iProm != iBronze and iProm != iIron and iProm != iMithril and iProm != iGreatCommander and iProm != iWild):
										if not gc.getPromotionInfo(iProm).isRace():
											pNewUnit.setHasPromotion(iProm, True)

def postCombatWonCuchumaquic(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isAlive():
		if pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAK')):
			pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAK'), False)
		elif CyGame().getSorenRandNum(1000, "Split Cuchumaquic") < 333:
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

			# opponent bare strength
			iWeaponExtraAttack = 0
			iWeaponExtraDefense = 0
			eWeapon = pOpponent.getWeapon()
			if eWeapon != WeaponTypes.NO_WEAPON:
				eWeaponPromotion = gc.getWeaponInfo(eWeapon).getWeaponPromotion()
				if eWeaponPromotion != PromotionTypes.NO_PROMOTION:
					iWeaponExtraAttack = gc.getPromotionInfo(eWeaponPromotion).getExtraCombatStr()
					iWeaponExtraDefense = gc.getPromotionInfo(eWeaponPromotion).getExtraCombatDefense()

			iOpponentBareCombatAttackTimes100 = pOpponent.getCombatAttackTimes100() - iWeaponExtraAttack * 100
			iOpponentBareCombatDefenseTimes100 = pOpponent.getCombatDefenseTimes100() - iWeaponExtraDefense * 100

			# difference between the bare strength
			iChangeAttackTimes100 = iBareCombatAttackTimes100 - iOpponentBareCombatAttackTimes100
			iChangeDefenseTimes100 = iBareCombatDefenseTimes100 - iOpponentBareCombatDefenseTimes100

			pPlayer = gc.getPlayer(pCaster.getOwner())
			iUnit = pCaster.getUnitType()
			pNewUnit = pPlayer.initUnit(iUnit, pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STRONG'), False)
			pNewUnit.changeCombatStr(-2)
			if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_STRONG')):
				pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAK'), True)
			iCount = 0
			for iProm in xrange(gc.getNumPromotionInfos()):
				if pNewUnit.isHasPromotion(iProm):
					iCount += 1
				else:
					if (pCaster.isHasPromotion(iProm)):
						if not gc.getPromotionInfo(iProm).isEquipment():
							if not gc.getPromotionInfo(iProm).isRace():
								pNewUnit.setHasPromotion(iProm, True)
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_KAIJIN_RACE'), False)
			pNewUnit.setDuration(1 + pCaster.getDuration())
			szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_SPLIT_CUCHUMAQUIC", (pCaster.getNameKey(), ))
			CyGame().pushGameMessage(pCaster.getOwner(), True, szMessage, '', '', en.eColorGreen, pCaster.getX(), pCaster.getY(), False, False)

def postCombatSplitCuchumaquic(argsList):
	pCaster, pOpponent = argsList
	if CyGame().getSorenRandNum(1000, "Split Cuchumaquic") < 333:
		if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAK')):
			pPlayer = gc.getPlayer(pCaster.getOwner())
			iUnit = pCaster.getUnitType()
			pNewUnit = pPlayer.initUnit(iUnit, pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit2 = pPlayer.initUnit(iUnit, pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STRONG'), False)
			pNewUnit2.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STRONG'), False)

			pNewUnit.setCombatAttackTimes100(pCaster.getCombatAttackTimes100())
			pNewUnit.setCombatDefenseTimes100(pCaster.getCombatDefenseTimes100())
			pNewUnit2.setCombatAttackTimes100(pCaster.getCombatAttackTimes100())
			pNewUnit2.setCombatDefenseTimes100(pCaster.getCombatDefenseTimes100())

			pNewUnit.setDamage(25, PlayerTypes.NO_PLAYER)
			pNewUnit2.setDamage(25, PlayerTypes.NO_PLAYER)
			if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_STRONG')):
				pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAK'), True)
				pNewUnit2.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAK'), True)
			iCount = 0
			for iProm in xrange(gc.getNumPromotionInfos()):
				if pNewUnit.isHasPromotion(iProm):
					iCount += 1
				else:
					if (pCaster.isHasPromotion(iProm)):
						if not gc.getPromotionInfo(iProm).isEquipment():
							if not gc.getPromotionInfo(iProm).isRace():
								pNewUnit.setHasPromotion(iProm, True)
								pNewUnit2.setHasPromotion(iProm, True)
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_KAIJIN_RACE'), False)
			pNewUnit2.setHasPromotion(gc.getInfoTypeForString('PROMOTION_KAIJIN_RACE'), False)
			pNewUnit.setDuration(pCaster.getDuration())
			pNewUnit2.setDuration(pCaster.getDuration())
			szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_SPLIT", (pCaster.getNameKey(), ))
			CyGame().pushGameMessage(pCaster.getOwner(), True, szMessage, '', gc.getUnitInfo(iUnit).getButton(), en.eColorRed, pCaster.getX(), pCaster.getY(), False, False)

## Altair
def postCombatMetatoronLost(argsList):
	pCaster, pOpponent = argsList
	if pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ILLUSION')):
		return
	iPlayer = pCaster.getOwner()
	pPlayer = gc.getPlayer(iPlayer)
	for iTrait in xrange(gc.getNumTraitInfos()):
		if iTrait != gc.getInfoTypeForString('TRAIT_AGNOSTIC'):
			if pPlayer.hasTrait(iTrait):
				pPlayer.setHasTrait(iTrait, False)

## Scions
def postCombatMartyrSuicide(argsList):
	pCaster, pOpponent = argsList
	if not pOpponent.canFight():
		return
	if CyGame().getSorenRandNum(100, "Check") < 33:
		pCaster.kill(True, 0)

# ent >>>
def postCombatBlighter(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isEdible() and pOpponent.getDamage() == 100 and not pOpponent.getAfterlife() in (AfterlifeTypes.AFTERLIFE_CAPTURED, AfterlifeTypes.AFTERLIFE_ENSLAVED):
		if pCaster.hasCargo():
			iCasterID = pCaster.getID()
			pPlot = pCaster.plot()
			eCreeper = gc.getInfoTypeForString('UNIT_CREEPER')
			eFed = gc.getInfoTypeForString('PROMOTION_FED_CREEPER')
			for iUnitIndex in xrange(pPlot.getNumUnits()):
				pLoopUnit = pPlot.getUnit(iUnitIndex)
				if pLoopUnit.isCargo() and pLoopUnit.getTransportUnit().getID() == iCasterID:
					if pLoopUnit.getUnitType() == eCreeper:
						if not pLoopUnit.isHasPromotion(eFed):
							pLoopUnit.setHasPromotion(eFed, True)
							pOpponent.setAfterlife(AfterlifeTypes.AFTERLIFE_PREYED)
							return
# ent <<<

## Tiger
def postCombatEin(argsList):
	pCaster, pOpponent = argsList
	if CyGame().getSorenRandNum(100, "Mercenaries Recruiter") <= 33:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MERCENARIES_RECRUITER'), True)

## Xoth
def postCombatAbsorb(argsList):
	pCaster, pOpponent = argsList

	if pCaster.getLevel() < 15:
		listProms = []
		iCount = 0
		for iProm in xrange(gc.getNumPromotionInfos()):
			if pCaster.isHasPromotion(iProm):
				iCount += 1
			else:
				if (pOpponent.isHasPromotion(iProm)):
					if not gc.getPromotionInfo(iProm).isEquipment():
						if not gc.getPromotionInfo(iProm).isRace():
							if gc.getPromotionInfo(iProm).getMinLevel() >= 0:
								listProms.append(iProm)
		if len(listProms) > 0:
			iCount += 1
			iRnd = CyGame().getSorenRandNum(len(listProms), "Absorb")
			pCaster.setHasPromotion(listProms[iRnd], True)
			pCaster.changeLevel(1)
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_ABSORB_ENEMY', (pCaster.getNameKey(), pOpponent.getNameKey(), gc.getPromotionInfo(listProms[iRnd]).getDescription()))
			szButton = gc.getPromotionInfo(listProms[iRnd]).getButton()
			CyGame().pushGameMessage(pCaster.getOwner(), True, szMessage, '', szButton, en.eColorGreen, pCaster.getX(), pCaster.getY(), True, True)
# ent - Move from UnitCreateFromCombat >>>
	if pCaster.getUnitType() == gc.getInfoTypeForString('UNIT_AZATHOTH'):
		if pOpponent.isEdible() and pOpponent.getDamage() == 100 and not pOpponent.getAfterlife() in (AfterlifeTypes.AFTERLIFE_CAPTURED, AfterlifeTypes.AFTERLIFE_ENSLAVED):
			if CyGame().getSorenRandNum(100, "azathoth") < 20:
				pNewUnit = gc.getPlayer(pCaster.getOwner()).initUnit(gc.getInfoTypeForString('UNIT_NIGGURATH'), pCaster.getX(), pCaster.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
				pNewUnit.setDuration(pCaster.getDuration())
				if not pNewUnit.isDuration():
					pNewUnit.setImmobileTimer(1)
			pOpponent.setAfterlife(AfterlifeTypes.AFTERLIFE_PREYED)
# ent <<<

## Baldralfer
def postCombatTriffid(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isAlive():
		if pCaster.getCombatAttackTimes100() < pOpponent.getCombatAttackTimes100():
			pCaster.changeCombatStr(1)
			szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_TRIFFID", (pCaster.getNameKey(), pOpponent.getNameKey()))
			szButton = gc.getPromotionInfo(gc.getInfoTypeForString('PROMOTION_CANNIBALIZE')).getButton()
			CyGame().pushGameMessage(pCaster.getOwner(), True, szMessage, '', szButton, en.eColorGreen, pCaster.getX(), pCaster.getY(), True, True)

## Aristrakh
def postCombatBattleFrenzy(argsList):
	pCaster, pOpponent = argsList
	if pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MURDEROUS_FRENZY4')):
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MURDEROUS_FRENZY4'), False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MURDEROUS_FRENZY5'), True)

	elif pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MURDEROUS_FRENZY3')):
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MURDEROUS_FRENZY3'), False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MURDEROUS_FRENZY4'), True)

	elif pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MURDEROUS_FRENZY2')):
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MURDEROUS_FRENZY2'), False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MURDEROUS_FRENZY3'), True)

	elif pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MURDEROUS_FRENZY1')):
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MURDEROUS_FRENZY1'), False)
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MURDEROUS_FRENZY2'), True)

	else:
		pCaster.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MURDEROUS_FRENZY1'), True)

## Trophies
def postCombatOse(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isHuman():
		szTorophyKey = 'TROPHY_DEFEATED_OSE'
		if not CyGame().isHasTrophy(szTorophyKey):
			CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatTezcatlipoca(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isHuman():
		szTorophyKey = 'TROPHY_DEFEATED_TEZCATLIPOCA'
		if not CyGame().isHasTrophy(szTorophyKey):
			CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatInugami(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isHuman():
		szTorophyKey = 'TROPHY_DEFEATED_INUGAMI'
		if not CyGame().isHasTrophy(szTorophyKey):
			CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatCeryneianHind(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isHuman():
		szTorophyKey = 'TROPHY_DEFEATED_CERYNEIAN_HIND'
		if not CyGame().isHasTrophy(szTorophyKey):
			CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatAzathoth(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isHuman():
		szTorophyKey = 'TROPHY_DEFEATED_AZATHOTH'
		if not CyGame().isHasTrophy(szTorophyKey):
			CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatLemegeton(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isHuman():
		szTorophyKey = 'TROPHY_DEFEATED_LEMEGETON'
		if not CyGame().isHasTrophy(szTorophyKey):
			CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatAlexander(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isHuman():
		szTorophyKey = 'TROPHY_DEFEATED_ALEXANDER'
		if not CyGame().isHasTrophy(szTorophyKey):
			CyGame().changeTrophyValue(szTorophyKey, 1)

def postCombatDiamonddrake(argsList):
	pCaster, pOpponent = argsList
	if pOpponent.isHuman():
		szTorophyKey = 'TROPHY_DEFEATED_DIAMOND_DRAKE'
		if not CyGame().isHasTrophy(szTorophyKey):
			CyGame().changeTrophyValue(szTorophyKey, 1)

# Kaijin <<<
