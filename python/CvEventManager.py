# Sid Meier's Civilization 4
# Copyright Firaxis Games 2006
#
# CvEventManager
# This class is passed an argsList from CvAppInterface.onEvent
# The argsList can contain anything from mouse location to key info
# The EVENTLIST that are being notified can be found

from CvPythonExtensions import *
import CvUtil
import CvScreensInterface
import CvDebugTools
import CvWBPopups
import PyHelpers
import Popup as PyPopup
import CvCameraControls
import CvTopCivs
import sys
import CvWorldBuilderScreen
import CvAdvisorUtils
import CvTechChooser

import CvIntroMovieScreen
import CustomFunctions
import ScenarioFunctions
##--------	Merging CGE: Added by Denev	--------##
import AlertsLog
##--------	Merging CGE: End Add		--------##
##--------	Enums Cache: Added by Denev	--------##
import CvPythonEnums
en = CvPythonEnums.CvPythonEnums()
##--------	Enums Cache: End Add		--------##

#FfH: Card Game: begin
import CvSomniumInterface
import CvCorporationScreen
#FfH: Card Game: end

#FfH: Added by Kael 10/15/2008 for OOS Logging
import OOSLogger
#FfH: End Add

#POPUP_MOD ADD START
import WorldUnitPopup
#POPUP_MOD ADD END

# globals
cf = CustomFunctions.CustomFunctions()
gc = CyGlobalContext()
localText = CyTranslator()
PyPlayer = PyHelpers.PyPlayer
PyInfo = PyHelpers.PyInfo
sf = ScenarioFunctions.ScenarioFunctions()

#FfH: Card Game: begin
cs = CvCorporationScreen.cs
#FfH: Card Game: end

##--------	TradeResourcePanel: Added by Denev	--------##
import TradeResourcePanel
tr = TradeResourcePanel.getInstance()
##--------	TradeResourcePanel: End Add			--------##


# globals
###################################################
class CvEventManager:
	def __init__(self):
		#################### ON EVENT MAP ######################
		#print "EVENTMANAGER INIT"

		self.bCtrl = False
		self.bShift = False
		self.bAlt = False
		self.bAllowCheats = False

		# OnEvent Enums
		self.EventLButtonDown=1
		self.EventLcButtonDblClick=2
		self.EventRButtonDown=3
		self.EventBack=4
		self.EventForward=5
		self.EventKeyDown=6
		self.EventKeyUp=7

		self.__LOG_MOVEMENT = 0
		self.__LOG_BUILDING = 0
		self.__LOG_COMBAT = 0
		self.__LOG_CONTACT = 0
		self.__LOG_IMPROVEMENT =0
		self.__LOG_CITYLOST = 0
		self.__LOG_CITYBUILDING = 0
		self.__LOG_TECH = 0
		self.__LOG_UNITBUILD = 0
		self.__LOG_UNITKILLED = 1
		self.__LOG_UNITLOST = 0
		self.__LOG_UNITPROMOTED = 0
		self.__LOG_UNITSELECTED = 0
		self.__LOG_UNITPILLAGE = 0
		self.__LOG_GOODYRECEIVED = 0
		self.__LOG_GREATPERSON = 0
		self.__LOG_RELIGION = 0
		self.__LOG_RELIGIONSPREAD = 0
		self.__LOG_GOLDENAGE = 0
		self.__LOG_ENDGOLDENAGE = 0
		self.__LOG_WARPEACE = 0
		self.__LOG_PUSH_MISSION = 0

		## EVENTLIST
		self.EventHandlerMap = {
			'mouseEvent'			: self.onMouseEvent,
			'kbdEvent'				: self.onKbdEvent,
			'ModNetMessage'			: self.onModNetMessage,
			'Init'					: self.onInit,
			'Update'				: self.onUpdate,
			'UnInit'				: self.onUnInit,
			'OnSave'				: self.onSaveGame,
			'OnPreSave'				: self.onPreSave,
			'OnLoad'				: self.onLoadGame,
			'GameStart'				: self.onGameStart,
			'GameEnd'				: self.onGameEnd,
			'plotRevealed'			: self.onPlotRevealed,
			'plotFeatureRemoved'	: self.onPlotFeatureRemoved,
			'plotPicked'			: self.onPlotPicked,
			'nukeExplosion'			: self.onNukeExplosion,
			'gotoPlotSet'			: self.onGotoPlotSet,
			'BeginGameTurn'			: self.onBeginGameTurn,
			'EndGameTurn'			: self.onEndGameTurn,
			'BeginPlayerTurn'		: self.onBeginPlayerTurn,
			'EndPlayerTurn'			: self.onEndPlayerTurn,
			'endTurnReady'			: self.onEndTurnReady,
			'combatResult'			: self.onCombatResult,
			'combatLogCalc'			: self.onCombatLogCalc,
			'combatLogHit'			: self.onCombatLogHit,
			'improvementBuilt'		: self.onImprovementBuilt,
			'improvementDestroyed'	: self.onImprovementDestroyed,
			'routeBuilt'			: self.onRouteBuilt,
			'firstContact'			: self.onFirstContact,
			'cityBuilt'				: self.onCityBuilt,
			'cityRazed'				: self.onCityRazed,
			'cityAcquired'			: self.onCityAcquired,
			'cityAcquiredAndKept'	: self.onCityAcquiredAndKept,
			'cityLost'				: self.onCityLost,
			'cultureExpansion'		: self.onCultureExpansion,
			'cityGrowth'			: self.onCityGrowth,
			'cityDoTurn'			: self.onCityDoTurn,
			'cityBuildingUnit'		: self.onCityBuildingUnit,
			'cityBuildingBuilding'	: self.onCityBuildingBuilding,
			'cityRename'			: self.onCityRename,
			'cityHurry'				: self.onCityHurry,
			'selectionGroupPushMission'	: self.onSelectionGroupPushMission,
			'unitMove'				: self.onUnitMove,
			'unitSetXY'				: self.onUnitSetXY,
			'unitCreated'			: self.onUnitCreated,
			'unitBuilt'				: self.onUnitBuilt,
			'unitKilled'			: self.onUnitKilled,
##--------	Advanced Rules: Added by Denev	--------##
			'unitRebirth'			: self.onUnitRebirth,
##--------	Advanced Rules: End Add			--------##
			'unitLost'				: self.onUnitLost,
			'unitPromoted'			: self.onUnitPromoted,
			'unitSelected'			: self.onUnitSelected,
			'UnitRename'				: self.onUnitRename,
			'unitPillage'				: self.onUnitPillage,
			'unitSpreadReligionAttempt'	: self.onUnitSpreadReligionAttempt,
			'unitGifted'				: self.onUnitGifted,
			'unitBuildImprovement'		: self.onUnitBuildImprovement,
			'goodyReceived'			: self.onGoodyReceived,
			'greatPersonBorn'		: self.onGreatPersonBorn,
			'buildingBuilt'			: self.onBuildingBuilt,
			'projectBuilt'			: self.onProjectBuilt,
			'techAcquired'			: self.onTechAcquired,
			'techSelected'			: self.onTechSelected,
			'religionFounded'		: self.onReligionFounded,
			'religionSpread'		: self.onReligionSpread,
			'religionRemove'		: self.onReligionRemove,
			'corporationFounded'	: self.onCorporationFounded,
			'corporationSpread'		: self.onCorporationSpread,
			'corporationRemove'		: self.onCorporationRemove,
			'goldenAge'				: self.onGoldenAge,
			'endGoldenAge'			: self.onEndGoldenAge,
			'chat'					: self.onChat,
			'victory'				: self.onVictory,
			'vassalState'			: self.onVassalState,
			'changeWar'				: self.onChangeWar,
			'setPlayerAlive'		: self.onSetPlayerAlive,
			'playerChangeStateReligion'	: self.onPlayerChangeStateReligion,
			'playerGoldTrade'		: self.onPlayerGoldTrade,
			'windowActivation'		: self.onWindowActivation,
			'gameUpdate'			: self.onGameUpdate,		# sample generic event
		}

		################## Events List ###############################
		#
		# Dictionary of Events, indexed by EventID (also used at popup context id)
		#   entries have name, beginFunction, applyFunction [, randomization weight...]
		#
		# Normal events first, random events after
		#
		################## Events List ###############################
		self.Events={
			CvUtil.EventEditCityName : ('EditCityName', self.__eventEditCityNameApply, self.__eventEditCityNameBegin),
			CvUtil.EventEditCity : ('EditCity', self.__eventEditCityApply, self.__eventEditCityBegin),
			CvUtil.EventPlaceObject : ('PlaceObject', self.__eventPlaceObjectApply, self.__eventPlaceObjectBegin),
			CvUtil.EventAwardTechsAndGold: ('AwardTechsAndGold', self.__eventAwardTechsAndGoldApply, self.__eventAwardTechsAndGoldBegin),
			CvUtil.EventEditUnitName : ('EditUnitName', self.__eventEditUnitNameApply, self.__eventEditUnitNameBegin),
			CvUtil.EventWBAllPlotsPopup : ('WBAllPlotsPopup', self.__eventWBAllPlotsPopupApply, self.__eventWBAllPlotsPopupBegin),
			CvUtil.EventWBLandmarkPopup : ('WBLandmarkPopup', self.__eventWBLandmarkPopupApply, self.__eventWBLandmarkPopupBegin),
			CvUtil.EventWBScriptPopup : ('WBScriptPopup', self.__eventWBScriptPopupApply, self.__eventWBScriptPopupBegin),
			CvUtil.EventWBStartYearPopup : ('WBStartYearPopup', self.__eventWBStartYearPopupApply, self.__eventWBStartYearPopupBegin),
			CvUtil.EventShowWonder: ('ShowWonder', self.__eventShowWonderApply, self.__eventShowWonderBegin),
		}
## FfH Card Game: begin
		self.Events[CvUtil.EventSelectSolmniumPlayer] = ('selectSolmniumPlayer', self.__EventSelectSolmniumPlayerApply, self.__EventSelectSolmniumPlayerBegin)
		self.Events[CvUtil.EventSolmniumAcceptGame] = ('solmniumAcceptGame', self.__EventSolmniumAcceptGameApply, self.__EventSolmniumAcceptGameBegin)
		self.Events[CvUtil.EventSolmniumConcedeGame] = ('solmniumConcedeGame', self.__EventSolmniumConcedeGameApply, self.__EventSolmniumConcedeGameBegin)
## FfH Card Game: end

#################### EVENT STARTERS ######################
	def handleEvent(self, argsList):
		'EventMgr entry point'
		# extract the last 6 args in the list, the first arg has already been consumed
		self.origArgsList = argsList	# point to original
		tag = argsList[0]				# event type string
		idx = len(argsList)-6
		bDummy = False
		self.bDbg, bDummy, self.bAlt, self.bCtrl, self.bShift, self.bAllowCheats = argsList[idx:]
		ret = 0
		if self.EventHandlerMap.has_key(tag):
			fxn = self.EventHandlerMap[tag]
			ret = fxn(argsList[1:idx])
		return ret

#################### EVENT APPLY ######################
	def beginEvent( self, context, argsList=-1 ):
		'Begin Event'
		entry = self.Events[context]
		return entry[2]( argsList )

	def applyEvent( self, argsList ):
		'Apply the effects of an event '
		context, playerID, netUserData, popupReturn = argsList

		if context == CvUtil.PopupTypeEffectViewer:
			return CvDebugTools.g_CvDebugTools.applyEffectViewer( playerID, netUserData, popupReturn )

		entry = self.Events[context]

		if ( context not in CvUtil.SilentEvents ):
			self.reportEvent(entry, context, (playerID, netUserData, popupReturn) )
		return entry[1]( playerID, netUserData, popupReturn )   # the apply function

	def reportEvent(self, entry, context, argsList):
		'Report an Event to Events.log '
		if (gc.getGame().getActivePlayer() != -1):
			message = "DEBUG Event: %s (%s)" %(entry[0], gc.getActivePlayer().getName())
			CyInterface().addImmediateMessage(message, "")
			CvUtil.pyPrint(message)
		return 0

#################### ON EVENTS ######################
	def onKbdEvent(self, argsList):
		'keypress handler - return 1 if the event was consumed'

		eventType, key, mx, my, px, py = argsList
		game = gc.getGame()

		if (self.bAllowCheats):
			# notify debug tools of input to allow it to override the control
			argsList = (eventType, key, self.bCtrl, self.bShift, self.bAlt, mx, my, px, py, gc.getGame().isNetworkMultiPlayer())
			if ( CvDebugTools.g_CvDebugTools.notifyInput(argsList) ):
				return 0

		if ( eventType == self.EventKeyDown ):
			theKey=int(key)

#FfH: Added by Kael 07/05/2008
			if (theKey == int(InputTypes.KB_LEFT)):
				if self.bCtrl:
						CyCamera().SetBaseTurn(CyCamera().GetBaseTurn() - 45.0)
						return 1
				elif self.bShift:
						CyCamera().SetBaseTurn(CyCamera().GetBaseTurn() - 10.0)
						return 1

			if (theKey == int(InputTypes.KB_RIGHT)):
					if self.bCtrl:
							CyCamera().SetBaseTurn(CyCamera().GetBaseTurn() + 45.0)
							return 1
					elif self.bShift:
							CyCamera().SetBaseTurn(CyCamera().GetBaseTurn() + 10.0)
							return 1
#FfH: End Add

			CvCameraControls.g_CameraControls.handleInput( theKey )

			if (self.bAllowCheats):
				# Shift - T (Debug - No MP)
				if (theKey == int(InputTypes.KB_T)):
					if ( self.bShift ):
						self.beginEvent(CvUtil.EventAwardTechsAndGold)
						#self.beginEvent(CvUtil.EventCameraControlPopup)
						return 1

				elif (theKey == int(InputTypes.KB_W)):
					if ( self.bShift and self.bCtrl):
						self.beginEvent(CvUtil.EventShowWonder)
						return 1

				# Shift - ] (Debug - currently mouse-overd unit, health += 10
				elif (theKey == int(InputTypes.KB_LBRACKET) and self.bShift ):
					unit = CyMap().plot(px, py).getUnit(0)
					if ( not unit.isNone() ):
						d = min( unit.maxHitPoints()-1, unit.getDamage() + 10 )
						unit.setDamage( d, PlayerTypes.NO_PLAYER )

				# Shift - [ (Debug - currently mouse-overd unit, health -= 10
				elif (theKey == int(InputTypes.KB_RBRACKET) and self.bShift ):
					unit = CyMap().plot(px, py).getUnit(0)
					if ( not unit.isNone() ):
						d = max( 0, unit.getDamage() - 10 )
						unit.setDamage( d, PlayerTypes.NO_PLAYER )

				elif (theKey == int(InputTypes.KB_F1)):
					if ( self.bShift ):
						CvScreensInterface.replayScreen.showScreen(False)
						return 1
					# don't return 1 unless you want the input consumed

				elif (theKey == int(InputTypes.KB_F2)):
					if ( self.bShift ):
						import CvDebugInfoScreen
						CvScreensInterface.showDebugInfoScreen()
						return 1

				elif (theKey == int(InputTypes.KB_F3)):
					if ( self.bShift ):
						CvScreensInterface.showDanQuayleScreen(())
						return 1

				elif (theKey == int(InputTypes.KB_F4)):
					if ( self.bShift ):
						CvScreensInterface.showUnVictoryScreen(())
						return 1

		return 0

	def onModNetMessage(self, argsList):
		'Called whenever CyMessageControl().sendModNetMessage() is called - this is all for you modders!'

		iData1, iData2, iData3, iData4, iData5 = argsList

#FfH Card Game: begin
#		print("Modder's net message!")
#		CvUtil.pyPrint( 'onModNetMessage' )
		if iData1 == CvUtil.Somnium : # iData1 == 0 : Solmnium message, iData2 = function, iData3 to iData5 = parameters
			if iData2 == 0 :
				if (iData3 == gc.getGame().getActivePlayer()):
					self.__EventSelectSolmniumPlayerBegin()
			elif iData2 == 1 :
				if (iData4 == gc.getGame().getActivePlayer()):
					self.__EventSolmniumConcedeGameBegin((iData3, iData4))
			else :
				cs.applyAction(iData2, iData3, iData4, iData5)
# FfH Card Game: end

	def onInit(self, argsList):
		'Called when Civ starts up'
		CvUtil.pyPrint( 'OnInit' )

	def onUpdate(self, argsList):
		'Called every frame'
		fDeltaTime = argsList[0]

		# allow camera to be updated
		CvCameraControls.g_CameraControls.onUpdate( fDeltaTime )

	def onWindowActivation(self, argsList):
		'Called when the game window activates or deactivates'
		bActive = argsList[0]

	def onUnInit(self, argsList):
		'Called when Civ shuts down'
		CvUtil.pyPrint('OnUnInit')

	def onPreSave(self, argsList):
		"called before a game is actually saved"
		CvUtil.pyPrint('OnPreSave')

	def onSaveGame(self, argsList):
		"return the string to be saved - Must be a string"
		return ""

	def onLoadGame(self, argsList):
		CvAdvisorUtils.resetNoLiberateCities()
		return 0

	def onGameStart(self, argsList):
		'Called at the start of the game'

		if CyGame().getWBMapScript():
			sf.gameStart()
		else:
			introMovie = CvIntroMovieScreen.CvIntroMovieScreen()
			introMovie.interfaceScreen()

		CvAdvisorUtils.resetNoLiberateCities()

		if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_THAW):
			for iPlotIndex in range (CyMap().numPlots()):
				pPlot = CyMap().plotByIndex(iPlotIndex)
#				if pPlot.getImprovementType() == ImprovementTypes.NO_IMPROVEMENT:
				if not pPlot.isWater():
					"""
					if pPlot.getFeatureType() == FeatureTypes.NO_FEATURE:
						iTerrain = pPlot.getTerrainType()
						iTimer = CyGame().getSorenRandNum(90, "Game Option Thaw") + 10
						iTimer = cyFlatValue(iTimer, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), True)
						if iTerrain == iTundra:
							pPlot.setTempTerrainType(iSnow, iTimer)
						elif iTerrain in (iGrass, iMarsh, iPlains):
							pPlot.setTempTerrainType(iTundra, iTimer)
						elif iTerrain == iDesert:
							pPlot.setTempTerrainType(iPlains, iTimer)
					"""
					iBaseTimer = 0
					if pPlot.getFeatureType() == FeatureTypes.NO_FEATURE:
						if pPlot.getBonusType(TeamTypes.NO_TEAM) == BonusTypes.NO_BONUS:
							iBaseTimer = 6000
						elif pPlot.getTerrainType() != en.eTerrainTundra:
							iBaseTimer = 2400
					elif pPlot.getFeatureType() == en.eFeatureForest:
						if pPlot.getTerrainType() != en.eTerrainTundra:
							iBaseTimer = 2400
					elif pPlot.getFeatureType() in (en.eFeatureScrub, en.eFeatureFloodPlains):
						iBaseTimer = 6000
					elif pPlot.getFeatureType() == en.eFeatureJungle:
						iBaseTimer = 2400
						pPlot.setFeatureType(en.eFeatureForest, -1)
					if iBaseTimer > 0:
						iTimer = CyGame().getSorenRandNum(iBaseTimer, "Game Option Thaw") + 3600
						pPlot.ceilColdCounter(iTimer, -1)
						if pPlot.getFeatureType() != FeatureTypes.NO_FEATURE:
							if not gc.getFeatureInfo(pPlot.getFeatureType()).isTerrain(pPlot.getTerrainType()):
								pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)

		for iPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
			pPlayer = gc.getPlayer(iPlayer)
			if pPlayer.isAlive():
				if pPlayer.getCivilizationType() == en.eCivilizationElohim:
					cf.showUniqueImprovements(iPlayer)
# Kaijin >>>
## Amurite - Show All Manas
				elif pPlayer.getCivilizationType() == en.eCivilizationAmurites:
					cf.showRawManas(iPlayer)

## Globalcounter initialization
				if not pPlayer.isBarbarian():
					cf.doGlobalcounterInitialization(iPlayer)

#orbi start
#		cf.doWetland()
#orbi end

		##Placement of the Lair
#		cf.doPutLair()

		##Placement of the Crystalplain
#		cf.doCrystalplain()

#		if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_LAIRS):
#			cf.doNoLairsOAC()

		if CyGame().isOption(gc.getInfoTypeForString('GAMEOPTION_MODDER_5')) and not gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_LAIRS):
			cf.doMoreLairsOAC()

		##Placement of the HauntedLand
#		cf.doHauntedLand()

#		##Allow Nuke
#		gc.getGame().makeNukesValid(True)
# Kaijin <<<

		if not gc.getGame().isNetworkMultiPlayer():
			szTorophyKey = "TROPHY_FEAT_INTRODUCTION"
			if not CyGame().isHasTrophy(szTorophyKey):
				CyGame().changeTrophyValue(szTorophyKey, 1)
				sf.addPopupWB(CyTranslator().getText("TXT_KEY_FFH_INTRO", ()), 'art/interface/popups/FfHIntro.dds')

		"""
		if not CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_BARBARIANS):
			iGoblinFort = gc.getInfoTypeForString('IMPROVEMENT_GOBLIN_FORT')
			pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
			for iPlotIndex in range (CyMap().numPlots()):
				pPlot = CyMap().plotByIndex(iPlotIndex)
				if pPlot.getImprovementType() == iGoblinFort:
					pBarbarianPlayer.initUnit(gc.getInfoTypeForString('UNIT_ARCHER_SCORPION_CLAN'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
		"""

		if (gc.getGame().getGameTurnYear() == gc.getDefineINT("START_YEAR") and not gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ADVANCED_START)):
			if not CyGame().getWBMapScript():
				for iPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
					pPlayer = gc.getPlayer(iPlayer)
					if pPlayer.isAlive() and pPlayer.isHuman():
						popupInfo = CyPopupInfo()
						popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON_SCREEN)
						popupInfo.setText(u"showDawnOfMan")
						popupInfo.addPopup(iPlayer)
		else:
			CyInterface().setSoundSelectionReady(True)

		if gc.getGame().isPbem():
			for iPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
				pPlayer = gc.getPlayer(iPlayer)
				if pPlayer.isAlive() and pPlayer.isHuman():
					popupInfo = CyPopupInfo()
					popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_DETAILS)
					popupInfo.setOption1(True)
					popupInfo.addPopup(iPlayer)

		CvAdvisorUtils.resetNoLiberateCities()

	def onGameEnd(self, argsList):
		'Called at the End of the game'
		print("Game is ending")
		return

	def onBeginGameTurn(self, argsList):
		'Called at the beginning of the end of each turn'
		iGameTurn = argsList[0]

		iOrthusTurn = cyFlatValue(75, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)

		if not CyGame().isUnitClassMaxedOut(gc.getInfoTypeForString('UNITCLASS_ORTHUS'), 0):
			if not CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_ORTHUS):
				if iGameTurn >= iOrthusTurn:
					iUnit = gc.getInfoTypeForString('UNIT_ORTHUS')
					cf.addBarbarianUnit(iUnit, gc.getInfoTypeForString('BARBARIAN_ORC'))
##--------	Merging Better BtS AI: Modified by Denev	--------##
#					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_ORTHUS_CREATION", ()), str(gc.getUnitInfo(iUnit).getImage()))
					if( CyGame().getAIAutoPlay() == 0 ):
						cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_ORTHUS_CREATION", ()), str(gc.getUnitInfo(iUnit).getImage()))
##--------	Merging Better BtS AI: End Modify			--------##

		if not CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_PLOT_COUNTER):
			cf.doHellTerrain()

		if CyGame().getWBMapScript():
			sf.doTurn()

#kaijin >>>
		if CyGame().isOption(gc.getInfoTypeForString('GAMEOPTION_MODDER_4')):
		## 氾濫原の発生と消失
			cf.doFlood()

		## 猛吹雪の発生と消失
		cf.doBlizzard()

		## 獣道への変化と逆変化
		cf.doTrail()

		## Plots
		for iPlotIndex in range (CyMap().numPlots()):
			pLoopPlot = CyMap().plotByIndex(iPlotIndex)

			## Civilization effects
			if pLoopPlot.isOwned():
				iPlayer = pLoopPlot.getOwner()
				pPlayer = gc.getPlayer(iPlayer)
				## Altair
				if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ALTAIR'):
					cf.doDesert(iPlayer, pLoopPlot)
				## Mazatl and Cualli - Deep Jungle
				elif pPlayer.getCivilizationType() in (	gc.getInfoTypeForString('CIVILIZATION_MAZATL'), 
														gc.getInfoTypeForString('CIVILIZATION_CUALLI')	):
					cf.doDeepJungle(iPlayer, pLoopPlot)
				## Nival
				elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_NIVAL'):
					iFrostlingPlayer = gc.getInfoTypeForString('BARBARIAN_FROSTLING') + gc.getBARBARIAN_PLAYER()
					pFrostlingPlayer = gc.getPlayer(iFrostlingPlayer)
					pFrostlingTeam = gc.getTeam(pFrostlingPlayer.getTeam())
					if not pFrostlingTeam.isAtWar(pPlayer.getTeam()):
						cf.doNival(iPlayer, pLoopPlot)
			"""
			## Armed fishing boats & Armed whaling boats
			iBonus = pLoopPlot.getBonusType(TeamTypes.NO_TEAM)
			if iBonus in (gc.getInfoTypeForString('BONUS_CLAM'), 
							gc.getInfoTypeForString('BONUS_CRAB'), 
							gc.getInfoTypeForString('BONUS_FISH'), 
							gc.getInfoTypeForString('BONUS_PEARL'), 
							gc.getInfoTypeForString('BONUS_SHRIMP'), 
							gc.getInfoTypeForString('BONUS_JADE'), 
							gc.getInfoTypeForString('BONUS_WHALE')):
				iImprovement = pLoopPlot.getImprovementType()
				if iImprovement != gc.getInfoTypeForString('IMPROVEMENT_FISHING_BOATS') and iImprovement != gc.getInfoTypeForString('IMPROVEMENT_WHALING_BOATS'):
					for iUnitIndex in xrange(pLoopPlot.getNumUnits()):
						pUnit = pLoopPlot.getUnit(iUnitIndex)
						if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_BASQUE'):
							if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_HELD')):
								pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HELD'), False)
			"""
		## Players
		for iPlayer in xrange(gc.getMAX_PLAYERS()):
			pPlayer = gc.getPlayer(iPlayer)

			## Units
			for pUnit in PyPlayer(iPlayer).getUnitList():

				## Doviello - Basque
				if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BASQUE')):

					def isInvalidOperation(pUnit):
						pPlot = pUnit.plot()
						eBonus = pPlot.getBonusType(pUnit.getTeam())
						eImprovement = pPlot.getImprovementType()
						eImprovementFishingBoats = gc.getInfoTypeForString('IMPROVEMENT_FISHING_BOATS')
						eImprovementWhalingBoats = gc.getInfoTypeForString('IMPROVEMENT_WHALING_BOATS')

						if eBonus == BonusTypes.NO_BONUS:
							return True
						elif gc.getImprovementInfo(eImprovementFishingBoats).isImprovementBonusMakesValid(eBonus):
							if eImprovement != eImprovementFishingBoats:
								return True
						elif gc.getImprovementInfo(eImprovementWhalingBoats).isImprovementBonusMakesValid(eBonus):
							if eImprovement != eImprovementWhalingBoats:
								return True
						else:
							return True
						if pPlot.isOwned():
							if pPlot.getOwner() != pUnit.getOwner():
								return True
						else:
							return True
						return False

					if isInvalidOperation(pUnit):
						pUnit.kill(False, PlayerTypes.NO_PLAYER)
						continue

				## Nival - Iceroad
				if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ICE_ROAD')):
					bValid = True
					iRange = 1
					pPlot = pUnit.plot()
					pTeam = gc.getTeam(pUnit.getTeam())
					if pPlot.isOwned():
						ePlotOwner = pPlot.getOwner()
						pPlotOwner = gc.getPlayer(ePlotOwner)
						if pPlotOwner.isAlive():
							if pPlotOwner.getCivilizationType() == en.eCivilizationNival:
								iRange = 2
							elif ePlotOwner != iPlayer:
								if not pTeam.isAtWar(pPlot.getTeam()):
									bValid = False
							else: # ePlotOwner == pUnit.getOwner() and pPlotOwner.getCivilizationType() != en.eCivilizationNival
								bValid = False
					if bValid:
						lpRangedPlots = cyGetRangedPlots(pUnit.plot(), iRange, False, False, TeamTypes.NO_TEAM)
						for pTargetPlot in lpRangedPlots:
							if not pTargetPlot.isWater():
								iDecreasingValue = 8000
								if pTargetPlot.isOwned():
									eTargetPlotOwner = pTargetPlot.getOwner()
									pTargetPlotOwner = gc.getPlayer(eTargetPlotOwner)
									if pTargetPlotOwner.isAlive():
										if pTargetPlotOwner.getCivilizationType() == en.eCivilizationNival:
											iDecreasingValue = 500
											cf.doBuildingColdEffects(pTargetPlot)
										elif eTargetPlotOwner != iPlayer:
											if not pTeam.isAtWar(pPlot.getTeam()):
												continue
										else: # eTargetPlotOwner == pUnit.getOwner() and pTargetPlotOwner.getCivilizationType() != en.eCivilizationNival
											continue
								pTargetPlot.ceilColdCounter(9600 + CyGame().getSorenRandNum(2400, "Built Temple of the Hand"), iDecreasingValue)

		"""
		## Random occurrences Barbarian Pirates
		if not gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_BARBARIANS):
			iPiratesSpawnRate = gc.getHandicapInfo(gc.getGame().getHandicapType()).getLairSpawnRate()
			iPiratesSpawnRate *= iPiratesSpawnRate
			if CyGame().getSorenRandNum(50, "Barbarian Pirates") < iPiratesSpawnRate:
				cf.doBarbarianPirates(iGameTurn)
		"""

		## Random occurrences Barbarian Animals
		if not gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_BARBARIANS):
			iAnimalsSpawnRate = gc.getHandicapInfo(gc.getGame().getHandicapType()).getLairSpawnRate()
			iAnimalsSpawnRate *= iAnimalsSpawnRate
			if CyGame().getSorenRandNum(50, "Barbarian Animals") < iAnimalsSpawnRate:
				cf.doBarbarianAnimals()

#kaijin <<<

#end
# FfH Card Game: begin
		cs.doTurn()
# FfH Card Game: end

##--------	Merging Better BtS AI: Modified by Denev	--------##
#		CvTopCivs.CvTopCivs().turnChecker(iGameTurn)
		if( CyGame().getAIAutoPlay() == 0 ):
			CvTopCivs.CvTopCivs().turnChecker(iGameTurn)
##--------	Merging Better BtS AI: End Modify			--------##

	def onEndGameTurn(self, argsList):
		'Called at the end of the end of each turn'
		iGameTurn = argsList[0]

	def onBeginPlayerTurn(self, argsList):
		'Called at the beginning of a players turn'
		iGameTurn, iPlayer = argsList
		pPlayer = gc.getPlayer(iPlayer)
		player = PyPlayer(iPlayer)
# ent >>>
		eCiv = pPlayer.getCivilizationType()
# ent <<<

		eStateReligion = pPlayer.getStateReligion()
		if eStateReligion == en.eReligionAshenVeil:
			if pPlayer.getCurrentEra() != gc.getInfoTypeForString('ERA_VEIL'):
				pPlayer.setCurrentEra(gc.getInfoTypeForString('ERA_VEIL'))

		elif eStateReligion == en.eReligionOrder:
			if pPlayer.getCurrentEra() != gc.getInfoTypeForString('ERA_ORDE'):
				pPlayer.setCurrentEra(gc.getInfoTypeForString('ERA_ORDE'))

		elif eStateReligion == en.eReligionFellowshipofLeaves:
			if pPlayer.getCurrentEra() != gc.getInfoTypeForString('ERA_LEAF'):
				pPlayer.setCurrentEra(gc.getInfoTypeForString('ERA_LEAF'))

		elif eStateReligion == en.eReligionRunesofKilmorph:
			if pPlayer.getCurrentEra() != gc.getInfoTypeForString('ERA_RUNE'):
				pPlayer.setCurrentEra(gc.getInfoTypeForString('ERA_RUNE'))

		elif eStateReligion == en.eReligionOctopusOverlords:
			if pPlayer.getCurrentEra() != gc.getInfoTypeForString('ERA_OCTO'):
				pPlayer.setCurrentEra(gc.getInfoTypeForString('ERA_OCTO'))

		elif eStateReligion == en.eReligionEmpyrean:
			if pPlayer.getCurrentEra() != gc.getInfoTypeForString('ERA_EMPY'):
				pPlayer.setCurrentEra(gc.getInfoTypeForString('ERA_EMPY'))

		elif eStateReligion == en.eReligionCouncilofEsus:
			if pPlayer.getCurrentEra() != gc.getInfoTypeForString('ERA_COUN'):
				pPlayer.setCurrentEra(gc.getInfoTypeForString('ERA_COUN'))
# ent - Return to Neutral Era >>>
		else:
			if pPlayer.getCurrentEra() > gc.getInfoTypeForString('ERA_RELIGIOUS'):
				eEraReligious = gc.getInfoTypeForString('ERA_RELIGIOUS')
				eLastEra = gc.getInfoTypeForString('ERA_ANCIENT')
				for eTech in xrange(gc.getNumTechInfos()):
					if pPlayer.isHasTech(eTech):
						eEra = gc.getTechInfo(eTech).getEra()
						if eEra > eLastEra and eEra != eEraReligious:
							eLastEra = eEra
				pPlayer.setCurrentEra(eLastEra)
# ent <<<

		if pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_CULTURAL_VALUES')) == gc.getInfoTypeForString('CIVIC_CRUSADE'):
			cf.doCrusade(iPlayer)

#Kaijin >>>

## doTurnKhazard is Move to "onBeginPlayerTurn - LoopCities"
#		if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_KHAZAD'):
#			cf.doTurnKhazad(iPlayer)

	## Loop check - Unit
		bLoopUnits = False

		bExperienceValue = False

		if CyGame().getGlobalCounter() > 30:
			bLoopUnits = True
#		elif eCiv in (gc.getInfoTypeForString('CIVILIZATION_ECHIGO'), gc.getInfoTypeForString('CIVILIZATION_NIRAIKANAI')):
#			bLoopUnits = True
		elif eCiv == gc.getInfoTypeForString('CIVILIZATION_LINEAGE'):
			bLoopUnits = True
		elif pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGGRESSIVE')):
			bLoopUnits = True
		elif pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_LEGEND')):
			bLoopUnits = True

		pTeam = gc.getTeam(pPlayer.getTeam())
		if pTeam.getAtWarCount(True) > 0:
			if not pPlayer.isHuman():
				bLoopUnits = True

	## Loop check - City
		"""
		bLoopCities = False

		if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_KHAZAD'):
			bLoopCities = True
		elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DROAUM'):
			bLoopCities = True
		elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DARK'):
			bLoopCities = True
		elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SCIONS'):
			bLoopCities = True
		elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_RARNA'):
			bLoopCities = True
		elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ARISTRAKH'):
			bLoopCities = True
		elif pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGGRESSIVE')):
			bLoopCities = True
		elif pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_CREATIVE')):
			bLoopCities = True
		elif pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_SUMMONER')):
			bLoopCities = True
		elif pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_ALMIGHTY')):
			bLoopCities = True
		elif pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_RICHES')):
			bLoopCities = True
		elif pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGRICULTURAL')):
			bLoopCities = True
		elif pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_MARTYRDOM')):
			bLoopCities = True
		elif pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_GREAT_PEOPLE')):
			bLoopCities = True
		elif pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_FANATIC')):
			bLoopCities = True
		elif pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_WARMONKEY')):
			bLoopCities = True
		elif pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_CRAZY_BY_WORLDHERITAGE')):
			bLoopCities = True
		"""
		bLoopCities = True

	## onBeginPlayerTurn - LoopUnits
		if bLoopUnits:
			for pUnit in PyPlayer(iPlayer).getUnitList():

				## Lineage
				if eCiv == gc.getInfoTypeForString('CIVILIZATION_LINEAGE'):
					## Disable Mounted Horse
					if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MOUNTED_HORSE')):
						bDisableValue = False
						if pUnit.getUnitClassType() in (	gc.getInfoTypeForString('UNITCLASS_HUNTER'), 
														gc.getInfoTypeForString('UNITCLASS_RANGER'), 
														gc.getInfoTypeForString('UNITCLASS_BEASTMASTER'), 
														gc.getInfoTypeForString('UNITCLASS_ASSASSIN'), 
														gc.getInfoTypeForString('UNITCLASS_AXEMAN'), 
														gc.getInfoTypeForString('UNITCLASS_CHAMPION'),
														gc.getInfoTypeForString('UNITCLASS_PHALANX'), 
														gc.getInfoTypeForString('UNITCLASS_MERCENARY'), 
														gc.getInfoTypeForString('UNITCLASS_ARCHER'), 
														gc.getInfoTypeForString('UNITCLASS_LONGBOWMAN'), 
														gc.getInfoTypeForString('UNITCLASS_MARKSMAN'), 
														gc.getInfoTypeForString('UNITCLASS_PALADIN'), 
														gc.getInfoTypeForString('UNITCLASS_LINEAGE_SAINT'), 
														gc.getInfoTypeForString('UNITCLASS_GOZEWAROS')		):
							bDisableValue = True
						if not bDisableValue:
							pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MOUNTED_HORSE'), False)

			## LoopUnits - Traits
				## Aggressive - Occupation forces get experience points
				if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGGRESSIVE')):
					iExperienceChance = cyFlatValue(20, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
					if gc.getGame().getSorenRandNum(100, "Unit gets Experience Percent") < iExperienceChance:
						pPlot = pUnit.plot()
						if pPlot.isCity():
							pUnit.changeExperience(1, 3, False, False, False)

				## Legend - Experience points to give the whole army every turn
				if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_LEGEND')):
					py = PyPlayer(iPlayer)
					if bExperienceValue == False:
						if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_HERO')):
							iExperienceChance = cyFlatValue(25, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
							if gc.getGame().getSorenRandNum(100, "Unit gets Experience Percent") < iExperienceChance:
								bExperienceValue = True
								for pAddExpUnit in py.getUnitList():
									pAddExpUnit.changeExperience(1, 100, False, False, False)

# Kaijin >>>	patch29 expansion - Start -
			## LoopUnits - Religions
				## Octopus Overlords - The Curse of the Necronomicon.
				pPlot = pUnit.plot()
				if pPlot.isOwned():
					if pPlot.isWater():
						pPlotPlayer = gc.getPlayer(pPlot.getOwner())
						if pPlotPlayer.getStateReligion() == gc.getInfoTypeForString('RELIGION_OCTOPUS_OVERLORDS'):
							pPlayerTeam = gc.getTeam(pPlayer.getTeam())
							pPlotPlayerTeam = gc.getTeam(pPlotPlayer.getTeam())
							if pPlayerTeam != pPlotPlayerTeam:
								if pPlotPlayer.getNumCities() > 0:
									if pPlotPlayer.getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_THE_NECRONOMICON')) > 0:
										pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SLOW'), True)
# Kaijin <<<	patch29 expansion - End -

			## LoopUnits - Another
				## Cursed token of ragnarok - Summon monster
				if CyGame().getGlobalCounter() > 30:
					if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CURSED_TOKEN_OF_RAGNAROK')) or pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_CURSED_TOKEN_OF_RAGNAROK'):
						if CyGame().getSorenRandNum(100, "Summon monster") < gc.getHandicapInfo(gc.getGame().getHandicapType()).getLairSpawnRate():
							iDemonsBarbarian = gc.getInfoTypeForString('BARBARIAN_DEMONS') + gc.getBARBARIAN_PLAYER()
							pDemonsBarbarian = gc.getPlayer(iDemonsBarbarian)
							liMonsters = [	gc.getInfoTypeForString('UNIT_MARCHOSIAS'),
									gc.getInfoTypeForString('UNIT_PIT_BEAST')	]
							if CyGame().getGlobalCounter() > 60:
								liMonsters += [	gc.getInfoTypeForString('UNIT_BEAST_OF_AGARES'),
										gc.getInfoTypeForString('UNIT_MANTICORE'),
										gc.getInfoTypeForString('UNIT_AHALPUH')	]

							pPlot = pUnit.plot()
							lpRangedPlots = cyGetRangedPlots(pPlot, 1, False, False, TeamTypes.NO_TEAM)
							for pLoopPlot in lpRangedPlots:
								if not pLoopPlot.isNone():
									if not pLoopPlot.isVisibleEnemyUnit(iDemonsBarbarian):
										if CyGame().getSorenRandNum(100, "Summon monster spawn") < 30:
											iMonsterUnit= liMonsters[CyGame().getSorenRandNum(len(liMonsters), "Pick Monster")]
											pNewUnit = pDemonsBarbarian.initUnit(iMonsterUnit, pLoopPlot.getX(), pLoopPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
				"""
			## Siege AI Bug Fix
				if not pPlayer.isHuman():
					eTeam = pPlayer.getTeam()
					pPlot = pUnit.plot()
					iRange = 1
					lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, False, TeamTypes.NO_TEAM)
					for pLoopPlot in lpRangedPlots:
						if pLoopPlot.isEnemyCity(pUnit):
							if pUnit.canMoveInto(pLoopPlot, False, False, False):
								lpRangedUnits = cyGetRangedUnits(pLoopPlot, 0, False, False, TeamTypes.NO_TEAM)
								lpDefensiveUnits = [ pDefensiveUnit for pDefensiveUnit in lpRangedUnits
															if	pDefensiveUnit.canFight()
															and	pDefensiveUnit.isEnemy(eTeam, pDefensiveUnit.plot())	]
								iTotalValue = 0
								for pLoopUnit in lpDefensiveUnits:
									iValue = 1
									if pLoopUnit.getLevel() >= 6:
										iValue += 1
									if pLoopUnit.getUnitCombatType() == en.eUnitCombatArcher:
										iValue += 1
									iTotalValue += (iValue * 5)
								if len(lpDefensiveUnits) <= 2 and iTotalValue < pUnit.getGroup().getNumUnits():
									pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, True, False, MissionAITypes.NO_MISSIONAI, pPlot, pUnit)
									pUnit.getGroup().pushMission(MissionTypes.MISSION_MOVE_TO, pLoopPlot.getX(), pLoopPlot.getY(), 0, False, False, MissionAITypes.NO_MISSIONAI, pLoopPlot, gc.getPlayer(pUnit.getOwner()).getUnit(-1))
									pUnit.getGroup().pushMoveToMission(pLoopPlot.getX(), pLoopPlot.getY())
				"""

	## onBeginPlayerTurn - LoopCities
		if bLoopCities:
			for pyCity in PyPlayer(iPlayer).getCityList():
				pCity = pyCity.GetCy()

			## LoopCities - Civilizations
				## Khazad
				if eCiv == gc.getInfoTypeForString('CIVILIZATION_KHAZAD'):
					if pPlayer.getNumCities() > 0:
						cf.doTurnKhazad(iPlayer, pCity)

				## Droaum
				elif eCiv == gc.getInfoTypeForString('CIVILIZATION_DROAUM'):
					if pPlayer.getNumCities() > 0:
						cf.doTurnDROAUM(iPlayer, pCity)

				## Scions
				elif eCiv == gc.getInfoTypeForString('CIVILIZATION_SCIONS'):
					if pPlayer.getNumCities() > 0:
						cf.doTurnScions(iPlayer, pCity)

				## Rarna
				elif eCiv == gc.getInfoTypeForString('CIVILIZATION_RARNA'):
					## Spread Corruption - Given Citizen of the Dead.
					if (	CyGame().getProjectCreatedCount(gc.getInfoTypeForString('PROJECT_SPREAD_CORRUPTION')) > 0 
							and CyGame().getProjectCreatedCount(gc.getInfoTypeForString('PROJECT_PRINCESS_OF_DARKNESS')) == 0	):
						if pPlayer.getNumCities() > 0:
							pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_CITIZEN_OF_THE_DEAD'), 1)
					## Princess of Darkness - Given Immortal Citizen and Abyss, Removed Citizen of the Dead.
					if CyGame().getProjectCreatedCount(gc.getInfoTypeForString('PROJECT_PRINCESS_OF_DARKNESS')) > 0:
						if pPlayer.getNumCities() > 0:
							pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_CITIZEN_OF_THE_DEAD'), 0)
							pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_IMMORTAL_CITIZEN'), 1)
							pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_ABYSS'), 1)

				## Aristrakh
				elif eCiv == gc.getInfoTypeForString('CIVILIZATION_ARISTRAKH'):
					if pPlayer.getNumCities() > 0:
						cf.doTurnAristrakh(iPlayer, pCity)

			## LoopCities - Traits
				## Aggressive - Installation of the Aggressive
				if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGGRESSIVE')):
					if pPlayer.getNumCities() > 0:
						pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_AGGRESSIVE'), 1)

				## Creative - Explosive creativity
				if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_CREATIVE')):
					if pPlayer.getNumCities() > 0:
						pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_CREATIVE'), 1)

				## Summoner - Installation of the Portal
				if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_SUMMONER')):
					if pPlayer.getNumCities() > 0:
						pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_SUMMONER'), 1)

				## Almighty - We Love the King !
				if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_ALMIGHTY')):
					if pPlayer.getNumCities() > 0:
						PerWeLoveTheKing = cyFlatValue(10, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
						if gc.getGame().getSorenRandNum(100, "Golden Age Percent") <= PerWeLoveTheKing:
							pCity.changeWeLoveTheKingDayProbability(90)

				## Riches - Installation of the Riches
				if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_RICHES')):
					if pPlayer.getNumCities() > 0:
						cf.doTurnRiches(iPlayer, pCity)

				## Agricultural - Installation of the Agricultural
				if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGRICULTURAL')):
					if pPlayer.getNumCities() > 0:
						pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_AGRICULTURAL'), 1)

				## Construction - Installation of the Construction
				if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_CONSTRUCTION')):
					if pPlayer.getNumCities() > 0:
						pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_CONSTRUCTION'), 1)

				## Martyrdom - Installation of the Martyrdom
				if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_MARTYRDOM')):
					if pPlayer.getNumCities() > 0:
						pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_MARTYRDOM'), 1)

				## Great people - Neat
				if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_GREAT_PEOPLE')):
					if pPlayer.getNumCities() > 0:
						pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_GREAT_PEOPLE'), 1)

				## Fanatic - Missionary and heresy purge
				if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_FANATIC')):
					iStateBelief = pPlayer.getStateReligion()
					if pPlayer.getNumCities() > 0 and iStateBelief != ReligionTypes.NO_RELIGION:
						if not pCity.isHolyCityByType(iStateBelief):
							pCity.setHasReligion(iStateBelief, True, True, True)
						for iReligion in xrange(gc.getNumReligionInfos()):
							if iStateBelief != iReligion and pCity.isHasReligion(iReligion) and not pCity.isHolyCityByType(iReligion):
								pCity.setHasReligion(iReligion, False, True, True)
								for iBuilding in xrange(gc.getNumBuildingInfos()):
									if gc.getBuildingInfo(iBuilding).getPrereqReligion() == iReligion:
										if pCity.isHasActiveBuilding(iBuilding):
											if gc.getBuildingClassInfo(gc.getBuildingInfo(iBuilding).getBuildingClassType()).getMaxGlobalInstances() != 1:
												pCity.setNumRealBuilding(iBuilding, 0)

				## Wormonkey - Give the city a hammer by the value of war weariness
				if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_WARMONKEY')):
					if pPlayer.getNumCities() > 0:
						iWearinessPercentAnger = pCity.getWarWearinessPercentAnger()
						iCityPop = pCity.getPopulation()
						iReligionPercentAnger = pCity.getReligionPercentAnger()
						##厭戦率から厭戦値を計算
						iWearinessAnger = (iCityPop * iWearinessPercentAnger) / 1000
						iReligionAnger = (iCityPop * iReligionPercentAnger) / 1000
						##実際の厭戦値を計算
						iWarTotalAnger = iWearinessAnger + iReligionAnger
						##厭戦値分のハンマーを都市に与える
						iProduction = cyFlatValue(iWarTotalAnger, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getConstructPercent(), False)
						pCity.changeProduction(iProduction)

				## Crazy by worldheritage - Heritage Enthusiasts
				if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_CRAZY_BY_WORLDHERITAGE')):
					if pPlayer.getNumCities() > 0:
						pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_CRAZY_BY_WORLDHERITAGE'), 1)

			## LoopCities - Another
				if pPlayer.getNumCities() > 0:
					## Gain CultureLevelBounus.
					if not pPlayer.isBarbarian():
						iCultureLevel = pCity.getCultureLevel()
						pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_CULTURELEVEL_BONUS_REFINED'), 0)
						pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_CULTURELEVEL_BONUS_INFLUENTIAL'), 0)
						pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_CULTURELEVEL_BONUS_LEGENDARY'), 0)

						if iCultureLevel == 4:
							pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_CULTURELEVEL_BONUS_REFINED'), 1)
						elif iCultureLevel == 5:
							pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_CULTURELEVEL_BONUS_INFLUENTIAL'), 1)
						elif iCultureLevel == 6:
							pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_CULTURELEVEL_BONUS_LEGENDARY'), 1)

					## Malakim - Citadel of Light
					if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_CITADEL_OF_LIGHT')):
						iCitadelOfLight = gc.getInfoTypeForString('BUILDING_CITADEL_OF_LIGHT')
						pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_LIGHTBRINGER'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
						pNewUnit.setName(gc.getBuildingInfo(iCitadelOfLight).getDescription())
						pNewUnit.cast(gc.getInfoTypeForString('SPELL_CITADEL_OF_LIGHT'))
						pNewUnit.kill(False, PlayerTypes.NO_PLAYER)

					## Despiel - Pollution Law Library
					if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_POLLUTION_LAW_LIBRARY')):
						iPollutionLawLibrary = gc.getInfoTypeForString('BUILDING_POLLUTION_LAW_LIBRARY')
						pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_BONE_PLAYER'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
						pNewUnit.setName(gc.getBuildingInfo(iPollutionLawLibrary).getDescription())
						pNewUnit.cast(gc.getInfoTypeForString('SPELL_POLLUTION_LAW_LIBRARY'))
						pNewUnit.kill(False, PlayerTypes.NO_PLAYER)

					## Megisus - Forest Eclipse
					if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_FOREST_ECLIPSE')):
						cf.doForestEclipse(iPlayer)

					## Runes of Kilmorph - Tablets of Bambur
					if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_TABLETS_OF_BAMBUR')):
						if pPlayer.getStateReligion() == gc.getInfoTypeForString('RELIGION_RUNES_OF_KILMORPH'):
							cf.doTabletsOfBambur(iPlayer)

## onBeginPlayerTurn - NoLoop
	## NoLoop - Civilizations
		## Tiger
		if eCiv == gc.getInfoTypeForString('CIVILIZATION_TIGER'):
			## Contract War
			if bool(pPlayer.getGuildPlusCounter(50)):
				cf.doTurnContract(iPlayer)
				if pPlayer.getNumCities() > 0:
					pCapital = pPlayer.getCapitalCity()
					pCapital.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_ECONOMIC_AGREEMENT'), 1)
			## Steindorf and Smiley
			if pPlayer.getLeaderType() != gc.getInfoTypeForString('LEADER_STEINDORF'):
				cf.doTigerSteindorfAndSmiley(iPlayer)

		## Xoth
		elif eCiv == gc.getInfoTypeForString('CIVILIZATION_XOTH'):
			iThresholdTurn = cyFlatValue(10, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
			if pPlayer.getGuildPlusCounter(51) == 0:
				if pPlayer.getGuildPlusCounter(50) > 0:
					pPlayer.changeGuildPlusCounter(50, -1)
				elif pPlayer.getGuildPlusCounter(50) < 0:
					pPlayer.setGuildPlusCounter(50, 0)
				pPlayer.setGuildPlusCounter(51, iThresholdTurn)
			else:
				pPlayer.changeGuildPlusCounter(51, -1)

		## Baldralfar
		elif eCiv == gc.getInfoTypeForString('CIVILIZATION_BALDRALFAR'):
			cf.doBaldralfar(iPlayer)

	## NoLoop - Traits
		## Imperialist - Installation of the Imperialist
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_IMPERIALIST')):
			if pPlayer.getNumCities() > 0:
				pCapital = pPlayer.getCapitalCity()
				pCapital.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_IMPERIALIST'), 1)

		## Legend - Activation of the golden age
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_LEGEND')):
			if not pPlayer.isGoldenAge():
				PerGoldenAge = cyFlatValue(5, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
				if gc.getGame().getSorenRandNum(100, "Golden Age Percent") < PerGoldenAge:
					pPlayer.changeGoldenAgeTurns(CyGame().goldenAgeLength() // 2)

		## Unreasonable - Random Golden Age
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_UNREASONABLE')):
			if not pPlayer.isGoldenAge():
				PerGoldenAge = cyFlatValue(3, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
				if gc.getGame().getSorenRandNum(100, "Golden Age Percent") < PerGoldenAge:
					pPlayer.changeGoldenAgeTurns(CyGame().goldenAgeLength() // 3)
			else:
				PerGoldenAge = cyFlatValue(5, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
				if gc.getGame().getSorenRandNum(100, "Golden Age Percent") < PerGoldenAge:
					iLength = -1 * (CyGame().goldenAgeLength() // 3)
					if pPlayer.getGoldenAgeTurns() < CyGame().goldenAgeLength() // 3:
						iLength = -1 * (pPlayer.getGoldenAgeTurns())
					pPlayer.changeGoldenAgeTurns(iLength)

		## Temperamental - Change alignment
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_TEMPERAMENTAL')):
			if CyGame().getSorenRandNum(1000, "Temperamental") < 100:
				iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(),'EVENTTRIGGER_TRAIT_TEMPERAMENTAL')
				triggerData = pPlayer.initTriggeredData(iEvent, True, -1, -1, -1, PlayerTypes.NO_PLAYER, -1, ReligionTypes.NO_RELIGION, CorporationTypes.NO_CORPORATION, -1, BuildingTypes.NO_BUILDING)

		## Fool - Change Two Traits
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_UNENLIGHTENED')):
			if CyGame().getSorenRandNum(1000, "Fool") <= 10:
				cf.doTraitFool(iPlayer)

		## Fanatic - Declared war on the known infidels
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_FANATIC')):
			iStateBelief = pPlayer.getStateReligion()
			if pPlayer.getNumCities() > 0 and iStateBelief != ReligionTypes.NO_RELIGION:
				iTeam = pPlayer.getTeam()
				pTeam = gc.getTeam(iTeam)
				for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
					pLoopPlayer = gc.getPlayer(iLoopPlayer)
					if pLoopPlayer.isAlive() and not pLoopPlayer.isBarbarian():
						if pLoopPlayer.getStateReligion() != ReligionTypes.NO_RELIGION and pLoopPlayer.getStateReligion() != iStateBelief:
							iLoopTeam = pLoopPlayer.getTeam()
							if iTeam != iLoopTeam:
								if pTeam.canDeclareWar(iLoopTeam):
									pTeam.declareWar(iLoopTeam, True, WarPlanTypes.WARPLAN_LIMITED)

		## Wormonkey - Declared war on the known player
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_WARMONKEY')):
			iGameTurn = CyGame().getGameTurn()
			iOrthusTurn = cyFlatValue(75, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
			if iGameTurn >= iOrthusTurn:
				iTeam = pPlayer.getTeam()
				pTeam = gc.getTeam(iTeam)
				for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
					pLoopPlayer = gc.getPlayer(iLoopPlayer)
					if pLoopPlayer.isAlive() and not pLoopPlayer.isBarbarian():
						iLoopTeam = pLoopPlayer.getTeam()
						if iTeam != iLoopTeam:
							if pTeam.canDeclareWar(iLoopTeam):
								pTeam.declareWar(iLoopTeam, True, WarPlanTypes.WARPLAN_LIMITED)

	## NoLoop - Another
# Kaijin >>>	patch29 expansion - Start -
		if pPlayer.getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_DEMONS_ALTAR')) > 0:
			if pPlayer.getGuildPlusCounter(5) != 0:
				pPlayer.setGuildPlusCounter(5, 0)
# Kaijin <<<	patch29 expansion - End -

		if pPlayer.isHuman():

			## anon begin
			## Productions Alert
			cf.doAlert(iPlayer)
			## anon end

		else:
# ent >>>
		## Victory Conditions Switch
			"""
			if not pPlayer.isBarbarian():
				## Victory - Conquest and Domination
				if CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_CONQUEST')) or CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_DOMINATION')):
					pyTeam = player.getTeam()

					iTotalLand = gc.getMap().getLandPlots()
					ourLand = pyTeam.getTotalLand()
					landPercent = -1
					if iTotalLand > 0:
						landPercent = (ourLand * 100.0) / iTotalLand
					if landPercent >= 35:
						pPlayer.setGuildPlusCounter(2, 1)

				## Victory - Cultural
				elif CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_CULTURAL')):
					pyTeam = player.getTeam()
					bNotTopCulture = -1

					ourCulture = pyTeam.countTotalCulture()
					for iLoopTeam in xrange(gc.getMAX_CIV_TEAMS()):
						if (gc.getTeam(iLoopTeam).isAlive() and not gc.getTeam(iLoopTeam).isMinorCiv() and not gc.getTeam(iLoopTeam).isBarbarian()):
							if (iLoopTeam != iActiveTeam and (pyTeam.isHasMet(iLoopTeam) or CyGame().isDebugMode())):
								iLoopTeamCulture = gc.getTeam(iLoopTeam).countTotalCulture()
								if (ourCulture < iLoopTeamCulture):
									bNotTopCulture = 1
					if not bNotTopCulture:
						pPlayer.setGuildPlusCounter(2, 2)

				## Victory - Religious
				elif CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_RELIGIOUS')):
					pyTeam = player.getTeam()

					for iLoopReligion in xrange(gc.getNumReligionInfos()):
						if pyTeam.hasHolyCity(iLoopReligion):
							iReligionPercent = CyGame().calculateReligionPercent(iLoopReligion)
							if iReligionPercent >= 30:
								pPlayer.setGuildPlusCounter(2, 3)
								break

				## Victory - Tower of mastery
				elif CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_TOWER_OF_MASTERY')):
					iTower = -1

					if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_TOWER_OF_ALTERATION')) >= 1:
						iTower += 1
					if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_TOWER_OF_DIVINATION')) >= 1:
						iTower += 1
					if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_TOWER_OF_NECROMANCY')) >= 1:
						iTower += 1
					if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_TOWER_OF_THE_ELEMENTS')) >= 1:
						iTower += 1

					if iTower >= 3:
						pPlayer.setGuildPlusCounter(2, 4)

				## Victory - Alter of the luonnotar
				elif CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_ALTAR_OF_THE_LUONNOTAR')):
					if ( pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_CONSECRATED')) >= 1
						or pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_DIVINE')) >= 1
						or pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_EXALTED')) >= 1
						or pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_FINAL')) >= 1	):

						pPlayer.setGuildPlusCounter(2, 5)

				## Victory - Led to the end
				elif CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_LED_TO_THE_END')) and not CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_GLOBAL_COUNTER):
					if ( pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_RAGE')) >= 1
						or pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_BLACK_DEATH')) >= 1
						or pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_HOLLOW')) >= 1
						or pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_END')) >= 1	):

						pPlayer.setGuildPlusCounter(2, 6)

				else:
					pPlayer.setGuildPlusCounter(2, 0)
			"""
			if not pPlayer.isBarbarian() and pPlayer.getGameProgressPercent() >= 30:

				def selectConditionSwitch():
					# 0: No Plan
					# 1: Victory - Conquest and Domination
					# 2: Victory - Cultural
					# 3: Victory - Religious
					# 4: Victory - Tower of mastery
					# 5: Victory - Alter of the luonnotar
					# 6: Victory - Led to the end
					# 7: Victory - Statue of Luxury

					pyTeam = player.getTeam()

					## Victory - Conquest and Domination
					if CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_CONQUEST')) or CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_DOMINATION')):
						if eCiv in (gc.getInfoTypeForString('CIVILIZATION_MERCURIANS'), gc.getInfoTypeForString('CIVILIZATION_ALTAIR')):
							return 1

						iTotalLand = gc.getMap().getLandPlots()
						ourLand = pyTeam.getTotalLand()
						landPercent = -1
						if iTotalLand > 0:
							landPercent = (ourLand * 100.0) / iTotalLand
						if landPercent >= 35:
							return 1

					## Victory - Tower of mastery
					if CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_TOWER_OF_MASTERY')):
						iNumTowers = 0
						iNumTowers += pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_TOWER_OF_ALTERATION'))
						iNumTowers += pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_TOWER_OF_DIVINATION'))
						iNumTowers += pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_TOWER_OF_NECROMANCY'))
						iNumTowers += pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_TOWER_OF_THE_ELEMENTS'))

						if iNumTowers >= 3:
							return 4

					## Victory - Alter of the luonnotar
					if CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_ALTAR_OF_THE_LUONNOTAR')):
						if ( pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_CONSECRATED')) >= 1
							or pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_DIVINE')) >= 1
							or pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_EXALTED')) >= 1
							or pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_FINAL')) >= 1	):

							return 5

					## Victory - Led to the end
					if CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_LED_TO_THE_END')) and not CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_GLOBAL_COUNTER) and CyGame().getGlobalCounter() > 30:
						if ( pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_RAGE')) >= 1
							or pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_BLACK_DEATH')) >= 1
							or pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_HOLLOW')) >= 1
							or pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_END')) >= 1	):

							return 6

					## Victory - Statue of Luxury
					if CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_STATUE_OF_LUXURY')):
						iNumPrereqLuxury = 0
						if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_MERCANTILISM')):
							iNumPrereqLuxury += 2
						if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_GUILDS')):
							iNumPrereqLuxury += 3
						if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_BLASTING_POWDER')):
							iNumPrereqLuxury += 3
						if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_MACHINERY')):
							iNumPrereqLuxury += 4
						if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_ASTRONOMY')):
							iNumPrereqLuxury += 2
						if pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_COPPER')) > 0:
							iNumPrereqLuxury += 1
						if pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_MITHRIL')) > 0:
							iNumPrereqLuxury += 3

						if iNumPrereqLuxury >= 10:
							return 7

					## Victory - Religious
					if CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_RELIGIOUS')):

						ltReligionPercents = []
						for eReligion in xrange(gc.getNumReligionInfos()):
							iReligionPercent = CyGame().calculateReligionPercent(eReligion)
							ltReligionPercents.append((iReligionPercent, eReligion))
						ltReligionPercents.sort()
						ltReligionPercents.reverse()
						eBestReligion = ltReligionPercents[0][1]
						if CyGame().getHolyCity(eBestReligion).getOwner() == iPlayer and gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getReligionWeightModifier(eBestReligion) >= 0:
							iBestReligionPercent = ltReligionPercents[0][0]
							if iBestReligionPercent > 50:
								return 3
							if iBestReligionPercent > 2 * ltReligionPercents[1][0]:
								return 3

					## Victory - Cultural
					if CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_CULTURAL')) and pPlayer.getNumCities() >= 3:
						# If you have a score in first group, you should not select cultural victory.
						if CyGame().getPlayerRank(iPlayer) >= 3 and (5 * CyGame().getPlayerScore(iPlayer) < 4 * CyGame().getPlayerScore(CyGame().getRankPlayer(1))):
							iCulturalResources = 0
							for eReligion in xrange(gc.getNumReligionInfos()):
								if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getReligionWeightModifier(eReligion) >= 0:
									if eReligion == en.eReligionCouncilofEsus:
										continue
									elif eReligion == en.eReligionOctopusOverlords:
										iCulturalResources += 2
									else:
										iCulturalResources += 1
							leCulturalWonders = [	gc.getInfoTypeForString('BUILDINGCLASS_THEATRE_OF_DREAMS'), 
													gc.getInfoTypeForString('BUILDINGCLASS_HALL_OF_KINGS'), 
													gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_TEMPORENCE') ]
							infoCiv = gc.getCivilizationInfo(pPlayer.getCivilizationType())
							for eBuildingClass in leCulturalWonders:
								eBuilding = infoCiv.getCivilizationBuildings(eBuildingClass)
								if eBuilding != BuildingTypes.NO_BUILDING:
									if pPlayer.getNumBuilding(eBuilding) > 0:
										iCulturalResources += 5
									elif not CyGame().isBuildingClassMaxedOut(eBuildingClass, 0):
										iCulturalResources += 1
							if iCulturalResources > 10: # max 22 (7 from Religions)
								return 2
							iActiveTeam = pPlayer.getTeam()
							ourCulture = pPlayer.countTotalCulture()
							for eLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
								pLoopPlayer = gc.getPlayer(eLoopPlayer)
								if pLoopPlayer.isAlive() and pLoopPlayer.getTeam() != iActiveTeam and CyGame().getPlayerRank(eLoopPlayer) < 3:
									if (ourCulture < pLoopPlayer.countTotalCulture()):
										break
							else:
								return 2
						if pyTeam.isAVassal():
							return 2

					return 0

				pPlayer.setGuildPlusCounter(2, selectConditionSwitch())
				CvUtil.pyPrint('AIPlayer %d (%s) set Victorious switch %d' %(iPlayer, pPlayer.getName(), pPlayer.getGuildPlusCounter(2)))
# ent <<<

#Kaijin <<<

##--------	Unofficial Bug Fix: Modified by Denev	--------##
#		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_INSANE')):
		if pPlayer.isInsane():
##--------	Unofficial Bug Fix: End Modify			--------##
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#			if CyGame().getSorenRandNum(1000, "Insane") < 20:
			if CyGame().getSorenRandNum(gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getGoldenAgePercent(), "Insane") < 2:
##--------	Unofficial Bug Fix: End Modify			--------##
##--------	Choose Trait: Modified by Denev 2013/02/23
				"""
				iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(), 'EVENTTRIGGER_TRAIT_INSANE')
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#				triggerData = pPlayer.initTriggeredData(iEvent, True, -1, -1, -1, iPlayer, -1, -1, -1, -1, -1)
				pPlayer.trigger(iEvent)
##--------	Unofficial Bug Fix: End Modify			--------##
				"""
				pPlayer.clearTrait(TraitSourceTypes.TRAITSOURCE_INSANE)
				leTrait = [eTrait for eTrait in xrange(gc.getNumTraitInfos()) if gc.getTraitInfo(eTrait).isSelectable() and not gc.getLeaderHeadInfo(pPlayer.getLeaderType()).hasTrait(eTrait)]
				leChosenTrait = []
				for iLoop in xrange(3):
					leChosenTrait.append(leTrait.pop(CyGame().getSorenRandNum(len(leTrait), "Insane")))
				leChosenTrait.sort()
				for eChosenTrait in leChosenTrait:
					pPlayer.setHasTraitWithSource(eChosenTrait, True, TraitSourceTypes.TRAITSOURCE_INSANE)

				if pPlayer.isHuman():
					popupInfo = CyPopupInfo()
					popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
					popupInfo.setText(localText.getText("TXT_KEY_EVENTTRIGGER_TRAIT_INSANE",()))
#					popupInfo.addPythonButton(localText.getText("TXT_KEY_EVENT_TRAIT_INSANE",()), gc.getTraitInfo(gc.getInfoTypeForString('TRAIT_INSANE')).getButton())
					popupInfo.addPythonButton(localText.getText("TXT_KEY_EVENT_TRAIT_INSANE",()), gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getButton())
					popupInfo.addPopup(iPlayer)
##--------	Choose Trait: End Modify			--------##

##--------	Unofficial Bug Fix: Modified by Denev	--------##
#		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_ADAPTIVE')):
		if pPlayer.isAdaptive():
##--------	Unofficial Bug Fix: End Modify			--------##
			iGameSpeed = gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getGoldenAgePercent()
			iCycleTurn = 100
			iMod = (((iGameTurn + 1) * 100) % (iCycleTurn * iGameSpeed)) // 100
			if iMod == 0:
##--------	Choose Trait: Modified by Denev 2013/02/23
				"""
				iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(), 'EVENTTRIGGER_TRAIT_ADAPTIVE')
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#				triggerData = pPlayer.initTriggeredData(iEvent, True, -1, -1, -1, iPlayer, -1, -1, -1, -1, -1)
				pPlayer.trigger(iEvent)
##--------	Unofficial Bug Fix: End Modify			--------##
				"""
				pPlayer.updateAdaptiveTrait()
##--------	Choose Trait: End Modify			--------##

# Kaijin >>>
##--------	Unofficial Bug Fix: Added by Denev	--------##
		"""
		for pyCity in PyPlayer(iPlayer).getCityList():
			pCity = pyCity.GetCy()

			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_CITADEL_OF_LIGHT')):
				iCitadelOfLight = gc.getInfoTypeForString('BUILDING_CITADEL_OF_LIGHT')
				pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_LIGHTBRINGER'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
				pNewUnit.setName(gc.getBuildingInfo(iCitadelOfLight).getDescription())
				pNewUnit.cast(gc.getInfoTypeForString('SPELL_CITADEL_OF_LIGHT'))
				pNewUnit.kill(False, PlayerTypes.NO_PLAYER)
		"""
		"""
		if not pPlayer.isBarbarian():
			for pyCity in PyPlayer(iPlayer).getCityList():
				pCity = pyCity.GetCy()

				if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_CITADEL_OF_LIGHT')):
					iCitadelOfLight = gc.getInfoTypeForString('BUILDING_CITADEL_OF_LIGHT')
					pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_LIGHTBRINGER'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
					pNewUnit.setName(gc.getBuildingInfo(iCitadelOfLight).getDescription())
					pNewUnit.cast(gc.getInfoTypeForString('SPELL_CITADEL_OF_LIGHT'))
					pNewUnit.kill(False, PlayerTypes.NO_PLAYER)
		"""
##--------	Unofficial Bug Fix: End Add			--------##
# Kaijin <<<

		if pPlayer.isHuman():
			if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_BARBARIAN')):
##--------	Multiple Barbarians Ally: Modified by ent	--------##
				"""
				pBarbarianTeam = gc.getTeam(gc.getBARBARIAN_TEAM())
				iTeam = pPlayer.getTeam()
				if not pBarbarianTeam.isAtWar(iTeam):
					if 2 * CyGame().getPlayerScore(iPlayer) >= 3 * CyGame().getPlayerScore(CyGame().getRankPlayer(1)):
						iGrace = cyFlatValue(24, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getGoldenAgePercent(), False)
						if iGameTurn > iGrace:
							pBarbarianTeam.declareWar(iTeam, False, WarPlanTypes.WARPLAN_TOTAL)
							if iPlayer == CyGame().getActivePlayer():
								cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_BARBARIAN_DECLARE_WAR", ()), 'art/interface/popups/Barbarian.dds')
				"""
				eTeam = pPlayer.getTeam()
				eBarbarianTeam = gc.getBARBARIAN_TEAM()
				if 2 * CyGame().getTeamScore(eTeam) >= 3 * CyGame().getTeamScore(CyGame().getRankTeam(1)):
					iGrace = cyFlatValue(24, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getGoldenAgePercent(), False)
					if iGameTurn > iGrace:
						if gc.getTeam(eTeam).isBarbarianAlly(eBarbarianTeam):
				 			pPlayer.setBarbarianAlly(eBarbarianTeam, False)
							if iPlayer == CyGame().getActivePlayer():
								cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_BARBARIAN_DECLARE_WAR", ()), 'art/interface/popups/Barbarian.dds')
##--------	Multiple Barbarians Ally: End Modify			--------##
##--------	Merging CGE: Added by Denev	--------##
			AlertsLog.AlertsLog().AlertsLogStartTurn()
##--------	Merging CGE: End Add		--------##

		else:
			if not CyGame().getWBMapScript():
				cf.warScript(iPlayer)

	def onEndPlayerTurn(self, argsList):
		'Called at the end of a players turn'
		iGameTurn, iPlayer = argsList

##--------	Advanced Rules: Added by Denev	--------##
		pPlayer = gc.getPlayer(iPlayer)
		if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_AMURITES'):
			cf.doTurnAmurites(iPlayer)

		elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LUCHUIRP'):
			cf.doTurnLuchuirp(iPlayer)

		eBabySpider = gc.getInfoTypeForString('UNIT_BABY_SPIDER')
		for pLoopUnit in PyPlayer(iPlayer).getUnitList():
			if pLoopUnit.getUnitType() == eBabySpider:
				if pLoopUnit.getLevel() > 3:
					pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_GIANT_SPIDER'), pLoopUnit.getX(), pLoopUnit.getY(), pLoopUnit.getUnitAIType(), pLoopUnit.getFacingDirection())
					CyInterface().addMessage(pNewUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_UNIT_AUTOMATIC_UPGRADE", (pLoopUnit.getName(), pNewUnit.getName())), '', InterfaceMessageTypes.MESSAGE_TYPE_MINOR_EVENT, pNewUnit.getButton(), en.eColorGreen, pNewUnit.getX(), pNewUnit.getY(), True, True)
					pNewUnit.convert(pLoopUnit)
##--------	Advanced Rules: End Add			--------##

##--------	Unofficial Bug Fix: Added by Denev	--------##
		for pyCity in PyPlayer(iPlayer).getCityList():
			pCity = pyCity.GetCy()
			pPlot = pCity.plot()

			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_HALL_OF_MIRRORS')):
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#				if CyGame().getSorenRandNum(100, "Hall of Mirrors") <= 100:
				if True:
##--------	Unofficial Bug Fix: End Modify			--------##
					lpRangedUnits = cyGetRangedUnits(pPlot, 1, False, True, pCity.getTeam())
					lpEnemyUnits = [	pEnemyUnit for pEnemyUnit in lpRangedUnits
													if	pEnemyUnit.canFight()
													and	pEnemyUnit.isEnemy(pCity.getTeam(), pEnemyUnit.plot())
													and	not pEnemyUnit.isImmuneToMagic()
													and not isWorldUnitClass(pEnemyUnit.getUnitClassType())
													and not pEnemyUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ILLUSION'))
													and not pEnemyUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_VAMPIRE'))	]
					if len(lpEnemyUnits) > 0:
						fBaseProbabilityPerUnit = 0.3
						iProbability = int((1.0 - fBaseProbabilityPerUnit ** len(lpEnemyUnits)) * 10000)
						if CyGame().getSorenRandNum(10000, "Hall of Mirrors") < iProbability:
							pEnemyUnit = lpEnemyUnits[CyGame().getSorenRandNum(len(lpEnemyUnits), "Pick Mirrored Enemy")]
							pNewUnit = pPlayer.initUnit(pEnemyUnit.getUnitType(), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
							pNewUnit.setHomeCivilizationType(pEnemyUnit.getHomeCivilizationType())
							for iPromotion in xrange(gc.getNumPromotionInfos()):
								if gc.getPromotionInfo(iPromotion).isEquipment():
									pNewUnit.setHasPromotion(iPromotion, False)
							pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ILLUSION'), True)
							eUnitArtStyle = pEnemyUnit.getUnitArtStyleType()
							if eUnitArtStyle == UnitArtStyleTypes.NO_UNIT_ARTSTYLE:
								eUnitArtStyle = gc.getCivilizationInfo(pEnemyUnit.getHomeCivilizationType()).getUnitArtStyleType()
							pNewUnit.setUnitArtStyleType(eUnitArtStyle)
							iDurationBaseTimes100 = (3 + pPlayer.getSummonDuration() * 2) * 100
							iDurationTimes100 = CyGame().getSorenRandNum(iDurationBaseTimes100, "Mirrored Unit Duration") + CyGame().getSorenRandNum(iDurationBaseTimes100, "Mirrored Unit Duration")
							iDurationTimes100 = (iDurationTimes100 * gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getGoldenAgePercent()) // 100
							pNewUnit.setDuration(max(1, iDurationTimes100 // 100) + 1)

							kHallOfMirror = gc.getBuildingInfo(gc.getInfoTypeForString('BUILDING_HALL_OF_MIRRORS'))
							szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_HALL_OF_MIRROR_GLITTER", (pNewUnit.getName(), kHallOfMirror.getTextKey()))
							CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorGreen, pNewUnit.getX(), pNewUnit.getY(), True, True)
							szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_HALL_OF_MIRROR_GLITTER_ENEMY", (pEnemyUnit.getName(), kHallOfMirror.getTextKey(), pCity.getName()))
							CyInterface().addMessage(pEnemyUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, kHallOfMirror.getButton(), en.eColorRed, pNewUnit.getX(), pNewUnit.getY(), True, True)

##--------	Cold Counter: Added by Denev	--------##
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_HAND')):
				lpRangedPlots = cyGetRangedPlots(pPlot, pCity.getPlotRadius(), False, False, TeamTypes.NO_TEAM)
				for pTargetPlot in lpRangedPlots:
					pWorkingCity = pTargetPlot.getWorkingCity()
					if pWorkingCity.getOwner() == pCity.getOwner() and pWorkingCity.getID() == pCity.getID():
# Kaijin OAC - Crystal Plains ...etc
						cf.doBuildingColdEffects(pTargetPlot)
						pTargetPlot.ceilColdCounter(9600 + CyGame().getSorenRandNum(2400, "Built Temple of the Hand"), 1000)
						"""
						if pTargetPlot.getImprovementType() == en.eImprovementSmoke:
							pTargetPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
						eFeature = pTargetPlot.getFeatureType()
						if eFeature in (en.eFeatureForest, en.eFeatureJungle):
							pTargetPlot.setFeatureType(en.eFeatureForest, 2)
#						elif eFeature in (en.eFeatureFlames, en.eFeatureFloodPlains, en.eFeatureScrub, en.eFeatureObsidianPlains, en.eFeatureOasis):
						elif eFeature in (en.eFeatureFlames, en.eFeatureFloodPlains, en.eFeatureScrub, en.eFeatureObsidianPlains):
							pTargetPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
						"""
# Kaijin OAC - end
##--------	Cold Counter: End Add		--------##

			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_PLANAR_GATE')):
				iPlanarGate = gc.getInfoTypeForString('BUILDING_PLANAR_GATE')
				iCounter = CyGame().getGlobalCounter()
##--------	Unofficial Bug Fix: Modified by Denev	--------##
				"""
				iProbability = gc.getDefineINT('PLANAR_GATE_CHANCE') * (3333 + (iCounter * 100)) / (gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getTrainPercent() * 33)
				if CyGame().getSorenRandNum(10000, "Planar Gate") < iProbability:
				"""
				iProbabilityTimes100 = gc.getDefineINT('PLANAR_GATE_CHANCE') * (100 + iCounter * 3)
				if CyGame().getSorenRandNum(gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getTrainPercent() * 100, "Planar Gate") * 100 < iProbabilityTimes100:
##--------	Unofficial Bug Fix: End Modify			--------##
					liEnteringUnits = []
					iMax = 1 + (iCounter * pPlayer.countNumBuildings(iPlanarGate)) // 33
					if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_GAMBLING_HOUSE')):
						if pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_REVELERS')) < iMax:
							liEnteringUnits.append(gc.getInfoTypeForString('UNIT_REVELERS'))
					if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_MAGE_GUILD')):
						if pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_MOBIUS_WITCH')) < iMax:
							liEnteringUnits.append(gc.getInfoTypeForString('UNIT_MOBIUS_WITCH'))
					if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_CARNIVAL')):
						if pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_CHAOS_MARAUDER')) < iMax:
							liEnteringUnits.append(gc.getInfoTypeForString('UNIT_CHAOS_MARAUDER'))
					if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_GROVE')):
						if pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_MANTICORE')) < iMax:
							liEnteringUnits.append(gc.getInfoTypeForString('UNIT_MANTICORE'))
					if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_PUBLIC_BATHS')):
						if pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_SUCCUBUS')) < iMax:
							liEnteringUnits.append(gc.getInfoTypeForString('UNIT_SUCCUBUS'))
					if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_OBSIDIAN_GATE')):
						if pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_MINOTAUR')) < iMax:
							liEnteringUnits.append(gc.getInfoTypeForString('UNIT_MINOTAUR'))
					if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_VEIL')):
						if pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_TAR_DEMON')) < iMax:
							liEnteringUnits.append(gc.getInfoTypeForString('UNIT_TAR_DEMON'))
					if len(liEnteringUnits) > 0:
						iEnteringUnit = liEnteringUnits[CyGame().getSorenRandNum(len(liEnteringUnits), "Planar Gate")]
						pNewUnit = pPlayer.initUnit(iEnteringUnit, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
						szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_PLANAR_GATE", (pNewUnit.getNameKey(), pCity.getNameKey(), gc.getBuildingInfo(iPlanarGate).getDescription()))
						CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
						if iEnteringUnit == gc.getInfoTypeForString('UNIT_MOBIUS_WITCH'):
							liPromotions = [	gc.getInfoTypeForString('PROMOTION_AIR1'),
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
							pNewUnit.setLevel(4)
							iXP = 10 + CyGame().getSorenRandNum(7, "Mobius Witch Starting XP")
							iModifier = gc.getPlayer(iPlayer).getLevelExperienceModifier()
							if (0 != iModifier):
								iXP *= (100 + iModifier)
								iXP //= 100
							pNewUnit.setExperience(iXP, -1)
							for iPromotion in liPromotions:
								if CyGame().getSorenRandNum(10, "Mobius Witch Starting Promotion") < 1:
									pNewUnit.setHasPromotion(iPromotion, True)
						else:
							iXP = 2 + CyGame().getSorenRandNum(4, "Starting XP")
							iModifier = gc.getPlayer(iPlayer).getLevelExperienceModifier()
							if (0 != iModifier):
								iXP *= (100 + iModifier)
								iXP //= 100
							pNewUnit.setExperience(iXP, -1)

			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_UNYIELDING_ORDER')):
				pCity.setOccupationTimer(0)
				pCity.changeHurryAngerTimer(min(pCity.getHurryAngerTimer(), pCity.flatHurryAngerLength()) * -1)
				pCity.changeConscriptAngerTimer(min(pCity.getConscriptAngerTimer(), pCity.flatConscriptAngerLength()) * -1)

##--------	Advanced Rules: Added by Denev	--------##
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_TOWER_OF_THE_ELEMENTS')):
				if CyGame().getSorenRandNum(100, "Elemental Spawn") < 2:
					lList = ['UNIT_AIR_ELEMENTAL', 'UNIT_EARTH_ELEMENTAL', 'UNIT_FIRE_ELEMENTAL', 'UNIT_WATER_ELEMENTAL']
					eUnit = gc.getInfoTypeForString(lList[CyGame().getSorenRandNum(len(lList), "Pick Elemental")])
					pNewUnit = pPlayer.initUnit(eUnit, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
#Kaijin >>>
					pNewUnit.setHasPromotion(en.ePromotionHeroicStrength, True)
					pNewUnit.setHasPromotion(en.ePromotionHeroicStrength2, True)
					pNewUnit.setHasPromotion(en.ePromotionHeroicDefense, True)
					pNewUnit.setHasPromotion(en.ePromotionHeroicDefense2, True)
					pNewUnit.setHasPromotion(en.ePromotionStrong, True)
					pNewUnit.setHasPromotion(en.ePromotionMusou, True)
#Kaijin <<<
					CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_TOWER_OF_THE_ELEMENTS_SPAWN", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getUnitInfo(eUnit).getButton(), en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
##--------	Advanced Rules: End Add			--------##

			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_EYES_AND_EARS_NETWORK')):
				"""
				liUnstealable = [	gc.getInfoTypeForString('TECH_ARETE'),
									gc.getInfoTypeForString('TECH_HIDDEN_PATHS'),
									gc.getInfoTypeForString('TECH_INFERNAL_PACT'),
									gc.getInfoTypeForString('TECH_MIND_STAPLING'),
									gc.getInfoTypeForString('TECH_SEAFARING')	]
				"""
				leStealable = [	eTech	for eTech in xrange(gc.getNumTechInfos())
										if not gc.getTechInfo(eTech).isDisable()
										and gc.getTechInfo(eTech).getResearchCost() >= 0
										and	gc.getTechInfo(eTech).isTrade()
										and	gc.getTechInfo(eTech).getPrereqReligion() == ReligionTypes.NO_RELIGION	]
				pTeam = gc.getTeam(pPlayer.getTeam())
				lpOpenBordersTeams = [gc.getTeam(eLoopTeam) for eLoopTeam in xrange(gc.getMAX_CIV_TEAMS()) if pTeam.isOpenBorders(eLoopTeam)]
				eEyesAndEarsNetwork = gc.getInfoTypeForString('BUILDING_EYES_AND_EARS_NETWORK')
				iLeakThreshold = gc.getBuildingInfo(eEyesAndEarsNetwork).getTechShare()
				if len(lpOpenBordersTeams) >= iLeakThreshold:
					for eTech in leStealable:
						if not pTeam.isHasTech(eTech):
							iCount = 0
							for pOpenBordersTeam in lpOpenBordersTeams:
								if pOpenBordersTeam.isHasTech(eTech):
									iCount += pOpenBordersTeam.getNumMembers()
							if iCount >= iLeakThreshold:
								pTeam.setHasTech(eTech, True, iPlayer, False, True)
								for iLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
									pLoopPlayer = gc.getPlayer(iLoopPlayer)
									if pLoopPlayer.isAlive() and pLoopPlayer.getTeam() == pPlayer.getTeam():
										szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_EYES_AND_EARS_NETWORK_FREE_TECH", (gc.getTechInfo(eTech).getDescription(), gc.getBuildingInfo(eEyesAndEarsNetwork).getDescription()))
										szButton = gc.getBuildingInfo(eEyesAndEarsNetwork).getButton()
										CyInterface().addMessage(iLoopPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorTech, pCity.getX(), pCity.getY(), True, True)

			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_SHRINE_OF_SIRONA')):
				pPlayer.setFeatAccomplished(FeatTypes.FEAT_HEAL_UNIT_PER_TURN, True)

			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_DRAGONS_HORDE')):
				if pPlayer.isBarbarian():
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#					if CyGame().getSorenRandNum(100, "Bob") <= gc.getHandicapInfo(gc.getGame().getHandicapType()).getLairSpawnRate():
					if CyGame().getSorenRandNum(100, "Bob") < gc.getHandicapInfo(gc.getGame().getHandicapType()).getLairSpawnRate():
##--------	Unofficial Bug Fix: End Modify			--------##
						iUnit = gc.getInfoTypeForString('UNIT_DISCIPLE_OF_ACHERON')
##--------	Advanced Rules: Deleted by Denev	--------##
						"""
						pTeam = gc.getTeam(pPlayer.getTeam())
						if pTeam.isHasTech(gc.getInfoTypeForString('TECH_SORCERY')):
							iUnit = gc.getInfoTypeForString('UNIT_SON_OF_THE_INFERNO')
						"""
##--------	Advanced Rules: End Delete			--------##
# ent: Cancel deletion >>>
						if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_SORCERY')):
							if not pPlayer.isProductionMaxedUnitClass(gc.getInfoTypeForString('UNITCLASS_ARCHMAGE')):
								iUnit = gc.getInfoTypeForString('UNIT_SON_OF_THE_INFERNO')
# ent: Cancel deletion <<<
						pNewUnit = pPlayer.initUnit(iUnit, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
##--------	Unofficial Bug Fix: End Add			--------##

# Kaijin >>>
	# Cities
	## LoopCities - National Building
		## Transition
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_TRANSITION')):
				infoCiv = gc.getCivilizationInfo(pCity.getCivilizationType())
				iNumManaDimensional = pPlayer.getNumAvailableBonuses(gc.getInfoTypeForString('BONUS_MANA_DIMENSIONAL'))
				iProbability = gc.getDefineINT('PLANAR_GATE_CHANCE') * (10 + iNumManaDimensional)
				if CyGame().getSorenRandNum(gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getTrainPercent() * 100, "Transition Chance") < iProbability:
					pTeam = gc.getTeam(pPlayer.getTeam())
					listUnits = []
					eTraining = infoCiv.getCivilizationBuildings(gc.getInfoTypeForString('BUILDINGCLASS_TRAINING_YARD'))
					eStable = infoCiv.getCivilizationBuildings(gc.getInfoTypeForString('BUILDINGCLASS_STABLE'))
					eHarbor = infoCiv.getCivilizationBuildings(gc.getInfoTypeForString('BUILDINGCLASS_HARBOR'))
					iMax = pPlayer.countNumBuildings(gc.getInfoTypeForString('BUILDING_TRANSITION')) + iNumManaDimensional

					if eTraining != BuildingTypes.NO_BUILDING:
						if pCity.isHasActiveBuilding(eTraining):
							if pTeam.isHasTech(gc.getInfoTypeForString('TECH_SMELTING')):
								if pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_TRANSITION_HOPLITE')) < iMax:
									listUnits.append(gc.getInfoTypeForString('UNIT_TRANSITION_HOPLITE'))
							if pTeam.isHasTech(gc.getInfoTypeForString('TECH_MITHRIL_WORKING')):
								if pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_TRANSITION_PRAETORIAN')) < iMax:
									if not pPlayer.isProductionMaxedUnitClass(gc.getInfoTypeForString('UNITCLASS_TRANSITION_PRAETORIAN')):
										listUnits.append(gc.getInfoTypeForString('UNIT_TRANSITION_PRAETORIAN'))
							if pTeam.isHasTech(gc.getInfoTypeForString('TECH_GUILDS')):
								if pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_TRANSITION_LANDSKNECHT')) < iMax:
									listUnits.append(gc.getInfoTypeForString('UNIT_TRANSITION_LANDSKNECHT'))
# ent >>>
						"""
						if pTeam.isHasTech(gc.getInfoTypeForString('TECH_DIVINE_ESSENCE')):
							if pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_DIAMOND_KNIGHT')) < iMax:
								if not pPlayer.isProductionMaxedUnitClass(gc.getInfoTypeForString('UNITCLASS_DIAMOND_KNIGHT')):
									listUnits.append(gc.getInfoTypeForString('UNIT_DIAMOND_KNIGHT'))
						"""
# ent <<<
					if eStable != BuildingTypes.NO_BUILDING:
						if pCity.isHasActiveBuilding(eStable):
							if pTeam.isHasTech(gc.getInfoTypeForString('TECH_STIRRUPS')):
								if pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_TRANSITION_LIGHT_CAVALRY')) < iMax:
									listUnits.append(gc.getInfoTypeForString('UNIT_TRANSITION_LIGHT_CAVALRY'))
							if pTeam.isHasTech(gc.getInfoTypeForString('TECH_WARHORSES')):
								if pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_TRANSITION_CATAPHRACT')) < iMax:
									if not pPlayer.isProductionMaxedUnitClass(gc.getInfoTypeForString('UNITCLASS_TRANSITION_CATAPHRACT')):
										listUnits.append(gc.getInfoTypeForString('UNIT_TRANSITION_CATAPHRACT'))
							if pTeam.isHasTech(gc.getInfoTypeForString('TECH_GUILDS')):
								if pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_TRANSITION_HUSSAR')) < iMax:
									listUnits.append(gc.getInfoTypeForString('UNIT_TRANSITION_HUSSAR'))

					if eHarbor != BuildingTypes.NO_BUILDING:
						if pCity.isHasActiveBuilding(eHarbor):
							if pTeam.isHasTech(gc.getInfoTypeForString('TECH_SAILING')):
								if pPlayer.getUnitClassCount(gc.getInfoTypeForString('UNITCLASS_TRANSITION_SAILOR')) < iMax:
									listUnits.append(gc.getInfoTypeForString('UNIT_TRANSITION_SAILOR'))

					if len(listUnits) > 0:
						iUnit = listUnits[CyGame().getSorenRandNum(len(listUnits), "Transition Unit")]
						newUnit = pPlayer.initUnit(iUnit, pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
						newUnit.setExperience(CyGame().getSorenRandNum(5, "Transition UnitExperience"), -1)
						CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_TRANSITION",()), 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, newUnit.getButton(), ColorTypes(8), pCity.getX(), pCity.getY(), True, True)

	## LoopCities - Unique Building
		## Malakim - Citadel of Light - Tile scorch
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_CITADEL_OF_LIGHT')):
				eEffect = gc.getInfoTypeForString('EFFECT_SCORCH')
				lpRangedPlots = cyGetRangedPlots(pPlot, pCity.getPlotRadius() - 1, False, False, TeamTypes.NO_TEAM)
				for pTargetPlot in lpRangedPlots:
					if not pTargetPlot.isWater():
						pWorkingCity = pTargetPlot.getWorkingCity()
						if pWorkingCity.getOwner() == pCity.getOwner() and pWorkingCity.getID() == pCity.getID():
							bEffect = False
							if pTargetPlot.getTerrainType() != en.eTerrainDesert:
# ent >>>
								"""
								pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
								pTargetPlot.clearColdCounter()
								pTargetPlot.setTerrainType(en.eTerrainDesert, True, True)
								"""
								pTargetPlot.setPlotCounter(0)
								iOldFood = pTargetPlot.getYield(YieldTypes.YIELD_FOOD)
								pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
								pTargetPlot.clearColdCounter()
								pTargetPlot.setTerrainType(en.eTerrainDesert, True, True)
								iNewFood = pTargetPlot.getYield(YieldTypes.YIELD_FOOD)
								iModFood = min(iOldFood - iNewFood, pTargetPlot.getYield(YieldTypes.YIELD_PRODUCTION))
								if not pTargetPlot.isCity() and iModFood > 0:
									if CyGame().isOption(gc.getInfoTypeForString('GAMEOPTION_MODDER_4')):
										if pTargetPlot.isFlatlands() and pTargetPlot.isRiver():
											continue
									CyGame().setPlotExtraYield(pTargetPlot.getX(), pTargetPlot.getY(), YieldTypes.YIELD_FOOD, iModFood)
									CyGame().setPlotExtraYield(pTargetPlot.getX(), pTargetPlot.getY(), YieldTypes.YIELD_PRODUCTION, -1*iModFood)
									sCaptionFood = CyTranslator().getText("TXT_KEY_SIGN_FORMAT_FOOD", (iModFood, )) + u" "
									sCaptionProd = CyTranslator().getText("TXT_KEY_SIGN_FORMAT_PROD", (-1*iModFood, )) + u" "
									sCaptionComm = ""
									sCaptionDesc = CyTranslator().getText("TXT_KEY_SIGN_CITADEL_OF_LIGHT", ())

									sCaption = CyTranslator().getText("TXT_KEY_SIGN_FORMAT_OVERVIEW", (sCaptionFood, sCaptionProd, sCaptionComm, sCaptionDesc))

									for eLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
										pLoopPlayer = gc.getPlayer(eLoopPlayer)
										if pLoopPlayer.isAlive() and pLoopPlayer.isHuman():
											CyEngine().addSign(pTargetPlot, eLoopPlayer, sCaption)
# ent <<<
								bEffect = True
							eFeature = pTargetPlot.getFeatureType()
							if eFeature in (en.eFeatureForest, en.eFeatureJungle, en.eFeatureForestAncient, en.eFeatureDeepJungle):
								pTargetPlot.setFeatureType(en.eFeatureScrub, -1)
								bEffect = True
							if bEffect and pTargetPlot.isVisibleToWatchingHuman():
								CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())

		## Tokoyami - Altar of flame - Tile corrosion
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_DARK_TEMPLE')) and not CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_PLOT_COUNTER):
				lpRangedPlots = cyGetRangedPlots(pPlot, pCity.getPlotRadius(), False, False, TeamTypes.NO_TEAM)
				for pTargetPlot in lpRangedPlots:
					pWorkingCity = pTargetPlot.getWorkingCity()
					if pWorkingCity.getOwner() == pCity.getOwner() and pWorkingCity.getID() == pCity.getID():
#						iFeature = pTargetPlot.getFeatureType()
#						iBonus = pTargetPlot.getBonusType(TeamTypes.NO_TEAM)
						pTargetPlot.setPlotCounter(100)
#						if iBonus != BonusTypes.NO_BONUS:
#							if gc.getImprovementInfo(en.eImprovementFarm).isImprovementBonusTrade(iBonus):
#								pTargetPlot.setImprovementType(en.eImprovementSnakePillar)
#						if iFeature == en.eFeatureFloodPlains:
#							pTargetPlot.setFeatureType(en.eFeatureObsidianPlains, -1)
						if pPlot.isVisibleToWatchingHuman():
							CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SCORCH'), pPlot.getPoint())

		## Tiger - Termination of economic agreements.
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_ECONOMIC_AGREEMENT')):
				if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_TIGER'):
					if pCity.isCapital():
						if not bool(pPlayer.getGuildPlusCounter(50)):
							pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_ECONOMIC_AGREEMENT'), 0)
				else:
					pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_ECONOMIC_AGREEMENT'), 0)

		## Nival - Palace - Tile cooling
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_PALACE_NIVAL')):
				lpRangedPlots = cyGetRangedPlots(pPlot, pCity.getPlotRadius(), False, False, TeamTypes.NO_TEAM)
				for pTargetPlot in lpRangedPlots:
					pWorkingCity = pTargetPlot.getWorkingCity()
					if pWorkingCity.getOwner() == pCity.getOwner() and pWorkingCity.getID() == pCity.getID():
						cf.doBuildingColdEffects(pTargetPlot)
						pTargetPlot.ceilColdCounter(9600 + CyGame().getSorenRandNum(2400, "Built Temple of the Hand"), 1000)

		## Baldralfer - Altar of rebirth - Tile Fertilization
			"""
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_BALDRALFAR_TEMPLE')):
				liDesertFeatures = [en.eFeatureFloodPlains, en.eFeatureOasis]
				iBurntForest = gc.getDefineINT('FLAMES_EXPIRE_EFFECT')
				iNewForest = gc.getInfoTypeForString('FEATURE_FOREST_NEW')
				lpRangedPlots = cyGetRangedPlots(pPlot, pCity.getPlotRadius(), False, False, TeamTypes.NO_TEAM)
				for pTargetPlot in lpRangedPlots:
					pWorkingCity = pTargetPlot.getWorkingCity()
					if pWorkingCity.getOwner() == pCity.getOwner() and pWorkingCity.getID() == pCity.getID():
						if not pTargetPlot.isWater():
							pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
							pTargetPlot.setPlotCounter(0)
#							pTargetPlot.clearColdCounter()
							iFeature = pTargetPlot.getFeatureType()
							if pTargetPlot.getTerrainType() == en.eTerrainSnow:
								pTargetPlot.setTerrainType(en.eTerrainTundra, False, True)
							elif pTargetPlot.getTerrainType() == en.eTerrainTundra:
								pTargetPlot.setTerrainType(en.eTerrainPlains, False, True)
							elif pTargetPlot.getTerrainType() == en.eTerrainDesert:
								if iFeature not in liDesertFeatures:
									pTargetPlot.setTerrainType(en.eTerrainPlains, False, True)
							elif pTargetPlot.getTerrainType() == en.eTerrainPlains:
								pTargetPlot.setTerrainType(en.eTerrainGrass, False, True)
							elif pTargetPlot.getTerrainType() == en.eTerrainGrass:
								if iFeature == FeatureTypes.NO_FEATURE:
									if pTargetPlot.canHaveFeatureOnImprovement(iNewForest):
										pTargetPlot.setFeatureType(iNewForest, 0)
							elif pTargetPlot.getTerrainType() == en.eTerrainMarsh:
								pTargetPlot.setTerrainType(en.eTerrainGrass, False, True)
							if iFeature == en.eFeatureJungle:
								pTargetPlot.setFeatureType(en.eFeatureForest, 0)
							elif iFeature == en.eFeatureFlames:
								pTargetPlot.setFeatureType(iBurntForest, 0)
							elif iFeature == en.eFeatureSwamp:
								pTargetPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
							elif iFeature == en.eFeatureBlizzard:
								pTargetPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
							elif iFeature != FeatureTypes.NO_FEATURE:
								iUpgrade = gc.getFeatureInfo(iFeature).getFeatureUpgrade()
								if iUpgrade != FeatureTypes.NO_FEATURE:
									iStateReligion = gc.getFeatureInfo(iUpgrade).getPrereqStateReligion()
									if iStateReligion in (ReligionTypes.NO_RELIGION, gc.getPlayer(iPlayer).getStateReligion()):
										pTargetPlot.setFeatureType(iUpgrade, 0)
							if pTargetPlot.getImprovementType() == gc.getDefineINT('FLAMES_SPREAD_EFFECT'):
								pTargetPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
			"""
	## LoopCities - Traits
		## GreatPeople - Building GreatPeople
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_GREAT_PEOPLE')):
				iAngry = pCity.angryPopulation(0)

				if iAngry > 0 and not pCity.isDisorder():
					# Reserach Addition
					iResearchTech = pPlayer.getCurrentResearch()
					if iResearchTech != TechTypes.NO_TECH:
						iResearchPoint = max(1, iAngry * pPlayer.calculateResearchModifier(iResearchTech) // 100)
						pTeam = gc.getTeam(pPlayer.getTeam())
						pTeam.changeResearchProgress(iResearchTech, iResearchPoint, iPlayer)

					# Culture Addition
					iCulture = iAngry * 5
					iCulture *= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(CyGame().getGameSpeedType())
					iCulture /= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(gc.getInfoTypeForString('GAMESPEED_NORMAL'))
					pCity.changeCulture(iPlayer, iCulture, True)

		## Organized - The reduced to one turn remaining rebellion period.
			if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_ORGANIZED')):
				if pCity.getOccupationTimer() > 0:
					pCity.changeOccupationTimer( pCity.getOccupationTimer() * -1 )

		## Aggressive - Removal of branch of Trait-Aggressive than.
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_AGGRESSIVE')) and not pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGGRESSIVE')):
				pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_AGGRESSIVE'), 0)

		## Creative - Removal of explosive creativity of Trait-Creative than.
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_CREATIVE')) and not pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_CREATIVE')):
				pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_CREATIVE'), 0)

		## Summoner - Removal of portal of Trait-Summoner than.
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_SUMMONER')) and not pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_SUMMONER')):
				pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_SUMMONER'), 0)

		## Agricultural - Removal of agricultural of Trait-Agricultural than.
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_AGRICULTURAL')) and not pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGRICULTURAL')):
				pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_AGRICULTURAL'), 0)

		## Construction - Removal of construction of Trait-Construction than.
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_CONSTRUCTION')) and not pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_CONSTRUCTION')):
				pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_CONSTRUCTION'), 0)

		## Martyrdom - Removal of Martyrdom of Trait-Martyrdom than.
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_MARTYRDOM')) and not pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_MARTYRDOM')):
				pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_MARTYRDOM'), 0)

		## Imperialist - Removal of imperialist of Trait-Imperialist than.
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_IMPERIALIST')):
				if not pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_IMPERIALIST')) or not pCity.isCapital():
					pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_IMPERIALIST'), 0)

		## Riche - Removal of  of Trait-Riche than.
			if not pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_RICHES')):
				if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_EMPTY')):
					pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_RICHS_EMPTY'), 0)
				elif pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_NONE')):
					pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_RICHS_NONE'), 0)
				elif pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_SMALL')):
					pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_RICHS_SMALL'), 0)
				elif pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_SAVED')):
					pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_RICHS_SAVED'), 0)
				elif pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED')):
					pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED'), 0)
				elif pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED_1')):
					pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED_1'), 0)
				elif pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED_2')):
					pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_RICHS_STUCKED_2'), 0)

		## GreatPeople - Removal of great people of Trait-GreatPeople than.
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_GREAT_PEOPLE')) and not pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_GREAT_PEOPLE')):
				pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_GREAT_PEOPLE'), 0)

		## CrazyByWorldheritage - Removal of crazy by worldheritage of Trait-CrazyByWorldheritage than.
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_CRAZY_BY_WORLDHERITAGE')) and not pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_CRAZY_BY_WORLDHERITAGE')):
				pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_CRAZY_BY_WORLDHERITAGE'), 0)

	## LoopCities - Religion
		## Cult of the Dragon - Betrayal of the believer.
			eReligionCult = gc.getInfoTypeForString('RELIGION_CULT_OF_THE_DRAGON')
			if pCity.isHolyCityByType(eReligionCult):
				for i in xrange (CyMap().numPlots()):
					pLoopPlot = CyMap().plotByIndex(i)
					if pLoopPlot.isOwned():
						if pLoopPlot.getOwner() == iPlayer:
							for i in xrange(pLoopPlot.getNumUnits() -1, -1, -1):
								pLoopUnit = pLoopPlot.getUnit(i)
								if pLoopUnit.getOwner() != iPlayer and pLoopUnit.getReligion() == eReligionCult and CyGame().getSorenRandNum(100, "Betray Chance") < 3:
									pTargetPlot = cf.findAdjacentClearPlot(iPlayer, pLoopPlot.getX(), pLoopPlot.getY(), False, False)
									if pTargetPlot is None or pLoopUnit.isImmuneToCapture():
										pLoopUnit.kill(True, 0)
										szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_ROAR_SELF_KILL', (pLoopUnit.getNameKey(), ))
										szMessageEnemy = CyTranslator().getText('TXT_KEY_MESSAGE_ROAR_SELF_KILL_ENEMY', (gc.getPlayer(pLoopUnit.getOwner()).getCivilizationAdjectiveKey(), pLoopUnit.getNameKey()))
									else:
										pNewUnit = pPlayer.initUnit(pLoopUnit.getUnitType(), pTargetPlot.getX(), pTargetPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
										pNewUnit.convert(pLoopUnit)
										szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_BETRAY_CULT_OF_THE_DRAGON', (pLoopUnit.getNameKey(), pPlayer.getCivilizationAdjectiveKey()))
										szMessageEnemy = CyTranslator().getText('TXT_KEY_MESSAGE_BETRAY_CULT_OF_THE_DRAGON_ENEMY', (gc.getPlayer(pLoopUnit.getOwner()).getCivilizationAdjectiveKey(), pLoopUnit.getNameKey()))
									CyInterface().addMessage(pLoopUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art_Kaijin/Interface/Buttons/Religions/cultofthedragon.dds', en.eColorRed, pLoopUnit.getX(), pLoopUnit.getY(), True, True)
									CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessageEnemy, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art_Kaijin/Interface/Buttons/Religions/cultofthedragon.dds', en.eColorGreen, pLoopPlot.getX(), pLoopPlot.getY(), True, True)

		## Cult of the Dragon - Culture addition
			if pCity.isHasReligion(eReligionCult) and not pCity.isDisorder():
				if pPlayer.getCivilizationType() in (gc.getInfoTypeForString('CIVILIZATION_KURIOTATES'), 
														gc.getInfoTypeForString('CIVILIZATION_SHEAIM'), 
														gc.getInfoTypeForString('CIVILIZATION_ILLIANS'), 
														gc.getInfoTypeForString('CIVILIZATION_MAZATL'), 
														gc.getInfoTypeForString('CIVILIZATION_ALTAIR')		):
					iCulture = 1
					iCulture *= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(CyGame().getGameSpeedType())
					iCulture /= gc.getCultureLevelInfo(gc.getNumCultureLevelInfos() - 1).getSpeedThreshold(gc.getInfoTypeForString('GAMESPEED_NORMAL'))
					pCity.changeCulture(iPlayer, iCulture, True)

	# Units
	## Loop - Unit
		for pUnit in PyPlayer(iPlayer).getUnitList():

		# Kaijin >>> Moved from CvEventManager.py "EndPlayerTurn"

		## Summon KOD
			if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_DIAMOND_DRAKE'):
				if pUnit.canCast(gc.getInfoTypeForString('SPELL_SUMMON_KOD'), 0):
					pUnit.cast(gc.getInfoTypeForString('SPELL_SUMMON_KOD'))

		## Figure of the witch
			elif pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_FIGURE'):
				if pUnit.isAlive():
					if not pUnit.isSummoned():
						if (	( pPlayer.getGuildPlusCounter(50) == 1 and pUnit.getExperience() >= 100 )
								or ( pPlayer.getGuildPlusCounter(50) == 2 and pUnit.getExperience() >= 90 )
								or ( pPlayer.getGuildPlusCounter(50) == 3 and pUnit.getExperience() >= 80 )
								or ( pPlayer.getGuildPlusCounter(50) == 4 and pUnit.getExperience() >= 60 )
								or ( pPlayer.getGuildPlusCounter(50) >= 5 and pUnit.getExperience() >= 40 )	):
							pUnit.setDuration(-1)

		## CrownofBrillance
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CROWN_OF_BRILLANCE')):
				pUnit.cast(gc.getInfoTypeForString('SPELL_CROWN_OF_BRILLANCE_PER_TURN'))

		## Kod's Items
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_KODS_ITEMS')):
				pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_REGENERATION'), True)
				pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STONESKIN'), True)
				pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENCHANTED_BLADE'), True)
				pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_COURAGE'), True)
				pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LOYALTY'), True)
				if CyGame().getSorenRandNum(100, "Tiltowaito") < 20:
					lpRangedUnits = cyGetSpellRangedUnits(pUnit, gc.getInfoTypeForString('SPELL_TILTOWAITO'), pUnit.plot(), False, True)
					eTeam = pUnit.getTeam()
					for pLoopUnit in lpRangedUnits:
						if pLoopUnit.isEnemy(eTeam, pLoopUnit.plot()):
							pUnit.cast(gc.getInfoTypeForString('SPELL_TILTOWAITO'))
							break

		## Trait - Intensified
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFICATION')):
				eTeam = pUnit.getTeam()
				lpRangedUnits = cyGetRangedUnits(pUnit.plot(), 1, False, True, eTeam)
				for pLoopUnit in lpRangedUnits:
					if not pLoopUnit.isEnemy(eTeam, pLoopUnit.plot()):
						if not pLoopUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_1')):
							pLoopUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_1'), True)

			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_1')):
				eTeam = pUnit.getTeam()
				iIntensify = 0
				lpRangedUnits = cyGetRangedUnits(pUnit.plot(), 1, False, True, eTeam)
				for pLoopUnit in lpRangedUnits:
					if not pLoopUnit.isEnemy(eTeam, pLoopUnit.plot()):
						if pLoopUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFICATION')) and iIntensify <=5:
							iIntensify += 1

				if iIntensify >= 5:
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_5'), True)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_4'), True)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_3'), True)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_2'), True)
				elif iIntensify == 4:
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_5'), False)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_4'), True)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_3'), True)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_2'), True)
				elif iIntensify == 3:
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_5'), False)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_4'), False)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_3'), True)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_2'), True)
				elif iIntensify == 2:
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_5'), False)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_4'), False)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_3'), False)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_2'), True)
				elif iIntensify == 1:
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_5'), False)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_4'), False)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_3'), False)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_2'), False)
				elif iIntensify == 0:
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_5'), False)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_4'), False)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_3'), False)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_2'), False)
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INTENSIFIED_1'), False)

		## Sealed
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SEALED')):
				if pUnit.getUncastableTimer() <= 1:
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_SEALED'), False)

		## Echigo - Formation of the Kurumagakari
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_KURUMA_ECHIGO')):
				eTeam = pUnit.getTeam()
				lpRangedUnits = cyGetRangedUnits(pUnit.plot(), 4, False, True, eTeam)
				for pLoopUnit in lpRangedUnits:
					if not pLoopUnit.isEnemy(eTeam, pLoopUnit.plot()):
						if pLoopUnit.getUnitType() == gc.getInfoTypeForString('UNIT_NAOE'):
							break
				else:
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_KURUMA_ECHIGO'), False)

		## Ys - Hoodoo Ash
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_HOODOO')):
				pPlot = pUnit.plot()
				if not pPlot.isNone():
					for iLoopUnit in xrange(pPlot.getNumUnits()):
						pLoopUnit = pPlot.getUnit(iLoopUnit)
						pLoopUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAKEN'), True)
						pLoopUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LOW_VITALITY'), True)

		## Lineage - Commander Gozewaros
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMMANDER')):
				eTeam = pUnit.getTeam()
				lpRangedUnits = cyGetRangedUnits(pUnit.plot(), 3, False, True, eTeam)
				for pLoopUnit in lpRangedUnits:
					if not pLoopUnit.isEnemy(eTeam, pLoopUnit.plot()):
						if not pLoopUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMMANDER')):
							pLoopUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MILITARY_LEADERSHIP'), True)

		## Lineage - Military Leadership
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MILITARY_LEADERSHIP')):
				eTeam = pUnit.getTeam()
				lpRangedUnits = cyGetRangedUnits(pUnit.plot(), 3, False, True, eTeam)
				for pLoopUnit in lpRangedUnits:
					if not pLoopUnit.isEnemy(eTeam, pLoopUnit.plot()):
						if pLoopUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMMANDER')):
							break
				else:
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MILITARY_LEADERSHIP'), False)

		## Scions - Burrs
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BURRS')):
				pPlot = pUnit.plot()
				if CyGame().getSorenRandNum(100, "BurrsHatching") < 30:
					szButton = gc.getPromotionInfo(gc.getInfoTypeForString('PROMOTION_BURRS')).getButton()
				#	if (pUnit.getLevel() >= 6 or pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_HERO'))):
					if pUnit.getDamage() < 80:
						CyInterface().addMessage(pUnit.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_BURRS_SURVIVED", ()),'',1,szButton,ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)
						pUnit.changeDamage(20, PlayerTypes.NO_PLAYER)
					else:
						CyInterface().addMessage(pUnit.getOwner(),True,25,CyTranslator().getText("TXT_KEY_MESSAGE_BURRS_DESTROYED", ()),'',1,szButton,ColorTypes(7),pPlot.getX(),pPlot.getY(),True,True)
						pUnit.kill(True, PlayerTypes.NO_PLAYER)
						if not pPlot.isCity():
							eBarbarianAnimal = gc.getBARBARIAN_PLAYER() + gc.getInfoTypeForString('BARBARIAN_ANIMAL')
							pBarbarianAnimal = gc.getPlayer(eBarbarianAnimal)
							pTargetPlot = cf.findAdjacentClearPlot(eBarbarianAnimal, pPlot.getX(), pPlot.getY(), False, False)
							if pTargetPlot is not None:
								pNewUnit = pBarbarianAnimal.initUnit(gc.getInfoTypeForString('UNIT_CREEPER'), pTargetPlot.getX(), pTargetPlot.getY(), UnitAITypes.UNITAI_ANIMAL, DirectionTypes.DIRECTION_SOUTH)
								pNewUnit.changeExperience(pUnit.getExperience() / 2, -1, False, False, False)

		## Nival - Croak of the snowstorm
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SNOWSTORM_AVATAR')):
				lpRangedPlots = cyGetRangedPlots(pUnit.plot(), 1, False, False, TeamTypes.NO_TEAM)
				for pTargetPlot in lpRangedPlots:
					if pTargetPlot.isFlatlands():
						if (pTargetPlot.getTerrainType() in (en.eTerrainSnow, en.eTerrainTundra)) and pTargetPlot.getFeatureType() == FeatureTypes.NO_FEATURE:
							if CyGame().getSorenRandNum(100, "Blizzard") < 33:
								pTargetPlot.setFeatureType(en.eFeatureBlizzard, 0)

		## Rarna - Soul hunger
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SOUL_HUNGER')):
				if pUnit.getExperience() > 0:
					if pUnit.getUnitType() != gc.getInfoTypeForString('UNIT_SOUL_HUNTER'):
						iExperienceChance = cyFlatValue(10, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
						if CyGame().getSorenRandNum(100, "Unit loses Experience Percent") < iExperienceChance:
							szButton = gc.getPromotionInfo(gc.getInfoTypeForString('PROMOTION_SOUL_HUNGER')).getButton()
							szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_SOUL_HUNGER_LOSE_EXPERIENCE', (pUnit.getNameKey(), ))
							CyInterface().addMessage(pUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pUnit.getX(), pUnit.getY(), True, True)
							pUnit.changeExperience(-1, -1, False, False, False)

		## Tiger - Mercenaries commander
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MERCENARIES_COMMANDER')):
				eTeam = pUnit.getTeam()
				pPlot = pUnit.plot()
				if not pPlot.isNone():
					for iLoopUnit in xrange(pPlot.getNumUnits()):
						pLoopUnit = pPlot.getUnit(iLoopUnit)
						if not pLoopUnit.isEnemy(eTeam, pPlot):
							pLoopUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MORALE'), True)

		## Tiger - Yell
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL1')):
				if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL5')) and CyGame().getSorenRandNum(100, "Yell") < 50:
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL5'), False)
				elif pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL4')) and CyGame().getSorenRandNum(100, "Yell") < 40:
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL4'), False)
				elif pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL3')) and CyGame().getSorenRandNum(100, "Yell") < 30:
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL3'), False)
				elif pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL2')) and CyGame().getSorenRandNum(100, "Yell") < 20:
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL2'), False)
				elif pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL1')) and CyGame().getSorenRandNum(100, "Yell") < 10:
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_YELL1'), False)

		## Baldralfer - Variant
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_VARIANT')):
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
						if not pUnit.isHasPromotion(iPromotion):
							liChosenPromotion.append(iPromotion)
					liChosenPromotion.sort()

					if len(liChosenPromotion) > 0:
						liSelectedPromotion = []
						for iLoop in xrange(iCount):
							liSelectedPromotion.append(liChosenPromotion.pop( CyGame().getSorenRandNum(len(liChosenPromotion), "Variant") ))
						liSelectedPromotion.sort()
						for iSelectedPromotion in liSelectedPromotion:
							if not pUnit.isHasPromotion(iSelectedPromotion):
								pUnit.setHasPromotion(iSelectedPromotion, True)
								szButton = gc.getPromotionInfo(iSelectedPromotion).getButton()
								CyInterface().addMessage(pUnit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_EFFECT_VARIANT", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pUnit.getX(), pUnit.getY(), True, True)

		## Nougbii - Muppet
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MUPPET')):
				pUnit.setExperience(0, -1)

	## Another
		## Traits - Speech
		iTeam = pPlayer.getTeam()
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_SPEECH')):
			## If a player have won Trait-Speech, It turns "on" the switch.
			if pPlayer.getGuildPlusCounter(3) == 0:
				pPlayer.setGuildPlusCounter(3, 1)
				## The upward revision diplomatic attitude.
				for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
					pLoopPlayer = gc.getPlayer(iLoopPlayer)
					if pLoopPlayer.isAlive():
						if not pLoopPlayer.isBarbarian():
							eLoopTeam = pLoopPlayer.getTeam()
							if eLoopTeam != iTeam:
								pLoopTeam = gc.getTeam(eLoopTeam)
								if pLoopTeam.isHasMet(iTeam):
									pLoopPlayer.AI_changeAttitudeExtra(iPlayer, 6)

		elif not pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_SPEECH')):
			## If a player have lost Trait-Speech,  It turns "off" the switch.
			if pPlayer.getGuildPlusCounter(3) == 1:
				pPlayer.setGuildPlusCounter(3, 0)
				## The downward revision diplomatic attitude.
				for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
					pLoopPlayer = gc.getPlayer(iLoopPlayer)
					if pLoopPlayer.isAlive():
						if not pLoopPlayer.isBarbarian():
							eLoopTeam = pLoopPlayer.getTeam()
							if eLoopTeam != iTeam:
								pLoopTeam = gc.getTeam(eLoopTeam)
								if pLoopTeam.isHasMet(iTeam):
									pLoopPlayer.AI_changeAttitudeExtra(iPlayer, -6)

		## Traits - Precocious - The losing Trait-Precocious, given Trait-Precocious Nerf.
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_PRECOCIOUS')):
			if pPlayer.getGameProgressPercent() >= 30:

				pPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_PRECOCIOUS'), False, TraitSourceTypes.NO_TRAITSOURCE)
				pPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_PRECOCIOUS_NERF'), True, TraitSourceTypes.TRAITSOURCE_OTHER_PERMANENT)

				popupInfo = CyPopupInfo()
				popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
				popupInfo.setText(CyTranslator().getText('TXT_KEY_EVENTTRIGGER_TRAIT_PRECOCIOUS',()))
				popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_EVENT_TRAIT_PRECOCIOUS",()), gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getButton())
				popupInfo.addPopup(iPlayer)

		## Traits - CrazyByWorldheritage - Heritage insanity is unscrupulous.
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_CRAZY_BY_WORLDHERITAGE')):
			CRAZY_OFFSET = 5
			for i in xrange(gc.getMAX_CIV_TEAMS()):
				iCounter = CRAZY_OFFSET + i
				if pPlayer.getGuildPlusCounter(iCounter) > 0:
					pPlayer.changeGuildPlusCounter(iCounter, -1)
					if not gc.getTeam(i).isAlive():
						pPlayer.setGuildPlusCounter(iCounter, 0)
					if pPlayer.getGuildPlusCounter(iCounter) == 0:
						pTeam = gc.getTeam(pPlayer.getTeam())
						pTeam.setPermanentWarPeace(i, False)

		## More events mod begins
		"""
		if pPlayer.getGuildPlusCounter(1) == 4:
			if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MERCURIANS'):
				for i in xrange(pPlot.getNumUnits()):
					pUnit = pPlot.getUnit(i)
					if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_GELA')):
						pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_GELA'), False)
						pMercuriansPlayer = gc.getPlayer(pUnit.getOwner())
						if not pPlot.isVisibleEnemyUnit(iPlayer):
							newUnit = pMercuriansPlayer.initUnit(gc.getInfoTypeForString('UNIT_ANGEL'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
							newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HERO'), True) 
							CyInterface().addMessage(pUnit.getOwner(), True, 25, CyTranslator().getText("TXT_KEY_MESSAGE_BASIUM_GELA", ()), '', 1, 'Art/Interface/Buttons/Units/Basium.dds', ColorTypes(7), pUnit.getX(), pUnit.getY(), True, True)
					CyGame().changeGlobalCounter(-10)
		"""
		## More events mod ends
# Kaijin <<<

		if (gc.getGame().getElapsedGameTurns() == 1):
			if (gc.getPlayer(iPlayer).isHuman()):
				if (gc.getPlayer(iPlayer).canRevolution(0)):
					popupInfo = CyPopupInfo()
					popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_CHANGECIVIC)
					popupInfo.addPopup(iPlayer)

		CvAdvisorUtils.resetAdvisorNags()
		CvAdvisorUtils.endTurnFeats(iPlayer)

	def onEndTurnReady(self, argsList):
		iGameTurn = argsList[0]

	def onFirstContact(self, argsList):
		'Contact'
		iTeamX, iHasMetTeamY = argsList
# mod ent >>>
		# Trait Speech
		for iLoopPlayerX in xrange(gc.getMAX_CIV_PLAYERS()):
			pLoopPlayerX = gc.getPlayer(iLoopPlayerX)
			if pLoopPlayerX.isAlive():
#				if pLoopPlayerX.hasTrait(gc.getInfoTypeForString('TRAIT_SPEECH')):
				if pLoopPlayerX.getGuildPlusCounter(3) == 1:
					iLoopTeamX = pLoopPlayerX.getTeam()
					if iLoopTeamX == iTeamX:
						for iLoopHasMetPlayerY in xrange(gc.getMAX_CIV_PLAYERS()):
							pLoopHasMetPlayerY = gc.getPlayer(iLoopHasMetPlayerY)
							if pLoopHasMetPlayerY.isAlive():
								iLoopHasMetTeamY = pLoopHasMetPlayerY.getTeam()
								if iLoopHasMetTeamY == iHasMetTeamY:
									pLoopHasMetPlayerY.AI_changeAttitudeExtra(iLoopPlayerX, 6)
# mod <<<
		if (not self.__LOG_CONTACT):
			return
		CvUtil.pyPrint('Team %d has met Team %d' %(iTeamX, iHasMetTeamY))

	def onCombatResult(self, argsList):
		'Combat Result'
##--------	Advanced Rules: Modified by Denev	--------##
#		pWinner, pLoser = argsList
		pWinner, pLoser, bAttackerWon = argsList

		eWinnerPlayer = pWinner.getOwner()
		pWinnerPlayer = gc.getPlayer(eWinnerPlayer)

		eLoserPlayer = pLoser.getOwner()
		pLoserPlayer = gc.getPlayer(eLoserPlayer)
##--------	Advanced Rules: End Modify			--------##
		playerX = PyPlayer(pWinner.getOwner())
		unitX = PyInfo.UnitInfo(pWinner.getUnitType())
		playerY = PyPlayer(pLoser.getOwner())
		unitY = PyInfo.UnitInfo(pLoser.getUnitType())
##--------	Advanced Rules: Added by Denev	--------##
		if pWinnerPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_DEFENDER')):
			if not bAttackerWon:
				"""
				pAttackingPlot = pWinner.plot()
			else:
				pAttackingPlot = pLoser.plot()
			if pAttackingPlot.getOwner() == pAttackingPlot.getOwner():
				"""
				if gc.getUnitInfo(pLoser.getUnitType()).getXPValueAttack() > 0:
					if not pLoser.isSummoned():
						pWinner.changeExperience(1, -1, True, False, False)

		if pWinnerPlayer.getCivilizationType() == en.eCivilizationDoviello:
			eLoserWeapon = pLoser.getWeapon()
			if eLoserWeapon != WeaponTypes.NO_WEAPON:
				iLoserWeaponTier = gc.getWeaponInfo(eLoserWeapon).getWeaponTier()

				eWinnerWeapon = pWinner.getWeapon()
				if eWinnerWeapon != WeaponTypes.NO_WEAPON:
					iWinnerWeaponTier = gc.getWeaponInfo(eWinnerWeapon).getWeaponTier()
				else:
					iWinnerWeaponTier = -1

				if iWinnerWeaponTier < iLoserWeaponTier <= gc.getUnitInfo(pWinner.getUnitType()).getWeaponTier():
					eWeaponPromotion = gc.getWeaponInfo(eLoserWeapon).getWeaponPromotion()
					pWinner.setHasPromotion(eWeaponPromotion, True)
					pLoser.setHasPromotion(eWeaponPromotion, False)

					szButton = gc.getPromotionInfo(eWeaponPromotion).getButton()
					szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_WEAPON_ROBBED", (pWinner.getName(), pLoser.getName(), gc.getPromotionInfo(eWeaponPromotion).getTextKey(), ))
					CyInterface().addMessage(eWinnerPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_REPAIR', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pLoser.getX(), pLoser.getY(), True, True)
					szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_WEAPON_WAS_ROBBED", (pWinner.getName(), pLoser.getName(), gc.getPromotionInfo(eWeaponPromotion).getTextKey(), ))
					CyInterface().addMessage(eLoserPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pLoser.getX(), pLoser.getY(), True, True)
##--------	Advanced Rules: End Add			--------##

#Kaijin >>>


	## Muppet - Initialization of Experience Points
		if pWinner.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MUPPET')):
			pWinner.setExperience(0, -1)

	## Trait Fool
		if pWinnerPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_UNENLIGHTENED')):
			if CyGame().getSorenRandNum(1000, "Fool") <= 2:
				cf.doTraitFool(eWinnerPlayer)

	## Trait Redeeming
		if pWinnerPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_REDEEMING')) and pWinnerPlayer.getNumCities() > 0:
			if not pWinnerPlayer.isGoldenAge():
				if pLoserPlayer.getAlignment() == gc.getInfoTypeForString('ALIGNMENT_EVIL') or pLoserPlayer.isBarbarian():
					if gc.getGame().getSorenRandNum(100, "Golden Age Percent") < 3:
						pWinnerPlayer.changeGoldenAgeTurns(CyGame().goldenAgeLength() // 2)

						szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_BEGINNING_THE_GOLDENAGE_REDEEMING", ())
						szButton = gc.getTraitInfo(gc.getInfoTypeForString('TRAIT_REDEEMING')).getButton()
						pWinnerCapitalCity = pWinnerPlayer.getCapitalCity()
						CyGame().pushGameMessage(eWinnerPlayer, True, szMessage, '', szButton, en.eColorGreen, pWinnerCapitalCity.getX(), pWinnerCapitalCity.getY(), True, True)

	## Trait Pillage - The pillage gold
		if pWinnerPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_PILLAGE')):
			if not pLoser.isSummoned():
				pPlot = pLoser.plot()
				if pPlot.isCity() and bAttackerWon:
					iGold = cyFlatValue(25, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
					pWinnerPlayer.changeGold(iGold)

					szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_THE_PILLAGE_GOLD", (iGold,))
					szButton = gc.getTraitInfo(gc.getInfoTypeForString('TRAIT_PILLAGE')).getButton()
					szSound = 'AS2D_GOODY_GOLD'
					CyGame().pushGameMessage(eWinnerPlayer, True, szMessage, szSound, szButton, en.eColorGreen, pWinner.getX(), pWinner.getY(), True, True)

	## Xoth - Sanity Point Changes
		if pWinnerPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_XOTH') and pWinnerPlayer.getNumCities() > 0:
			if not pWinner.isAlive() and not pWinner.isMechUnit():
				if pWinnerPlayer.getGuildPlusCounter(50) < 0:
					pWinnerPlayer.setGuildPlusCounter(50, 0)
				elif pWinnerPlayer.getGuildPlusCounter(50) > 0:
					pWinnerPlayer.changeGuildPlusCounter(50, -1)

					szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_XOTH_SANITY_POINT_DECREASE', ('1', ))
					szButton = gc.getCivilizationInfo(gc.getInfoTypeForString('CIVILIZATION_XOTH')).getButton()
					szSound = 'AS3D_SPELL_CHARM_PERSON'
					CyGame().pushGameMessage(eWinnerPlayer, True, szMessage, szSound, szButton, en.eColorGreen, pWinner.getX(), pWinner.getY(), True, True)

	## Guildplus - Contcart War
		if pWinnerPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_TIGER'):
			if not pLoser.isSummoned():
				bContract = bool(pWinnerPlayer.getGuildPlusCounter(50))
				if bContract:
					iNum = pWinnerPlayer.getGuildPlusCounter(59)
					for iIndex in xrange(iNum):
						iEnemy = pWinnerPlayer.getGuildPlusCounter(60 + iIndex)
						if eLoserPlayer == iEnemy:
#							iAT = gc.getUnitInfo(pLoser.getUnitType()).getCombat()
#							iDF = gc.getUnitInfo(pLoser.getUnitType()).getCombatDefense()
#							iReward = max(iAT, iDF)
#							iReward = max(iAT, iDF) * 2 * gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent() // 100
							iPower = gc.getUnitInfo(pLoser.getUnitType()).getPowerValue()
							iReward = iPower * 2 * gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent() // 100
							if iReward > 0:
								pWinnerPlayer.changeGuildPlusCounter(53, 1)
								pWinnerPlayer.changeGuildPlusCounter(54, iReward*5)
								pWinnerPlayer.changeGold(iReward)
							break
#Kaijin <<<
##>>>>Advanced Kamikaze Rules: Modified by ent 2019/07/30
		if pWinner.getKamikazePercent() != 0:
			pWinner.kill(True, eLoserPlayer)
##<<<<Advanced Kamikaze Rules: End Modify

		if (not self.__LOG_COMBAT):
			return
		if playerX and playerX and unitX and playerY:
			CvUtil.pyPrint('Player %d Civilization %s Unit %s has defeated Player %d Civilization %s Unit %s'
				%(playerX.getID(), playerX.getCivilizationName(), unitX.getDescription(),
				playerY.getID(), playerY.getCivilizationName(), unitY.getDescription()))

	def onCombatLogCalc(self, argsList):
		'Combat Result'
		genericArgs = argsList[0][0]
		cdAttacker = genericArgs[0]
		cdDefender = genericArgs[1]
		iCombatOdds = genericArgs[2]
		CvUtil.combatMessageBuilder(cdAttacker, cdDefender, iCombatOdds)

	def onCombatLogHit(self, argsList):
		'Combat Message'
		global gCombatMessages, gCombatLog
		genericArgs = argsList[0][0]
		cdAttacker = genericArgs[0]
		cdDefender = genericArgs[1]
		iIsAttacker = genericArgs[2]
		iDamage = genericArgs[3]

		if cdDefender.eOwner == cdDefender.eVisualOwner:
			szDefenderName = gc.getPlayer(cdDefender.eOwner).getNameKey()
		else:
			szDefenderName = localText.getText("TXT_KEY_TRAIT_PLAYER_UNKNOWN", ())
		if cdAttacker.eOwner == cdAttacker.eVisualOwner:
			szAttackerName = gc.getPlayer(cdAttacker.eOwner).getNameKey()
		else:
			szAttackerName = localText.getText("TXT_KEY_TRAIT_PLAYER_UNKNOWN", ())

		if (iIsAttacker == 0):
			combatMessage = localText.getText("TXT_KEY_COMBAT_MESSAGE_HIT", (szDefenderName, cdDefender.sUnitName, iDamage, cdDefender.iCurrHitPoints, cdDefender.iMaxHitPoints))
			CyInterface().addCombatMessage(cdAttacker.eOwner, combatMessage)
			CyInterface().addCombatMessage(cdDefender.eOwner, combatMessage)
			if (cdDefender.iCurrHitPoints <= 0):
				combatMessage = localText.getText("TXT_KEY_COMBAT_MESSAGE_DEFEATED", (szAttackerName, cdAttacker.sUnitName, szDefenderName, cdDefender.sUnitName))
				CyInterface().addCombatMessage(cdAttacker.eOwner, combatMessage)
				CyInterface().addCombatMessage(cdDefender.eOwner, combatMessage)
		elif (iIsAttacker == 1):
			combatMessage = localText.getText("TXT_KEY_COMBAT_MESSAGE_HIT", (szAttackerName, cdAttacker.sUnitName, iDamage, cdAttacker.iCurrHitPoints, cdAttacker.iMaxHitPoints))
			CyInterface().addCombatMessage(cdAttacker.eOwner, combatMessage)
			CyInterface().addCombatMessage(cdDefender.eOwner, combatMessage)
			if (cdAttacker.iCurrHitPoints <= 0):
				combatMessage = localText.getText("TXT_KEY_COMBAT_MESSAGE_DEFEATED", (szDefenderName, cdDefender.sUnitName, szAttackerName, cdAttacker.sUnitName))
				CyInterface().addCombatMessage(cdAttacker.eOwner, combatMessage)
				CyInterface().addCombatMessage(cdDefender.eOwner, combatMessage)

	def onImprovementBuilt(self, argsList):
		'Improvement Built'
		iImprovement, iX, iY = argsList
		pPlot = CyMap().plot(iX, iY)

		if gc.getImprovementInfo(iImprovement).isUnique():
#Localize: Modified by anonymous
#			CyEngine().addLandmark(pPlot, CvUtil.convertToStr(gc.getImprovementInfo(iImprovement).getDescription()))
			CyEngine().addSign(pPlot, PlayerTypes.NO_PLAYER, gc.getImprovementInfo(iImprovement).getDescription())
#Localize: End Modify

			if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_RING_OF_CARCER'):
# Kaijin >>>
#				pPlot.setMinLevel(15)
				pPlot.setMinLevel(12)
# Kaijin <<<
				pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
				pBarbarianPlayer.initUnit(gc.getInfoTypeForString('UNIT_BRIGIT_HELD'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

			elif iImprovement in (gc.getInfoTypeForString('IMPROVEMENT_SEVEN_PINES'), gc.getInfoTypeForString('IMPROVEMENT_YGGDRASIL')):
				pPlot.setFeatureType(gc.getInfoTypeForString('FEATURE_FOREST_ANCIENT'), -1)
# OAC >>>
			elif iImprovement == gc.getInfoTypeForString('IMPROVEMENT_MOUNT_KALSHEKK'):
				pPlot.setFeatureType(gc.getInfoTypeForString('FEATURE_DEEP_JUNGLE'), 0)

		if iImprovement in (gc.getInfoTypeForString('IMPROVEMENT_BARROW'), gc.getInfoTypeForString('IMPROVEMENT_HAUNTED_RUINS')):
			pPlot.setFeatureType(gc.getInfoTypeForString('FEATURE_HAUNTED_LANDS'), -1)
# OAC <<<
		if gc.getImprovementInfo(iImprovement).getBonusConvert() != BonusTypes.NO_BONUS:
			if pPlot.getRouteType() == RouteTypes.NO_ROUTE:
				pPlot.setRouteType(gc.getInfoTypeForString('ROUTE_ROAD'))	#help out the AI for the moment

		if (not self.__LOG_IMPROVEMENT):
			return
		CvUtil.pyPrint('Improvement %s was built at %d, %d'
			%(PyInfo.ImprovementInfo(iImprovement).getDescription(), iX, iY))

	def onImprovementDestroyed(self, argsList):
		'Improvement Destroyed'
		iImprovement, iOwner, iX, iY = argsList

		if gc.getImprovementInfo(iImprovement).isUnique():
			pPlot = CyMap().plot(iX, iY)
			CyEngine().removeLandmark(pPlot)

			if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_RING_OF_CARCER'):
				pPlot.setMinLevel(-1)

		if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_NECROTOTEM'):
			CyGame().changeGlobalCounter(-2)

		if CyGame().getWBMapScript():
			sf.onImprovementDestroyed(iImprovement, iOwner, iX, iY)

		if (not self.__LOG_IMPROVEMENT):
			return
		CvUtil.pyPrint('Improvement %s was Destroyed at %d, %d'
			%(PyInfo.ImprovementInfo(iImprovement).getDescription(), iX, iY))

	def onRouteBuilt(self, argsList):
		'Route Built'
		iRoute, iX, iY = argsList
		if (not self.__LOG_IMPROVEMENT):
			return
		CvUtil.pyPrint('Route %s was built at %d, %d'
			%(gc.getRouteInfo(iRoute).getDescription(), iX, iY))

	def onPlotRevealed(self, argsList):
		'Plot Revealed'
		pPlot = argsList[0]
		iTeam = argsList[1]

	def onPlotFeatureRemoved(self, argsList):
		'Plot Revealed'
		pPlot = argsList[0]
		iFeatureType = argsList[1]
		pCity = argsList[2] # This can be null

	def onPlotPicked(self, argsList):
		'Plot Picked'
		pPlot = argsList[0]
		CvUtil.pyPrint('Plot was picked at %d, %d'
			%(pPlot.getX(), pPlot.getY()))

	def onNukeExplosion(self, argsList):
		'Nuke Explosion'
		pPlot, pNukeUnit = argsList
		CvUtil.pyPrint('Nuke detonated at %d, %d'
			%(pPlot.getX(), pPlot.getY()))

		if pNukeUnit is not None:
			eDiamondDrake = gc.getInfoTypeForString('UNIT_DIAMOND_DRAKE')
			eDistortion = gc.getInfoTypeForString('FEATURE_DISTORTION')
			eVoid = gc.getInfoTypeForString('FEATURE_VOID')
			iRange = pNukeUnit.nukeRange()
			lpRangedPlots = cyGetRangedPlots(pPlot, iRange, False, False, TeamTypes.NO_TEAM)
			
			for pTargetPlot in lpRangedPlots:

				iImprovement = pTargetPlot.getImprovementType()
				if iImprovement != ImprovementTypes.NO_IMPROVEMENT:
					pTargetPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
				iBonus = pTargetPlot.getBonusType(TeamTypes.NO_TEAM)
				if iBonus != BonusTypes.NO_BONUS:
					pTargetPlot.setBonusType(BonusTypes.NO_BONUS)

				bValue = True
				for iUnitIndex in xrange(pTargetPlot.getNumUnits()):
					pUnit = pTargetPlot.getUnit(iUnitIndex)
					if pUnit.getUnitType() == eDiamondDrake:
						bValue = False
					else:
						pUnit.kill(False, PlayerTypes.NO_PLAYER)
				if not pTargetPlot.isWater() and bValue:
					pTargetPlot.setPlotType(PlotTypes.PLOT_OCEAN, True, True)

#				if pTargetPlot.getFeatureType() != FeatureTypes.NO_FEATURE:
#					pTargetPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
				pTargetPlot.setFeatureType(eDistortion, 0)

			pPlot.setFeatureType(eVoid, 0)
			if pPlot.isVisibleToWatchingHuman():
				CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_HOLY_GRENADE_EXPLODE'), pPlot.getPoint())

	def onGotoPlotSet(self, argsList):
		'Nuke Explosion'
		pPlot, iPlayer = argsList

	def onBuildingBuilt(self, argsList):
		'Building Completed'
		pCity, iBuildingType = argsList
		player = pCity.getOwner()
		pPlayer = gc.getPlayer(player)
		pPlot = pCity.plot()
		game = gc.getGame()
		iBuildingClass = gc.getBuildingInfo(iBuildingType).getBuildingClassType()

		if ((not gc.getGame().isNetworkMultiPlayer()) and (pCity.getOwner() == gc.getGame().getActivePlayer()) and isWorldWonderClass(iBuildingClass)):
			if gc.getBuildingInfo(iBuildingType).getMovie():
				# If this is a wonder...
				popupInfo = CyPopupInfo()
				popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON_SCREEN)
				popupInfo.setData1(iBuildingType)
				popupInfo.setData2(pCity.getID())
				popupInfo.setData3(0)
				popupInfo.setText(u"showWonderMovie")
				popupInfo.addPopup(pCity.getOwner())

		if iBuildingType == gc.getInfoTypeForString('BUILDING_INFERNAL_GRIMOIRE'):
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#			if CyGame().getSorenRandNum(100, "Bob") <= 20:
			if CyGame().getSorenRandNum(100, "Bob") < 20:
##--------	Unofficial Bug Fix: End Modify			--------##
				pPlot2 = cf.findClearPlot(-1, pPlot)
				if pPlot2 != -1:
					pDemonPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER() + gc.getInfoTypeForString('BARBARIAN_DEMONS'))
					pNewUnit = pDemonPlayer.initUnit(gc.getInfoTypeForString('UNIT_BALOR'), pPlot2.getX(), pPlot2.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
					CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_INFERNAL_GRIMOIRE_BALOR", ()), 'AS2D_BALOR', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorRed, pNewUnit.getX(), pNewUnit.getY(), True, True)
					if pCity.getOwner() == CyGame().getActivePlayer():
						cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_INFERNAL_GRIMOIRE_BALOR", ()), 'art/interface/popups/Balor.dds')

##--------	Overriding Serial Buildings: Deleted by Denev	--------##
			pass
			"""
		elif iBuildingType == gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_FINAL'):
			pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_EXALTED'), 0)
		elif iBuildingType == gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_EXALTED'):
			pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_DIVINE'), 0)
		elif iBuildingType == gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_DIVINE'):
			pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_CONSECRATED'), 0)
		elif iBuildingType == gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_CONSECRATED'):
			pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_BLESSED'), 0)
		elif iBuildingType == gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_BLESSED'):
			pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_ANOINTED'), 0)
		elif iBuildingType == gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_ANOINTED'):
			pCity.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR'), 0)
			"""
##--------	Overriding Serial Buildings: End Delete			--------##

		elif iBuildingType == gc.getInfoTypeForString('BUILDING_MERCURIAN_GATE'):
##--------	Unofficial Bug Fix: Modified by Denev	--------##
			"""
			iMercurianPlayer = cf.getOpenPlayer()
			iTeam = pPlayer.getTeam()
			pPlot2 = cf.findClearPlot(-1, pCity.plot())
			if (iMercurianPlayer != -1 and pPlot2 != -1):
				for i in xrange(pPlot.getNumUnits(), -1, -1):
					pUnit = pPlot.getUnit(i)
					pUnit.setXY(pPlot2.getX(), pPlot2.getY(), True, True, True)
				CyGame().addPlayerAdvanced(iMercurianPlayer, iTeam, gc.getInfoTypeForString('LEADER_BASIUM'), gc.getInfoTypeForString('CIVILIZATION_MERCURIANS'))
				gc.getPlayer(iMercurianPlayer).initUnit(gc.getInfoTypeForString('UNIT_BASIUM'), pPlot.getX(), pPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
			"""
			for iLoop in xrange(pPlot.getNumUnits(), -1, -1):
				pUnit = pPlot.getUnit(iLoop)
				pUnit.jumpToNearestValidPlot()

			iMercurianPlayer = pPlayer.initNewEmpire(gc.getInfoTypeForString('LEADER_BASIUM'), en.eCivilizationMercurians)
			if iMercurianPlayer != PlayerTypes.NO_PLAYER:
				pMercurianPlayer = gc.getPlayer(iMercurianPlayer)
				iTeam = pPlayer.getTeam()
				iMercurianTeam = pMercurianPlayer.getTeam()
				if iTeam < iMercurianTeam:
					gc.getTeam(iTeam).addTeam(iMercurianTeam)
				else:
					gc.getTeam(iMercurianTeam).addTeam(iTeam)

##--------	Unofficial Bug Fix: Added by Denev	--------##
				pMercurianPlayer.setStartingPlot(pPlot, True)
##--------	Unofficial Bug Fix: End Add			--------##

				iX = pPlot.getX()
				iY = pPlot.getY()
				pBasiumUnit = pMercurianPlayer.initUnit(gc.getInfoTypeForString('UNIT_BASIUM'), iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
				pBasiumUnit.setAvatarOfCivLeader(True)	# When Basium is killed, his civilization loses all trait from him.
				pBasiumUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, True, False, MissionAITypes.NO_MISSIONAI, pBasiumUnit.plot(), pBasiumUnit)
				pBasiumUnit.getGroup().pushMission(MissionTypes.MISSION_SPELL, gc.getInfoTypeForString('SPELL_CONVERT_CITY_BASIUM'), 0, 0, True, False, MissionAITypes.NO_MISSIONAI, pBasiumUnit.plot(), pBasiumUnit)
				ltStartingUnits = [	(4,	gc.getInfoTypeForString('UNIT_ANGEL'),		[]	),
									(1,	gc.getInfoTypeForString('UNIT_SETTLER'),	[]	),
									(1,	gc.getInfoTypeForString('UNIT_WORKER'),		[]	)	]
				for iNumUnits, iUnit, liPromotions in ltStartingUnits:
					for iLoop in xrange(iNumUnits):
						pNewUnit = pMercurianPlayer.initUnit(iUnit, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
						for iPromotion in liPromotions:
							pNewUnit.setHasPromotion(iPromotion, True)

				pMercurianPlayer.AI_updateFoundValues(False)
##--------	Unofficial Bug Fix: End Modify			--------##

				if pPlayer.isHuman():
					popupInfo = CyPopupInfo()
					popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
					popupInfo.setText(CyTranslator().getText("TXT_KEY_POPUP_CONTROL_MERCURIANS", ()))
					popupInfo.setData1(player)
					popupInfo.setData2(iMercurianPlayer)
					popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_POPUP_YES", ()), "")
					popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_POPUP_NO", ()), "")
					popupInfo.setOnClickedPythonCallback("reassignPlayer")
					popupInfo.addPopup(player)

		elif iBuildingType == gc.getInfoTypeForString('BUILDING_TOWER_OF_THE_ELEMENTS'):
			lList = ['UNIT_AIR_ELEMENTAL', 'UNIT_EARTH_ELEMENTAL', 'UNIT_FIRE_ELEMENTAL', 'UNIT_WATER_ELEMENTAL']
			iUnit = gc.getInfoTypeForString(lList[CyGame().getSorenRandNum(len(lList), "Pick Elemental")])
			pNewUnit = pPlayer.initUnit(iUnit, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
#			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HELD'), True)
#Kaijin >>>
			pNewUnit.setHasPromotion(en.ePromotionHeroicStrength, True)
			pNewUnit.setHasPromotion(en.ePromotionHeroicStrength2, True)
			pNewUnit.setHasPromotion(en.ePromotionHeroicDefense, True)
			pNewUnit.setHasPromotion(en.ePromotionHeroicDefense2, True)
			pNewUnit.setHasPromotion(en.ePromotionStrong, True)
			pNewUnit.setHasPromotion(en.ePromotionMusou, True)
#Kaijin <<<
			CyInterface().addMessage(player, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_TOWER_OF_THE_ELEMENTS_SPAWN", ()), '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getUnitInfo(iUnit).getButton(), en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
			for pUnit in PyPlayer(player).getUnitList():
				if pUnit.getRace() == en.eRaceElemental:
					pUnit.setHasPromotion(en.ePromotionStrong, True)

		elif iBuildingType == gc.getInfoTypeForString('BUILDING_TOWER_OF_NECROMANCY'):
			for pUnit in PyPlayer(player).getUnitList():
				if pUnit.getRace() == en.eRaceUndead:
					pUnit.setHasPromotion(en.ePromotionStrong, True)

		elif iBuildingType == gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_HAND'):
			eEffect = gc.getInfoTypeForString('EFFECT_SNOWFALL')
			lpRangedPlots = cyGetRangedPlots(pPlot, pCity.getPlotRadius(), False, False, TeamTypes.NO_TEAM)
			for pTargetPlot in lpRangedPlots:
# Kaijin OAC - Crystal Plains ...etc
				"""
				if pTargetPlot.getImprovementType() == en.eImprovementSmoke:
					pTargetPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
				pTargetPlot.ceilColdCounter(9600 + CyGame().getSorenRandNum(2400, "Built Temple of the Hand"), 1000)
				eFeature = pTargetPlot.getFeatureType()
				if eFeature in (en.eFeatureForest, en.eFeatureJungle):
					pTargetPlot.setFeatureType(en.eFeatureForest, 2)
#				elif eFeature in (en.eFeatureFlames, en.eFeatureFloodPlains, en.eFeatureScrub, en.eFeatureObsidianPlains, en.eFeatureOasis):
				elif eFeature in (en.eFeatureFlames, en.eFeatureFloodPlains, en.eFeatureScrub, en.eFeatureObsidianPlains):
					pTargetPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)

			if pPlot.isVisibleToWatchingHuman():
				CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_SNOWFALL'), pPlot.getPoint())
				"""
				pWorkingCity = pTargetPlot.getWorkingCity()
				if pWorkingCity.getOwner() == pCity.getOwner() and pWorkingCity.getID() == pCity.getID():
					cf.doBuildingColdEffects(pTargetPlot)
					pTargetPlot.ceilColdCounter(9600 + CyGame().getSorenRandNum(2400, "Built Temple of the Hand"), 1000)

					if pTargetPlot.isVisibleToWatchingHuman():
						CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())
# Kaijin OAC - end

		elif iBuildingType == gc.getInfoTypeForString('BUILDING_GRAND_MENAGERIE'):
			if pPlayer.isHuman():
				if not CyGame().getWBMapScript():
					szTorophyKey = "TROPHY_FEAT_GRAND_MENAGERIE"
					if not CyGame().isHasTrophy(szTorophyKey):
						CyGame().changeTrophyValue(szTorophyKey, 1)

	## Malakim - Citadel of Light - Tile scorch
		elif iBuildingType == gc.getInfoTypeForString('BUILDING_CITADEL_OF_LIGHT'):
			eEffect = gc.getInfoTypeForString('EFFECT_SCORCH')
			lpRangedPlots = cyGetRangedPlots(pPlot, pCity.getPlotRadius() - 1, False, False, TeamTypes.NO_TEAM)
			for pTargetPlot in lpRangedPlots:
				if not pTargetPlot.isWater():
					pWorkingCity = pTargetPlot.getWorkingCity()
					if pWorkingCity.getOwner() == pCity.getOwner() and pWorkingCity.getID() == pCity.getID():
						bEffect = False
						if pTargetPlot.getTerrainType() != en.eTerrainDesert:
# ent >>>
							"""
							pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
							pTargetPlot.clearColdCounter()
							pTargetPlot.setTerrainType(en.eTerrainDesert, True, True)
							"""
							pTargetPlot.setPlotCounter(0)
							iOldFood = pTargetPlot.getYield(YieldTypes.YIELD_FOOD)
							pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
							pTargetPlot.clearColdCounter()
							pTargetPlot.setTerrainType(en.eTerrainDesert, True, True)
							iNewFood = pTargetPlot.getYield(YieldTypes.YIELD_FOOD)
							iModFood = min(iOldFood - iNewFood, pTargetPlot.getYield(YieldTypes.YIELD_PRODUCTION))
							if not pTargetPlot.isCity() and iModFood > 0:
								if CyGame().isOption(gc.getInfoTypeForString('GAMEOPTION_MODDER_4')):
									if pTargetPlot.isFlatlands() and pTargetPlot.isRiver():
										continue
								CyGame().setPlotExtraYield(pTargetPlot.getX(), pTargetPlot.getY(), YieldTypes.YIELD_FOOD, iModFood)
								CyGame().setPlotExtraYield(pTargetPlot.getX(), pTargetPlot.getY(), YieldTypes.YIELD_PRODUCTION, -1*iModFood)
								sCaptionFood = CyTranslator().getText("TXT_KEY_SIGN_FORMAT_FOOD", (iModFood, )) + u" "
								sCaptionProd = CyTranslator().getText("TXT_KEY_SIGN_FORMAT_PROD", (-1*iModFood, )) + u" "
								sCaptionComm = ""
								sCaptionDesc = CyTranslator().getText("TXT_KEY_SIGN_CITADEL_OF_LIGHT", ())

								sCaption = CyTranslator().getText("TXT_KEY_SIGN_FORMAT_OVERVIEW", (sCaptionFood, sCaptionProd, sCaptionComm, sCaptionDesc))

								for eLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
									pLoopPlayer = gc.getPlayer(eLoopPlayer)
									if pLoopPlayer.isAlive() and pLoopPlayer.isHuman():
										CyEngine().addSign(pTargetPlot, eLoopPlayer, sCaption)
# ent <<<
							bEffect = True
						eFeature = pTargetPlot.getFeatureType()
						if eFeature in (en.eFeatureForest, en.eFeatureJungle, en.eFeatureForestAncient, en.eFeatureDeepJungle):
							pTargetPlot.setFeatureType(en.eFeatureScrub, -1)
							bEffect = True
						if bEffect and pTargetPlot.isVisibleToWatchingHuman():
							CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())

	## Tokoyami - 炎獄の祭壇による地獄の浸食
		elif iBuildingType == gc.getInfoTypeForString('BUILDING_DARK_TEMPLE') and not CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_PLOT_COUNTER):
			eEffect = gc.getInfoTypeForString('EFFECT_SCORCH')
			lpRangedPlots = cyGetRangedPlots(pPlot, pCity.getPlotRadius(), False, False, TeamTypes.NO_TEAM)
			for pTargetPlot in lpRangedPlots:
				pWorkingCity = pTargetPlot.getWorkingCity()
				if pWorkingCity.getOwner() == pCity.getOwner() and pWorkingCity.getID() == pCity.getID():
#					iFeature = pTargetPlot.getFeatureType()
#					iBonus = pTargetPlot.getBonusType(TeamTypes.NO_TEAM)
					pTargetPlot.setPlotCounter(100)
#					if iBonus != BonusTypes.NO_BONUS:
#						if gc.getImprovementInfo(en.eImprovementFarm).isImprovementBonusTrade(iBonus):
#							pTargetPlot.setImprovementType(en.eImprovementSnakePillar)
#					if iFeature == en.eFeatureFloodPlains:
#						pTargetPlot.setFeatureType(en.eFeatureObsidianPlains, -1)
					if pTargetPlot.isVisibleToWatchingHuman():
						CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())

	## Nival - 宮殿による寒冷化
		elif iBuildingType == gc.getInfoTypeForString('BUILDING_PALACE_NIVAL'):
			eEffect = gc.getInfoTypeForString('EFFECT_SNOWFALL')
			lpRangedPlots = cyGetRangedPlots(pPlot, pCity.getPlotRadius(), False, False, TeamTypes.NO_TEAM)
			for pTargetPlot in lpRangedPlots:
				pWorkingCity = pTargetPlot.getWorkingCity()
				if pWorkingCity.getOwner() == pCity.getOwner() and pWorkingCity.getID() == pCity.getID():
					cf.doBuildingColdEffects(pTargetPlot)
					pTargetPlot.ceilColdCounter(9600 + CyGame().getSorenRandNum(2400, "Built Temple of the Hand"), 1000)
					if pTargetPlot.getTerrainType() != en.eTerrainSnow:
						if pTargetPlot.isVisibleToWatchingHuman():
							CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())

	## Baldralfar - 再生の祭壇による肥沃化
		elif iBuildingType == gc.getInfoTypeForString('BUILDING_BALDRALFAR_TEMPLE'):
			liDesertFeatures = [en.eFeatureFloodPlains, en.eFeatureOasis]
			iBurntForest = gc.getDefineINT('FLAMES_EXPIRE_EFFECT')
			lpRangedPlots = cyGetRangedPlots(pPlot, pCity.getPlotRadius(), False, False, TeamTypes.NO_TEAM)
			for pTargetPlot in lpRangedPlots:
				if not pTargetPlot.isWater():
					pWorkingCity = pTargetPlot.getWorkingCity()
					if pWorkingCity.getOwner() == pCity.getOwner() and pWorkingCity.getID() == pCity.getID():
						pTargetPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
						pTargetPlot.setPlotCounter(0)
#						pTargetPlot.clearColdCounter()
						iFeature = pTargetPlot.getFeatureType()
						if pTargetPlot.getTerrainType() == en.eTerrainSnow:
							pTargetPlot.setTerrainType(en.eTerrainTundra, False, True)
						elif pTargetPlot.getTerrainType() == en.eTerrainTundra:
							pTargetPlot.setTerrainType(en.eTerrainPlains, False, True)
						elif pTargetPlot.getTerrainType() == en.eTerrainDesert:
							if iFeature not in liDesertFeatures:
								pTargetPlot.setTerrainType(en.eTerrainPlains, False, True)
						elif pTargetPlot.getTerrainType() == en.eTerrainPlains:
							pTargetPlot.setTerrainType(en.eTerrainGrass, False, True)
						elif pTargetPlot.getTerrainType() == en.eTerrainGrass:
							if iFeature == FeatureTypes.NO_FEATURE:
								if pTargetPlot.canHaveFeatureOnImprovement(en.eFeatureForestNew):
									pTargetPlot.setFeatureType(en.eFeatureForestNew, 0)
						elif pTargetPlot.getTerrainType() == en.eTerrainMarsh:
							pTargetPlot.setTerrainType(en.eTerrainGrass, False, True)
						if iFeature == en.eFeatureJungle:
							pTargetPlot.setFeatureType(en.eFeatureForest, 0)
						elif iFeature == en.eFeatureFlames:
							pTargetPlot.setFeatureType(iBurntForest, 0)
						elif iFeature == en.eFeatureSwamp:
							pTargetPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
						elif iFeature == en.eFeatureBlizzard:
							pTargetPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
						elif iFeature != FeatureTypes.NO_FEATURE:
							iUpgrade = gc.getFeatureInfo(iFeature).getFeatureUpgrade()
							if iUpgrade != FeatureTypes.NO_FEATURE:
								iStateReligion = gc.getFeatureInfo(iUpgrade).getPrereqStateReligion()
								if iStateReligion in (ReligionTypes.NO_RELIGION, gc.getPlayer(player).getStateReligion()):
									pTargetPlot.setFeatureType(iUpgrade, 0)
						if pTargetPlot.getImprovementType() == gc.getDefineINT('FLAMES_SPREAD_EFFECT'):
							pTargetPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)

	## Megisus - グヌークの泉による生きている鎧の強化
		elif iBuildingType == gc.getInfoTypeForString('BUILDING_SPRING_OF_GHNUKE'):
			eLivingArmor = gc.getInfoTypeForString('UNIT_LIVING_ARMOR')
			eVarrage1 = gc.getInfoTypeForString('PROMOTION_BARRAGE1')
			for pUnit in PyPlayer(player).getUnitList():
				if pUnit.getUnitType() == eLivingArmor:
					pUnit.setHasPromotion(eVarrage1, True)

	## Megisus - 陽と風の魔法円による生きている鎧の強化
		elif iBuildingType == gc.getInfoTypeForString('BUILDING_CIRCLE_OF_MONSOON'):
			eLivingArmor = gc.getInfoTypeForString('UNIT_LIVING_ARMOR')
			for pUnit in PyPlayer(player).getUnitList():
				if pUnit.getUnitType() == eLivingArmor:
					pUnit.changeCombatStr(1)

# 遺産狂志向
		if isWorldWonderClass(iBuildingClass):
		## マーキュリアンの門と聖都建造物（祭殿＋固有装備品）は除外
			if iBuildingType != gc.getInfoTypeForString('BUILDING_MERCURIAN_GATE') and gc.getBuildingInfo(iBuildingType).getHolyCity() == ReligionTypes.NO_RELIGION:
				eTraitWorldHeritage = gc.getInfoTypeForString('TRAIT_CRAZY_BY_WORLDHERITAGE')
		## 遺産完成により黄金期始動または延長
				if pPlayer.hasTrait(eTraitWorldHeritage):
					pPlayer.changeGoldenAgeTurns(CyGame().goldenAgeLength() // 2)
		## 遺産狂志向ではない指導者が遺産を完成させた場合の処理
				else:
					iTeam = pPlayer.getTeam()
					for iLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
						pLoopPlayer = gc.getPlayer(iLoopPlayer)
						if pLoopPlayer.isAlive():
							if pLoopPlayer.hasTrait(eTraitWorldHeritage):
								## 黄金期中ならば期間短縮の上で、各都市が20%で叛乱
								if pLoopPlayer.isGoldenAge():
									pLoopPlayer.changeGoldenAgeTurns(-1 * (CyGame().goldenAgeLength() // 2))
									for pyCity in PyPlayer(iLoopPlayer).getCityList() :
										pLoopCity = pyCity.GetCy()
										if CyGame().getSorenRandNum(100, "Angry") < 20:
											pLoopCity.changeOccupationTimer(5)
								## 遺産を横取りした文明に対して、怒りの宣戦布告と一時断交
								pLoopTeam = gc.getTeam(pLoopPlayer.getTeam())
								if not gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ALWAYS_PEACE):
									eBuiltTeam = pPlayer.getTeam()
									pBuiltTeam = gc.getTeam(eBuiltTeam)
									if pLoopTeam.isHasMet(eBuiltTeam):
										if pLoopTeam.canChangeWarPeace(eBuiltTeam):
											pLoopTeam.declareWar(eBuiltTeam, False, WarPlanTypes.WARPLAN_LIMITED)
										pLoopTeam.setPermanentWarPeace(eBuiltTeam, True)
										iRefusal = cyFlatValue(20, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getGoldenAgePercent(), False)
										CRAZY_OFFSET = 5
										pLoopPlayer.setGuildPlusCounter(eBuiltTeam + CRAZY_OFFSET, iRefusal)

# Equipments - AI to equip automatically.
		if not pPlayer.isHuman():
			if iBuildingType in (gc.getInfoTypeForString('BUILDING_INFERNAL_GRIMOIRE'), 
									gc.getInfoTypeForString('BUILDING_EARTH_PULSE'), 
									gc.getInfoTypeForString('BUILDING_GLORIOUS_SHIELD'), 
									gc.getInfoTypeForString('BUILDING_BRACELET_OF_NIGHTMARE'), 
									gc.getInfoTypeForString('BUILDING_ORB_OF_YGGFRASIL'), 
									gc.getInfoTypeForString('BUILDING_DEMONS_FANG'), 
									gc.getInfoTypeForString('BUILDING_RING_OF_THE_SUN'), 
									gc.getInfoTypeForString('BUILDING_BLOODY_OATH')	):
				lpRangedUnits = cyGetRangedUnits(pPlot, 0, False, True, pCity.getTeam())
				lpEquipedUnits = [	pEquipedUnit for pEquipedUnit in lpRangedUnits
												if	pEquipedUnit.canFight()
												and	not pEquipedUnit.isSummoned()
												and not pEquipedUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ILLUSION'))		]
				if len(lpEquipedUnits) > 0:
					pEquipedUnit = lpEquipedUnits[CyGame().getSorenRandNum(len(lpEquipedUnits), "Pick Equiped Unit")]
					ltEquipments = []
					if gc.getBuildingInfo(iBuildingType).isEquipment():
						if pCity.getNumRealBuilding(iBuildingType) > 0:
							ltEquipments.append((iBuildingType, pCity))

					if len(ltEquipments) > 0:
						iRnd = CyGame().getSorenRandNum(len(ltEquipments), 'Choose Target')
						iEquipmentIndex, pVictim = ltEquipments[iRnd]

						for iLoopUnit in xrange(gc.getNumUnitInfos()):
							if gc.getUnitInfo(iLoopUnit).getBuildings(iEquipmentIndex):
								iBuilding = iEquipmentIndex
								iEquipmentIndex = gc.getUnitInfo(iLoopUnit).getEquipmentPromotion()
								break
						kEquipmentPromotion = gc.getPromotionInfo(iEquipmentIndex)

						pVictim.setNumRealBuilding(iBuilding, 0)
						pEquipedUnit.setHasPromotion(iEquipmentIndex, True)

# Kaijin <<<
		CvAdvisorUtils.buildingBuiltFeats(pCity, iBuildingType)

		if (not self.__LOG_BUILDING):
			return
		CvUtil.pyPrint('%s was finished by Player %d Civilization %s'
			%(PyInfo.BuildingInfo(iBuildingType).getDescription(), pCity.getOwner(), gc.getPlayer(pCity.getOwner()).getCivilizationDescription(0)))

	def onProjectBuilt(self, argsList):
		'Project Completed'
		pCity, iProjectType = argsList
		game = gc.getGame()
		iPlayer = pCity.getOwner()
		pPlayer = gc.getPlayer(iPlayer)
		if not gc.getGame().isNetworkMultiPlayer() and pCity.getOwner() == gc.getGame().getActivePlayer():
			popupInfo = CyPopupInfo()
			popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON_SCREEN)
			popupInfo.setData1(iProjectType)
			popupInfo.setData2(pCity.getID())
			popupInfo.setData3(2)
			popupInfo.setText(u"showWonderMovie")
			popupInfo.addPopup(iPlayer)

		if iProjectType == gc.getInfoTypeForString('PROJECT_BANE_DIVINE'):
			"""
			iCombatDisciple = gc.getInfoTypeForString('UNITCOMBAT_DISCIPLE')
			for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
				pLoopPlayer = gc.getPlayer(iLoopPlayer)
				if pLoopPlayer.isAlive():
					apUnitList = PyPlayer(iLoopPlayer).getUnitList()
					for pUnit in apUnitList:
						if pUnit.getUnitCombatType() == iCombatDisciple:
							pUnit.kill(False, pCity.getOwner())
			"""
			iDelay = cyFlatValue(30, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), True)
			for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
				pLoopPlayer = gc.getPlayer(iLoopPlayer)
				if pLoopPlayer.isAlive():
					apUnitList = PyPlayer(iLoopPlayer).getUnitList()
					for pUnit in apUnitList:
						if pUnit.getUnitCombatType() == en.eUnitCombatDisciple:
							if pUnit.isHasPromotion(en.ePromotionDivine):
								pUnit.setHasPromotion(en.ePromotionSealed, True)
								pUnit.setUncastableTimer(iDelay)

		elif iProjectType == gc.getInfoTypeForString('PROJECT_GENESIS'):
			cf.genesis(iPlayer)

		elif iProjectType == gc.getInfoTypeForString('PROJECT_GLORY_EVERLASTING'):
			"""
			iDemon = gc.getInfoTypeForString('PROMOTION_DEMON')
			iUndead = gc.getInfoTypeForString('PROMOTION_UNDEAD')
			for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
				pLoopPlayer = gc.getPlayer(iLoopPlayer)
				if pLoopPlayer.isAlive():
					apUnitList = PyPlayer(iLoopPlayer).getUnitList()
					for pUnit in apUnitList:
						if pUnit.getRace() in (iDemon, iUndead):
							pUnit.kill(False, iPlayer)
			"""
			iDelay = cyFlatValue(10, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getGoldenAgePercent(), True)
			for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
				pLoopPlayer = gc.getPlayer(iLoopPlayer)
				if pLoopPlayer.isAlive():
					apUnitList = PyPlayer(iLoopPlayer).getUnitList()
					for pUnit in apUnitList:
						if pUnit.getRace() in (en.eRaceDemon, en.eRaceUndead):
							pUnit.changeImmobileTimer(iDelay)

		elif iProjectType == gc.getInfoTypeForString('PROJECT_RITES_OF_OGHMA'):
			iBaseNumber = gc.getWorldInfo(CyMap().getWorldSize()).getDefaultPlayers()
			iNumBonuses = CyGame().getSorenRandNum(iBaseNumber, "Rites of Oghma") + CyGame().getSorenRandNum(iBaseNumber, "Rites of Oghma") + 1
			iNumBonuses = (iBaseNumber + iNumBonuses + 1) // 2
			cf.addBonus(gc.getInfoTypeForString('BONUS_MANA'), iNumBonuses)

		elif iProjectType == gc.getInfoTypeForString('PROJECT_NATURES_REVOLT'):
			pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
			eAnimalPlayer = gc.getBARBARIAN_PLAYER() + gc.getInfoTypeForString('BARBARIAN_ANIMAL')
			pAnimalPlayer = gc.getPlayer(eAnimalPlayer)
			eWorker		= gc.getInfoTypeForString('UNITCLASS_WORKER')
			eScout		= gc.getInfoTypeForString('UNITCLASS_SCOUT')
			eHunter		= gc.getInfoTypeForString('UNITCLASS_HUNTER')
			eWarrior	= gc.getInfoTypeForString('UNITCLASS_WARRIOR')
			eAxeman		= gc.getInfoTypeForString('UNITCLASS_AXEMAN')
			eArcher		= gc.getInfoTypeForString('UNITCLASS_ARCHER')
			eHorseman	= gc.getInfoTypeForString('UNITCLASS_HORSEMAN')
			eBear		= gc.getInfoTypeForString('UNIT_BEAR')
			eGorilla	= gc.getInfoTypeForString('UNIT_GORILLA')
			eLion		= gc.getInfoTypeForString('UNIT_LION')
			eLionPride	= gc.getInfoTypeForString('UNIT_LION_PRIDE')
			eScorpion	= gc.getInfoTypeForString('UNIT_SCORPION')
			eBabySpider	= gc.getInfoTypeForString('UNIT_BABY_SPIDER')
			eBigSpider	= gc.getInfoTypeForString('UNIT_GIANT_SPIDER')
			eTiger		= gc.getInfoTypeForString('UNIT_TIGER')
			eWolf		= gc.getInfoTypeForString('UNIT_WOLF')
			eWolfPack	= gc.getInfoTypeForString('UNIT_WOLF_PACK')
			for pUnit in PyPlayer(gc.getBARBARIAN_PLAYER()).getUnitList():
				leNewUnit = []
				if pUnit.getUnitClassType() == eWorker:
					leNewUnit = [eWolf, eWolf, eWolf]
				elif pUnit.getUnitClassType() == eScout:
					leNewUnit = [eWolfPack, eWolfPack, eWolfPack]
				elif pUnit.getUnitClassType() == eWarrior:
					leNewUnit = [eLion, eLion, eBabySpider]
				elif pUnit.getUnitClassType() == eHunter:
					leNewUnit = [eTiger, eTiger, eBigSpider]
				elif pUnit.getUnitClassType() == eAxeman:
					leNewUnit = [eBear, eBear, eBear]
				elif pUnit.getUnitClassType() == eArcher:
					leNewUnit = [eScorpion, eScorpion, eScorpion]
				elif pUnit.getUnitClassType() == eHorseman:
					leNewUnit = [eLionPride, eLionPride, eGorilla]
				if len(leNewUnit) > 0:
					iBestValue = -1
					pBestPlot = None
					for iDirection in xrange(DirectionTypes.NUM_DIRECTION_TYPES):
						pLoopPlot = plotDirection(pUnit.getX(), pUnit.getY(), DirectionTypes(iDirection))
						if not pLoopPlot.isNone():
							if pLoopPlot.isVisibleEnemyUnit(eAnimalPlayer) == 0:
								if not pLoopPlot.isWater() and not pLoopPlot.isImpassable() and not pLoopPlot.isCity():
									iValue = CyGame().getSorenRandNum(1000, "FindAdjacentClearPlot")
									if iBestValue < iValue:
										pBestPlot = pLoopPlot
										iBestValue = iValue
					if pBestPlot is None:
						continue
					eNewUnit = leNewUnit.pop(0)
					pNewUnit = pAnimalPlayer.initUnit(eNewUnit, pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_NORTH)
					pNewUnit.convert(pUnit)
					eRace = pNewUnit.getRace()
					for eNewUnit in leNewUnit:
						pNewUnit = pAnimalPlayer.initUnit(eNewUnit, pBestPlot.getX(), pBestPlot.getY(), UnitAITypes.UNITAI_ATTACK, DirectionTypes.DIRECTION_SOUTH)
						pNewUnit.setHasPromotion(eRace, True)
						pNewUnit.changeImmobileTimer(1)
			for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
				pLoopPlayer = gc.getPlayer(iLoopPlayer)
				if pLoopPlayer.isAlive():
					for pUnit in PyPlayer(iLoopPlayer).getUnitList():
						if pUnit.getUnitCombatType() == en.eUnitCombatAnimal:
							pUnit.setHasPromotion(en.ePromotionHeroicStrength, True)
							pUnit.setHasPromotion(en.ePromotionHeroicStrength2, True)
							pUnit.setHasPromotion(en.ePromotionHeroicDefense, True)
							pUnit.setHasPromotion(en.ePromotionHeroicDefense2, True)

		elif iProjectType == gc.getInfoTypeForString('PROJECT_BLOOD_OF_THE_PHOENIX'):
			for pUnit in PyPlayer(iPlayer).getUnitList():
				if pUnit.isAlive():
##--------	Unofficial Bug Fix: Added by Denev	--------##
					if pUnit.getUnitCombatType() != UnitCombatTypes.NO_UNITCOMBAT:
##--------	Unofficial Bug Fix: End Add			--------##
						pUnit.setHasPromotion(en.ePromotionImmortal, True)

		elif iProjectType == gc.getInfoTypeForString('PROJECT_PURGE_THE_UNFAITHFUL'):
			for pyCity in PyPlayer(iPlayer).getCityList():
				pLoopCity = pyCity.GetCy()
				iOccupationTimer = CyGame().getSorenRandNum(2, "Purge the Unfaithful")
				StateBelief = pPlayer.getStateReligion()
				if StateBelief == en.eReligionOrder:
					iOccupationTimer -= 1
				for iReligion in xrange(gc.getNumReligionInfos()):
					if StateBelief != iReligion and pLoopCity.isHasReligion(iReligion) and not pLoopCity.isHolyCityByType(iReligion):
						pLoopCity.setHasReligion(iReligion, False, True, True)
						iOccupationTimer += 1
						for iBuilding in xrange(gc.getNumBuildingInfos()):
							if gc.getBuildingInfo(iBuilding).getPrereqReligion() == iReligion:
								pLoopCity.setNumRealBuilding(iBuilding, 0)
				iOccupationTimer = cyFlatValue(iOccupationTimer, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getHurryConscriptAngerPercent(), True)
				if iOccupationTimer > 0:
					pLoopCity.setOccupationTimer(pLoopCity.getOccupationTimer() + iOccupationTimer)

		elif iProjectType == gc.getInfoTypeForString('PROJECT_BIRTHRIGHT_REGAINED'):
			pPlayer.setFeatAccomplished(FeatTypes.FEAT_GLOBAL_SPELL, False)

		elif iProjectType == gc.getInfoTypeForString('PROJECT_SAMHAIN'):
			iNumPlayers = CyGame().countCivPlayersAlive()
			iCount = iNumPlayers + CyGame().getNumCities() // iNumPlayers
			eBarbarianFrostling = gc.getInfoTypeForString('BARBARIAN_FROSTLING')
			eFrostling = gc.getInfoTypeForString('UNIT_FROSTLING')
			eArcher = gc.getInfoTypeForString('UNIT_ARCHER')
			eWolfRider = gc.getInfoTypeForString('UNIT_WOLF_RIDER')
			"""
			for i in xrange(iCount):
				pNewUnit1 = cf.addBarbarianUnit(eFrostling, eBarbarianFrostling)
				pNewUnit2 = cf.addBarbarianUnit(eFrostling, eBarbarianFrostling)
				pNewUnit3 = cf.addBarbarianUnit(eArcher, eBarbarianFrostling)
				pNewUnit4 = cf.addBarbarianUnit(eWolfRider, eBarbarianFrostling)
				pNewUnit1.changeImmobileTimer(1)
				pNewUnit2.changeImmobileTimer(1)
				pNewUnit3.changeImmobileTimer(1)
				pNewUnit4.changeImmobileTimer(1)
			pNewUnit = cf.addBarbarianUnit(gc.getInfoTypeForString('UNIT_MOKKA'), eBarbarianFrostling)
			pNewUnit.changeImmobileTimer(1)
			"""

			pNewUnit = cf.addBarbarianUnit(gc.getInfoTypeForString('UNIT_MOKKA'), eBarbarianFrostling)
			if pNewUnit is not None:
				pNewUnit.changeImmobileTimer(1)

			leMonsters = [eFrostling, eFrostling, eArcher, eWolfRider]
			for i in xrange(iCount):
				for eMonster in leMonsters:
					pNewUnit = cf.addBarbarianUnit(eMonster, eBarbarianFrostling)
					if pNewUnit is not None:
						pNewUnit.changeImmobileTimer(1)

			for pyCity in PyPlayer(iPlayer).getCityList():
				pLoopCity = pyCity.GetCy()
				pLoopCity.changeWeLoveTheKingDayProbability(90)

		elif iProjectType == gc.getInfoTypeForString('PROJECT_THE_WHITE_HAND'):
			iNumPriests = 3
			ePriest = gc.getInfoTypeForString('UNIT_PRIEST_OF_WINTER')
			for iLoop in xrange(iNumPriests):
				pNewUnit = pPlayer.initUnit(ePriest, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
				pCity.applyBuildEffects(pNewUnit)
				pNewUnit.setHasPromotion(en.ePromotionHeroicStrength, True)
				pNewUnit.setHasPromotion(en.ePromotionHeroicStrength2, True)
				pNewUnit.setHasPromotion(en.ePromotionHeroicDefense, True)
				pNewUnit.setHasPromotion(en.ePromotionHeroicDefense2, True)
				CvAdvisorUtils.unitBuiltFeats(pCity, pNewUnit)

##--------	Advanced Winter Projects: Added by ent
			eTempleHand = gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_HAND')
			for pyCity in PyPlayer(iPlayer).getCityList():
				pLoopCity = pyCity.GetCy()
				if pLoopCity.isHasActiveBuilding(eTempleHand):
					pNewUnit = pPlayer.initUnit(ePriest, pLoopCity.getX(), pLoopCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
					pLoopCity.applyBuildEffects(pNewUnit)
##--------	Advanced Winter Projects: End Add

		elif iProjectType == gc.getInfoTypeForString('PROJECT_THE_DEEPENING'):
			for iPlotIndex in range (CyMap().numPlots()):
				pPlot = CyMap().plotByIndex(iPlotIndex)
				if pPlot.isWater() or pPlot.isImpassable() or pPlot.getFeatureType() == en.eFeatureOasis:
					continue
				elif CyGame().getSorenRandNum(1000, "Deepening") < 333:
					continue
				iTerrain = pPlot.getTerrainType()
				if pPlot.getImprovementType() == en.eImprovementSmoke:
					pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
				pPlot.ceilColdCounter(2000 + CyGame().getSorenRandNum(6000, "The Deepening"), -1)
				eFeature = pPlot.getFeatureType()
				if eFeature in (en.eFeatureForest, en.eFeatureJungle):
					pPlot.setFeatureType(en.eFeatureForest, 2)
				elif eFeature == en.eFeatureFlames:
					pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
				elif eFeature in (en.eFeatureFloodPlains, en.eFeatureOasis, en.eFeatureScrub, en.eFeatureObsidianPlains):
					if not gc.getFeatureInfo(eFeature).isTerrain(pPlot.getTerrainType()):
						pPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)
				if iTerrain in (en.eTerrainSnow, en.eTerrainTundra):
					if CyGame().getSorenRandNum(100, "The Deepening: Blizzard") < 1:
						pPlot.setFeatureType(en.eFeatureBlizzard, 0)
##--------	Cold Counter: Added by Denev	--------##
# Temp Delete
#			CyGame().changeIceAge(1)
##--------	Cold Counter: End Add			--------##

		elif iProjectType == gc.getInfoTypeForString('PROJECT_STIR_FROM_SLUMBER'):
			pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_DRIFA'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pCity.applyBuildEffects(pNewUnit)
##--------	Advanced Winter Projects: Added by ent
			iNumPriests = 3
			ePriest = gc.getInfoTypeForString('UNIT_DISCIPLE_OF_THE_DRAGON')
			for iLoop in xrange(iNumPriests):
				pNewUnit = pPlayer.initUnit(ePriest, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
				pCity.applyBuildEffects(pNewUnit)
##--------	Advanced Winter Projects: End Add

		elif iProjectType == gc.getInfoTypeForString('PROJECT_THE_DRAW'):
			pPlayer.changeNoDiplomacyWithEnemies(1)
			iTeam = pPlayer.getTeam()
			pTeam = gc.getTeam(iTeam)
			liDeclareWarTeams = []
			if not gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ALWAYS_PEACE):
				for eLoopTeam in xrange(gc.getMAX_CIV_TEAMS()):
					pLoopTeam = gc.getTeam(eLoopTeam)
					if pLoopTeam.isAlive():
						if pTeam.canChangeWarPeace(eLoopTeam):
							liDeclareWarTeams.append(eLoopTeam)
			while len(liDeclareWarTeams) > 0:
				iDeclareWarTeam = liDeclareWarTeams.pop(CyGame().getSorenRandNum(len(liDeclareWarTeams), "The Draw"))
				pTeam.declareWar(iDeclareWarTeam, False, WarPlanTypes.WARPLAN_TOTAL)
			py = PyPlayer(iPlayer)
			for pUnit in py.getUnitList():
				iDmg = max(50, min(pUnit.maxHitPoints() - 1, pUnit.getDamage() * 2))
				pUnit.setDamage(iDmg, iPlayer)
			for pyCity in PyPlayer(iPlayer).getCityList():
				pLoopCity = pyCity.GetCy()
				iPop = max(1, pLoopCity.getPopulation() // 2)
				pLoopCity.setPopulation(iPop)

		elif iProjectType == gc.getInfoTypeForString('PROJECT_ASCENSION'):
##--------	Unofficial Bug Fix: Modified by Denev	--------##
			"When Auric is killed, his civilization loses all trait from him."
#			pPlayer.initUnit(gc.getInfoTypeForString('UNIT_AURIC_ASCENDED'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pAuricUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_AURIC_ASCENDED'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pAuricUnit.setAvatarOfCivLeader(True)
##--------	Unofficial Bug Fix: End Modify			--------##
##--------	Cold Counter: Added by Denev	--------##
			CyGame().changeIceAge(1)
##--------	Cold Counter: End Add			--------##
			if pPlayer.isHuman():
				szTorophyKey = "TROPHY_FEAT_ASCENSION"
				if not CyGame().isHasTrophy(szTorophyKey):
					CyGame().changeTrophyValue(szTorophyKey, 1)
			if not CyGame().getWBMapScript():
				iBestPlayer = -1
				iBestValue = 0
				for iLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
					pLoopPlayer = gc.getPlayer(iLoopPlayer)
					if pLoopPlayer.isAlive():
						if pLoopPlayer.getTeam() != pPlayer.getTeam():
							iValue = CyGame().getSorenRandNum(500, "Ascension")
							if pLoopPlayer.isHuman():
								iValue += 2000
							iValue += (20 - CyGame().getPlayerRank(iLoopPlayer)) * 50
							if iValue > iBestValue:
								iBestValue = iValue
								iBestPlayer = iLoopPlayer
				if iBestPlayer != -1:
					pBestPlayer = gc.getPlayer(iBestPlayer)
					pBestCity = pBestPlayer.getCapitalCity()
					if pBestPlayer.isHuman():
						iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(), 'EVENTTRIGGER_GODSLAYER')
##--------	Unofficial Bug Fix: Modified by Denev	--------##
#						triggerData = gc.getPlayer(iBestPlayer).initTriggeredData(iEvent, True, -1, pBestCity.getX(), pBestCity.getY(), iBestPlayer, -1, -1, -1, -1, -1)
						gc.getPlayer(iBestPlayer).triggerCustomEvent(iEvent, -1, pBestCity.getX(), pBestCity.getY(), PlayerTypes.NO_PLAYER, -1, ReligionTypes.NO_RELIGION, CorporationTypes.NO_CORPORATION, -1, BuildingTypes.NO_BUILDING)
##--------	Unofficial Bug Fix: End Modify			--------##
					else:
						pBestPlayer.initUnit(gc.getInfoTypeForString('UNIT_GODSLAYER'), pBestCity.getX(), pBestCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

		elif iProjectType == gc.getInfoTypeForString('PROJECT_PACT_OF_THE_NILHORN'):
			lszNames = [	CyTranslator().getText("TXT_KEY_UNIT_HILL_GIANT_OF_NILHORN_01", ()),
							CyTranslator().getText("TXT_KEY_UNIT_HILL_GIANT_OF_NILHORN_02", ()),
							CyTranslator().getText("TXT_KEY_UNIT_HILL_GIANT_OF_NILHORN_03", ())	]
			for szName in lszNames:
				pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_HILL_GIANT'), pCity.getX(), pCity.getY(), UnitAITypes.UNITAI_ATTACK_CITY, DirectionTypes.DIRECTION_NORTH)
				pNewUnit.setHasPromotion(gc.getDefineINT('HIDDEN_NATIONALITY_PROMOTION'), True)
				pNewUnit.setName(szName)
				CvAdvisorUtils.unitBuiltFeats(pCity, pNewUnit)

# Kaijin >>>
# Sheaim
	## Elegy of the Sheaim
		elif iProjectType == gc.getInfoTypeForString('PROJECT_ELEGY_OF_THE_SHEAIM'):
			eProphecyMark = gc.getInfoTypeForString('PROMOTION_PROPHECY_MARK')
			for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
				pLoopPlayer = gc.getPlayer(iLoopPlayer)
				if pLoopPlayer.isAlive():
					if pLoopPlayer.getCivilizationType() == en.eCivilizationSheaim:
						py = PyPlayer(iLoopPlayer)
						for pLoopUnit in py.getUnitList():
							if not pLoopUnit.isHasPromotion(eProphecyMark):
								if CyGame().getSorenRandNum(100, "Prophecy") < 25:
									pLoopUnit.setHasPromotion(eProphecyMark, True)
							pLoopUnit.doDamage(10, 80, en.eDamageUnholy)

# Elohim
	## Elegy of the Sheaim
		elif iProjectType == gc.getInfoTypeForString('PROJECT_HALLOWING_OF_THE_ELOHIM'):
			ePoisoned = gc.getInfoTypeForString('PROMOTION_POISONED')
			eDiseased = gc.getInfoTypeForString('PROMOTION_DISEASED')
			ePlagued = gc.getInfoTypeForString('PROMOTION_PLAGUED')
			eWithered = gc.getInfoTypeForString('PROMOTION_WITHERED')
			for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
				pLoopPlayer = gc.getPlayer(iLoopPlayer)
				if pLoopPlayer.isAlive():
					if pLoopPlayer.getCivilizationType() == en.eCivilizationElohim:
						py = PyPlayer(iLoopPlayer)
						for pLoopUnit in py.getUnitList():
							pLoopUnit.setHasPromotion(ePoisoned, False)
							pLoopUnit.setHasPromotion(eDiseased, False)
							pLoopUnit.setHasPromotion(ePlagued, False)
							pLoopUnit.setHasPromotion(eWithered, False)
							pLoopUnit.changeDamage(-5, PlayerTypes.NO_PLAYER)
# ent >>>
			iCount = min(CyGame().getProjectCreatedCount(gc.getInfoTypeForString('PROJECT_HALLOWING_OF_THE_ELOHIM')), 10)
			CyGame().changeGlobalCounter(-3 * iCount)
# ent <<<

# Droaum
	## Secret of evolution
		elif iProjectType == gc.getInfoTypeForString('PROJECT_SECRET_OF_EVOLUTION_DROAUM'):
			pPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_FALLOW'), True, TraitSourceTypes.TRAITSOURCE_OTHER_PERMANENT)

# Despiel
	## Life of the immortal
		elif iProjectType == gc.getInfoTypeForString('PROJECT_LIFE_OF_THE_IMMORTAL'):
			if not CyGame().isUnitClassMaxedOut(gc.getInfoTypeForString('UNITCLASS_YENOIAH'), 0):
				eDespielHero = 0
				eBlime = gc.getInfoTypeForString('UNITCLASS_BLIME')
				eNizar = gc.getInfoTypeForString('UNITCLASS_NIZAR')
				ePulufraus = gc.getInfoTypeForString('UNITCLASS_PULUFRAUS')
				eGogureg = gc.getInfoTypeForString('UNITCLASS_GOGUREG')
				iHeroExp = 20
				py = PyPlayer(iPlayer)
				apUnitList = py.getUnitList()
				for pUnit in apUnitList:
					eUnitClassType = pUnit.getUnitClassType()
					if eUnitClassType == eBlime:
						eDespielHero = gc.getInfoTypeForString('UNIT_BLIME_IMMORTAL')
					elif eUnitClassType == eNizar:
						eDespielHero = gc.getInfoTypeForString('UNIT_NIZAR_IMMORTAL')
					elif eUnitClassType == ePulufraus:
						eDespielHero = gc.getInfoTypeForString('UNIT_PULUFRAUS_IMMORTAL')
					elif eUnitClassType == eGogureg:
						eDespielHero = gc.getInfoTypeForString('UNIT_GOGUREG_IMMORTAL')
					else:
						continue
					iExp = pUnit.getExperience()
					pNewUnit = pPlayer.initUnit(eDespielHero, pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
					pNewUnit.setDamage(pUnit.getDamage(), PlayerTypes.NO_PLAYER)
					pNewUnit.setLevel(pUnit.getLevel())
					pNewUnit.changeExperience(iExp, -1, False, False, False)
					pNewUnit.convert(pUnit)
					if iExp > iHeroExp:
						iHeroExp = iExp
					break

				if eDespielHero != gc.getInfoTypeForString('UNIT_BLIME_IMMORTAL'):
					pNewUnit1 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_BLIME_IMMORTAL'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
					pNewUnit1.changeExperience(iHeroExp, -1, False, False, False)
				if eDespielHero != gc.getInfoTypeForString('UNIT_NIZAR_IMMORTAL'):
					pNewUnit2 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_NIZAR_IMMORTAL'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
					pNewUnit2.changeExperience(iHeroExp, -1, False, False, False)
				if eDespielHero != gc.getInfoTypeForString('UNIT_PULUFRAUS_IMMORTAL'):
					pNewUnit3 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_PULUFRAUS_IMMORTAL'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
					pNewUnit3.changeExperience(iHeroExp, -1, False, False, False)
				if eDespielHero != gc.getInfoTypeForString('UNIT_GOGUREG_IMMORTAL'):
					pNewUnit4 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_GOGUREG_IMMORTAL'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
					pNewUnit4.changeExperience(iHeroExp, -1, False, False, False)
				pNewUnit5 = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_YENOIAH'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
				pNewUnit5.setExperience(100, -1)

			eKaijin = gc.getInfoTypeForString('PROMOTION_KAIJIN_RACE')
			eStranger = gc.getInfoTypeForString('PROMOTION_STRANGER')
			for iPlotIndex in range (CyMap().numPlots()):
				pLoopPlot = CyMap().plotByIndex(iPlotIndex)
				if pLoopPlot.getOwner() == iPlayer:
					for iUnitIndex in xrange(pLoopPlot.getNumUnits()):
						pUnit = pLoopPlot.getUnit(iUnitIndex)
						if pUnit.isAlive():
							if pUnit.getRace() != eKaijin:
								if pUnit.isHasPromotion(eStranger) or CyGame().getSorenRandNum(100, "Degenerate Chanse") < 50:
									pUnit.setHasPromotion(eStranger, False)
									pUnit.setHasPromotion(eKaijin, True)

# Victory - Led to the end
	## May sickness
		elif iProjectType == gc.getInfoTypeForString('PROJECT_MAY_SICKNESS'):
			szButton = gc.getProjectInfo(iProjectType).getButton()
			eAcheron = gc.getInfoTypeForString('UNIT_ACHERON')
			for iTargetPlayer in xrange(gc.getMAX_PLAYERS()):
				pTargetPlayer = gc.getPlayer(iTargetPlayer)
				if pTargetPlayer.isAlive():
					if iTargetPlayer != iPlayer:
						for pyCity in PyPlayer(iTargetPlayer).getCityList() :
							pLoopCity = pyCity.GetCy()
							if CyGame().getSorenRandNum(1000, "May Sickness") >= 750:
								szMessage = CyTranslator().getText('TXT_KEY_EFFECT_MAY_SICKNESS', (pLoopCity.getNameKey(), ))
								CyInterface().addMessage(iTargetPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pLoopCity.getX(), pLoopCity.getY(), True, True)

								pLoopCityPlot = CyMap().plot(pLoopCity.getX(), pLoopCity.getY())
								for i in xrange(pLoopCityPlot.getNumUnits()):
									pUnit = pLoopCityPlot.getUnit(i)
									if pUnit.getUnitType() != eAcheron:
										iImmobileTimer = cyFlatValue(5, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getHurryConscriptAngerPercent(), True)
										pUnit.changeImmobileTimer(iImmobileTimer)
										pUnit.setFortifyTurns(0)

	## Black rain
		elif iProjectType == gc.getInfoTypeForString('PROJECT_BLACK_RAIN'):
			szButton = gc.getProjectInfo(iProjectType).getButton()
			for iTargetPlayer in xrange(gc.getMAX_PLAYERS()):
				if iTargetPlayer != iPlayer:
					pTargetPlayer = gc.getPlayer(iTargetPlayer)
					if pTargetPlayer.isAlive() and pTargetPlayer.getCivilizationType() != en.eCivilizationInfernal:
						for pyCity in PyPlayer(iTargetPlayer).getCityList() :
							pLoopCity = pyCity.GetCy()
							i = 3
							i += pLoopCity.getPopulation()
							i -= pLoopCity.totalGoodBuildingHealth()
							if i > 0:
								pLoopCity.changeEspionageHealthCounter(i)
								szMessage = CyTranslator().getText('TXT_KEY_EFFECT_BLACK_RAIN', (pLoopCity.getNameKey(), ))
								CyInterface().addMessage(iTargetPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pLoopCity.getX(), pLoopCity.getY(), True, True)

								pLoopCityPlot = CyMap().plot(pLoopCity.getX(), pLoopCity.getY())
								for i in xrange(pLoopCityPlot.getNumUnits()):
									pUnit = pLoopCityPlot.getUnit(i)
									if pUnit.isAlive():
										if pUnit.canFight():
											pUnit.doDamage(25, 100, en.eDamageDeath)

	## Return soul
		elif iProjectType == gc.getInfoTypeForString('PROJECT_RETURN_SOUL'):
			iNumPlayers = CyGame().countCivPlayersAlive()
			iCount = iNumPlayers + CyGame().getNumCities() // iNumPlayers
			eBarbarianUndead = gc.getInfoTypeForString('BARBARIAN_UNDEAD')
			pPlayer = gc.getPlayer(iPlayer)
			pNewUnit = -1
			eDiseasedCorpse = gc.getInfoTypeForString('UNIT_DISEASED_CORPSE')
			eSpectre = gc.getInfoTypeForString('UNIT_SPECTRE')
			eSkeleton = gc.getInfoTypeForString('UNIT_SKELETON')
			eStrong = gc.getInfoTypeForString('PROMOTION_STRONG')
			eSheutStone = gc.getInfoTypeForString('PROMOTION_SHEUT_STONE')
			for i in xrange(iCount):
				pNewUnit = cf.addBarbarianUnit(eDiseasedCorpse, eBarbarianUndead)
				if pNewUnit is not None:
					pNewUnit.setHasPromotion(eStrong, True)
					pNewUnit.changeImmobileTimer(1)
				pNewUnit = cf.addBarbarianUnit(eSpectre, eBarbarianUndead)
				if pNewUnit is not None:
					pNewUnit.setHasPromotion(eStrong, True)
					pNewUnit.setHasPromotion(eSheutStone, True)
					pNewUnit.changeImmobileTimer(1)
				pNewUnit = cf.addBarbarianUnit(eSkeleton, eBarbarianUndead)
				if pNewUnit is not None:
					pNewUnit.setHasPromotion(eStrong, True)
					pNewUnit.setHasPromotion(eSheutStone, True)
					pNewUnit.changeImmobileTimer(1)

			pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_BARBATOS_THE_LICH'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

			ePlayerTeam = gc.getPlayer(iPlayer).getTeam()
			pPlayerTeam = gc.getTeam(ePlayerTeam)

			eBarbTeam = gc.getBARBARIAN_TEAM()
			eUndeadTeam = eBarbTeam + eBarbarianUndead
##--------	Multiple Barbarians Ally: Modified by ent	--------##
##			pPlayerTeam.makePeace(eUndeadTeam)
			if not pPlayerTeam.isBarbarianAlly(eUndeadTeam):
	 			pPlayer.setBarbarianAlly(eUndeadTeam, True)
##--------	Multiple Barbarians Ally: End Modify			--------##

	## Disaster
		elif iProjectType == gc.getInfoTypeForString('PROJECT_DISASTER'):
			szButton = gc.getProjectInfo(iProjectType).getButton()
			eEffect = gc.getInfoTypeForString('EFFECT_AIR_SUMMON')
			for i in xrange (CyMap().numPlots()):
				pPlot = CyMap().plotByIndex(i)
				if not pPlot.isNone():
					if not pPlot.isCity():
						iTargetPlayer = pPlot.getOwner()
						if iTargetPlayer != iPlayer:
							if CyGame().getSorenRandNum(1000, "Disaster") < 50:
								eImprovement = pPlot.getImprovementType()
								if eImprovement != ImprovementTypes.NO_IMPROVEMENT and not gc.getImprovementInfo(eImprovement).isPermanent():
									pPlot.setImprovementType(gc.getImprovementInfo(eImprovement).getImprovementPillage());
									if pPlot.isVisibleToWatchingHuman():
										CyEngine().triggerEffect(eEffect, pPlot.getPoint())
									szMessage = CyTranslator().getText("TXT_KEY_EFFECT_DISASTER", (gc.getImprovementInfo(eImprovement).getDescription(), ))
									CyInterface().addMessage(iTargetPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pPlot.getX(), pPlot.getY(), True, True)

									for i in xrange(pPlot.getNumUnits()):
										pUnit = pPlot.getUnit(i)
										if pUnit.isAlive():
											if pUnit.canFight():
												pUnit.doDamage(25, 100, en.eDamageLightning)

			iNumPlayers = CyGame().countCivPlayersAlive()
			iCount = iNumPlayers + CyGame().getNumCities() // iNumPlayers
			eBarbarianOrc = gc.getInfoTypeForString('BARBARIAN_ORC')
			eAirElemental = gc.getInfoTypeForString('UNIT_AIR_ELEMENTAL')
			eEarthElemental = gc.getInfoTypeForString('UNIT_EARTH_ELEMENTAL')
			for i in xrange(iCount):
				pNewUnitAir = cf.addBarbarianUnit(eAirElemental, eBarbarianOrc)
				pNewUnitEarth = cf.addBarbarianUnit(eEarthElemental, eBarbarianOrc)

				if pNewUnitAir is not None:
					pNewUnitAir.setHasPromotion(en.ePromotionHeroicStrength, True)
					pNewUnitAir.setHasPromotion(en.ePromotionHeroicStrength2, True)
					pNewUnitAir.setHasPromotion(en.ePromotionHeroicDefense, True)
					pNewUnitAir.setHasPromotion(en.ePromotionHeroicDefense2, True)
					pNewUnitAir.setHasPromotion(en.ePromotionStrong, True)
					pNewUnitAir.setHasPromotion(en.ePromotionMusou, True)
					pNewUnitAir.changeImmobileTimer(1)

				if pNewUnitEarth is not None:
					pNewUnitEarth.setHasPromotion(en.ePromotionHeroicStrength, True)
					pNewUnitEarth.setHasPromotion(en.ePromotionHeroicStrength2, True)
					pNewUnitEarth.setHasPromotion(en.ePromotionHeroicDefense, True)
					pNewUnitEarth.setHasPromotion(en.ePromotionHeroicDefense2, True)
					pNewUnitEarth.setHasPromotion(en.ePromotionStrong, True)
					pNewUnitEarth.setHasPromotion(en.ePromotionMusou, True)
					pNewUnitEarth.changeImmobileTimer(1)

	## Festival of the berserkers
		elif iProjectType == gc.getInfoTypeForString('PROJECT_FESTIVAL_OF_THE_BERSERKERS'):
			szButton = gc.getProjectInfo(iProjectType).getButton()
			iEnraged = gc.getInfoTypeForString('PROMOTION_ENRAGED')
			iLand = gc.getInfoTypeForString('DOMAIN_LAND')
			eEffect = gc.getInfoTypeForString('EFFECT_CREATION')
			for iTargetPlayer in xrange(gc.getMAX_PLAYERS()):
				pTargetPlayer = gc.getPlayer(iTargetPlayer)
				if pTargetPlayer.isAlive():
					if iTargetPlayer != iPlayer:
						py = PyPlayer(iTargetPlayer)
						for pUnit in py.getUnitList():
							if pUnit.getDomainType() == iLand:
								if pUnit.isAlive():
									if not isWorldUnitClass(pUnit.getUnitClassType()):
										if pUnit.canFight():
											if CyGame().getSorenRandNum(1000, "Berserk") >= 850:
												pUnit.setHasPromotion(iEnraged, True)
												pPlot = pUnit.plot()
												if pPlot.isVisibleToWatchingHuman():
													CyEngine().triggerEffect(eEffect, pPlot.getPoint())
												szMessage = CyTranslator().getText('TXT_KEY_EFFECT_FESTIVAL_OF_THE_BERSERKERS', (pUnit.getNameKey(), ))
												CyInterface().addMessage(iTargetPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pUnit.getX(), pUnit.getY(), True, True)

			eBerserker = gc.getCivilizationInfo(pPlayer.getCivilizationType()).getCivilizationUnits(gc.getInfoTypeForString('UNITCLASS_BERSERKER'))
			if eBerserker == -1:
				classInfo = gc.getUnitClassInfo(gc.getInfoTypeForString('UNITCLASS_BERSERKER'))
				eBerserker = classInfo.getDefaultUnitIndex()
			pNewUnit = pPlayer.initUnit(eBerserker, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HERO'), True)
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STRONG'), True)
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STIGMATA'), True)
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CRAZED'), True)
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MAGIC_IMMUNE'), True)

	## Stigma the black
		elif iProjectType == gc.getInfoTypeForString('PROJECT_STIGMA_THE_BLACK'):
			szButton = gc.getProjectInfo(iProjectType).getButton()
			iPest = gc.getInfoTypeForString('PROMOTION_PEST')
			iLand = gc.getInfoTypeForString('DOMAIN_LAND')
			eEffect = gc.getInfoTypeForString('EFFECT_ENTROPY_SUMMON')
			for iTargetPlayer in xrange(gc.getMAX_PLAYERS()):
				pTargetPlayer = gc.getPlayer(iTargetPlayer)
				if pTargetPlayer.isAlive():
					if iTargetPlayer != iPlayer:
						py = PyPlayer(iTargetPlayer)
						for pUnit in py.getUnitList():
							if pUnit.getDomainType() == iLand:
								if pUnit.isAlive():
									if not isWorldUnitClass(pUnit.getUnitClassType()):
										if pUnit.canFight():
											if CyGame().getSorenRandNum(1000, "Pest") >= 900:
												pUnit.setHasPromotion(iPest, True)
												pPlot = pUnit.plot()
												if pPlot.isVisibleToWatchingHuman():
													CyEngine().triggerEffect(eEffect, pPlot.getPoint())
												szMessage = CyTranslator().getText('TXT_KEY_EFFECT_STIGMA_THE_BLACK', (pUnit.getNameKey(), ))
												CyInterface().addMessage(iTargetPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pUnit.getX(), pUnit.getY(), True, True)

			pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_BALOR'), pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HERO'), True)
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUE_CARRIER'), True)
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_RESERVOIRS_DROAUM'), True)
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STIGMATA'), True)
			pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MAGIC_IMMUNE'), True)

	## Dark gate
		elif iProjectType == gc.getInfoTypeForString('PROJECT_DARK_GATE'):
			iDarkgate = gc.getInfoTypeForString('IMPROVEMENT_DARKGATE')
			iDarkgate2 = gc.getInfoTypeForString('IMPROVEMENT_DARKGATE2')
			iHellfireChance = gc.getDefineINT('HELLFIRE_CHANCE')
			eEffect = gc.getInfoTypeForString('EFFECT_ENTROPY_SUMMON')
			for i in xrange (CyMap().numPlots()):
				pPlot = CyMap().plotByIndex(i)
				if not pPlot.isWater():
					if pPlot.getNumUnits() == 0:
						if not pPlot.isCity():
							if pPlot.isFlatlands():
								if pPlot.getBonusType(TeamTypes.NO_TEAM) == BonusTypes.NO_BONUS:
									if pPlot.isImpassable():
										continue
									iImprovement = pPlot.getImprovementType()
									if iImprovement != ImprovementTypes.NO_IMPROVEMENT:
										if gc.getImprovementInfo(iImprovement).isPermanent():
											continue
									if CyGame().getSorenRandNum(4000, "Hellfire") <= iHellfireChance:
										pPlot.setImprovementType(iDarkgate)
										if pPlot.isVisibleToWatchingHuman():
											CyEngine().triggerEffect(eEffect, pPlot.getPoint())
									elif CyGame().getSorenRandNum(10000, "Hellfire") <= iHellfireChance:
										pPlot.setImprovementType(iDarkgate2)
										if pPlot.isVisibleToWatchingHuman():
											CyEngine().triggerEffect(eEffect, pPlot.getPoint())

			eDragonliche = gc.getInfoTypeForString('UNIT_DRAGONLICHE')
			for pyCity in PyPlayer(iPlayer).getCityList() :
				pLoopCity = pyCity.GetCy()
				pNewUnit = pPlayer.initUnit(eDragonliche, pLoopCity.getX(), pLoopCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

# Rarna
	## Spread corruption
		elif iProjectType == gc.getInfoTypeForString('PROJECT_SPREAD_CORRUPTION'):
			eDemonBarbTeam = gc.getBARBARIAN_TEAM() + gc.getInfoTypeForString('BARBARIAN_DEMONS')
			eCitizenoftheDead = gc.getInfoTypeForString('BUILDING_CITIZEN_OF_THE_DEAD')
			for iRarnaPlayer in xrange(gc.getMAX_PLAYERS()):
				pRarnaPlayer = gc.getPlayer(iRarnaPlayer)
				if pRarnaPlayer.isAlive():
					if pRarnaPlayer.getCivilizationType() == en.eCivilizationRarna:
						pRarnaPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_STARVATION'), True, TraitSourceTypes.TRAITSOURCE_OTHER_PERMANENT)
						pRarnaPlayer.setAlignment(en.eAlignmentEvil)

						eRarnaTeam = pRarnaPlayer.getTeam()
						pRarnaTeam = gc.getTeam(eRarnaTeam)
##--------	Multiple Barbarians Ally: Modified by ent	--------##
##						pRarnaTeam.makePeace(eDemonBarbTeam)
						if not pRarnaTeam.isBarbarianAlly(eDemonBarbTeam):
				 			pRarnaPlayer.setBarbarianAlly(eDemonBarbTeam, True)
##--------	Multiple Barbarians Ally: End Modify			--------##

						py = PyPlayer(iRarnaPlayer)
						for pRarnaUnit in py.getUnitList():
							if pRarnaUnit.getRace() == en.eRaceAngel:
								if not isWorldUnitClass(pRarnaUnit.getUnitClassType()):
									pRarnaUnit.setHasPromotion(en.eRaceDemon, True)

						for pyCity in py.getCityList():
							pRarnaCity = pyCity.GetCy()
							pRarnaCity.setNumRealBuilding(eCitizenoftheDead, 1)

	## Fire inheritance
		elif iProjectType == gc.getInfoTypeForString('PROJECT_FIRE_INHERITANCE'):
			eUndeadBarbTeam = gc.getBARBARIAN_TEAM() + gc.getInfoTypeForString('BARBARIAN_UNDEAD')
			eImmuneFire = gc.getInfoTypeForString('PROMOTION_IMMUNE_FIRE')
			eEffect = gc.getInfoTypeForString('EFFECT_PILLAR_OF_FIRE')
			for iRarnaPlayer in xrange(gc.getMAX_PLAYERS()):
				pRarnaPlayer = gc.getPlayer(iRarnaPlayer)
				if pRarnaPlayer.isAlive():
					if pRarnaPlayer.getCivilizationType() == en.eCivilizationRarna:
						pRarnaPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_BARBARIAN'), True, TraitSourceTypes.TRAITSOURCE_OTHER_PERMANENT)
						pRarnaPlayer.setAlignment(en.eAlignmentNeutral)

						eRarnaTeam = pRarnaPlayer.getTeam()
						pRarnaTeam = gc.getTeam(eRarnaTeam)
##--------	Multiple Barbarians Ally: Modified by ent	--------##
##						pRarnaTeam.makePeace(eUndeadBarbTeam)
						if not pRarnaTeam.isBarbarianAlly(eUndeadBarbTeam):
				 			pRarnaPlayer.setBarbarianAlly(eUndeadBarbTeam, True)
##--------	Multiple Barbarians Ally: End Modify			--------##

						py = PyPlayer(iRarnaPlayer)
						for pRarnaUnit in py.getUnitList():
							pRarnaUnit.setHasPromotion(eImmuneFire, True)

						for iPlotIndex in range (CyMap().numPlots()):
							pLoopPlot = CyMap().plotByIndex(iPlotIndex)
							if pLoopPlot.getOwner() == iRarnaPlayer:
								if pLoopPlot.isWater() or pLoopPlot.isImpassable():
									continue
								eFeature = pLoopPlot.getFeatureType()
								if eFeature != FeatureTypes.NO_FEATURE and gc.getFeatureInfo(eFeature).isFlammable():
									pLoopPlot.setFeatureType(en.eFeatureFlames, 0)

					else:
						py = PyPlayer(iRarnaPlayer)
						for pUnit in py.getUnitList():
							pUnit.doDamage(30, 90, en.eDamageFire)
							pPlot = pUnit.plot()
							if not pPlot.isCity():
								if pPlot.isVisibleToWatchingHuman():
									CyEngine().triggerEffect(eEffect, pPlot.getPoint())

	## Princess of darkness
		elif iProjectType == gc.getInfoTypeForString('PROJECT_PRINCESS_OF_DARKNESS'):
			eUnitMichael = gc.getInfoTypeForString('UNIT_MICHAEL')
			eCitizenoftheDead = gc.getInfoTypeForString('BUILDING_CITIZEN_OF_THE_DEAD')
			eImmortalCitizen = gc.getInfoTypeForString('BUILDING_IMMORTAL_CITIZEN')
			eAbyss = gc.getInfoTypeForString('BUILDING_ABYSS')
			eEffect = gc.getInfoTypeForString('EFFECT_PIT_BEAST_SUMMON')
			for iRarnaPlayer in xrange(gc.getMAX_PLAYERS()):
				pRarnaPlayer = gc.getPlayer(iRarnaPlayer)
				if pRarnaPlayer.isAlive():
					if pRarnaPlayer.getCivilizationType() == en.eCivilizationRarna:
						pRarnaPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_FALLOW'), True, TraitSourceTypes.TRAITSOURCE_OTHER_PERMANENT)
						pRarnaPlayer.setHasTraitWithSource(gc.getInfoTypeForString('TRAIT_DEATHTOUCHED'), True, TraitSourceTypes.TRAITSOURCE_OTHER_PERMANENT)

						py = PyPlayer(iRarnaPlayer)
						for pRarnaUnit in py.getUnitList():
							pRarnaUnit.setHasPromotion(en.ePromotionImmortal, True)

							if pRarnaUnit.getUnitType() == eUnitMichael:
								pRarnaUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_UNHOLY_TAINT'), True)
								pRarnaUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FEAR'), True)
								pRarnaUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STIGMATA'), True)

						if not CyGame().isUnitClassMaxedOut(gc.getInfoTypeForString('UNITCLASS_MICHAEL'), 0):
							pCapital = pPlayer.getCapitalCity()
							pNewUnit = pPlayer.initUnit(eUnitMichael, pCapital.getX(), pCapital.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
							pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_UNHOLY_TAINT'), True)
							pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FEAR'), True)
							pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STIGMATA'), True)
							pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IMMORTAL'), True)

						for pyCity in py.getCityList():
							pRarnaCity = pyCity.GetCy()
							pRarnaCity.setNumRealBuilding(eCitizenoftheDead, 0)
							pRarnaCity.setNumRealBuilding(eImmortalCitizen, 1)
							pRarnaCity.setNumRealBuilding(eAbyss, 1)

					else:
						py = PyPlayer(iRarnaPlayer)
						for pUnit in py.getUnitList():
							pUnit.doDamage(70, 90, en.eDamageUnholy)
							pPlot = pUnit.plot()
							if not pPlot.isCity():
								if pPlot.isVisibleToWatchingHuman():
									CyEngine().triggerEffect(eEffect, pPlot.getPoint())

	## Death pact
		elif iProjectType in (	gc.getInfoTypeForString('PROJECT_DEATH_PACT_1'),
								gc.getInfoTypeForString('PROJECT_DEATH_PACT_2'),
								gc.getInfoTypeForString('PROJECT_DEATH_PACT_3'),
								gc.getInfoTypeForString('PROJECT_DEATH_PACT_4'),
								gc.getInfoTypeForString('PROJECT_DEATH_PACT_5')		):
			cf.ConvertLifeForce(pCity)

	## Death Ritual
		elif iProjectType == gc.getInfoTypeForString('PROJECT_DEATH_RITUAL'):
			pPlayer.changeGuildPlusCounter(51, 1)
			for pyCity in PyPlayer(iPlayer).getCityList():
				pLoopCity = pyCity.GetCy()
				pLoopCity.changePopulation(1)

# Kaijin <<<

	def onSelectionGroupPushMission(self, argsList):
		'selection group mission'
		eOwner = argsList[0]
		eMission = argsList[1]
		iNumUnits = argsList[2]
		listUnitIds = argsList[3]

		if (not self.__LOG_PUSH_MISSION):
			return
		if pHeadUnit:
			CvUtil.pyPrint("Selection Group pushed mission %d" %(eMission))

	def onUnitMove(self, argsList):
		'unit move'
		pPlot, pUnit, pOldPlot = argsList
		player = PyPlayer(pUnit.getOwner())
		unitInfo = PyInfo.UnitInfo(pUnit.getUnitType())
		if (not self.__LOG_MOVEMENT):
			return
		if player and unitInfo:
			CvUtil.pyPrint('Player %d Civilization %s unit %s is moving to %d, %d'
				%(player.getID(), player.getCivilizationName(), unitInfo.getDescription(),
				pUnit.getX(), pUnit.getY()))

	def onUnitSetXY(self, argsList):
		'units xy coords set manually'
		pPlot, pUnit = argsList
		player = PyPlayer(pUnit.getOwner())
		unitInfo = PyInfo.UnitInfo(pUnit.getUnitType())
		if (not self.__LOG_MOVEMENT):
			return

	def onUnitCreated(self, argsList):
		'Unit Completed'
		unit = argsList[0]
		player = PyPlayer(unit.getOwner())
		pPlayer = gc.getPlayer(unit.getOwner())

# Kaijin >>>
		eUnitType = unit.getUnitType()
		eUnitClassType = unit.getUnitClassType()
		eCiv = pPlayer.getCivilizationType()
	## Magic Master
		if unit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ADEPT'):
			cf.setArcanePromotionFromRedundantManas(unit)
# Kaijin <<<

		if unit.getRace() == gc.getInfoTypeForString('PROMOTION_ELEMENTAL'):
			if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_TOWER_OF_THE_ELEMENTS')) > 0:
				unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STRONG'), True)

		elif unit.getRace() == gc.getInfoTypeForString('PROMOTION_UNDEAD'):
			if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_TOWER_OF_NECROMANCY')) > 0:
				unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STRONG'), True)

# ent - Spread Cult of the Dragon >>>
		elif unit.getRace() == gc.getInfoTypeForString('PROMOTION_DRAGON'):
			pCity = unit.plot().getWorkingCity()
			if not pCity.isNone():
				eReligionCultoftheDragon = gc.getInfoTypeForString('RELIGION_CULT_OF_THE_DRAGON')
				if not pCity.isHasReligion(eReligionCultoftheDragon):
					pCity.setHasReligion(eReligionCultoftheDragon, True, True, True)
					if not CyGame().isReligionFounded(eReligionCultoftheDragon):
						CyGame().setHolyCity(eReligionCultoftheDragon, pCity, True)
# ent <<<

##--------	Better AI: Added by Denev	--------##
		eCouncil = gc.getInfoTypeForString('RELIGION_COUNCIL_OF_ESUS')
		if unit.getReligion() == eCouncil:
# ent >>>
#			unit.setUnitAIType(UnitAITypes.UNITAI_MISSIONARY)
			if pPlayer.hasHolyCity(eCouncil) or pPlayer.getStateReligion() == eCouncil:
				unit.setUnitAIType(UnitAITypes.UNITAI_MISSIONARY)
# ent <<<
##--------	Better AI: End Add			--------##

##--------	Female Great People: Added by Denev	--------##
#		if unit.getSpecialUnitType() == gc.getInfoTypeForString('SPECIALUNIT_PEOPLE'):
		if eUnitClassType in (	gc.getInfoTypeForString('UNITCLASS_ARTIST'), 
										gc.getInfoTypeForString('UNITCLASS_COMMANDER'), 
										gc.getInfoTypeForString('UNITCLASS_ENGINEER'), 
										gc.getInfoTypeForString('UNITCLASS_MERCHANT'), 
										gc.getInfoTypeForString('UNITCLASS_PROPHET'), 
										gc.getInfoTypeForString('UNITCLASS_SCIENTIST'), 
										gc.getInfoTypeForString('UNITCLASS_GARDENER')		):
			bFemale = argsList[1]
#			bPlural = argsList[2]
			if bFemale:
				"""
				if unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_ARTIST'):
					if CyGame().getSorenRandNum(2, "Female Great People") == 0:
						unit.setUnitArtStyleType(gc.getInfoTypeForString('ART_DEF_UNIT_FEMALE_ARTIST'))
					else:
						unit.setUnitArtStyleType(gc.getInfoTypeForString('ART_DEF_UNIT_FEMALE_ARTIST_MODERN'))
				elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_COMMANDER'):
					if CyGame().getSorenRandNum(2, "Female Great People") == 0:
						unit.setUnitArtStyleType(gc.getInfoTypeForString('ART_DEF_UNIT_FEMALE_COMMANDER_ANCIENT'))
					else:
						unit.setUnitArtStyleType(gc.getInfoTypeForString('ART_DEF_UNIT_FEMALE_COMMANDER_MEDIEVAL'))
						unit.setUnitArtStyleType(gc.getInfoTypeForString('ART_DEF_UNIT_FEMALE_ARTIST_MODERN'))
				elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_ENGINEER'):
					unit.setUnitArtStyleType(gc.getInfoTypeForString('ART_DEF_UNIT_FEMALE_ENGINEER'))
				elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_MERCHANT'):
					unit.setUnitArtStyleType(gc.getInfoTypeForString('ART_DEF_UNIT_FEMALE_MERCHANT'))
				elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_PROPHET'):
					unit.setUnitArtStyleType(gc.getInfoTypeForString('ART_DEF_UNIT_FEMALE_PROPHET'))
				elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_SCIENTIST'):
					unit.setUnitArtStyleType(gc.getInfoTypeForString('ART_DEF_UNIT_FEMALE_SCIENTIST'))
				"""
				if CyGame().getElapsedGameTurns() % 2 == 0:
					unit.setUnitArtStyleType(gc.getInfoTypeForString('UNIT_ARTSTYLE_FEMALE'))
				else:
					unit.setUnitArtStyleType(gc.getInfoTypeForString('UNIT_ARTSTYLE_FEMALE2'))

				unit.reloadEntity()
##--------	Female Great People: End Add			--------##

# Kaijin >>>
		iTeam = pPlayer.getTeam()
		eTeam = gc.getTeam(iTeam)

	## Ys
		if eCiv == gc.getInfoTypeForString('CIVILIZATION_YS'):
			if not unit.isSummoned():
				if unit.canFight():
# ent >>>
#					if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_FAST_CHANT')):
					def isUniqueCivUnit():
						if eCiv == gc.getUnitInfo(eUnitType).getPrereqCiv():
							return True
						if eUnitType == gc.getUnitClassInfo(eUnitClassType).getDefaultUnitIndex():
							return False
						if eUnitType == gc.getCivilizationInfo(eCiv).getCivilizationUnits(eUnitClassType):
							return True
						return False

					if unit.isFastChant() and isUniqueCivUnit():
# ent <<<
						liSelectedPromotion = []

						liChosenPromRank1 = []
						if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING1')):
							liPromRank1 = [	gc.getInfoTypeForString('PROMOTION_AIR1'),
												gc.getInfoTypeForString('PROMOTION_EARTH1'),
												gc.getInfoTypeForString('PROMOTION_FIRE1'),
												gc.getInfoTypeForString('PROMOTION_WATER1'),
												gc.getInfoTypeForString('PROMOTION_BODY1'),
												gc.getInfoTypeForString('PROMOTION_ENCHANTMENT1'),
												gc.getInfoTypeForString('PROMOTION_MIND1'),
												gc.getInfoTypeForString('PROMOTION_NATURE1'),
												gc.getInfoTypeForString('PROMOTION_CHAOS1'),
												gc.getInfoTypeForString('PROMOTION_DEATH1'),
												gc.getInfoTypeForString('PROMOTION_ENTROPY1'),
												gc.getInfoTypeForString('PROMOTION_SHADOW1'),
												gc.getInfoTypeForString('PROMOTION_LAW1'),
												gc.getInfoTypeForString('PROMOTION_LIFE1'),
												gc.getInfoTypeForString('PROMOTION_SPIRIT1'),
												gc.getInfoTypeForString('PROMOTION_SUN1'),
												gc.getInfoTypeForString('PROMOTION_METAMAGIC1'),
												gc.getInfoTypeForString('PROMOTION_ICE1')			]

							for iPromotion in liPromRank1:
								if not unit.isHasPromotion(iPromotion):
									liChosenPromRank1.append(iPromotion)
							liChosenPromRank1.sort()
							liSelectedPromotion.append(liChosenPromRank1.pop( CyGame().getSorenRandNum(len(liChosenPromRank1), "Ark of napishtim") ))
							liSelectedPromotion.sort()

						liChosenPromRank2 = []
						if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING2')):
							liPromRank2 = [	gc.getInfoTypeForString('PROMOTION_AIR2'),
												gc.getInfoTypeForString('PROMOTION_EARTH2'),
												gc.getInfoTypeForString('PROMOTION_FIRE2'),
												gc.getInfoTypeForString('PROMOTION_WATER2'),
												gc.getInfoTypeForString('PROMOTION_BODY2'),
												gc.getInfoTypeForString('PROMOTION_ENCHANTMENT2'),
												gc.getInfoTypeForString('PROMOTION_MIND2'),
												gc.getInfoTypeForString('PROMOTION_NATURE2'),
												gc.getInfoTypeForString('PROMOTION_CHAOS2'),
												gc.getInfoTypeForString('PROMOTION_DEATH2'),
												gc.getInfoTypeForString('PROMOTION_ENTROPY2'),
												gc.getInfoTypeForString('PROMOTION_SHADOW2'),
												gc.getInfoTypeForString('PROMOTION_LAW2'),
												gc.getInfoTypeForString('PROMOTION_LIFE2'),
												gc.getInfoTypeForString('PROMOTION_SPIRIT2'),
												gc.getInfoTypeForString('PROMOTION_SUN2'),
												gc.getInfoTypeForString('PROMOTION_METAMAGIC2'),
												gc.getInfoTypeForString('PROMOTION_ICE2')			]

							for iPromotion in liPromRank2:
								if not unit.isHasPromotion(iPromotion):
									liChosenPromRank2.append(iPromotion)
							liChosenPromRank2.sort()
							liSelectedPromotion.append(liChosenPromRank2.pop( CyGame().getSorenRandNum(len(liChosenPromRank2), "Ark of napishtim") ))
							liSelectedPromotion.sort()

						liChosenPromRank3 = []
						if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING3')):
							liPromRank3 = [	gc.getInfoTypeForString('PROMOTION_AIR3'),
												gc.getInfoTypeForString('PROMOTION_EARTH3'),
												gc.getInfoTypeForString('PROMOTION_FIRE3'),
												gc.getInfoTypeForString('PROMOTION_WATER3'),
												gc.getInfoTypeForString('PROMOTION_BODY3'),
												gc.getInfoTypeForString('PROMOTION_ENCHANTMENT3'),
												gc.getInfoTypeForString('PROMOTION_MIND3'),
												gc.getInfoTypeForString('PROMOTION_NATURE3'),
												gc.getInfoTypeForString('PROMOTION_CHAOS3'),
												gc.getInfoTypeForString('PROMOTION_DEATH3'),
												gc.getInfoTypeForString('PROMOTION_ENTROPY3'),
												gc.getInfoTypeForString('PROMOTION_SHADOW3'),
												gc.getInfoTypeForString('PROMOTION_LAW3'),
												gc.getInfoTypeForString('PROMOTION_LIFE3'),
												gc.getInfoTypeForString('PROMOTION_SPIRIT3'),
												gc.getInfoTypeForString('PROMOTION_SUN3'),
												gc.getInfoTypeForString('PROMOTION_METAMAGIC3'),
												gc.getInfoTypeForString('PROMOTION_ICE3')			]

							for iPromotion in liPromRank3:
								if not unit.isHasPromotion(iPromotion):
									liChosenPromRank3.append(iPromotion)
							liChosenPromRank3.sort()
							liSelectedPromotion.append(liChosenPromRank3.pop( CyGame().getSorenRandNum(len(liChosenPromRank3), "Ark of napishtim") ))
							liSelectedPromotion.sort()

						if len(liSelectedPromotion) > 0:
							for iSelectedPromotion in liSelectedPromotion:
								if not unit.isHasPromotion(iSelectedPromotion):
									unit.setHasPromotion(iSelectedPromotion, True)

	## Sicons
		if eCiv == gc.getInfoTypeForString('CIVILIZATION_SCIONS'):
			## Disable "Undead"
##--------	Advanced Rules: Modified by ent
#			if eUnitType in (	gc.getInfoTypeForString('UNIT_WARRIOR'), 
			if eUnitType in (	gc.getInfoTypeForString('UNIT_CENTENI'), 
##--------	Advanced Rules: End Modify
								gc.getInfoTypeForString('UNIT_KORRINA_RED'), 
								gc.getInfoTypeForString('UNIT_KORRINA')	):
				unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_UNDEAD'), False)

	## Megisus
		## Strengthening of Living armor by Spring of Ghnuke.
		if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_SPRING_OF_GHNUKE')) > 0:
			if eUnitType == gc.getInfoTypeForString('UNIT_LIVING_ARMOR'):
				unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BARRAGE1'), True)

		## Strengthening of Living armor by Cercle of Monsoon.
		if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_CIRCLE_OF_MONSOON')) > 0:
			if eUnitType == gc.getInfoTypeForString('UNIT_LIVING_ARMOR'):
				unit.changeCombatStr(1)

	## Barbarian - Heroes join random artifact.
		if eUnitType in (	gc.getInfoTypeForString('UNIT_TUMTUM'), 
									gc.getInfoTypeForString('UNIT_GURID'), 
									gc.getInfoTypeForString('UNIT_MARGALARD'), 
									gc.getInfoTypeForString('UNIT_MOKKA'), 
									gc.getInfoTypeForString('UNIT_OSE'), 
									gc.getInfoTypeForString('UNIT_TEZCATLIPOCA'), 
									gc.getInfoTypeForString('UNIT_INUGAMI'), 
									gc.getInfoTypeForString('UNIT_CERYNEIAN_HIND'), 
									gc.getInfoTypeForString('UNIT_AZATHOTH'), 
									gc.getInfoTypeForString('UNIT_LEMEGETON'), 
									gc.getInfoTypeForString('UNIT_ALEXANDER')	):
			liEquipment = [	gc.getInfoTypeForString('PROMOTION_MUTATION_POTION'),
							gc.getInfoTypeForString('PROMOTION_HEART_AMULET'),
							gc.getInfoTypeForString('PROMOTION_SWIFT_BOOTS'),
							gc.getInfoTypeForString('PROMOTION_TRAVELLERS_CLOAK'),
							gc.getInfoTypeForString('PROMOTION_RING_OF_PERCEPTION'),
							gc.getInfoTypeForString('PROMOTION_RING_OF_STRIKING'),
							gc.getInfoTypeForString('PROMOTION_COMPELLING_JEWEL'),
							gc.getInfoTypeForString('PROMOTION_STARVATION_HELM'),
							gc.getInfoTypeForString('PROMOTION_HAUBERK_OF_ABJURATION'),
							gc.getInfoTypeForString('PROMOTION_BUG_DA_RAKE'),
							gc.getInfoTypeForString('PROMOTION_HEALING_SALVE'),
							gc.getInfoTypeForString('PROMOTION_JADE_TORC'),
							gc.getInfoTypeForString('PROMOTION_POTION_OF_INVISIBILITY'),
							gc.getInfoTypeForString('PROMOTION_POTION_OF_RESTORATION'),
							gc.getInfoTypeForString('PROMOTION_ROD_OF_WINDS'),
							gc.getInfoTypeForString('PROMOTION_SCORCHED_STAFF'),
							gc.getInfoTypeForString('PROMOTION_TIMOR_MASK')				]
			iChosenEquipment = liEquipment.pop( CyGame().getSorenRandNum(len(liEquipment), "Random artifacts") )
			unit.setHasPromotion(iChosenEquipment, True)

	## Barbarian - Converted to pirate the Barbarian naval units.
		if pPlayer.isBarbarian():
			if eCiv != gc.getInfoTypeForString('CIVILIZATION_PIRATES'):
				if not isWorldUnitClass(eUnitClassType):
					if not unit.isHiddenNationality():
						if unit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_NAVAL'):
							ePiratesBarbarian = gc.getInfoTypeForString('BARBARIAN_PIRATES') + gc.getBARBARIAN_PLAYER()
							pPiratesBarbarian = gc.getPlayer(ePiratesBarbarian)
							pTargetPlot = cf.findAdjacentClearPlot(ePiratesBarbarian, unit.getX(), unit.getY(), True, True)
							if pTargetPlot is not None:
								pNewUnit = pPiratesBarbarian.initSkeletalUnit(eUnitType, pTargetPlot.getX(), pTargetPlot.getY(), unit.getUnitAIType())
								pNewUnit.convert(unit)
								pNewUnit.setUnitAIType(UnitAITypes.UNITAI_PIRATE_SEA)

	## Almighty - Unit gain experience points for free.
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_ALMIGHTY')):
			if unit.canFight():
				unit.changeExperience(2, -1, False, False, False)

	## General
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_GENERAL')):
			if (gc.getGame().getElapsedGameTurns() == 0):
				if unit.canFight():
					iPromotion = 1 + CyGame().getSorenRandNum(2, "Trait General")
					unit.changeFreePromotionPick(iPromotion)

	## Kaijin - Dark Magic
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_BLACK_MAGIC')):
			if CyGame().getSorenRandNum(100, "Despiel Sense") < 20:
				if unit.canFight():
					iTier = gc.getUnitInfo(eUnitType).getTier()
					if iTier >= 2:
						unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DARK_MAGIC1'), True)
					if iTier >= 3:
						unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DARK_MAGIC2'), True)
					if iTier >= 4:
						unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DARK_MAGIC3'), True)

	## Undead - Unit is given Reservoir and Undead.
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_UNDEAD')):
			if (gc.getGame().getElapsedGameTurns() == 0):
				if unit.isAlive():
					if unit.canFight():
						if not isWorldUnitClass(eUnitClassType):
							if not eUnitClassType in (gc.getInfoTypeForString('UNITCLASS_SETTLER'), gc.getInfoTypeForString('UNITCLASS_WORKER')):
								unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_UNDEAD'), True)
								unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_RESERVOIRS_DROAUM'), True)

	## Fool
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_UNENLIGHTENED')):
			if CyGame().getSorenRandNum(1000, "Fool") <= 1:
				cf.doTraitFool(unit.getOwner())

	## Muppet - Initialization of Experience Points
		if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MUPPET')):
			unit.setExperience(0, -1)

	## Game option "Legend of the Heroes"
		if CyGame().isOption(gc.getInfoTypeForString('GAMEOPTION_MODDER_2')):
			if isWorldUnitClass(eUnitClassType) or unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_HERO')):
				if unit.getExperience() < 100:
					unit.setExperience(100, -1)

		if pPlayer.isHuman():
		# More Events mod starts#
			if pPlayer.getGuildPlusCounter(1) == 0:
				if eUnitClassType == gc.getInfoTypeForString('UNITCLASS_GELA'):
					if not eCiv == gc.getInfoTypeForString('CIVILIZATION_INFERNAL'):
						pPlayer.setGuildPlusCounter(1, 1)
						iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(),'EVENTTRIGGER_GELA')
						triggerData = pPlayer.initTriggeredData(iEvent, True, -1, -1, -1, unit.getOwner(), -1, -1, -1, -1, -1)
		#More Events mod ends #

	#POPUP_MOD ADD START
		if( CyGame().getAIAutoPlay() == 0 ):
			if isWorldUnitClass(eUnitClassType):
				WorldUnitPopup.process(unit, player)
	#POPUP_MOD ADD END

# Kaijin <<<
	
		if CyGame().getWBMapScript():
			sf.onUnitCreated(unit)

		if (not self.__LOG_UNITBUILD):
			return

	def onUnitBuilt(self, argsList):
		'Unit Completed'
		city = argsList[0]
		unit = argsList[1]
		player = PyPlayer(city.getOwner())
		pPlayer = gc.getPlayer(unit.getOwner())

##--------	Unofficial Bug Fix: Deleted by Denev	--------##
#		iFreeProm = unit.getFreePromotionPick()
##--------	Unofficial Bug Fix: End Delete			--------##

		if unit.getUnitType() == gc.getInfoTypeForString('UNIT_BEAST_OF_AGARES'):
# Kaijin >>> for Fallow
#			if city.getCivilizationType() != en.eCivilizationInfernal:
			if not pPlayer.isIgnoreFood():
# Kaijin <<<
				iPop = max(1, city.getPopulation() - 4)
				city.setPopulation(iPop)
# Kaijin >>> for Demonic Civilizations
			if city.getCivilizationType() != gc.getInfoTypeForString('CIVILIZATION_INFERNAL') and city.getCivilizationType() != gc.getInfoTypeForString('CIVILIZATION_DARK'):
# Kaijin <<<
				iOccupationTimer = cyFlatValue(4, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getHurryConscriptAngerPercent(), True)
				city.setOccupationTimer(iOccupationTimer)

				"""
##--------	Unofficial Bug Fix: Added by Denev		--------##
# For the Horde! world spell can not convert Disciple of Acheron or Son of the Inferno.
		elif unit.getUnitType() in (gc.getInfoTypeForString('UNIT_DISCIPLE_OF_ACHERON'), gc.getInfoTypeForString('UNIT_SON_OF_THE_INFERNO')):
			unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ORC'), False)
##--------	Unofficial Bug Fix: End Add				--------##
				"""

##--------	Unofficial Bug Fix: Deleted by Denev	--------##
		"Moved to self.applyBuildEffects"
		"""
		if city.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_CHANCEL_OF_GUARDIANS')) > 0:
			if CyGame().getSorenRandNum(100, "Chancel of Guardians") < 20:
				unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEFENSIVE'), True)

		if (city.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_CAVE_OF_ANCESTORS')) > 0 and unit.getUnitCombatType() == (gc.getInfoTypeForString('UNITCOMBAT_ADEPT'))):
			i = 0
			for iBonus in xrange(gc.getNumBonusInfos()):
				if gc.getBonusInfo(iBonus).getBonusClassType() == gc.getInfoTypeForString('BONUSCLASS_MANA'):
					if city.hasBonus(iBonus):
						i = i + 1
			if i >= 1:
				unit.changeExperience(i, -1, False, False, False)

		if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_GOLEM')):
			if city.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_BLASTING_WORKSHOP')) > 0:
				unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FIRE2'), True)
			if city.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_PALLENS_ENGINE')) > 0:
				unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PERFECT_SIGHT'), True)
			if city.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_ADULARIA_CHAMBER')) > 0:
				unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HIDDEN'), True)

		if city.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_ASYLUM')) > 0:
			if unit.isAlive():
				if isWorldUnitClass(unit.getUnitClassType()) == False:
					if CyGame().getSorenRandNum(100, "Bob") <= 10:
						unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CRAZED'), True)
						unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENRAGED'), True)
		"""
##--------	Unofficial Bug Fix: End Delete			--------##

		if unit.getUnitType() == gc.getInfoTypeForString('UNIT_ACHERON'):
#			unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HELD'), True)
			city.setNumRealBuilding(gc.getInfoTypeForString('BUILDING_DRAGONS_HORDE'), 1)
# Kaijin CultOfTheDragon >>>
			"""
			"Moved to onUnitCreated"
			if not CyGame().isReligionFounded(gc.getInfoTypeForString('RELIGION_CULT_OF_THE_DRAGON')):
				city.setHasReligion(gc.getInfoTypeForString('RELIGION_CULT_OF_THE_DRAGON'), True, True, True)
				CyGame().setHolyCity(gc.getInfoTypeForString('RELIGION_CULT_OF_THE_DRAGON'), city, True)
			"""
# Kaijin CultOfTheDragon <<<
			iX = city.getX()
			iY = city.getY()
			for iDirection in xrange(DirectionTypes.NUM_DIRECTION_TYPES):
				pLoopPlot = plotDirection(iX, iY, DirectionTypes(iDirection))
				if not pLoopPlot.isNone():
					iFeature = pLoopPlot.getFeatureType()
					if iFeature != FeatureTypes.NO_FEATURE and gc.getFeatureInfo(iFeature).isFlammable():
						pLoopPlot.setFeatureType(gc.getDefineINT('FLAMES_FEATURE'), -1)
						iImprovement = pLoopPlot.getImprovementType()
						if iImprovement != ImprovementTypes.NO_IMPROVEMENT and not gc.getImprovementInfo(iImprovement).isPermanent():
							pLoopPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
##--------	Merging Better BtS AI: Modified by Denev	--------##
#			cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_ACHERON_CREATION", ()), str(gc.getUnitInfo(unit.getUnitType()).getImage()))
			if( CyGame().getAIAutoPlay() == 0 ):
				cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_ACHERON_CREATION", ()), str(gc.getUnitInfo(unit.getUnitType()).getImage()))
##--------	Merging Better BtS AI: End Modify			--------##

##--------	Unofficial Bug Fix: Deleted by Denev	--------##
		"Moved to self.applyBuildEffects"
		"""
		if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DWARF')):
			if city.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_BREWERY')) > 0:
				unit.changeExperience(2, -1, False, False, False)

		if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON')):
			if city.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_DEMONS_ALTAR')) > 0:
				unit.changeExperience(2, -1, False, False, False)
		"""
##--------	Unofficial Bug Fix: End Delete			--------##

##--------	Unofficial Bug Fix: Deleted by Denev	--------##
		"""
		if unit.getFreePromotionPick() < iFreeProm:
			unit.changeFreePromotionPick(iFreeProm - unit.getFreePromotionPick())
		"""
##--------	Unofficial Bug Fix: End Delete			--------##

		if city.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_WARRENS')):
			if not isWorldUnitClass(unit.getUnitClassType()):
				if not isNationalUnitClass(unit.getUnitClassType()):
##--------	Unofficial Bug Fix: Modified by Denev	--------##
					"""
					if unit.getUnitCombatType() != gc.getInfoTypeForString('UNITCOMBAT_SIEGE'):
						if unit.getUnitCombatType() != gc.getInfoTypeForString('UNITCOMBAT_NAVAL'):
					"""
#					if not unit.isMechUnit():
# Kaijin OAC >>>
#					if unit.getRace() in (gc.getInfoTypeForString('PROMOTION_ORC'), gc.getInfoTypeForString('PROMOTION_OGRE')):
					if unit.getRace() in (gc.getInfoTypeForString('PROMOTION_ORC'), gc.getInfoTypeForString('PROMOTION_OGRE'), gc.getInfoTypeForString('PROMOTION_GOBLIN')):
# Kaijin OAC <<<
##--------	Unofficial Bug Fix: End Modify			--------##
							pNewUnit = pPlayer.initUnit(unit.getUnitType(), city.getX(), city.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
							city.applyBuildEffects(pNewUnit)

##--------	Advanced Rules: Added by Denev	--------##
		if pPlayer.isBarbarian():
			pBestDefender = city.plot().getBestDefender(city.getOwner(), PlayerTypes.NO_PLAYER, pPlayer.getUnit(-1), False, False, False)
			if gc.getUnitInfo(pBestDefender.getUnitType()).getTier() < 2:
				pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ARCHER'), city.getX(), city.getY(), UnitAITypes.UNITAI_CITY_DEFENSE, DirectionTypes.DIRECTION_SOUTH)
				pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAK'), True)
##--------	Advanced Rules: End Add			--------##

		CvAdvisorUtils.unitBuiltFeats(city, unit)

# Kaijin >>>
## Units
	## Freak
		if unit.getUnitType() == gc.getInfoTypeForString('UNIT_FREAK'):
			iCount = CyGame().getSorenRandNum(2, 'the number of effects') + 2
			liPromotion = [	gc.getInfoTypeForString('PROMOTION_AMPHIBIOUS'),
							gc.getInfoTypeForString('PROMOTION_COLD_RESISTANCE'),
							gc.getInfoTypeForString('PROMOTION_COMMAND1'),
							gc.getInfoTypeForString('PROMOTION_CRAZED'),
							gc.getInfoTypeForString('PROMOTION_DRILL1'),
							gc.getInfoTypeForString('PROMOTION_FEAR'),
							gc.getInfoTypeForString('PROMOTION_FIRE_RESISTANCE'),
							gc.getInfoTypeForString('PROMOTION_LIGHT'),
							gc.getInfoTypeForString('PROMOTION_LIGHTNING_RESISTANCE'),
							gc.getInfoTypeForString('PROMOTION_MAGIC_IMMUNE'),
							gc.getInfoTypeForString('PROMOTION_MEDIC1'),
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
							gc.getInfoTypeForString('PROMOTION_STRANGER'),
							gc.getInfoTypeForString('PROMOTION_MARK_OF_THE_WARDEN'),
							gc.getInfoTypeForString('PROMOTION_ADVENTURER')				]
			liChosenPromotion = []
			for iLoop in xrange(iCount):
				liChosenPromotion.append(liPromotion.pop( CyGame().getSorenRandNum(len(liPromotion), "Variant") ))
			liChosenPromotion.sort()
			for iChosenPromotion in liChosenPromotion:
				unit.setHasPromotion(iChosenPromotion, True)

## Promotions
	## Sheutstone Forge - Dark magic
		if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SHEUT_STONE')):
			if city.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_DARK_FORGE')):
				if CyGame().getSorenRandNum(100, "Despiel Sense") < 20:
					unit.setHasPromotion(gc.getInfoTypeForString("PROMOTION_DARK_MAGIC1") , True)

	## Stable of nightmares - Dark magic
		if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_NIGHTMARE')):
			if city.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_STABLE_OF_NIGHTMARES')):
				if CyGame().getSorenRandNum(100, "Despiel Sense") < 20:
					unit.setHasPromotion(gc.getInfoTypeForString("PROMOTION_DARK_MAGIC1") , True)

	## Variant elf
		if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_VARIANT')):
			iCount = CyGame().getSorenRandNum(2, 'the number of effects') + 1
			liPromotion = [	gc.getInfoTypeForString('PROMOTION_AMPHIBIOUS'),
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
							gc.getInfoTypeForString('PROMOTION_ADVENTURER')				]
			liChosenPromotion = []
			for iLoop in xrange(iCount):
				liChosenPromotion.append(liPromotion.pop( CyGame().getSorenRandNum(len(liPromotion), "Variant") ))
			liChosenPromotion.sort()
			for iChosenPromotion in liChosenPromotion:
				unit.setHasPromotion(iChosenPromotion, True)

## Religions
	## Cult of the Dragon
		if city.isHasReligion(gc.getInfoTypeForString('RELIGION_CULT_OF_THE_DRAGON')):
			if not pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGNOSTIC')):
				if unit.getReligion() == ReligionTypes.NO_RELIGION:
					if CyGame().getSorenRandNum(100, "Bob") <= 20:
						unit.setReligion(gc.getInfoTypeForString('RELIGION_CULT_OF_THE_DRAGON'))

## Civilizations
	## Droaum
		if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_DROAUM'):
		### Undying court - Biological unit that does not have a race to become the demon.
# ent >>>
#			if pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_ECONOMY')) == gc.getInfoTypeForString('CIVIC_UNDYING_COURT_DROAUM'):
			if pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_ECONOMY')) == gc.getInfoTypeForString('CIVIC_UNDYING_COURT_DROAUM') and city.isCapital():
# ent <<<
				if unit.getRace() == PromotionTypes.NO_PROMOTION:
# ent >>>
#					if unit.isAlive():
					if unit.canHaveDefaultRace():
# ent <<<
						unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)

	## Lineage
		if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_LINEAGE'):
			if not unit.isSummoned():
				if unit.canFight():
					## Militaly Academy
					if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_MILITALY_ACADEMY')) > 0:
						unit.changeFreePromotionPick(1)

					## Craftman Studio
					if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_CRAFTMAN_STUDIO')) > 0:
						iStudioNum = pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_CRAFTMAN_STUDIO'))
						lePromotionCombats = [en.ePromotionCombat1, en.ePromotionCombat2, en.ePromotionCombat3, en.ePromotionCombat4, en.ePromotionCombat5]
						for iNum in xrange(iStudioNum):
							ePromotionCombat = lePromotionCombats[iNum]
							ePromotionEmpower = gc.getPromotionInfo(ePromotionCombat).getPromotionSummonPerk()
							unit.setHasPromotion(ePromotionEmpower, True)

	## Rarna
		if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_RARNA'):
		## 火の継承による火炎無効
			if CyGame().getProjectCreatedCount(gc.getInfoTypeForString('PROJECT_FIRE_INHERITANCE')) > 0:
				unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IMMUNE_FIRE'), True)
		## 闇の皇女による不死身
			if CyGame().getProjectCreatedCount(gc.getInfoTypeForString('PROJECT_PRINCESS_OF_DARKNESS')) > 0:
				unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IMMORTAL'), True)
				if unit == gc.getInfoTypeForString('UNIT_MICHAEL'):
					unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_UNHOLY_TAINT'), True)
					unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FEAR'), True)
					unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STIGMATA'), True)

	## Xoth
		if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_XOTH'):
			if unit.isAlive():
				if not isWorldUnitClass(unit.getUnitClassType()):
					if CyGame().getSorenRandNum(100, "Sanity") > pPlayer.getGuildPlusCounter(50):
						unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CRAZED'), True)

## Traits
	## Iron Will - Given faith.
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_IRON_WILL')):
			if pPlayer.getStateReligion() != ReligionTypes.NO_RELIGION:
				if unit.getReligion() == ReligionTypes.NO_RELIGION:
					unit.setReligion(pPlayer.getStateReligion())

	## Inorganic - Given the Destruct Systems to golems.
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_INORGANIC')):
			if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_GOLEM')):
				if not unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DESTRUCT_SYSTEM')):
					if CyGame().getSorenRandNum(100, "Destruct System") < 5:
						unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DESTRUCT_SYSTEM'), True)

	## Undead - undead and diseased
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_UNDEAD')):
# ent >>>
#			if pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_ECONOMY')) != gc.getInfoTypeForString('CIVIC_UNDYING_COURT_DROAUM'):
			if pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_ECONOMY')) != gc.getInfoTypeForString('CIVIC_UNDYING_COURT_DROAUM') or not city.isCapital():
# ent <<<
				if unit.getRace() == PromotionTypes.NO_PROMOTION:
# ent >>>
					"""
					if unit.isAlive():
						if unit.canFight():
							if not isWorldUnitClass(unit.getUnitClassType()):
								if unit.getUnitClassType() != gc.getInfoTypeForString('UNITCLASS_SETTLER') and unit.getUnitClassType() != gc.getInfoTypeForString('UNITCLASS_WORKER'):
									unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_UNDEAD'), True)
									unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_RESERVOIRS_DROAUM'), True)
					"""
					if unit.canHaveDefaultRace():
						if unit.canFight():
							unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_UNDEAD'), True)
							unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_RESERVOIRS_DROAUM'), True)
# ent <<<

	## Agnostic - Atheist
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGNOSTIC')):
			unit.setReligion(-1)

	## Diverse- by WildMana
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_DIVERSE')):
			if unit.getRace() == PromotionTypes.NO_PROMOTION:
				if unit.isAlive():
					iChance = 40
					if CyGame().getSorenRandNum(100, "Bob") < iChance:

						lList = ['PROMOTION_GOBLIN', 'PROMOTION_ORC', 'PROMOTION_LIZARDMAN', 'PROMOTION_OGRE', 'PROMOTION_ELF', 'PROMOTION_DARK_ELF', 'PROMOTION_DWARF']
						eRace = gc.getInfoTypeForString(lList[CyGame().getSorenRandNum(len(lList), "Pick Race")])
						eNewUnit = -1

						if eRace == gc.getInfoTypeForString('PROMOTION_GOBLIN'):
							if unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_SCOUT'):
								eNewUnit = gc.getInfoTypeForString('UNIT_GOBLIN')
							elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_HORSEMAN'):
								eNewUnit = gc.getInfoTypeForString('UNIT_WOLF_RIDER')
							elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_CHARIOT'):
								eNewUnit = gc.getInfoTypeForString('UNIT_WOLF_CHARIOT')

						elif eRace == gc.getInfoTypeForString('PROMOTION_LIZARDMAN'):
							if unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_HUNTER'):
								lUnitList = ['UNIT_LIZARDMAN', 'UNIT_BLOOD_HUNTER']
								eNewUnit = gc.getInfoTypeForString(lUnitList[CyGame().getSorenRandNum(len(lUnitList), "Pick Unit")])
							elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_RANGER'):
								eNewUnit = gc.getInfoTypeForString('UNIT_SLAUGHTERER')
							elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_BEASTMASTER'):
								eNewUnit = gc.getInfoTypeForString('UNIT_ABUSER')
							elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_ASSASSIN'):
								eNewUnit = gc.getInfoTypeForString('UNIT_ADVANCE_GUARD_OF_AGRUONN')
							elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_ARCHER'):
								eNewUnit = gc.getInfoTypeForString('UNIT_JAVELIN_THROWER')
							elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_LONGBOWMAN'):
								eNewUnit = gc.getInfoTypeForString('UNIT_LIZARD_BLOWPIPE')
							elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_CROSSBOWMAN'):
								eNewUnit = gc.getInfoTypeForString('UNIT_TRAP_MASTER')
							elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_MARKSMAN'):
								eNewUnit = gc.getInfoTypeForString('UNIT_AMBUSH')

						elif eRace == gc.getInfoTypeForString('PROMOTION_OGRE'):
							if unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_CHAMPION'):
								eNewUnit = gc.getInfoTypeForString('UNIT_OGRE')
							elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_PHALANX'):
								eNewUnit = gc.getInfoTypeForString('UNIT_STONESKIN_OGRE')

						elif eRace == gc.getInfoTypeForString('PROMOTION_ELF'):
							if unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_CHAMPION'):
								eNewUnit = gc.getInfoTypeForString('UNIT_NUNTIUS')
							elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_HORSE_ARCHER'):
								lUnitList = ['UNIT_FYRDWELL', 'UNIT_VIGILATE']
								eNewUnit = gc.getInfoTypeForString(lUnitList[CyGame().getSorenRandNum(len(lUnitList), "Pick Unit")])
							elif  unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_LONGBOWMAN'):
								lUnitList = ['UNIT_ARROWS_OF_THE_QUEEN', 'UNIT_FERRUM']
								eNewUnit = gc.getInfoTypeForString(lUnitList[CyGame().getSorenRandNum(len(lUnitList), "Pick Unit")])
							elif  unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_CROSSBOWMAN'):
								eNewUnit = gc.getInfoTypeForString('UNIT_FLURRY')

						elif eRace == gc.getInfoTypeForString('PROMOTION_DARK_ELF'):
							if unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_HORSE_ARCHER'):
								eNewUnit = gc.getInfoTypeForString('UNIT_NYXKIN')
							elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_RANGER'):
								eNewUnit = gc.getInfoTypeForString('UNIT_DARK_STOKER')

						elif eRace == gc.getInfoTypeForString('PROMOTION_DWARF'):
							if unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_KNIGHT'):
								eNewUnit = gc.getInfoTypeForString('UNIT_HORNGUARD')
							elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_HORSEMAN'):
								eNewUnit = gc.getInfoTypeForString('UNIT_BOAR_RIDER')
							elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_SHADOW'):
								eNewUnit = gc.getInfoTypeForString('UNIT_DWARVEN_SHADOW')
							elif unit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_DRUID'):
								eNewUnit = gc.getInfoTypeForString('UNIT_DWARVEN_DRUID')

						unit.setHasPromotion(eRace, True)
						if eNewUnit != -1:
							pNewUnit = pPlayer.initUnit(eNewUnit, unit.getX(), unit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
							pNewUnit.convert(unit)
# Kaijin <<<

		if (not self.__LOG_UNITBUILD):
			return
		CvUtil.pyPrint('%s was finished by Player %d Civilization %s'
			%(PyInfo.UnitInfo(unit.getUnitType()).getDescription(), player.getID(), player.getCivilizationName()))

	def onUnitKilled(self, argsList):
		'Unit Killed'
##--------	Single Afterlife: Modified by Denev	--------##
#		unit, iAttacker = argsList
		unit, iAttacker, pKillerUnit = argsList		# pKillerUnit is combat opponent
		bCombatKilled = not pKillerUnit.isNone()
		if bCombatKilled:
			eKillerPlayer = pKillerUnit.getOwner()
		else:
			eKillerPlayer = PlayerTypes.NO_PLAYER
##--------	Single Afterlife: End Modify		--------##
		iPlayer = unit.getOwner()
		player = PyPlayer(iPlayer)
		attacker = PyPlayer(iAttacker)
		pPlayer = gc.getPlayer(iPlayer)
##--------	Single Afterlife: Modified by Denev	--------##
		"""
		if (unit.isAlive() and unit.isImmortal() == False):
			iX = unit.getX()
			iY = unit.getY()
			iSoulForge = gc.getInfoTypeForString('BUILDING_SOUL_FORGE')
			for iiX in xrange(iX-1, iX+2, 1):
				for iiY in xrange(iY-1, iY+2, 1):
					pPlot2 = CyMap().plot(iiX, iiY)
					if pPlot2.isCity():
						pCity = pPlot2.getPlotCity()
						if pCity.isHasActiveBuilding(iSoulForge):
							pCity.changeProduction(unit.getExperience() + 10)
							CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_SOUL_FORGE", ()), 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Buildings/Soulforge.dds', en.eColorRed, pCity.getX(), pCity.getY(), True, True)
			pPlot = CyMap().plot(iX, iY)
			if pPlot.isCity():
				pCity = pPlot.getPlotCity()
				if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_MOKKAS_CAULDRON')):
					if pCity.getOwner() == unit.getOwner():
						iUnit = cf.getUnholyVersion(unit)
						if iUnit != -1:
							pNewUnit = pPlayer.initUnit(iUnit, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
							pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)
							pNewUnit.setDamage(50, PlayerTypes.NO_PLAYER)
							pNewUnit.finishMoves()
							szBuffer = gc.getUnitInfo(pNewUnit.getUnitType()).getDescription()
							CyInterface().addMessage(unit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_MOKKAS_CAULDRON", ((szBuffer, ))), 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Buildings/Mokkas Cauldron.dds', en.eColorRed, pCity.getX(), pCity.getY(), True, True)

			if (unit.getReligion() == gc.getInfoTypeForString('RELIGION_COUNCIL_OF_ESUS') or unit.getReligion() == gc.getInfoTypeForString('RELIGION_THE_ASHEN_VEIL') or unit.getReligion() == gc.getInfoTypeForString('RELIGION_OCTOPUS_OVERLORDS') or unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DEATH1')) or unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ENTROPY1'))):
				cf.giftUnit(gc.getInfoTypeForString('UNIT_MANES'), gc.getInfoTypeForString('CIVILIZATION_INFERNAL'), 0, unit.plot(), unit.getOwner())
				cf.giftUnit(gc.getInfoTypeForString('UNIT_MANES'), gc.getInfoTypeForString('CIVILIZATION_INFERNAL'), 0, unit.plot(), unit.getOwner())

			if (unit.getReligion() == gc.getInfoTypeForString('RELIGION_THE_EMPYREAN') or unit.getReligion() == gc.getInfoTypeForString('RELIGION_THE_ORDER') or unit.getReligion() == gc.getInfoTypeForString('RELIGION_RUNES_OF_KILMORPH') or (unit.getUnitCombatType() != gc.getInfoTypeForString('UNITCOMBAT_ANIMAL') and pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MERCURIANS'))):
				cf.giftUnit(gc.getInfoTypeForString('UNIT_ANGEL'), gc.getInfoTypeForString('CIVILIZATION_MERCURIANS'), unit.getExperience(), unit.plot(), unit.getOwner())

			if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SPIRIT_GUIDE')):
				if unit.getExperience() > 0:
					py = PyPlayer(iPlayer)
					lUnits = []
					for pLoopUnit in py.getUnitList():
						if pLoopUnit.isAlive():
							if not pLoopUnit.isOnlyDefensive():
								if not pLoopUnit.isDelayedDeath():
									lUnits.append(pLoopUnit)
					if len(lUnits) > 0:
						pUnit = lUnits[CyGame().getSorenRandNum(len(lUnits), "Spirit Guide")-1]
						iXP = unit.getExperience() / 2
						pUnit.changeExperience(iXP, -1, False, False, False)
						unit.changeExperience(iXP * -1, -1, False, False, False)
						CyInterface().addMessage(unit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_SPIRIT_GUIDE", ()), 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Promotions/SpiritGuide.dds', en.eColorRed, pUnit.getX(), pUnit.getY(), True, True)

		if unit.getUnitType() == gc.getInfoTypeForString('UNIT_ACHERON'):
			unit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HELD'), False)
		"""
#Kaijin >>>
		eUnitType = unit.getUnitType()
		pPlot = unit.plot()
#Kaijin <<<

# ent >>>
#		if eUnitType == gc.getInfoTypeForString('UNIT_WAR_MACHINE'):
		if eUnitType in (gc.getInfoTypeForString('UNIT_WAR_MACHINE'), gc.getInfoTypeForString('UNIT_DAMIEN')):
# ent <<<
			CyGame().decrementUnitCreatedCount(eUnitType)
			CyGame().decrementUnitClassCreatedCount(unit.getUnitClassType())

		'AutoCombatSpell by Combat Killed.'
		if eUnitType in (gc.getInfoTypeForString('UNIT_PYRE_ZOMBIE'), gc.getInfoTypeForString('UNIT_AZER')):
			if bCombatKilled:
				unit.cast(gc.getInfoTypeForString('SPELL_PYRE_EXPLODE'))

#Kaijin >>>
		elif eUnitType == gc.getInfoTypeForString('UNIT_HELLFIRE_ELEMENTAL'):
			if bCombatKilled:
				unit.cast(gc.getInfoTypeForString('SPELL_PYRE_EXPLODE_MINOR'))

		elif eUnitType in (gc.getInfoTypeForString('UNIT_UNDEAD_FURY'), gc.getInfoTypeForString('UNIT_BONE_HORDE')):
			if bCombatKilled:
				unit.cast(gc.getInfoTypeForString('SPELL_PYRE_EXPLODE_GREATER'))

		elif eUnitType == gc.getInfoTypeForString('UNIT_ICE_ELEMENTAL'):
			if bCombatKilled:
				unit.cast(gc.getInfoTypeForString('SPELL_COMBAT_COLD'))

		elif eUnitType == gc.getInfoTypeForString('UNIT_AIR_ELEMENTAL'):
			if bCombatKilled:
				unit.cast(gc.getInfoTypeForString('SPELL_COMBAT_LIGHTNING'))

		elif eUnitType in (gc.getInfoTypeForString('UNIT_ZOMBIE_CITIZEN'), gc.getInfoTypeForString('UNIT_ZOMBIE_SOLDIER'), gc.getInfoTypeForString('UNIT_ZOMBIE_LORD')):
			if bCombatKilled:
				unit.cast(gc.getInfoTypeForString('SPELL_COMBAT_POISON'))

		elif eUnitType in (gc.getInfoTypeForString('UNIT_FROST_GIANT'), gc.getInfoTypeForString('UNIT_SNOW_MONSTROSITY'), gc.getInfoTypeForString('UNIT_ICE_STATUE')):
			if bCombatKilled:
				unit.cast(gc.getInfoTypeForString('SPELL_COMBAT_BLIZZARD'))

		elif unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ELEMENTAL')) and pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_HEART_OF_THE_CHAOS')) >= 1:
			if bCombatKilled:
				unit.cast(gc.getInfoTypeForString('SPELL_COMBAT_POISON'))

		elif unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DESTRUCT_SYSTEM')):
			if bCombatKilled:
				unit.cast(gc.getInfoTypeForString('SPELL_PYRE_EXPLODE_MINOR'))

		if unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_REVENGER')):
			if bCombatKilled:
				eTeam = unit.getTeam()
				lpRangedUnits = cyGetRangedUnits(pPlot, 1, False, True, eTeam)
				for pLoopUnit in lpRangedUnits:
					if not pLoopUnit.isEnemy(eTeam, pLoopUnit.plot()):
						if pLoopUnit.canFight():
							pLoopUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MORALE'), True)

#Kaijin <<<

		'Afterlife of Killed Unit.'
		if eUnitType == gc.getInfoTypeForString('UNIT_BARNAXUS'):
			pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_PIECES_OF_BARNAXUS'), unit.getX(), unit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

#Kaijin >>>
		elif eUnitType in (gc.getInfoTypeForString('UNIT_BLIME'), gc.getInfoTypeForString('UNIT_NIZAR'), gc.getInfoTypeForString('UNIT_PULUFRAUS')):
			if unit.isAlive() and not unit.isDuration():
				iKaijinHero = gc.getInfoTypeForString('UNIT_NIZAR')
				if eUnitType == gc.getInfoTypeForString('UNIT_NIZAR'):
					iKaijinHero = gc.getInfoTypeForString('UNIT_PULUFRAUS')
				elif eUnitType == gc.getInfoTypeForString('UNIT_PULUFRAUS'):
					iKaijinHero = gc.getInfoTypeForString('UNIT_GOGUREG')
				pCapitalPlot = pPlayer.getCapitalCity().plot()
				if pCapitalPlot != -1:
					pCapitalPlot = pPlot
				pNewUnit = pPlayer.initUnit(iKaijinHero, pCapitalPlot.getX(), pCapitalPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
				pNewUnit.changeExperience(unit.getExperience(), -1, False, False, False)
				if pCapitalPlot.isVisibleToWatchingHuman():
					CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_DEATH_AND_DECAY'), pCapitalPlot.getPoint())
					CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_RESURRECTION'), pCapitalPlot.getPoint())

	## Despiel - Immortality of Yenoiah.
		elif eUnitType == gc.getInfoTypeForString('UNIT_YENOIAH'):
			if not unit.isSummoned():

				lpCities = []
				if pPlayer.isAlive():
					for pyCity in player.getCityList():
						pLoopCity = pyCity.GetCy()
						if pPlot.getX() != pLoopCity.getX() or pPlot.getY() != pLoopCity.getY():
							lpCities.append(pyCity)

				if len(lpCities) > 0:
					iRnd = CyGame().getSorenRandNum(len(lpCities), "Select City")
					pRevivalCity = lpCities[iRnd]

					pNewUnit = pPlayer.initUnit(eUnitType, pRevivalCity.getX(), pRevivalCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
					pCityPlot = pRevivalCity.plot()
					if pCityPlot.isVisibleToWatchingHuman():
						CyEngine().triggerEffect(gc.getInfoTypeForString('EFFECT_RESURRECTION'), pCityPlot.getPoint())

					for iProm in xrange(gc.getNumPromotionInfos()):
						if not pNewUnit.isHasPromotion(iProm):
							if (unit.isHasPromotion(iProm)):
								if not gc.getPromotionInfo(iProm).isEquipment():
									if not gc.getPromotionInfo(iProm).isRace():
										pNewUnit.setHasPromotion(iProm, True)

					pNewUnit.setLevel(unit.getLevel())
					pNewUnit.setExperience(unit.getExperience(), -1)
					if unit.getReligion() != ReligionTypes.NO_RELIGION:
						pNewUnit.setReligion(unit.getReligion())

					pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WITHERED'), False)
					pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAK'), False)
					pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DISEASED'), False)
					pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUED'), False)
					pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PEST'), False)
					pNewUnit.changeImmobileTimer(1)

		elif unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_PARASITIC')):
			if bCombatKilled:
				eParasitePlayer = cf.getCivilization(gc.getInfoTypeForString('CIVILIZATION_BALDRALFAR'))
				if eParasitePlayer == PlayerTypes.NO_PLAYER:
					eParasitePlayer = gc.getBARBARIAN_PLAYER() + gc.getInfoTypeForString('BARBARIAN_ANIMAL')
				pParasitePlayer = gc.getPlayer(eParasitePlayer)
				pTargetPlot = cf.findAdjacentClearPlot(eParasitePlayer, pPlot.getX(), pPlot.getY(), False, False)
				if pTargetPlot is not None:
					pNewUnit = pParasitePlayer.initUnit(gc.getInfoTypeForString('UNIT_DRYAS'), pTargetPlot.getX(), pTargetPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
					pNewUnit.setHomeCivilizationType(eParasitePlayer)
					szButton = gc.getPromotionInfo(gc.getInfoTypeForString('PROMOTION_PARASITIC')).getButton()
					szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_BIRTH_OF_PARASITIC_ENEMY', (unit.getNameKey(), pParasitePlayer.getCivilizationAdjectiveKey()))
					CyInterface().addMessage(eKillerPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorRed, pNewUnit.getX(), pNewUnit.getY(), True, True)

#Kaijin <<<

# Kaijin >>>
#		if unit.isAlive():
		elif (	(unit.isAlive() or unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ANGEL_PAC')))
				 and unit.getCaptureUnitType(pPlayer.getCivilizationType()) == UnitTypes.NO_UNIT			):
# Kaijin <<<

			'Afterlife of Killed Unit with Body or Soul.'
# Kaijin >>>
	## Despiel - Soul Culture Facilities
			bCultureSoul = False
# Kaijin >>>	patch29 expansion - Start -
			"""
			pCity = pPlot.getWorkingCity()
			if not pCity.isNone():
				if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_SOUL_CULTURE_FACILITIES')):
					bCultureSoul = True
			"""
# Kaijin <<<	patch29 expansion - End -

	## Nougbii - Do not have a soul.
			if unit.isAlive() and unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_MUPPET')):
				unit.setAfterlife(AfterlifeTypes.AFTERLIFE_RISE_OR_FALL)

	## Nougbii - Angel-pac gives a soul.
			if not unit.isAlive() and unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ANGEL_PAC')):
				unit.setAfterlife(AfterlifeTypes.AFTERLIFE_PREYED)

# ent >>>
			def doConsumeLives(pUnit, bConsumeBody, bConsumeSoul, bCultureSoul):
				if bConsumeBody and bConsumeSoul:
					if bCultureSoul:
						bCultureSoul = False
						pUnit.setAfterlife(AfterlifeTypes.AFTERLIFE_PREYED)
					else:
						pUnit.setAfterlife(AfterlifeTypes.AFTERLIFE_PYTHON)
				elif not bConsumeBody and bConsumeSoul:
					if bCultureSoul:
						bCultureSoul = False
					elif pUnit.getAfterlife() == AfterlifeTypes.NO_AFTERLIFE:
						pUnit.setAfterlife(AfterlifeTypes.AFTERLIFE_RISE_OR_FALL)
					else: # pUnit.getAfterlife() == AfterlifeTypes.AFTERLIFE_PREYED:
						pUnit.setAfterlife(AfterlifeTypes.AFTERLIFE_PYTHON)
				elif bConsumeBody and not bConsumeSoul:
					if pUnit.getAfterlife() == AfterlifeTypes.NO_AFTERLIFE:
						pUnit.setAfterlife(AfterlifeTypes.AFTERLIFE_PREYED)
					else: # pUnit.getAfterlife() == AfterlifeTypes.AFTERLIFE_RISE_OR_FALL:
						pUnit.setAfterlife(AfterlifeTypes.AFTERLIFE_PYTHON)
				return bCultureSoul
# ent <<<

# Kaijin <<<

			iSpiritGuide = gc.getInfoTypeForString('PROMOTION_SPIRIT_GUIDE')
			if unit.isHasPromotion(iSpiritGuide):
# Kaijin OAC - for Only Difensive Units --------------
#				if unit.getExperience() > 0:
				if unit.getExperience() > 0 and not unit.isOnlyDefensive():
# Kaijin OAC - End -------------------- --------------
					lpGuidedUnits = []
					for pLoopUnit in player.getUnitList():
						if pLoopUnit.isAlive():
							if not pLoopUnit.isOnlyDefensive():
								if not pLoopUnit.isDelayedDeath():
									lpGuidedUnits.append(pLoopUnit)
					if len(lpGuidedUnits) > 0:
						pGuidedUnit = lpGuidedUnits[CyGame().getSorenRandNum(len(lpGuidedUnits), "Spirit Guide")]
						iXP = max(1, unit.getExperience() // 2)
						pGuidedUnit.changeExperience(iXP, -1, False, False, False)
						unit.changeExperience(iXP * -1, -1, False, False, False)
						szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_SPIRIT_GUIDE", (gc.getPromotionInfo(iSpiritGuide).getDescription(), pGuidedUnit.getNameKey(), iXP))
						CyInterface().addMessage(unit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getPromotionInfo(iSpiritGuide).getButton(), en.eColorRed, pGuidedUnit.getX(), pGuidedUnit.getY(), True, True)

# Kaijin >>>
			if unit.getAfterlife() == AfterlifeTypes.NO_AFTERLIFE:
				if not unit.isDuration() and not unit.isSummoned():
					if (CyGame().getSorenRandNum(100, "Necromancy") < 20 and not isWorldUnitClass(unit.getUnitClassType())):
						eNecromancy = gc.getInfoTypeForString('PROMOTION_NECROMANCY')
						lpRangedUnits = cyGetRangedUnits(pPlot, 1, False, True, unit.getTeam())
						lpNecromancers = [	pNecromancer for pNecromancer in lpRangedUnits
														if	pNecromancer.canFight()
														and	pNecromancer.isHasPromotion(eNecromancy)	]
						if len(lpNecromancers) > 0:
							pNecromancer = lpNecromancers[gc.getGame().getSorenRandNum(len(lpNecromancers), "Necromancer")]
							iNecroPlayer = pNecromancer.getOwner()
							pNecroPlayer = gc.getPlayer(iNecroPlayer)
							pNewUnit = pNecroPlayer.initUnit(eUnitType, pNecromancer.getX(), pNecromancer.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
							pNewUnit.setDamage(pNewUnit.maxHitPoints() // 2, PlayerTypes.NO_PLAYER)
							pNewUnit.setHomeCivilizationType(unit.getHomeCivilizationType())

							for iPromotion in xrange(gc.getNumPromotionInfos()):
								if gc.getPromotionInfo(iPromotion).isEquipment():
									pNewUnit.setHasPromotion(iPromotion, False)

							pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_UNDEAD'), True)
							eUnitArtStyle = unit.getUnitArtStyleType()
							if eUnitArtStyle == UnitArtStyleTypes.NO_UNIT_ARTSTYLE:
								eUnitArtStyle = gc.getCivilizationInfo(unit.getHomeCivilizationType()).getUnitArtStyleType()
							pNewUnit.setUnitArtStyleType(eUnitArtStyle)

							kNecromancy = gc.getPromotionInfo(eNecromancy)
							szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_NECROMANCY_RESURRECTION", (pNewUnit.getName(), kNecromancy.getTextKey()))
							CyInterface().addMessage(iNecroPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pNewUnit.getButton(), en.eColorGreen, pNewUnit.getX(), pNewUnit.getY(), True, True)
							if unit.getTeam() != pNecromancer.getTeam():
								szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_NECROMANCY_RESURRECTION_ENEMY", (unit.getName(), kNecromancy.getTextKey(), pNecromancer.getName()))
								CyInterface().addMessage(unit.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, kNecromancy.getButton(), en.eColorRed, pNewUnit.getX(), pNewUnit.getY(), True, True)

							bCultureSoul = doConsumeLives(unit, True, True, bCultureSoul)
# Kaijin <<<

			if unit.getAfterlife() == AfterlifeTypes.NO_AFTERLIFE:
#				if not unit.isDuration():			# not summoned
				if not unit.isSummoned():
					pCity = pPlot.getWorkingCity()
					if not pCity.isNone():
						eCityOwner = pCity.getOwner()
						if eCityOwner in (unit.getOwner(), eKillerPlayer):
# Kaijin >>>
							"""
							if pCity.isHasActiveBuilding(eCauldron):
								eRebornUnit = cf.getUnholyVersion(unit)
								if eRebornUnit != UnitTypes.NO_UNIT:
									pNewUnit = gc.getPlayer(eCityOwner).initUnit(eRebornUnit, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
									pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)
									pNewUnit.setHomeCivilizationType(en.eCivilizationInfernal)
									pNewUnit.setDamage(pNewUnit.maxHitPoints() // 2, PlayerTypes.NO_PLAYER)
									pNewUnit.finishMoves()
									CyInterface().addMessage(eCityOwner, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_MOKKAS_CAULDRON", ((pNewUnit.getNameKey(), ))), 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getBuildingInfo(eCauldron).getButton(), en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
									unit.setAfterlife(AfterlifeTypes.AFTERLIFE_PYTHON)
							"""
							pCityOwner = gc.getPlayer(eCityOwner)
							if pCityOwner.getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_MOKKAS_CAULDRON')) > 0:
								if CyGame().getSorenRandNum(100, "Reborn") < 50:
									eCauldron = gc.getInfoTypeForString('BUILDING_MOKKAS_CAULDRON')
									for pyCity in PyPlayer(eCityOwner).getCityList():
										pLoopCity = pyCity.GetCy()
										if pLoopCity.isHasActiveBuilding(eCauldron):
											eRebornUnit = cf.getUnholyVersion(unit)
											if eRebornUnit != UnitTypes.NO_UNIT:
												pNewUnit = pCityOwner.initUnit(eRebornUnit, pLoopCity.getX(), pLoopCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
												pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEMON'), True)
												pNewUnit.setHomeCivilizationType(en.eCivilizationInfernal)
												pNewUnit.setDamage(pNewUnit.maxHitPoints() // 2, PlayerTypes.NO_PLAYER)
												pNewUnit.finishMoves()
												CyInterface().addMessage(eCityOwner, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_MOKKAS_CAULDRON", ((pNewUnit.getNameKey(), ))), 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getBuildingInfo(eCauldron).getButton(), en.eColorGreen, pLoopCity.getX(), pLoopCity.getY(), True, True)
												# Kaijin - Culture soul -
												"""
												unit.setAfterlife(AfterlifeTypes.AFTERLIFE_PYTHON)
												"""
												bCultureSoul = doConsumeLives(unit, True, True, bCultureSoul)
												break
												# Kaijin - End -
# Kaijin <<<

			if unit.getAfterlife() in (AfterlifeTypes.NO_AFTERLIFE, AfterlifeTypes.AFTERLIFE_PREYED):
				"""
				pCity = pPlot.getWorkingCity()
				if not pCity.isNone():
					iSoulForge = gc.getInfoTypeForString('BUILDING_SOUL_FORGE')
					if pCity.isHasActiveBuilding(iSoulForge):
						iProduction = unit.getExperience() + 10
						iProduction = cyFlatValue(iProduction, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getConstructPercent(), True)
						pCity.changeProduction(iProduction)
						CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_SOUL_FORGE", ()), 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getBuildingInfo(iSoulForge).getButton(), en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
						unit.setAfterlife(AfterlifeTypes.AFTERLIFE_PYTHON)
				"""
# Kaijin >>>	patch29 expansion - Start -
				"""
				if pPlot.isOwned():
					if gc.getPlayer(pPlot.getOwner()).getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_SOUL_FORGE')) > 0:
						eSoulForge = gc.getInfoTypeForString('BUILDING_SOUL_FORGE')
						for pyCity in PyPlayer(pPlot.getOwner()).getCityList():
							pCity = pyCity.GetCy()
							if pCity.isHasActiveBuilding(eSoulForge):
								if pCity.getProductionProcess() == ProcessTypes.NO_PROCESS:
									iProductionTimes100 = (unit.getExperience() + 10) * (100 + pCity.getProductionModifier())
									iProductionTimes100 = cyFlatValue(iProductionTimes100, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getConstructPercent(), True)
									pCity.changeProduction(iProductionTimes100 // 100)
									CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_SOUL_FORGE", ()), 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getBuildingInfo(eSoulForge).getButton(), en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
									# Kaijin - Culture soul -
#									unit.setAfterlife(AfterlifeTypes.AFTERLIFE_PYTHON)
									bCultureSoul = doConsumeLives(unit, False, True, bCultureSoul)
									break
									# Kaijin - End -
				"""
				bValid = 0
				eOwner = 0
				if pPlot.isOwned() and gc.getPlayer(pPlot.getOwner()).getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_SOUL_FORGE')) > 0:
					if gc.getPlayer(pPlot.getOwner()).isAlive():
						eOwner = pPlot.getOwner()
						bValid = 1
				elif bCombatKilled:
					if gc.getPlayer(eKillerPlayer).getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_SOUL_FORGE')) > 0:
						if gc.getPlayer(eKillerPlayer).isAlive():
							eOwner = eKillerPlayer
							bValid = 2

				if bValid:
					eSoulForge = gc.getInfoTypeForString('BUILDING_SOUL_FORGE')
					for pyCity in PyPlayer(eOwner).getCityList():
						pCity = pyCity.GetCy()
						if pCity.isHasActiveBuilding(eSoulForge):
							if pCity.getProductionProcess() == ProcessTypes.NO_PROCESS:
								#死亡したユニットの世代で基本値を設定
								iBaseProduction = 0
								eUnit = gc.getUnitInfo(unit.getUnitType())
								if eUnit.getProductionCost() > 0:
									iBaseProduction = eUnit.getProductionCost()
								else:
									if gc.getUnitInfo(unit.getUnitType()).getTier() == 1:
										iBaseProduction = 25
									elif gc.getUnitInfo(unit.getUnitType()).getTier() == 2:
										iBaseProduction = 60
									elif gc.getUnitInfo(unit.getUnitType()).getTier() == 3:
										iBaseProduction = 120
									elif gc.getUnitInfo(unit.getUnitType()).getTier() == 4:
										iBaseProduction = 180

								iProductionTimes100 = (unit.getExperience() + iBaseProduction) * (50 + pCity.getProductionModifier())
								iProductionTimes100 = cyFlatValue(iProductionTimes100, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getConstructPercent(), True)
								if bValid == 2:		#自領外ではハンマー変換の発生確率を低下
									iChance = 25
									if CyGame().getSorenRandNum(100, "Soul forge") >= iChance:
										break
								if bValid:
									pCity.changeProduction(iProductionTimes100 // 100)
									CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_SOUL_FORGE", ()), 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, gc.getBuildingInfo(eSoulForge).getButton(), en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
									if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_SOUL_CULTURE_FACILITIES')):		#霊魂培養所による魂の残機増加
										bCultureSoul = True
									bCultureSoul = doConsumeLives(unit, False, True, bCultureSoul)
									break
# Kaijin <<<	patch29 expansion - End -

# Kaijin >>>
	## Despiel - Experimental Facility
			if unit.getAfterlife() == AfterlifeTypes.NO_AFTERLIFE:
# Kaijin >>>	patch29 expansion - Start -
				"""
				if CyGame().getSorenRandNum(100, "Experimental") < 10:
					if not unit.isSummoned():
						pCity = pPlot.getWorkingCity()
						if not pCity.isNone():
							eCityOwner = pCity.getOwner()
							if eCityOwner in (unit.getOwner(), eKillerPlayer):
								eExperimental = gc.getInfoTypeForString('BUILDING_EXPERIMENTAL_FACILITY')
								if pCity.isHasActiveBuilding(eExperimental):
									liUnits = [	gc.getInfoTypeForString('UNIT_BONE_PLAYER'),
												gc.getInfoTypeForString('UNIT_HUNCHBACK'),
												gc.getInfoTypeForString('UNIT_SNEERED'),
												gc.getInfoTypeForString('UNIT_ARCHER')	]
									eRebornUnit = liUnits.pop( CyGame().getSorenRandNum(len(liUnits), "Transmigration") )
									if eRebornUnit != UnitTypes.NO_UNIT:
										pNewUnit = gc.getPlayer(eCityOwner).initUnit(eRebornUnit, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
										pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_KAIJIN_RACE'), True)
										pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WITHERED'), False)
										pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAK'), False)
										pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DISEASED'), False)
										pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUED'), False)
										pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PEST'), False)
										pNewUnit.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_DESPIEL'))
										pNewUnit.setDamage(pNewUnit.maxHitPoints() // 2, PlayerTypes.NO_PLAYER)
										pNewUnit.finishMoves()

										szText = CyTranslator().getText("TXT_KEY_MESSAGE_EXPERIMENTAL_FACILITY",(unit.getNameKey(), pCity.getNameKey(), pNewUnit.getNameKey()))
										szButton = gc.getBuildingInfo(eExperimental).getButton()
										CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szText, 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
										# Kaijin - Culture soul -
#										unit.setAfterlife(AfterlifeTypes.AFTERLIFE_PYTHON)
										bCultureSoul = doConsumeLives(unit, True, True, bCultureSoul)
										# Kaijin - End -
				"""
				bValid = 0
				eOwner = 0
				if pPlot.isOwned() and gc.getPlayer(pPlot.getOwner()).getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_DUNGEON')) > 0:
					if gc.getPlayer(pPlot.getOwner()).isAlive():
						eOwner = pPlot.getOwner()
						bValid = 1
				elif bCombatKilled:
					if gc.getPlayer(eKillerPlayer).getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_DUNGEON')) > 0:
						if gc.getPlayer(eKillerPlayer).isAlive():
							eOwner = eKillerPlayer
							bValid = 2
				if unit.isSummoned():
					bValid = 0

				if bValid:
					eBuilding = gc.getInfoTypeForString('BUILDING_EXPERIMENTAL_FACILITY')
					lpCity = []
					lpChosenCity = []
					for pyCity in PyPlayer(eOwner).getCityList():
						pCity = pyCity.GetCy()
						if pCity.isHasActiveBuilding(eBuilding):
							lpCity.append(pCity)
					if len(lpCity) > 0:
						pCity = lpCity[CyGame().getSorenRandNum(len(lpCity), "Chosen")]

						if bValid == 1:		#自領内では発生確率50%固定
							iChance = 50
						if bValid == 2:		#自領外では発生確率を低下
							iChance = 10
							iChance + (5 ** (gc.getPlayer(eOwner).getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_DUNGEON'))))
							if iChance > 50:
								iChance = 50
							if CyGame().getSorenRandNum(100, "chance") >= iChance:
								bValid = 0

						if bValid:
							liUnits = [	gc.getInfoTypeForString('UNIT_BONE_PLAYER'),
										gc.getInfoTypeForString('UNIT_HUNCHBACK'),
										gc.getInfoTypeForString('UNIT_SNEERED'),
										gc.getInfoTypeForString('UNIT_ARCHER')	]
							eRebornUnit = liUnits.pop( CyGame().getSorenRandNum(len(liUnits), "Transmigration") )
							if eRebornUnit != UnitTypes.NO_UNIT:
								pNewUnit = gc.getPlayer(pCity.getOwner()).initUnit(eRebornUnit, pCity.getX(), pCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
								pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_KAIJIN_RACE'), True)
								pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WITHERED'), False)
								pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_WEAK'), False)
								pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DISEASED'), False)
								pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PLAGUED'), False)
								pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PEST'), False)
								pNewUnit.setHomeCivilizationType(gc.getInfoTypeForString('CIVILIZATION_DESPIEL'))
								pNewUnit.setDamage(pNewUnit.maxHitPoints() // 2, PlayerTypes.NO_PLAYER)
								pNewUnit.finishMoves()

								szText = CyTranslator().getText("TXT_KEY_MESSAGE_EXPERIMENTAL_FACILITY",(unit.getNameKey(), pCity.getNameKey(), pNewUnit.getNameKey()))
								szButton = gc.getBuildingInfo(eBuilding).getButton()
								CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szText, 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
								if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_SOUL_CULTURE_FACILITIES')):		#霊魂培養所による魂の残機増加
									bCultureSoul = True
								bCultureSoul = doConsumeLives(unit, False, True, bCultureSoul)
# Kaijin <<<	patch29 expansion - End -

	## Despiel - Soul Exchange
			if unit.getAfterlife() in (AfterlifeTypes.NO_AFTERLIFE, AfterlifeTypes.AFTERLIFE_PREYED):
# Kaijin >>>	patch29 expansion - Start -
				"""
				pCity = pPlot.getWorkingCity()
				if not pCity.isNone():
					eSoulExchange = gc.getInfoTypeForString('BUILDING_SOUL_EXCHANGE')
					if pCity.isHasActiveBuilding(eSoulExchange):
						iCityPlayer = pCity.getOwner()
						pCityPlayer = gc.getPlayer(iCityPlayer)
						eTeam = gc.getTeam(pCityPlayer.getTeam())
						iResearchTech = pCityPlayer.getCurrentResearch()
						iNum = (10 + (unit.getLevel() * unit.getLevel())) * 5
						if iResearchTech != TechTypes.NO_TECH:
							eTeam.changeResearchProgress(iResearchTech, iNum, iCityPlayer)

							szText = CyTranslator().getText("TXT_KEY_MESSAGE_SOUL_EXCHANGE",(unit.getNameKey(), pCity.getNameKey()))
							szButton = gc.getBuildingInfo(eSoulExchange).getButton()
							CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szText, 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
							bCultureSoul = doConsumeLives(unit, False, True, bCultureSoul)
				"""
				bValid = 0
				eOwner = 0
				if pPlot.isOwned() and gc.getPlayer(pPlot.getOwner()).getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_FORGE')) > 0:
					if gc.getPlayer(pPlot.getOwner()).isAlive():
						eOwner = pPlot.getOwner()
						bValid = 1
				elif bCombatKilled:
					if gc.getPlayer(eKillerPlayer).getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_FORGE')) > 0:
						if gc.getPlayer(eKillerPlayer).isAlive():
							eOwner = eKillerPlayer
							bValid = 2

				if bValid:
					eBuilding = gc.getInfoTypeForString('BUILDING_SOUL_EXCHANGE')
					lpCity = []
					lpChosenCity = []
					for pyCity in PyPlayer(eOwner).getCityList():
						pCity = pyCity.GetCy()
						if pCity.isHasActiveBuilding(eBuilding):
							lpCity.append(pCity)
					if len(lpCity) > 0:
						pCity = lpCity[CyGame().getSorenRandNum(len(lpCity), "Chosen")]

						if bValid == 2:		#自領外では発生確率を低下
							iChance = 10
							iChance + (5 ** (gc.getPlayer(eOwner).getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_FORGE'))))
							if iChance > 50:
								iChance = 50
							if CyGame().getSorenRandNum(100, "chance") >= iChance:
								bValid = 0

						if bValid:
							iCityPlayer = pCity.getOwner()
							pCityPlayer = gc.getPlayer(iCityPlayer)
							eTeam = gc.getTeam(pCityPlayer.getTeam())
							iResearchTech = pCityPlayer.getCurrentResearch()
							iNum = (10 + (unit.getLevel() * unit.getLevel())) * 5
							if iResearchTech != TechTypes.NO_TECH:
								eTeam.changeResearchProgress(iResearchTech, iNum, iCityPlayer)

								szText = CyTranslator().getText("TXT_KEY_MESSAGE_SOUL_EXCHANGE",(unit.getNameKey(), pCity.getNameKey()))
								szButton = gc.getBuildingInfo(eBuilding).getButton()
								CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szText, 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
								if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_SOUL_CULTURE_FACILITIES')):		#霊魂培養所による魂の残機増加
									bCultureSoul = True
								bCultureSoul = doConsumeLives(unit, False, True, bCultureSoul)
# Kaijin <<<	patch29 expansion - End -

	## Despiel - Strange Butcher
			if unit.getAfterlife() in (AfterlifeTypes.NO_AFTERLIFE, AfterlifeTypes.AFTERLIFE_RISE_OR_FALL):
# Kaijin >>>	patch29 expansion - Start -
				"""
				pCity = pPlot.getWorkingCity()
				if not pCity.isNone():
					eStrangeButcher = gc.getInfoTypeForString('BUILDING_STRANGE_BUTCHER')
					if pCity.isHasActiveBuilding(eStrangeButcher):
						iCityPlayer = pCity.getOwner()
						pCityPlayer = gc.getPlayer(iCityPlayer)
						if pCity.happyLevel() - pCity.unhappyLevel(0) > 0:
							if pCity.goodHealth() - pCity.badHealth(False) > 0:
								pCity.changePopulation(1)
								iBadHealth = CyGame().getSorenRandNum(4, "Unhealth") + 1
								pCity.changeEspionageHealthCounter(iBadHealth)

								szText = CyTranslator().getText("TXT_KEY_MESSAGE_SACRIFICE_POPULATION",(unit.getNameKey(), pCity.getNameKey()))
								szButton = gc.getBuildingInfo(eStrangeButcher).getButton()
								CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szText, 'AS2D_POSITIVE_DINK', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
								bCultureSoul = doConsumeLives(unit, True, False, bCultureSoul)
				"""
				bValid = 0
				eOwner = 0
				if pPlot.isOwned() and gc.getPlayer(pPlot.getOwner()).getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_MARKET')) > 0:
					if gc.getPlayer(pPlot.getOwner()).isAlive():
						eOwner = pPlot.getOwner()
						bValid = 1
				elif bCombatKilled:
					if gc.getPlayer(eKillerPlayer).getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_MARKET')) > 0:
						if gc.getPlayer(eKillerPlayer).isAlive():
							eOwner = eKillerPlayer
							bValid = 2

				if bValid:
					eBuilding = gc.getInfoTypeForString('BUILDING_STRANGE_BUTCHER')
					lpCity = []
					lpChosenCity = []
					for pyCity in PyPlayer(eOwner).getCityList():
						pCity = pyCity.GetCy()
						if pCity.isHasActiveBuilding(eBuilding):
							if pCity.happyLevel() - pCity.unhappyLevel(0) > 0:
								if pCity.goodHealth() - pCity.badHealth(False) > 0:
									lpCity.append(pCity)
					if len(lpCity) > 0:
						pCity = lpCity[CyGame().getSorenRandNum(len(lpCity), "Chosen")]

						if bValid == 2:		#自領外では発生確率を低下
							iChance = 10
							iChance + (5 ** (gc.getPlayer(eOwner).getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_MARKET'))))
							if iChance > 50:
								iChance = 50
							if CyGame().getSorenRandNum(100, "chance") >= iChance:
								bValid = 0

						if bValid:
							pCity.changePopulation(1)
							iBadHealth = CyGame().getSorenRandNum(4, "Unhealth") + 1
							pCity.changeEspionageHealthCounter(iBadHealth)

							szText = CyTranslator().getText("TXT_KEY_MESSAGE_SACRIFICE_POPULATION",(unit.getNameKey(), pCity.getNameKey()))
							szButton = gc.getBuildingInfo(eBuilding).getButton()
							CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szText, 'AS2D_POSITIVE_DINK', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
							if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_SOUL_CULTURE_FACILITIES')):		#霊魂培養所による魂の残機増加
								bCultureSoul = True
							bCultureSoul = doConsumeLives(unit, False, True, bCultureSoul)
# Kaijin <<<	patch29 expansion - End -

	## Despiel - Altar of Evil Faith
			if unit.getAfterlife() in (AfterlifeTypes.NO_AFTERLIFE, AfterlifeTypes.AFTERLIFE_RISE_OR_FALL):
# Kaijin >>>	patch29 expansion - Start -
				"""
				pCity = pPlot.getWorkingCity()
				if not pCity.isNone():
					eDespielAltar = gc.getInfoTypeForString('BUILDING_ALTAR_OF_EVIL_FAITH')
					if pCity.isHasActiveBuilding(eDespielAltar):
						iCityPlayer = pCity.getOwner()
						pCityPlayer = gc.getPlayer(iCityPlayer)
						iNum = (5 + (unit.getLevel() * unit.getLevel()))
						pCityPlayer.changeGold(iNum)

						szText = CyTranslator().getText("TXT_KEY_MESSAGE_SACRIFICE_GOLD",(unit.getNameKey(), pCity.getNameKey()))
						szButton = gc.getBuildingInfo(eDespielAltar).getButton()
						CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szText, 'AS2D_POSITIVE_DINK', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
						bCultureSoul = doConsumeLives(unit, True, False, bCultureSoul)
				"""
				bValid = 0
				eOwner = 0
				if pPlot.isOwned() and gc.getPlayer(pPlot.getOwner()).getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_PAGAN_TEMPLE')) > 0:
					if gc.getPlayer(pPlot.getOwner()).isAlive():
						eOwner = pPlot.getOwner()
						bValid = 1
				elif bCombatKilled:
					if gc.getPlayer(eKillerPlayer).getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_PAGAN_TEMPLE')) > 0:
						if gc.getPlayer(eKillerPlayer).isAlive():
							eOwner = eKillerPlayer
							bValid = 2

				if bValid:
					eBuilding = gc.getInfoTypeForString('BUILDING_ALTAR_OF_EVIL_FAITH')
					lpCity = []
					lpChosenCity = []
					for pyCity in PyPlayer(eOwner).getCityList():
						pCity = pyCity.GetCy()
						if pCity.isHasActiveBuilding(eBuilding):
							lpCity.append(pCity)
					if len(lpCity) > 0:
						pCity = lpCity[CyGame().getSorenRandNum(len(lpCity), "Chosen")]

						if bValid == 2:		#自領外では発生確率を低下
							iChance = 10
							iChance + (5 ** (gc.getPlayer(eOwner).getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_PAGAN_TEMPLE'))))
							if iChance > 50:
								iChance = 50
							if CyGame().getSorenRandNum(100, "chance") >= iChance:
								bValid = 0

						if bValid:
							iCityPlayer = pCity.getOwner()
							pCityPlayer = gc.getPlayer(iCityPlayer)
							iNum = (5 + (unit.getLevel() * unit.getLevel()))
							pCityPlayer.changeGold(iNum)

							szText = CyTranslator().getText("TXT_KEY_MESSAGE_SACRIFICE_GOLD",(unit.getNameKey(), pCity.getNameKey()))
							szButton = gc.getBuildingInfo(eBuilding).getButton()
							CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szText, 'AS2D_POSITIVE_DINK', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
							if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_SOUL_CULTURE_FACILITIES')):		#霊魂培養所による魂の残機増加
								bCultureSoul = True
							bCultureSoul = doConsumeLives(unit, False, True, bCultureSoul)
# Kaijin <<<	patch29 expansion - End -

	## Nougbii - Food storage
			if unit.getAfterlife() in (AfterlifeTypes.NO_AFTERLIFE, AfterlifeTypes.AFTERLIFE_RISE_OR_FALL):
				pCity = pPlot.getWorkingCity()
				if not pCity.isNone():
					if gc.getPlayer(pCity.getOwner()).getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_NOUGBII'):
						iNum = unit.getLevel() * unit.getLevel()
						pCity.changeFood(+iNum)
						szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_NOUGBII_FOOD_STRAGE', (pCity.getNameKey(), ))
						CyInterface().addMessage(pCity.getOwner(), True, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Symbols/Food/food05.dds', en.eColorGreen, pCity.getX(), pCity.getY(), True, True)
						bCultureSoul = doConsumeLives(unit, True, False, bCultureSoul)

	## Rarna - Reincarnation to Various things.
			if unit.getAfterlife() in (AfterlifeTypes.NO_AFTERLIFE, AfterlifeTypes.AFTERLIFE_PREYED) and CyGame().getProjectCreatedCount(gc.getInfoTypeForString('PROJECT_PRINCESS_OF_DARKNESS')) == 0:
				if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_RARNA'):
					if pPlayer.isAlive():
						if not unit.isSummoned():
							#転生確率の基礎値
							iChance = 50
							#殉教者の塔により転生確率+10～+30
							iChance += (pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_TOWER_OF_MARTYR')) * 10)
							#死亡ユニットはレベル1より高い場合、+1毎に転生確率-5%
							iChance += (-5 * unit.getLevel())
							if CyGame().getSorenRandNum(100, "Rarna Reincarnation") < iChance:
								pNewUnit = cf.doAfterLifeRarna(unit, pPlot, unit.getOwner(), unit.getExperience())
								if pNewUnit is not None:
									bCultureSoul = doConsumeLives(unit, False, True, bCultureSoul)

	## Rarna - Return of the soul.
			if unit.getAfterlife() in (AfterlifeTypes.NO_AFTERLIFE, AfterlifeTypes.AFTERLIFE_PREYED):
				if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_RARNA'):
					if pPlayer.isAlive():
						if not unit.isSummoned():

							iResearchTech = pPlayer.getCurrentResearch()
							if iResearchTech != TechTypes.NO_TECH:
								eAltar = gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_IMPORTANCE')
								iNum = pPlayer.countNumBuildings(eAltar)
								if iNum > 0:
									iNum *= (10 + (unit.getLevel() * unit.getLevel())) // 4
									pTeam = gc.getTeam(pPlayer.getTeam())
									pTeam.changeResearchProgress(iResearchTech, iNum, iPlayer)
									szText = CyTranslator().getText('TXT_KEY_MESSAGE_RETURN_OF_THE_SOUL', (unit.getNameKey(), ))
									szButton = gc.getBuildingInfo(eAltar).getButton()
									CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szText, 'AS2D_DISCOVERBONUS', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, unit.getX(), unit.getY(), True, True)
									bCultureSoul = doConsumeLives(unit, False, True, bCultureSoul)

	## Baldralfar - Reincarnation to Dryas.
			if unit.getAfterlife() in (AfterlifeTypes.NO_AFTERLIFE, AfterlifeTypes.AFTERLIFE_PREYED):
				if unit.getReligion() == gc.getInfoTypeForString('RELIGION_FELLOWSHIP_OF_LEAVES'):
					if CyGame().getSorenRandNum(100, "Dryas num") < 67:
						pNewUnit = cf.doAfterLifeBaldralfar(False, pPlot, unit.getOwner(), 0)
						if pNewUnit is not None:
							bCultureSoul = doConsumeLives(unit, False, True, bCultureSoul)

# Kaijin <<<

			if unit.getAfterlife() in (AfterlifeTypes.NO_AFTERLIFE, AfterlifeTypes.AFTERLIFE_PREYED):
				iNumManes = 0
				if unit.getReligion() != ReligionTypes.NO_RELIGION and gc.getReligionInfo(unit.getReligion()).getAlignment() == gc.getInfoTypeForString('ALIGNMENT_EVIL'):
					iNumManes = 2
				elif unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ENTROPY1')):
					iNumManes = 2
				elif unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_DEATH1')):
					iNumManes = 1
				if iNumManes > 0:
					pNewUnit = cf.doAfterLife(False, iNumManes, pPlot, unit, None, 0)
					if pNewUnit is not None:
						# Kaijin - Culture soul -
						"""
						unit.setAfterlife(AfterlifeTypes.AFTERLIFE_RISE_OR_FALL)
						"""
						bCultureSoul = doConsumeLives(unit, False, True, bCultureSoul)
						# Kaijin - End -

			if unit.getAfterlife() in (AfterlifeTypes.NO_AFTERLIFE, AfterlifeTypes.AFTERLIFE_PREYED):
				iNumAngel = 0
				if unit.getReligion() != ReligionTypes.NO_RELIGION and gc.getReligionInfo(unit.getReligion()).getAlignment() == gc.getInfoTypeForString('ALIGNMENT_GOOD'):
					iNumAngel = 1
				elif pPlayer.getCivilizationType() == en.eCivilizationMercurians and unit.getUnitCombatType() != gc.getInfoTypeForString('UNITCOMBAT_ANIMAL'):
					iNumAngel = 1
				if iNumAngel > 0:
					pNewUnit = cf.doAfterLife(True, iNumAngel, pPlot, unit, None, unit.getExperience())
					if pNewUnit is not None:
						# Kaijin - Culture soul -
						"""
						unit.setAfterlife(AfterlifeTypes.AFTERLIFE_RISE_OR_FALL)
						"""
						bCultureSoul = doConsumeLives(unit, False, True, bCultureSoul)
						# Kaijin - End -
##--------	Single Afterlife: End Modify		--------##

		if CyGame().getWBMapScript():
			sf.onUnitKilled(unit, iAttacker)

		if (not self.__LOG_UNITKILLED):
			return
		CvUtil.pyPrint('Player %d Civilization %s Unit %s was killed by Player %d'
			%(player.getID(), player.getCivilizationName(), PyInfo.UnitInfo(unit.getUnitType()).getDescription(), attacker.getID()))

##--------	Advanced Rules: Added by Denev	--------##
	def onUnitRebirth(self, argsList):
		genericArgs = argsList[0][0]
		unit = genericArgs[0]

		if unit.getLeaderUnitType() == gc.getInfoTypeForString('UNIT_COMMANDER'):
			if not unit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_GREAT_COMMANDER')):
				unit.setName('')
				unit.setLeaderUnitType(UnitTypes.NO_UNIT)
##--------	Advanced Rules: End Add			--------##

	def onUnitLost(self, argsList):
		'Unit Lost'
		unit = argsList[0]
		player = PyPlayer(unit.getOwner())
		if (not self.__LOG_UNITLOST):
			return
		CvUtil.pyPrint('%s was lost by Player %d Civilization %s'
			%(PyInfo.UnitInfo(unit.getUnitType()).getDescription(), player.getID(), player.getCivilizationName()))

	def onUnitPromoted(self, argsList):
		'Unit Promoted'
		pUnit, iPromotion = argsList
		player = PyPlayer(pUnit.getOwner())
		if (not self.__LOG_UNITPROMOTED):
			return
		CvUtil.pyPrint('Unit Promotion Event: %s - %s' %(player.getCivilizationName(), pUnit.getName(),))

	def onUnitSelected(self, argsList):
		'Unit Selected'
		unit = argsList[0]
		player = PyPlayer(unit.getOwner())
		if (not self.__LOG_UNITSELECTED):
			return
		CvUtil.pyPrint('%s was selected by Player %d Civilization %s'
			%(PyInfo.UnitInfo(unit.getUnitType()).getDescription(), player.getID(), player.getCivilizationName()))

	def onUnitRename(self, argsList):
		'Unit is renamed'
		pUnit = argsList[0]
		if (pUnit.getOwner() == gc.getGame().getActivePlayer()):
			self.__eventEditUnitNameBegin(pUnit)

	def onUnitPillage(self, argsList):
		'Unit pillages a plot'
		pUnit, iImprovement, iRoute, iOwner = argsList
		iPlotX = pUnit.getX()
		iPlotY = pUnit.getY()
		pPlot = CyMap().plot(iPlotX, iPlotY)
		pPlayer = gc.getPlayer(pUnit.getOwner())

		if (not self.__LOG_UNITPILLAGE):
			return
		CvUtil.pyPrint("Player %d's %s pillaged improvement %d and route %d at plot at (%d, %d)"
			%(iOwner, PyInfo.UnitInfo(pUnit.getUnitType()).getDescription(), iImprovement, iRoute, iPlotX, iPlotY))

	def onUnitSpreadReligionAttempt(self, argsList):
		'Unit tries to spread religion to a city'
		pUnit, iReligion, bSuccess = argsList

		iX = pUnit.getX()
		iY = pUnit.getY()
		pPlot = CyMap().plot(iX, iY)
		pCity = pPlot.getPlotCity()

	def onUnitGifted(self, argsList):
		'Unit is gifted from one player to another'
		pUnit, iGiftingPlayer, pPlotLocation = argsList

	def onUnitBuildImprovement(self, argsList):
		'Unit begins enacting a Build (building an Improvement or Route)'
		pUnit, iBuild, bFinished = argsList
# ent >>>
		if bFinished:
			if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_BASQUE'):
				if iBuild in (gc.getInfoTypeForString('BUILD_FISHING_BOATS'), gc.getInfoTypeForString('BUILD_WHALING_BOATS')):
					pPlayer = gc.getPlayer(pUnit.getOwner())
					pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_BASQUE'), pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.NO_DIRECTION)
					pNewUnit.convert(pUnit)
					pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_BASQUE'), True)
					pNewUnit.setUnitAIType(UnitAITypes.UNITAI_UNKNOWN)
					pNewUnit.getGroup().pushMission(MissionTypes.MISSION_SEAPATROL, 0, 0, 0, False, False, MissionAITypes.NO_MISSIONAI, pUnit.plot(), pUnit)
# ent <<<

	def onGoodyReceived(self, argsList):
		'Goody received'
		iPlayer, pPlot, pUnit, iGoodyType = argsList
		if (not self.__LOG_GOODYRECEIVED):
			return
		CvUtil.pyPrint('%s received a goody' %(gc.getPlayer(iPlayer).getCivilizationDescription(0)),)

	def onGreatPersonBorn(self, argsList):
		'Unit Promoted'
		pUnit, iPlayer, pCity = argsList
		player = PyPlayer(iPlayer)
		if pUnit.isNone() or pCity.isNone():
			return

#Kaijin >>>
		pPlayer = gc.getPlayer(iPlayer)
		## Lineage - Add a great commander.
		if pPlayer.getCivilizationType() == en.eCivilizationLineage:
			if CyGame().getSorenRandNum(100, "Commander born") < 33:
				if pUnit.getUnitClassType() in (	gc.getInfoTypeForString('UNITCLASS_ARTIST'), 
													gc.getInfoTypeForString('UNITCLASS_COMMANDER'), 
													gc.getInfoTypeForString('UNITCLASS_ENGINEER'), 
													gc.getInfoTypeForString('UNITCLASS_MERCHANT'), 
													gc.getInfoTypeForString('UNITCLASS_PROPHET'), 
													gc.getInfoTypeForString('UNITCLASS_SCIENTIST'), 
													gc.getInfoTypeForString('UNITCLASS_GARDENER')		):
					pCapitalPlot = pPlayer.getCapitalCity().plot()
					pNewUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_COMMANDER'), pCapitalPlot.getX(), pCapitalPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
# ent >>>
					pNewUnit.setUnitAIType(UnitAITypes.UNITAI_GENERAL)
# ent <<<
#Kaijin <<<

		if (not self.__LOG_GREATPERSON):
			return
		CvUtil.pyPrint('A %s was born for %s in %s' %(pUnit.getName(), player.getCivilizationName(), pCity.getName()))

	def onTechAcquired(self, argsList):
		'Tech Acquired'
		iTechType, iTeam, iPlayer, bAnnounce = argsList
		# Note that iPlayer may be NULL (-1) and not a refer to a player object
		pPlayer = gc.getPlayer(iPlayer)

		# Show tech splash when applicable
		if iPlayer != PlayerTypes.NO_PLAYER and bAnnounce and not CyInterface().noTechSplash():
			if (gc.getGame().isFinalInitialized() and not gc.getGame().GetWorldBuilderMode()):
				if ((not gc.getGame().isNetworkMultiPlayer()) and (iPlayer == gc.getGame().getActivePlayer())):
					popupInfo = CyPopupInfo()
					popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON_SCREEN)
					popupInfo.setData1(iTechType)
					popupInfo.setText(u"showTechSplash")
					popupInfo.addPopup(iPlayer)

##--------	Advanced Rules: Moved to DLL by Denev	--------##
					"""
		if iPlayer != PlayerTypes.NO_PLAYER and iPlayer != gc.getBARBARIAN_PLAYER():
			pPlayer = gc.getPlayer(iPlayer)
			for iReligion in xrange(gc.getNumReligionInfos()):
				if iTechType == gc.getReligionInfo(iReligion).getTechPrereq():
					iUnitClass = gc.getReligionInfo(iReligion).getFreeUnitClass()
					break
			else:
				iReligion = -1
			if iReligion != -1:
				if CyGame().isReligionFounded(iReligion):
					iUnit = gc.getCivilizationInfo(pPlayer.getCivilizationType()).getCivilizationUnits(iUnitClass)
					pNewUnit = cf.giftUnit(iPlayer, iUnit, 0)
					"""
##--------	Advanced Rules: End Move				--------##

##--------	Advanced Rules: Added by Denev	--------##
		if iTechType in (gc.getInfoTypeForString('TECH_MINING'), gc.getInfoTypeForString('TECH_BRONZE_WORKING'), gc.getInfoTypeForString('TECH_ARCHERY')):
			pBarbarianTeam = gc.getTeam(gc.getBARBARIAN_TEAM())
			if not pBarbarianTeam.isHasTech(iTechType):
				if (CyGame().countKnownTechNumTeams(iTechType) * 100 // CyGame().countCivTeamsEverAlive()) > 20:
					pBarbarianTeam.setHasTech(iTechType, True, PlayerTypes.NO_PLAYER, False, False)
##--------	Advanced Rules: End Add			--------##


#Kaijin >>>
		pCity = pPlayer.getCapitalCity()
		pPlot = pCity.plot()
		pTeam = gc.getTeam(iTeam)

		## LoopPlayers
		for iLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
			pLoopPlayer = gc.getPlayer(iLoopPlayer)
			if pLoopPlayer.isAlive():

				iLoopTeam = pLoopPlayer.getTeam()
				pLoopTeam = gc.getTeam(iLoopTeam)

				## Altair - Upgrade Metatoron
				if pLoopPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ALTAIR') and pLoopPlayer.getNumCities() > 0:
					if iLoopTeam == iTeam:
# ent >>>
						eMetatoronClass = gc.getInfoTypeForString('UNITCLASS_METATORON')
						eMetatoron = gc.getInfoTypeForString('UNIT_METATORON1')
						bPromotion = False
						if iTechType == gc.getInfoTypeForString('TECH_BRONZE_WORKING'):
							eMetatoron = gc.getInfoTypeForString('UNIT_METATORON2')
							bPromotion = True
						if iTechType == gc.getInfoTypeForString('TECH_IRON_WORKING'):
							eMetatoron = gc.getInfoTypeForString('UNIT_METATORON3')
							bPromotion = True
						if iTechType == gc.getInfoTypeForString('TECH_DIVINE_ESSENCE'):
							eMetatoron = gc.getInfoTypeForString('UNIT_METATORON4')
							bPromotion = True
						if bPromotion:
							for pUnit in PyPlayer(iLoopPlayer).getUnitList():
								if pUnit.getUnitClassType() == eMetatoronClass and pUnit.getUnitType() < eMetatoron:
									pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ELDER_DRAGON'), False)
									pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_GREATER_DRAGON'), False)
									pNewUnit = pLoopPlayer.initUnit(eMetatoron, pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
									pNewUnit.convert(pUnit)
									break
						"""
						if iTechType == gc.getInfoTypeForString('TECH_BRONZE_WORKING'):
							for pUnit in PyPlayer(iLoopPlayer).getUnitList():
								if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_METATORON1'):
									pNewUnit = pLoopPlayer.initUnit(gc.getInfoTypeForString('UNIT_METATORON2'), pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
									pNewUnit.convert(pUnit)
						if iTechType == gc.getInfoTypeForString('TECH_IRON_WORKING'):
							for pUnit in PyPlayer(iLoopPlayer).getUnitList():
								if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_METATORON2'):
									pNewUnit = pLoopPlayer.initUnit(gc.getInfoTypeForString('UNIT_METATORON3'), pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
									pNewUnit.convert(pUnit)
									pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ELDER_DRAGON'), False)
						if iTechType == gc.getInfoTypeForString('TECH_DIVINE_ESSENCE'):
							for pUnit in PyPlayer(iLoopPlayer).getUnitList():
								if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_METATORON3'):
									pNewUnit = pLoopPlayer.initUnit(gc.getInfoTypeForString('UNIT_METATORON4'), pUnit.getX(), pUnit.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
									pNewUnit.convert(pUnit)
									pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_GREATER_DRAGON'), False)
						"""
# ent <<<

				## Scions - Heroes
				if pLoopPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SCIONS') and pLoopPlayer.getNumCities() > 0:
					pLoopCity = pLoopPlayer.getCapitalCity()
					pLoopPlot = pLoopCity.plot()
					if iLoopTeam == iTeam:
						if iTechType == gc.getInfoTypeForString('TECH_CURRENCY'):
							pLoopPlayer.initUnit(gc.getInfoTypeForString('UNIT_PELEMOC'), pLoopPlot.getX(), pLoopPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

						if iTechType == gc.getInfoTypeForString('TECH_CODE_OF_LAWS'):
							pLoopPlayer.initUnit(gc.getInfoTypeForString('UNIT_MELANTE'), pLoopPlot.getX(), pLoopPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

						if iTechType == gc.getInfoTypeForString('TECH_KNOWLEDGE_OF_THE_ETHER'):
							pLoopPlayer.initUnit(gc.getInfoTypeForString('UNIT_ALCINUS'), pLoopPlot.getX(), pLoopPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

						if iTechType == gc.getInfoTypeForString('TECH_TRACKING'):
							pLoopPlayer.initUnit(gc.getInfoTypeForString('UNIT_THEMOCH'), pLoopPlot.getX(), pLoopPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

						if iTechType in (gc.getInfoTypeForString('TECH_BRONZE_WORKING'), gc.getInfoTypeForString('TECH_TRACKING')):
							for pUnit in PyPlayer(iLoopPlayer).getUnitList():
								if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_KORRINA'):
									pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HELD'), False)

				## Xoth - Sanity Point Decreased
				if pLoopPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_XOTH') and pLoopPlayer.getNumCities() > 0:
					if iLoopTeam == iTeam:
						if pLoopPlayer.getGuildPlusCounter(50) < 0:
							pLoopPlayer.setGuildPlusCounter(50, 0)
						elif pLoopPlayer.getGuildPlusCounter(50) > 0:
							pLoopPlayer.changeGuildPlusCounter(50, -1)

							pLoopCity = pLoopPlayer.getCapitalCity()
							szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_XOTH_SANITY_POINT_DECREASE', ('1', ))
							szButton = gc.getCivilizationInfo(gc.getInfoTypeForString('CIVILIZATION_XOTH')).getButton()
							CyGame().pushGameMessage(iLoopPlayer, True, szMessage, '', szButton, en.eColorGreen, pLoopCity.getX(), pLoopCity.getY(), True, True)

				## Trait Fool
				if pLoopPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_UNENLIGHTENED')):
					if iLoopTeam == iTeam:
						if CyGame().getSorenRandNum(1000, "Fool") <= 800:
							cf.doTraitFool(iLoopPlayer)

				## Visualization of gunpowder resources if you do not have the technology of alchemy.
				if (	pLoopPlayer.getCivilizationType() in [	gc.getInfoTypeForString('CIVILIZATION_KHAZAD'),
																gc.getInfoTypeForString('CIVILIZATION_LINEAGE'),
																gc.getInfoTypeForString('CIVILIZATION_MECHANOS')	]
						 and pLoopPlayer.getNumCities() > 0																):
					if iTechType == gc.getInfoTypeForString('TECH_IRON_WORKING'):
						if iLoopTeam == iTeam:
							if not pLoopTeam.isHasTech(gc.getInfoTypeForString('TECH_ALCHEMY')):
								iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(), 'EVENTTRIGGER_GUNPOWDER_REVEALED')
								triggerData = pPlayer.initTriggeredData(iEvent, True, -1, -1, -1, iPlayer, -1, -1, -1, -1, -1)

# Delete by ent >>>
				"""
				## It will give a Mobility1 to the Siege by Construction.
				if pLoopTeam.isHasTech(gc.getInfoTypeForString('TECH_CONSTRUCTION')):
					for pUnit in PyPlayer(iLoopPlayer).getUnitList():
						if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_SIEGE'):
							pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MOBILITY1'), True)
				"""
# <<<

# Kaijin >>>	patch29 expansion - Start -
				if pLoopPlayer.getBuildingClassCount(gc.getInfoTypeForString('BUILDINGCLASS_CELESTIAL_COMPASS')) > 0:
					if iLoopTeam == iTeam:
						liEvents = [	'EVENTTRIGGER_SIGN_AERON',
										'EVENTTRIGGER_SIGN_AGARES',
										'EVENTTRIGGER_SIGN_AMATHAON',
										'EVENTTRIGGER_SIGN_ARAWN',
										'EVENTTRIGGER_SIGN_BHALL',
										'EVENTTRIGGER_SIGN_CAMULOS',
										'EVENTTRIGGER_SIGN_CERIDWEN',
										'EVENTTRIGGER_SIGN_CERNUNNOS',
										'EVENTTRIGGER_SIGN_DAGDA',
										'EVENTTRIGGER_SIGN_DANALIN',
										'EVENTTRIGGER_SIGN_ESUS',
										'EVENTTRIGGER_SIGN_JUNIL',
										'EVENTTRIGGER_SIGN_KILMORPH',
										'EVENTTRIGGER_SIGN_LUGUS',
										'EVENTTRIGGER_SIGN_MAMMON',
										'EVENTTRIGGER_SIGN_MULCARN',
										'EVENTTRIGGER_SIGN_NANTOSUELTA',
										'EVENTTRIGGER_SIGN_OGHMA',
										'EVENTTRIGGER_SIGN_SIRONA',
										'EVENTTRIGGER_SIGN_SUCELLUS',
										'EVENTTRIGGER_SIGN_TALI'	]
						iChosenEvent = liEvents.pop( CyGame().getSorenRandNum(len(liEvents), "Seiza Gatya") )
						iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(), iChosenEvent)
						triggerData = pLoopPlayer.initTriggeredData(iEvent, True, -1, -1, -1, iPlayer, -1, -1, -1, -1, -1)
# Kaijin <<<	patch29 expansion - End -

		## Xoth - R'lyeh emerging
		if iTechType == gc.getInfoTypeForString('TECH_MIND_STAPLING') and iPlayer != PlayerTypes.NO_PLAYER:
			if CyGame().isOption(gc.getInfoTypeForString('GAMEOPTION_MODDER_1')):
				if CyGame().countKnownTechNumTeams(iTechType) == 1 and not CyGame().isUnitClassMaxedOut(gc.getInfoTypeForString('UNITCLASS_MYNOGHRA'), 0):
					iXothPlayer = pPlayer.initNewEmpire(gc.getInfoTypeForString('LEADER_HYDRA'), en.eCivilizationXoth)
					if iXothPlayer != PlayerTypes.NO_PLAYER:
						pXothPlayer = gc.getPlayer(iXothPlayer)

						pBestPlot = -1
						iBestValue = 0
						for i in xrange(CyMap().numPlots()):
							pPlot = CyMap().plotByIndex(i)
							if not pPlot.isWater():
								continue
							if pPlot.isOwned():
								continue
							if pPlot.getNumUnits() > 0:
								continue
							if pPlot.isImpassable():
								continue
							if pPlot.getImprovementType() != ImprovementTypes.NO_IMPROVEMENT:
								continue
							if pPlot.getBonusType(TeamTypes.NO_TEAM) != BonusTypes.NO_BONUS:
								continue
							bCannotConstruct = False
							lpAroundPlots = cyGetRangedPlots(pPlot, 2, True, False, TeamTypes.NO_TEAM)
							for pAroundPlot in lpAroundPlots:
								if pAroundPlot.isCity():
									bCannotConstruct = True
									break
							if bCannotConstruct:
								continue
							iValue = CyGame().getSorenRandNum(1000, "R'lyeh")
							#if pPlot.getTerrainType() == en.eTerrainOcean:
							#	iValue += 500
							if pPlot.getLatitude() < 30:
								iValue += 1500
							elif pPlot.getLatitude() < 60:
								iValue += 1000
							iValue += pPlot.area().getNumTiles() * 2
							iValue += pPlot.area().getNumUnownedTiles() * 10
							lpLargeAroundPlots = cyGetRangedPlots(pPlot, 3, False, False, TeamTypes.NO_TEAM)
							for pLargeAroundPlot in lpLargeAroundPlots:
								#if pLargeAroundPlot.isWater():
								#	iValue += 100
								#if not pLargeAroundPlot.isOwned():
								#	iValue += 100
								if pLargeAroundPlot.getBonusType(TeamTypes.NO_TEAM) != BonusTypes.NO_BONUS:
									iValue += 100
							if iValue > iBestValue:
								iBestValue = iValue
								pBestPlot = pPlot

						if pBestPlot != -1:
							pXothPlayer.setStartingPlot(pBestPlot, True)
							iFounderTeam = gc.getPlayer(iPlayer).getTeam()
							pFounderTeam = gc.getTeam(gc.getPlayer(iPlayer).getTeam())
							iXothTeam = gc.getPlayer(iXothPlayer).getTeam()
							pXothTeam = gc.getTeam(iXothTeam)

							iBarbTeam = gc.getBARBARIAN_TEAM()
							pXothTeam.makePeace(iBarbTeam)

							pXothPlayer.AI_changeAttitudeExtra(iPlayer, 4)

							iX = pBestPlot.getX()
							iY = pBestPlot.getY()


							pBestPlot.setPlotType(PlotTypes.PLOT_LAND, True, True)
							pBestPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
							pBestPlot.clearColdCounter()
							pBestPlot.setTerrainType(en.eTerrainGrass, True, True)
							if pBestPlot.getFeatureType() == gc.getInfoTypeForString('FEATURE_ICE'):
								pBestPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)

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
										if pAdjacentPlot.getOwner() != iXothPlayer:
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
										if pAdjacentPlot.getOwner() != iXothPlayer:
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

							eEffect = gc.getInfoTypeForString('EFFECT_SPRING')
							lszWaterBonus = [	'BONUS_CLAM', 'BONUS_CRAB', 'BONUS_FISH', 'BONUS_PEARL', 'BONUS_SHRIMP', 'BONUS_JADE', 'BONUS_WHALE'	]
							leDesertFeatures = [en.eFeatureFloodPlains, en.eFeatureOasis]
							eBurntForest = gc.getDefineINT('FLAMES_EXPIRE_EFFECT')
							lpWorkingPlots = cyGetRangedPlots(pBestPlot, 3, False, False, TeamTypes.NO_TEAM)
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
								else:
									pWorkingPlot.setTempTerrainType(TerrainTypes.NO_TERRAIN, 0)
									pWorkingPlot.setPlotCounter(0)
									pWorkingPlot.clearColdCounter()

									eFeature = pWorkingPlot.getFeatureType()
									if eFeature != FeatureTypes.NO_FEATURE:
										eUpgrade = gc.getFeatureInfo(eFeature).getFeatureUpgrade()
										if eUpgrade != FeatureTypes.NO_FEATURE:
											eStateReligion = gc.getFeatureInfo(eUpgrade).getPrereqStateReligion()
											if eStateReligion in (ReligionTypes.NO_RELIGION, pPlayer.getStateReligion()):
												pWorkingPlot.setFeatureType(eUpgrade, 0)
									if eFeature in (en.eFeatureJungle, en.eFeatureDeepJungle, en.eFeatureSwamp, en.eFeatureScrub):
										pWorkingPlot.setFeatureType(en.eFeatureForest, 0)
									elif eFeature in (en.eFeatureFlames, en.eFeatureHauntedLands):
										pWorkingPlot.setFeatureType(eBurntForest, 0)

									if pWorkingPlot.getTerrainType() == en.eTerrainSnow:
										pWorkingPlot.setTerrainType(en.eTerrainPlains, True, True)
									elif pWorkingPlot.getTerrainType() in (en.eTerrainTundra, en.eTerrainPlains, en.eTerrainMarsh):
										pWorkingPlot.setTerrainType(en.eTerrainGrass, True, True)
									elif pWorkingPlot.getTerrainType() == en.eTerrainDesert:
										if eFeature not in leDesertFeatures:
											pWorkingPlot.setTerrainType(en.eTerrainPlains, True, True)
									elif pWorkingPlot.getTerrainType() == en.eTerrainGrass:
										if pWorkingPlot.canHaveFeatureOnImprovement(en.eFeatureForest):
											pWorkingPlot.setFeatureType(en.eFeatureForest, 0)

									if pWorkingPlot.getImprovementType() == gc.getDefineINT('FLAMES_SPREAD_EFFECT'):
										pWorkingPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
									if eFeature != FeatureTypes.NO_FEATURE:
										if not gc.getFeatureInfo(eFeature).isTerrain(pWorkingPlot.getTerrainType()):
											pWorkingPlot.setFeatureType(FeatureTypes.NO_FEATURE, -1)

							pXothCity = pXothPlayer.initCity(iX, iY)
							pXothCity.setPopulation(5)
							iCulture = gc.getCultureLevelInfo(gc.getInfoTypeForString('CULTURELEVEL_REFINED')).getSpeedThreshold(CyGame().getGameSpeedType())
							pXothCity.setCulture(iXothPlayer, iCulture, True)
							pXothCity.setHasReligion(en.eReligionOctopusOverlords, True, True, True)
							pNewUnit = pXothPlayer.initUnit(gc.getInfoTypeForString('UNIT_MYNOGHRA'), iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
							pNewUnit.setHasCasted(True)
							eMobility1		= gc.getInfoTypeForString('PROMOTION_MOBILITY1')
							eWaterWalking		= gc.getInfoTypeForString('PROMOTION_WATER_WALKING')
							eSettlerBonus	= gc.getInfoTypeForString('PROMOTION_STARTING_SETTLER')
							leStartingUnits = [	(2,	gc.getInfoTypeForString('UNIT_SHOGGOTH'),	[eMobility1]				),
												(3,	gc.getInfoTypeForString('UNIT_SLAVE'),		[eWaterWalking]							),
												(2,	gc.getInfoTypeForString('UNIT_PRIEST_OF_THE_OVERLORDS'),		[]				),
												(1,	gc.getInfoTypeForString('UNIT_SETTLER'),		[eSettlerBonus]				),
												(4,	gc.getInfoTypeForString('UNIT_GREATRACE'),		[eMobility1]							),
												(2,	gc.getInfoTypeForString('UNIT_CARAVEL'),	[]				)	]
							for iNumUnits, eUnit, lePromotions in leStartingUnits:
								for iLoop in xrange(iNumUnits):
									pNewUnit = pXothPlayer.initUnit(eUnit, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
									for ePromotion in lePromotions:
										pNewUnit.setHasPromotion(ePromotion, True)

							pXothTeam.signOpenBorders(iFounderTeam)
							pXothTeam.signDefensivePact(iFounderTeam)
							for iPlotIndex in xrange(CyMap().numPlots()):
								pLoopPlot = CyMap().plotByIndex(iPlotIndex)
								if pLoopPlot.isRevealed(iFounderTeam, False):
									pLoopPlot.setRevealed(iXothTeam, True, False, iFounderTeam)
								if pLoopPlot.isRevealed(iXothTeam, False):
									pLoopPlot.setRevealed(iFounderTeam, True, False, iXothTeam)
							for iLoopTeam in xrange(gc.getMAX_CIV_TEAMS()):
								pLoopTeam = gc.getTeam(iLoopTeam)
								if pLoopTeam.isAlive():
									if pLoopTeam.isHasMet(iFounderTeam):
										pLoopTeam.meet(iXothTeam, True)
							for iTeam in xrange(gc.getMAX_CIV_TEAMS()):
								pLoopTeam = gc.getTeam(iTeam)
								if pLoopTeam.isAlive():
									if pFounderTeam.isAtWar(iTeam):
										pXothTeam.declareWar(iTeam, False, WarPlanTypes.WARPLAN_LIMITED)

							if not pXothTeam.isHasTech(gc.getInfoTypeForString('TECH_SEAFARING')):
								pXothTeam.setHasTech(gc.getInfoTypeForString('TECH_SEAFARING'), True, iXothPlayer, False, True)

							## Globalcounter initialization
							cf.doGlobalcounterInitialization(iXothPlayer)

							if gc.getPlayer(iPlayer).isHuman():
								popupInfo = CyPopupInfo()
								popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
								popupInfo.setText(CyTranslator().getText("TXT_KEY_POPUP_CONTROL_XOTH", ()))
								popupInfo.setData1(iPlayer)
								popupInfo.setData2(iXothPlayer)
								popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_POPUP_YES", ()), "")
								popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_POPUP_NO", ()), "")
								popupInfo.setOnClickedPythonCallback("reassignPlayer")
								popupInfo.addPopup(iPlayer)

#Kaijin <<<

		if iTechType == gc.getInfoTypeForString('TECH_INFERNAL_PACT') and iPlayer != PlayerTypes.NO_PLAYER:
			if not gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_HYBOREM_OR_BASIUM):
				if CyGame().countKnownTechNumTeams(iTechType) == 1 and not CyGame().isUnitClassMaxedOut(gc.getInfoTypeForString('UNITCLASS_HYBOREM'), 0):
					iInfernalPlayer = pPlayer.initNewEmpire(gc.getInfoTypeForString('LEADER_HYBOREM'), en.eCivilizationInfernal)
					if iInfernalPlayer != PlayerTypes.NO_PLAYER:
						pInfernalPlayer = gc.getPlayer(iInfernalPlayer)

						pBestPlot = -1
						iBestPlot = -1
						for iPlotIndex in range (CyMap().numPlots()):
							pPlot = CyMap().plotByIndex(iPlotIndex)
							iPlot = -1
							if pInfernalPlayer.canFound(pPlot.getX(), pPlot.getY()):
								if pPlot.getNumUnits() == 0:
									iPlot = CyGame().getSorenRandNum(500, "Place Hyborem")
									iPlot += pPlot.area().getNumTiles() * 2
									iPlot += pPlot.area().getNumUnownedTiles() * 10
									if not pPlot.isOwned():
										iPlot += 500
							if iPlot > iBestPlot:
								iBestPlot = iPlot
								pBestPlot = pPlot

						if pBestPlot != -1:
##--------	Unofficial Bug Fix: Added by Denev	--------##
							pInfernalPlayer.setStartingPlot(pBestPlot, True)
##--------	Unofficial Bug Fix: End Add			--------##
							eFounderTeam = gc.getPlayer(iPlayer).getTeam()
							pFounderTeam = gc.getTeam(eFounderTeam)
							eInfernalTeam = gc.getPlayer(iInfernalPlayer).getTeam()
							pInfernalTeam = gc.getTeam(eInfernalTeam)

							eBarbTeam = gc.getBARBARIAN_TEAM()
							eDemonBarbTeam = eBarbTeam + gc.getInfoTypeForString('BARBARIAN_DEMONS')
							pInfernalTeam.makePeace(eBarbTeam)
							pInfernalTeam.makePeace(eDemonBarbTeam)

							pInfernalPlayer.AI_changeAttitudeExtra(iPlayer, 4)

							iX = pBestPlot.getX()
							iY = pBestPlot.getY()
							pNewUnit = pInfernalPlayer.initUnit(gc.getInfoTypeForString('UNIT_HYBOREM'), iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
							pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_IMMORTAL'), True)
							pNewUnit.setHasCasted(True)
							pNewUnit.setAvatarOfCivLeader(True)
							eIronWeapon		= gc.getInfoTypeForString('PROMOTION_IRON_WEAPONS')
							eMobility1		= gc.getInfoTypeForString('PROMOTION_MOBILITY1')
							eSettlerBonus	= gc.getInfoTypeForString('PROMOTION_STARTING_SETTLER')
							ltStartingUnits = [	(2,	gc.getInfoTypeForString('UNIT_LONGBOWMAN'),	[eMobility1]				),
												(2,	gc.getInfoTypeForString('UNIT_TORTURER'),	[eMobility1, eIronWeapon]	),
												(1,	gc.getInfoTypeForString('UNIT_WORKER'),		[]							),
												(1,	gc.getInfoTypeForString('UNIT_IMP'),		[eMobility1]				),
												(3,	gc.getInfoTypeForString('UNIT_MANES'),		[]							),
												(2,	gc.getInfoTypeForString('UNIT_SETTLER'),	[eSettlerBonus]				)	]
							for iNumUnits, eUnit, lePromotions in ltStartingUnits:
								for iLoop in xrange(iNumUnits):
									pNewUnit = pInfernalPlayer.initUnit(eUnit, iX, iY, UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_NORTH)
									for ePromotions in lePromotions:
										pNewUnit.setHasPromotion(ePromotions, True)

							pInfernalTeam.signOpenBorders(eFounderTeam)
							pInfernalTeam.signDefensivePact(eFounderTeam)
							for iPlotIndex in xrange(CyMap().numPlots()):
								pLoopPlot = CyMap().plotByIndex(iPlotIndex)
								if pLoopPlot.isRevealed(eFounderTeam, False):
									pLoopPlot.setRevealed(eInfernalTeam, True, False, eFounderTeam)
								if pLoopPlot.isRevealed(eInfernalTeam, False):
									pLoopPlot.setRevealed(eFounderTeam, True, False, eInfernalTeam)
							for eLoopTeam in xrange(gc.getMAX_CIV_TEAMS()):
								pLoopTeam = gc.getTeam(eLoopTeam)
								if pLoopTeam.isAlive():
									if pLoopTeam.isHasMet(eFounderTeam):
										pInfernalTeam.meet(eLoopTeam, True)
									if pLoopTeam.isAtWar(eFounderTeam):
										pInfernalTeam.declareWar(eLoopTeam, False, WarPlanTypes.WARPLAN_LIMITED)

							pInfernalPlayer.AI_updateFoundValues(False)

#Kaijin >>>
							## Globalcounter initialization
							cf.doGlobalcounterInitialization(iInfernalPlayer)
#Kaijin <<<
# ent: 初手奨学金制採用におけるストライキ対策 >>>
							iGold = cyFlatValue(200, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
							pInfernalPlayer.changeGold(iGold)
# ent <<<
							if gc.getPlayer(iPlayer).isHuman():
								popupInfo = CyPopupInfo()
								popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON)
								popupInfo.setText(CyTranslator().getText("TXT_KEY_POPUP_CONTROL_INFERNAL", ()))
								popupInfo.setData1(iPlayer)
								popupInfo.setData2(iInfernalPlayer)
								popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_POPUP_YES", ()), "")
								popupInfo.addPythonButton(CyTranslator().getText("TXT_KEY_POPUP_NO", ()), "")
								popupInfo.setOnClickedPythonCallback("reassignPlayer")
								popupInfo.addPopup(iPlayer)

# ent - Religious Era is not last one. (Ancient < Classical < Religious < Medieval < Future < StateReligiousEras) >>>
		eEraReligious = gc.getInfoTypeForString('ERA_RELIGIOUS')
		if pPlayer.getCurrentEra() == eEraReligious:
			eLastEra = gc.getInfoTypeForString('ERA_ANCIENT')
			for eTech in xrange(gc.getNumTechInfos()):
				if pPlayer.isHasTech(eTech):
					eEra = gc.getTechInfo(eTech).getEra()
					if eEra > eLastEra and eEra != eEraReligious:
						eLastEra = eEra
			if eLastEra <= gc.getInfoTypeForString('ERA_CLASSICAL'):
				eLastEra = eEraReligious
			pPlayer.setCurrentEra(eLastEra)
# ent <<<

		if CyGame().getWBMapScript():
			sf.onTechAcquired(iTechType, iTeam, iPlayer, bAnnounce)

		if (not self.__LOG_TECH):
			return
		CvUtil.pyPrint('%s was finished by Team %d'
			%(PyInfo.TechnologyInfo(iTechType).getDescription(), iTeam))

	def onTechSelected(self, argsList):
		'Tech Selected'
		iTechType, iPlayer = argsList
		if (not self.__LOG_TECH):
			return
		CvUtil.pyPrint('%s was selected by Player %d' %(PyInfo.TechnologyInfo(iTechType).getDescription(), iPlayer))

	def onReligionFounded(self, argsList):
		'Religion Founded'
		iReligion, iFounder = argsList
		player = PyPlayer(iFounder)
		pPlayer = gc.getPlayer(iFounder)

		iCityId = gc.getGame().getHolyCity(iReligion).getID()
		if (gc.getGame().isFinalInitialized() and not gc.getGame().GetWorldBuilderMode()):
			if ((not gc.getGame().isNetworkMultiPlayer()) and (iFounder == gc.getGame().getActivePlayer())):
				popupInfo = CyPopupInfo()
				popupInfo.setButtonPopupType(ButtonPopupTypes.BUTTONPOPUP_PYTHON_SCREEN)
				popupInfo.setData1(iReligion)
				popupInfo.setData2(iCityId)
				if (iReligion == gc.getInfoTypeForString('RELIGION_THE_EMPYREAN') or iReligion == gc.getInfoTypeForString('RELIGION_COUNCIL_OF_ESUS')):
					popupInfo.setData3(3)
				else:
					popupInfo.setData3(1)
				popupInfo.setText(u"showWonderMovie")
				popupInfo.addPopup(iFounder)

#Kaijin >>>
## Trait Faith - 宗教創始により黄金期に突入
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_FAITH')):
			pPlayer.changeGoldenAgeTurns(CyGame().goldenAgeLength())

## CivGoldEmpires - Trait Iron Will 宗教創始時の自動的な布教
		for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
			pLoopPlayer = gc.getPlayer(iLoopPlayer)
			if pLoopPlayer.isAlive():
				if iLoopPlayer == iFounder:
					for pyCity in PyPlayer(iLoopPlayer).getCityList():
						pCity = pyCity.GetCy()
						if pLoopPlayer.hasTrait(gc.getInfoTypeForString("TRAIT_IRON_WILL")):
							if not pCity.isHolyCityByType(iReligion):
								if CyGame().getSorenRandNum(100, "Chance to get Religion") <= 50:
									pCity.setHasReligion(iReligion, True, True, True)
#Kaijin <<<

		if CyGame().getWBMapScript():
			sf.onReligionFounded(iReligion, iFounder)

		if (not self.__LOG_RELIGION):
			return
		CvUtil.pyPrint('Player %d Civilization %s has founded %s'
			%(iFounder, player.getCivilizationName(), gc.getReligionInfo(iReligion).getDescription()))

	def onReligionSpread(self, argsList):
		'Religion Has Spread to a City'
		iReligion, iOwner, pSpreadCity = argsList
		player = PyPlayer(iOwner)
		iOrder = gc.getInfoTypeForString('RELIGION_THE_ORDER')
		pPlayer = gc.getPlayer(iOwner)

		if iReligion == iOrder and CyGame().getGameTurn() != CyGame().getStartTurn():
			if (pPlayer.getStateReligion() == iOrder and pSpreadCity.getOccupationTimer() <= 0):
				if (CyGame().getSorenRandNum(100, "Order Spawn") < gc.getDefineINT('ORDER_SPAWN_CHANCE')):
					pTeam = gc.getTeam(pPlayer.getTeam())
					if pTeam.isHasTech(gc.getInfoTypeForString('TECH_FANATICISM')):
						iUnit = gc.getInfoTypeForString('UNIT_CRUSADER')
						CyInterface().addMessage(iOwner, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_ORDER_SPAWN_CRUSADER", ()), 'AS2D_UNIT_BUILD_UNIT', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Units/Crusader.dds', en.eColorGreen, pSpreadCity.getX(), pSpreadCity.getY(), True, True)
					else:
						iUnit = gc.getInfoTypeForString('UNIT_DISCIPLE_THE_ORDER')
						CyInterface().addMessage(iOwner, True, gc.getEVENT_MESSAGE_TIME(), CyTranslator().getText("TXT_KEY_MESSAGE_ORDER_SPAWN_ACOLYTE", ()), 'AS2D_UNIT_BUILD_UNIT', InterfaceMessageTypes.MESSAGE_TYPE_INFO, 'Art/Interface/Buttons/Units/Disciple Order.dds', en.eColorGreen, pSpreadCity.getX(), pSpreadCity.getY(), True, True)
					pNewUnit = pPlayer.initUnit(iUnit, pSpreadCity.getX(), pSpreadCity.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

		if (not self.__LOG_RELIGIONSPREAD):
			return
		CvUtil.pyPrint('%s has spread to Player %d Civilization %s city of %s'
			%(gc.getReligionInfo(iReligion).getDescription(), iOwner, player.getCivilizationName(), pSpreadCity.getName()))

	def onReligionRemove(self, argsList):
		'Religion Has been removed from a City'
		iReligion, iOwner, pRemoveCity = argsList
		player = PyPlayer(iOwner)
		if (not self.__LOG_RELIGIONSPREAD):
			return
		CvUtil.pyPrint('%s has been removed from Player %d Civilization %s city of %s'
			%(gc.getReligionInfo(iReligion).getDescription(), iOwner, player.getCivilizationName(), pRemoveCity.getName()))

	def onCorporationFounded(self, argsList):
		'Corporation Founded'
		iCorporation, iFounder = argsList
		player = PyPlayer(iFounder)
		if (not self.__LOG_RELIGION):
			return
		CvUtil.pyPrint('Player %d Civilization %s has founded %s'
			%(iFounder, player.getCivilizationName(), gc.getCorporationInfo(iCorporation).getDescription()))

	def onCorporationSpread(self, argsList):
		'Corporation Has Spread to a City'
		iCorporation, iOwner, pSpreadCity = argsList
		player = PyPlayer(iOwner)
		if (not self.__LOG_RELIGIONSPREAD):
			return
		CvUtil.pyPrint('%s has spread to Player %d Civilization %s city of %s'
			%(gc.getCorporationInfo(iCorporation).getDescription(), iOwner, player.getCivilizationName(), pSpreadCity.getName()))

	def onCorporationRemove(self, argsList):
		'Corporation Has been removed from a City'
		iCorporation, iOwner, pRemoveCity = argsList
		player = PyPlayer(iOwner)
		if (not self.__LOG_RELIGIONSPREAD):
			return
		CvUtil.pyPrint('%s has been removed from Player %d Civilization %s city of %s'
			%(gc.getReligionInfo(iReligion).getDescription(), iOwner, player.getCivilizationName(), pRemoveCity.getName()))

	def onGoldenAge(self, argsList):
		'Golden Age'
		iPlayer = argsList[0]
		player = PyPlayer(iPlayer)
		if (not self.__LOG_GOLDENAGE):
			return
		CvUtil.pyPrint('Player %d Civilization %s has begun a golden age'
			%(iPlayer, player.getCivilizationName()))

	def onEndGoldenAge(self, argsList):
		'End Golden Age'
		iPlayer = argsList[0]
		player = PyPlayer(iPlayer)
		if (not self.__LOG_ENDGOLDENAGE):
			return
		CvUtil.pyPrint('Player %d Civilization %s golden age has ended'
			%(iPlayer, player.getCivilizationName()))

	def onChangeWar(self, argsList):
		'War Status Changes'
		bIsWar = argsList[0]
		iTeam = argsList[1]
		iRivalTeam = argsList[2]
		if (not self.__LOG_WARPEACE):
			return
		if (bIsWar):
			strStatus = "declared war"
		else:
			strStatus = "declared peace"
		CvUtil.pyPrint('Team %d has %s on Team %d'
			%(iTeam, strStatus, iRivalTeam))

	def onChat(self, argsList):
		'Chat Message Event'
		chatMessage = "%s" %(argsList[0],)

	def onSetPlayerAlive(self, argsList):
		'Set Player Alive Event'
		iPlayerID = argsList[0]
		bNewValue = argsList[1]
		CvUtil.pyPrint("Player %d's alive status set to: %d" %(iPlayerID, int(bNewValue)))

##--------	Cold Counter: Added by Denev	--------##
# Temp Delete
		"""
		if not bNewValue:
			eIllians = gc.getInfoTypeForString('CIVILIZATION_ILLIANS')
			if gc.getPlayer(iPlayerID).getCivilizationType() == eIllians:
				if CyGame().getProjectCreatedCount(gc.getInfoTypeForString('PROJECT_THE_DEEPENING')) > 0:
					for iLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
						if gc.getPlayer(iLoopPlayer).isAlive():
							if gc.getPlayer(iLoopPlayer).getCivilizationType() == eIllians:
								if iLoopPlayer != iPlayerID:
									break
					else:
						CyGame().changeIceAge(-1)
		"""
##--------	Cold Counter: End Add			--------##

##--------	TradeResourcePanel: Added by Denev	--------##
		if CyGame().isFinalInitialized():
			tr.rebuildCivTechResPanel()
##--------	TradeResourcePanel: End Add			--------##

##--------	Advanced Rules: Added by Denev	--------##
		pPlayer = gc.getPlayer(iPlayerID)
		if not bNewValue:
			if pPlayer.getAlignment() == gc.getInfoTypeForString('ALIGNMENT_GOOD'):
				CyGame().changeGlobalCounter(6)
			elif pPlayer.getAlignment() == gc.getInfoTypeForString('ALIGNMENT_EVIL'):
				CyGame().changeGlobalCounter(-2)
			else:
				CyGame().changeGlobalCounter(2)

			if gc.getPlayer(iPlayerID).getLeaderType() == gc.getInfoTypeForString('LEADER_HYBOREM'):
				CyGame().incrementBuildingClassCreatedCount(gc.getInfoTypeForString('BUILDINGCLASS_MERCURIAN_GATE'))
##--------	Advanced Rules: End Add			--------##

		if (not bNewValue and gc.getGame().getGameTurnYear() >= 5):
			if CyGame().getWBMapScript():
				sf.playerDefeated(pPlayer)
			else:
				eLeader = pPlayer.getLeaderType()
				if eLeader == gc.getInfoTypeForString('LEADER_ALEXIS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_CALABIM", ()), 'art/interface/popups/Alexis.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_AMELANCHIER'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LJOSALFAR", ()), 'art/interface/popups/Amelanchier.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ARENDEL'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LJOSALFAR", ()), 'art/interface/popups/Arendel.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ARTURUS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KHAZAD", ()), 'art/interface/popups/Arturus.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_AURIC'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_ILLIANS", ()), 'art/interface/popups/Auric.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_BASIUM'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_MERCURIANS", ()), 'art/interface/popups/Basium.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_BEERI'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LUCHUIRP", ()), 'art/interface/popups/Beeri.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_CAPRIA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_BANNOR", ()), 'art/interface/popups/Capria.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_CARDITH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KURIOTATES", ()), 'art/interface/popups/Cardith.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_CASSIEL'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_GRIGORI", ()), 'art/interface/popups/Cassiel.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_CHARADON'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_DOVIELLO", ()), 'art/interface/popups/Charadon.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_DAIN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_AMURITES", ()), 'art/interface/popups/Dain.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_DECIUS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_DECIUS", ()), 'art/interface/popups/Decius.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_EINION'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_ELOHIM", ()), 'art/interface/popups/Einion.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ETHNE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_ELOHIM", ()), 'art/interface/popups/Ethne.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_FAERYL'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SVARTALFAR", ()), 'art/interface/popups/Faeryl.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_FALAMAR'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LANUN", ()), 'art/interface/popups/Falamar.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_FLAUROS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_CALABIM", ()), 'art/interface/popups/Flauros.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_GARRIM'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LUCHUIRP", ()), 'art/interface/popups/Garrim.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_HANNAH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HANNAH", ()), 'art/interface/popups/Hannah.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_HYBOREM'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_INFERNAL", ()), 'art/interface/popups/Hyborem.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_JONAS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_CLAN_OF_EMBERS", ()), 'art/interface/popups/Jonus.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_KANDROS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KHAZAD", ()), 'art/interface/popups/Kandros.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_KEELYN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KEELYN", ()), 'art/interface/popups/Keelyn.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_MAHALA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_DOVIELLO", ()), 'art/interface/popups/Mahala.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_SANDALPHON'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SIDAR", ()), 'art/interface/popups/Sandalphon.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_OS-GABELLA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SHEAIM", ()), 'art/interface/popups/Os-Gabella.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_PERPENTACH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_BALSERAPHS", ()), 'art/interface/popups/Perpentach.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_RHOANNA'):
#Localize: Modified by anonymous
#					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HIPPUS", ()), 'art/interface/popups/Rhoanna.dds')
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_RHOANNA", ()),'art/interface/popups/Rhoanna.dds')
#Localize: End Modify
				elif eLeader == gc.getInfoTypeForString('LEADER_SABATHIEL'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_BANNOR", ()), 'art/interface/popups/Sabathiel.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_SHEELBA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_CLAN_OF_EMBERS", ()), 'art/interface/popups/Sheelba.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_TASUNKE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HIPPUS", ()), 'art/interface/popups/Tasunke.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_TEBRYN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SHEAIM", ()), 'art/interface/popups/Tebryn.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_THESSA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LJOSALFAR", ()), 'art/interface/popups/Thessa.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_VALLEDIA'):
#Localize: Modified by anonymous
#					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_AMURITES", ()), 'art/interface/popups/Valledia.dds')
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_VALLEDIA", ()),'art/interface/popups/Valledia.dds')
#Localize: End Modify
				elif eLeader == gc.getInfoTypeForString('LEADER_VARN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_MALAKIM", ()), 'art/interface/popups/Varn.dds')

# Kaijin >>>
	# Amurites
				elif eLeader == gc.getInfoTypeForString('LEADER_TYA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_TYA",()),'Art/Interface/Popups/Tya.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_GWYEN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_AMURITES",()),'Art_Kaijin/Interface/Popups/GwyenPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_VERLAIN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_AMURITES",()), 'Art_Kaijin/Interface/Popups/verlain_banner.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_LORELEI'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_VALLEDIA",()), 'Art_Kaijin/Interface/Popups/lorelei_banner.dds')
	# Balseraphs
				elif eLeader == gc.getInfoTypeForString('LEADER_WEEVIL'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_WEEVIL",()),'Art/Interface/Popups/Weevil.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_FURIA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_FURIA",()),'Art/Interface/Popups/Furia.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_MELISANDRE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_MELISANDRE",()),'Art/Interface/Popups/Melisandre.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_TALIESIN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_BALSERAPHS",()),'Art_Kaijin/Interface/Popups/TaliesinPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NOJAH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_WEEVIL",()),'Art_Kaijin/Interface/Popups/nojah_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NELL'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_MELISANDRE",()),'Art_Kaijin/Interface/Popups/nell_banner.dds')
	# Bannor
				elif eLeader == gc.getInfoTypeForString('LEADER_TETHIRA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_BANNOR",()),'Art/Interface/Popups/Tethira.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_GAHERIS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_BANNOR",()),'Art_Kaijin/Interface/Popups/GaherisPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ANGAAD'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_BANNOR",()), 'Art_Kaijin/Interface/Popups/angaad_banner.dds')
	# Calabim
				elif eLeader == gc.getInfoTypeForString('LEADER_MAHON'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_CALABIM",()),'Art/Interface/Popups/Mahon.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NERGAL'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_CALABIM",()),'Art_Kaijin/Interface/Popups/NergalPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ELENA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_CALABIM",()), 'Art_Kaijin/Interface/Popups/kromear_banner.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ELIJAH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_CALABIM",()), 'Art_Kaijin/Interface/Popups/elijah_banner.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_AILIMER'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_CALABIM",()),'Art_Kaijin/Interface/Popups/Remilia_pop.dds')
	# Clan of Embers
				elif eLeader == gc.getInfoTypeForString('LEADER_HAFGAN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_CLAN_OF_EMBERS",()),'Art/Interface/Popups/Barbarian.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_AZZAN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_CLAN_OF_EMBERS",()),'Art_Kaijin/Interface/Popups/AzzanPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_JI'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_CLAN_OF_EMBERS",()), 'Art_Kaijin/Interface/Popups/ji_banner.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_HEHNKU'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_CLAN_OF_EMBERS",()), 'Art_Kaijin/Interface/Popups/hehnku_banner.dds')
	# Doviello
				elif eLeader == gc.getInfoTypeForString('LEADER_DUIN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_DOVIELLO",()),'Art/Interface/Popups/Baron Duin Halfmorn.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_BYGGVIR'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_DOVIELLO",()),'Art_Kaijin/Interface/Popups/ByggvirPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_SIRVAGHA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_DOVIELLO",()), 'Art_Kaijin/Interface/Popups/sirvagha_banner.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_EMMA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_DOVIELLO", ()), 'Art_Kaijin/Interface/Popups/emma_banner.dds')
	# Elohim
				elif eLeader == gc.getInfoTypeForString('LEADER_THESSALONICA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_ELOHIM",()),'Art/Interface/Popups/Thessalonica.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NEPHELE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_ELOHIM",()),'Art_Kaijin/Interface/Popups/NephelePopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_MEELAIS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_ELOHIM",()), 'Art_Kaijin/Interface/Popups/meelais_banner.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_VESTA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_ELOHIM",()),'Art_Kaijin/Interface/Popups/Vesta_pop.dds')
	# Grigori
				elif eLeader == gc.getInfoTypeForString('LEADER_KOUN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KOUN",()),'Art/Interface/Popups/Koun.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_GOLBEZ'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_GRIGORI",()),'Art_Kaijin/Interface/Popups/Golbez_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_MELISSA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_GRIGORI",()),'Art_Kaijin/Interface/Popups/Melissa_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_GOODREAU'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_GRIGORI",()),'Art_Kaijin/addition/original/goodreau/goodreau_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_MENEC'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_GRIGORI",()), 'Art_Kaijin/Interface/Popups/menec_banner.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ZODALORE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_GRIGORI",()), 'Art_Kaijin/Interface/Popups/zodalore_banner.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_OUTHE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_GRIGORI",()), 'Art_Kaijin/Interface/Popups/outhe_banner.dds')
	# Hippus
				elif eLeader == gc.getInfoTypeForString('LEADER_OSTANES'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HIPPUS",()),'Art/Interface/Popups/Ostanes.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ULDANOR'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HIPPUS",()),'Art/Interface/Popups/Uldanor.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_SELMA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_RHOANNA",()),'Art_Kaijin/Interface/Popups/SelmaPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ILITHIRIDAN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_RHOANNA",()),'Art_Kaijin/Interface/Popups/ilithiridan_banner.dds')
	# Illians
				elif eLeader == gc.getInfoTypeForString('LEADER_BRAEDEN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_BRAEDEN",()),'Art/Interface/Popups/Braeden.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_DUMANNIOS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_PRIESTS_OF_WINTER",()),'Art/Interface/Popups/Dumannios.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ANAGANTIOS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_PRIESTS_OF_WINTER",()),'Art/Interface/Popups/Anagantios.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_RIUROS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_PRIESTS_OF_WINTER",()),'Art/Interface/Popups/Riuros.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_RAITLOR'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_PRIESTS_OF_WINTER",()), 'Art_Kaijin/Interface/Popups/raitlor_banner.dds')
	# Infernal
				elif eLeader == gc.getInfoTypeForString('LEADER_JUDECCA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_INFERNAL",()),'Art/Interface/Popups/Judecca.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_SALLOS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_INFERNAL",()),'Art/Interface/Popups/Sallos.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_OUZZA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_INFERNAL",()),'Art/Interface/Popups/Ouzza.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_MERESIN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_INFERNAL",()),'Art/Interface/Popups/Meresin.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_STATIUS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_INFERNAL",()),'Art/Interface/Popups/Statius.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_LETHE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_INFERNAL",()),'Art/Interface/Popups/Lethe.dds')
	# Khazad
				elif eLeader == gc.getInfoTypeForString('LEADER_NICODEMUS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KHAZAD",()),'Art_Kaijin/Interface/Popups/NicodemusPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ATHEL'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KHAZAD",()),'Art_Kaijin/addition/original/athel/athel_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_VITNIR'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KHAZAD",()), 'Art_Kaijin/Interface/Popups/vitnir_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_LLAMERADA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KHAZAD",()), 'Art_Kaijin/Interface/Popups/Llamerada_pop.dds')
	# Kuritates
				elif eLeader == gc.getInfoTypeForString('LEADER_TEACHER'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_TEACHER",()),'Art_Kaijin/Interface/Popups/Teacher_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_FAVNA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KURIOTATES",()),'Art_Kaijin/Interface/Popups/FavnaPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_HYUNKEL'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KURIOTATES",()),'Art_Kaijin/Interface/Popups/HyunkelPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_HERNE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KURIOTATES",()), 'Art_Kaijin/Interface/Popups/herne_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_CITH_MOR'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KURIOTATES",()), 'Art_Kaijin/Interface/Popups/cith_mor_banner.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_CHERON'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KURIOTATES",()), 'Art_Kaijin/Interface/Popups/cheron_pop.dds')
	# Lanun
				elif eLeader == gc.getInfoTypeForString('LEADER_FRITZ'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LANUN",()),'Art_Kaijin/Interface/Popups/FritzPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NAIAS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LANUN",()),'Art_Kaijin/Interface/Popups/NaiasPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_CASIN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LANUN",()), 'Art_Kaijin/Interface/Popups/casin_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_MORDMORGAN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LANUN",()), 'Art_Kaijin/Interface/Popups/mordmorgan_pop.dds')
	# Ljosalfer
				elif eLeader == gc.getInfoTypeForString('LEADER_AIBELL'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LJOSALFAR",()),'Art_Kaijin/Interface/Popups/AibellPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_SAULE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LJOSALFAR",()),'Art_Kaijin/Interface/Popups/SaulePopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ELDARWEN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LJOSALFAR",()), 'Art_Kaijin/Interface/Popups/eldarwen_banner.dds')
	# Luchuirp
				elif eLeader == gc.getInfoTypeForString('LEADER_GISLI'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LUCHUIRP",()),'Art_Kaijin/Interface/Popups/GisliPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_KISH_RIKA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LUCHUIRP",()), 'Art_Kaijin/Interface/Popups/kish_rika_banner.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_LETIGO'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LUCHUIRP",()), 'Art_Kaijin/Interface/Popups/letigo_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_BEAR_GUIN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LUCHUIRP",()), 'Art_Kaijin/Interface/Popups/Bear_guin_pop.dds')
	# Malakim
				elif eLeader == gc.getInfoTypeForString('LEADER_KANE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KANE",()),'Art/Interface/Popups/Kane.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_SHAMASH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KANE",()),'Art_Kaijin/Interface/Popups/ShamashPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_USHEEJA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_MALAKIM",()),'Art_Kaijin/Interface/Popups/UsheejaPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_SARALET'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_MALAKIM",()), 'Art_Kaijin/Interface/Popups/saralet_banner.dds')
	# Mercurians
	# Svartalfer
				elif eLeader == gc.getInfoTypeForString('LEADER_VOLANNA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SVARTALFAR",()),'Art/Interface/Popups/Volanna.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_RIVANNA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SVARTALFAR",()),'Art/Interface/Popups/Rivanna.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_MATHEUS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SVARTALFAR",()),'Art_Kaijin/Interface/Popups/MatheusPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_HATHEIM'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SVARTALFAR",()), 'Art_Kaijin/Interface/Popups/hatheim_banner.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_UTIRUSO'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SVARTALFAR",()), 'Art_Kaijin/Interface/Popups/utiruso_banner.dds')
	# Sheaim
				elif eLeader == gc.getInfoTypeForString('LEADER_AVERAX'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SHEAIM",()),'Art/Interface/Popups/Averax.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_GOSEA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SHEAIM",()),'Art/Interface/Popups/Gosea.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_MALCHAVIC'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SHEAIM",()),'Art/Interface/Popups/Malchavic.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_EROMKCALB'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SHEAIM", ()), 'Art_Kaijin/Interface/Popups/Eromkcalb_pop.dds')
	# Sidar
				elif eLeader == gc.getInfoTypeForString('LEADER_SHEKINAH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SIDAR",()),'Art/Interface/Popups/Shekinah.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_SHUMUEL'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SIDAR",()),'Art_Kaijin/Interface/Popups/ShumuelPopup.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_MIRROUGH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SIDAR",()), 'Art_Kaijin/Interface/Popups/mirrough_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_LEASIEIGH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SIDAR",()), 'Art_Kaijin/Interface/Popups/leasieigh_banner.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_RASIEL'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SIDAR",()), 'Art_Kaijin/Interface/Popups/Rasiel_pop.dds')
	# Niraikanai
				elif eLeader == gc.getInfoTypeForString('LEADER_NIRAIKANAI_MA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_MA",()),'Art_Kaijin/Interface/Popups/MA_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NIRAIKANAI_TINA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_NIRAIKANAI_TINA",()),'Art_Kaijin/Interface/Popups/TINA_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NIRAIKANAI_LISA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_MA",()),'Art_Kaijin/Interface/Popups/Lisa_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NIRAIKANAI_SENDAK'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_NIRAIKANAI_TINA",()),'Art_Kaijin/Interface/Popups/Sendak_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NIRAIKANAI_TERRY'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_DOGI",()),'Art_Kaijin/Interface/Popups/Terry_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NIRAIKANAI_LEAKAGE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_NIRAIKANAI_TINA",()),'Art_Kaijin/Interface/Popups/Leakage_pop.dds')
	# Tokoyami
				elif eLeader == gc.getInfoTypeForString('LEADER_DARK'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_DARK",()),'Art_Kaijin/Interface/Popups/DARK_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_PROFESSOR'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_PROFESSOR",()),'Art_Kaijin/Interface/Popups/Professor_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_OMAEMONA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_PROFESSOR",()),'Art_Kaijin/Interface/Popups/MonaPop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_GIKO_HANYAAN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_PROFESSOR",()),'Art_Kaijin/Interface/Popups/GikoPop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_MORALER'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_PROFESSOR",()),'Art_Kaijin/Interface/Popups/Moraler_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_HAGURUMA_OH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_PROFESSOR",()),'Art_Kaijin/Interface/Popups/Hagurumaoh_pop.dds')
	# Echigo
				elif eLeader == gc.getInfoTypeForString('LEADER_KENSHIN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KENSIN_ECHIGO",()),'Art_Echigo/Interface/Popups/Kensin_echigo_Popups.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NAOE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_NAOE_ECHIGO",()),'Art_Echigo/Interface/Popups/NAOE_echigo_Popups.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_KAGETSUNA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_NAOE_ECHIGO",()),'Art_Kaijin/Interface/Popups/Kagetsuna_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_KAKIZAKI'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_NAOE_ECHIGO",()),'Art_Kaijin/Interface/Popups/Kakizaki_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_USAMI'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_NAOE_ECHIGO",()),'Art_Kaijin/Interface/Popups/Usami_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_AMAKASU'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_NAOE_ECHIGO",()),'Art_Kaijin/Interface/Popups/Amakasu_Pop.dds')
	# Droaum
				elif eLeader == gc.getInfoTypeForString('LEADER_KATRA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KATRA_DROAUM",()),'Art_Kaijin/Droaum/Interface/Popups/KATRA_DROAUM_Popups.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_TERAZA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_TERAZA_DROAUM",()),'Art_Kaijin/Interface/Popups/Teraza_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ROBERT'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_TERAZA_DROAUM",()),'Art_Kaijin/Interface/Popups/Robert_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_RICHARD'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_TERAZA_DROAUM",()),'Art_Kaijin/Interface/Popups/Richard_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_DARSK'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_DARSK_DROAUM",()),'Art_Kaijin/Interface/Popups/Darsk_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_SHERLALAQUE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SHERLALAQUE_DROAUM",()),'Art_Kaijin/Interface/Popups/Sherlalaque_pop.dds')
	# YS
				elif eLeader == gc.getInfoTypeForString('LEADER_REAH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_REAH",()),'Art_Kaijin/REAH/reah_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_FEENA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_FEENA",()),'Art_Kaijin/REAH/feena_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_FLEURETTE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_YUNICA",()),'Art_Kaijin/Interface/Popups/YS_Fleurette_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_JAHL'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_DOGI",()),'Art_Kaijin/Interface/Popups/YS_Jahl_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_LISE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_YUNICA",()), 'Art_Kaijin/Interface/Popups/YS_Lise_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_GERD'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_YUNICA",()), 'Art_Kaijin/Interface/Popups/YS_Gerd_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_OLIVIER'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_DOGI",()),'Art_Kaijin/Interface/Popups/YS_Olivier_pop.dds')
	# Despiel
				elif eLeader == gc.getInfoTypeForString('LEADER_YENOIAH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KAIJIN",()),'Art_Kaijin/Interface/Popups/Yenoiah_Popups.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_LADIBARRE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KAIJIN2",()),'Art_Kaijin/Interface/Popups/Ladibarre_Popups.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ARGYROS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KAIJIN3",()),'Art_Kaijin/Interface/Popups/Argyros_Popups.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_GOLY'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_GOLY",()),'Art_Kaijin/Interface/Popups/GolyPop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ARSINE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KAIJIN3",()),'Art_Kaijin/Interface/Popups/Arsine_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_PZEVDARGYROS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KAIJIN3",()),'Art_Kaijin/Interface/Popups/Pzevdargyros_pop.dds')
	# Lineage
				elif eLeader == gc.getInfoTypeForString('LEADER_MARIS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_MARIS",()),'Art_Kaijin/Interface/Popups/MarisPop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_LEORD'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LEORD",()),'Art_Kaijin/Interface/Popups/LeordPop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_GEORISTALPEHN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LEORD",()),'Art_Kaijin/Interface/Popups/Georistalpehn_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_CARSE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_CARSE",()),'Art_Kaijin/Interface/Popups/CarsePop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_DIANA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_DIANA",()),'Art_Kaijin/Interface/Popups/DianaPop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_YAMAMOTO'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_YAMAMOTO",()),'Art_Kaijin/Interface/Popups/YamamotoPop.dds')
	# Mazatl
				elif eLeader == gc.getInfoTypeForString('LEADER_HIANTHROGH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HIANTHROGH",()),'Art_Kaijin/Interface/Popups/Hianthrogh.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_KHSET'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HIANTHROGH",()),'Art_Kaijin/Interface/Popups/khset.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_AMINZERUGH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HIANTHROGH",()),'Art_Kaijin/Interface/Popups/Aminzerugh_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_MARST'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HIANTHROGH",()),'Art_Kaijin/Interface/Popups/Marst_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_SACCHATHROGHN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HIANTHROGH",()),'Art_Kaijin/Interface/Popups/Sacchathroghn_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_RAFFISERUNO'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HIANTHROGH",()),'Art_Kaijin/Interface/Popups/Raffiseruno_pop.dds')
	# Cualli
				elif eLeader == gc.getInfoTypeForString('LEADER_KOLSEHVAHN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KOLSEHVAHN",()),'Art_Kaijin/Interface/Popups/kolsehvahn.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_MIHUATL'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KOLSEHVAHN",()),'Art_Kaijin/Interface/Popups/mihuatl_banner.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_GHUROVAH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KOLSEHVAHN",()),'Art_Kaijin/Interface/Popups/Ghurovah_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_INVERUPH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KOLSEHVAHN",()),'Art_Kaijin/Interface/Popups/Inveruphu_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_CHYSTAOLLI'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KOLSEHVAHN",()),'Art_Kaijin/Interface/Popups/Chystaolli_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_GLUCOATL'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KOLSEHVAHN",()),'Art_Kaijin/Interface/Popups/Glucoatl_pop.dds')
	# Altair
				elif eLeader == gc.getInfoTypeForString('LEADER_METATORON'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_METATORON",()),'Art_Kaijin/Interface/Popups/MetatoronPop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_LKBRETH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LKBRETH",()),'Art_Kaijin/Interface/Popups/LkbrethPop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_BJEW'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_BJEW",()),'Art_Kaijin/Interface/Popups/BjewPop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_YAHWEH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_METATORON",()),'Art_Kaijin/Interface/Popups/YHWH_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ASTARTE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LKBRETH",()),'Art_Kaijin/Interface/Popups/Astarte_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_GEHENNA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_LKBRETH",()),'Art_Kaijin/Interface/Popups/Gehenna_pop.dds')
	# Mechanos
				elif eLeader == gc.getInfoTypeForString('LEADER_VEROCCHIO'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_VEROCCHIO",()),'Art_Kaijin/Interface/Popups/Verocchio.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_MAER'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_VEROCCHIO",()),'Art_Kaijin/Interface/Popups/maer.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_METALWOLF'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_VEROCCHIO",()),'Art_Kaijin/Interface/Popups/MetalWolf_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_RAIDEN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_VEROCCHIO",()),'Art_Kaijin/Interface/Popups/Raiden_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ATMAN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_VEROCCHIO",()),'Art_Kaijin/Interface/Popups/Atman_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_AMAZIGH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_VEROCCHIO",()),'Art_Kaijin/Interface/Popups/Ama_pop.dds')
	# Scions
				elif eLeader == gc.getInfoTypeForString('LEADER_RISEN_EMPEROR'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_RISEN_EMPEROR",()),'Art_Kaijin/Interface/Popups/risenemperor.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_KORRINA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KORRINA",()),'Art_Kaijin/Interface/Popups/korrina.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_OPHELIA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_KORRINA",()),'Art_Kaijin/Interface/Popups/ophelia_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_XIVAN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_RISEN_EMPEROR",()),'Art_Kaijin/Interface/Popups/icecirolh_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NERO'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_RISEN_EMPEROR",()),'Art_Kaijin/Interface/Popups/Nero_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_TIBERIUS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_RISEN_EMPEROR",()),'Art_Kaijin/Interface/Popups/Tiberius_pop.dds')
	# Nival
				elif eLeader == gc.getInfoTypeForString('LEADER_EKHLO'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_EKHLO",()),'Art_Kaijin/Interface/Popups/EkhloPop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_QITURN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_QITURN",()),'Art_Kaijin/Interface/Popups/QiturnPop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_SCHOENGAR'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_QITURN",()),'Art_Kaijin/Interface/Popups/Schoengar_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NEIGE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_QITURN",()),'Art_Kaijin/Interface/Popups/Neige_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_HIVER'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_QITURN",()),'Art_Kaijin/Interface/Popups/Hiver_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_GIVRE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_QITURN",()),'Art_Kaijin/Interface/Popups/Givre_pop.dds')
	# Rarna
				elif eLeader == gc.getInfoTypeForString('LEADER_RAPHEL'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_RAPHEL",()),'Art_Kaijin/Interface/Popups/Raphael_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_GEORGES'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_GEORGES",()),'Art_Kaijin/Interface/Popups/Georges_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_MARGARETE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_RAPHEL",()),'Art_Kaijin/Interface/Popups/Margarete_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_OSWALD'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_GEORGES",()),'Art_Kaijin/Interface/Popups/Oswald_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_LASLO'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_GEORGES",()),'Art_Kaijin/Interface/Popups/Laslo_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_IGNATIUS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_GEORGES",()),'Art_Kaijin/Interface/Popups/Ignatius_pop.dds')
	# Tiger
				elif eLeader == gc.getInfoTypeForString('LEADER_FOX'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_FOX",()),'Art_Kaijin/Interface/Popups/FOX_POP.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_HOUND'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HOUND",()),'Art_Kaijin/Interface/Popups/hound_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_VULEPES'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_VULEPES",()),'Art_Kaijin/Interface/Popups/Vulepes_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_COYOTE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HOUND",()),'Art_Kaijin/Interface/Popups/coyotepop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_STEINDORF'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_VULEPES",()),'Art_Kaijin/Interface/popups/Steindorf_Pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_SMILEY'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_SMILEY",()),'Art_Kaijin/Interface/Popups/Smiley_Pop.dds')
	# Xoth
				elif eLeader == gc.getInfoTypeForString('LEADER_HYDRA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HYDRA",()),'Art_Kaijin/Interface/Popups/Hydra_pop.dds')
	# Baldralfer
				elif eLeader == gc.getInfoTypeForString('LEADER_INGWE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_INGWE",()),'Art_Kaijin/Interface/Popups/Ingwe_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_WERDNA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_INGWE",()),'Art_Kaijin/Interface/Popups/Werdna_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ARDWEN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_INGWE",()),'Art_Kaijin/Interface/Popups/Ardwen_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_LUTHIEN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_INGWE",()),'Art_Kaijin/Interface/Popups/Luthien_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_FINWE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_INGWE",()),'Art_Kaijin/Interface/Popups/Finwe_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ELWE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_INGWE",()),'Art_Kaijin/Interface/Popups/Elwe_pop.dds')
	# Nougbii
				elif eLeader == gc.getInfoTypeForString('LEADER_ADELAIS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_ADELAIS",()),'Art_Kaijin/Interface/Popups/Adelais_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_YRTSUDNI'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_ADELAIS",()),'Art_Kaijin/Interface/Popups/Yrtsudni_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_EPYTR'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_ADELAIS",()),'Art_Kaijin/Interface/Popups/Epytr_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ANIPUSA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_ADELAIS",()),'Art_Kaijin/Interface/Popups/Anipusa_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ENYDLACI'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_ADELAIS",()),'Art_Kaijin/Interface/Popups/Enydlaci_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_TIVAVQA'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_ADELAIS",()),'Art_Kaijin/Interface/Popups/Tivavqa_pop.dds')
	# Aristrakh
				elif eLeader == gc.getInfoTypeForString('LEADER_NIKEPHOROS'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_NIKEPHOROS",()),'Art_Kaijin/Interface/Popups/Nikephoros_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NAJESH'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_NIKEPHOROS",()),'Art_Kaijin/Interface/Popups/Najesh_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NUSLUEL'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_NIKEPHOROS",()),'Art_Kaijin/Interface/Popups/Notzyuleguhna_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NOHMAMARE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_NIKEPHOROS",()),'Art_Kaijin/Interface/Popups/Nohmamare_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NEWT'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_NIKEPHOROS",()),'Art_Kaijin/Interface/Popups/Newt_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NOTHERLY'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_NIKEPHOROS",()),'Art_Kaijin/Interface/Popups/Notherly_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NESGOSYM'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_NIKEPHOROS",()),'Art_Kaijin/Interface/Popups/Nesgosym_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_NECROZOURE'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_NIKEPHOROS",()),'Art_Kaijin/Interface/Popups/Necrozoure_pop.dds')
	# Megisus
				elif eLeader == gc.getInfoTypeForString('LEADER_HERMES_THE_SECOND'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HERMES_THE_SECOND",()),'Art_Kaijin/Interface/Popups/HermesTheSecond_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ROGEREN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HERMES_THE_SECOND",()),'Art_Kaijin/Interface/Popups/Rogeren_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_ALBERAT'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HERMES_THE_SECOND",()),'Art_Kaijin/Interface/Popups/Alberat_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_HERMES_THE_THIRD'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HERMES_THE_SECOND",()),'Art_Kaijin/Interface/Popups/HermesTheThird_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_PARASTENDI'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HERMES_THE_SECOND",()),'Art_Kaijin/Interface/Popups/Parastendi_pop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_GEBERAR'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_HERMES_THE_SECOND",()),'Art_Kaijin/Interface/Popups/Geberar_pop.dds')
	# Letum Frigus
				elif eLeader == gc.getInfoTypeForString('LEADER_MULCARN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_YAMAMOTO",()),'Art_Kaijin/Interface/Popups/MulcarnPop.dds')
				elif eLeader == gc.getInfoTypeForString('LEADER_KYLORIN'):
					cf.addPopup(CyTranslator().getText("TXT_KEY_POPUP_DEFEATED_YAMAMOTO",()),'Art_Kaijin/Interface/Popups/KylorinPop.dds')
# Kaijin <<<
# ent - Assimilation >>>
		if (not bNewValue):
			eCiv = pPlayer.getCivilizationType()
			if cf.getCivilization(eCiv) == PlayerTypes.NO_PLAYER:
				for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
					pLoopPlayer = gc.getPlayer(iLoopPlayer)
					if pLoopPlayer.isAlive():
						for pyCity in PyPlayer(iLoopPlayer).getCityList():
							pCity = pyCity.GetCy()
							if pCity.getCivilizationType() == eCiv:
								pCity.setCivilizationType(pLoopPlayer.getCivilizationType())
								pLoopPlayer.acquireCity(pCity, False, True)
# ent <<<

	def onPlayerChangeStateReligion(self, argsList):
		'Player changes his state religion'
		iPlayer, iNewReligion, iOldReligion = argsList
##--------	The White Hand: Added by Denev	--------##
		"""
		eReligionWhiteHand = gc.getInfoTypeForString('RELIGION_THE_WHITE_HAND')
		if iNewReligion == eReligionWhiteHand:
			gc.getPlayer(iPlayer).changeStayColdCounter(1)
		elif iOldReligion == eReligionWhiteHand:
			gc.getPlayer(iPlayer).changeStayColdCounter(-1)
		"""
##--------	The White Hand: End Add			--------##

	def onPlayerGoldTrade(self, argsList):
		'Player Trades gold to another player'
		iFromPlayer, iToPlayer, iGoldAmount = argsList

#Kaijin >>>
		pToPlayer = gc.getPlayer(iToPlayer)
		pFromPlayer = gc.getPlayer(iFromPlayer)
#チーム間取引を除外する
		if pToPlayer.getTeam() != pFromPlayer.getTeam():
## CivGoldEmpires - Riches どこかでゴールド取引が発生するとその10%を得る
			for iLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
				loopPlayer = gc.getPlayer(iLoopPlayer)
				if (loopPlayer.isAlive() and not loopPlayer.isMinorCiv() and not loopPlayer.isBarbarian()):
					if (loopPlayer.hasTrait(gc.getInfoTypeForString("TRAIT_RICHES"))):
						iGold = iGoldAmount // 10
						loopPlayer.changeGold(iGold)
						pLPID = loopPlayer.getID()
						CyInterface().addMessage(pLPID,False,15,CyTranslator().getText("TXT_KEY_RICHES_AFFILIATE",(iGold,)),'AS2D_BUILD_BANK',1,'-1',ColorTypes(44), -1, -1, True,True)

## CivGoldEmpires - Riches ゴールド取引で得られる金額増加
			if (pToPlayer.isHuman() and pFromPlayer.isHuman()) or (pToPlayer.isHuman() and not pFromPlayer.isHuman()):
					pToID = pToPlayer.getID()
					if (pToPlayer.hasTrait(gc.getInfoTypeForString("TRAIT_RICHES"))):
						iGold = iGoldAmount // 2
						loopPlayer.changeGold(iGold)
						CyInterface().addMessage(pToID,False,15,CyTranslator().getText("TXT_KEY_RICHES_ABILITY",(iGold,)),'AS2D_BUILD_BANK',1,'-1',ColorTypes(44), -1, -1, True,True)
#Kaijn <<<

	def onCityBuilt(self, argsList):
		'City Built'
		city = argsList[0]
		pPlot = city.plot()
		pPlayer = gc.getPlayer(city.getOwner())
		eCiv = pPlayer.getCivilizationType()

		if CyGame().isFinalInitialized():
			if eCiv == en.eCivilizationInfernal:
				city.setHasReligion(en.eReligionAshenVeil, True, True, True)
# Kaijin >>>
#				city.setPopulation(3)
				if pPlayer.getNumCities() == 1:
					city.setPopulation(15)
				else:
					city.setPopulation(5)

		## Xoth
			elif eCiv == en.eCivilizationXoth:
				city.setHasReligion(gc.getInfoTypeForString('RELIGION_OCTOPUS_OVERLORDS'), True, True, True)
				if pPlayer.getNumCities() == 1:
					city.setPopulation(5)
				else:
					city.setPopulation(3)

	## 初期ユニットの自動生産
		if pPlayer.getNumCities() == 1:
# ent >>>
			cf.initFreeHeros(city.getOwner(), pPlot)
			"""
			pTeam = gc.getTeam(pPlayer.getTeam())
			if eCiv == en.eCivilizationDoviello:
				newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_LUCIAN'), city.getX(), city.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

			if eCiv == en.eCivilizationNiraikanai:
				newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_BRAGGART'), city.getX(), city.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

			if eCiv == en.eCivilizationYs:
				newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_YUNICA'), city.getX(), city.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

			if eCiv == en.eCivilizationAltair:
				newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_METATORON1'), city.getX(), city.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

			if eCiv == en.eCivilizationScions:
				newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_KORRINA'), city.getX(), city.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
				if pTeam.isHasTech(gc.getInfoTypeForString('TECH_BRONZE_WORKING')) or pTeam.isHasTech(gc.getInfoTypeForString('TECH_TRACKING')):
					newUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HELD'), False)

	## Scions - Heroes
				if pTeam.isHasTech(gc.getInfoTypeForString('TECH_TRACKING')):
					newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_THEMOCH'), city.getX(), city.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

				if pTeam.isHasTech(gc.getInfoTypeForString('TECH_CURRENCY')):
					newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_PELEMOC'), city.getX(), city.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

				if pTeam.isHasTech(gc.getInfoTypeForString('TECH_CODE_OF_LAWS')):
					newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_MELANTE'), city.getX(), city.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)

				if pTeam.isHasTech(gc.getInfoTypeForString('TECH_KNOWLEDGE_OF_THE_ETHER')):
					newUnit = pPlayer.initUnit(gc.getInfoTypeForString('UNIT_ALCINUS'), city.getX(), city.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
			"""
# ent <<<

	## Nival - Palace
		if eCiv == en.eCivilizationNival and pPlayer.getNumCities() == 1:
			lpRangedPlots = cyGetRangedPlots(pPlot, city.getPlotRadius() - 1, False, False, TeamTypes.NO_TEAM)
			eEffect = gc.getInfoTypeForString('EFFECT_SNOWFALL')
			for pTargetPlot in lpRangedPlots:
				pWorkingCity = pTargetPlot.getWorkingCity()
				if pWorkingCity.getOwner() == city.getOwner() and pWorkingCity.getID() == city.getID():
					cf.doBuildingColdEffects(pTargetPlot)
					pTargetPlot.ceilColdCounter(9600 + CyGame().getSorenRandNum(2400, "Built Temple of the Hand"), 1000)
					if pTargetPlot.getTerrainType() != en.eTerrainSnow:
						if pTargetPlot.isVisibleToWatchingHuman():
							CyEngine().triggerEffect(eEffect, pTargetPlot.getPoint())

	## CivGoldEmpires - Agricultural Trait
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGRICULTURAL')):
			city.changePopulation(1)
	## CivGoldEmpires - IronWill Trait
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_IRON_WILL')):
			if pPlayer.getStateReligion() != ReligionTypes.NO_RELIGION:
				city.setHasReligion(pPlayer.getStateReligion(), True, True, True)

# Kaijin <<<

		if CyGame().getWBMapScript():
			sf.onCityBuilt(city)

##--------	Merging Better BtS AI: Modified by Denev	--------##
#		if (city.getOwner() == gc.getGame().getActivePlayer()):
		if (city.getOwner() == CyGame().getActivePlayer() and CyGame().getAIAutoPlay() == 0):
##--------	Merging Better BtS AI: End Modify			--------##
			self.__eventEditCityNameBegin(city, False)
		CvUtil.pyPrint('City Built Event: %s' %(city.getName()))

	def onCityRazed(self, argsList):
		'City Razed'
		city, iPlayer = argsList
		iOwner = city.findHighestCulture()

		# Partisans!
#		if city.getPopulation > 1 and iOwner != -1 and iPlayer != -1:
#			owner = gc.getPlayer(iOwner)
#			if not owner.isBarbarian() and owner.getNumCities() > 0:
#				if gc.getTeam(owner.getTeam()).isAtWar(gc.getPlayer(iPlayer).getTeam()):
#					if gc.getNumEventTriggerInfos() > 0: # prevents mods that don't have events from getting an error
#						iEvent = CvUtil.findInfoTypeNum(gc.getEventTriggerInfo, gc.getNumEventTriggerInfos(), 'EVENTTRIGGER_PARTISANS')
#						if iEvent != -1 and gc.getGame().isEventActive(iEvent) and owner.getEventTriggerWeight(iEvent) >= 0:
#							triggerData = owner.initTriggeredData(iEvent, True, -1, city.getX(), city.getY(), iPlayer, city.getID(), -1, -1, -1, -1)

		pPlayer = gc.getPlayer(iPlayer)
		ePreviousOwner = city.getPreviousOwner()
		iAlignment = gc.getPlayer(ePreviousOwner).getAlignment()
		iPopulation = city.getPopulation()
		if iAlignment == AlignmentTypes.ALIGNMENT_EVIL:
			ePreviousCivilization = gc.getPlayer(ePreviousOwner).getCivilizationType()
			ePreviousDefaultRace = gc.getCivilizationInfo(ePreviousCivilization).getDefaultRace()
			if ePreviousDefaultRace == PromotionTypes.NO_PROMOTION or not gc.getPromotionInfo(ePreviousDefaultRace).isNotAlive():
				cf.doAfterLife(False, iPopulation, city.plot(), None, city, 0)

		elif iAlignment == AlignmentTypes.ALIGNMENT_NEUTRAL:
			cf.doAfterLife(False, (iPopulation + 1) // 2, city.plot(), None, city, 0)
			cf.doAfterLife(True, (iPopulation + 2) // 4, city.plot(), None, city, 0)

		elif iAlignment == AlignmentTypes.ALIGNMENT_GOOD:
			cf.doAfterLife(True, (iPopulation + 1) // 2, city.plot(), None, city, 0)

#Kaijin >>>
		iPreviousOwner = city.getPreviousOwner()
		pPreviousOwner = gc.getPlayer(iPreviousOwner)
		iOriginalOwner = city.getOriginalOwner()
		pOriginalOwner = gc.getPlayer(iOriginalOwner)
	# scions start - Gives Reborn when razing cities.  The function reducing the population of Scion conquests kicks in first.  Currently Reborn given = that population -1.  Requires Sorc. and Priestood.  It's been suggested that be changed to requiring the civic "Glory."
		if gc.getPlayer(city.getOwner()).getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SCIONS'):
			if pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_LABOR')) == gc.getInfoTypeForString('CIVIC_GLORY'):
				for i in xrange(city.getPopulation() // 3):
					pPlayer.initUnit(gc.getInfoTypeForString('UNIT_REBORN'), city.getX(), city.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
	# scions end

#Kaijin <<<

##--------	Advanced Rules: Added by ent	--------##
	## Gain Slave.
		if iPlayer <= gc.getBARBARIAN_PLAYER():
			iNumSlave = iPopulation  + city.totalFreeSpecialists()
			if not pPlayer.isCivic(gc.getInfoTypeForString('CIVIC_CONQUEST')):
				iNumSlave /= 2
			if iNumSlave > 0:
				eUnitSlave = gc.getInfoTypeForString('UNIT_SLAVE')
				pTargetPlot = cf.findAdjacentClearPlot(iPreviousOwner, city.getX(), city.getY(), False, True)
				if pTargetPlot is not None:
					for i in xrange(iNumSlave):
						pUnit = pPreviousOwner.initUnit(eUnitSlave, pTargetPlot.getX(), pTargetPlot.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
						pNewUnit = pPlayer.initSkeletalUnit(eUnitSlave, city.getX(), city.getY(), UnitAITypes.NO_UNITAI)
						pNewUnit.convert(pUnit)
				else:
					eDefaultRace = gc.getCivilizationInfo(pPreviousOwner.getCivilizationType()).getDefaultRace()
					for i in xrange(iNumSlave):
						pUnit = pPlayer.initUnit(eUnitSlave, city.getX(), city.getY(), UnitAITypes.NO_UNITAI, DirectionTypes.DIRECTION_SOUTH)
						if eDefaultRace != PromotionTypes.NO_PROMOTION:
							pUnit.setHasPromotion(eDefaultRace, True)
				szButton = gc.getUnitInfo(eUnitSlave).getButton()
				szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_SLAVE_RAZE_CITY", (city.getName(), iNumSlave))
				CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, city.getX(), city.getY(), True, True)

	## Doviello - Pillage around the city.
		if pPlayer.getCivilizationType() == en.eCivilizationDoviello:
			iPillageGold = 0
			lpRangedPlots = cyGetRangedPlots(city.plot(), city.getPlotRadius(), False, False, TeamTypes.NO_TEAM)
			for pTargetPlot in lpRangedPlots:
				if not pTargetPlot.isOwned():
					while pTargetPlot.getImprovementType() != ImprovementTypes.NO_IMPROVEMENT:
						kImprovement = gc.getImprovementInfo(pTargetPlot.getImprovementType())
						if kImprovement.isPermanent():
							break
						iPillageGold += CyGame().getSorenRandNum(kImprovement.getPillageGold(), "Pillage Gold 1")
						iPillageGold += CyGame().getSorenRandNum(kImprovement.getPillageGold(), "Pillage Gold 2")
						pTargetPlot.setImprovementType(kImprovement.getImprovementPillage())
			iModifier = 0
			iModifier += pPlayer.getPillagingGold()
			if pPlayer.isCivic(gc.getInfoTypeForString('CIVIC_CONQUEST')):
				iModifier += 100
			iPillageGold += (iPillageGold * iModifier) // 100
			if iPillageGold > 0:
				pPlayer.changeGold(iPillageGold)
				szButton = gc.getMissionInfo(MissionTypes.MISSION_PILLAGE).getButton()
				szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_DOVIELLO_RAZE_CITY", (city.getName(), iPillageGold))
				CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_PILLAGED', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorGreen, city.getX(), city.getY(), True, True)
##--------	Advanced Rules: End Add			--------##

		if CyGame().getWBMapScript():
			sf.onCityRazed(city, iPlayer)

		CvUtil.pyPrint("City Razed Event: %s" %(city.getName(),))

	def onCityAcquired(self, argsList):
		'City Acquired'
		iPreviousOwner, iNewOwner, pCity, bConquest, bTrade = argsList
		pPlayer = gc.getPlayer(iNewOwner)

# ent >>>
## Colony - Spilit Empire
		if pPlayer.getNumCities() == 1:
			if pPlayer.getCivilizationType() == en.eCivilizationElohim:
				cf.showUniqueImprovements(iNewOwner)
## Amurite - Show All Manas
			elif pPlayer.getCivilizationType() == en.eCivilizationAmurites:
				cf.showRawManas(iNewOwner)

## Globalcounter initialization
			if not pPlayer.isBarbarian():
				cf.doGlobalcounterInitialization(iNewOwner)
			cf.initFreeHeros(iNewOwner, pCity)
# ent <<<

#Kaijin >>>
## Guildplus - Contract War
		if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_TIGER') and bConquest:
			bContract = bool(pPlayer.getGuildPlusCounter(50))
			if bContract:
				iNum = pPlayer.getGuildPlusCounter(59)
				for iIndex in xrange(iNum):
					iEnemy = pPlayer.getGuildPlusCounter(60 + iIndex)
					if iPreviousOwner == iEnemy:
						iPopulation = pCity.getPopulation()
						pPlayer.changeGuildPlusCounter(53, iPopulation)
#						iBonus = iPopulation * 10
						iBonus = iPopulation * 100 * 2 * gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent() // 100
						pPlayer.changeGuildPlusCounter(54, iBonus)
						break
#Kaijin <<<

		if CyGame().getWBMapScript():
			sf.onCityAcquired(iPreviousOwner, iNewOwner, pCity, bConquest, bTrade)

		CvUtil.pyPrint('City Acquired Event: %s' %(pCity.getName()))

	def onCityAcquiredAndKept(self, argsList):
		'City Acquired and Kept'
		iOwner, pCity = argsList

		pPlayer = gc.getPlayer(iOwner)

		if pPlayer.getCivilizationType() == en.eCivilizationInfernal:
			pCity.setHasReligion(gc.getInfoTypeForString('RELIGION_THE_ORDER'), False, True, True)
			pCity.setHasReligion(en.eReligionAshenVeil, True, True, True)

		elif pPlayer.getCivilizationType() == en.eCivilizationMercurians:
			pCity.setName(pPlayer.getNewCityName(), False)

#Kaijin >>>
# Xoth
		elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_XOTH'):
			pCity.setHasReligion(gc.getInfoTypeForString('RELIGION_OCTOPUS_OVERLORDS'), True, True, True)

# Trait Faith
## 国教の聖都を獲得したら黄金期に突入
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_FAITH')):
			if pPlayer.getStateReligion() != ReligionTypes.NO_RELIGION:
				if pCity.isHolyCityByType(pPlayer.getStateReligion()):
					if not pPlayer.isGoldenAge():
						pPlayer.changeGoldenAgeTurns(CyGame().goldenAgeLength())
#Kaijin <<<

		#Functions added here tend to cause OOS issues

		CvUtil.pyPrint('City Acquired and Kept Event: %s' %(pCity.getName()))

	def onCityLost(self, argsList):
		'City Lost'
		city = argsList[0]
		player = PyPlayer(city.getOwner())
		if (not self.__LOG_CITYLOST):
			return
		CvUtil.pyPrint('City %s was lost by Player %d Civilization %s'
			%(city.getName(), player.getID(), player.getCivilizationName()))

	def onCultureExpansion(self, argsList):
		'City Culture Expansion'
		pCity = argsList[0]
		iPlayer = argsList[1]
		CvUtil.pyPrint("City %s's culture has expanded" %(pCity.getName(),))

	def onCityGrowth(self, argsList):
		'City Population Growth'
		pCity = argsList[0]
		iPlayer = argsList[1]
		CvUtil.pyPrint("%s has grown" %(pCity.getName(),))

	def onCityDoTurn(self, argsList):
		'City Production'
		pCity = argsList[0]
		iPlayer = argsList[1]
		pPlot = pCity.plot()
		iPlayer = pCity.getOwner()
		pPlayer = gc.getPlayer(iPlayer)

		if gc.getPlayer(pCity.getOwner()).getCivilizationType() == en.eCivilizationInfernal:
			pCity.setHasReligion(gc.getInfoTypeForString('RELIGION_THE_ORDER'), False, True, True)
			pCity.setHasReligion(en.eReligionAshenVeil, True, True, True)

		elif gc.getPlayer(pCity.getOwner()).getCivilizationType() == en.eCivilizationMercurians:
			pCity.setHasReligion(en.eReligionAshenVeil, False, True, True)

		CvAdvisorUtils.cityAdvise(pCity, iPlayer)

	def onCityBuildingUnit(self, argsList):
		'City begins building a unit'
		pCity = argsList[0]
		iUnitType = argsList[1]
##--------	Unofficial Bug Fix: Added by Denev	--------##
		if iUnitType == gc.getInfoTypeForString('UNIT_ACHERON'):
			szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_START_PRODUCTION_ACHERON", (pCity.getName(), ))
			szButton = gc.getUnitInfo(iUnitType).getButton()
			for iPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
				if gc.getPlayer(iPlayer).isAlive():
					CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorUnit, pCity.getX(), pCity.getY(), True, True)
##--------	Unofficial Bug Fix: End Modify			--------##
# Kaijin OAC >>>
		## Alert - Element Destroyer
		if iUnitType == gc.getInfoTypeForString('UNIT_ELEMENT_DESTROYER'):
			szMessage = CyTranslator().getText("TXT_KEY_MESSAGE_START_PRODUCTION_ELEMENT_DESTROYER", (pCity.getName(), ))
			szButton = gc.getUnitInfo(iUnitType).getButton()
			for iPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
				if gc.getPlayer(iPlayer).isAlive():
					CyInterface().addMessage(iPlayer, True, gc.getEVENT_MESSAGE_TIME(), szMessage, '', InterfaceMessageTypes.MESSAGE_TYPE_INFO, szButton, en.eColorUnit, pCity.getX(), pCity.getY(), True, True)
# Kaijin OAC <<<
		if (not self.__LOG_CITYBUILDING):
			return
		CvUtil.pyPrint("%s has begun building a %s" %(pCity.getName(), gc.getUnitInfo(iUnitType).getDescription()))

	def onCityBuildingBuilding(self, argsList):
		'City begins building a Building'
		pCity = argsList[0]
		iBuildingType = argsList[1]
		if (not self.__LOG_CITYBUILDING):
			return
		CvUtil.pyPrint("%s has begun building a %s" %(pCity.getName(), gc.getBuildingInfo(iBuildingType).getDescription()))

	def onCityRename(self, argsList):
		'City is renamed'
		pCity = argsList[0]
		if (pCity.getOwner() == gc.getGame().getActivePlayer()):
			self.__eventEditCityNameBegin(pCity, True)

	def onCityHurry(self, argsList):
		'City is renamed'
		pCity = argsList[0]
		iHurryType = argsList[1]

	def onVictory(self, argsList):
		'Victory'
		iTeam, iVictory = argsList
		if (iVictory >= 0 and iVictory < gc.getNumVictoryInfos()):
			for iPlayer in xrange(gc.getMAX_PLAYERS()):
				pPlayer = gc.getPlayer(iPlayer)
				if pPlayer.isAlive():
					if pPlayer.isHuman():
						if pPlayer.getTeam() == iTeam:
							if CyGame().getWBMapScript():
								sf.onVictory(iPlayer, iVictory)
							else:
								iCiv = pPlayer.getCivilizationType()
								if iCiv == gc.getInfoTypeForString('CIVILIZATION_AMURITES'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_AMURITES", 1)
								elif iCiv == en.eCivilizationBalseraphs:
									CyGame().changeTrophyValue("TROPHY_VICTORY_BALSERAPHS", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_BANNOR'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_BANNOR", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_CALABIM'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_CALABIM", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_CLAN_OF_EMBERS'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_CLAN_OF_EMBERS", 1)
								elif iCiv == en.eCivilizationDoviello:
									CyGame().changeTrophyValue("TROPHY_VICTORY_DOVIELLO", 1)
								elif iCiv == en.eCivilizationElohim:
									CyGame().changeTrophyValue("TROPHY_VICTORY_ELOHIM", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_GRIGORI'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_GRIGORI", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_HIPPUS'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_HIPPUS", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_ILLIANS'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_ILLIANS", 1)
								elif iCiv == en.eCivilizationInfernal:
									CyGame().changeTrophyValue("TROPHY_VICTORY_INFERNAL", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_KHAZAD'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_KHAZAD", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_KURIOTATES'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_KURIOTATES", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_LANUN'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_LANUN", 1)
								elif iCiv == en.eCivilizationLjosalfar:
									CyGame().changeTrophyValue("TROPHY_VICTORY_LJOSALFAR", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_LUCHUIRP'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_LUCHUIRP", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_MALAKIM'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_MALAKIM", 1)
								elif iCiv == en.eCivilizationMercurians:
									CyGame().changeTrophyValue("TROPHY_VICTORY_MERCURIANS", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_SHEAIM'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_SHEAIM", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_SIDAR'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_SIDAR", 1)
								elif iCiv == en.eCivilizationSvartalfar:
									CyGame().changeTrophyValue("TROPHY_VICTORY_SVARTALFAR", 1)

								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_NIRAIKANAI'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_NIRAIKANAI", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_DARK'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_DARK", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_YS'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_YS", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_ECHIGO'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_ECHIGO", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_DROAUM'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_DROAUM", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_DESPIEL'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_DESPIEL", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_LINEAGE'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_LINEAGE", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_MAZATL'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_MAZATL", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_CUALLI'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_CUALLI", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_ALTAIR'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_ALTAIR", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_MECHANOS'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_MECHANOS", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_SCIONS'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_SCIONS", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_NIVAL'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_NIVAL", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_RARNA'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_RARNA", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_TIGER'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_TIGER", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_XOTH'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_XOTH", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_BALDRALFAR'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_BALDRALFAR", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_NOUGBII'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_NOUGBII", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_ARISTRAKH'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_ARISTRAKH", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_MEGISUS'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_MEGISUS", 1)
								elif iCiv == gc.getInfoTypeForString('CIVILIZATION_LETUM_FRIGUS'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_LETUM_FRIGUS", 1)

								if iVictory == gc.getInfoTypeForString('VICTORY_ALTAR_OF_THE_LUONNOTAR'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_ALTAR_OF_THE_LUONNOTAR", 1)
								elif iVictory == gc.getInfoTypeForString('VICTORY_CONQUEST'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_CONQUEST", 1)
								elif iVictory == gc.getInfoTypeForString('VICTORY_CULTURAL'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_CULTURAL", 1)
								elif iVictory == gc.getInfoTypeForString('VICTORY_DOMINATION'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_DOMINATION", 1)
								elif iVictory == gc.getInfoTypeForString('VICTORY_RELIGIOUS'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_RELIGIOUS", 1)
								elif iVictory == gc.getInfoTypeForString('VICTORY_SCORE'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_SCORE", 1)
								elif iVictory == gc.getInfoTypeForString('VICTORY_TIME'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_TIME", 1)
								elif iVictory == gc.getInfoTypeForString('VICTORY_TOWER_OF_MASTERY'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_TOWER_OF_MASTERY", 1)
								elif iVictory == gc.getInfoTypeForString('VICTORY_STATUE_OF_LUXURY'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_STATUE_OF_LUXURY", 1)
								elif iVictory == gc.getInfoTypeForString('VICTORY_LED_TO_THE_END'):
									CyGame().changeTrophyValue("TROPHY_VICTORY_LED_TO_THE_END", 1)

								if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_BARBARIAN_WORLD):
									CyGame().changeTrophyValue("TROPHY_VICTORY_BARBARIAN_WORLD", 1)
								if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_CHALLENGE_CUT_LOSERS):
									CyGame().changeTrophyValue("TROPHY_VICTORY_FINAL_FIVE", 1)
								if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_CHALLENGE_HIGH_TO_LOW):
									CyGame().changeTrophyValue("TROPHY_VICTORY_HIGH_TO_LOW", 1)
								if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_CHALLENGE_INCREASING_DIFFICULTY):
									CyGame().changeTrophyValue("TROPHY_VICTORY_INCREASING_DIFFICULTY", 1)

# Kaijin >>>
							# The birth of Diamond Drake.
							pNewUnit = cf.addBarbarianUnit(gc.getInfoTypeForString('UNIT_DIAMOND_DRAKE'), gc.getInfoTypeForString('BARBARIAN_ORC'))
							if pNewUnit is not None:
								pNewUnit.setLevel(15)
								pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_REGENERATION'), True)
								pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_STONESKIN'), True)
								pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENCHANTED_BLADE'), True)
								pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_COURAGE'), True)
								pNewUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_LOYALTY'), True)
								pBarbarianTeam = gc.getTeam(gc.getBARBARIAN_TEAM())
								pBarbarianTeam.declareWar(iTeam, False, WarPlanTypes.WARPLAN_TOTAL)
# Kaijin <<<

			victoryInfo = gc.getVictoryInfo(int(iVictory))
			CvUtil.pyPrint("Victory!  Team %d achieves a %s victory"
				%(iTeam, victoryInfo.getDescription()))

	def onVassalState(self, argsList):
		'Vassal State'
		iMaster, iVassal, bVassal = argsList

		if (bVassal):
			CvUtil.pyPrint("Team %d becomes a Vassal State of Team %d"
				%(iVassal, iMaster))
		else:
			CvUtil.pyPrint("Team %d revolts and is no longer a Vassal State of Team %d"
				%(iVassal, iMaster))

	def onGameUpdate(self, argsList):
		'sample generic event, called on each game turn slice'
		genericArgs = argsList[0][0]	# tuple of tuple of my args
		turnSlice = genericArgs[0]

#FfH: 10/15/2008 Added by Kael for OOS logging.
		OOSLogger.doGameUpdate()
#FfH: End add

	def onMouseEvent(self, argsList):
		'mouse handler - returns 1 if the event was consumed'
		eventType, mx, my, px, py, interfaceConsumed, screens = argsList
		if ( px!=-1 and py!=-1 ):
			if ( eventType == self.EventLButtonDown ):
				if (self.bAllowCheats and self.bCtrl and self.bAlt and CyMap().plot(px, py).isCity() and not interfaceConsumed):
					# Launch Edit City Event
					self.beginEvent( CvUtil.EventEditCity, (px, py) )
					return 1

				elif (self.bAllowCheats and self.bCtrl and self.bShift and not interfaceConsumed):
					# Launch Place Object Event
					self.beginEvent( CvUtil.EventPlaceObject, (px, py) )
					return 1

		if ( eventType == self.EventBack ):
			return CvScreensInterface.handleBack(screens)
		elif ( eventType == self.EventForward ):
			return CvScreensInterface.handleForward(screens)

		return 0


#################### TRIGGERED EVENTS ##################

	def __eventEditCityNameBegin(self, city, bRename):
		popup = PyPopup.PyPopup(CvUtil.EventEditCityName, EventContextTypes.EVENTCONTEXT_ALL)
		popup.setUserData((city.getID(), bRename))
		popup.setHeaderString(localText.getText("TXT_KEY_NAME_CITY", ()))
		popup.setBodyString(localText.getText("TXT_KEY_SETTLE_NEW_CITY_NAME", ()))
		popup.createEditBox(city.getName())
		popup.setEditBoxMaxCharCount( 15 )
		popup.launch()

	def __eventEditCityNameApply(self, playerID, userData, popupReturn):
		'Edit City Name Event'
		iCityID = userData[0]
		bRename = userData[1]
		player = gc.getPlayer(playerID)
		city = player.getCity(iCityID)
		cityName = popupReturn.getEditBoxString(0)
		if (len(cityName) > 30):
			cityName = cityName[:30]
		city.setName(cityName, not bRename)

	def __eventEditCityBegin(self, argsList):
		'Edit City Event'
		px, py = argsList
		CvWBPopups.CvWBPopups().initEditCity(argsList)

	def __eventEditCityApply(self, playerID, userData, popupReturn):
		'Edit City Event Apply'
		if (getChtLvl() > 0):
			CvWBPopups.CvWBPopups().applyEditCity( (popupReturn, userData) )

	def __eventPlaceObjectBegin(self, argsList):
		'Place Object Event'
		CvDebugTools.CvDebugTools().initUnitPicker(argsList)

	def __eventPlaceObjectApply(self, playerID, userData, popupReturn):
		'Place Object Event Apply'
		if (getChtLvl() > 0):
			CvDebugTools.CvDebugTools().applyUnitPicker( (popupReturn, userData) )

	def __eventAwardTechsAndGoldBegin(self, argsList):
		'Award Techs & Gold Event'
		CvDebugTools.CvDebugTools().cheatTechs()

	def __eventAwardTechsAndGoldApply(self, playerID, netUserData, popupReturn):
		'Award Techs & Gold Event Apply'
		if (getChtLvl() > 0):
			CvDebugTools.CvDebugTools().applyTechCheat( (popupReturn) )

	def __eventShowWonderBegin(self, argsList):
		'Show Wonder Event'
		CvDebugTools.CvDebugTools().wonderMovie()

	def __eventShowWonderApply(self, playerID, netUserData, popupReturn):
		'Wonder Movie Apply'
		if (getChtLvl() > 0):
			CvDebugTools.CvDebugTools().applyWonderMovie( (popupReturn) )

	def __eventEditUnitNameBegin(self, argsList):
		pUnit = argsList
		popup = PyPopup.PyPopup(CvUtil.EventEditUnitName, EventContextTypes.EVENTCONTEXT_ALL)
		popup.setUserData((pUnit.getID(),))
		popup.setBodyString(localText.getText("TXT_KEY_RENAME_UNIT", ()))
		popup.createEditBox(pUnit.getNameNoDesc())
		popup.launch()

	def __eventEditUnitNameApply(self, playerID, userData, popupReturn):
		'Edit Unit Name Event'
		iUnitID = userData[0]
		unit = gc.getPlayer(playerID).getUnit(iUnitID)
		newName = popupReturn.getEditBoxString(0)
		if (len(newName) > 25):
			newName = newName[:25]
		unit.setName(newName)

	def __eventWBAllPlotsPopupBegin(self, argsList):
		CvScreensInterface.getWorldBuilderScreen().allPlotsCB()
		return
	def __eventWBAllPlotsPopupApply(self, playerID, userData, popupReturn):
		if (popupReturn.getButtonClicked() >= 0):
			CvScreensInterface.getWorldBuilderScreen().handleAllPlotsCB(popupReturn)
		return

	def __eventWBLandmarkPopupBegin(self, argsList):
		CvScreensInterface.getWorldBuilderScreen().setLandmarkCB("")
		#popup = PyPopup.PyPopup(CvUtil.EventWBLandmarkPopup, EventContextTypes.EVENTCONTEXT_ALL)
		#popup.createEditBox(localText.getText("TXT_KEY_WB_LANDMARK_START", ()))
		#popup.launch()
		return

	def __eventWBLandmarkPopupApply(self, playerID, userData, popupReturn):
		if (popupReturn.getEditBoxString(0)):
			szLandmark = popupReturn.getEditBoxString(0)
			if (len(szLandmark)):
				CvScreensInterface.getWorldBuilderScreen().setLandmarkCB(szLandmark)
		return

	def __eventWBScriptPopupBegin(self, argsList):
		popup = PyPopup.PyPopup(CvUtil.EventWBScriptPopup, EventContextTypes.EVENTCONTEXT_ALL)
		popup.setHeaderString(localText.getText("TXT_KEY_WB_SCRIPT", ()))
# >>> CYBERFRONT // text: script
#		popup.createEditBox(CvScreensInterface.getWorldBuilderScreen().getCurrentScript())
		popup.createEditBox(CvUtil.convertToUnicode(CvScreensInterface.getWorldBuilderScreen().getCurrentScript()))
# <<< CYBERFRONT
		popup.launch()
		return

	def __eventWBScriptPopupApply(self, playerID, userData, popupReturn):
		if (popupReturn.getEditBoxString(0)):
			szScriptName = popupReturn.getEditBoxString(0)
# >>> CYBERFRONT // text: script
#			CvScreensInterface.getWorldBuilderScreen().setScriptCB(szScriptName)
			CvScreensInterface.getWorldBuilderScreen().setScriptCB(CvUtil.convertToStr(szScriptName))
# <<< CYBERFRONT
		return

	def __eventWBStartYearPopupBegin(self, argsList):
		popup = PyPopup.PyPopup(CvUtil.EventWBStartYearPopup, EventContextTypes.EVENTCONTEXT_ALL)
		popup.createSpinBox(0, "", gc.getGame().getStartYear(), 1, 5000, -5000)
		popup.launch()
		return

	def __eventWBStartYearPopupApply(self, playerID, userData, popupReturn):
		iStartYear = popupReturn.getSpinnerWidgetValue(int(0))
		CvScreensInterface.getWorldBuilderScreen().setStartYearCB(iStartYear)
		return

## FfH Card Game: begin
	def __EventSelectSolmniumPlayerBegin(self):
		iHUPlayer = gc.getGame().getActivePlayer()

		if iHUPlayer == -1 : return 0
		if not cs.canStartGame(iHUPlayer): return 0

		popup = PyPopup.PyPopup(CvUtil.EventSelectSolmniumPlayer, EventContextTypes.EVENTCONTEXT_ALL)

		sResText = CyUserProfile().getResolutionString(CyUserProfile().getResolution())
		sX, sY = sResText.split("x")
		iXRes = int(sX)
		iYRes = int(sY)

		iW = 620
		iH = 650

		popup.setSize(iW, iH)
		popup.setPosition((iXRes - iW) / 2, 30)

		lStates = []

		for iPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
			pPlayer = gc.getPlayer(iPlayer)

			if pPlayer.isNone(): continue

			if pPlayer.isHuman():
				lPlayerState = cs.getStartGameMPWith(iHUPlayer, iPlayer)
				if lPlayerState[0][0] in ["No", "notMet"] : continue
				lStates.append([iPlayer, lPlayerState])
			else :
				lPlayerState = cs.getStartGameAIWith(iHUPlayer, iPlayer)
				if lPlayerState[0][0] in ["No", "notMet"] : continue
				lStates.append([iPlayer, lPlayerState])

		lPlayerButtons = []

		popup.addDDS(CyArtFileMgr().getInterfaceArtInfo("SOMNIUM_POPUP_INTRO").getPath(), 0, 0, 512, 128)
		popup.addSeparator()
		#popup.setHeaderString(localText.getText("TXT_KEY_SOMNIUM_START", ()), CvUtil.FONT_CENTER_JUSTIFY)
		if len(lStates) == 0 :
			popup.setBodyString(localText.getText("TXT_KEY_SOMNIUM_NOONE_MET", ()))
		else :
			#popup.setBodyString(localText.getText("TXT_KEY_SOMNIUM_PLAY_WITH", ()))
			popup.addSeparator()
			popup.addSeparator()

			sText = u""
			for iPlayer, lPlayerState in lStates :
				pPlayer = gc.getPlayer(iPlayer)
				sPlayerName = pPlayer.getName()
				iPositiveChange = gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getMemoryAttitudePercent(MemoryTypes.MEMORY_SOMNIUM_POSITIVE) / 100
				iNegativeChange = gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getMemoryAttitudePercent(MemoryTypes.MEMORY_SOMNIUM_NEGATIVE) / 100
				bShift = True

				for item in lPlayerState :

					sTag = item[0]
					if (sTag == "atWar"):
						if len(sText) > 0 : sText += localText.getText("[NEWLINE]", ())
						sText += localText.getText("TXT_KEY_SOMNIUM_AT_WAR", (sPlayerName, ))

					elif (sTag == "InGame"):
						if len(sText) > 0 : sText += localText.getText("[NEWLINE]", ())
						sText += localText.getText("TXT_KEY_SOMNIUM_IN_GAME", (sPlayerName, ))

					elif (sTag == "relation"):
						delay = item[1]
						if (delay > 0):
							if len(sText) > 0 : sText += localText.getText("[NEWLINE]", ())
							sText += localText.getText("TXT_KEY_SOMNIUM_GAME_DELAYED", (sPlayerName, delay))
						else :
							if bShift :
								bShift = False
								popup.addSeparator()
							popup.addButton(localText.getText("TXT_KEY_SOMNIUM_GAME_RELATION", (sPlayerName, iPositiveChange, iNegativeChange)))
							lPlayerButtons.append((iPlayer, -1))

					elif (sTag == "gold"):
						for iGold in item[1] :
							if bShift :
								bShift = False
								popup.addSeparator()
							if iGold == 0 :
								popup.addButton(localText.getText("TXT_KEY_SOMNIUM_GAME_FUN", (sPlayerName, )))
								lPlayerButtons.append((iPlayer, iGold))
							else :
								popup.addButton(localText.getText("TXT_KEY_SOMNIUM_GAME_GOLD", (sPlayerName, iGold)))
								lPlayerButtons.append((iPlayer, iGold))

			if len(sText) > 0 :
				popup.addSeparator()
				popup.addSeparator()
				popup.setBodyString(sText)

		popup.setUserData(tuple(lPlayerButtons))
		popup.launch()

	def __EventSelectSolmniumPlayerApply(self, playerID, userData, popupReturn):
		if userData :
			idButtonCliked = popupReturn.getButtonClicked()
			if idButtonCliked in xrange(len(userData)):
				iOpponent, iGold = userData[idButtonCliked]

				pLeftPlayer = gc.getPlayer(playerID)
				pRightPlayer = gc.getPlayer(iOpponent)

				if not pRightPlayer.isHuman():
					if (cs.canStartGame(playerID)) and (pLeftPlayer.isAlive()) and (pRightPlayer.isAlive()):
						cs.startGame(playerID, iOpponent, iGold)
					else :
						CyInterface().addMessage(playerID, True, 25, CyTranslator().getText("TXT_KEY_SOMNIUM_CANT_START_GAME", (gc.getPlayer(iOpponent).getName(), )), '', 1, '', en.eColorRed, -1, -1, False, False)
				else :
					if (cs.canStartGame(playerID)) and (cs.canStartGame(iOpponent)) and (pLeftPlayer.isAlive()) and (pRightPlayer.isAlive()):
						if (iOpponent == gc.getGame().getActivePlayer()):
							self.__EventSolmniumAcceptGameBegin((playerID, iOpponent, iGold))
					else :
						CyInterface().addMessage(playerID, True, 25, CyTranslator().getText("TXT_KEY_SOMNIUM_CANT_START_GAME", (gc.getPlayer(iOpponent).getName(), )), '', 1, '', en.eColorRed, -1, -1, False, False)

	def __EventSolmniumAcceptGameBegin(self, argslist):
		iPlayer, iOpponent, iGold = argslist
		if not gc.getPlayer(iOpponent).isAlive(): return 0

		popup = PyPopup.PyPopup(CvUtil.EventSolmniumAcceptGame, EventContextTypes.EVENTCONTEXT_ALL)

		popup.setUserData(argslist)

		popup.setHeaderString(localText.getText("TXT_KEY_SOMNIUM_START", ()))
		if iGold > 0 :
			popup.setBodyString(localText.getText("TXT_KEY_SOMNIUM_ACCEPT_GAME", (gc.getPlayer(iPlayer).getName(), iGold)))
		else :
			popup.setBodyString(localText.getText("TXT_KEY_SOMNIUM_ACCEPT_GAME_FUN", (gc.getPlayer(iPlayer).getName(), )))

		popup.addButton( localText.getText("AI_DIPLO_ACCEPT_1", ()) )
		popup.addButton( localText.getText("AI_DIPLO_NO_PEACE_3", ()) )

		popup.launch(False, PopupStates.POPUPSTATE_IMMEDIATE)

	def __EventSolmniumAcceptGameApply(self, playerID, userData, popupReturn):
		if userData :
			iPlayer, iOpponent, iGold = userData
			idButtonCliked = popupReturn.getButtonClicked()
			if idButtonCliked == 0 :
				if (cs.canStartGame(iPlayer)) and (cs.canStartGame(iOpponent)) and (gc.getPlayer(iPlayer).isAlive()) and (gc.getPlayer(iOpponent).isAlive()):
					cs.startGame(iPlayer, iOpponent, iGold)
				else :
					CyInterface().addMessage(iPlayer, True, 25, CyTranslator().getText("TXT_KEY_SOMNIUM_CANT_START_GAME", (gc.getPlayer(iOpponent).getName(), )), '', 1, '', en.eColorRed, -1, -1, False, False)
					CyInterface().addMessage(iOpponent, True, 25, CyTranslator().getText("TXT_KEY_SOMNIUM_CANT_START_GAME", (gc.getPlayer(iPlayer).getName(), )), '', 1, '', en.eColorRed, -1, -1, False, False)
			else :
					CyInterface().addMessage(iPlayer, True, 25, CyTranslator().getText("TXT_KEY_SOMNIUM_REFUSE_GAME", (gc.getPlayer(iOpponent).getName(), iGold)), '', 1, '', en.eColorRed, -1, -1, False, False)

	def __EventSolmniumConcedeGameBegin(self, argslist):
		popup = PyPopup.PyPopup(CvUtil.EventSolmniumConcedeGame, EventContextTypes.EVENTCONTEXT_ALL)

		popup.setUserData(argslist)

		popup.setHeaderString(localText.getText("TXT_KEY_SOMNIUM_START", ()))
		popup.setBodyString(localText.getText("TXT_KEY_SOMNIUM_CONCEDE_GAME", ()))

		popup.addButton( localText.getText("AI_DIPLO_ACCEPT_1", ()) )
		popup.addButton( localText.getText("AI_DIPLO_NO_PEACE_3", ()) )

		popup.launch(False, PopupStates.POPUPSTATE_IMMEDIATE)

	def __EventSolmniumConcedeGameApply(self, playerID, userData, popupReturn):
		if userData :
			idButtonCliked = popupReturn.getButtonClicked()
			if idButtonCliked == 0 :
				cs.endGame(userData[0], userData[1])
## FfH Card Game: end
