# Sid Meier's Civilization 4
# Copyright Firaxis Games 2005
#
# CvRandomEventInterface.py
#
# These functions are App Entry Points from C++
# WARNING: These function names should not be changed
# WARNING: These functions can not be placed into a class
#
# No other modules should import this
#
import CvUtil
from CvPythonExtensions import *
import CustomFunctions
import PyHelpers
##--------	Enums Cache: Added by Denev	--------##
import CvPythonEnums
en = CvPythonEnums.CvPythonEnums()
##--------	Enums Cache: End Add		--------##

cf = CustomFunctions.CustomFunctions()
gc = CyGlobalContext()
localText = CyTranslator()
PyPlayer = PyHelpers.PyPlayer

def canUnitTriggerAeronsChosen(argsList):
	eTrigger, pUnit = argsList
	return pUnit.getLevel() >= 5

def canUnitTriggerAmuriteTrial(argsList):
	eTrigger, pUnit = argsList
	return not pUnit.isHiddenNationality()

def applyAmuriteTrial1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pUnit = getUnit(kTriggeredData.ePlayer, kTriggeredData.iUnitId)
	ePlayer2 = cf.getCivilization(gc.getInfoTypeForString('CIVILIZATION_AMURITES'))
	if ePlayer2 != PlayerTypes.NO_PLAYER:
		pPlayer2 = gc.getPlayer(ePlayer2)
		pCity = pPlayer2.getCapitalCity()
		pUnit.setXY(pCity.getX(), pCity.getY(), False, True, True)

def doArmageddonApocalypse(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	iPercent = gc.getDefineINT('APOCALYPSE_KILL_CHANCE')
	if not pPlayer.isIgnoreFood():
		for pyCity in PyPlayer(ePlayer).getCityList():
			pCity = pyCity.GetCy()
			iPop = max(1, pCity.getPopulation() // 2)
			pCity.setPopulation(iPop)
	pyPlayer = PyPlayer(ePlayer)
	apUnitList = pyPlayer.getUnitList()
	for pUnit in apUnitList:
		if pUnit.isAlive():
			if (CyGame().getSorenRandNum(100, "Apocalypse") < iPercent):
				pUnit.kill(False, PlayerTypes.NO_PLAYER)
				CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_APOCALYPSE_KILLED", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Apocalypse.dds', en.eColorRed, pUnit.getX(), pUnit.getY(), True, True)
	if pPlayer.isHuman():
		t = "TROPHY_FEAT_APOCALYPSE"
		if not CyGame().isHasTrophy(t):
			CyGame().changeTrophyValue(t, 1)

def doArmageddonArs(argsList):
	eUnit = gc.getInfoTypeForString('UNIT_ARS')
	if CyGame().getUnitCreatedCount(eUnit) == 0:
		pNewUnit = cf.addBarbarianUnit(eUnit, gc.getInfoTypeForString('BARBARIAN_DEMONS'))
		if pNewUnit is not None:
			pNewUnit.changeImmobileTimer(1)

def doArmageddonBlight(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	py = PyPlayer(ePlayer)
#Kaijin >>>
#	if not pPlayer.isIgnoreFood():
	iCiv = pPlayer.getCivilizationType()
	if not pPlayer.isIgnoreFood() and iCiv != gc.getInfoTypeForString('CIVILIZATION_DARK') and iCiv != gc.getInfoTypeForString('CIVILIZATION_RARNA'):
#Kaijin <<<
		for pyCity in py.getCityList():
			pCity = pyCity.GetCy()
			iBlight = CyGame().getSorenRandNum(15, "Blight")
#			iBlight = 10
			iBlight += pCity.getPopulation()
			iBlight -= pCity.totalGoodBuildingHealth()
			iBlight -= max(0, pCity.getFeatureGoodHealth() - pCity.getFeatureBadHealth())
			if iBlight > 0:
				pCity.changeEspionageHealthCounter(iBlight)
	for pUnit in py.getUnitList():
		if pUnit.isAlive():
			if pUnit.canFight():
				pUnit.doDamage(25, 100, gc.getInfoTypeForString('DAMAGE_DEATH'))

def doArmageddonBuboes(argsList):
	eUnit = gc.getInfoTypeForString('UNIT_BUBOES')
	if CyGame().getUnitCreatedCount(eUnit) == 0:
		pNewUnit = cf.addBarbarianUnit(eUnit, gc.getInfoTypeForString('BARBARIAN_DEMONS'))
		if pNewUnit is not None:
			pNewUnit.changeImmobileTimer(1)

def doArmageddonHellfire(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	if not pPlayer.isTriggerFired(kTriggeredData.eTrigger):
		eChampion = gc.getInfoTypeForString('UNIT_CHAMPION')
		eDemon = gc.getInfoTypeForString('PROMOTION_DEMON')
		eHellfire = gc.getInfoTypeForString('IMPROVEMENT_HELLFIRE')
		iHellfireChance = gc.getDefineINT('HELLFIRE_CHANCE')
		eDemonPlayer = cf.getCivilization(gc.getInfoTypeForString('CIVILIZATION_INFERNAL'))
		if eDemonPlayer == PlayerTypes.NO_PLAYER:
			eDemonPlayer = gc.getBARBARIAN_PLAYER() + gc.getInfoTypeForString('BARBARIAN_DEMONS')
		pDemonPlayer = gc.getPlayer(eDemonPlayer)
		for iPlotIndex in range (CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(iPlotIndex)
			if pPlot.getNumUnits() == 0:
				if pPlot.canHaveImprovement(eHellfire, PlayerTypes.NO_PLAYER, False):
					if pPlot.getBonusType(TeamTypes.NO_TEAM) == BonusTypes.NO_BONUS:
						iImprovement = pPlot.getImprovementType()
						if iImprovement == ImprovementTypes.NO_IMPROVEMENT or not gc.getImprovementInfo(iImprovement).isPermanent():
							if CyGame().getMapRandNum(10000, "Hellfire") < iHellfireChance:
								pPlot.setImprovementType(eHellfire)
								if not pPlot.isVisibleEnemyUnit(eDemonPlayer):
									pNewUnit = pDemonPlayer.initUnit(eChampion, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
									pNewUnit.setHasPromotion(eDemon, True)

def doArmageddonPestilence(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	py = PyPlayer(ePlayer)
#Kaijin >>>
#	if not pPlayer.isIgnoreFood():
	iCiv = pPlayer.getCivilizationType()
	if not pPlayer.isIgnoreFood() and iCiv != gc.getInfoTypeForString('CIVILIZATION_DARK') and iCiv != gc.getInfoTypeForString('CIVILIZATION_RARNA'):
#Kaijin <<<
		for pyCity in py.getCityList():
			pCity = pyCity.GetCy()
			iBlight = CyGame().getSorenRandNum(9, "Pestilence")
			iBlight += (pCity.getPopulation() // 4)
			iBlight -= pCity.totalGoodBuildingHealth()
			iBlight -= max(0, pCity.getFeatureGoodHealth() - pCity.getFeatureBadHealth())
			pCity.changeEspionageHealthCounter(iBlight)
	for pUnit in py.getUnitList():
		if pUnit.isAlive():
			if pUnit.canFight():
				pUnit.doDamage(25, 100, gc.getInfoTypeForString('DAMAGE_DEATH'))

def doArmageddonStephanos(argsList):
	eUnit = gc.getInfoTypeForString('UNIT_STEPHANOS')
	if CyGame().getUnitCreatedCount(eUnit) == 0:
		pNewUnit = cf.addBarbarianUnit(eUnit, gc.getInfoTypeForString('BARBARIAN_DEMONS'))
		if pNewUnit is not None:
			pNewUnit.changeImmobileTimer(1)

def doArmageddonWrath(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	eUnit = gc.getInfoTypeForString('UNIT_WRATH')
	iWrathConvertChance = gc.getDefineINT('WRATH_CONVERT_CHANCE')
	if CyGame().getUnitCreatedCount(eUnit) == 0:
		pNewUnit = cf.addBarbarianUnit(eUnit, gc.getInfoTypeForString('BARBARIAN_DEMONS'))
		if pNewUnit is not None:
			pNewUnit.changeImmobileTimer(1)
			pPlot = pNewUnit.plot()
			if pPlot is not None:
				pPoint = pPlot.getPoint()
				CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_ABADDON_BIRTH'), pPoint)

	eEnraged = gc.getInfoTypeForString('PROMOTION_ENRAGED')
	eDomainLand = gc.getInfoTypeForString('DOMAIN_LAND')
	py = PyPlayer(ePlayer)
	for pUnit in py.getUnitList():
		if pUnit.getDomainType() == eDomainLand:
			if pUnit.isAlive():
				if CyGame().getSorenRandNum(100, "Wrath") < iWrathConvertChance:
					if not isWorldUnitClass(pUnit.getUnitClassType()):
						pUnit.setHasPromotion(eEnraged, True)
						CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_WRATH_ENRAGED", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Promotions/Enraged.dds', en.eColorRed, pUnit.getX(), pUnit.getY(), True, True)

def doArmageddonYersinia(argsList):
	eUnit = gc.getInfoTypeForString('UNIT_YERSINIA')
	if CyGame().getUnitCreatedCount(eUnit) == 0:
		pNewUnit = cf.addBarbarianUnit(eUnit, gc.getInfoTypeForString('BARBARIAN_DEMONS'))
		if pNewUnit is not None:
			pNewUnit.changeImmobileTimer(1)

def doAzer(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	eUnit = gc.getInfoTypeForString('UNIT_AZER')
	if not pPlot.isNone():
		pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
		pNewUnit = pBarbarianPlayer.initUnit(eUnit, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit.changeImmobileTimer(1)

def doBanditNietz3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_HORSEMAN'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
##--------		Advanced Rules: Modified by Denev	--------##
#	pNewUnit.setName("Nietz the Bandit Lord")
	pNewUnit.setName(localText.getText("TXT_KEY_UNIT_NIETZ", ()))
##--------		Advanced Rules: End Modify			--------##
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HERO'), True)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MOBILITY1'), True)

def helpBanditNietz3(argsList):
#	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_BANDIT_NIETZ_3_HELP", ())
	return szHelp

def doCalabimSanctuary1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	eCalabimPlayer = cf.getCivilization(gc.getInfoTypeForString('CIVILIZATION_CALABIM'))
	if eCalabimPlayer != PlayerTypes.NO_PLAYER:
		pPlayer2 = gc.getPlayer(eCalabimPlayer)
		pPlayer2.AI_changeAttitudeExtra(ePlayer,-4)

def canCityTriggerCityFeud(argsList):
	eTrigger, pCity = argsList
	return not pCity.isCapital()

def doCityFeudArson(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	cf.doCityFire(pCity)

def doCityFeudStart1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCapitalCity = pPlayer.getCapitalCity()
	pCapitalCity.changeHappinessTimer(5)

def doCityFeudStart3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCapitalCity = pPlayer.getCapitalCity()
	pCapitalCity.changeOccupationTimer(5)
# ent: insert applyLandmarkFromEvent() at EventSigns.py >>>
	event = gc.getEventInfo(eEvent)
	iComm = event.getPlotExtraYield(YieldTypes.YIELD_COMMERCE)

	sCaptionFood = ""
	sCaptionProd = ""
	sCaptionComm = localText.getText("TXT_KEY_SIGN_FORMAT_COMM", (iComm, )) + u" "
	sCaptionDesc = localText.getText("TXT_KEY_SIGN_" + event.getType(), ())
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)

	sCaption = localText.getText("TXT_KEY_SIGN_FORMAT_OVERVIEW", (sCaptionFood, sCaptionProd, sCaptionComm, sCaptionDesc))

	for ePlayer in xrange(gc.getMAX_CIV_PLAYERS()):
		pPlayer = gc.getPlayer(ePlayer)
		if pPlayer.isAlive() and pPlayer.isHuman():
			CyEngine().addSign(pPlot, ePlayer, sCaption)
# ent <<<

def helpCityFeudStart1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = pPlayer.getCapitalCity()
	szHelp = localText.getText("TXT_KEY_EVENT_CITY_FEUD_START_1_HELP", (pCity.getName(), ))
	return szHelp

def helpCityFeudStart3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = pPlayer.getCapitalCity()
	szHelp = localText.getText("TXT_KEY_EVENT_CITY_FEUD_START_3_HELP", (pCity.getName(), ))
	return szHelp

def canTriggerCitySplit(argsList):
# Kaijin >>> オプション『都市の独立の有効化』
	if not CyGame().isOption(gc.getInfoTypeForString('GAMEOPTION_MODDER_3')):
		return False
# Kaijin <<<
	if CyGame().getWBMapScript():
		return False
	ePlayer, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
# Kaijin >>> 蛮族志向のプレイヤーでも発生させる
#	if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_BARBARIAN')):
	if pPlayer == gc.getPlayer(gc.getBARBARIAN_PLAYER()):
# Kaijin <<<
		return False
	if pPlayer.getOpenPlayer() == PlayerTypes.NO_PLAYER:
		return False
# Kaijin >>>
	"""
	eKoun = gc.getInfoTypeForString('LEADER_KOUN')
	for eLoopPlayer in range(gc.getMAX_CIV_PLAYERS()):
		pLoopPlayer = gc.getPlayer(eLoopPlayer)
		if pLoopPlayer.isAlive():
			if pLoopPlayer.getLeaderType() == eKoun:
				return False
	"""
	Leaders = [ 'LEADER_KOUN' ]
# Kaijin <<<
	if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_BANNOR'):
		Leaders = [ 'LEADER_SABATHIEL','LEADER_CAPRIA','LEADER_TETHIRA','LEADER_DECIUS','LEADER_GAHERIS','LEADER_ANGAAD' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MALAKIM'):
		Leaders = [ 'LEADER_VARN','LEADER_DECIUS','LEADER_KANE','LEADER_SHAMASH','LEADER_USHEEJA','LEADER_SARALET' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ELOHIM'):
		Leaders = [ 'LEADER_ETHNE','LEADER_EINION','LEADER_THESSALONICA','LEADER_NEPHELE','LEADER_MEELAIS','LEADER_VESTA' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MERCURIANS'):
		Leaders = [ 'LEADER_JUDECCA','LEADER_SALLOS','LEADER_OUZZA','LEADER_MERESIN','LEADER_STATIUS','LEADER_LETHE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LUCHUIRP'):
		Leaders = [ 'LEADER_GARRIM','LEADER_BEERI','LEADER_GISLI','LEADER_KISH_RIKA','LEADER_LETIGO','LEADER_BEAR_GUIN' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_KURIOTATES'):
		Leaders = [ 'LEADER_CARDITH','LEADER_FAVNA','LEADER_HYUNKEL','LEADER_HERNE','LEADER_CITH_MOR','LEADER_CHERON','LEADER_TEACHER' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LJOSALFAR'):
		Leaders = [ 'LEADER_AMELANCHIER','LEADER_ARENDEL','LEADER_THESSA','LEADER_AIBELL','LEADER_SAULE','LEADER_ELDARWEN' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_KHAZAD'):
		Leaders = [ 'LEADER_ARTURUS','LEADER_KANDROS','LEADER_NICODEMUS','LEADER_ATHEL','LEADER_VITNIR','LEADER_LLAMERADA' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SIDAR'):
		Leaders = [ 'LEADER_SANDALPHON','LEADER_SHEKINAH','LEADER_SHUMUEL','LEADER_MIRROUGH','LEADER_LEASIEIGH','LEADER_RASIEL' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LANUN'):
		Leaders = [ 'LEADER_FALAMAR','LEADER_HANNAH','LEADER_FRITZ','LEADER_NAIAS','LEADER_CASIN','LEADER_MORDMORGAN' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_GRIGORI'):
		Leaders = [ 'LEADER_CASSIEL','LEADER_GOODREAU','LEADER_MENEC','LEADER_ZODALORE','LEADER_OUTHE','LEADER_GOLBEZ','LEADER_KOUN' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_HIPPUS'):
		Leaders = [ 'LEADER_TASUNKE','LEADER_RHOANNA','LEADER_OSTANES','LEADER_ULDANOR','LEADER_SELMA','LEADER_ILITHIRIDAN' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_AMURITES'):
		Leaders = [ 'LEADER_VALLEDIA','LEADER_DAIN','LEADER_TYA','LEADER_GWYEN','LEADER_VERLAIN','LEADER_LORELEI' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DOVIELLO'):
		Leaders = [ 'LEADER_CHARADON','LEADER_MAHALA','LEADER_DUIN','LEADER_BYGGVIR','LEADER_SIRVAGHA','LEADER_EMMA' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_BALSERAPHS'):
		Leaders = [ 'LEADER_PERPENTACH','LEADER_KEELYN','LEADER_WEEVIL','LEADER_FURIA','LEADER_MELISANDRE','LEADER_TALIESIN','LEADER_NOJAH','LEADER_NELL' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_CLAN_OF_EMBERS'):
		Leaders = [ 'LEADER_JONAS','LEADER_SHEELBA','LEADER_HAFGAN','LEADER_AZZAN','LEADER_JI','LEADER_HEHNKU' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SVARTALFAR'):
		Leaders = [ 'LEADER_FAERYL','LEADER_RIVANNA','LEADER_VOLANNA','LEADER_MATHEUS','LEADER_HATHEIM','LEADER_UTIRUSO' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_CALABIM'):
		Leaders = [ 'LEADER_ALEXIS','LEADER_FLAUROS','LEADER_DECIUS','LEADER_MAHON','LEADER_NERGAL','LEADER_ELENA','LEADER_ELIJAH','LEADER_AILIMER' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SHEAIM'):
		Leaders = [ 'LEADER_TEBRYN','LEADER_OS-GABELLA','LEADER_AVERAX','LEADER_GOSEA','LEADER_MALCHAVIC','LEADER_EROMKCALB' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_INFERNAL'):
		Leaders = [ 'LEADER_JUDECCA','LEADER_SALLOS','LEADER_OUZZA','LEADER_MERESIN','LEADER_STATIUS','LEADER_LETHE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ILLIANS'):
		Leaders = [ 'LEADER_AURIC','LEADER_BRAEDEN','LEADER_DUMANNIOS','LEADER_RIUROS','LEADER_ANAGANTIOS','LEADER_RAITLOR' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_NIRAIKANAI'):
		Leaders = [ 'LEADER_NIRAIKANAI_MA','LEADER_NIRAIKANAI_TINA','LEADER_NIRAIKANAI_LISA','LEADER_NIRAIKANAI_SENDAK','LEADER_NIRAIKANAI_TERRY','LEADER_NIRAIKANAI_LEAKAGE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DARK'):
		Leaders = [ 'LEADER_DARK','LEADER_PROFESSOR','LEADER_OMAEMONA','LEADER_GIKO_HANYAAN','LEADER_MORALER','LEADER_HAGURUMA_OH' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_YS'):
		Leaders = [ 'LEADER_REAH','LEADER_FEENA','LEADER_FLEURETTE','LEADER_JAHL','LEADER_LISE','LEADER_OLIVIER' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ECHIGO'):
		Leaders = [ 'LEADER_KENSHIN','LEADER_NAOE','LEADER_KAGETSUNA','LEADER_KAKIZAKI','LEADER_USAMI','LEADER_AMAKASU' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DROAUM'):
		Leaders = [ 'LEADER_KATRA','LEADER_TERAZA','LEADER_ROBERT','LEADER_RICHARD','LEADER_DARSK','LEADER_SHERLALAQUE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DESPIEL'):
		Leaders = [ 'LEADER_YENOIAH','LEADER_LADIBARRE','LEADER_ARGYROS','LEADER_GOLY','LEADER_ARSINE','LEADER_PZEVDARGYROS' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LINEAGE'):
		Leaders = [ 'LEADER_MARIS','LEADER_LEORD','LEADER_GEORISTALPEHN','LEADER_CARSE','LEADER_DIANA','LEADER_YAMAMOTO' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MAZATL'):
		Leaders = [ 'LEADER_HIANTHROGH','LEADER_KHSET','LEADER_AMINZERUGH','LEADER_MARST','LEADER_SACCHATHROGHN','LEADER_RAFFISERUNO' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_CUALLI'):
		Leaders = [ 'LEADER_KOLSEHVAHN','LEADER_MIHUATL','LEADER_GHUROVAH','LEADER_INVERUPH','LEADER_CHYSTAOLLI','LEADER_GLUCOATL' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ALTAIR'):
		Leaders = [ 'LEADER_METATORON','LEADER_LKBRETH','LEADER_BJEW','LEADER_YAHWEH','LEADER_ASTARTE','LEADER_GEHENNA' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MECHANOS'):
		Leaders = [ 'LEADER_VEROCCHIO','LEADER_MAER','LEADER_METALWOLF','LEADER_RAIDEN','LEADER_ATMAN','LEADER_AMAZIGH' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SCIONS'):
		Leaders = [ 'LEADER_RISEN_EMPEROR','LEADER_KORRINA','LEADER_OPHELIA','LEADER_XIVAN','LEADER_NERO','LEADER_TIBERIUS' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_NIVAL'):
		Leaders = [ 'LEADER_EKHLO','LEADER_QITURN','LEADER_SCHOENGAR','LEADER_NEIGE','LEADER_HIVER','LEADER_GIVRE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_RARNA'):
		Leaders = [ 'LEADER_RAPHEL','LEADER_GEORGES','LEADER_MARGARETE','LEADER_OSWALD','LEADER_LASLO','LEADER_IGNATIUS' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_TIGER'):
		Leaders = [ 'LEADER_FOX','LEADER_HOUND','LEADER_VULEPES','LEADER_COYOTE','LEADER_STEINDORF' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_XOTH'):
		Leaders = [ 'LEADER_JUDECCA','LEADER_SALLOS','LEADER_OUZZA','LEADER_MERESIN','LEADER_STATIUS','LEADER_LETHE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_BALDRALFAR'):
		Leaders = [ 'LEADER_INGWE','LEADER_WERDNA','LEADER_ARDWEN','LEADER_LUTHIEN','LEADER_FINWE','LEADER_ELWE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_NOUGBII'):
		Leaders = [ 'LEADER_ADELAIS','LEADER_YRTSUDNI','LEADER_EPYTR','LEADER_ANIPUSA','LEADER_ENYDLACI','LEADER_TIVAVQA' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ARISTRAKH'):
		Leaders = [ 'LEADER_NIKEPHOROS','LEADER_NAJESH','LEADER_NUSLUEL','LEADER_NOHMAMARE','LEADER_NEWT','LEADER_NOTHERLY','LEADER_NESGOSYM','LEADER_NECROZOURE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MEGISUS'):
		Leaders = [ 'LEADER_HERMES_THE_SECOND','LEADER_ROGEREN','LEADER_ALBERAT','LEADER_HERMES_THE_THIRD','LEADER_PARASTENDI','LEADER_GEBERAR' ]

	iLeaders = []
	for sLeader in Leaders:
		iLeaders.append(gc.getInfoTypeForString(sLeader))
#	print gc.getMAX_PLAYERS()
	for iPlayer in range(gc.getMAX_PLAYERS()):
		pLoopPlayer = gc.getPlayer(iPlayer)
#		print pLoopPlayer.getLeaderType()
		if pLoopPlayer.getLeaderType() in iLeaders:
			iLeaders.remove(pLoopPlayer.getLeaderType())
	return len(iLeaders) > 0
        
def canCityTriggerSplitCity(argsList):
	eTrigger, pCity = argsList
	return not pCity.isCapital()

def doCitySplit1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
# Kaijin >>>
#	pSplitPlayer = cf.formEmpire(pPlayer.getCivilizationType(), gc.getInfoTypeForString('LEADER_KOUN'), TeamTypes.NO_TEAM, pCity, pPlayer.getAlignment(), pPlayer)
	Leaders = [ 'LEADER_KOUN' ]
	if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_BANNOR'):
		Leaders = [ 'LEADER_SABATHIEL','LEADER_CAPRIA','LEADER_TETHIRA','LEADER_DECIUS','LEADER_GAHERIS','LEADER_ANGAAD' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MALAKIM'):
		Leaders = [ 'LEADER_VARN','LEADER_DECIUS','LEADER_KANE','LEADER_SHAMASH','LEADER_USHEEJA','LEADER_SARALET' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ELOHIM'):
		Leaders = [ 'LEADER_ETHNE','LEADER_EINION','LEADER_THESSALONICA','LEADER_NEPHELE','LEADER_MEELAIS','LEADER_VESTA' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MERCURIANS'):
		Leaders = [ 'LEADER_JUDECCA','LEADER_SALLOS','LEADER_OUZZA','LEADER_MERESIN','LEADER_STATIUS','LEADER_LETHE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LUCHUIRP'):
		Leaders = [ 'LEADER_GARRIM','LEADER_BEERI','LEADER_GISLI','LEADER_KISH_RIKA','LEADER_LETIGO','LEADER_BEAR_GUIN' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_KURIOTATES'):
		Leaders = [ 'LEADER_CARDITH','LEADER_FAVNA','LEADER_HYUNKEL','LEADER_HERNE','LEADER_CITH_MOR','LEADER_CHERON','LEADER_TEACHER' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LJOSALFAR'):
		Leaders = [ 'LEADER_AMELANCHIER','LEADER_ARENDEL','LEADER_THESSA','LEADER_AIBELL','LEADER_SAULE','LEADER_ELDARWEN' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_KHAZAD'):
		Leaders = [ 'LEADER_ARTURUS','LEADER_KANDROS','LEADER_NICODEMUS','LEADER_ATHEL','LEADER_VITNIR','LEADER_LLAMERADA' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SIDAR'):
		Leaders = [ 'LEADER_SANDALPHON','LEADER_SHEKINAH','LEADER_SHUMUEL','LEADER_MIRROUGH','LEADER_LEASIEIGH','LEADER_RASIEL' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LANUN'):
		Leaders = [ 'LEADER_FALAMAR','LEADER_HANNAH','LEADER_FRITZ','LEADER_NAIAS','LEADER_CASIN','LEADER_MORDMORGAN' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_GRIGORI'):
		Leaders = [ 'LEADER_CASSIEL','LEADER_GOODREAU','LEADER_MENEC','LEADER_ZODALORE','LEADER_OUTHE','LEADER_GOLBEZ','LEADER_KOUN' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_HIPPUS'):
		Leaders = [ 'LEADER_TASUNKE','LEADER_RHOANNA','LEADER_OSTANES','LEADER_ULDANOR','LEADER_SELMA','LEADER_ILITHIRIDAN' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_AMURITES'):
		Leaders = [ 'LEADER_VALLEDIA','LEADER_DAIN','LEADER_TYA','LEADER_GWYEN','LEADER_VERLAIN','LEADER_LORELEI' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DOVIELLO'):
		Leaders = [ 'LEADER_CHARADON','LEADER_MAHALA','LEADER_DUIN','LEADER_BYGGVIR','LEADER_SIRVAGHA','LEADER_EMMA' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_BALSERAPHS'):
		Leaders = [ 'LEADER_PERPENTACH','LEADER_KEELYN','LEADER_WEEVIL','LEADER_FURIA','LEADER_MELISANDRE','LEADER_TALIESIN','LEADER_NOJAH','LEADER_NELL' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_CLAN_OF_EMBERS'):
		Leaders = [ 'LEADER_JONAS','LEADER_SHEELBA','LEADER_HAFGAN','LEADER_AZZAN','LEADER_JI','LEADER_HEHNKU' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SVARTALFAR'):
		Leaders = [ 'LEADER_FAERYL','LEADER_RIVANNA','LEADER_VOLANNA','LEADER_MATHEUS','LEADER_HATHEIM','LEADER_UTIRUSO' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_CALABIM'):
		Leaders = [ 'LEADER_ALEXIS','LEADER_FLAUROS','LEADER_DECIUS','LEADER_MAHON','LEADER_NERGAL','LEADER_ELENA','LEADER_ELIJAH','LEADER_AILIMER' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SHEAIM'):
		Leaders = [ 'LEADER_TEBRYN','LEADER_OS-GABELLA','LEADER_AVERAX','LEADER_GOSEA','LEADER_MALCHAVIC','LEADER_EROMKCALB' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_INFERNAL'):
		Leaders = [ 'LEADER_JUDECCA','LEADER_SALLOS','LEADER_OUZZA','LEADER_MERESIN','LEADER_STATIUS','LEADER_LETHE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ILLIANS'):
		Leaders = [ 'LEADER_AURIC','LEADER_BRAEDEN','LEADER_DUMANNIOS','LEADER_RIUROS','LEADER_ANAGANTIOS','LEADER_RAITLOR' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_NIRAIKANAI'):
		Leaders = [ 'LEADER_NIRAIKANAI_MA','LEADER_NIRAIKANAI_TINA','LEADER_NIRAIKANAI_LISA','LEADER_NIRAIKANAI_SENDAK','LEADER_NIRAIKANAI_TERRY','LEADER_NIRAIKANAI_LEAKAGE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DARK'):
		Leaders = [ 'LEADER_DARK','LEADER_PROFESSOR','LEADER_OMAEMONA','LEADER_GIKO_HANYAAN','LEADER_MORALER','LEADER_HAGURUMA_OH' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_YS'):
		Leaders = [ 'LEADER_REAH','LEADER_FEENA','LEADER_FLEURETTE','LEADER_JAHL','LEADER_LISE','LEADER_OLIVIER' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ECHIGO'):
		Leaders = [ 'LEADER_KENSHIN','LEADER_NAOE','LEADER_KAGETSUNA','LEADER_KAKIZAKI','LEADER_USAMI','LEADER_AMAKASU' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DROAUM'):
		Leaders = [ 'LEADER_KATRA','LEADER_TERAZA','LEADER_ROBERT','LEADER_RICHARD','LEADER_DARSK','LEADER_SHERLALAQUE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DESPIEL'):
		Leaders = [ 'LEADER_YENOIAH','LEADER_LADIBARRE','LEADER_ARGYROS','LEADER_GOLY','LEADER_ARSINE','LEADER_PZEVDARGYROS' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LINEAGE'):
		Leaders = [ 'LEADER_MARIS','LEADER_LEORD','LEADER_GEORISTALPEHN','LEADER_CARSE','LEADER_DIANA','LEADER_YAMAMOTO' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MAZATL'):
		Leaders = [ 'LEADER_HIANTHROGH','LEADER_KHSET','LEADER_AMINZERUGH','LEADER_MARST','LEADER_SACCHATHROGHN','LEADER_RAFFISERUNO' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_CUALLI'):
		Leaders = [ 'LEADER_KOLSEHVAHN','LEADER_MIHUATL','LEADER_GHUROVAH','LEADER_INVERUPH','LEADER_CHYSTAOLLI','LEADER_GLUCOATL' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ALTAIR'):
		Leaders = [ 'LEADER_METATORON','LEADER_LKBRETH','LEADER_BJEW','LEADER_YAHWEH','LEADER_ASTARTE','LEADER_GEHENNA' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MECHANOS'):
		Leaders = [ 'LEADER_VEROCCHIO','LEADER_MAER','LEADER_METALWOLF','LEADER_RAIDEN','LEADER_ATMAN','LEADER_AMAZIGH' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SCIONS'):
		Leaders = [ 'LEADER_RISEN_EMPEROR','LEADER_KORRINA','LEADER_OPHELIA','LEADER_XIVAN','LEADER_NERO','LEADER_TIBERIUS' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_NIVAL'):
		Leaders = [ 'LEADER_EKHLO','LEADER_QITURN','LEADER_SCHOENGAR','LEADER_NEIGE','LEADER_HIVER','LEADER_GIVRE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_RARNA'):
		Leaders = [ 'LEADER_RAPHEL','LEADER_GEORGES','LEADER_MARGARETE','LEADER_OSWALD','LEADER_LASLO','LEADER_IGNATIUS' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_TIGER'):
		Leaders = [ 'LEADER_FOX','LEADER_HOUND','LEADER_VULEPES','LEADER_COYOTE','LEADER_STEINDORF' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_XOTH'):
		Leaders = [ 'LEADER_JUDECCA','LEADER_SALLOS','LEADER_OUZZA','LEADER_MERESIN','LEADER_STATIUS','LEADER_LETHE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_BALDRALFAR'):
		Leaders = [ 'LEADER_INGWE','LEADER_WERDNA','LEADER_ARDWEN','LEADER_LUTHIEN','LEADER_FINWE','LEADER_ELWE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_NOUGBII'):
		Leaders = [ 'LEADER_ADELAIS','LEADER_YRTSUDNI','LEADER_EPYTR','LEADER_ANIPUSA','LEADER_ENYDLACI','LEADER_TIVAVQA' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ARISTRAKH'):
		Leaders = [ 'LEADER_NIKEPHOROS','LEADER_NAJESH','LEADER_NUSLUEL','LEADER_NOHMAMARE','LEADER_NEWT','LEADER_NOTHERLY','LEADER_NESGOSYM','LEADER_NECROZOURE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MEGISUS'):
		Leaders = [ 'LEADER_HERMES_THE_SECOND','LEADER_ROGEREN','LEADER_ALBERAT','LEADER_HERMES_THE_THIRD','LEADER_PARASTENDI','LEADER_GEBERAR' ]

	iLeaders = []
	for sLeader in Leaders:
		iLeaders.append(gc.getInfoTypeForString(sLeader))

	for iPlayer in range(gc.getMAX_PLAYERS()):
		pLoopPlayer = gc.getPlayer(iPlayer)
		if pLoopPlayer.getLeaderType() in iLeaders:
			iLeaders.remove(pLoopPlayer.getLeaderType())
	iKoun = iLeaders[CyGame().getSorenRandNum(len(iLeaders), "Leaders Select")]
	pSplitPlayer = cf.formEmpire(pPlayer.getCivilizationType(), iKoun, TeamTypes.NO_TEAM, pCity, pPlayer.getAlignment(), pPlayer)

	## Globalcounter initialization
	cf.doGlobalcounterInitialization(pSplitPlayer.getID())

# Kaijin <<<
	pSplitPlayer.setParent(kTriggeredData.ePlayer)

def doSoverignCity1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
# Kaijin >>>
#	cf.formEmpire(pPlayer.getCivilizationType(), gc.getInfoTypeForString('LEADER_KOUN'), pPlayer.getTeam(), pCity, pPlayer.getAlignment(), pPlayer)
	Leaders = [ 'LEADER_KOUN' ]
	if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_BANNOR'):
		Leaders = [ 'LEADER_SABATHIEL','LEADER_CAPRIA','LEADER_TETHIRA','LEADER_DECIUS','LEADER_GAHERIS','LEADER_ANGAAD' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MALAKIM'):
		Leaders = [ 'LEADER_VARN','LEADER_DECIUS','LEADER_KANE','LEADER_SHAMASH','LEADER_USHEEJA','LEADER_SARALET' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ELOHIM'):
		Leaders = [ 'LEADER_ETHNE','LEADER_EINION','LEADER_THESSALONICA','LEADER_NEPHELE','LEADER_MEELAIS','LEADER_VESTA' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MERCURIANS'):
		Leaders = [ 'LEADER_JUDECCA','LEADER_SALLOS','LEADER_OUZZA','LEADER_MERESIN','LEADER_STATIUS','LEADER_LETHE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LUCHUIRP'):
		Leaders = [ 'LEADER_GARRIM','LEADER_BEERI','LEADER_GISLI','LEADER_KISH_RIKA','LEADER_LETIGO','LEADER_BEAR_GUIN' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_KURIOTATES'):
		Leaders = [ 'LEADER_CARDITH','LEADER_FAVNA','LEADER_HYUNKEL','LEADER_HERNE','LEADER_CITH_MOR','LEADER_CHERON','LEADER_TEACHER' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LJOSALFAR'):
		Leaders = [ 'LEADER_AMELANCHIER','LEADER_ARENDEL','LEADER_THESSA','LEADER_AIBELL','LEADER_SAULE','LEADER_ELDARWEN' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_KHAZAD'):
		Leaders = [ 'LEADER_ARTURUS','LEADER_KANDROS','LEADER_NICODEMUS','LEADER_ATHEL','LEADER_VITNIR','LEADER_LLAMERADA' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SIDAR'):
		Leaders = [ 'LEADER_SANDALPHON','LEADER_SHEKINAH','LEADER_SHUMUEL','LEADER_MIRROUGH','LEADER_LEASIEIGH','LEADER_RASIEL' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LANUN'):
		Leaders = [ 'LEADER_FALAMAR','LEADER_HANNAH','LEADER_FRITZ','LEADER_NAIAS','LEADER_CASIN','LEADER_MORDMORGAN' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_GRIGORI'):
		Leaders = [ 'LEADER_CASSIEL','LEADER_GOODREAU','LEADER_MENEC','LEADER_ZODALORE','LEADER_OUTHE','LEADER_GOLBEZ','LEADER_KOUN' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_HIPPUS'):
		Leaders = [ 'LEADER_TASUNKE','LEADER_RHOANNA','LEADER_OSTANES','LEADER_ULDANOR','LEADER_SELMA','LEADER_ILITHIRIDAN' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_AMURITES'):
		Leaders = [ 'LEADER_VALLEDIA','LEADER_DAIN','LEADER_TYA','LEADER_GWYEN','LEADER_VERLAIN','LEADER_LORELEI' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DOVIELLO'):
		Leaders = [ 'LEADER_CHARADON','LEADER_MAHALA','LEADER_DUIN','LEADER_BYGGVIR','LEADER_SIRVAGHA','LEADER_EMMA' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_BALSERAPHS'):
		Leaders = [ 'LEADER_PERPENTACH','LEADER_KEELYN','LEADER_WEEVIL','LEADER_FURIA','LEADER_MELISANDRE','LEADER_TALIESIN','LEADER_NOJAH','LEADER_NELL' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_CLAN_OF_EMBERS'):
		Leaders = [ 'LEADER_JONAS','LEADER_SHEELBA','LEADER_HAFGAN','LEADER_AZZAN','LEADER_JI','LEADER_HEHNKU' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SVARTALFAR'):
		Leaders = [ 'LEADER_FAERYL','LEADER_RIVANNA','LEADER_VOLANNA','LEADER_MATHEUS','LEADER_HATHEIM','LEADER_UTIRUSO' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_CALABIM'):
		Leaders = [ 'LEADER_ALEXIS','LEADER_FLAUROS','LEADER_DECIUS','LEADER_MAHON','LEADER_NERGAL','LEADER_ELENA','LEADER_ELIJAH','LEADER_AILIMER' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SHEAIM'):
		Leaders = [ 'LEADER_TEBRYN','LEADER_OS-GABELLA','LEADER_AVERAX','LEADER_GOSEA','LEADER_MALCHAVIC','LEADER_EROMKCALB' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_INFERNAL'):
		Leaders = [ 'LEADER_JUDECCA','LEADER_SALLOS','LEADER_OUZZA','LEADER_MERESIN','LEADER_STATIUS','LEADER_LETHE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ILLIANS'):
		Leaders = [ 'LEADER_AURIC','LEADER_BRAEDEN','LEADER_DUMANNIOS','LEADER_RIUROS','LEADER_ANAGANTIOS','LEADER_RAITLOR' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_NIRAIKANAI'):
		Leaders = [ 'LEADER_NIRAIKANAI_MA','LEADER_NIRAIKANAI_TINA','LEADER_NIRAIKANAI_LISA','LEADER_NIRAIKANAI_SENDAK','LEADER_NIRAIKANAI_TERRY','LEADER_NIRAIKANAI_LEAKAGE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DARK'):
		Leaders = [ 'LEADER_DARK','LEADER_PROFESSOR','LEADER_OMAEMONA','LEADER_GIKO_HANYAAN','LEADER_MORALER','LEADER_HAGURUMA_OH' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_YS'):
		Leaders = [ 'LEADER_REAH','LEADER_FEENA','LEADER_FLEURETTE','LEADER_JAHL','LEADER_LISE','LEADER_OLIVIER' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ECHIGO'):
		Leaders = [ 'LEADER_KENSHIN','LEADER_NAOE','LEADER_KAGETSUNA','LEADER_KAKIZAKI','LEADER_USAMI','LEADER_AMAKASU' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DROAUM'):
		Leaders = [ 'LEADER_KATRA','LEADER_TERAZA','LEADER_ROBERT','LEADER_RICHARD','LEADER_DARSK','LEADER_SHERLALAQUE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DESPIEL'):
		Leaders = [ 'LEADER_YENOIAH','LEADER_LADIBARRE','LEADER_ARGYROS','LEADER_GOLY','LEADER_ARSINE','LEADER_PZEVDARGYROS' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LINEAGE'):
		Leaders = [ 'LEADER_MARIS','LEADER_LEORD','LEADER_GEORISTALPEHN','LEADER_CARSE','LEADER_DIANA','LEADER_YAMAMOTO' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MAZATL'):
		Leaders = [ 'LEADER_HIANTHROGH','LEADER_KHSET','LEADER_AMINZERUGH','LEADER_MARST','LEADER_SACCHATHROGHN','LEADER_RAFFISERUNO' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_CUALLI'):
		Leaders = [ 'LEADER_KOLSEHVAHN','LEADER_MIHUATL','LEADER_GHUROVAH','LEADER_INVERUPH','LEADER_CHYSTAOLLI','LEADER_GLUCOATL' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ALTAIR'):
		Leaders = [ 'LEADER_METATORON','LEADER_LKBRETH','LEADER_BJEW','LEADER_YAHWEH','LEADER_ASTARTE','LEADER_GEHENNA' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MECHANOS'):
		Leaders = [ 'LEADER_VEROCCHIO','LEADER_MAER','LEADER_METALWOLF','LEADER_RAIDEN','LEADER_ATMAN','LEADER_AMAZIGH' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SCIONS'):
		Leaders = [ 'LEADER_RISEN_EMPEROR','LEADER_KORRINA','LEADER_OPHELIA','LEADER_XIVAN','LEADER_NERO','LEADER_TIBERIUS' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_NIVAL'):
		Leaders = [ 'LEADER_EKHLO','LEADER_QITURN','LEADER_SCHOENGAR','LEADER_NEIGE','LEADER_HIVER','LEADER_GIVRE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_RARNA'):
		Leaders = [ 'LEADER_RAPHEL','LEADER_GEORGES','LEADER_MARGARETE','LEADER_OSWALD','LEADER_LASLO','LEADER_IGNATIUS' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_TIGER'):
		Leaders = [ 'LEADER_FOX','LEADER_HOUND','LEADER_VULEPES','LEADER_COYOTE','LEADER_STEINDORF' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_XOTH'):
		Leaders = [ 'LEADER_JUDECCA','LEADER_SALLOS','LEADER_OUZZA','LEADER_MERESIN','LEADER_STATIUS','LEADER_LETHE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_BALDRALFAR'):
		Leaders = [ 'LEADER_INGWE','LEADER_WERDNA','LEADER_ARDWEN','LEADER_LUTHIEN','LEADER_FINWE','LEADER_ELWE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_NOUGBII'):
		Leaders = [ 'LEADER_ADELAIS','LEADER_YRTSUDNI','LEADER_EPYTR','LEADER_ANIPUSA','LEADER_ENYDLACI','LEADER_TIVAVQA' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ARISTRAKH'):
		Leaders = [ 'LEADER_NIKEPHOROS','LEADER_NAJESH','LEADER_NUSLUEL','LEADER_NOHMAMARE','LEADER_NEWT','LEADER_NOTHERLY','LEADER_NESGOSYM','LEADER_NECROZOURE' ]
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MEGISUS'):
		Leaders = [ 'LEADER_HERMES_THE_SECOND','LEADER_ROGEREN','LEADER_ALBERAT','LEADER_HERMES_THE_THIRD','LEADER_PARASTENDI','LEADER_GEBERAR' ]

	iLeaders = []
	for sLeader in Leaders:
		iLeaders.append(gc.getInfoTypeForString(sLeader))

	for iPlayer in range(gc.getMAX_PLAYERS()):
		pLoopPlayer = gc.getPlayer(iPlayer)
		if pLoopPlayer.getLeaderType() in iLeaders:
			iLeaders.remove(pLoopPlayer.getLeaderType())
	iKoun = iLeaders[CyGame().getSorenRandNum(len(iLeaders), "Leaders Select")]
#	cf.formEmpire(pPlayer.getCivilizationType(), iKoun, pPlayer.getTeam(), pCity, pPlayer.getAlignment(), pPlayer)
	pSplitPlayer = cf.formEmpire(pPlayer.getCivilizationType(), iKoun, pPlayer.getTeam(), pCity, pPlayer.getAlignment(), pPlayer)

	## Globalcounter initialization
	cf.doGlobalcounterInitialization(pSplitPlayer.getID())

# Kaijin <<<

def doDissent1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	if gc.getGame().getSorenRandNum(100, "Dissent 1") < 50:
		pCity.changeOccupationTimer(2)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_DISSENT_1", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Actions/Pillage.dds', en.eColorRed, pCity.getX(), pCity.getY(), True, True)

def helpDissent1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_DISSENT_1_HELP", ())
	return szHelp

def doDissent2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	if gc.getGame().getSorenRandNum(100, "Dissent 2") < 50:
		pCity.changeOccupationTimer(4)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_DISSENT_2_BAD", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Actions/Pillage.dds', en.eColorRed, pCity.getX(), pCity.getY(), True, True)
	else:
		pCity.changeHappinessTimer(5)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_DISSENT_2_GOOD", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/General/happy_person.dds', en.eColorGreen, pCity.getX(), pCity.getY(), True, True)

def helpDissent2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_DISSENT_2_HELP", ())
	return szHelp

def canApplyDissent4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	if pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_CULTURAL_VALUES')) != gc.getInfoTypeForString('CIVIC_SOCIAL_ORDER'):
		return False
	return True

def applyExploreLairDepths1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pUnit = getUnit(kTriggeredData.ePlayer, kTriggeredData.iUnitId)
	if CyGame().getSorenRandNum(2, "Explore Lair") == 0:
		cf.exploreLairBigBad(pUnit)
	else:
		cf.exploreLairBigGood(pUnit)

def applyExploreLairDwarfVsLizardmen1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pUnit = getUnit(kTriggeredData.ePlayer, kTriggeredData.iUnitId)
	pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
	bBronze = False
	bPoison = False
	if pBarbarianPlayer.isHasTech(gc.getInfoTypeForString('TECH_BRONZE_WORKING')):
		bBronze = True
	if pBarbarianPlayer.isHasTech(gc.getInfoTypeForString('TECH_TRACKING')):
		bPoison = True
	pPlot = pUnit.plot()
	pNewPlot = cf.findClearPlot(-1, pPlot)
	if pNewPlot != -1:
		pNewUnit = pBarbarianPlayer.initUnit(gc.getInfoTypeForString('UNIT_LIZARDMAN'), pNewPlot.getX(), pNewPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit2 = pBarbarianPlayer.initUnit(gc.getInfoTypeForString('UNIT_LIZARDMAN'), pNewPlot.getX(), pNewPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit3 = pBarbarianPlayer.initUnit(gc.getInfoTypeForString('UNIT_LIZARDMAN'), pNewPlot.getX(), pNewPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		if bPoison:
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED_BLADE'), True)
			pNewUnit2.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED_BLADE'), True)
			pNewUnit3.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED_BLADE'), True)
		pPlayer = gc.getPlayer(ePlayer)
		pNewUnit4 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_AXEMAN'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit4.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DWARF'), True)
		pNewUnit5 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_AXEMAN'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit5.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DWARF'), True)
		if bBronze:
			pNewUnit4.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS'), True)
			pNewUnit5.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS'), True)

def applyExploreLairDwarfVsLizardmen2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pUnit = getUnit(kTriggeredData.ePlayer, kTriggeredData.iUnitId)
	pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
	bBronze = False
	bPoison = False
	if pBarbarianPlayer.isHasTech(gc.getInfoTypeForString('TECH_BRONZE_WORKING')):
		bBronze = True
	if pBarbarianPlayer.isHasTech(gc.getInfoTypeForString('TECH_TRACKING')):
		bPoison = True
	pPlot = pUnit.plot()
	pNewPlot = cf.findClearPlot(-1, pPlot)
	if pNewPlot != -1:
		pPlayer = gc.getPlayer(ePlayer)
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_LIZARDMAN'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit2 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_LIZARDMAN'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		if bPoison:
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED_BLADE'), True)
			pNewUnit2.setHasPromotion(gc.getInfoTypeForString('PROMOTION_POISONED_BLADE'), True)
		pNewUnit3 = pBarbarianPlayer.initUnit(gc.getInfoTypeForString('UNIT_AXEMAN'), pNewPlot.getX(), pNewPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit3.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DWARF'), True)
		pNewUnit4 = pBarbarianPlayer.initUnit(gc.getInfoTypeForString('UNIT_AXEMAN'), pNewPlot.getX(), pNewPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit4.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DWARF'), True)
		pNewUnit5 = pBarbarianPlayer.initUnit(gc.getInfoTypeForString('UNIT_AXEMAN'), pNewPlot.getX(), pNewPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit5.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DWARF'), True)
		if bBronze:
			pNewUnit3.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS'), True)
			pNewUnit4.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS'), True)
			pNewUnit5.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BRONZE_WEAPONS'), True)

def applyExploreLairPortal1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pUnit = getUnit(kTriggeredData.ePlayer, kTriggeredData.iUnitId)
	iBestValue = 0
	pBestPlot = -1
	for i in range (CyMap().numPlots()):
		iValue = 0
		pPlot = CyMap().plotByIndex(i)
		if not pPlot.isWater():
			if not pPlot.isPeak():
				if pPlot.getNumUnits() == 0:
					iValue = CyGame().getSorenRandNum(1000, "Portal")
					if not pPlot.isOwned():
						iValue += 1000
					if iValue > iBestValue:
						iBestValue = iValue
						pBestPlot = pPlot
	if pBestPlot != -1:
		pUnit.setXY(pBestPlot.getX(), pBestPlot.getY(), False, True, True)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_EXPLORE_LAIR_PORTAL",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Spells/Explore Lair.dds', en.eColorGreen, pBestPlot.getX(), pBestPlot.getY(), True, True)

def doFlareEntropyNode(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = CyMap().plot(kTriggeredData.iPlotX,kTriggeredData.iPlotY)
	point = pPlot.getPoint()
	CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPELL1'), point)
	CyAudioGame().Play3DSound("AS3D_SPELL_DEFILE", point.x, point.y, point.z)
	for iX in range(kTriggeredData.iPlotX-1, kTriggeredData.iPlotX+2, 1):
		for iY in range(kTriggeredData.iPlotY-1, kTriggeredData.iPlotY+2, 1):
			pPlot = CyMap().plot(iX,iY)
			if not pPlot.isNone():
				pPlot.setPlotCounter(100)
	CyGame().changeGlobalCounter(2)

def doFlareFireNode(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = CyMap().plot(kTriggeredData.iPlotX,kTriggeredData.iPlotY)
	point = pPlot.getPoint()
	CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_ARTILLERY_SHELL_EXPLODE'), point)
	CyAudioGame().Play3DSound("AS3D_UN_GRENADE_EXPLODE", point.x, point.y, point.z)
	for iX in range(kTriggeredData.iPlotX-1, kTriggeredData.iPlotX+2, 1):
		for iY in range(kTriggeredData.iPlotY-1, kTriggeredData.iPlotY+2, 1):
			pPlot = CyMap().plot(iX,iY)
			if not pPlot.isNone():
				if (pPlot.getFeatureType() == en.eFeatureForest or pPlot.getFeatureType() == en.eFeatureJungle):
					pPlot.setFeatureType(en.eFeatureFlames, 0)
					if pPlot.isOwned():
						CyInterface().addMessage(pPlot.getOwner(), False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_FLAMES", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Fire.dds', en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)

def doFlareLifeNode(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = CyMap().plot(kTriggeredData.iPlotX,kTriggeredData.iPlotY)
	point = pPlot.getPoint()
	CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPELL1'), point)
	CyAudioGame().Play3DSound("AS3D_SPELL_SANCTIFY", point.x, point.y, point.z)
	for iX in range(kTriggeredData.iPlotX-2, kTriggeredData.iPlotX+3, 1):
		for iY in range(kTriggeredData.iPlotY-2, kTriggeredData.iPlotY+3, 1):
			pPlot = CyMap().plot(iX,iY)
			if not pPlot.isNone():
				pPlot.setPlotCounter(0)
	CyGame().changeGlobalCounter(-2)

def doFlareNatureNode(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = CyMap().plot(kTriggeredData.iPlotX,kTriggeredData.iPlotY)
	point = pPlot.getPoint()
	CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_BLOOM'), point)
	CyAudioGame().Play3DSound("AS3D_SPELL_BLOOM", point.x, point.y, point.z)
	iForestNew = gc.getInfoTypeForString('FEATURE_FOREST_NEW')
	for iX in range(kTriggeredData.iPlotX-1, kTriggeredData.iPlotX+2, 1):
		for iY in range(kTriggeredData.iPlotY-1, kTriggeredData.iPlotY+2, 1):
			pPlot = CyMap().plot(iX,iY)
			if not pPlot.isNone():
##--------	Advanced Rules: Modified by Denev 2010/01/29
				"""
				if (pPlot.getImprovementType() == -1 and pPlot.getFeatureType() == -1 and not pPlot.isWater()):
					if not pPlot.isPeak():
				"""
				if pPlot.canHaveFeatureOnImprovement(iForestNew):
##--------	Advanced Rules: End Modify
						pPlot.setFeatureType(iForestNew, 0)

def doFlareWaterNode(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = CyMap().plot(kTriggeredData.iPlotX,kTriggeredData.iPlotY)
	point = pPlot.getPoint()
	CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPRING'), point)
	CyAudioGame().Play3DSound("AS3D_SPELL_SPRING", point.x, point.y, point.z)
	for iX in range(kTriggeredData.iPlotX-1, kTriggeredData.iPlotX+2, 1):
		for iY in range(kTriggeredData.iPlotY-1, kTriggeredData.iPlotY+2, 1):
			pPlot = CyMap().plot(iX,iY)
			if not pPlot.isNone():
				if pPlot.getTerrainType() == en.eTerrainDesert:
					pPlot.setTerrainType(en.eTerrainPlains, True, True)
				if pPlot.getFeatureType() == en.eFeatureFlames:
					pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
				if pPlot.getImprovementType() == en.eImprovementSmoke:
					pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)

def canTriggerPlotEmpty(argsList):
	ePlayer, kTriggeredData = argsList
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if pPlot.isNone():
		return False
	if pPlot.getNumUnits() > 0:
		return False
	return True

def canUnitTriggerFoodSickness(argsList):
	eTrigger, pUnit = argsList
	return pUnit.isAlive()

def doFoodSickness(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pUnit = getUnit(kTriggeredData.ePlayer, kTriggeredData.iUnitId)
	iDmg = min(99, pUnit.getDamage() + 20)
	pUnit.doDamage(20, 99, gc.getInfoTypeForString('DAMAGE_POISON'))
	pUnit.finishMoves()
	pUnit.changeImmobileTimer(1)

def doFrostling(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if not pPlot.isNone():
		eFrostlingPlayer = PlayerTypes.NO_PLAYER
		for ePlayer in range(gc.getMAX_CIV_PLAYERS(), gc.getMAX_PLAYERS()):
			if gc.getPlayer(ePlayer).getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_FROSTLING'):
				eFrostlingPlayer = ePlayer
				break
		if eFrostlingPlayer != PlayerTypes.NO_PLAYER:
			pBarbarianPlayer = gc.getPlayer(eFrostlingPlayer)
			pNewUnit = pBarbarianPlayer.initUnit(gc.getInfoTypeForString('UNIT_FROSTLING'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit.changeImmobileTimer(1)

def getHelpGoblinWaste(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	szHelp = localText.getText("TXT_KEY_SPELL_CHANGE_TERRAIN", (gc.getTerrainInfo(pPlot.getTerrainType()).getTextKey(), gc.getTerrainInfo(gc.getInfoTypeForString('TERRAIN_MARSH')).getTextKey()))
	return szHelp

def doGoblinWaste(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if not pPlot.isNone():
		pPlot.setTerrainType(gc.getInfoTypeForString('TERRAIN_MARSH'), True, True)

def doGodslayer(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
#	cf.placeTreasure(ePlayer, gc.getInfoTypeForString('EQUIPMENT_GODSLAYER'))
	cf.placeTreasure(ePlayer, gc.getInfoTypeForString('UNIT_GODSLAYER'))

def doGovernorAssassination(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	bMatch = False
	eCivic = pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_GOVERNMENT'))
	if eCivic != gc.getInfoTypeForString('CIVIC_DESPOTISM'):
		if eCivic == gc.getInfoTypeForString('CIVIC_GOD_KING'):
			bMatch = True
		elif eCivic == gc.getInfoTypeForString('CIVIC_ARISTOCRACY'):
			if eEvent == gc.getInfoTypeForString('EVENT_GOVERNOR_ASSASSINATION_1'):
				bMatch = True
		elif eCivic == gc.getInfoTypeForString('CIVIC_CITY_STATES') or eCivic == gc.getInfoTypeForString('CIVIC_REPUBLIC'):
			if eEvent == gc.getInfoTypeForString('EVENT_GOVERNOR_ASSASSINATION_3'):
				bMatch = True
		elif eCivic == gc.getInfoTypeForString('CIVIC_THEOCRACY'):
			if eEvent == gc.getInfoTypeForString('EVENT_GOVERNOR_ASSASSINATION_4'):
				bMatch = True
		iGameSpeedPercent = gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent()
		iTimer = cyFlatValue(12, iGameSpeedPercent, True)
		if bMatch:
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_PEOPLE_APPROVE", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/General/happy_person.dds', en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
			pCity.changeHappinessTimer(iTimer)
		else:
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_JUDGEMENT_WRONG", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/General/unhealthy_person.dds', en.eColorRed, pCity.getX(), pCity.getY(), True, True)
			pCity.changeHurryAngerTimer(iTimer)

def doGuildOfTheNineMerc41(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_MERCENARY'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ELF'), True)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WOODSMAN1'), True)
	pNewUnit2 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_LONGBOWMAN'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit2.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ELF'), True)
	pNewUnit2.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEXTEROUS'), True)
	pNewUnit3 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_RANGER'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit3.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DARK_ELF'), True)
	pNewUnit3.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SINISTER'), True)

	pNewUnit.finishMoves()
	pNewUnit2.finishMoves()
	pNewUnit3.finishMoves()

	pNewUnit.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_LJOSALFAR'))
	pNewUnit2.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_LJOSALFAR'))
	pNewUnit3.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_SVARTALFAR'))

def canCityTriggerGuildOfTheNineMerc5(argsList):
	eTrigger, pCity = argsList
	return pCity.isCoastal(10)

def doGuildOfTheNineMerc51(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_MERCENARY'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_AMPHIBIOUS'), True)
	pNewUnit2 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_BOARDING_PARTY'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit3 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_PRIVATEER'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit3.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HIDDEN_NATIONALITY'), True)

	pNewUnit.finishMoves()
	pNewUnit2.finishMoves()
	pNewUnit3.finishMoves()

	pNewUnit.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_LANUN'))
	pNewUnit2.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_LANUN'))
	pNewUnit3.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_LANUN'))

def doGuildOfTheNineMerc61(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_MERCENARY'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MUTATED'), True)
	pNewUnit2 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_TASKMASTER'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit3 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_HUNTER'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit3.setUnitArtStyleType(gc.getInfoTypeForString('UNIT_ARTSTYLE_BALSERAPHS'))

	pNewUnit.finishMoves()
	pNewUnit2.finishMoves()
	pNewUnit3.finishMoves()

	pNewUnit.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_BALSERAPHS'))
	pNewUnit2.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_BALSERAPHS'))
	pNewUnit3.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_BALSERAPHS'))

def doGuildOfTheNineMerc71(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_MERCENARY'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEFENSIVE'), True)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DWARF'), True)
	pNewUnit2 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_CHAMPION'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit2.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DWARF'), True)
	pNewUnit3 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_DWARVEN_CANNON'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

	pNewUnit.finishMoves()
	pNewUnit2.finishMoves()
	pNewUnit3.finishMoves()

	pNewUnit.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_KHAZAD'))
	pNewUnit2.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_KHAZAD'))
	pNewUnit3.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_KHAZAD'))

def doGuildOfTheNineMerc81(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_MERCENARY'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ORC'), True)
	pNewUnit2 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_OGRE'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit3 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_LIZARDMAN'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

	pNewUnit.finishMoves()
	pNewUnit2.finishMoves()
	pNewUnit3.finishMoves()

	pNewUnit.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_CLAN_OF_EMBERS'))
	pNewUnit2.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_CLAN_OF_EMBERS'))
	pNewUnit3.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_CLAN_OF_EMBERS'))

def doGreatBeastGurid(argsList):
	eUnit = gc.getInfoTypeForString('UNIT_GURID')
	if CyGame().getUnitCreatedCount(eUnit) == 0:
		pNewUnit = cf.addBarbarianUnit(eUnit, gc.getInfoTypeForString('BARBARIAN_ANIMAL'))
		if pNewUnit is not None:
			pNewUnit.changeImmobileTimer(1)

def doGreatBeastLeviathan(argsList):
	eUnit = gc.getInfoTypeForString('UNIT_LEVIATHAN')
	if CyGame().getUnitCreatedCount(eUnit) == 0:
		pBestPlot = -1
		iBestPlot = -1
		for i in range (CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(i)
			iPlot = -1
			if pPlot.isWater():
				if pPlot.getNumUnits() == 0:
					iPlot = CyGame().getSorenRandNum(500, "Leviathan")
					iPlot = iPlot + (pPlot.area().getNumTiles() * 10)
			if iPlot > iBestPlot:
				iBestPlot = iPlot
				pBestPlot = pPlot
		if iBestPlot != -1:
#			pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
			pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER() + en.eBarbarianAnimal)
			pNewUnit = pBarbarianPlayer.initUnit(eUnit, pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

def doGreatBeastMargalard(argsList):
	eUnit = gc.getInfoTypeForString('UNIT_MARGALARD')
	if CyGame().getUnitCreatedCount(eUnit) == 0:
		pNewUnit = cf.addBarbarianUnit(eUnit, gc.getInfoTypeForString('BARBARIAN_ANIMAL'))
		if pNewUnit is not None:
			pNewUnit.changeImmobileTimer(1)

def applyHyboremsWhisper1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = cf.getAshenVeilCity(1)
	pPlayer.acquireCity(pCity, False, False)

def helpHyboremsWhisper1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = cf.getAshenVeilCity(1)
	szHelp = localText.getText("TXT_KEY_EVENT_HYBOREMS_WHISPER_HELP", (pCity.getName(), ))
	return szHelp

def applyHyboremsWhisper2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = cf.getAshenVeilCity(2)
	pPlayer.acquireCity(pCity, False, False)

def helpHyboremsWhisper2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = cf.getAshenVeilCity(2)
	szHelp = localText.getText("TXT_KEY_EVENT_HYBOREMS_WHISPER_HELP", (pCity.getName(), ))
	return szHelp

def applyHyboremsWhisper3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = cf.getAshenVeilCity(3)
	pPlayer.acquireCity(pCity, False, False)

def helpHyboremsWhisper3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = cf.getAshenVeilCity(3)
	szHelp = localText.getText("TXT_KEY_EVENT_HYBOREMS_WHISPER_HELP", (pCity.getName(), ))
	return szHelp

def applyIronOrb3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	szBuffer = localText.getText("TXT_KEY_EVENT_IRON_ORB_3_RESULT", ())
	pPlayer.chooseTech(1, szBuffer, True)

def doJudgementRight(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_JUDGEMENT_RIGHT", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/General/happy_person.dds', en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
	pCity.changeHappinessTimer(10)

def doJudgementWrong(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_JUDGEMENT_WRONG", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/General/unhealthy_person.dds', en.eColorRed, pCity.getX(), pCity.getY(), True, True)
	pCity.changeCrime(3)

def doLetumFrigus3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
##--------	Advanced Rules: Modified by Denev
#	pPlayer.setHasTrait(gc.getInfoTypeForString('TRAIT_AGGRESSIVE'), True)
# Kaijin >>>
#	pPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_AGGRESSIVE'), True, TraitSourceTypes.TRAITSOURCE_RANDOM_EVENT)
	if not pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_SPIRITUAL')):
		pPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_SPIRITUAL'), True, TraitSourceTypes.TRAITSOURCE_RANDOM_EVENT)
	else:
		leTrait = [eTrait for eTrait in range(gc.getNumTraitInfos()) if gc.getTraitInfo(eTrait).isSelectable() and not pPlayer.hasTrait(eTrait)]
		liChosenTrait = []
		liChosenTrait.append(leTrait.pop( CyGame().getSorenRandNum(len(leTrait), "LetumFrigus") ))
		liChosenTrait.sort()
		for iChosenTrait in liChosenTrait:
			pPlayer.setHasTraitWithSource(iChosenTrait, True, TraitSourceTypes.TRAITSOURCE_RANDOM_EVENT)
# Kaijin <<<
##--------	Advanced Rules: End Modify

def helpLetumFrigus3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_LETUM_FRIGUS_3_HELP_OAC", ())
	return szHelp

def canCityTriggerLunatic(argsList):
	eTrigger, pCity = argsList
	eReligion = gc.getPlayer(pCity.getOwner()).getStateReligion()
	eTemple = BuildingTypes.NO_BUILDING
	if eReligion == gc.getInfoTypeForString('RELIGION_THE_ORDER'):
		eTemple = gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_ORDER')
	elif eReligion == gc.getInfoTypeForString('RELIGION_FELLOWSHIP_OF_LEAVES'):
		eTemple = gc.getInfoTypeForString('BUILDING_TEMPLE_OF_LEAVES')
	elif eReligion == gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL'):
		eTemple = gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_VEIL')
	elif eReligion == gc.getInfoTypeForString('RELIGION_OCTOPUS_OVERLORDS'):
		eTemple = gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_OVERLORDS')
	elif eReligion == gc.getInfoTypeForString('RELIGION_RUNES_OF_KILMORPH'):
		eTemple = gc.getInfoTypeForString('BUILDING_TEMPLE_OF_KILMORPH')
	elif eReligion == gc.getInfoTypeForString('RELIGION_THE_EMPYREAN'):
		eTemple = gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_EMPYREAN')
	if eTemple == BuildingTypes.NO_BUILDING:
		return False
	if pCity.getNumRealBuilding(eTemple) == 0:
		return False
	return True

def doMachineParts1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_CLOCKWORK_GOLEM'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAK'), True)

def doMachineParts2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_CLOCKWORK_GOLEM'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STRONG'), True)

def applyMalakimPilgrimage1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pUnit = getUnit(kTriggeredData.ePlayer, kTriggeredData.iUnitId)
	eMalakimPlayer = cf.getCivilization(gc.getInfoTypeForString('CIVILIZATION_MALAKIM'))
	if eMalakimPlayer != PlayerTypes.NO_PLAYER:
		pMalakimPlayer = gc.getPlayer(eMalakimPlayer)
		pCity = pMalakimPlayer.getCapitalCity()
		pUnit.setXY(pCity.getX(), pCity.getY(), False, True, True)

def doMarketTheft2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	iRnd = gc.getGame().getSorenRandNum(20, "Market Theft 2") - 10
	pCity.changeCrime(iRnd)

def helpMarketTheft2(argsList):
	szHelp = localText.getText("TXT_KEY_EVENT_MARKET_THEFT_2_HELP", ())
	return szHelp

def canCityTriggerMerchantKeep(argsList):
	eTrigger, pCity = argsList
	return pCity.getSpecialistCount(gc.getInfoTypeForString('SPECIALIST_GREAT_MERCHANT')) != 0

def doMistforms(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
	eMistform = gc.getInfoTypeForString('UNIT_MISTFORM')
	pNewUnit1 = pBarbarianPlayer.initUnit(eMistform, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit2 = pBarbarianPlayer.initUnit(eMistform, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit3 = pBarbarianPlayer.initUnit(eMistform, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit1.changeImmobileTimer(1)
	pNewUnit2.changeImmobileTimer(1)
	pNewUnit3.changeImmobileTimer(1)

def doMushrooms(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
# Kaijin OAC >>>
#	pPlot.setImprovementType(gc.getInfoTypeForString('IMPROVEMENT_MUSHROOMS'))
	pPlot.setBonusType(gc.getInfoTypeForString('BONUS_MUSHROOMS'))
# Kaijin OAC <<<

def canUnitTriggerMutate(argsList):
	eTrigger, pUnit = argsList
	return not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MUTATED'))

def canApplyNoOrder(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	if pPlayer.getStateReligion() == gc.getInfoTypeForString('RELIGION_THE_ORDER'):
		return False
	return True

def doOrderVsVeil1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pCity.changeOccupationTimer(1)
	iOrder = gc.getInfoTypeForString('RELIGION_THE_ORDER')
	iVeil = gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL')
	if not pCity.isHolyCityByType(iVeil):
		if gc.getGame().getSorenRandNum(100, "Order vs Veil 1") < 50:
			pCity.setHasReligion(iVeil, False, False, False)
	(loopCity, iter) = pPlayer.firstCity(False)
	while(loopCity):
		if loopCity.isHasReligion(iOrder):
			loopCity.changeHappinessTimer(5)
		if loopCity.isHasReligion(iVeil):
			loopCity.changeHurryAngerTimer(5)
		(loopCity, iter) = pPlayer.nextCity(iter, False)

def doOrderVsVeil2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pCity.changeOccupationTimer(1)
	iOrder = gc.getInfoTypeForString('RELIGION_THE_ORDER')
	iVeil = gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL')
	if not pCity.isHolyCityByType(iOrder):
		if gc.getGame().getSorenRandNum(100, "Order vs Veil 2") < 50:
			pCity.setHasReligion(iOrder, False, False, False)
	(loopCity, iter) = pPlayer.firstCity(False)
	while(loopCity):
		if loopCity.isHasReligion(iVeil):
			loopCity.changeHappinessTimer(5)
		if loopCity.isHasReligion(iOrder):
			loopCity.changeHurryAngerTimer(5)
		(loopCity, iter) = pPlayer.nextCity(iter, False)

def doOrderVsVeil3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pCity.changeOccupationTimer(3)
	iOrder = gc.getInfoTypeForString('RELIGION_THE_ORDER')
	iVeil = gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL')
	if not pCity.isHolyCityByType(iVeil):
		if gc.getGame().getSorenRandNum(100, "Order vs Veil 3") < 25:
			pCity.setHasReligion(iVeil, False, False, False)
	if not pCity.isHolyCityByType(iOrder):
		if gc.getGame().getSorenRandNum(100, "Order vs Veil 3") < 25:
			pCity.setHasReligion(iOrder, False, False, False)
	if gc.getGame().getSorenRandNum(100, "Order vs Veil 3") < 50:
		pCity.changePopulation(-1)

def canApplyOrderVsVeil4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	if pCity.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_DUNGEON')) == 0:
		return False
	return True

def helpOrderVsVeil1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_ORDER_VS_VEIL_1_HELP", ())
	return szHelp

def helpOrderVsVeil2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_ORDER_VS_VEIL_2_HELP", ())
	return szHelp

def helpOrderVsVeil3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_ORDER_VS_VEIL_3_HELP", ())
	return szHelp

def doOrderVsVeilTemple1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pCity.changeOccupationTimer(1)
	iOrder = gc.getInfoTypeForString('RELIGION_THE_ORDER')
	iVeil = gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL')
	pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_VEIL'), 0)
	if not pCity.isHolyCityByType(iVeil):
		if gc.getGame().getSorenRandNum(100, "Order vs Veil Temple 1") < 50:
			pCity.setHasReligion(iVeil, False, False, False)
	(loopCity, iter) = pPlayer.firstCity(False)
	while(loopCity):
		if loopCity.isHasReligion(iOrder):
			loopCity.changeHappinessTimer(5)
		if loopCity.isHasReligion(iVeil):
			loopCity.changeHurryAngerTimer(5)
		(loopCity, iter) = pPlayer.nextCity(iter, False)

def doOrderVsVeilTemple2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pCity.changeOccupationTimer(1)
	iVeil = gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL')
	if gc.getGame().getSorenRandNum(100, "Order vs Veil Temple 2") < 50:
		pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_VEIL'), 0)
	if not pCity.isHolyCityByType(iVeil):
		if gc.getGame().getSorenRandNum(100, "Order vs Veil Temple 2") < 50:
			pCity.setHasReligion(iVeil, False, False, False)
	if gc.getGame().getSorenRandNum(100, "Order vs Veil Temple 2") < 50:
		pCity.changePopulation(-1)

def doOrderVsVeilTemple3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pCity.changeOccupationTimer(3)
	iOrder = gc.getInfoTypeForString('RELIGION_THE_ORDER')
	iVeil = gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL')
	(loopCity, iter) = pPlayer.firstCity(False)
	while(loopCity):
		if loopCity.isHasReligion(iVeil):
			loopCity.changeHappinessTimer(5)
		if loopCity.isHasReligion(iOrder):
			loopCity.changeHurryAngerTimer(5)
		(loopCity, iter) = pPlayer.nextCity(iter, False)

def helpOrderVsVeilTemple1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_ORDER_VS_VEIL_TEMPLE_1_HELP", ())
	return szHelp

def helpOrderVsVeilTemple2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_ORDER_VS_VEIL_TEMPLE_2_HELP", ())
	return szHelp

def helpOrderVsVeilTemple3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_ORDER_VS_VEIL_TEMPLE_3_HELP", ())
	return szHelp

def canTriggerParith(argsList):
	ePlayer, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	if not pPlayer.isHuman():
		return False
	if CyGame().getTrophyValue("TROPHY_WB_SPLINTERED_COURT_PARITH") != 1:
		return False
	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_WB_THE_SPLINTERED_COURT):
		return False
	return True

def applyParithYes(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pUnit = getUnit(kTriggeredData.ePlayer, kTriggeredData.iUnitId)
	CyGame().setTrophyValue("TROPHY_WB_SPLINTERED_COURT_PARITH", pUnit.getUnitType())

def canTriggerPenguins(argsList):
	ePlayer, kTriggeredData = argsList
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if not pPlot.isAdjacentToWater():
		return False
	if pPlot.isPeak():
		return False
	return True

def doPenguins(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	pPlot.setImprovementType(gc.getInfoTypeForString('IMPROVEMENT_PENGUINS'))

def canTriggerPickAlignment(argsList):
	ePlayer, kTriggeredData = argsList
	if CyGame().getWBMapScript():
		return False
	return True

def doPickAlignment1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pPlayer.setAlignment(gc.getInfoTypeForString('ALIGNMENT_GOOD'))

def doPickAlignment2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pPlayer.setAlignment(gc.getInfoTypeForString('ALIGNMENT_NEUTRAL'))

def doPickAlignment3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pPlayer.setAlignment(gc.getInfoTypeForString('ALIGNMENT_EVIL'))

def doPigGiant3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pPlot = cf.findClearPlot(-1, pCity.plot())
	if pPlot != -1:
		pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
		pNewUnit = pBarbarianPlayer.initUnit(gc.getInfoTypeForString('UNIT_HILL_GIANT'), pPlot.getX(), pPlot.getY(), UnitAITypes.UNITAI_ATTACK_CITY, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_COMMANDO'), True)
		pNewUnit.changeImmobileTimer(1)

def applyPronCapria(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_CAPRIA'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		pPronPlayer = gc.getPlayer(ePronPlayer)
		pPronPlayer.AI_changeAttitudeExtra(ePlayer, 4)
		cf.addPlayerPopup(CyTranslator().getText("TXT_KEY_EVENT_PRON_CAPRIA_POPUP",()), ePlayer)

def canTriggerPronCapria(argsList):
	ePlayer, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_CAPRIA'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		eTeam = gc.getPlayer(ePlayer).getTeam()
		pTeam = gc.getTeam(eTeam)
		pPronPlayer = gc.getPlayer(ePronPlayer)
		ePronTeam = pPronPlayer.getTeam()
		if pTeam.isHasMet(ePronTeam):
			if pPronPlayer.AI_getAttitude(ePlayer) == gc.getInfoTypeForString('ATTITUDE_FRIENDLY'):
				return True
	return False

def applyPronEthne(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_ETHNE'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		pPronPlayer = gc.getPlayer(ePronPlayer)
		pPronPlayer.AI_changeAttitudeExtra(ePlayer, 4)
		cf.addPlayerPopup(CyTranslator().getText("TXT_KEY_EVENT_PRON_ETHNE_POPUP",()), ePlayer)

def canTriggerPronEthne(argsList):
	ePlayer, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_ETHNE'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		eTeam = gc.getPlayer(ePlayer).getTeam()
		pTeam = gc.getTeam(eTeam)
		pPronPlayer = gc.getPlayer(ePronPlayer)
		ePronTeam = pPronPlayer.getTeam()
		if pTeam.isHasMet(ePronTeam):
			if pPronPlayer.AI_getAttitude(ePlayer) == gc.getInfoTypeForString('ATTITUDE_FRIENDLY'):
				return True
	return False

def applyPronArendel(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_ARENDEL'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		pPronPlayer = gc.getPlayer(ePronPlayer)
		pPronPlayer.AI_changeAttitudeExtra(ePlayer, 4)
		cf.addPlayerPopup(CyTranslator().getText("TXT_KEY_EVENT_PRON_ARENDEL_POPUP",()), ePlayer)

def canTriggerPronArendel(argsList):
	ePlayer, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_ARENDEL'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		eTeam = gc.getPlayer(ePlayer).getTeam()
		pTeam = gc.getTeam(eTeam)
		pPronPlayer = gc.getPlayer(ePronPlayer)
		ePronTeam = pPronPlayer.getTeam()
		if pTeam.isHasMet(ePronTeam):
			if pPronPlayer.AI_getAttitude(ePlayer) == gc.getInfoTypeForString('ATTITUDE_FRIENDLY'):
				return True
	return False

def applyPronThessa(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_THESSA'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		pPronPlayer = gc.getPlayer(ePronPlayer)
		pPronPlayer.AI_changeAttitudeExtra(ePlayer, 4)
		cf.addPlayerPopup(CyTranslator().getText("TXT_KEY_EVENT_PRON_THESSA_POPUP",()), ePlayer)

def canTriggerPronThessa(argsList):
	ePlayer, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_THESSA'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		eTeam = gc.getPlayer(ePlayer).getTeam()
		pTeam = gc.getTeam(eTeam)
		pPronPlayer = gc.getPlayer(ePronPlayer)
		ePronTeam = pPronPlayer.getTeam()
		if pTeam.isHasMet(ePronTeam):
			if pPronPlayer.AI_getAttitude(ePlayer) == gc.getInfoTypeForString('ATTITUDE_FRIENDLY'):
				return True
	return False

def applyPronHannah(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_HANNAH'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		pPronPlayer = gc.getPlayer(ePronPlayer)
		pPronPlayer.AI_changeAttitudeExtra(ePlayer, 4)
		cf.addPlayerPopup(CyTranslator().getText("TXT_KEY_EVENT_PRON_HANNAH_POPUP",()), ePlayer)

def canTriggerPronHannah(argsList):
	ePlayer, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_HANNAH'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		eTeam = gc.getPlayer(ePlayer).getTeam()
		pTeam = gc.getTeam(eTeam)
		pPronPlayer = gc.getPlayer(ePronPlayer)
		ePronTeam = pPronPlayer.getTeam()
		if pTeam.isHasMet(ePronTeam):
			if pPronPlayer.AI_getAttitude(ePlayer) == gc.getInfoTypeForString('ATTITUDE_FRIENDLY'):
				return True
	return False

def applyPronRhoanna(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_RHOANNA'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		pPronPlayer = gc.getPlayer(ePronPlayer)
		pPronPlayer.AI_changeAttitudeExtra(ePlayer, 4)
		cf.addPlayerPopup(CyTranslator().getText("TXT_KEY_EVENT_PRON_RHOANNA_POPUP",()), ePlayer)

def canTriggerPronRhoanna(argsList):
	ePlayer, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_RHOANNA'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		eTeam = gc.getPlayer(ePlayer).getTeam()
		pTeam = gc.getTeam(eTeam)
		pPronPlayer = gc.getPlayer(ePronPlayer)
		ePronTeam = pPronPlayer.getTeam()
		if pTeam.isHasMet(ePronTeam):
			if pPronPlayer.AI_getAttitude(ePlayer) == gc.getInfoTypeForString('ATTITUDE_FRIENDLY'):
				return True
	return False

def applyPronValledia(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_VALLEDIA'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		pPronPlayer = gc.getPlayer(ePronPlayer)
		pPronPlayer.AI_changeAttitudeExtra(ePlayer, 4)
		cf.addPlayerPopup(CyTranslator().getText("TXT_KEY_EVENT_PRON_VALLEDIA_POPUP",()), ePlayer)

def canTriggerPronValledia(argsList):
	ePlayer, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_VALLEDIA'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		eTeam = gc.getPlayer(ePlayer).getTeam()
		pTeam = gc.getTeam(eTeam)
		pPronPlayer = gc.getPlayer(ePronPlayer)
		ePronTeam = pPronPlayer.getTeam()
		if pTeam.isHasMet(ePronTeam):
			if pPronPlayer.AI_getAttitude(ePlayer) == gc.getInfoTypeForString('ATTITUDE_FRIENDLY'):
				return True
	return False

def applyPronMahala(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_MAHALA'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		pPronPlayer = gc.getPlayer(ePronPlayer)
		pPronPlayer.AI_changeAttitudeExtra(ePlayer, 4)
		cf.addPlayerPopup(CyTranslator().getText("TXT_KEY_EVENT_PRON_MAHALA_POPUP",()), ePlayer)

def canTriggerPronMahala(argsList):
	ePlayer, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_MAHALA'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		eTeam = gc.getPlayer(ePlayer).getTeam()
		pTeam = gc.getTeam(eTeam)
		pPronPlayer = gc.getPlayer(ePronPlayer)
		ePronTeam = pPronPlayer.getTeam()
		if pTeam.isHasMet(ePronTeam):
			if pPronPlayer.AI_getAttitude(ePlayer) == gc.getInfoTypeForString('ATTITUDE_FRIENDLY'):
				return True
	return False

def applyPronKeelyn(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_KEELYN'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		pPronPlayer = gc.getPlayer(ePronPlayer)
		pPronPlayer.AI_changeAttitudeExtra(ePlayer, 4)
		cf.addPlayerPopup(CyTranslator().getText("TXT_KEY_EVENT_PRON_KEELYN_POPUP",()), ePlayer)

def canTriggerPronKeelyn(argsList):
	ePlayer, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_KEELYN'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		eTeam = gc.getPlayer(ePlayer).getTeam()
		pTeam = gc.getTeam(eTeam)
		pPronPlayer = gc.getPlayer(ePronPlayer)
		ePronTeam = pPronPlayer.getTeam()
		if pTeam.isHasMet(ePronTeam):
			if pPronPlayer.AI_getAttitude(ePlayer) == gc.getInfoTypeForString('ATTITUDE_FRIENDLY'):
				return True
	return False

def applyPronSheelba(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_SHEELBA'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		pPronPlayer = gc.getPlayer(ePronPlayer)
		pPronPlayer.AI_changeAttitudeExtra(ePlayer, 4)
		cf.addPlayerPopup(CyTranslator().getText("TXT_KEY_EVENT_PRON_SHEELBA_POPUP",()), ePlayer)

def canTriggerPronSheelba(argsList):
	ePlayer, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_SHEELBA'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		eTeam = gc.getPlayer(ePlayer).getTeam()
		pTeam = gc.getTeam(eTeam)
		pPronPlayer = gc.getPlayer(ePronPlayer)
		ePronTeam = pPronPlayer.getTeam()
		if pTeam.isHasMet(ePronTeam):
			if pPronPlayer.AI_getAttitude(ePlayer) == gc.getInfoTypeForString('ATTITUDE_FRIENDLY'):
				return True
	return False

def applyPronFaeryl(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_FAERYL'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		pPronPlayer = gc.getPlayer(ePronPlayer)
		pPronPlayer.AI_changeAttitudeExtra(ePlayer, 4)
		cf.addPlayerPopup(CyTranslator().getText("TXT_KEY_EVENT_PRON_FAERYL_POPUP",()), ePlayer)

def canTriggerPronFaeryl(argsList):
	ePlayer, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_FAERYL'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		eTeam = gc.getPlayer(ePlayer).getTeam()
		pTeam = gc.getTeam(eTeam)
		pPronPlayer = gc.getPlayer(ePronPlayer)
		ePronTeam = pPronPlayer.getTeam()
		if pTeam.isHasMet(ePronTeam):
			if pPronPlayer.AI_getAttitude(ePlayer) == gc.getInfoTypeForString('ATTITUDE_FRIENDLY'):
				return True
	return False

def applyPronAlexis(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_ALEXIS'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		pPronPlayer = gc.getPlayer(ePronPlayer)
		pPronPlayer.AI_changeAttitudeExtra(ePlayer, 4)
		cf.addPlayerPopup(CyTranslator().getText("TXT_KEY_EVENT_PRON_ALEXIS_POPUP",()), ePlayer)

def canTriggerPronAlexis(argsList):
	ePlayer, kTriggeredData = argsList
	ePronPlayer = cf.getLeader(gc.getInfoTypeForString('LEADER_ALEXIS'))
	if ePronPlayer != PlayerTypes.NO_PLAYER:
		eTeam = gc.getPlayer(ePlayer).getTeam()
		pTeam = gc.getTeam(eTeam)
		pPronPlayer = gc.getPlayer(ePronPlayer)
		ePronTeam = pPronPlayer.getTeam()
		if pTeam.isHasMet(ePronTeam):
			if pPronPlayer.AI_getAttitude(ePlayer) == gc.getInfoTypeForString('ATTITUDE_FRIENDLY'):
				return True
	return False

def canTriggerUniqueFeatureAifonIsle(argsList):
	ePlayer, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	if not pPlayer.isHuman():
		return False
	iImp = gc.getInfoTypeForString('IMPROVEMENT_AIFON_ISLE')
	for i in range(CyMap().getNumAreas()):
		if CyMap().getArea(i).getNumImprovements(iImp) > 0:
			return True
	return False

def canTriggerUniqueFeatureBradelinesWell(argsList):
	ePlayer, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	if not pPlayer.isHuman():
		return False
	iImp = gc.getInfoTypeForString('IMPROVEMENT_BRADELINES_WELL')
	for i in range(CyMap().getNumAreas()):
		if CyMap().getArea(i).getNumImprovements(iImp) > 0:
			return True
	return False

def canTriggerUniqueFeatureBrokenSepulcher(argsList):
	ePlayer, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	if not pPlayer.isHuman():
		return False
	iImp = gc.getInfoTypeForString('IMPROVEMENT_BROKEN_SEPULCHER')
	for i in range(CyMap().getNumAreas()):
		if CyMap().getArea(i).getNumImprovements(iImp) > 0:
			return True
	return False

def canTriggerUniqueFeatureGuardian(argsList):
	ePlayer, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	if not pPlayer.isHuman():
		return False
	iImp = gc.getInfoTypeForString('IMPROVEMENT_GUARDIAN')
	for i in range(CyMap().getNumAreas()):
		if CyMap().getArea(i).getNumImprovements(iImp) > 0:
			return True
	return False

def canTriggerUniqueFeatureLetumFrigus(argsList):
	ePlayer, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	if not pPlayer.isHuman():
		return False
	if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ILLIANS'):
		return False
	iImp = gc.getInfoTypeForString('IMPROVEMENT_LETUM_FRIGUS')
	for i in range(CyMap().getNumAreas()):
		if CyMap().getArea(i).getNumImprovements(iImp) > 0:
			return True
	return False

def canTriggerUniqueFeatureLetumFrigusIllians(argsList):
	ePlayer, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	if not pPlayer.isHuman():
		return False
	iImp = gc.getInfoTypeForString('IMPROVEMENT_LETUM_FRIGUS')
	for i in range(CyMap().getNumAreas()):
		if CyMap().getArea(i).getNumImprovements(iImp) > 0:
			return True
	return False

def canTriggerUniqueFeaturePyreOfTheSeraphic(argsList):
	ePlayer, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	if not pPlayer.isHuman():
		return False
	if pPlayer.getAlignment() == gc.getInfoTypeForString('ALIGNMENT_EVIL'):
		return False
	iImp = gc.getInfoTypeForString('IMPROVEMENT_PYRE_OF_THE_SERAPHIC')
	for i in range(CyMap().getNumAreas()):
		if CyMap().getArea(i).getNumImprovements(iImp) > 0:
			return True
	return False

def canCityTriggerSageKeep(argsList):
	eTrigger, pCity = argsList
	return pCity.getSpecialistCount(gc.getInfoTypeForString('SPECIALIST_GREAT_SCIENTIST')) != 0

def doSailorsDirge(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	eUnit = gc.getInfoTypeForString('UNIT_SAILORS_DIRGE')
	if CyGame().getUnitCreatedCount(eUnit) == 0:
		pBestPlot = -1
		iBestPlot = -1
		for i in range (CyMap().numPlots()):
			pPlot = CyMap().plotByIndex(i)
			iPlot = -1
			if pPlot.isWater():
				if pPlot.getNumUnits() == 0:
					iPlot = CyGame().getSorenRandNum(500, "Sailors Dirge")
					iPlot = iPlot + (pPlot.area().getNumTiles() * 10)
					if pPlot.isOwned():
						iPlot = iPlot / 2
					if iPlot > iBestPlot:
						iBestPlot = iPlot
						pBestPlot = pPlot
		if iBestPlot != -1:
			"""
			pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
			pNewUnit = pBarbarianPlayer.initUnit(eUnit, pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			iSkeleton = gc.getInfoTypeForString('UNIT_SKELETON')
			pBarbarianPlayer.initUnit(iSkeleton, pNewUnit.getX(), pNewUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pBarbarianPlayer.initUnit(iSkeleton, pNewUnit.getX(), pNewUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pBarbarianPlayer.initUnit(iSkeleton, pNewUnit.getX(), pNewUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			"""
			pUndeadPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER() + gc.getInfoTypeForString('BARBARIAN_UNDEAD'))
			pNewUnit = pUndeadPlayer.initUnit(eUnit, pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

			cf.spawnSailorsDirgeCrew(pNewUnit)
"""
def doSailorsDirgeDefeated(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
#	cf.placeTreasure(ePlayer, gc.getInfoTypeForString('EQUIPMENT_TREASURE'))
	cf.placeTreasure(ePlayer, gc.getInfoTypeForString('UNIT_TREASURE'))
"""
def applyShrineCamulos2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	if CyGame().getSorenRandNum(100, "Shrine Camulos") < 10:
		pPlot = cf.findClearPlot(-1, pCity.plot())
		if pPlot != -1:
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_SHRINE_CAMULOS",()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Units/Pit Beast.dds', en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
#			pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
			pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER() + en.eBarbarianDemons)
			pNewUnit = pBarbarianPlayer.initUnit(gc.getInfoTypeForString('UNIT_PIT_BEAST'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit.attack(pCity.plot(), False)

def doSignAeron(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	CyGame().changeGlobalCounter(3)

def doSignBhall(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	for i in range (CyMap().numPlots()):
		pPlot = CyMap().plotByIndex(i)
		if pPlot.getOwner() == ePlayer:
			if pPlot.isColdCounter():
				iGameSpeedPercent = gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent()
				iThawTurns = cyFlatValue(24, iGameSpeedPercent, True)
				pPlot.doThawColdCounter(iThawTurns)
			elif pPlot.getFeatureType() == FeatureTypes.NO_FEATURE:
				if pPlot.getImprovementType() == ImprovementTypes.NO_IMPROVEMENT:
					if not pPlot.isWater():
						if CyGame().getSorenRandNum(100, "SignBhall") < 10:
							eTerrain = pPlot.getTerrainType()
							if eTerrain == en.eTerrainSnow:
								pPlot.setTempTerrainType(en.eTerrainTundra, CyGame().getSorenRandNum(10, "Bob") + 10)
							elif eTerrain == en.eTerrainTundra:
								pPlot.setTempTerrainType(en.eTerrainGrass, CyGame().getSorenRandNum(10, "Bob") + 10)
							elif eTerrain == en.eTerrainGrass:
								pPlot.setTempTerrainType(en.eTerrainPlains, CyGame().getSorenRandNum(10, "Bob") + 10)
							elif eTerrain == en.eTerrainPlains:
								pPlot.setTempTerrainType(en.eTerrainDesert, CyGame().getSorenRandNum(10, "Bob") + 10)

def doSignCamulos(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	for eLoopPlayer in range(gc.getMAX_CIV_PLAYERS()):
		loopPlayer = gc.getPlayer(eLoopPlayer)
		if loopPlayer.isAlive():
			if loopPlayer.getTeam() != pPlayer.getTeam():
				loopPlayer.AI_changeAttitudeExtra(ePlayer, -1)
				pPlayer.AI_changeAttitudeExtra(eLoopPlayer, -1)

def doSignDagda(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	for eLoopPlayer in range(gc.getMAX_CIV_PLAYERS()):
		loopPlayer = gc.getPlayer(eLoopPlayer)
		if loopPlayer.isAlive():
			if loopPlayer.getTeam() != pPlayer.getTeam():
				loopPlayer.AI_changeAttitudeExtra(ePlayer, 1)
				pPlayer.AI_changeAttitudeExtra(eLoopPlayer, 1)

def doSignEsus(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	CyGame().changeCrime(5)

def doSignLugus(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	CyGame().changeCrime(-5)

def doSignMulcarn(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	for i in range (CyMap().numPlots()):
		pPlot = CyMap().plotByIndex(i)
		if pPlot.getOwner() == ePlayer:
			if pPlot.getFeatureType() == -1:
				if pPlot.getImprovementType() == -1:
					if not pPlot.isWater():
						iRnd = CyGame().getSorenRandNum(3000, "SignMulcarn")
						if iRnd < 300:
							pPlot.ceilColdCounter(3000 + iRnd, -1)

def doSignSirona(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	CyGame().changeGlobalCounter(-3)

def doSignSucellus(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	eDiseased = gc.getInfoTypeForString('PROMOTION_DISEASED')
	for pUnit in PyPlayer(ePlayer).getUnitList():
##--------	Advanced Rules: Modified by Denev 2011/01/28
		"""
		if pUnit.isHasPromotion(eDiseased):
			pUnit.setHasPromotion(eDiseased, False)
			CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_POOL_OF_TEARS_DISEASED",()), 'AS2D_FEATUREGROWTH', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Spells/Curedisease.dds', en.eColorGreen, pUnit.getX(), pUnit.getY(), True, True)
		if pUnit.getDamage() > 0:
			pUnit.setDamage(pUnit.getDamage() / 2, PlayerTypes.NO_PLAYER)
			CyInterface().addMessage(ePlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_UNIT_HEALED",()), 'AS2D_FEATUREGROWTH', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Spells/Heal.dds', en.eColorGreen, pUnit.getX(), pUnit.getY(), True, True)
		"""
		leCuredPromotions = []
		iHealAmount = False
		if pUnit.getDamage() > 0:
			iHealAmount = pUnit.getDamage() // 2
			pUnit.setDamage(pUnit.getDamage() - iHealAmount, PlayerTypes.NO_PLAYER)
			kSpellHeal = gc.getSpellInfo(gc.getInfoTypeForString('SPELL_HEAL'))
			szSound = kSpellHeal.getSound()
			szButton = kSpellHeal.getButton()
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_UNIT_WAS_HEALED", (pUnit.getNameKey(), iHealAmount)), szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pUnit.getX(), pUnit.getY(), True, True)
		if pUnit.isHasPromotion(eDiseased):
			pUnit.setHasPromotion(eDiseased, False)
			leCuredPromotions.append(eDiseased)
		if len(leCuredPromotions) > 0:
			kSpellCureDisease = gc.getSpellInfo(gc.getInfoTypeForString('SPELL_CURE_DISEASE'))
			szSound = kSpellCureDisease.getSound()
			szButton = kSpellCureDisease.getButton()
			for eCuredPromotion in leCuredPromotions:
				szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_UNIT_WAS_CURED", (pUnit.getNameKey(), gc.getPromotionInfo(eCuredPromotion).getTextKey()))
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), szMessage, szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pUnit.getX(), pUnit.getY(), True, True)
##--------	Advanced Rules: End Modify

def doSignTali(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	for i in range (CyMap().numPlots()):
		pPlot = CyMap().plotByIndex(i)
		if pPlot.getOwner() == ePlayer:
			if pPlot.getFeatureType() == en.eFeatureFlames:
				point = pPlot.getPoint()
				CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPRING'), point)
				CyAudioGame().Play3DSound("AS3D_SPELL_SPRING", point.x, point.y, point.z)
				pPlot.setFeatureType(FeatureTypes.NO_FEATURE, 0)
			if pPlot.getImprovementType() == en.eImprovementSmoke:
				point = pPlot.getPoint()
				CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPRING'), point)
				CyAudioGame().Play3DSound("AS3D_SPELL_SPRING", point.x, point.y, point.z)
				pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)

def canCityTriggerSmugglers(argsList):
	eTrigger, pCity = argsList
	if pCity.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_SMUGGLERS_PORT')) > 0:
		return False
	if not pCity.isCoastal(10):
		return False
	return True

def doSpiderMine3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if pPlot.getNumUnits() == 0:
		pAnimalPlayer = gc.getPlayer(gc.getANIMAL_PLAYER())
		pNewUnit = pAnimalPlayer.initUnit(gc.getInfoTypeForString('UNIT_GIANT_SPIDER'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
"""
def applyTreasure1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
#	cf.placeTreasure(ePlayer, gc.getInfoTypeForString('EQUIPMENT_TREASURE'))
	cf.placeTreasure(ePlayer, gc.getInfoTypeForString('UNIT_TREASURE'))
"""
def canTriggerSwitchCivs(argsList):
	ePlayer, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pOtherPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	if not pPlayer.isHuman():
		return False
	if CyGame().getRankPlayer(0) != kTriggeredData.ePlayer:
		return False
	if CyGame().getGameTurn() < 20:
		return False
	if gc.getTeam(pOtherPlayer.getTeam()).isAVassal():
		return False
	if CyGame().getWBMapScript():
		return False
	return True

def doSwitchCivs2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	CyGame().reassignPlayerAdvanced(ePlayer, kTriggeredData.eOtherPlayer, -1)

def canCityTriggerTraitor(argsList):
	eTrigger, pCity = argsList
	return (pCity.happyLevel() - pCity.unhappyLevel(0)) >= 0

def doVeilVsOrderTemple1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pCity.changeOccupationTimer(1)
	iOrder = gc.getInfoTypeForString('RELIGION_THE_ORDER')
	iVeil = gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL')
	pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_ORDER'), 0)
	if not pCity.isHolyCityByType(iOrder):
		if gc.getGame().getSorenRandNum(100, "Veil vs Order Temple 1") < 50:
			pCity.setHasReligion(iOrder, False, False, False)
	(loopCity, iter) = pPlayer.firstCity(False)
	while(loopCity):
		if loopCity.isHasReligion(iVeil):
			loopCity.changeHappinessTimer(5)
		if loopCity.isHasReligion(iOrder):
			loopCity.changeHurryAngerTimer(5)
		(loopCity, iter) = pPlayer.nextCity(iter, False)

def doVeilVsOrderTemple2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pCity.changeOccupationTimer(1)
	iOrder = gc.getInfoTypeForString('RELIGION_THE_ORDER')
	if gc.getGame().getSorenRandNum(100, "Veil Vs Order Temple 2") < 50:
		pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_ORDER'), 0)
	if not pCity.isHolyCityByType(iOrder):
		if gc.getGame().getSorenRandNum(100, "Veil Vs Order Temple 2") < 50:
			pCity.setHasReligion(iOrder, False, False, False)
	if gc.getGame().getSorenRandNum(100, "Veil Vs Order Temple 2") < 50:
		pCity.changePopulation(-1)

def doVeilVsOrderTemple3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pCity.changeOccupationTimer(3)
	iOrder = gc.getInfoTypeForString('RELIGION_THE_ORDER')
	iVeil = gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL')
	(loopCity, iter) = pPlayer.firstCity(False)
	while(loopCity):
		if loopCity.isHasReligion(iOrder):
			loopCity.changeHappinessTimer(5)
		if loopCity.isHasReligion(iVeil):
			loopCity.changeHurryAngerTimer(5)
		(loopCity, iter) = pPlayer.nextCity(iter, False)

def helpVeilVsOrderTemple1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_VEIL_VS_ORDER_TEMPLE_1_HELP", ())
	return szHelp

def helpVeilVsOrderTemple2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_VEIL_VS_ORDER_TEMPLE_2_HELP", ())
	return szHelp

def helpVeilVsOrderTemple3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_VEIL_VS_ORDER_TEMPLE_3_HELP", ())
	return szHelp

def doSlaveEscape(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pUnit = getUnit(kTriggeredData.ePlayer, kTriggeredData.iUnitId)
	pUnit.kill(False, PlayerTypes.NO_PLAYER)
	CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_SLAVE_ESCAPE", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Units/Slave.dds', en.eColorGreen, pUnit.getX(), pUnit.getY(), True, True)

def canUnitTriggerSlaveRevolt(argsList):
	eTrigger, pUnit = argsList
	pPlot = pUnit.plot()
	return pPlot.getNumUnits() == 1

def doSlaveRevolt(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pUnit = getUnit(kTriggeredData.ePlayer, kTriggeredData.iUnitId)
	eRace = pUnit.getRace()
	plot = pUnit.plot()
	pUnit.kill(False, PlayerTypes.NO_PLAYER)
	pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
	pNewUnit = pBarbarianPlayer.initUnit(gc.getInfoTypeForString('UNIT_WARRIOR'), plot.getX(), plot.getY(), UnitAITypes.UNITAI_ATTACK_CITY, DirectionTypes.DIRECTION_SOUTH)
	if eRace != PromotionTypes.NO_PROMOTION:
		pNewUnit.setHasPromotion(eRace, True)
	CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_SLAVE_REVOLT", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Units/Slave.dds', en.eColorGreen, pUnit.getX(), pUnit.getY(), True, True)

##--------	Choose Trait: Deleted by Denev 2013/02/23
	'''
def canApplyTraitAggressive(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
##--------	Advanced Rules: Modified by Denev
#	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() == gc.getInfoTypeForString('TRAIT_AGGRESSIVE'):
	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).hasTrait(gc.getInfoTypeForString('TRAIT_AGGRESSIVE')):
##--------	Advanced Rules: End Modify
		return False
	return True

def doTraitAggressive(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	for eTrait in range(gc.getNumTraitInfos()):
		if pPlayer.hasTrait(eTrait):
			if (gc.getTraitInfo(eTrait).isSelectable()):
##--------	Advanced Rules: Modified by Denev
				"""
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() != eTrait:
					pPlayer.setHasTrait(eTrait, False)
	pPlayer.setHasTrait(gc.getInfoTypeForString('TRAIT_AGGRESSIVE'), True)
				"""
				pPlayer.setHasTraitWithSource(eTrait, False, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
	pPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_AGGRESSIVE'), True, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
##--------	Advanced Rules: End Modify

def canApplyTraitArcane(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
##--------	Advanced Rules: Modified by Denev
#	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() == gc.getInfoTypeForString('TRAIT_ARCANE'):
	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).hasTrait(gc.getInfoTypeForString('TRAIT_ARCANE')):
##--------	Advanced Rules: End Modify
		return False
	return True

def doTraitArcane(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	for eTrait in range(gc.getNumTraitInfos()):
		if pPlayer.hasTrait(eTrait):
			if (gc.getTraitInfo(eTrait).isSelectable()):
##--------	Advanced Rules: Modified by Denev
				"""
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() != eTrait:
					pPlayer.setHasTrait(eTrait, False)
	pPlayer.setHasTrait(gc.getInfoTypeForString('TRAIT_ARCANE'), True)
				"""
				pPlayer.setHasTraitWithSource(eTrait, False, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
	pPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_ARCANE'), True, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
##--------	Advanced Rules: End Modify

def canApplyTraitCharismatic(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
##--------	Advanced Rules: Modified by Denev
#	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() == gc.getInfoTypeForString('TRAIT_CHARISMATIC'):
	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).hasTrait(gc.getInfoTypeForString('TRAIT_CHARISMATIC')):
##--------	Advanced Rules: End Modify
		return False
	return True

def doTraitCharismatic(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	for eTrait in range(gc.getNumTraitInfos()):
		if pPlayer.hasTrait(eTrait):
			if (gc.getTraitInfo(eTrait).isSelectable()):
##--------	Advanced Rules: Modified by Denev
				"""
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() != eTrait:
					pPlayer.setHasTrait(eTrait, False)
	pPlayer.setHasTrait(gc.getInfoTypeForString('TRAIT_CHARISMATIC'), True)
				"""
				pPlayer.setHasTraitWithSource(eTrait, False, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
	pPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_CHARISMATIC'), True, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
##--------	Advanced Rules: End Modify

def canApplyTraitCreative(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
##--------	Advanced Rules: Modified by Denev
#	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() == gc.getInfoTypeForString('TRAIT_CREATIVE'):
	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).hasTrait(gc.getInfoTypeForString('TRAIT_CREATIVE')):
##--------	Advanced Rules: End Modify
		return False
	return True

def doTraitCreative(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	for eTrait in range(gc.getNumTraitInfos()):
		if pPlayer.hasTrait(eTrait):
			if (gc.getTraitInfo(eTrait).isSelectable()):
##--------	Advanced Rules: Modified by Denev
				"""
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() != eTrait:
					pPlayer.setHasTrait(eTrait, False)
	pPlayer.setHasTrait(gc.getInfoTypeForString('TRAIT_CREATIVE'), True)
				"""
				pPlayer.setHasTraitWithSource(eTrait, False, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
	pPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_CREATIVE'), True, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
##--------	Advanced Rules: End Modify

def canApplyTraitExpansive(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
##--------	Advanced Rules: Modified by Denev
#	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() == gc.getInfoTypeForString('TRAIT_EXPANSIVE'):
	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).hasTrait(gc.getInfoTypeForString('TRAIT_EXPANSIVE')):
##--------	Advanced Rules: End Modify
		return False
	return True

def doTraitExpansive(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	for eTrait in range(gc.getNumTraitInfos()):
		if pPlayer.hasTrait(eTrait):
			if (gc.getTraitInfo(eTrait).isSelectable()):
##--------	Advanced Rules: Modified by Denev
				"""
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() != eTrait:
					pPlayer.setHasTrait(eTrait, False)
	pPlayer.setHasTrait(gc.getInfoTypeForString('TRAIT_EXPANSIVE'), True)
				"""
				pPlayer.setHasTraitWithSource(eTrait, False, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
	pPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_EXPANSIVE'), True, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
##--------	Advanced Rules: End Modify

def canApplyTraitFinancial(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
##--------	Advanced Rules: Modified by Denev
#	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() == gc.getInfoTypeForString('TRAIT_FINANCIAL'):
	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).hasTrait(gc.getInfoTypeForString('TRAIT_FINANCIAL')):
##--------	Advanced Rules: End Modify
		return False
	return True

def doTraitFinancial(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	for eTrait in range(gc.getNumTraitInfos()):
		if pPlayer.hasTrait(eTrait):
			if (gc.getTraitInfo(eTrait).isSelectable()):
##--------	Advanced Rules: Modified by Denev
				"""
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() != eTrait:
					pPlayer.setHasTrait(eTrait, False)
	pPlayer.setHasTrait(gc.getInfoTypeForString('TRAIT_FINANCIAL'), True)
				"""
				pPlayer.setHasTraitWithSource(eTrait, False, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
	pPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_FINANCIAL'), True, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
##--------	Advanced Rules: End Modify

def canApplyTraitIndustrious(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
##--------	Advanced Rules: Modified by Denev
#	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() == gc.getInfoTypeForString('TRAIT_INDUSTRIOUS'):
	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).hasTrait(gc.getInfoTypeForString('TRAIT_INDUSTRIOUS')):
##--------	Advanced Rules: End Modify
		return False
	return True

def doTraitIndustrious(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	for eTrait in range(gc.getNumTraitInfos()):
		if pPlayer.hasTrait(eTrait):
			if (gc.getTraitInfo(eTrait).isSelectable()):
##--------	Advanced Rules: Modified by Denev
				"""
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() != eTrait:
					pPlayer.setHasTrait(eTrait, False)
	pPlayer.setHasTrait(gc.getInfoTypeForString('TRAIT_INDUSTRIOUS'), True)
				"""
				pPlayer.setHasTraitWithSource(eTrait, False, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
	pPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_INDUSTRIOUS'), True, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
##--------	Advanced Rules: End Modify

def doTraitInsane(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	for i in range(gc.getNumTraitInfos()):
##--------	Advanced Rules: Modified by Denev 2009/10/04
#		if (pPlayer.hasTrait(i) and i != gc.getInfoTypeForString('TRAIT_INSANE')):
		if (pPlayer.hasTrait(i) and gc.getTraitInfo(i).isSelectable()):
##--------	Advanced Rules: End Modify
##--------	Advanced Rules: Modified by Denev
#			pPlayer.setHasTrait(i, False)
			pPlayer.setHasTraitWithSource(i, False, TraitSourceTypes.TRAITSOURCE_INSANE)
##--------	Advanced Rules: End Modify
##--------	Advanced Rules: Modified by Denev 2009/10/04
	"avoid hard coding trait types"
	"""
	Traits = [ 'TRAIT_AGGRESSIVE', 'TRAIT_ARCANE', 'TRAIT_CHARISMATIC', 'TRAIT_CREATIVE', 'TRAIT_EXPANSIVE', 'TRAIT_FINANCIAL', 'TRAIT_INDUSTRIOUS', 'TRAIT_ORGANIZED', 'TRAIT_PHILOSOPHICAL', 'TRAIT_RAIDERS', 'TRAIT_SPIRITUAL' ]
	iRnd1 = CyGame().getSorenRandNum(len(Traits), "Insane")
	iRnd2 = CyGame().getSorenRandNum(len(Traits), "Insane")
	while iRnd2 == iRnd1:
		iRnd2 = CyGame().getSorenRandNum(len(Traits), "Insane")
	iRnd3 = CyGame().getSorenRandNum(len(Traits), "Insane")
	while iRnd3 == iRnd1 or iRnd3 == iRnd2:
		iRnd3 = CyGame().getSorenRandNum(len(Traits), "Insane")
	pPlayer.setHasTrait(gc.getInfoTypeForString(Traits[iRnd1]), True)
	pPlayer.setHasTrait(gc.getInfoTypeForString(Traits[iRnd2]), True)
	pPlayer.setHasTrait(gc.getInfoTypeForString(Traits[iRnd3]), True)
	"""
	leTrait = [eTrait for eTrait in range(gc.getNumTraitInfos()) if gc.getTraitInfo(eTrait).isSelectable()]
	liChosenTrait = []
	for iLoop in range(3):
		liChosenTrait.append(leTrait.pop( CyGame().getSorenRandNum(len(leTrait), "Insane") ))
	liChosenTrait.sort()
	for iChosenTrait in liChosenTrait:
##--------	Advanced Rules: Modified by Denev
#		pPlayer.setHasTrait(iChosenTrait, True)
		pPlayer.setHasTraitWithSource(iChosenTrait, True, TraitSourceTypes.TRAITSOURCE_INSANE)
##--------	Advanced Rules: End Modify
##--------	Advanced Rules: End Modify

def canApplyTraitOrganized(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
##--------	Advanced Rules: Modified by Denev
#	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() == gc.getInfoTypeForString('TRAIT_ORGANIZED'):
	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).hasTrait(gc.getInfoTypeForString('TRAIT_ORGANIZED')):
##--------	Advanced Rules: End Modify
		return False
	return True

def doTraitOrganized(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	for eTrait in range(gc.getNumTraitInfos()):
		if pPlayer.hasTrait(eTrait):
			if (gc.getTraitInfo(eTrait).isSelectable()):
##--------	Advanced Rules: Modified by Denev
				"""
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() != eTrait:
					pPlayer.setHasTrait(eTrait, False)
	pPlayer.setHasTrait(gc.getInfoTypeForString('TRAIT_ORGANIZED'), True)
				"""
				pPlayer.setHasTraitWithSource(eTrait, False, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
	pPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_ORGANIZED'), True, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
##--------	Advanced Rules: End Modify

def canApplyTraitPhilosophical(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
##--------	Advanced Rules: Modified by Denev
#	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() == gc.getInfoTypeForString('TRAIT_PHILOSOPHICAL'):
	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).hasTrait(gc.getInfoTypeForString('TRAIT_PHILOSOPHICAL')):
##--------	Advanced Rules: End Modify
		return False
	return True

def doTraitPhilosophical(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	for eTrait in range(gc.getNumTraitInfos()):
		if pPlayer.hasTrait(eTrait):
			if (gc.getTraitInfo(eTrait).isSelectable()):
##--------	Advanced Rules: Modified by Denev
				"""
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() != eTrait:
					pPlayer.setHasTrait(eTrait, False)
	pPlayer.setHasTrait(gc.getInfoTypeForString('TRAIT_PHILOSOPHICAL'), True)
				"""
				pPlayer.setHasTraitWithSource(eTrait, False, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
	pPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_PHILOSOPHICAL'), True, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
##--------	Advanced Rules: End Modify

def canApplyTraitRaiders(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
##--------	Advanced Rules: Modified by Denev
#	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() == gc.getInfoTypeForString('TRAIT_RAIDERS'):
	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).hasTrait(gc.getInfoTypeForString('TRAIT_RAIDERS')):
##--------	Advanced Rules: End Modify
		return False
	return True

def doTraitRaiders(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	for eTrait in range(gc.getNumTraitInfos()):
		if pPlayer.hasTrait(eTrait):
			if (gc.getTraitInfo(eTrait).isSelectable()):
##--------	Advanced Rules: Modified by Denev
				"""
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() != eTrait:
					pPlayer.setHasTrait(eTrait, False)
	pPlayer.setHasTrait(gc.getInfoTypeForString('TRAIT_RAIDERS'), True)
				"""
				pPlayer.setHasTraitWithSource(eTrait, False, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
	pPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_RAIDERS'), True, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
##--------	Advanced Rules: End Modify

def canApplyTraitSpiritual(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
##--------	Advanced Rules: Modified by Denev
#	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() == gc.getInfoTypeForString('TRAIT_SPIRITUAL'):
	if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).hasTrait(gc.getInfoTypeForString('TRAIT_SPIRITUAL')):
##--------	Advanced Rules: End Modify
		return False
#Kaijin >>>
	if not pPlayer.isHuman():
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGNOSTIC')):
			return False
#Kaijin <<<
	return True

def doTraitSpiritual(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	for eTrait in range(gc.getNumTraitInfos()):
		if pPlayer.hasTrait(eTrait):
			if (gc.getTraitInfo(eTrait).isSelectable()):
##--------	Advanced Rules: Modified by Denev
				"""
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getPermanentTrait() != eTrait:
					pPlayer.setHasTrait(eTrait, False)
	pPlayer.setHasTrait(gc.getInfoTypeForString('TRAIT_SPIRITUAL'), True)
				"""
				pPlayer.setHasTraitWithSource(eTrait, False, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
	pPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_SPIRITUAL'), True, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
##--------	Advanced Rules: End Modify
	'''
##--------	Choose Trait: End Modify			--------##

def doVolcanoCreation(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	pPlot.setPlotType(PlotTypes.PLOT_LAND, True, True)
	pPlot.setFeatureType(gc.getInfoTypeForString('FEATURE_VOLCANO'), 0)
	point = pPlot.getPoint()
	CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_ARTILLERY_SHELL_EXPLODE'), point)
	CyAudioGame().Play3DSound("AS3D_UN_GRENADE_EXPLODE", point.x, point.y, point.z)

def canUnitTriggerWarGames(argsList):
	eTrigger, pUnit = argsList
	if not pUnit.isAlive():
		return False
	if pUnit.isOnlyDefensive():
		return False
	return True

def applyWBFallOfCuantineRosier1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	CyGame().setTrophyValue("TROPHY_WB_FALL_OF_CUANTINE_ROSIER_ALLY", 0)

def applyWBFallOfCuantineRosier2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	CyGame().setTrophyValue("TROPHY_WB_FALL_OF_CUANTINE_ROSIER_ALLY", 1)

def applyWBFallOfCuantineFleeCalabim(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	CyGame().setTrophyValue("TROPHY_WB_CIV_DECIUS", gc.getInfoTypeForString('CIVILIZATION_CALABIM'))

def applyWBFallOfCuantineFleeMalakim(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	CyGame().setTrophyValue("TROPHY_WB_CIV_DECIUS", gc.getInfoTypeForString('CIVILIZATION_MALAKIM'))

def applyWBGiftOfKylorinMeshabberRight(argsList):
	pPlot = CyMap().plot(19,16)
	pPlot.setPythonActive(False)
	pPlot = CyMap().plot(20,16)
	pUnit = pPlot.getUnit(0)
	pUnit.kill(True, 0)
	cf.addPopup(CyTranslator().getText("TXT_KEY_WB_GIFT_OF_KYLORIN_MESHABBER_RIGHT",()), 'art/interface/popups/Tya.dds')

def applyWBGiftOfKylorinMeshabberWrong(argsList):
	pPlot1 = CyMap().plot(19,16)
	pPlot1.setPythonActive(False)
	pPlot2 = CyMap().plot(20,16)
	pUnit = pPlot2.getUnit(0)
	pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HELD'), False)
	pUnit.attack(pPlot1, False)
	cf.addPopup(CyTranslator().getText("TXT_KEY_WB_GIFT_OF_KYLORIN_MESHABBER_WRONG",()), 'art/interface/popups/Tya.dds')

def applyWBGiftOfKylorinSecretDoorYes(argsList):
	pPlot = CyMap().plot(23,6)
	pPlot.setPythonActive(False)
	pPlot = CyMap().plot(23,5)
	pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)

def applyWBLordOfTheBalorsTemptJudeccaYes(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	eOtherPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	eEnemyTeam = eOtherPlayer.getTeam()
	pTeam = gc.getTeam(gc.getPlayer(ePlayer).getTeam())
	pTeam.setPermanentWarPeace(eEnemyTeam, False)
	pTeam.setPermanentWarPeace(6, False)
	pTeam.makePeace(6)
	pTeam.declareWar(eEnemyTeam, True, WarPlanTypes.WARPLAN_TOTAL)
	pTeam.setPermanentWarPeace(eEnemyTeam, True)
	pTeam.setPermanentWarPeace(6, True)

def applyWBLordOfTheBalorsTemptSallosYes(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pTeam = gc.getTeam(gc.getPlayer(ePlayer).getTeam())
	pTeam.setPermanentWarPeace(7, False)
	pTeam.makePeace(7)
	pTeam.setPermanentWarPeace(7, True)

def applyWBLordOfTheBalorsTemptOuzzaYes(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pTeam = gc.getTeam(gc.getPlayer(ePlayer).getTeam())
	pTeam.setPermanentWarPeace(8, False)
	pTeam.makePeace(8)
	pTeam.setPermanentWarPeace(8, True)
	for pyCity in PyPlayer(ePlayer).getCityList():
		pCity = pyCity.GetCy()
		if pCity.getPopulation() > 1:
			pCity.changePopulation(-1)

def applyWBLordOfTheBalorsTemptMeresinYes(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pTeam = gc.getTeam(gc.getPlayer(ePlayer).getTeam())
	pTeam.setPermanentWarPeace(9, False)
	pTeam.makePeace(9)
	pTeam.setPermanentWarPeace(9, True)

def applyWBLordOfTheBalorsTemptStatiusYes(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pTeam = gc.getTeam(gc.getPlayer(ePlayer).getTeam())
	pTeam.setPermanentWarPeace(10, False)
	pTeam.makePeace(10)
	pTeam.setPermanentWarPeace(10, True)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	gc.getPlayer(10).acquireCity(pCity, False, False)

def applyWBLordOfTheBalorsTemptLetheYes(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pUnit = getUnit(kTriggeredData.ePlayer, kTriggeredData.iUnitId)
	pTeam = gc.getTeam(pPlayer.getTeam())
	pTeam.setPermanentWarPeace(11, False)
	pTeam.makePeace(11)
	pTeam.setPermanentWarPeace(11, True)
	pUnit.kill(True, 0)

def applyWBSplinteredCourtDefeatedAmelanchier3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	eLjosalfarTeam = TeamTypes.NO_TEAM
	eDovielloTeam = TeamTypes.NO_TEAM
	eSvartalfarTeam = TeamTypes.NO_TEAM
	CyGame().setTrophyValue("TROPHY_WB_CIV_AMELANCHIER", gc.getInfoTypeForString('CIVILIZATION_DOVIELLO'))
	for eLoopPlayer in range(gc.getMAX_PLAYERS()):
		pLoopPlayer = gc.getPlayer(eLoopPlayer)
		if pLoopPlayer.isAlive():
			if pLoopPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DOVIELLO'):
				eDovielloTeam = pLoopPlayer.getTeam()
			if pLoopPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LJOSALFAR'):
				eLjosalfarTeam = pLoopPlayer.getTeam()
			if pLoopPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SVARTALFAR'):
				eSvartalfarTeam = pLoopPlayer.getTeam()
	if TeamTypes.NO_TEAM not in (eDovielloTeam, eLjosalfarTeam, eSvartalfarTeam):
		pTeam = gc.getTeam(eDovielloTeam)
		if pTeam.isAtWar(eSvartalfarTeam):
			pTeam.makePeace(eSvartalfarTeam)
		if not pTeam.isAtWar(eLjosalfarTeam):
			pTeam.declareWar(eLjosalfarTeam, False, WarPlanTypes.WARPLAN_LIMITED)

def applyWBSplinteredCourtDefeatedThessa3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	eLjosalfarTeam = TeamTypes.NO_TEAM
	eCalabimTeam = TeamTypes.NO_TEAM
	eSvartalfarTeam = TeamTypes.NO_TEAM
	CyGame().setTrophyValue("TROPHY_WB_CIV_THESSA", gc.getInfoTypeForString('CIVILIZATION_CALABIM'))
	for iLoopPlayer in range(gc.getMAX_PLAYERS()):
		pLoopPlayer = gc.getPlayer(iLoopPlayer)
		if pLoopPlayer.isAlive():
			if pLoopPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_CALABIM'):
				eCalabimTeam = pLoopPlayer.getTeam()
			if pLoopPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LJOSALFAR'):
				eLjosalfarTeam = pLoopPlayer.getTeam()
			if pLoopPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SVARTALFAR'):
				eSvartalfarTeam = pLoopPlayer.getTeam()
	if TeamTypes.NO_TEAM not in (eCalabimTeam, eLjosalfarTeam, eSvartalfarTeam):
		pTeam = gc.getTeam(eCalabimTeam)
		if pTeam.isAtWar(eSvartalfarTeam):
			pTeam.makePeace(eSvartalfarTeam)
		if not pTeam.isAtWar(eLjosalfarTeam):
			pTeam.declareWar(eLjosalfarTeam, False, WarPlanTypes.WARPLAN_LIMITED)

def applyWBSplinteredCourtDefeatedRivanna3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	eLjosalfarTeam = TeamTypes.NO_TEAM
	eCalabimTeam = TeamTypes.NO_TEAM
	eSvartalfarTeam = TeamTypes.NO_TEAM
	CyGame().setTrophyValue("TROPHY_WB_CIV_RIVANNA", gc.getInfoTypeForString('CIVILIZATION_CALABIM'))
	for eLoopPlayer in range(gc.getMAX_PLAYERS()):
		pLoopPlayer = gc.getPlayer(eLoopPlayer)
		if pLoopPlayer.isAlive():
			if pLoopPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_CALABIM'):
				eCalabimTeam = pLoopPlayer.getTeam()
			if pLoopPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LJOSALFAR'):
				eLjosalfarTeam = pLoopPlayer.getTeam()
			if pLoopPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SVARTALFAR'):
				eSvartalfarTeam = pLoopPlayer.getTeam()
	if TeamTypes.NO_TEAM not in (eCalabimTeam, eLjosalfarTeam, eSvartalfarTeam):
		pTeam = gc.getTeam(eCalabimTeam)
		if pTeam.isAtWar(eLjosalfarTeam):
			pTeam.makePeace(eLjosalfarTeam)
		if not pTeam.isAtWar(eSvartalfarTeam):
			pTeam.declareWar(eSvartalfarTeam, False, WarPlanTypes.WARPLAN_LIMITED)

def applyWBSplinteredCourtDefeatedVolanna3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	eLjosalfarTeam = TeamTypes.NO_TEAM
	eDovielloTeam = TeamTypes.NO_TEAM
	eSvartalfarTeam = TeamTypes.NO_TEAM
	CyGame().setTrophyValue("TROPHY_WB_CIV_VOLANNA", gc.getInfoTypeForString('CIVILIZATION_DOVIELLO'))
	for eLoopPlayer in range(gc.getMAX_PLAYERS()):
		pLoopPlayer = gc.getPlayer(eLoopPlayer)
		if pLoopPlayer.isAlive():
			if pLoopPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DOVIELLO'):
				eDovielloTeam = pLoopPlayer.getTeam()
			if pLoopPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LJOSALFAR'):
				eLjosalfarTeam = pLoopPlayer.getTeam()
			if pLoopPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SVARTALFAR'):
				eSvartalfarTeam = pLoopPlayer.getTeam()
	if TeamTypes.NO_TEAM not in (eDovielloTeam, eLjosalfarTeam, eSvartalfarTeam):
		pTeam = gc.getTeam(eDovielloTeam)
		if pTeam.isAtWar(eLjosalfarTeam):
			pTeam.makePeace(eLjosalfarTeam)
		if not pTeam.isAtWar(eSvartalfarTeam):
			pTeam.declareWar(eSvartalfarTeam, False, WarPlanTypes.WARPLAN_LIMITED)

def applyWBSplinteredCourtParithYes(argsList):
	CyGame().setTrophyValue("TROPHY_WB_SPLINTERED_COURT_PARITH", 1)

def canDoWBTheBlackTowerPickCivBannor(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	if CyGame().isHasTrophy("TROPHY_WB_THE_RADIANT_GUARD_CAPRIA_ALLY"):
		return True
	return False

def applyWBTheBlackTowerPickCivBannor(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	pCity = pPlot.getPlotCity()
	pCity.setCivilizationType(gc.getInfoTypeForString('CIVILIZATION_BANNOR'))
	CyInterface().setDirty(InterfaceDirtyBits.CityInfo_DIRTY_BIT, True)

def applyWBTheBlackTowerPickCivHippus(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	pCity = pPlot.getPlotCity()
	pCity.setCivilizationType(gc.getInfoTypeForString('CIVILIZATION_HIPPUS'))
	CyInterface().setDirty(InterfaceDirtyBits.CityInfo_DIRTY_BIT, True)

def applyWBTheBlackTowerPickCivLanun(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	pCity = pPlot.getPlotCity()
	pCity.setCivilizationType(gc.getInfoTypeForString('CIVILIZATION_LANUN'))
	CyInterface().setDirty(InterfaceDirtyBits.CityInfo_DIRTY_BIT, True)

def canDoWBTheBlackTowerPickCivLjosalfar(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	if CyGame().isHasTrophy("TROPHY_WB_THE_SPLINTERED_COURT_LJOSALFAR"):
		return True
	return False

def applyWBTheBlackTowerPickCivLjosalfar(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	pCity = pPlot.getPlotCity()
	pCity.setCivilizationType(gc.getInfoTypeForString('CIVILIZATION_LJOSALFAR'))
	CyInterface().setDirty(InterfaceDirtyBits.CityInfo_DIRTY_BIT, True)

def canDoWBTheBlackTowerPickCivLuchuirp(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	if CyGame().isHasTrophy("TROPHY_WB_THE_MOMUS_BEERI_ALLY"):
		return True
	return False

def applyWBTheBlackTowerPickCivLuchuirp(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	pCity = pPlot.getPlotCity()
	pCity.setCivilizationType(gc.getInfoTypeForString('CIVILIZATION_LUCHUIRP'))
	CyInterface().setDirty(InterfaceDirtyBits.CityInfo_DIRTY_BIT, True)

def canDoWBTheBlackTowerPickCivSvartalfar(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	if CyGame().isHasTrophy("TROPHY_WB_THE_SPLINTERED_COURT_SVARTALFAR"):
		return True
	return False

def applyWBTheBlackTowerPickCivSvartalfar(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	pCity = pPlot.getPlotCity()
	pCity.setCivilizationType(gc.getInfoTypeForString('CIVILIZATION_SVARTALFAR'))
	CyInterface().setDirty(InterfaceDirtyBits.CityInfo_DIRTY_BIT, True)

def applyWBTheMomusBeerisOfferYes(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	gc.getGame().changeTrophyValue("TROPHY_WB_THE_MOMUS_BEERI_ALLY", 1)
	pTeam = gc.getTeam(0) #Falamar
	pTeam7 = gc.getTeam(7) #Beeri
	pTeam.setPermanentWarPeace(1, False)
	pTeam.setPermanentWarPeace(7, False)
	pTeam.declareWar(1, True, WarPlanTypes.WARPLAN_TOTAL)
	pTeam7.declareWar(1, True, WarPlanTypes.WARPLAN_TOTAL)
	pTeam.makePeace(7)
	pTeam.setPermanentWarPeace(1, True)
	pTeam.setPermanentWarPeace(7, True)

def applyWBTheRadiantGuardChooseSidesBasium(argsList):
	gc.getGame().setTrophyValue("TROPHY_WB_THE_RADIANT_GUARD_HYBOREM_ALLY", 0)
	gc.getGame().setTrophyValue("TROPHY_WB_THE_RADIANT_GUARD_BASIUM_ALLY", 1)

def applyWBTheRadiantGuardChooseSidesHyborem(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	gc.getGame().setTrophyValue("TROPHY_WB_THE_RADIANT_GUARD_HYBOREM_ALLY", 1)
	gc.getGame().setTrophyValue("TROPHY_WB_THE_RADIANT_GUARD_BASIUM_ALLY", 0)
	pPlayer = gc.getPlayer(1) #Basium
	pCity = pPlayer.getCapitalCity()
	apUnitList = PyPlayer(0).getUnitList()
	for pLoopUnit in apUnitList:
		if gc.getUnitInfo(pLoopUnit.getUnitType()).getReligionType() == gc.getInfoTypeForString('RELIGION_THE_EMPYREAN'):
			szBuffer = CyTranslator().getText("TXT_KEY_MESSAGE_UNIT_ABANDON", (pLoopUnit.getName(), ))
			CyInterface().addMessage(0, True, gc.getEVENT_MESSAGE_TIME(), szBuffer, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getUnitInfo(pLoopUnit.getUnitType()).getButton(), en.eColorRed, pLoopUnit.getX(), pLoopUnit.getY(), True, True)
			pNewUnit = pPlayer.initUnit(pLoopUnit.getUnitType(), pCity.getX(), pCity.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit.convert(pLoopUnit)
	pTeam = gc.getTeam(0) #Falamar
	pTeam.setPermanentWarPeace(1, False)
	pTeam.setPermanentWarPeace(2, False)
	pTeam.declareWar(1, True, WarPlanTypes.WARPLAN_TOTAL)
	pTeam.makePeace(2)
	pTeam.setPermanentWarPeace(1, True)
	pTeam.setPermanentWarPeace(2, True)

def doWerewolf1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pPlot = cf.findClearPlot(-1, pCity.plot())
	if pPlot != -1:
		pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
		pBarbarianPlayer.initUnit(gc.getInfoTypeForString('UNIT_WEREWOLF'), pPlot.getX(), pPlot.getY(), UnitAITypes.UNITAI_ATTACK_CITY, DirectionTypes.DIRECTION_SOUTH)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_WEREWOLF_RELEASED", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Units/Werewolf.dds', en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)

def doWerewolf3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_WEREWOLF_KILLED", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Units/Werewolf.dds', en.eColorGreen, pCity.getX(), pCity.getY(), True, True)

######## BLESSED SEA ###########

def getHelpBlessedSea1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	map = gc.getMap()
	iOurMinLandmass = (3 * gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers()) / 2

	szHelp = localText.getText("TXT_KEY_EVENT_BLESSED_SEA_HELP", (iOurMinLandmass, ))

	return szHelp

def canTriggerBlessedSea(argsList):
	ePlayer, kTriggeredData = argsList
	map = gc.getMap()

	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and gc.getPlayer(kTriggeredData.ePlayer).isHuman():
		return False

	iMapMinLandmass = 2 * gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers()
	iOurMaxLandmass = gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers() / 2

	if (map.getNumLandAreas() < iMapMinLandmass):
		return False

	iOurLandmasses = 0
	for i in range(map.getIndexAfterLastArea()):
		area = map.getArea(i)
		if not area.isNone() and not area.isWater() and area.getCitiesPerPlayer(kTriggeredData.ePlayer) > 0:
			iOurLandmasses += 1

	if (iOurLandmasses > iOurMaxLandmass):
		return False

	player = gc.getPlayer(kTriggeredData.ePlayer)
	if player.getUnitClassCount(CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_GALLEY')) == 0:
		if player.getUnitClassCount(CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_CARAVEL')) == 0:
			if player.getUnitClassCount(CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_GALLEON')) == 0:
				return False

	return True

def canTriggerBlessedSea2(argsList):
	ePlayer, kTriggeredData = argsList
	map = gc.getMap()
	iOurMinLandmass = (3 * gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers()) / 2

	iOurLandmasses = 0
	for i in range(map.getIndexAfterLastArea()):
		area = map.getArea(i)
		if not area.isNone() and not area.isWater() and area.getCitiesPerPlayer(kTriggeredData.ePlayer) > 0:
			iOurLandmasses += 1

	if (iOurLandmasses < iOurMinLandmass):
		return False

	return True

def applyBlessedSea2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	iBuilding = -1

	if (-1 != kTriggeredData.eReligion):
		for i in range(gc.getNumBuildingInfos()):
			if (gc.getBuildingInfo(i).getSpecialBuildingType() == CvUtil.findInfoTypeNum(gc.getSpecialBuildingInfo,gc.getNumSpecialBuildingInfos(), 'SPECIALBUILDING_TEMPLE')):
				if (gc.getBuildingInfo(i).getReligionType() == kTriggeredData.eReligion):
					iBuilding = i
					break


	if (iBuilding == -1):
		return

	player = gc.getPlayer(kTriggeredData.ePlayer)
	(loopCity, iter) = player.firstCity(False)

	while(loopCity):

		if (loopCity.getPopulation() >= 5):
			if (loopCity.canConstruct(iBuilding, False, False, True)):
				loopCity.setNumRealBuilding(iBuilding, 1)

		(loopCity, iter) = player.nextCity(iter, False)


def canApplyBlessedSea2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	iBuilding = -1

	if (-1 != kTriggeredData.eReligion):
		for i in range(gc.getNumBuildingInfos()):
			if (gc.getBuildingInfo(i).getSpecialBuildingType() == CvUtil.findInfoTypeNum(gc.getSpecialBuildingInfo,gc.getNumSpecialBuildingInfos(), 'SPECIALBUILDING_TEMPLE')):
				if (gc.getBuildingInfo(i).getReligionType() == kTriggeredData.eReligion):
					iBuilding = i
					break


	if (iBuilding == -1):
		return False

	player = gc.getPlayer(kTriggeredData.ePlayer)
	(loopCity, iter) = player.firstCity(False)
	bFound = False

	while(loopCity):

		if (loopCity.getPopulation() >= 5):
			if (loopCity.canConstruct(iBuilding, False, False, True)):
				bFound = True
				break

		(loopCity, iter) = player.nextCity(iter, False)

	return bFound

######## MARATHON ###########

def canTriggerMarathon(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)
	otherPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	team = gc.getTeam(player.getTeam())

	if (team.AI_getAtWarCounter(otherPlayer.getTeam()) == 1):
		(loopUnit, iter) = otherPlayer.firstUnit(False)
		while( loopUnit ):
			plot = loopUnit.plot()
			if (not plot.isNone()):
				if (plot.getOwner() == kTriggeredData.ePlayer):
					return True
			(loopUnit, iter) = otherPlayer.nextUnit(iter, False)

	return False

######## WEDDING FEUD ###########

def doWeddingFeud2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	player = gc.getPlayer(kTriggeredData.ePlayer)
	(loopCity, iter) = player.firstCity(False)

	while(loopCity):
		if loopCity.isHasReligion(kTriggeredData.eReligion):
			loopCity.changeHappinessTimer(30)
		(loopCity, iter) = player.nextCity(iter, False)

	return 1

def getHelpWeddingFeud2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	religion = gc.getReligionInfo(kTriggeredData.eReligion)

	szHelp = localText.getText("TXT_KEY_EVENT_WEDDING_FEUD_2_HELP", (gc.getDefineINT("TEMP_HAPPY"), 30, religion.getChar()))

	return szHelp

def canDoWeddingFeud3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	player = gc.getPlayer(kTriggeredData.ePlayer)

	if player.getGold() - 10 * player.getNumCities() < 0:
		return False

	return True

def doWeddingFeud3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	destPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	player = gc.getPlayer(kTriggeredData.ePlayer)

	for iLoopPlayer in range(gc.getMAX_CIV_PLAYERS()):
		loopPlayer = gc.getPlayer(iLoopPlayer)
		if loopPlayer.isAlive() and loopPlayer.getStateReligion() == player.getStateReligion():
			loopPlayer.AI_changeAttitudeExtra(kTriggeredData.ePlayer, 1)
			player.AI_changeAttitudeExtra(iLoopPlayer, 1)

	if gc.getTeam(destPlayer.getTeam()).canDeclareWar(player.getTeam()):
		if destPlayer.isHuman():
			# this works only because it's a single-player only event
			popupInfo = CyPopupInfo()
			popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
			popupInfo.setText(localText.getText("TXT_KEY_EVENT_WEDDING_FEUD_OTHER_3", (gc.getReligionInfo(kTriggeredData.eReligion).getAdjectiveKey(), player.getCivilizationShortDescriptionKey())))
			popupInfo.setData1(kTriggeredData.eOtherPlayer)
			popupInfo.setData2(kTriggeredData.ePlayer)
			popupInfo.setPythonModule("CvRandomEventInterface")
			popupInfo.setOnClickedPythonCallback("weddingFeud3Callback")
			popupInfo.addPythonButton(localText.getText("TXT_KEY_POPUP_YES", ()), "")
			popupInfo.addPythonButton(localText.getText("TXT_KEY_POPUP_NO", ()), "")
			popupInfo.addPopup(kTriggeredData.eOtherPlayer)
		else:
			gc.getTeam(destPlayer.getTeam()).declareWar(player.getTeam(), False, WarPlanTypes.WARPLAN_LIMITED)

	return 1


def weddingFeud3Callback(argsList):
	iButton, iData1, iData2, iData3, iFlags, szText, bOption1, bOption2 = argsList

	if iButton == 0:
		destPlayer = gc.getPlayer(iData1)
		player = gc.getPlayer(iData2)
		gc.getTeam(destPlayer.getTeam()).declareWar(player.getTeam(), False, WarPlanTypes.WARPLAN_LIMITED)

	return 0

def getHelpWeddingFeud3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	religion = gc.getReligionInfo(kTriggeredData.eReligion)

	szHelp = localText.getText("TXT_KEY_EVENT_WEDDING_FEUD_3_HELP", (1, religion.getChar()))

	return szHelp

######## SPICY ###########

def canTriggerSpicy(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iSpice = CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(), 'BONUS_SPICES')
	iHappyBonuses = 0
	bSpices = False
	for i in range(gc.getNumBonusInfos()):
		bonus = gc.getBonusInfo(i)
		iNum = player.getNumAvailableBonuses(i)
		if iNum > 0:
			if bonus.getHappiness() > 0:
				iHappyBonuses += 1
				if iHappyBonuses > 4:
					return False
			if i == iSpice:
				return False

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if not plot.canHaveBonus(iSpice, False):
		return False

	return True

def doSpicy2(argsList):
#	need this because plantations are notmally not allowed unless there are already spices
	ePlayer, eEvent, kTriggeredData = argsList

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)

	if not plot.isNone():
		plot.setImprovementType(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(), 'IMPROVEMENT_PLANTATION'))

	return 1

def getHelpSpicy2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	iPlantation = CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(), 'IMPROVEMENT_PLANTATION')
	szHelp = localText.getText("TXT_KEY_EVENT_IMPROVEMENT_GROWTH", ( gc.getImprovementInfo(iPlantation).getTextKey(), ))

	return szHelp

######## BABY BOOM ###########

def canTriggerBabyBoom(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)
	team = gc.getTeam(player.getTeam())

	if team.getAtWarCount(True) > 0:
		return False

	for iLoopTeam in range(gc.getMAX_CIV_TEAMS()):
		if iLoopTeam != player.getTeam():
			if team.AI_getAtPeaceCounter(iLoopTeam) == 1:
				return True

	return False

######## BARD TALE ###########

def applyBardTale3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	player = gc.getPlayer(kTriggeredData.ePlayer)

	player.changeGold(-10 * player.getNumCities())

def canApplyBardTale3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	player = gc.getPlayer(kTriggeredData.ePlayer)

	if player.getGold() - 10 * player.getNumCities() < 0:
		return False

	return True


def getHelpBardTale3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	player = gc.getPlayer(kTriggeredData.ePlayer)

	szHelp = localText.getText("TXT_KEY_EVENT_GOLD_LOST", (10 * player.getNumCities(), ))

	return szHelp

######## LOOTERS ###########

def getHelpLooters3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	city = getCity(kTriggeredData.eOtherPlayer, kTriggeredData.iOtherPlayerCityId)

	szHelp = localText.getText("TXT_KEY_EVENT_LOOTERS_3_HELP", (1, 2, city.getNameKey()))

	return szHelp

def canApplyLooters3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	city = getCity(kTriggeredData.eOtherPlayer, kTriggeredData.iOtherPlayerCityId)

	iNumBuildings = 0
	for iBuilding in range(gc.getNumBuildingInfos()):
		if (city.getNumRealBuilding(iBuilding) > 0 and gc.getBuildingInfo(iBuilding).getProductionCost() <= 100 and gc.getBuildingInfo(iBuilding).getProductionCost() > 0  and not isLimitedWonderClass(gc.getBuildingInfo(iBuilding).getBuildingClassType())):
			iNumBuildings += 1

	return (iNumBuildings > 0)


def applyLooters3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	city = getCity(kTriggeredData.eOtherPlayer, kTriggeredData.iOtherPlayerCityId)

	iNumBuildings = gc.getGame().getSorenRandNum(2, "Looters event number of buildings destroyed")
	iNumBuildingsDestroyed = 0

	listBuildings = []
	for iBuilding in range(gc.getNumBuildingInfos()):
		if (city.getNumRealBuilding(iBuilding) > 0 and gc.getBuildingInfo(iBuilding).getProductionCost() <= 100 and gc.getBuildingInfo(iBuilding).getProductionCost() > 0  and not isLimitedWonderClass(gc.getBuildingInfo(iBuilding).getBuildingClassType())):
			listBuildings.append(iBuilding)

	for i in range(iNumBuildings+1):
		if len(listBuildings) > 0:
			iBuilding = listBuildings[gc.getGame().getSorenRandNum(len(listBuildings), "Looters event building destroyed")]
			szBuffer = localText.getText("TXT_KEY_EVENT_CITY_IMPROVEMENT_DESTROYED", (gc.getBuildingInfo(iBuilding).getTextKey(), ))
			CyInterface().addMessage(kTriggeredData.eOtherPlayer, False, gc.getEVENT_MESSAGE_TIME(), szBuffer, "AS2D_BOMBARDED", InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getBuildingInfo(iBuilding).getButton(), gc.getInfoTypeForString("COLOR_RED"), city.getX(), city.getY(), True, True)
			city.setNumRealBuilding(iBuilding, 0)
			iNumBuildingsDestroyed += 1
			listBuildings.remove(iBuilding)

	if iNumBuildingsDestroyed > 0:
		szBuffer = localText.getText("TXT_KEY_EVENT_NUM_BUILDINGS_DESTROYED", (iNumBuildingsDestroyed, gc.getPlayer(kTriggeredData.eOtherPlayer).getCivilizationAdjectiveKey(), city.getNameKey()))
		CyInterface().addMessage(kTriggeredData.ePlayer, False, gc.getEVENT_MESSAGE_TIME(), szBuffer, "AS2D_BOMBARDED", InterfaceMessageTypes.MESSAGE_TYPE_INFO, None, gc.getInfoTypeForString("COLOR_WHITE"), -1, -1, True, True)

######## BROTHERS IN NEED ###########

def canTriggerBrothersInNeed(argsList):
	ePlayer, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pOtherPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)

	if not pPlayer.canTradeNetworkWith(kTriggeredData.eOtherPlayer):
		return False

	listResources = []
	listResources.append(CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(), 'BONUS_COPPER'))
	listResources.append(CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(), 'BONUS_IRON'))
	listResources.append(CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(), 'BONUS_HORSE'))
	listResources.append(CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(), 'BONUS_IVORY'))

#FfH: Modified by Kael 10/01/2007
#	listResources.append(CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(), 'BONUS_OIL'))
#	listResources.append(CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(), 'BONUS_URANIUM'))
#FfH: End Modify

	bFound = False
	for iResource in listResources:
		if (pPlayer.getNumTradeableBonuses(iResource) > 1 and pOtherPlayer.getNumAvailableBonuses(iResource) <= 0):
			bFound = True
			break

	if not bFound:
		return False

	for iTeam in range(gc.getMAX_CIV_TEAMS()):
		if iTeam != pPlayer.getTeam() and iTeam != pOtherPlayer.getTeam() and gc.getTeam(iTeam).isAlive():
			if gc.getTeam(iTeam).isAtWar(pOtherPlayer.getTeam()) and not gc.getTeam(iTeam).isAtWar(pPlayer.getTeam()):
				return True

	return False

######## HURRICANE ###########

def canCityTriggerHurricane(argsList):
	eTrigger, city = argsList

	if city.isNone():
		return False

	if not city.isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
		return False

	if city.plot().getLatitude() <= 0:
		return False

	if city.getPopulation() < 2:
		return False

	return True

def canApplyHurricane1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)

	listBuildings = []
	for iBuilding in range(gc.getNumBuildingInfos()):
		if (city.getNumRealBuilding(iBuilding) > 0 and gc.getBuildingInfo(iBuilding).getProductionCost() > 0 and not isLimitedWonderClass(gc.getBuildingInfo(iBuilding).getBuildingClassType())):
			listBuildings.append(iBuilding)

	return (len(listBuildings) > 0)

def canApplyHurricane2(argsList):
	return (not canApplyHurricane1(argsList))


def applyHurricane1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)

	listCheapBuildings = []
	listExpensiveBuildings = []
	for iBuilding in range(gc.getNumBuildingInfos()):
		if (city.getNumRealBuilding(iBuilding) > 0 and gc.getBuildingInfo(iBuilding).getProductionCost() <= 100 and gc.getBuildingInfo(iBuilding).getProductionCost() > 0 and not isLimitedWonderClass(gc.getBuildingInfo(iBuilding).getBuildingClassType())):
			listCheapBuildings.append(iBuilding)
		if (city.getNumRealBuilding(iBuilding) > 0 and gc.getBuildingInfo(iBuilding).getProductionCost() > 100 and gc.getBuildingInfo(iBuilding).getProductionCost() > 0 and not isLimitedWonderClass(gc.getBuildingInfo(iBuilding).getBuildingClassType())):
			listExpensiveBuildings.append(iBuilding)

	if len(listCheapBuildings) > 0:
		iBuilding = listCheapBuildings[gc.getGame().getSorenRandNum(len(listCheapBuildings), "Hurricane event cheap building destroyed")]
		szBuffer = localText.getText("TXT_KEY_EVENT_CITY_IMPROVEMENT_DESTROYED", (gc.getBuildingInfo(iBuilding).getTextKey(), ))
		CyInterface().addMessage(kTriggeredData.ePlayer, False, gc.getEVENT_MESSAGE_TIME(), szBuffer, "AS2D_BOMBARDED", InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getBuildingInfo(iBuilding).getButton(), gc.getInfoTypeForString("COLOR_RED"), city.getX(), city.getY(), True, True)
		city.setNumRealBuilding(iBuilding, 0)

	if len(listExpensiveBuildings) > 0:
		iBuilding = listExpensiveBuildings[gc.getGame().getSorenRandNum(len(listExpensiveBuildings), "Hurricane event expensive building destroyed")]
		szBuffer = localText.getText("TXT_KEY_EVENT_CITY_IMPROVEMENT_DESTROYED", (gc.getBuildingInfo(iBuilding).getTextKey(), ))
		CyInterface().addMessage(kTriggeredData.ePlayer, False, gc.getEVENT_MESSAGE_TIME(), szBuffer, "AS2D_BOMBARDED", InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getBuildingInfo(iBuilding).getButton(), gc.getInfoTypeForString("COLOR_RED"), city.getX(), city.getY(), True, True)
		city.setNumRealBuilding(iBuilding, 0)


######## CYCLONE ###########

def canCityTriggerCyclone(argsList):
	eTrigger, city = argsList

	if city.isNone():
		return False

	if not city.isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
		return False

	if city.plot().getLatitude() >= 0:
		return False

	return True

######## TSUNAMI ###########

def canCityTriggerTsunami(argsList):
	eTrigger, city = argsList

	if city.isNone():
		return False

	if not city.isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
		return False

	return True

def canApplyTsunami1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)

	return (city.getPopulation() < 6)

def canApplyTsunami2(argsList):
	return (not canApplyTsunami1(argsList))


def applyTsunami1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)

	city.kill()

def applyTsunami2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)

	listBuildings = []
	for iBuilding in range(gc.getNumBuildingInfos()):
		if (city.getNumRealBuilding(iBuilding) > 0 and gc.getBuildingInfo(iBuilding).getProductionCost() > 0  and not isLimitedWonderClass(gc.getBuildingInfo(iBuilding).getBuildingClassType())):
			listBuildings.append(iBuilding)

	for i in range(5):
		if len(listBuildings) > 0:
			iBuilding = listBuildings[gc.getGame().getSorenRandNum(len(listBuildings), "Tsunami event building destroyed")]
			szBuffer = localText.getText("TXT_KEY_EVENT_CITY_IMPROVEMENT_DESTROYED", (gc.getBuildingInfo(iBuilding).getTextKey(), ))
			CyInterface().addMessage(kTriggeredData.ePlayer, False, gc.getEVENT_MESSAGE_TIME(), szBuffer, "AS2D_BOMBARDED", InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getBuildingInfo(iBuilding).getButton(), gc.getInfoTypeForString("COLOR_RED"), city.getX(), city.getY(), True, True)
			city.setNumRealBuilding(iBuilding, 0)
			listBuildings.remove(iBuilding)


def getHelpTsunami2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)
	city = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)

	szHelp = localText.getText("TXT_KEY_EVENT_TSUNAMI_2_HELP", (5, city.getNameKey()))

	return szHelp


######## MONSOON ###########

def canCityTriggerMonsoon(argsList):
	eTrigger, city = argsList

	if city.isNone():
		return False

	if city.isCoastal(gc.getMIN_WATER_SIZE_FOR_OCEAN()):
		return False

	for iDX in range(-3, 4):
		for iDY in range(-3, 4):
			pLoopPlot = plotXY(city.getX(), city.getY(), iDX, iDY)
			if not pLoopPlot.isNone() and pLoopPlot.getFeatureType() == en.eFeatureJungle:
				return True

	return False

######## VOLCANO ###########

def getHelpVolcano1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	szHelp = localText.getText("TXT_KEY_EVENT_VOLCANO_1_HELP", ())

	return szHelp

def canApplyVolcano1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	iNumImprovements = 0
	for iDX in range(-1, 2):
		for iDY in range(-1, 2):
			loopPlot = plotXY(kTriggeredData.iPlotX, kTriggeredData.iPlotY, iDX, iDY)
			if not loopPlot.isNone():
				if (iDX != 0 or iDY != 0):
					if loopPlot.getImprovementType() != -1:
						iNumImprovements += 1

	return (iNumImprovements > 0)

def applyVolcano1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	listPlots = []
	for iDX in range(-1, 2):
		for iDY in range(-1, 2):
			loopPlot = plotXY(kTriggeredData.iPlotX, kTriggeredData.iPlotY, iDX, iDY)
			if not loopPlot.isNone():
				if (iDX != 0 or iDY != 0):
					if loopPlot.getImprovementType() != -1:
						listPlots.append(loopPlot)

	listRuins = []
	listRuins.append(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(), 'IMPROVEMENT_COTTAGE'))
	listRuins.append(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(), 'IMPROVEMENT_HAMLET'))
	listRuins.append(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(), 'IMPROVEMENT_VILLAGE'))
	listRuins.append(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(), 'IMPROVEMENT_TOWN'))

	iRuins = CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(), 'IMPROVEMENT_CITY_RUINS')

	for i in range(3):
		if len(listPlots) > 0:
			plot = listPlots[gc.getGame().getSorenRandNum(len(listPlots), "Volcano event improvement destroyed")]
			iImprovement = plot.getImprovementType()
			szBuffer = localText.getText("TXT_KEY_EVENT_CITY_IMPROVEMENT_DESTROYED", (gc.getImprovementInfo(iImprovement).getTextKey(), ))
			CyInterface().addMessage(kTriggeredData.ePlayer, False, gc.getEVENT_MESSAGE_TIME(), szBuffer, "AS2D_BOMBARDED", InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getImprovementInfo(iImprovement).getButton(), gc.getInfoTypeForString("COLOR_RED"), plot.getX(), plot.getY(), True, True)
			if iImprovement in listRuins:
				plot.setImprovementType(iRuins)
			else:
				plot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
			listPlots.remove(plot)

			if i == 1 and gc.getGame().getSorenRandNum(100, "Volcano event num improvements destroyed") < 50:
				break

######## DUSTBOWL ###########

			"""
def canTriggerDustbowlCont(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger)
	player = gc.getPlayer(kTriggeredData.ePlayer)

	kOrigTriggeredData = player.getEventOccured(trigger.getPrereqEvent(0))

	if (kOrigTriggeredData == None):
		return False

	iFarmType = CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(), 'IMPROVEMENT_FARM')
	iPlainsType = CvUtil.findInfoTypeNum(gc.getTerrainInfo,gc.getNumTerrainInfos(), 'TERRAIN_PLAINS')

	map = gc.getMap()
	iBestValue = map.getGridWidth() + map.getGridHeight()
	bestPlot = None
	for i in range(map.numPlots()):
		plot = map.plotByIndex(i)
		if (plot.getOwner() == kTriggeredData.ePlayer and plot.getImprovementType() == iFarmType and plot.getTerrainType() == iPlainsType):
			iValue = plotDistance(kOrigTriggeredData.iPlotX, kOrigTriggeredData.iPlotY, plot.getX(), plot.getY())
			if iValue < iBestValue:
				iBestValue = iValue
				bestPlot = plot

	if bestPlot != None:
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#		kActualTriggeredDataObject = player.getEventTriggered(kTriggeredData.iId)
		kActualTriggeredDataObject = player.getEventTriggered(EventTriggerTypes(kTriggeredData.eTrigger))
##--------	Unofficial Bug Fix: End Modify			--------##
		kActualTriggeredDataObject.iPlotX = bestPlot.getX()
		kActualTriggeredDataObject.iPlotY = bestPlot.getY()
	else:
		player.resetEventOccured(trigger.getPrereqEvent(0))
		return False

	return True

def getHelpDustBowl2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	szHelp = localText.getText("TXT_KEY_EVENT_DUSTBOWL_2_HELP", ())

	return szHelp
			"""

######## SALTPETER ###########

def getSaltpeterNumExtraPlots():
	map = gc.getMap()
	if map.getWorldSize() <= 1:
		return 1
	elif map.getWorldSize() <= 3:
		return 2
	elif map.getWorldSize() <= 4:
		return 3
	else:
		return 4

def getHelpSaltpeter(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	szHelp = localText.getText("TXT_KEY_EVENT_SALTPETER_HELP", (getSaltpeterNumExtraPlots(), ))

	return szHelp

def canApplySaltpeter(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	map = gc.getMap()

	player = gc.getPlayer(kTriggeredData.ePlayer)

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if (plot == None):
		return False

	iNumPlots = 0
	for i in range(map.numPlots()):
		loopPlot = map.plotByIndex(i)
		if (loopPlot.getOwner() == kTriggeredData.ePlayer and loopPlot.getFeatureType() == en.eFeatureForest and loopPlot.isHills()):
			iDistance = plotDistance(kTriggeredData.iPlotX, kTriggeredData.iPlotY, loopPlot.getX(), loopPlot.getY())
			if iDistance > 0:
				iNumPlots += 1

	return (iNumPlots >= getSaltpeterNumExtraPlots())

def applySaltpeter(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	map = gc.getMap()

	player = gc.getPlayer(kTriggeredData.ePlayer)

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if (plot == None):
		return

	listPlots = []
	for i in range(map.numPlots()):
		loopPlot = map.plotByIndex(i)
		if (loopPlot.getOwner() == kTriggeredData.ePlayer and loopPlot.getFeatureType() == en.eFeatureForest and loopPlot.isHills()):
			iDistance = plotDistance(kTriggeredData.iPlotX, kTriggeredData.iPlotY, loopPlot.getX(), loopPlot.getY())
			if iDistance > 0:
				listPlots.append((iDistance, loopPlot))

	listPlots.sort()

	iCount = getSaltpeterNumExtraPlots()
	for loopPlot in listPlots:
		if iCount == 0:
			break
		iCount -= 1
		gc.getGame().setPlotExtraYield(loopPlot[1].getX(), loopPlot[1].getY(), YieldTypes.YIELD_COMMERCE, 1)
		CyInterface().addMessage(kTriggeredData.ePlayer, False, gc.getEVENT_MESSAGE_TIME(), localText.getText("TXT_KEY_EVENT_SALTPETER_DISCOVERED", ()), "", InterfaceMessageTypes.MESSAGE_TYPE_INFO, None, gc.getInfoTypeForString("COLOR_WHITE"), loopPlot[1].getX(), loopPlot[1].getY(), True, True)

######## GREAT DEPRESSION ###########

def applyGreatDepression(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	player = gc.getPlayer(kTriggeredData.ePlayer)
	corporation = gc.getCorporationInfo(kTriggeredData.eCorporation)

	for ePlayer in range(gc.getMAX_CIV_PLAYERS()):
		loopPlayer = gc.getPlayer(ePlayer)
		if loopPlayer.isAlive():
			loopPlayer.changeGold(-loopPlayer.getGold()/4)

			if ePlayer != kTriggeredData.ePlayer:
				szText = localText.getText("TXT_KEY_EVENTTRIGGER_GREAT_DEPRESSION", (player.getCivilizationAdjectiveKey(), u"", u"", u"", u"", corporation.getTextKey()))
				szText += u"\n\n" + localText.getText("TXT_KEY_EVENT_GREAT_DEPRESSION_HELP", (25, ))
				popupInfo = CyPopupInfo()
				popupInfo.setText(szText)
				popupInfo.addPopup(ePlayer)


def getHelpGreatDepression(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	szHelp = localText.getText("TXT_KEY_EVENT_GREAT_DEPRESSION_HELP", (25, ))

	return szHelp

######## CHAMPION ###########

def canTriggerChampion(argsList):
	ePlayer, kTriggeredData = argsList

	player = gc.getPlayer(kTriggeredData.ePlayer)
	team = gc.getTeam(player.getTeam())

	if team.getAtWarCount(True) > 0:
		return False

	return True

def canUnitTriggerChampion(argsList):
	eTrigger, unit = argsList

	if unit.isNone():
		return False

	if unit.getDamage() > 0:
		return False

	if unit.getExperience() < 3:
		return False

#FfH: Modified by Kael 09/26/2007
#	iLeadership = CvUtil.findInfoTypeNum(gc.getPromotionInfo,gc.getNumPromotionInfos(), 'PROMOTION_LEADERSHIP')
	iLeadership = gc.getInfoTypeForString('PROMOTION_HERO')
#FfH: End Modify

	if unit.isHasPromotion(iLeadership):
		return False

	return True

def applyChampion(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	player = gc.getPlayer(kTriggeredData.ePlayer)
	unit = player.getUnit(kTriggeredData.iUnitId)

#FfH: Modified by Kael 10/01/2007
#	iLeadership = CvUtil.findInfoTypeNum(gc.getPromotionInfo,gc.getNumPromotionInfos(), 'PROMOTION_LEADERSHIP')
	iLeadership = gc.getInfoTypeForString('PROMOTION_HERO')
#FfH: End Modify

	unit.setHasPromotion(iLeadership, True)

def getHelpChampion(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	player = gc.getPlayer(kTriggeredData.ePlayer)
	unit = player.getUnit(kTriggeredData.iUnitId)

#FfH: Modified by Kael 09/26/2007
#	iLeadership = CvUtil.findInfoTypeNum(gc.getPromotionInfo,gc.getNumPromotionInfos(), 'PROMOTION_LEADERSHIP')
	iLeadership = gc.getInfoTypeForString('PROMOTION_HERO')
#FfH: End Modify

	szHelp = localText.getText("TXT_KEY_EVENT_CHAMPION_HELP", (unit.getNameKey(), gc.getPromotionInfo(iLeadership).getTextKey()))

	return szHelp


######## ANTELOPE ###########

def canTriggerAntelope(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iDeer = CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(), 'BONUS_DEER')
	iHappyBonuses = 0
	bDeer = False
	for i in range(gc.getNumBonusInfos()):
		bonus = gc.getBonusInfo(i)
		iNum = player.getNumAvailableBonuses(i)
		if iNum > 0:
			if bonus.getHappiness() > 0:
				iHappyBonuses += 1
				if iHappyBonuses > 5:
					return False
			if i == iDeer:
				return False

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if not plot.canHaveBonus(iDeer, False):
		return False

	return True

def doAntelope2(argsList):
#	Need this because camps are not normally allowed unless there is already deer.
	ePlayer, eEvent, kTriggeredData = argsList

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)

	if not plot.isNone():
		plot.setImprovementType(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(), 'IMPROVEMENT_CAMP'))

	return 1

def getHelpAntelope2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	iCamp = CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(), 'IMPROVEMENT_CAMP')
	szHelp = localText.getText("TXT_KEY_EVENT_IMPROVEMENT_GROWTH", ( gc.getImprovementInfo(iCamp).getTextKey(), ))

	return szHelp

######## WHALEOFATHING ###########

def canTriggerWhaleOfAThing(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iWhale = CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(), 'BONUS_WHALE')
	iHappyBonuses = 0
	bWhale = False
	for i in range(gc.getNumBonusInfos()):
		bonus = gc.getBonusInfo(i)
		iNum = player.getNumAvailableBonuses(i)
		if iNum > 0:
			if bonus.getHappiness() > 0:
				iHappyBonuses += 1
				if iHappyBonuses > 5:
					return False
			if i == iWhale:
				return False

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if not plot.canHaveBonus(iWhale, False):
		return False

	return True


######## HIYOSILVER ###########

def canTriggerHiyoSilver(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iSilver = CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(), 'BONUS_SILVER')
	iHappyBonuses = 0
	bSilver = False
	for i in range(gc.getNumBonusInfos()):
		bonus = gc.getBonusInfo(i)
		iNum = player.getNumAvailableBonuses(i)
		if iNum > 0:
			if bonus.getHappiness() > 0:
				iHappyBonuses += 1
				if iHappyBonuses > 5:
					return False
			if i == iSilver:
				return False

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if not plot.canHaveBonus(iSilver, False):
		return False

	return True

######## WININGMONKS ###########

def canTriggerWiningMonks(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	if player.getNumAvailableBonuses(CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(), 'BONUS_WINE')) > 0:
		return False

	return True


def doWiningMonks2(argsList):
#	Need this because wineries are not normally allowed unless there is already wine.
	ePlayer, eEvent, kTriggeredData = argsList

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)

	if not plot.isNone():
		plot.setImprovementType(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(), 'IMPROVEMENT_WINERY'))

	return 1

def getHelpWiningMonks2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	iImp = CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(), 'IMPROVEMENT_WINERY')
	szHelp = localText.getText("TXT_KEY_EVENT_IMPROVEMENT_GROWTH", ( gc.getImprovementInfo(iImp).getTextKey(), ))

	return szHelp

######## ANCIENT OLYMPICS ###########

def doAncientOlympics2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	for eLoopPlayer in range(gc.getMAX_CIV_PLAYERS()):
		if eLoopPlayer != kTriggeredData.ePlayer:
			pLoopPlayer = gc.getPlayer(eLoopPlayer)
			if pLoopPlayer.isAlive() and not pLoopPlayer.isMinorCiv():
				for iPlotIndex in range(gc.getMap().numPlots()):
					pPlot = gc.getMap().plotByIndex(iPlotIndex)
					if not pPlot.isWater() and pPlot.getOwner() == kTriggeredData.ePlayer and pPlot.isAdjacentPlayer(eLoopPlayer, True):
						pLoopPlayer.AI_changeMemoryCount(kTriggeredData.ePlayer, MemoryTypes.MEMORY_EVENT_GOOD_TO_US, 1)
						break

	return 1

def getHelpAncientOlympics2(argsList):
	szHelp = localText.getText("TXT_KEY_EVENT_ANCIENTOLYMPICS_HELP_2", ( 1, ))

	return szHelp


######## HEROIC_GESTURE ###########

def canTriggerHeroicGesture(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)
	destPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)

	if not gc.getTeam(destPlayer.getTeam()).canChangeWarPeace(player.getTeam()):
		return False

	if gc.getTeam(destPlayer.getTeam()).AI_getWarSuccess(player.getTeam()) <= 0:
		return False

	if gc.getTeam(player.getTeam()).AI_getWarSuccess(destPlayer.getTeam()) <= 0:
		return False

	return True

def doHeroicGesture2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	destPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	player = gc.getPlayer(kTriggeredData.ePlayer)

	if destPlayer.isHuman():
		# this works only because it's a single-player only event
		popupInfo = CyPopupInfo()
		popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
		popupInfo.setText(localText.getText("TXT_KEY_EVENT_HEROIC_GESTURE_OTHER_3", (player.getCivilizationAdjectiveKey(), )))
		popupInfo.setData1(kTriggeredData.eOtherPlayer)
		popupInfo.setData2(kTriggeredData.ePlayer)
		popupInfo.setPythonModule("CvRandomEventInterface")
		popupInfo.setOnClickedPythonCallback("heroicGesture2Callback")
		popupInfo.addPythonButton(localText.getText("TXT_KEY_POPUP_YES", ()), "")
		popupInfo.addPythonButton(localText.getText("TXT_KEY_POPUP_NO", ()), "")
		popupInfo.addPopup(kTriggeredData.eOtherPlayer)
	else:
		destPlayer.forcePeace(kTriggeredData.ePlayer)
		destPlayer.AI_changeAttitudeExtra(kTriggeredData.ePlayer, 1)
		player.AI_changeAttitudeExtra(kTriggeredData.eOtherPlayer, 1)

	return

def heroicGesture2Callback(argsList):
	iButton, iData1, iData2, iData3, iFlags, szText, bOption1, bOption2 = argsList

	if iButton == 0:
		destPlayer = gc.getPlayer(iData1)
		player = gc.getPlayer(iData2)
		destPlayer.forcePeace(iData2)
		destPlayer.AI_changeAttitudeExtra(iData2, 1)
		player.AI_changeAttitudeExtra(iData1, 1)

	return 0

def getHelpHeroicGesture2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	destPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)

	# Get help text
	szHelp = localText.getText("TXT_KEY_EVENT_ATTITUDE_GOOD", (1, destPlayer.getNameKey()));

	return szHelp

######## GREAT_MEDIATOR ###########

def canTriggerGreatMediator(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)
	destPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)

	if not gc.getTeam(player.getTeam()).canChangeWarPeace(destPlayer.getTeam()):
		return False

	if gc.getTeam(player.getTeam()).AI_getAtWarCounter(destPlayer.getTeam()) < 10:
		return False

	return True

def doGreatMediator2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	destPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	player = gc.getPlayer(kTriggeredData.ePlayer)

	if destPlayer.isHuman():
		# this works only because it's a single-player only event
		popupInfo = CyPopupInfo()
		popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
		popupInfo.setText(localText.getText("TXT_KEY_EVENT_GREAT_MEDIATOR_OTHER_3", (player.getCivilizationAdjectiveKey(), )))
		popupInfo.setData1(kTriggeredData.eOtherPlayer)
		popupInfo.setData2(kTriggeredData.ePlayer)
		popupInfo.setPythonModule("CvRandomEventInterface")
		popupInfo.setOnClickedPythonCallback("greatMediator2Callback")
		popupInfo.addPythonButton(localText.getText("TXT_KEY_POPUP_YES", ()), "")
		popupInfo.addPythonButton(localText.getText("TXT_KEY_POPUP_NO", ()), "")
		popupInfo.addPopup(kTriggeredData.eOtherPlayer)
	else:
		gc.getTeam(player.getTeam()).makePeace(destPlayer.getTeam())
		destPlayer.AI_changeAttitudeExtra(kTriggeredData.ePlayer, 1)
		player.AI_changeAttitudeExtra(kTriggeredData.eOtherPlayer, 1)

	return

def greatMediator2Callback(argsList):
	iButton, iData1, iData2, iData3, iFlags, szText, bOption1, bOption2 = argsList

	if iButton == 0:
		destPlayer = gc.getPlayer(iData1)
		player = gc.getPlayer(iData2)
		gc.getTeam(destPlayer.getTeam()).makePeace(player.getTeam())
		destPlayer.AI_changeAttitudeExtra(iData2, 1)
		player.AI_changeAttitudeExtra(iData1, 1)

	return 0

def getHelpGreatMediator2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	destPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)

	# Get help text
	szHelp = localText.getText("TXT_KEY_EVENT_ATTITUDE_GOOD", (1, destPlayer.getNameKey()));

	return szHelp

######## ANCIENT_TEXTS ###########

def doAncientTexts2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	for ePlayer in range(gc.getMAX_CIV_PLAYERS()):
		loopPlayer = gc.getPlayer(ePlayer)
		if loopPlayer.isAlive() and ePlayer != kTriggeredData.ePlayer:
			loopTeam = gc.getTeam(loopPlayer.getTeam())
			if loopTeam.isHasMet(gc.getPlayer(kTriggeredData.ePlayer).getTeam()):
				loopPlayer.AI_changeAttitudeExtra(kTriggeredData.ePlayer, 1)

	return

def getHelpAncientTexts2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	szHelp = localText.getText("TXT_KEY_EVENT_SOLO_FLIGHT_HELP_1", (1, ))

	return szHelp


######## IMPACT_CRATER ###########

def canTriggerImpactCrater(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iUranium = CvUtil.findInfoTypeNum(gc.getBonusInfo,gc.getNumBonusInfos(), 'BONUS_URANIUM')
	if player.getNumAvailableBonuses(iUranium) > 0:
		return False

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if not plot.canHaveBonus(iUranium, False):
		return False

	return True

def doImpactCrater2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)

	if not plot.isNone():
		plot.setImprovementType(CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(), 'IMPROVEMENT_MINE'))

	return 1

def getHelpImpactCrater2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	iMine = CvUtil.findInfoTypeNum(gc.getImprovementInfo,gc.getNumImprovementInfos(), 'IMPROVEMENT_MINE')
	szHelp = localText.getText("TXT_KEY_EVENT_IMPROVEMENT_GROWTH", ( gc.getImprovementInfo(iMine).getTextKey(), ))

	return szHelp


######## THE_HUNS ###########

def canTriggerTheHuns(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

#   If Barbarians are disabled in this game, this event will not occur.
	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_BARBARIANS):
		return False

#   At least one civ on the board must know Horseback Riding.
	bFoundValid = False
	iTech = CvUtil.findInfoTypeNum(gc.getTechInfo, gc.getNumTechInfos(), 'TECH_HORSEBACK_RIDING')
	for ePlayer in range(gc.getMAX_CIV_PLAYERS()):
		loopPlayer = gc.getPlayer(ePlayer)
		if loopPlayer.isAlive():
			if gc.getTeam(loopPlayer.getTeam()).isHasTech(iTech):
				bFoundValid = True
				break

	if not bFoundValid:
		return False

#   At least one civ on the board must know Iron Working.
	bFoundValid = False
	iTech = CvUtil.findInfoTypeNum(gc.getTechInfo, gc.getNumTechInfos(), 'TECH_IRON_WORKING')
	for ePlayer in range(gc.getMAX_CIV_PLAYERS()):
		loopPlayer = gc.getPlayer(ePlayer)
		if loopPlayer.isAlive():
			if gc.getTeam(loopPlayer.getTeam()).isHasTech(iTech):
				bFoundValid = True
				break

	if not bFoundValid:
		return False

	# Can we build the counter unit?
	iCounterUnitClass = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_SPEARMAN')
	iCounterUnit = gc.getCivilizationInfo(player.getCivilizationType()).getCivilizationUnits(iCounterUnitClass)
	if iCounterUnit == -1:
		return False

	(loopCity, iter) = player.firstCity(False)
	bFound = False
	while(loopCity):
		if (loopCity.canTrain(iCounterUnit, False, False)):
			bFound = True
			break

		(loopCity, iter) = player.nextCity(iter, False)

	if not bFound:
		return False

#	Find an eligible plot
	map = gc.getMap()
	for i in range(map.numPlots()):
		plot = map.plotByIndex(i)
		if (plot.getOwner() == -1 and not plot.isWater() and not plot.isImpassable() and plot.area().getCitiesPerPlayer(kTriggeredData.ePlayer) > 0 and plot.isAdjacentPlayer(kTriggeredData.ePlayer, True)):
			return True

	return False


def getHelpTheHuns1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	szHelp = localText.getText("TXT_KEY_EVENT_THE_HUNS_HELP_1", ())

	return szHelp


def applyTheHuns1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	listPlots = []
	map = gc.getMap()
	for i in range(map.numPlots()):
		plot = map.plotByIndex(i)
		if (plot.getOwner() == -1 and not plot.isWater() and not plot.isImpassable() and plot.area().getCitiesPerPlayer(kTriggeredData.ePlayer) > 0 and plot.isAdjacentPlayer(kTriggeredData.ePlayer, True)):
			listPlots.append(i)

	if 0 == len(listPlots):
		return

	plot = map.plotByIndex(listPlots[gc.getGame().getSorenRandNum(len(listPlots), "Hun event location")])

	if map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_DUEL'):
		iNumUnits  = 1
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_TINY'):
		iNumUnits  = 2
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_SMALL'):
		iNumUnits  = 3
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_STANDARD'):
		iNumUnits  = 4
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_LARGE'):
		iNumUnits  = 5
	else:
		iNumUnits  = 6

	iUnitType = CvUtil.findInfoTypeNum(gc.getUnitInfo, gc.getNumUnitInfos(), 'UNIT_HORSE_ARCHER')

	pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
	for i in range(iNumUnits):
		pBarbarianPlayer.initUnit(iUnitType, plot.getX(), plot.getY(), UnitAITypes.UNITAI_ATTACK_CITY, DirectionTypes.DIRECTION_SOUTH)


######## THE_VANDALS ###########

def canTriggerTheVandals(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

#   If Barbarians are disabled in this game, this event will not occur.
	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_BARBARIANS):
		return False

#   At least one civ on the board must know Metal Casting.
	bFoundValid = False
	iTech = CvUtil.findInfoTypeNum(gc.getTechInfo, gc.getNumTechInfos(), 'TECH_METAL_CASTING')
	for ePlayer in range(gc.getMAX_CIV_PLAYERS()):
		loopPlayer = gc.getPlayer(ePlayer)
		if loopPlayer.isAlive():
			if gc.getTeam(loopPlayer.getTeam()).isHasTech(iTech):
				bFoundValid = True
				break

	if not bFoundValid:
		return False

#   At least one civ on the board must know Iron Working.
	bFoundValid = False
	iTech = CvUtil.findInfoTypeNum(gc.getTechInfo, gc.getNumTechInfos(), 'TECH_IRON_WORKING')
	for ePlayer in range(gc.getMAX_CIV_PLAYERS()):
		loopPlayer = gc.getPlayer(ePlayer)
		if loopPlayer.isAlive():
			if gc.getTeam(loopPlayer.getTeam()).isHasTech(iTech):
				bFoundValid = True
				break

	if not bFoundValid:
		return False

	# Can we build the counter unit?
	iCounterUnitClass = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_AXEMAN')
	iCounterUnit = gc.getCivilizationInfo(player.getCivilizationType()).getCivilizationUnits(iCounterUnitClass)
	if iCounterUnit == -1:
		return False

	(loopCity, iter) = player.firstCity(False)
	bFound = False
	while(loopCity):
		if (loopCity.canTrain(iCounterUnit, False, False)):
			bFound = True
			break

		(loopCity, iter) = player.nextCity(iter, False)

	if not bFound:
		return False

#	Find an eligible plot
	map = gc.getMap()
	for i in range(map.numPlots()):
		plot = map.plotByIndex(i)
		if (plot.getOwner() == -1 and not plot.isWater() and not plot.isImpassable() and plot.area().getCitiesPerPlayer(kTriggeredData.ePlayer) > 0 and plot.isAdjacentPlayer(kTriggeredData.ePlayer, True)):
			return True

	return False


def getHelpTheVandals1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	szHelp = localText.getText("TXT_KEY_EVENT_THE_VANDALS_HELP_1", ())

	return szHelp


def applyTheVandals1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	listPlots = []
	map = gc.getMap()
	for i in range(map.numPlots()):
		plot = map.plotByIndex(i)
		if (plot.getOwner() == -1 and not plot.isWater() and not plot.isImpassable() and plot.area().getCitiesPerPlayer(kTriggeredData.ePlayer) > 0 and plot.isAdjacentPlayer(kTriggeredData.ePlayer, True)):
			listPlots.append(i)

	if 0 == len(listPlots):
		return

	plot = map.plotByIndex(listPlots[gc.getGame().getSorenRandNum(len(listPlots), "Vandal event location")])

	if map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_DUEL'):
		iNumUnits  = 1
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_TINY'):
		iNumUnits  = 2
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_SMALL'):
		iNumUnits  = 3
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_STANDARD'):
		iNumUnits  = 4
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_LARGE'):
		iNumUnits  = 5
	else:
		iNumUnits  = 6

	iUnitType = CvUtil.findInfoTypeNum(gc.getUnitInfo, gc.getNumUnitInfos(), 'UNIT_SWORDSMAN')

	pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
	for i in range(iNumUnits):
		pBarbarianPlayer.initUnit(iUnitType, plot.getX(), plot.getY(), UnitAITypes.UNITAI_ATTACK_CITY, DirectionTypes.DIRECTION_SOUTH)


######## THE_GOTHS ###########

def canTriggerTheGoths(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

#   If Barbarians are disabled in this game, this event will not occur.
	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_BARBARIANS):
		return False

#   At least one civ on the board must know Mathematics.
	bFoundValid = False
	iTech = CvUtil.findInfoTypeNum(gc.getTechInfo, gc.getNumTechInfos(), 'TECH_MATHEMATICS')
	for ePlayer in range(gc.getMAX_CIV_PLAYERS()):
		loopPlayer = gc.getPlayer(ePlayer)
		if loopPlayer.isAlive():
			if gc.getTeam(loopPlayer.getTeam()).isHasTech(iTech):
				bFoundValid = True
				break

	if not bFoundValid:
		return False

#   At least one civ on the board must know Iron Working.
	bFoundValid = False
	iTech = CvUtil.findInfoTypeNum(gc.getTechInfo, gc.getNumTechInfos(), 'TECH_IRON_WORKING')
	for ePlayer in range(gc.getMAX_CIV_PLAYERS()):
		loopPlayer = gc.getPlayer(ePlayer)
		if loopPlayer.isAlive():
			if gc.getTeam(loopPlayer.getTeam()).isHasTech(iTech):
				bFoundValid = True
				break

	if not bFoundValid:
		return False

	# Can we build the counter unit?
	iCounterUnitClass = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_CHARIOT')
	iCounterUnit = gc.getCivilizationInfo(player.getCivilizationType()).getCivilizationUnits(iCounterUnitClass)
	if iCounterUnit == -1:
		return False

	(loopCity, iter) = player.firstCity(False)
	bFound = False
	while(loopCity):
		if (loopCity.canTrain(iCounterUnit, False, False)):
			bFound = True
			break

		(loopCity, iter) = player.nextCity(iter, False)

	if not bFound:
		return False

#	Find an eligible plot
	map = gc.getMap()
	for i in range(map.numPlots()):
		plot = map.plotByIndex(i)
		if (plot.getOwner() == -1 and not plot.isWater() and not plot.isImpassable() and plot.area().getCitiesPerPlayer(kTriggeredData.ePlayer) > 0 and plot.isAdjacentPlayer(kTriggeredData.ePlayer, True)):
			return True

	return False


def getHelpTheGoths1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	szHelp = localText.getText("TXT_KEY_EVENT_THE_GOTHS_HELP_1", ())

	return szHelp


def applyTheGoths1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	listPlots = []
	map = gc.getMap()
	for i in range(map.numPlots()):
		plot = map.plotByIndex(i)
		if (plot.getOwner() == -1 and not plot.isWater() and not plot.isImpassable() and plot.area().getCitiesPerPlayer(kTriggeredData.ePlayer) > 0 and plot.isAdjacentPlayer(kTriggeredData.ePlayer, True)):
			listPlots.append(i)

	if 0 == len(listPlots):
		return

	plot = map.plotByIndex(listPlots[gc.getGame().getSorenRandNum(len(listPlots), "Goth event location")])

	if map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_DUEL'):
		iNumUnits  = 1
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_TINY'):
		iNumUnits  = 2
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_SMALL'):
		iNumUnits  = 3
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_STANDARD'):
		iNumUnits  = 4
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_LARGE'):
		iNumUnits  = 5
	else:
		iNumUnits  = 6

	iUnitType = CvUtil.findInfoTypeNum(gc.getUnitInfo, gc.getNumUnitInfos(), 'UNIT_AXEMAN')

	pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
	for i in range(iNumUnits):
		pBarbarianPlayer.initUnit(iUnitType, plot.getX(), plot.getY(), UnitAITypes.UNITAI_ATTACK_CITY, DirectionTypes.DIRECTION_SOUTH)


######## THE_PHILISTINES ###########

def canTriggerThePhilistines(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

#   If Barbarians are disabled in this game, this event will not occur.
	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_BARBARIANS):
		return False

#   At least one civ on the board must know Monotheism.
	bFoundValid = False
	iTech = CvUtil.findInfoTypeNum(gc.getTechInfo, gc.getNumTechInfos(), 'TECH_MONOTHEISM')
	for ePlayer in range(gc.getMAX_CIV_PLAYERS()):
		loopPlayer = gc.getPlayer(ePlayer)
		if loopPlayer.isAlive():
			if gc.getTeam(loopPlayer.getTeam()).isHasTech(iTech):
				bFoundValid = True
				break

	if not bFoundValid:
		return False

#   At least one civ on the board must know Bronze Working.
	bFoundValid = False
	iTech = CvUtil.findInfoTypeNum(gc.getTechInfo, gc.getNumTechInfos(), 'TECH_BRONZE_WORKING')
	for ePlayer in range(gc.getMAX_CIV_PLAYERS()):
		loopPlayer = gc.getPlayer(ePlayer)
		if loopPlayer.isAlive():
			if gc.getTeam(loopPlayer.getTeam()).isHasTech(iTech):
				bFoundValid = True
				break

	if not bFoundValid:
		return False

	# Can we build the counter unit?
	iCounterUnitClass = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_AXEMAN')
	iCounterUnit = gc.getCivilizationInfo(player.getCivilizationType()).getCivilizationUnits(iCounterUnitClass)
	if iCounterUnit == -1:
		return False

	(loopCity, iter) = player.firstCity(False)
	bFound = False
	while(loopCity):
		if (loopCity.canTrain(iCounterUnit, False, False)):
			bFound = True
			break

		(loopCity, iter) = player.nextCity(iter, False)

	if not bFound:
		return False

#	Find an eligible plot
	map = gc.getMap()
	for i in range(map.numPlots()):
		plot = map.plotByIndex(i)
		if (plot.getOwner() == -1 and not plot.isWater() and not plot.isImpassable() and plot.area().getCitiesPerPlayer(kTriggeredData.ePlayer) > 0 and plot.isAdjacentPlayer(kTriggeredData.ePlayer, True)):
			return True

	return False


def getHelpThePhilistines1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	szHelp = localText.getText("TXT_KEY_EVENT_THE_PHILISTINES_HELP_1", ())

	return szHelp


def applyThePhilistines1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	listPlots = []
	map = gc.getMap()
	for i in range(map.numPlots()):
		plot = map.plotByIndex(i)
		if (plot.getOwner() == -1 and not plot.isWater() and not plot.isImpassable() and plot.area().getCitiesPerPlayer(kTriggeredData.ePlayer) > 0 and plot.isAdjacentPlayer(kTriggeredData.ePlayer, True)):
			listPlots.append(i)

	if 0 == len(listPlots):
		return

	plot = map.plotByIndex(listPlots[gc.getGame().getSorenRandNum(len(listPlots), "Philistine event location")])

	if map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_DUEL'):
		iNumUnits  = 1
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_TINY'):
		iNumUnits  = 2
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_SMALL'):
		iNumUnits  = 3
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_STANDARD'):
		iNumUnits  = 4
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_LARGE'):
		iNumUnits  = 5
	else:
		iNumUnits  = 6

	iUnitType = CvUtil.findInfoTypeNum(gc.getUnitInfo, gc.getNumUnitInfos(), 'UNIT_SPEARMAN')

	pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
	for i in range(iNumUnits):
		pBarbarianPlayer.initUnit(iUnitType, plot.getX(), plot.getY(), UnitAITypes.UNITAI_ATTACK_CITY, DirectionTypes.DIRECTION_SOUTH)


######## THE_VEDIC_ARYANS ###########

def canTriggerTheVedicAryans(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

#   If Barbarians are disabled in this game, this event will not occur.
	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_BARBARIANS):
		return False

#   At least one civ on the board must know Polytheism.
	bFoundValid = False
	iTech = CvUtil.findInfoTypeNum(gc.getTechInfo, gc.getNumTechInfos(), 'TECH_POLYTHEISM')
	for ePlayer in range(gc.getMAX_CIV_PLAYERS()):
		loopPlayer = gc.getPlayer(ePlayer)
		if loopPlayer.isAlive():
			if gc.getTeam(loopPlayer.getTeam()).isHasTech(iTech):
				bFoundValid = True
				break

	if not bFoundValid:
		return False

#   At least one civ on the board must know Archery.
	bFoundValid = False
	iTech = CvUtil.findInfoTypeNum(gc.getTechInfo, gc.getNumTechInfos(), 'TECH_ARCHERY')
	for ePlayer in range(gc.getMAX_CIV_PLAYERS()):
		loopPlayer = gc.getPlayer(ePlayer)
		if loopPlayer.isAlive():
			if gc.getTeam(loopPlayer.getTeam()).isHasTech(iTech):
				bFoundValid = True
				break

	if not bFoundValid:
		return False

	# Can we build the counter unit?
	iCounterUnitClass = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_ARCHER')
	iCounterUnit = gc.getCivilizationInfo(player.getCivilizationType()).getCivilizationUnits(iCounterUnitClass)
	if iCounterUnit == -1:
		return False

	(loopCity, iter) = player.firstCity(False)
	bFound = False
	while(loopCity):
		if (loopCity.canTrain(iCounterUnit, False, False)):
			bFound = True
			break

		(loopCity, iter) = player.nextCity(iter, False)

	if not bFound:
		return False

#	Find an eligible plot
	map = gc.getMap()
	for i in range(map.numPlots()):
		plot = map.plotByIndex(i)
		if (plot.getOwner() == -1 and not plot.isWater() and not plot.isImpassable() and plot.area().getCitiesPerPlayer(kTriggeredData.ePlayer) > 0 and plot.isAdjacentPlayer(kTriggeredData.ePlayer, True)):
			return True

	return False


def getHelpTheVedicAryans1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	szHelp = localText.getText("TXT_KEY_EVENT_THE_VEDIC_ARYANS_HELP_1", ())

	return szHelp


def applyTheVedicAryans1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	listPlots = []
	map = gc.getMap()
	for i in range(map.numPlots()):
		plot = map.plotByIndex(i)
		if (plot.getOwner() == -1 and not plot.isWater() and not plot.isImpassable() and plot.area().getCitiesPerPlayer(kTriggeredData.ePlayer) > 0 and plot.isAdjacentPlayer(kTriggeredData.ePlayer, True)):
			listPlots.append(i)

	if 0 == len(listPlots):
		return

	plot = map.plotByIndex(listPlots[gc.getGame().getSorenRandNum(len(listPlots), "Vedic Aryan event location")])

	if map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_DUEL'):
		iNumUnits  = 1
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_TINY'):
		iNumUnits  = 2
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_SMALL'):
		iNumUnits  = 3
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_STANDARD'):
		iNumUnits  = 4
	elif map.getWorldSize() == CvUtil.findInfoTypeNum(gc.getWorldInfo, gc.getNumWorldInfos(), 'WORLDSIZE_LARGE'):
		iNumUnits  = 5
	else:
		iNumUnits  = 6

	iUnitType = CvUtil.findInfoTypeNum(gc.getUnitInfo, gc.getNumUnitInfos(), 'UNIT_ARCHER')

	pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
	for i in range(iNumUnits):
		pBarbarianPlayer.initUnit(iUnitType, plot.getX(), plot.getY(), UnitAITypes.UNITAI_ATTACK_CITY, DirectionTypes.DIRECTION_SOUTH)

######## SECURITY_TAX ###########

def canTriggerSecurityTax(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iWalls = CvUtil.findInfoTypeNum(gc.getBuildingClassInfo, gc.getNumBuildingClassInfos(), 'BUILDINGCLASS_WALLS')
	if player.getNumCities() > player.getBuildingClassCount(iWalls):
		return False

	return True


######## LITERACY ###########

def canTriggerLiteracy(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iLibrary = CvUtil.findInfoTypeNum(gc.getBuildingClassInfo, gc.getNumBuildingClassInfos(), 'BUILDINGCLASS_LIBRARY')
	if player.getNumCities() > player.getBuildingClassCount(iLibrary):
		return False

	return True

######## TEA ###########

def canTriggerTea(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	if player.isCivic(CvUtil.findInfoTypeNum(gc.getCivicInfo,gc.getNumCivicInfos(), 'CIVIC_MERCANTILISM')):
		return False

	bCanTrade = False
	for iLoopPlayer in range(gc.getMAX_CIV_PLAYERS()):
		if player.canHaveTradeRoutesWith(iLoopPlayer):
			bCanTrade = True
			break

	if not bCanTrade:
		return False

	return True

######## HORSE WHISPERING ###########

def canTriggerHorseWhispering(argsList):
	ePlayer, kTriggeredData = argsList

	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and gc.getPlayer(kTriggeredData.ePlayer).isHuman():
		return False

	return True

def getHelpHorseWhispering1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	map = gc.getMap()

	iNumStables = gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers()
	szHelp = localText.getText("TXT_KEY_EVENT_HORSE_WHISPERING_HELP", (iNumStables, ))

	return szHelp

def canTriggerHorseWhisperingDone(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iStable = CvUtil.findInfoTypeNum(gc.getBuildingClassInfo, gc.getNumBuildingClassInfos(), 'BUILDINGCLASS_STABLE')
	if gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() > player.getBuildingClassCount(iStable):
		return False

	return True

def getHelpHorseWhisperingDone1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	map = gc.getMap()

	iNumUnits = gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers()
	szHelp = localText.getText("TXT_KEY_EVENT_HORSE_WHISPERING_DONE_HELP_1", (iNumUnits, ))

	return szHelp

def applyHorseWhisperingDone1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	map = gc.getMap()
	plot = map.plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	iNumUnits = gc.getWorldInfo(map.getWorldSize()).getDefaultPlayers()
	iUnitClassType = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_HORSE_ARCHER')
	iUnitType = gc.getCivilizationInfo(player.getCivilizationType()).getCivilizationUnits(iUnitClassType)

	if iUnitType != -1:
		for i in range(iNumUnits):
			player.initUnit(iUnitType, plot.getX(), plot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)

######## HARBORMASTER ###########

def getHelpHarbormaster1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	iHarborsRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	iCaravelsRequired = iHarborsRequired / 2 + 1

	szHelp = localText.getText("TXT_KEY_EVENT_HARBORMASTER_HELP", (iHarborsRequired, iCaravelsRequired))

	return szHelp


def canTriggerHarbormaster(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and gc.getPlayer(kTriggeredData.ePlayer).isHuman():
		return False

	map = gc.getMap()

	iNumWater = 0

	for i in range(map.numPlots()):
		plot = map.plotByIndex(i)

		if plot.isWater():
			iNumWater += 1

		if 100 * iNumWater >= 40 * map.numPlots():
			return True

	return False

def canTriggerHarbormasterDone(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iHarbor = CvUtil.findInfoTypeNum(gc.getBuildingClassInfo, gc.getNumBuildingClassInfos(), 'BUILDINGCLASS_HARBOR')
	iHarborsRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	if iHarborsRequired > player.getBuildingClassCount(iHarbor):
		return False

	iCaravel = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_CARAVEL')
	iCaravelsRequired = iHarborsRequired / 2 + 1
	if iCaravelsRequired > player.getUnitClassCount(iCaravel):
		return False

	return True

######## CLASSIC LITERATURE ###########

def canTriggerClassicLiterature(argsList):
	ePlayer, kTriggeredData = argsList

	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and gc.getPlayer(kTriggeredData.ePlayer).isHuman():
		return False

	return True

def getHelpClassicLiterature1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	iLibrariesRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()

	szHelp = localText.getText("TXT_KEY_EVENT_CLASSIC_LITERATURE_HELP_1", (iLibrariesRequired, ))

	return szHelp


def canTriggerClassicLiteratureDone(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iLibrary = CvUtil.findInfoTypeNum(gc.getBuildingClassInfo, gc.getNumBuildingClassInfos(), 'BUILDINGCLASS_LIBRARY')
	iBuildingsRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	if iBuildingsRequired > player.getBuildingClassCount(iLibrary):
		return False

	return True

def getHelpClassicLiteratureDone2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	szHelp = localText.getText("TXT_KEY_EVENT_CLASSIC_LITERATURE_DONE_HELP_2", ( ))

	return szHelp

def canApplyClassicLiteratureDone2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iEraAncient = CvUtil.findInfoTypeNum(gc.getEraInfo, gc.getNumEraInfos(), 'ERA_ANCIENT')

	for iTech in range(gc.getNumTechInfos()):
		if gc.getTechInfo(iTech).getEra() == iEraAncient and player.canResearch(iTech, False):
			return True

	return False

def applyClassicLiteratureDone2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iEraAncient = CvUtil.findInfoTypeNum(gc.getEraInfo, gc.getNumEraInfos(), 'ERA_ANCIENT')

	listTechs = []
	for iTech in range(gc.getNumTechInfos()):
		if gc.getTechInfo(iTech).getEra() == iEraAncient and player.canResearch(iTech, False):
			listTechs.append(iTech)

	if len(listTechs) > 0:
		iTech = listTechs[gc.getGame().getSorenRandNum(len(listTechs), "Classic Literature Event Tech selection")]
		gc.getTeam(player.getTeam()).setHasTech(iTech, True, kTriggeredData.ePlayer, True, True)

def getHelpClassicLiteratureDone3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iSpecialist = CvUtil.findInfoTypeNum(gc.getSpecialistInfo, gc.getNumSpecialistInfos(), 'SPECIALIST_SCIENTIST', )
	iGreatLibrary = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_GREAT_LIBRARY')

	szCityName = u""
	(loopCity, iter) = player.firstCity(False)
	while(loopCity):
		if (loopCity.isHasBuilding(iGreatLibrary)):
			szCityName = loopCity.getNameKey()
			break

		(loopCity, iter) = player.nextCity(iter, False)

	szHelp = localText.getText("TXT_KEY_EVENT_FREE_SPECIALIST", (1, gc.getSpecialistInfo(iSpecialist).getTextKey(), szCityName))

	return szHelp

def canApplyClassicLiteratureDone3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iGreatLibrary = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_GREAT_LIBRARY')

	(loopCity, iter) = player.firstCity(False)
	while(loopCity):
		if (loopCity.isHasBuilding(iGreatLibrary)):
			return True

		(loopCity, iter) = player.nextCity(iter, False)

	return False

def applyClassicLiteratureDone3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iSpecialist = CvUtil.findInfoTypeNum(gc.getSpecialistInfo, gc.getNumSpecialistInfos(), 'SPECIALIST_SCIENTIST', )
	iGreatLibrary = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_GREAT_LIBRARY')

	(loopCity, iter) = player.firstCity(False)
	while(loopCity):
		if (loopCity.isHasBuilding(iGreatLibrary)):
			loopCity.changeFreeSpecialistCount(iSpecialist, 1)
			return

		(loopCity, iter) = player.nextCity(iter, False)

######## THE BEST DEFENSE ###########

def canTriggerBestDefense(argsList):
	ePlayer, kTriggeredData = argsList

	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and gc.getPlayer(kTriggeredData.ePlayer).isHuman():
		return False

	return True

def getHelpBestDefense1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()

	szHelp = localText.getText("TXT_KEY_EVENT_BEST_DEFENSE_HELP_1", (iRequired, ))

	return szHelp

def canTriggerBestDefenseDone(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iCastle = CvUtil.findInfoTypeNum(gc.getBuildingClassInfo, gc.getNumBuildingClassInfos(), 'BUILDINGCLASS_CASTLE')
	iBuildingsRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	if iBuildingsRequired > player.getBuildingClassCount(iCastle):
		return False

	return True

def getHelpBestDefenseDone2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	szHelp = localText.getText("TXT_KEY_EVENT_BEST_DEFENSE_DONE_HELP_2", (3, ))

	return szHelp

def applyBestDefenseDone2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	for ePlayer in range(gc.getMAX_CIV_PLAYERS()):
		loopPlayer = gc.getPlayer(ePlayer)
		if loopPlayer.isAlive() and ePlayer != kTriggeredData.ePlayer:
			loopTeam = gc.getTeam(loopPlayer.getTeam())
			if loopTeam.isHasMet(gc.getPlayer(kTriggeredData.ePlayer).getTeam()):
				loopPlayer.AI_changeAttitudeExtra(kTriggeredData.ePlayer, 3)


def canApplyBestDefenseDone3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iGreatWall = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_GREAT_WALL')

	(loopCity, iter) = player.firstCity(False)
	while(loopCity):
		if (loopCity.isHasBuilding(iGreatWall)):
			return True

		(loopCity, iter) = player.nextCity(iter, False)

	return False

######## NATIONAL SPORTS LEAGUE ###########

def canTriggerSportsLeague(argsList):
	ePlayer, kTriggeredData = argsList

	if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and gc.getPlayer(kTriggeredData.ePlayer).isHuman():
		return False

	return True
def getHelpSportsLeague1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	iBuilding = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_STATUE_OF_ZEUS')

	szHelp = localText.getText("TXT_KEY_EVENT_SPORTS_LEAGUE_HELP_1", (iRequired, gc.getBuildingInfo(iBuilding).getTextKey()))

	return szHelp

def canTriggerSportsLeagueDone(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iCastle = CvUtil.findInfoTypeNum(gc.getBuildingClassInfo, gc.getNumBuildingClassInfos(), 'BUILDINGCLASS_COLOSSEUM')
	iBuildingsRequired = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	if iBuildingsRequired > player.getBuildingClassCount(iCastle):
		return False

	return True

def canApplySportsLeagueDone3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iZeus = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_STATUE_OF_ZEUS')

	(loopCity, iter) = player.firstCity(False)
	while(loopCity):
		if (loopCity.isHasBuilding(iZeus)):
			return True

		(loopCity, iter) = player.nextCity(iter, False)

	return False

######## ESTEEMEED_PLAYWRIGHT ###########

def canTriggerEsteemedPlaywright(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	# If source civ is operating this Civic, disallow the event to trigger.
	if player.isCivic(CvUtil.findInfoTypeNum(gc.getCivicInfo,gc.getNumCivicInfos(), 'CIVIC_SLAVERY')):
		return False

	return True


######## SECRET_KNOWLEDGE ###########

def getHelpSecretKnowledge2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	szHelp = localText.getText("TXT_KEY_EVENT_YIELD_CHANGE_BUILDING", (gc.getBuildingInfo(kTriggeredData.eBuilding).getTextKey(), u"+4[ICON_CULTURE]"))

	return szHelp

def applySecretKnowledge2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	city = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	city.setBuildingCommerceChange(gc.getBuildingInfo(kTriggeredData.eBuilding).getBuildingClassType(), CommerceTypes.COMMERCE_CULTURE, 4)

######## HIGH_WARLORD ###########

def canTriggerHighWarlord(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	# If source civ is operating this Civic, disallow the event to trigger.
	if player.isCivic(CvUtil.findInfoTypeNum(gc.getCivicInfo,gc.getNumCivicInfos(), 'CIVIC_EMANCIPATION')):
		return False

	return True


######## EXPERIENCED_CAPTAIN ###########

def canTriggerExperiencedCaptain(argsList):
	ePlayer, kTriggeredData = argsList

	player = gc.getPlayer(kTriggeredData.ePlayer)
	unit = player.getUnit(kTriggeredData.iUnitId)

	if unit.isNone():
		return False

	if unit.getExperience() < 7:
		return False

	return True

######## PARTISANS ###########

def getNumPartisanUnits(plot, ePlayer):
	for i in range(gc.getNumCultureLevelInfos()):
		iI = gc.getNumCultureLevelInfos() - i - 1
		if plot.getCulture(ePlayer) >= gc.getCultureLevelInfo(iI).getSpeedThreshold(gc.getGame().getGameSpeedType()):
			return iI
	return 0

def getHelpPartisans1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)
	capital = player.getCapitalCity()
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)

	if None != capital and not capital.isNone():
		iNumUnits = getNumPartisanUnits(plot, kTriggeredData.ePlayer)
		szUnit = gc.getUnitInfo(capital.getConscriptUnit()).getTextKey()

		szHelp = localText.getText("TXT_KEY_EVENT_PARTISANS_HELP_1", (iNumUnits, szUnit))

	return szHelp

def canApplyPartisans1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)

	if getNumPartisanUnits(plot, kTriggeredData.ePlayer) <= 0:
		return False

	for i in range(3):
		for j in range(3):
			loopPlot = gc.getMap().plot(kTriggeredData.iPlotX + i - 1, kTriggeredData.iPlotY + j - 1)
			if None != loopPlot and not loopPlot.isNone():
				if not (loopPlot.isVisibleEnemyUnit(kTriggeredData.ePlayer) or loopPlot.isWater() or loopPlot.isImpassable() or loopPlot.isCity()):
					return True
	return False


def applyPartisans1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)
	capital = player.getCapitalCity()
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)

	if None != capital and not capital.isNone():
		iNumUnits = getNumPartisanUnits(plot, kTriggeredData.ePlayer)

		listPlots = []
		for i in range(3):
			for j in range(3):
				loopPlot = gc.getMap().plot(kTriggeredData.iPlotX + i - 1, kTriggeredData.iPlotY + j - 1)
				if None != loopPlot and not loopPlot.isNone() and (i != 1 or j != 1):
					if not (loopPlot.isVisibleEnemyUnit(kTriggeredData.ePlayer) or loopPlot.isWater() or loopPlot.isImpassable()):
						listPlots.append(loopPlot)

		if len(listPlots) > 0:
			for i in range(iNumUnits):
				iPlot = gc.getGame().getSorenRandNum(len(listPlots), "Partisan event placement")
				player.initUnit(capital.getConscriptUnit(), listPlots[iPlot].getX(), listPlots[iPlot].getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)

def getHelpPartisans2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)
	capital = player.getCapitalCity()
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)

	if None != capital and not capital.isNone():
		iNumUnits = max(1, getNumPartisanUnits(plot, kTriggeredData.ePlayer) / 2)
		szUnit = gc.getUnitInfo(capital.getConscriptUnit()).getTextKey()

		szHelp = localText.getText("TXT_KEY_EVENT_PARTISANS_HELP_2", (iNumUnits, szUnit, capital.getNameKey()))

	return szHelp

def canApplyPartisans2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)

	return (max(1, getNumPartisanUnits(plot, kTriggeredData.ePlayer) / 2) > 0)

def applyPartisans2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)
	capital = player.getCapitalCity()
	plot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)

	if None != capital and not capital.isNone():
		iNumUnits = max(1, getNumPartisanUnits(plot, kTriggeredData.ePlayer) / 2)
		for i in range(iNumUnits):
			player.initUnit(capital.getConscriptUnit(), capital.getX(), capital.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)

######## ELITE SWORDSMEN ###########

def getHelpEliteSwords1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() + 1
	szHelp = localText.getText("TXT_KEY_EVENT_ELITE_SWORDS_HELP_1", (iNumUnits, ))

	return szHelp

def canTriggerEliteSwordsDone(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() + 1
	iUnitClassType = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_SWORDSMAN')
	if player.getUnitClassCount(iUnitClassType) < iNumUnits:
		return False

	return True


def canApplyEliteSwordsDone2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iCivic = CvUtil.findInfoTypeNum(gc.getCivicInfo,gc.getNumCivicInfos(), 'CIVIC_HEREDITARY_RULE')

	if not player.isCivic(iCivic):
		return False

	return True

######## WARSHIPS ###########

def canTriggerWarships(argsList):
	ePlayer, kTriggeredData = argsList

	map = gc.getMap()
	iNumWater = 0

	for i in range(map.numPlots()):
		plot = map.plotByIndex(i)

		if plot.isWater():
			iNumWater += 1

		if 100 * iNumWater >= 55 * map.numPlots():
			return True

	return False

def getHelpWarships1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()

	iBuilding = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_GREAT_LIGHTHOUSE')
	szHelp = localText.getText("TXT_KEY_EVENT_WARSHIPS_HELP_1", (iNumUnits, gc.getBuildingInfo(iBuilding).getTextKey()))

	return szHelp

def canTriggerWarshipsDone(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers()
	iUnitClassType = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_TRIREME')

	if player.getUnitClassCount(iUnitClassType) < iNumUnits:
		return False

	return True


def canApplyWarshipsDone2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iBuilding = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_GREAT_LIGHTHOUSE')
	if player.getBuildingClassCount(gc.getBuildingInfo(iBuilding).getBuildingClassType()) == 0:
		return False

	return True

######## GUNS NOT BUTTER ###########

def getHelpGunsButter1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() + 1
	iBuilding = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_TAJ_MAHAL')

	szHelp = localText.getText("TXT_KEY_EVENT_GUNS_BUTTER_HELP_1", (iNumUnits, gc.getBuildingInfo(iBuilding).getTextKey()))

	return szHelp

def canTriggerGunsButterDone(argsList):
	ePlayer, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iNumUnits = gc.getWorldInfo(gc.getMap().getWorldSize()).getDefaultPlayers() + 1
	iUnitClassType = CvUtil.findInfoTypeNum(gc.getUnitClassInfo, gc.getNumUnitClassInfos(), 'UNITCLASS_MUSKETMAN')

	if player.getUnitClassCount(iUnitClassType) < iNumUnits:
		return False

	return True


def canApplyGunsButterDone2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iCivic = CvUtil.findInfoTypeNum(gc.getCivicInfo,gc.getNumCivicInfos(), 'CIVIC_VASSALAGE')

	if not player.isCivic(iCivic):
		return False

	return True

def canApplyGunsButterDone3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	iBuilding = CvUtil.findInfoTypeNum(gc.getBuildingInfo, gc.getNumBuildingInfos(), 'BUILDING_TAJ_MAHAL')
	if player.getBuildingClassCount(gc.getBuildingInfo(iBuilding).getBuildingClassType()) == 0:
		return False

	return True


######## Great Beast ########

def doGreatBeast3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList

	player = gc.getPlayer(kTriggeredData.ePlayer)
	(loopCity, iter) = player.firstCity(False)

	while(loopCity):
		if loopCity.isHasReligion(kTriggeredData.eReligion):
			loopCity.changeHappinessTimer(40)
		(loopCity, iter) = player.nextCity(iter, False)

def getHelpGreatBeast3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	religion = gc.getReligionInfo(kTriggeredData.eReligion)

	szHelp = localText.getText("TXT_KEY_EVENT_GREAT_BEAST_3_HELP", (gc.getDefineINT("TEMP_HAPPY"), 40, religion.getChar()))

	return szHelp

####### Comet Fragment ########

def canDoCometFragment(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	if (player.getSpaceProductionModifier()) > 10:
		return False

	return True

####### Immigrants ########

def canTriggerImmigrantCity(argsList):
	eTrigger, city = argsList

	if city.isNone():
		return False

	if ((city.happyLevel() - city.unhappyLevel(0) < 1) or (city.goodHealth() - city.badHealth(True) < 1)):
		return False

	if (city.getCommerceRateTimes100(CommerceTypes.COMMERCE_CULTURE) < 5500):
		return False

####### Controversial Philosopher ######

def canCityTriggerControversialPhilosopher(argsList):
	eTrigger, city = argsList

	if city.isNone():
		return False
	if (not city.isCapital()):
		return False
	if (city.getCommerceRateTimes100(CommerceTypes.COMMERCE_RESEARCH) < 3500):
		return False

	return True


##--------		Unofficial Bug Fix: Deleted by Denev	--------##
	"""
######## Toxcatl (Aztec event) #########

def canTriggerToxcatl(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	player = gc.getPlayer(kTriggeredData.ePlayer)

	if (player.getCivilizationType() == gc.getInfoTypeForString("CIVILIZATION_AZTEC")):
		return True
	return False
	"""
##--------		Unofficial Bug Fix: End Delete			--------##

######## Republic Election ########

def removeRepublicTraits(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	cf.removeTemporaryTraits(kTriggeredData.ePlayer, TraitSourceTypes.TRAITSOURCE_ELECTION)

def doElectionSupportHawk(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	pCapital = pPlayer.getCapitalCity()
	iCapitalX = pCapital.getX()
	iCapitalY = pCapital.getY()

	if CyGame().getSorenRandNum(100, "Election") < 20:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_OPPOSITION_PARTY_WINS", ()), 'AS2D_SOMNIUM_LOSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)

	elif pPlayer.hasTrait(en.eTraitRaiders):
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_COMMANDER'), iCapitalX, iCapitalY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HAWK_WINS_ALREADY_RAIDERS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorWhite, iCapitalX, iCapitalY, True, True)

	else:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HAWK_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitRaiders).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		pPlayer.setHasTraitWithSource(en.eTraitRaiders, True, TraitSourceTypes.TRAITSOURCE_ELECTION)


def getHelpElectionSupportHawk(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	iWin = 80
	iLose = 100 - iWin

	if pPlayer.hasTrait(en.eTraitRaiders):
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_ALREADY", (iWin, gc.getUnitInfo(gc.getInfoTypeForString('UNIT_COMMANDER')).getTextKey()))
	else:
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iWin, gc.getTraitInfo(en.eTraitRaiders).getTextKey()))
	szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_LOSE", (iLose, ))

	return szHelp


def doElectionSupportDove(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	if CyGame().getSorenRandNum(100, "Election") < 20:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_OPPOSITION_PARTY_WINS", ()), 'AS2D_SOMNIUM_LOSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)

	elif pPlayer.hasTrait(en.eTraitDefender):
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_DOVE_WINS_ALREADY_DEFENSIVE", (3,)), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		doElectionDoveWinsAlreadyDefensive(ePlayer)

	else:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_DOVE_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitDefender).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		pPlayer.setHasTraitWithSource(en.eTraitDefender, True, TraitSourceTypes.TRAITSOURCE_ELECTION)

def getHelpElectionSupportDove(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	iWin = 80
	iLose = 100 - iWin

	if pPlayer.hasTrait(en.eTraitDefender):
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_DOVE_ALREADY_DEFENSIVE", (iWin, 3))
	else:
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iWin, gc.getTraitInfo(en.eTraitDefender).getTextKey()))
	szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_LOSE", (iLose, ))

	return szHelp

def doElectionFairHawkVsDove(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	pCapital = pPlayer.getCapitalCity()
	iCapitalX = pCapital.getX()
	iCapitalY = pCapital.getY()

	if CyGame().getSorenRandNum(100, "Election") < 50:
		if pPlayer.hasTrait(en.eTraitRaiders):
			pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_COMMANDER'), iCapitalX, iCapitalY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HAWK_WINS_ALREADY_RAIDERS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorWhite, iCapitalX, iCapitalY, True, True)
		else:
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HAWK_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitRaiders).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			pPlayer.setHasTraitWithSource(en.eTraitRaiders, True, TraitSourceTypes.TRAITSOURCE_ELECTION)

	else:
		if pPlayer.hasTrait(en.eTraitDefender):
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_DOVE_WINS_ALREADY_DEFENSIVE", (3,)), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			doElectionDoveWinsAlreadyDefensive(ePlayer)
		else:
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_DOVE_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitDefender).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			pPlayer.setHasTraitWithSource(en.eTraitDefender, True, TraitSourceTypes.TRAITSOURCE_ELECTION)


def getHelpElectionFairHawkVsDove(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	szHelp = u""

	iFormerWin = 50
	iLatterWin = 100 - iFormerWin

	if pPlayer.hasTrait(en.eTraitRaiders):
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_ALREADY", (iFormerWin, gc.getUnitInfo(gc.getInfoTypeForString('UNIT_COMMANDER')).getTextKey()))
	else:
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iFormerWin, gc.getTraitInfo(en.eTraitRaiders).getTextKey()))

	szHelp += u"\n"

	if pPlayer.hasTrait(en.eTraitDefender):
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_DOVE_ALREADY_DEFENSIVE", (iLatterWin, 3))
	else:
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iLatterWin, gc.getTraitInfo(en.eTraitDefender).getTextKey()))

	return szHelp

##

def doElectionSupportLandOwner(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	pCapital = pPlayer.getCapitalCity()
	iCapitalX = pCapital.getX()
	iCapitalY = pCapital.getY()

	if CyGame().getSorenRandNum(100, "Election") < 20:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_OPPOSITION_PARTY_WINS", ()), 'AS2D_SOMNIUM_LOSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)

	elif pPlayer.hasTrait(en.eTraitFinancial):
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_MERCHANT'), iCapitalX, iCapitalY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_LANDOWNER_WINS_ALREADY_FINANCIAL", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorWhite, iCapitalX, iCapitalY, True, True)

	else:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_LANDOWNER_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitFinancial).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		pPlayer.setHasTraitWithSource(en.eTraitFinancial, True, TraitSourceTypes.TRAITSOURCE_ELECTION)


def getHelpElectionSupportLandOwner(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	iWin = 80
	iLose = 100 - iWin

	if pPlayer.hasTrait(en.eTraitFinancial):
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_ALREADY", (iWin, gc.getUnitInfo(gc.getInfoTypeForString('UNIT_MERCHANT')).getTextKey()))
	else:
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iWin, gc.getTraitInfo(en.eTraitFinancial).getTextKey()))
	szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_LOSE", (iLose, ))

	return szHelp


def doElectionSupportPeasant(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	if CyGame().getSorenRandNum(100, "Election") < 20:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_OPPOSITION_PARTY_WINS", ()), 'AS2D_SOMNIUM_LOSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)

	elif pPlayer.hasTrait(en.eTraitExpansive):
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_PEASANT_WINS_ALREADY_EXPANSIVE", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		doElectionPeasantWinsAlreadyExpansive(ePlayer)

	else:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_PEASANT_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitExpansive).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		pPlayer.setHasTraitWithSource(en.eTraitExpansive, True, TraitSourceTypes.TRAITSOURCE_ELECTION)


def getHelpElectionSupportPeasant(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	iWin = 80
	iLose = 100 - iWin

	if pPlayer.hasTrait(en.eTraitExpansive):
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_PEASANT_ALREADY_EXPANSIVE", (iWin, ))
	else:
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iWin, gc.getTraitInfo(en.eTraitExpansive).getTextKey()))
	szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_LOSE", (iLose, ))

	return szHelp

def doElectionFairLandOwnerVsPeasant(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	pCapital = pPlayer.getCapitalCity()
	iCapitalX = pCapital.getX()
	iCapitalY = pCapital.getY()

	if CyGame().getSorenRandNum(100, "Election") < 50:
		if pPlayer.hasTrait(en.eTraitFinancial):
			pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_MERCHANT'), iCapitalX, iCapitalY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_LANDOWNER_WINS_ALREADY_FINANCIAL", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorWhite, iCapitalX, iCapitalY, True, True)
		else:
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_LANDOWNER_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitFinancial).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			pPlayer.setHasTraitWithSource(en.eTraitFinancial, True, TraitSourceTypes.TRAITSOURCE_ELECTION)

	else:
		if pPlayer.hasTrait(en.eTraitExpansive):
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_PEASANT_WINS_ALREADY_EXPANSIVE", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			doElectionPeasantWinsAlreadyExpansive(ePlayer)
		else:
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_PEASANT_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitExpansive).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			pPlayer.setHasTraitWithSource(en.eTraitExpansive, True, TraitSourceTypes.TRAITSOURCE_ELECTION)

	return


def getHelpElectionFairLandOwnerVsPeasant(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	szHelp = u""

	iFormerWin = 50
	iLatterWin = 100 - iFormerWin

	if pPlayer.hasTrait(en.eTraitFinancial):
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_ALREADY", (iFormerWin, gc.getUnitInfo(gc.getInfoTypeForString('UNIT_MERCHANT')).getTextKey()))
	else:
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iFormerWin, gc.getTraitInfo(en.eTraitFinancial).getTextKey()))

	szHelp += u"\n"

	if pPlayer.hasTrait(en.eTraitExpansive):
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_PEASANT_ALREADY_EXPANSIVE", (iLatterWin, ))
	else:
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iLatterWin, gc.getTraitInfo(en.eTraitExpansive).getTextKey()))

	return szHelp

##

def doElectionSupportChurch(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	pCapital = pPlayer.getCapitalCity()
	iCapitalX = pCapital.getX()
	iCapitalY = pCapital.getY()

	if CyGame().getSorenRandNum(100, "Election") < 20:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_OPPOSITION_PARTY_WINS", ()), 'AS2D_SOMNIUM_LOSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)

	elif pPlayer.hasTrait(en.eTraitSpiritual):
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_PROPHET'), iCapitalX, iCapitalY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_CHURCH_WINS_ALREADY_SPIRITUAL", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorWhite, iCapitalX, iCapitalY, True, True)

	else:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_CHURCH_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitSpiritual).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		pPlayer.setHasTraitWithSource(en.eTraitSpiritual, True, TraitSourceTypes.TRAITSOURCE_ELECTION)


def getHelpElectionSupportChurch(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	iWin = 80
	iLose = 100 - iWin

	if pPlayer.hasTrait(en.eTraitSpiritual):
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_ALREADY", (iWin, gc.getUnitInfo(gc.getInfoTypeForString('UNIT_PROPHET')).getTextKey()))
	else:
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iWin, gc.getTraitInfo(en.eTraitSpiritual).getTextKey()))
	szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_LOSE", (iLose, ))

	return szHelp


def doElectionSupportState(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	if CyGame().getSorenRandNum(100, "Election") < 20:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_OPPOSITION_PARTY_WINS", ()), 'AS2D_SOMNIUM_LOSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)

	elif pPlayer.hasTrait(en.eTraitOrganized):
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_STATE_WINS_ALREADY_ORGANIZED", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		pPlayer.changeGoldenAgeTurns(CyGame().goldenAgeLength())

	else:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_STATE_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitOrganized).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		pPlayer.setHasTraitWithSource(en.eTraitOrganized, True, TraitSourceTypes.TRAITSOURCE_ELECTION)


def getHelpElectionSupportState(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	iWin = 80
	iLose = 100 - iWin

	if pPlayer.hasTrait(en.eTraitOrganized):
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_STATE_ALREADY_ORGANIZED", (iWin, ))
	else:
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iWin, gc.getTraitInfo(en.eTraitOrganized).getTextKey()))
	szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_LOSE", (iLose, ))

	return szHelp

def doElectionFairChurchVsState(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	pCapital = pPlayer.getCapitalCity()
	iCapitalX = pCapital.getX()
	iCapitalY = pCapital.getY()

	if CyGame().getSorenRandNum(100, "Election") < 50:
		if pPlayer.hasTrait(en.eTraitSpiritual):
			pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_PROPHET'), iCapitalX, iCapitalY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_CHURCH_WINS_ALREADY_SPIRITUAL", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorWhite, iCapitalX, iCapitalY, True, True)
		else:
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_CHURCH_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitSpiritual).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			pPlayer.setHasTraitWithSource(en.eTraitSpiritual, True, TraitSourceTypes.TRAITSOURCE_ELECTION)

	else:
		if pPlayer.hasTrait(en.eTraitOrganized):
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_STATE_WINS_ALREADY_ORGANIZED", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			pPlayer.changeGoldenAgeTurns(CyGame().goldenAgeLength())
		else:
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_STATE_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitOrganized).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			pPlayer.setHasTraitWithSource(en.eTraitOrganized, True, TraitSourceTypes.TRAITSOURCE_ELECTION)

	return

def getHelpElectionFairChurchVsState(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	szHelp = u""

	iFormerWin = 50
	iLatterWin = 100 - iFormerWin

	if pPlayer.hasTrait(en.eTraitSpiritual):
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_ALREADY", (iWin, gc.getUnitInfo(gc.getInfoTypeForString('UNIT_PROPHET')).getTextKey()))
	else:
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iFormerWin, gc.getTraitInfo(en.eTraitSpiritual).getTextKey()))

	szHelp += u"\n"

	if pPlayer.hasTrait(en.eTraitOrganized):
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_STATE_ALREADY_ORGANIZED", (iLatterWin, ))
	else:
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iLatterWin, gc.getTraitInfo(en.eTraitOrganized).getTextKey()))

	return szHelp
##

def doElectionSupportLabor(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	pCapital = pPlayer.getCapitalCity()
	iCapitalX = pCapital.getX()
	iCapitalY = pCapital.getY()

	if CyGame().getSorenRandNum(100, "Election") < 20:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_OPPOSITION_PARTY_WINS", ()), 'AS2D_SOMNIUM_LOSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)

	elif pPlayer.hasTrait(en.eTraitIndustrious):
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ENGINEER'), iCapitalX, iCapitalY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_LABOR_WINS_ALREADY_INDUSTRIOUS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorWhite, iCapitalX, iCapitalY, True, True)

	else:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_LABOR_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitIndustrious).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		pPlayer.setHasTraitWithSource(en.eTraitIndustrious, True, TraitSourceTypes.TRAITSOURCE_ELECTION)


def getHelpElectionSupportLabor(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	iWin = 80
	iLose = 100 - iWin

	if pPlayer.hasTrait(en.eTraitIndustrious):
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_ALREADY", (iWin, gc.getUnitInfo(gc.getInfoTypeForString('UNIT_ENGINEER')).getTextKey()))
	else:
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iWin, gc.getTraitInfo(en.eTraitIndustrious).getTextKey()))
	szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_LOSE", (iLose, ))

	return szHelp


def doElectionSupportAcademia(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	pCapital = pPlayer.getCapitalCity()
	iCapitalX = pCapital.getX()
	iCapitalY = pCapital.getY()

	if CyGame().getSorenRandNum(100, "Election") < 20:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_OPPOSITION_PARTY_WINS", ()), 'AS2D_SOMNIUM_LOSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)

	elif pPlayer.hasTrait(en.eTraitPhilosophical):
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_SCIENTIST'), iCapitalX, iCapitalY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_ACADEMIA_WINS_ALREADY_PHILOSOPHICAL", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorWhite, iCapitalX, iCapitalY, True, True)

	else:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_ACADEMIA_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitPhilosophical).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		pPlayer.setHasTraitWithSource(en.eTraitPhilosophical, True, TraitSourceTypes.TRAITSOURCE_ELECTION)


def getHelpElectionSupportAcademia(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	iWin = 80
	iLose = 100 - iWin

	if pPlayer.hasTrait(en.eTraitPhilosophical):
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_ALREADY", (iWin, gc.getUnitInfo(gc.getInfoTypeForString('UNIT_SCIENTIST')).getTextKey()))
	else:
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iWin, gc.getTraitInfo(en.eTraitPhilosophical).getTextKey()))
	szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_LOSE", (iLose, ))

	return szHelp

def doElectionFairLaborVsAcademia(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	pCapital = pPlayer.getCapitalCity()
	iCapitalX = pCapital.getX()
	iCapitalY = pCapital.getY()

	if CyGame().getSorenRandNum(100, "Election") < 50:
		if pPlayer.hasTrait(en.eTraitIndustrious):
			pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ENGINEER'), iCapitalX, iCapitalY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_LABOR_WINS_ALREADY_INDUSTRIOUS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorWhite, iCapitalX, iCapitalY, True, True)
		else:
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_LABOR_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitIndustrious).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			pPlayer.setHasTraitWithSource(en.eTraitIndustrious, True, TraitSourceTypes.TRAITSOURCE_ELECTION)

	else:
		if pPlayer.hasTrait(en.eTraitPhilosophical):
			pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_SCIENTIST'), iCapitalX, iCapitalY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_ACADEMIA_WINS_ALREADY_PHILOSOPHICAL", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorWhite, iCapitalX, iCapitalY, True, True)
		else:
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_ACADEMIA_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitPhilosophical).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			pPlayer.setHasTraitWithSource(en.eTraitPhilosophical, True, TraitSourceTypes.TRAITSOURCE_ELECTION)

	return


def getHelpElectionFairLaborVsAcademia(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	szHelp = u""

	iFormerWin = 50
	iLatterWin = 100 - iFormerWin

	if pPlayer.hasTrait(en.eTraitIndustrious):
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_ALREADY", (iFormerWin, gc.getUnitInfo(gc.getInfoTypeForString('UNIT_ENGINEER')).getTextKey()))
	else:
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iFormerWin, gc.getTraitInfo(en.eTraitIndustrious).getTextKey()))

	szHelp += u"\n"

	if pPlayer.hasTrait(en.eTraitPhilosophical):
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_ALREADY", (iLatterWin, gc.getUnitInfo(gc.getInfoTypeForString('UNIT_SCIENTIST')).getTextKey()))
	else:
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iLatterWin, gc.getTraitInfo(en.eTraitPhilosophical).getTextKey()))

	return szHelp

##

def doElectionSupportMight(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	if CyGame().getSorenRandNum(100, "Election") < 20:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_OPPOSITION_PARTY_WINS", ()), 'AS2D_SOMNIUM_LOSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)

	elif pPlayer.hasTrait(en.eTraitAggressive):
		iBonusExperience = 3
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_MIGHT_WINS_ALREADY_AGGRESSIVE", (iBonusExperience, )), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		doElectionMightWinsAlreadyAggressive(ePlayer)

	else:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_MIGHT_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitAggressive).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		pPlayer.setHasTraitWithSource(en.eTraitAggressive, True, TraitSourceTypes.TRAITSOURCE_ELECTION)


def getHelpElectionSupportMight(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	iWin = 80
	iLose = 100 - iWin

	if pPlayer.hasTrait(en.eTraitAggressive):
		iBonusExperience = 3
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_MIGHT_ALREADY_AGGRESSIVE", (iWin, iBonusExperience))
	else:
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iWin, gc.getTraitInfo(en.eTraitAggressive).getTextKey()))
	szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_LOSE", (iLose, ))

	return szHelp


def doElectionSupportMagic(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	pCapital = pPlayer.getCapitalCity()
	iCapitalX = pCapital.getX()
	iCapitalY = pCapital.getY()

	if CyGame().getSorenRandNum(100, "Election") < 20:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_OPPOSITION_PARTY_WINS", ()), 'AS2D_SOMNIUM_LOSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)

	elif pPlayer.hasTrait(en.eTraitArcane):
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ARCHMAGE'), iCapitalX, iCapitalY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit.changeFreePromotionPick(4)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_MAGIC_WINS_ALREADY_ARCANE", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorWhite, iCapitalX, iCapitalY, True, True)

	else:
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_MAGIC_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitArcane).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
		pPlayer.setHasTraitWithSource(en.eTraitArcane, True, TraitSourceTypes.TRAITSOURCE_ELECTION)

def getHelpElectionSupportMagic(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	iWin = 80
	iLose = 100 - iWin

	if pPlayer.hasTrait(en.eTraitArcane):
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_ALREADY", (iWin, gc.getUnitInfo(gc.getInfoTypeForString('UNIT_ARCHMAGE')).getTextKey()))
	else:
		szHelp = localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iWin, gc.getTraitInfo(en.eTraitArcane).getTextKey()))
	szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_LOSE", (iLose, ))

	return szHelp

def doElectionFairMightVsMagic(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	pCapital = pPlayer.getCapitalCity()
	iCapitalX = pCapital.getX()
	iCapitalY = pCapital.getY()

	if CyGame().getSorenRandNum(100, "Election") < 50:
		if pPlayer.hasTrait(en.eTraitAggressive):
			iBonusExperience = 3
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_MIGHT_WINS_ALREADY_AGGRESSIVE", (iBonusExperience, )), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			doElectionMightWinsAlreadyAggressive(ePlayer)
		else:
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_MIGHT_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitAggressive).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			pPlayer.setHasTraitWithSource(en.eTraitAggressive, True, TraitSourceTypes.TRAITSOURCE_ELECTION)

	else:
		if pPlayer.hasTrait(en.eTraitArcane):
			eArchMage = gc.getCivilizationInfo(pPlayer.getCivilizationType()).getCivilizationUnits(gc.getInfoTypeForString('UNITCLASS_ARCHMAGE'))
			if eArchMage == UnitTypes.NO_UNIT:
				eArchMage = gc.getInfoTypeForString('UNIT_ARCHMAGE')
			pNewUnit = pPlayer.initUnit(eArchMage, iCapitalX, iCapitalY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit.changeFreePromotionPick(2)
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_MAGIC_WINS_ALREADY_ARCANE", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorWhite, iCapitalX, iCapitalY, True, True)
		else:
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_MAGIC_WINS", ()), 'AS2D_WELOVEKING', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			CyInterface().addMessage(ePlayer, False, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_GAINS_TRAIT", (gc.getTraitInfo(en.eTraitArcane).getTextKey(), )), 'AS2D_SOMNIUM_APPLAUSE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, '', en.eColorWhite, -1, -1, False, False)
			pPlayer.setHasTraitWithSource(en.eTraitArcane, True, TraitSourceTypes.TRAITSOURCE_ELECTION)


def getHelpElectionFairMightVsMagic(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)

	szHelp = u""

	iFormerWin = 50
	iLatterWin = 100 - iFormerWin

	if pPlayer.hasTrait(en.eTraitAggressive):
		iBonusExperience = 3
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_MIGHT_ALREADY_AGGRESSIVE", (iLatterWin, iBonusExperience))
	else:
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iFormerWin, gc.getTraitInfo(en.eTraitAggressive).getTextKey()))

	szHelp += u"\n"

	if pPlayer.hasTrait(en.eTraitArcane):
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL_ALREADY", (iFormerWin, gc.getUnitInfo(gc.getInfoTypeForString('UNIT_ARCHMAGE')).getTextKey()))
	else:
		szHelp += localText.getText("TXT_KEY_EVENT_REPUBLIC_ELECTION_HELP_SUPPORT_GENERAL", (iLatterWin, gc.getTraitInfo(en.eTraitArcane).getTextKey()))

	return szHelp


def doElectionDoveWinsAlreadyDefensive(ePlayer):
	pPlayer = gc.getPlayer(ePlayer)
	eTeam = pPlayer.getTeam()
	for eLoopPlayer in range(gc.getMAX_CIV_PLAYERS()):
		pLoopPlayer = gc.getPlayer(eLoopPlayer)
		if pLoopPlayer.isAlive():
			eLoopTeam = pLoopPlayer.getTeam()
			if eLoopTeam != eTeam:
				if gc.getTeam(eLoopTeam).isHasMet(eTeam):
					pLoopPlayer.AI_changeAttitudeExtra(ePlayer, 3)
					pPlayer.AI_changeAttitudeExtra(eLoopPlayer, 3)


def doElectionPeasantWinsAlreadyExpansive(ePlayer):
	iGameSpeedPercent = gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent()
	iHappy = cyFlatValue(24, iGameSpeedPercent, True)
	iHealth = cyFlatValue(6, iGameSpeedPercent, True)
	for pyCity in PyPlayer(ePlayer).getCityList():
		pCity = pyCity.GetCy()
		pCity.changeHappinessTimer(iHappy)
		pCity.changeEspionageHealthCounter(-iHealth)


def doElectionMightWinsAlreadyAggressive(ePlayer):
	for pUnit in PyPlayer(ePlayer).getUnitList():
		if pUnit.getUnitCombatType() != UnitCombatTypes.NO_UNITCOMBAT:
			if pUnit.canFight():
				iBonusExperience = 3
				pUnit.changeExperience(iBonusExperience, -1, False, False, False)

# Kaijin OAC >>> Start

##More Events Mod starts

def applyGela2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pPlayer.setGuildPlusCounter(1, 2)

def applyGela3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pPlayer.setGuildPlusCounter(1, 3)

def applyGela4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pPlayer.setGuildPlusCounter(1, 4)

def applyGela5(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pPlayer.setGuildPlusCounter(1, 5)

def applyGela6(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pPlayer.setGuildPlusCounter(1, 6)

def applyGela7(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pPlayer.setGuildPlusCounter(1, 7)

def canDoGela2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iImp = gc.getInfoTypeForString('IMPROVEMENT_POOL_OF_TEARS')
	iCount = 0
	for i in range(CyMap().getNumAreas()):
		iCount += CyMap().getArea(i).getNumImprovements(iImp)
	if iCount == 0:
		return False
	return True

def canDoGela3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iImp = gc.getInfoTypeForString('IMPROVEMENT_MAELSTROM')
	iCount = 0
	for i in range(CyMap().getNumAreas()):
		iCount += CyMap().getArea(i).getNumImprovements(iImp)
	if iCount == 0:
		return False
	return True

def canDoGela4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer2 = cf.getCivilization(gc.getInfoTypeForString('CIVILIZATION_MERCURIANS'))
	if iPlayer2 != -1:
		return True
	return False

def canDoGela5(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iImp = gc.getInfoTypeForString('IMPROVEMENT_PYRE_OF_THE_SERAPHIC')
	iCount = 0
	for i in range(CyMap().getNumAreas()):
		iCount += CyMap().getArea(i).getNumImprovements(iImp)
	if iCount == 0:
		return False
	return True

def canDoGela6(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iImp = gc.getInfoTypeForString('IMPROVEMENT_BROKEN_SEPULCHER')
	iCount = 0
	for i in range(CyMap().getNumAreas()):
		iCount += CyMap().getArea(i).getNumImprovements(iImp)
	if iCount == 0:
		return False
	return True

def canDoGela7(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iImp = gc.getInfoTypeForString('IMPROVEMENT_MIRROR_OF_HEAVEN')
	iCount = 0
	for i in range(CyMap().getNumAreas()):
		iCount += CyMap().getArea(i).getNumImprovements(iImp)
	if iCount == 0:
		return False
	return True

def doStrangeAdept(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ADEPT'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENTROPY1'), True)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEATH1'), True)

def helpStrangeAdept(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_STRANGE_ADEPT_HELP", ())
	return szHelp

def canDoHellRefugees(argsList):
	ePlayer, kTriggeredData = argsList
	for iPlayer2 in range(gc.getMAX_PLAYERS()):
		pPlayer2 = gc.getPlayer(iPlayer2)
		if (pPlayer2.isAlive()):
			if pPlayer2.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_INFERNAL'):
				return True
	return False

def doHellRefugees3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_CHAMPION'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BLESSED'), True)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON_SLAYING'), True)
	pNewUnit2 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_CHAMPION'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit2.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BLESSED'), True)
	pNewUnit2.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON_SLAYING'), True)

def canDoHellRefugees4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	if CyGame().getGlobalCounter() >35 :
		return True
	return False

def doHellRefugees4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_HIGH_PRIEST_OF_THE_ORDER'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

def doHellRefugees5(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	
	eTeam = gc.getTeam(pPlayer.getTeam())
	for iPlayer2 in range(gc.getMAX_PLAYERS()):
		pPlayer2 = gc.getPlayer(iPlayer2)
		if (pPlayer2.isAlive() and pPlayer2 != pPlayer  and iPlayer2 != gc.getBARBARIAN_PLAYER()):
			iReligion = pPlayer2.getStateReligion()
			if iReligion == gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL'):
				i2Team = gc.getPlayer(iPlayer2).getTeam()
				if eTeam.isAtWar(i2Team):
					eTeam.makePeace(i2Team)	

def helpHellRefugees3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_HELL_REFUGEES_3_HELP", ())
	return szHelp

def helpHellRefugees4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_HELL_REFUGEES_4_HELP", ())
	return szHelp

def canDoScholars4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_BARBARIAN')):
		return True
	return False

def doTrappedFrostlings2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	pPlot = pCity.plot()

	iUnit = gc.getInfoTypeForString('UNIT_FROSTLING')
	eFrostlingsPlayer = gc.getInfoTypeForString('BARBARIAN_FROSTLING') + gc.getBARBARIAN_PLAYER()
	pFrostlingsPlayer = gc.getPlayer(eFrostlingsPlayer)
	pTargetPlot = cf.findAdjacentClearPlot(eFrostlingsPlayer, pPlot.getX(), pPlot.getY(), False, True)
	if pTargetPlot is not None:
		pNewUnit = pFrostlingsPlayer.initUnit(iUnit, pTargetPlot.getX(), pTargetPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

def canDoTrappedFrostlings3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	if pCity.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_FREAK_SHOW')) == 0:
		return False
	return True

def doTrappedFrostlings5(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	iUnit = gc.getInfoTypeForString('UNIT_FROSTLING')
	pNewUnit = pPlayer.initUnit(iUnit, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STRONG'), True)

def helpTrappedFrostlings5(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_TRAPPED_FROSTLINGS_5_HELP", ())
	return szHelp

def canTriggerTrappedFrostlings(argsList):
	ePlayer, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	pPlot = pCity.plot()

	lpRangedPlots = cyGetRangedPlots(pPlot, pCity.getPlotRadius() + 1, False, False, TeamTypes.NO_TEAM)
	for pTargetPlot in lpRangedPlots:
		if not pTargetPlot.isWater():
			if pTargetPlot.getTerrainType() in (en.eTerrainTundra, en.eTerrainSnow):
				return True
	return False

def doPacifistDemonstration2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	destPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	eTeam = gc.getTeam(pPlayer.getTeam())
	eTeam.changeWarWeariness(pPlayer.getTeam(),25)

def helpPacifistDemonstration2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_PACIFIST_DEMONSTRATION_2_HELP", ())
	return szHelp

def doPacifistDemonstration3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	for i in range(pCity.plot().getNumUnits()):
		pUnit = pCity.plot().getUnit(i)
		pUnit.changeExperience(3, -1, False, False, False)

def helpPacifistDemonstration3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_PACIFIST_DEMONSTRATION_3_HELP", ())
	return szHelp

def canDoPacifistDemonstration4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_BARBARIAN')):
		return True
	return False

def doPacifistDemonstration4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_AXEMAN'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAK'), True)

def helpPacifistDemonstration4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_PACIFIST_DEMONSTRATION_4_HELP", ())
	return szHelp

def doPacifistDemonstration5(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	destPlayer = gc.getPlayer(kTriggeredData.eOtherPlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	eTeam = gc.getTeam(pPlayer.getTeam())
	eTeam.changeWarWeariness(pPlayer.getTeam(),-10)
	for i in range(pCity.plot().getNumUnits()):
		pUnit = pCity.plot().getUnit(i)
		if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_VAMPIRE')):
			pUnit.changeExperience(3, -1, False, False, False)

def helpPacifistDemonstration5(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_PACIFIST_DEMONSTRATION_5_HELP", ())
	return szHelp

def canTriggerDemonSign(argsList):
	ePlayer, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	if (pPlayer.getCivilizationType() == gc.getInfoTypeForString("CIVILIZATION_MERCURIANS")):
		return False
	if (pPlayer.getCivilizationType() == gc.getInfoTypeForString("CIVILIZATION_INFERNAL")):
		return False
	return True

def doDemonSign2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_PROPHET'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

def doDemonSign3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_HIGH_PRIEST_OF_THE_VEIL'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PROPHECY_MARK'), True)

def doDemonSign5(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_CHAMPION'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PROPHECY_MARK'), True)

def doDemonSign6(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_LUONNOTAR'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

def helpDemonSign2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_DEMON_SIGN_2_HELP", ())
	return szHelp

def helpDemonSign3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_DEMON_SIGN_3_HELP", ())
	return szHelp

def helpDemonSign5(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_DEMON_SIGN_5_HELP", ())
	return szHelp

def helpDemonSign6(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_DEMON_SIGN_6_HELP", ())
	return szHelp

def canDoAshCough2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	if (pPlayer.getCivilizationType() == gc.getInfoTypeForString("CIVILIZATION_SHEAIM")):
		return True
	if (pPlayer.getCivilizationType() == gc.getInfoTypeForString("CIVILIZATION_KURIOTATES")):
		return True
	return False

def canDoAshCough4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	if pCity.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_MAGE_GUILD')) == 0:
		return False
	return True

def doAshCough4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	if CyGame().getSorenRandNum(100, "Cough")< 50 :
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ADEPT'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FIRE1'), True)
		pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENTROPY1'), True)
	else:
		pCity.changeHurryAngerTimer(10)

def helpAshCough4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_ASH_COUGH_4_HELP", ())
	return szHelp

def canDoDeadAngel2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if pPlayer.getAlignment() == gc.getInfoTypeForString('ALIGNMENT_EVIL'):
		return False
	return True

def doDeadAngel4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	iFeature = pPlot.getFeatureType()
	iBonus = pPlot.getBonusType(TeamTypes.NO_TEAM)
	pPlot.setPlotCounter(100)
	if iBonus != BonusTypes.NO_BONUS:
		if gc.getImprovementInfo(en.eImprovementFarm).isImprovementBonusTrade(iBonus):
			pPlot.setImprovementType(en.eImprovementSnakePillar)
	if iFeature == en.eFeatureFloodPlains:
		pPlot.setFeatureType(en.eFeatureObsidianPlains, 0)

def doDeadAngel5(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	pTargetPlot = cf.findAdjacentClearPlot(ePlayer, pPlot.getX(), pPlot.getY(), False, True)
	if pTargetPlot is not None:
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ANGEL'), pTargetPlot.getX(), pTargetPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_UNDEAD'), True)
		pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUE_CARRIER'), True)

def helpDeadAngel4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_DEAD_ANGEL_4_HELP", ())
	return szHelp

def helpDeadAngel5(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_DEAD_ANGEL_5_HELP", ())
	return szHelp

def doDevastatingPlague1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	
	iPop = pCity.getPopulation()
	iPop = int(iPop / 2)
	if iPop == 0:
		iPop = 1
	pCity.setPopulation(iPop)
	for i in range((pCity.plot()).getNumUnits()):
		pUnit = (pCity.plot()).getUnit(i)
		pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUED'), True)

def doDevastatingPlague4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	
	iPop = pCity.getPopulation()
	iPop = int(iPop / 2)
	if iPop == 0:
		iPop = 1
	pCity.setPopulation(iPop)
	iPop = int(iPop / 2)
	if iPop == 0:
		iPop = 1
	for i in range(0,iPop,1): 
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_DISEASED_CORPSE'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

def helpDevastatingPlague1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_DEVASTATING_PLAGUE_1_HELP", ())
	return szHelp

def helpDevastatingPlague4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_DEVASTATING_PLAGUE_4_HELP", ())
	return szHelp

def doMassiveSuicide5(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_MANES'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit1 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_MANES'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit2 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_MANES'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

def helpMassiveSuicide5(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_MASSIVE_SUICIDE_5_HELP", ())
	return szHelp

def canDoNecroCannibalism2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pPlot = gc.getMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if pPlayer.getAlignment() == gc.getInfoTypeForString('ALIGNMENT_GOOD'):
		return False
	return True
	
def doNecroCannibalism2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	
	iPop = pCity.getPopulation()
	iPop = int(iPop / 2)
	if iPop == 0:
		iPop = 1
	pCity.setPopulation(iPop)
	for i in range(0,iPop,1): 
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_WARRIOR'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CANNIBALIZE'), True)
	
def doNecroCannibalism4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_DISEASED_CORPSE'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit1 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_DISEASED_CORPSE'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

def helpNecroCannibalism2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_NECRO_CANNIBALISM_2_HELP", ())
	return szHelp

def helpNecroCannibalism4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_NECRO_CANNIBALISM_4_HELP", ())
	return szHelp

def canTriggerHellPortalCity(argsList):
	eTrigger, pCity = argsList
	pPlayer = gc.getPlayer(pCity.getOwner())
	if pPlayer.getStateReligion() == gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL'):
		if pCity.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_DEMONIC_CITIZENS')) == 0:
			return True
		return False
	return False

def doHellPortal(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_DEMONIC_CITIZENS'), 1)

def doGhostShip(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)

	eUndeadPlayer = gc.getBARBARIAN_PLAYER() + gc.getInfoTypeForString('BARBARIAN_UNDEAD')
	pUndeadPlayer = gc.getPlayer(eUndeadPlayer)
#	iRandNum = CyGame().getSorenRandNum(120, "GhostShip")
	iRandNum = CyGame().getSorenRandNum(100, "GhostShip")
	szSound = 'AS2D_FEATUREGROWTH'
	szButton = 'Art/Interface/Buttons/Improvements/Maelstrom.dds'
	szMessage = -1

	if iRandNum < 20:
		for iLoop in xrange(4):
			pTargetPlot = cf.findAdjacentClearPlot(eUndeadPlayer, pCity.getX(), pCity.getY(), True, False)
			if pTargetPlot is not None:
				pNewUnit = pUndeadPlayer.initUnit(gc.getInfoTypeForString('UNIT_DROWN'), pTargetPlot.getX(), pTargetPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		szMessage = CyTranslator().getText("TXT_KEY_EVENT_GHOST_SHIP_1_1", ())
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_GALLEON'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

	if iRandNum >= 20 and iRandNum < 40:
		szMessage = CyTranslator().getText("TXT_KEY_EVENT_GHOST_SHIP_1_2", ())
		pCity.changeEspionageHealthCounter(5)
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_GALLEON'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

	if iRandNum >= 40 and iRandNum < 60:
		szMessage = CyTranslator().getText("TXT_KEY_EVENT_GHOST_SHIP_1_3", ())
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_LUNATIC'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_GALLEON'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

	if iRandNum >= 60 and iRandNum < 80:
		szMessage = CyTranslator().getText("TXT_KEY_EVENT_GHOST_SHIP_1_4", ())
		pPlayer.changeGold(50)
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_GALLEON'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

	if iRandNum >= 80 and iRandNum < 100:
		szMessage = CyTranslator().getText("TXT_KEY_EVENT_GHOST_SHIP_1_5", ())
		pCity.changeHurryAngerTimer(5)
	"""
	if iRandNum >= 100:
		szMessage = CyTranslator().getText("TXT_KEY_EVENT_GHOST_SHIP_1_6", ())
		cf.placeTreasure(iPlayer, gc.getInfoTypeForString('UNIT_TREASURE'))
		pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_GALLEON'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	"""
	if szMessage != -1:
		CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, szSound, InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pCity.getX(), pCity.getY(), True, True)

## More Events Mod End

#YSbegin
######## BUYWEAPON (YS event) ########

def canbuyweaponYssword1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSWORD1')):
		return False
	elif pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSWORD2')):
		return False
	elif pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSWORD3')):
		return False
	return True

def applybuyweaponYssword1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)
	CyInterface().addMessage(pUnit.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_BUYWEAPON_YSSWORD1",()),'AS2D_REPAIR',1,'Art_Kaijin/REAH/ade/ade7.dds',ColorTypes(8),pUnit.getX(),pUnit.getY(),True,True)

def canbuyweaponYssword2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSWORD2')):
		return False
	elif pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSWORD3')):
		return False
	return True

def applybuyweaponYssword2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSWORD1'), False)
	CyInterface().addMessage(pUnit.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_BUYWEAPON_YSSWORD2",()),'AS2D_REPAIR',1,'Art_Kaijin/REAH/ade/ade8.dds',ColorTypes(8),pUnit.getX(),pUnit.getY(),True,True)

def canbuyweaponYssword3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSWORD3')):
		return False
	return True

def applybuyweaponYssword3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSWORD1'), False)
	pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSWORD2'), False)
	CyInterface().addMessage(pUnit.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_BUYWEAPON_YSSWORD3",()),'AS2D_REPAIR',1,'Art_Kaijin/REAH/ade/ade8.dds',ColorTypes(8),pUnit.getX(),pUnit.getY(),True,True)

def canbuyweaponYsarmor1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSARMOR1')):
		return False
	elif pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSARMOR2')):
		return False
	elif pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSARMOR3')):
		return False
	return True

def applybuyweaponYsarmor1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)
	CyInterface().addMessage(pUnit.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_BUYWEAPON_YSARMOR1",()),'AS2D_REPAIR',1,'Art_Kaijin/REAH/ade/ade11.dds',ColorTypes(8),pUnit.getX(),pUnit.getY(),True,True)

def canbuyweaponYsarmor2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSARMOR2')):
		return False
	elif pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSARMOR3')):
		return False
	return True

def applybuyweaponYsarmor2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YSARMOR1'), False)
	CyInterface().addMessage(pUnit.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_BUYWEAPON_YSARMOR2",()),'AS2D_REPAIR',1,'Art_Kaijin/REAH/ade/ade12.dds',ColorTypes(8),pUnit.getX(),pUnit.getY(),True,True)

def canbuyweaponYsarmor3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSARMOR3')):
		return False
	return True

def applybuyweaponYsarmor3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YSARMOR1'), False)
	pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YSARMOR2'), False)
	CyInterface().addMessage(pUnit.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_BUYWEAPON_YSARMOR3",()),'AS2D_REPAIR',1,'Art_Kaijin/REAH/ade/ade12.dds',ColorTypes(8),pUnit.getX(),pUnit.getY(),True,True)

def canbuyweaponYsshield1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSHIELD1')):
		return False
	elif pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSHIELD2')):
		return False
	elif pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSHIELD3')):
		return False
	return True

def applybuyweaponYsshield1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)
	CyInterface().addMessage(pUnit.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_BUYWEAPON_YSSHIELD1",()),'AS2D_REPAIR',1,'Art_Kaijin/REAH/ade/ade9.dds',ColorTypes(8),pUnit.getX(),pUnit.getY(),True,True)

def canbuyweaponYsshield2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSHIELD2')):
		return False
	elif pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSHIELD3')):
		return False
	return True

def applybuyweaponYsshield2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSHIELD1'), False)
	CyInterface().addMessage(pUnit.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_BUYWEAPON_YSSHIELD2",()),'AS2D_REPAIR',1,'Art_Kaijin/REAH/ade/ade10.dds',ColorTypes(8),pUnit.getX(),pUnit.getY(),True,True)

def canbuyweaponYsshield3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSHIELD3')):
		return False
	return True

def applybuyweaponYsshield3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSHIELD1'), False)
	pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YSSHIELD2'), False)
	CyInterface().addMessage(pUnit.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_BUYWEAPON_YSSHIELD3",()),'AS2D_REPAIR',1,'Art_Kaijin/REAH/ade/ade10.dds',ColorTypes(8),pUnit.getX(),pUnit.getY(),True,True)

def canbuyweaponYsneckless(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YSNECKLESS')):
		return False
	return True

def applybuyweaponYsneckless(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)
	CyInterface().addMessage(pUnit.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_BUYWEAPON_YSNECKLESS",()),'AS2D_REPAIR',1,'Art_Kaijin/REAH/ade/ade16.dds',ColorTypes(8),pUnit.getX(),pUnit.getY(),True,True)

#YSend

def doWitchReturn(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ADEPT'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LIFE1'), True)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SPIRIT1'), True)

def helpWitchReturn(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_WITCH_RETURN_HELP", ())
	return szHelp

# Kaijin Start
# CultOfTheDragon >>>

def canTriggerCultOfTheDragonFound(argsList):
	ePlayer, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SHEAIM'):
		return True
 	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_KURIOTATES'):
		return True 
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MAZATL'):
		return True 
	elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ALTAIR'):
		return True
	return False

def doCultOfTheDragonFound1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	pCity.setHasReligion(gc.getInfoTypeForString('RELIGION_CULT_OF_THE_DRAGON'), True, True, True)

def canTriggerNegativeCultEvents(argsList):
	ePlayer, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SHEAIM'):
		return False
	if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_KURIOTATES'):
		return False
	if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MAZATL'):
		return False
	if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ILLIANS'):
		return False
	if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ALTAIR'):
		return False
	if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_BARBARIAN'):
		return False
	if pCity.isHasReligion(gc.getInfoTypeForString('RELIGION_CULT_OF_THE_DRAGON')):
		return True
	return False

def canDoRemoveCult(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	if pCity.isHolyCityByType(gc.getInfoTypeForString('RELIGION_CULT_OF_THE_DRAGON')) == True:
		return False
	return True

def doCultOfTheDragonUnrest2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	if gc.getGame().getSorenRandNum(100, "Cult of the Dragon Unrest 2") < 25:
		pCity.setHasReligion(gc.getInfoTypeForString('RELIGION_CULT_OF_THE_DRAGON'), False, True, True)

def helpCultOfTheDragonUnrest2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_CULT_OF_THE_DRAGON_UNREST_2_HELP", ())
	return szHelp

def doCultOfTheDragonProduction1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	pCity.setProduction(0)

def helpCultOfTheDragonProduction1(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_CULT_OF_THE_DRAGON_PRODUCTION_1_HELP", ())
	return szHelp

def doCultOfTheDragonProduction2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	pCity.setProduction(0)
	if gc.getGame().getSorenRandNum(100, "Cult of the Dragon Production 2") < 25:
		pCity.setHasReligion(gc.getInfoTypeForString('RELIGION_CULT_OF_THE_DRAGON'), False, True, True)

def helpCultOfTheDragonProduction2(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_CULT_OF_THE_DRAGON_PRODUCTION_2_HELP", ())
	return szHelp

# CultOfTheDragon <<<
# Nival >>>
def doTrappedFrostlings6(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	pCity = pPlayer.getCity(kTriggeredData.iCityId)
	iUnit = gc.getInfoTypeForString('UNIT_HUNTER')
	pNewUnit = pPlayer.initUnit(iUnit, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MOBILITY1'), True)
	pNewUnit.setHomeCivilizationType(pPlayer.getCivilizationType())

def helpTrappedFrostlings6(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	szHelp = localText.getText("TXT_KEY_EVENT_TRAPPED_FROSTLINGS_6_HELP", ())
	return szHelp

# Nival <<<
## Trait Temperamental
def doTraitTemperamental(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	Alignments = [ 'ALIGNMENT_GOOD','ALIGNMENT_NEUTRAL','ALIGNMENT_EVIL' ]
	iRnd = CyGame().getSorenRandNum(len(Alignments), "Temperamental")
	while iRnd == pPlayer.getAlignment():
		iRnd = CyGame().getSorenRandNum(len(Alignments), "Temperamental")
	pPlayer.setAlignment(gc.getInfoTypeForString(Alignments[iRnd]))

## Sharp Artillery
def doSharpArtillery4(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_LINEAGE_HEAVY_BALLISTA'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

	pNewUnit.setName(localText.getText("TXT_KEY_UNIT_BURROUGHS", ()))
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HERO'), True)
	pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LONGRANGE'), True)

def helpSharpArtillery4(argsList):
	szHelp = localText.getText("TXT_KEY_EVENTSHARP_ARTILLERY_4_HELP", ())
	return szHelp

# Animals
def doGreatBeastOse(argsList):
	eUnit = gc.getInfoTypeForString('UNIT_OSE')
	if CyGame().getUnitCreatedCount(eUnit) == 0:
		pNewUnit = cf.addBarbarianUnit(eUnit, gc.getInfoTypeForString('BARBARIAN_ANIMAL'))
		if pNewUnit is not None:
			pNewUnit.changeImmobileTimer(1)

def doGreatBeastTezcatlipoca(argsList):
	eUnit = gc.getInfoTypeForString('UNIT_TEZCATLIPOCA')
	if CyGame().getUnitCreatedCount(eUnit) == 0:
		pNewUnit = cf.addBarbarianUnit(eUnit, gc.getInfoTypeForString('BARBARIAN_ANIMAL'))
		if pNewUnit is not None:
			pNewUnit.changeImmobileTimer(1)

def doGreatBeastInugami(argsList):
	eUnit = gc.getInfoTypeForString('UNIT_INUGAMI')
	if CyGame().getUnitCreatedCount(eUnit) == 0:
		pNewUnit = cf.addBarbarianUnit(eUnit, gc.getInfoTypeForString('BARBARIAN_ANIMAL'))
		if pNewUnit is not None:
			pNewUnit.changeImmobileTimer(1)

def doGreatBeastCeryneianHind(argsList):
	eUnit = gc.getInfoTypeForString('UNIT_CERYNEIAN_HIND')
	if CyGame().getUnitCreatedCount(eUnit) == 0:
		pNewUnit = cf.addBarbarianUnit(eUnit, gc.getInfoTypeForString('BARBARIAN_ANIMAL'))
		if pNewUnit is not None:
			pNewUnit.changeImmobileTimer(1)

def doArmageddonDragonAzathoth(argsList):
	eUnit = gc.getInfoTypeForString('UNIT_AZATHOTH')
	if CyGame().getUnitCreatedCount(eUnit) == 0:
		pNewUnit = cf.addBarbarianUnit(eUnit, gc.getInfoTypeForString('BARBARIAN_DEMONS'))
		if pNewUnit is not None:
			pNewUnit.changeImmobileTimer(1)

def doArmageddonDragonLemegeton(argsList):
	eUnit = gc.getInfoTypeForString('UNIT_LEMEGETON')
	if CyGame().getUnitCreatedCount(eUnit) == 0:
		pNewUnit = cf.addBarbarianUnit(eUnit, gc.getInfoTypeForString('BARBARIAN_DEMONS'))
		if pNewUnit is not None:
			pNewUnit.changeImmobileTimer(1)

def doArmageddonDragonAlexander(argsList):
	eUnit = gc.getInfoTypeForString('UNIT_ALEXANDER')
	if CyGame().getUnitCreatedCount(eUnit) == 0:
		pNewUnit = cf.addBarbarianUnit(eUnit, gc.getInfoTypeForString('BARBARIAN_DEMONS'))
		if pNewUnit is not None:
			pNewUnit.changeImmobileTimer(1)

# Winds of miasma
def canTriggerWindsofMiasma(argsList):
	ePlayer, kTriggeredData = argsList
	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)
	for iLoopPlayer in range(gc.getMAX_PLAYERS()):
		pLoopPlayer = gc.getPlayer(iLoopPlayer)
		if pLoopPlayer.isAlive():
			if pLoopPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_BALDRALFAR'):
				return True
	return False

def doWindsofMiasma(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	py = PyPlayer(iPlayer)
	liPromotions = []
	if pPlayer.getStateReligion() != ReligionTypes.NO_RELIGION and gc.getReligionInfo(pPlayer.getStateReligion()).getAlignment() == gc.getInfoTypeForString('ALIGNMENT_EVIL'):
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
	elif pPlayer.getStateReligion() == gc.getInfoTypeForString('RELIGION_FELLOWSHIP_OF_LEAVES'):
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

	for pUnit in py.getUnitList():
		if pUnit.isAlive():
			if CyGame().getSorenRandNum(100, "Winds of Miasma") < 20 and len(liPromotions) > 0:
				iCount = CyGame().getSorenRandNum(2, 'the number of effects') + 1
				liMiasmaPromotions = [iPromotion for iPromotion in liPromotions if not pUnit.isHasPromotion(iPromotion)]

				if len(liMiasmaPromotions) < iCount:
					iCount = len(liMiasmaPromotions)
				liChosenPromotion = []
				for iLoop in range(iCount):
					liChosenPromotion.append(liMiasmaPromotions.pop( CyGame().getSorenRandNum(len(liMiasmaPromotions), "Variant") ))

				liChosenPromotion.sort()
				for iChosenPromotion in liChosenPromotion:
					pUnit.setHasPromotion(iChosenPromotion, True)

# Spell Conversion
def canSpellConversionFellowship(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	eReligion = gc.getInfoTypeForString('RELIGION_FELLOWSHIP_OF_LEAVES')

	for pyCity in PyPlayer(iPlayer).getCityList():
		pLoopCity = pyCity.GetCy()
		if pLoopCity.isHasReligion(eReligion):
			if pUnit.getReligion() != eReligion:
				return True
	return False

def applySpellConversionFellowship(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)
	pPlot = CyMap().plot(kTriggeredData.iPlotX,kTriggeredData.iPlotY)

	eReligion = gc.getInfoTypeForString('RELIGION_FELLOWSHIP_OF_LEAVES')
	pUnit.setReligion(eReligion)
	point = pPlot.getPoint()
	CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPELL1'), point)
	CyAudioGame().Play3DSound("AS3D_SPELL_SANCTIFY", point.x, point.y, point.z)

def canSpellConversionOrder(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	eReligion = gc.getInfoTypeForString('RELIGION_THE_ORDER')

	for pyCity in PyPlayer(iPlayer).getCityList():
		pLoopCity = pyCity.GetCy()
		if pLoopCity.isHasReligion(eReligion):
			if pUnit.getReligion() != eReligion:
				return True
	return False

def applySpellConversionOrder(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)
	pPlot = CyMap().plot(kTriggeredData.iPlotX,kTriggeredData.iPlotY)

	eReligion = gc.getInfoTypeForString('RELIGION_THE_ORDER')
	pUnit.setReligion(eReligion)
	point = pPlot.getPoint()
	CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPELL1'), point)
	CyAudioGame().Play3DSound("AS3D_SPELL_SANCTIFY", point.x, point.y, point.z)

def canSpellConversionOverlords(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	eReligion = gc.getInfoTypeForString('RELIGION_OCTOPUS_OVERLORDS')

	for pyCity in PyPlayer(iPlayer).getCityList():
		pLoopCity = pyCity.GetCy()
		if pLoopCity.isHasReligion(eReligion):
			if pUnit.getReligion() != eReligion:
				return True
	return False

def applySpellConversionOverlords(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)
	pPlot = CyMap().plot(kTriggeredData.iPlotX,kTriggeredData.iPlotY)

	eReligion = gc.getInfoTypeForString('RELIGION_OCTOPUS_OVERLORDS')
	pUnit.setReligion(eReligion)
	point = pPlot.getPoint()
	CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPELL1'), point)
	CyAudioGame().Play3DSound("AS3D_SPELL_SANCTIFY", point.x, point.y, point.z)

def canSpellConversionRunes(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	eReligion = gc.getInfoTypeForString('RELIGION_RUNES_OF_KILMORPH')

	for pyCity in PyPlayer(iPlayer).getCityList():
		pLoopCity = pyCity.GetCy()
		if pLoopCity.isHasReligion(eReligion):
			if pUnit.getReligion() != eReligion:
				return True
	return False

def applySpellConversionRunes(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)
	pPlot = CyMap().plot(kTriggeredData.iPlotX,kTriggeredData.iPlotY)

	eReligion = gc.getInfoTypeForString('RELIGION_RUNES_OF_KILMORPH')
	pUnit.setReligion(eReligion)
	point = pPlot.getPoint()
	CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPELL1'), point)
	CyAudioGame().Play3DSound("AS3D_SPELL_SANCTIFY", point.x, point.y, point.z)

def canSpellConversionAshen(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	eReligion = gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL')

	for pyCity in PyPlayer(iPlayer).getCityList():
		pLoopCity = pyCity.GetCy()
		if pLoopCity.isHasReligion(eReligion):
			if pUnit.getReligion() != eReligion:
				return True
	return False

def applySpellConversionAshen(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)
	pPlot = CyMap().plot(kTriggeredData.iPlotX,kTriggeredData.iPlotY)

	eReligion = gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL')
	pUnit.setReligion(eReligion)
	point = pPlot.getPoint()
	CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPELL1'), point)
	CyAudioGame().Play3DSound("AS3D_SPELL_SANCTIFY", point.x, point.y, point.z)

def canSpellConversionEmpyrean(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	eReligion = gc.getInfoTypeForString('RELIGION_THE_EMPYREAN')

	for pyCity in PyPlayer(iPlayer).getCityList():
		pLoopCity = pyCity.GetCy()
		if pLoopCity.isHasReligion(eReligion):
			if pUnit.getReligion() != eReligion:
				return True
	return False

def applySpellConversionEmpyrean(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)
	pPlot = CyMap().plot(kTriggeredData.iPlotX,kTriggeredData.iPlotY)

	eReligion = gc.getInfoTypeForString('RELIGION_THE_EMPYREAN')
	pUnit.setReligion(eReligion)
	point = pPlot.getPoint()
	CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPELL1'), point)
	CyAudioGame().Play3DSound("AS3D_SPELL_SANCTIFY", point.x, point.y, point.z)

def canSpellConversionEsus(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	eReligion = gc.getInfoTypeForString('RELIGION_COUNCIL_OF_ESUS')

	for pyCity in PyPlayer(iPlayer).getCityList():
		pLoopCity = pyCity.GetCy()
		if pLoopCity.isHasReligion(eReligion):
			if pUnit.getReligion() != eReligion:
				return True
	return False

def applySpellConversionEsus(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)
	pPlot = CyMap().plot(kTriggeredData.iPlotX,kTriggeredData.iPlotY)

	eReligion = gc.getInfoTypeForString('RELIGION_COUNCIL_OF_ESUS')
	pUnit.setReligion(eReligion)
	point = pPlot.getPoint()
	CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPELL1'), point)
	CyAudioGame().Play3DSound("AS3D_SPELL_SANCTIFY", point.x, point.y, point.z)

def canSpellConversionDragon(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)

	eReligion = gc.getInfoTypeForString('RELIGION_CULT_OF_THE_DRAGON')

	for pyCity in PyPlayer(iPlayer).getCityList():
		pLoopCity = pyCity.GetCy()
		if pLoopCity.isHasReligion(eReligion):
			if pUnit.getReligion() != eReligion:
				return True
	return False

def applySpellConversionDragon(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	iPlayer = kTriggeredData.ePlayer
	pPlayer = gc.getPlayer(iPlayer)
	pUnit = pPlayer.getUnit(kTriggeredData.iUnitId)
	pPlot = CyMap().plot(kTriggeredData.iPlotX,kTriggeredData.iPlotY)

	eReligion = gc.getInfoTypeForString('RELIGION_CULT_OF_THE_DRAGON')
	pUnit.setReligion(eReligion)
	point = pPlot.getPoint()
	CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SPELL1'), point)
	CyAudioGame().Play3DSound("AS3D_SPELL_SANCTIFY", point.x, point.y, point.z)

# Armageddon Event Trigger
def canTriggerArmageddonEvent(argsList):
	ePlayer, kTriggeredData = argsList
	iGameTurn = CyGame().getGameTurn()
	iThresholdTurn = cyFlatValue(150, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
	if iGameTurn < iThresholdTurn:
		return False
	return True

# Kaijin End
# Kaijin OAC <<< End
# ent >>>
def canTriggerTransmutation(argsList):
	ePlayer, kTriggeredData = argsList
	pPlot = CyMap().plot(kTriggeredData.iPlotX, kTriggeredData.iPlotY)
	if pPlot.getImprovementType() != ImprovementTypes.NO_IMPROVEMENT:
		if gc.getImprovementInfo(pPlot.getImprovementType()).isUnique():
			return False
	return True

def applyAncientCity3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pPlayer = gc.getPlayer(ePlayer)
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	pPlot = pCity.plot()
	iPopulation = pCity.getPopulation()
	eReborn = gc.getInfoTypeForString('UNIT_REBORN')
	for i in range (iPopulation):
		pNewUnit = pPlayer.initUnit(eReborn, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	pCity.kill()
	pPlot.setBonusType(gc.getInfoTypeForString('BONUS_PATRIAN_ARTIFACTS'))

def canApplyAncientCity3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	return not pCity.isCapital()

def getHelpAncientCity3(argsList):
	ePlayer, eEvent, kTriggeredData = argsList
	pCity = getCity(kTriggeredData.ePlayer, kTriggeredData.iCityId)
	szHelp = localText.getText("TXT_KEY_EVENT_ANCIENT_CITY_3_HELP", (pCity.getName(), ))
	return szHelp

# ent <<<