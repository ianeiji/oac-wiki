## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005
##
## Implementaion of miscellaneous game functions

import CvUtil
from CvPythonExtensions import *
import CvEventInterface
import CustomFunctions
import ScenarioFunctions
##--------	Enums Cache: Added by Denev	--------##
import CvPythonEnums
en = CvPythonEnums.CvPythonEnums()
##--------	Enums Cache: End Add		--------##

import PyHelpers
PyPlayer = PyHelpers.PyPlayer

import copy

# globals
cf = CustomFunctions.CustomFunctions()
gc = CyGlobalContext()
sf = ScenarioFunctions.ScenarioFunctions()


class CvFfHGameUtils:
	"Miscellaneous game functions"
	def __init__(self):
##--------	Advanced Rules: Modified by Denev
#		pass

		self.eChanneling1 = gc.getInfoTypeForString('PROMOTION_CHANNELING1')
		self.eChanneling2 = gc.getInfoTypeForString('PROMOTION_CHANNELING2')
		self.eChanneling3 = gc.getInfoTypeForString('PROMOTION_CHANNELING3')

		self.iSphereLimit = 3

		leSpellPromotions = [ePromotion for ePromotion in xrange(gc.getNumPromotionInfos()) if cyGetSphereFromPromotion(ePromotion) != PromotionTypes.NO_PROMOTION]
		self.leRank3SpellPromotions = [ePromotion for ePromotion in leSpellPromotions if gc.getPromotionInfo(ePromotion).getPromotionNextLevel() == PromotionTypes.NO_PROMOTION]
		self.leRank2SpellPromotions = [ePromotion for ePromotion in leSpellPromotions if gc.getPromotionInfo(ePromotion).getPromotionNextLevel() in self.leRank3SpellPromotions]
		self.leRank1SpellPromotions = [ePromotion for ePromotion in leSpellPromotions if gc.getPromotionInfo(ePromotion).getPromotionNextLevel() in self.leRank2SpellPromotions]

		self.leCombatUnitAIs = []
		lszCombatUnitAIs = ['UNITAI_ATTACK', 'UNITAI_ATTACK_CITY', 'UNITAI_RESERVE', 'UNITAI_COUNTER', 'UNITAI_CITY_DEFENSE', 'UNITAI_EXPLORE', 'UNITAI_HERO']
		for szCombatUnitAI in lszCombatUnitAIs:
			self.leCombatUnitAIs.append(gc.getInfoTypeForString(szCombatUnitAI))

		self.leCombatImportantPromotions = []
# Kaijin >>> --- OAC magic promotions ------------------------------------------------
		"""
		self.leCombatImportantPromotions.append(gc.getInfoTypeForString('PROMOTION_FIRE2'))		# fireball
		"""
		self.leCombatImportantPromotions.append(gc.getInfoTypeForString('PROMOTION_FIRE1'))		# fireball
		self.leCombatImportantPromotions.append(gc.getInfoTypeForString('PROMOTION_FIRE2'))		# fire elemental
		self.leCombatImportantPromotions.append(gc.getInfoTypeForString('PROMOTION_EARTH1'))	# stoneskin
		self.leCombatImportantPromotions.append(gc.getInfoTypeForString('PROMOTION_EARTH2'))	# earth elemental
# Kaijin <<< --- OAC magic promotions ------------------------------------------------

		self.leTerraformingPromotions = []
# Kaijin >>> --- OAC magic promotions ------------------------------------------------
		"""
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_METAMAGIC2'))	# dispel
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_METAMAGIC1'))
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_WATER2'))		# spring
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_WATER1'))
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_SUN1'))			# scorch
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_LIFE1'))		# sanctify
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_MOBILITY2'))
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_MOBILITY1'))
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_NATURE3'))		# vitalize
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_NATURE2'))
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_NATURE1'))
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_BODY1'))		# haste
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_EARTH1'))		# wall of stone
#		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_SPIRIT3'))		# trust
#		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_SPIRIT2'))		# hope
#		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_SPIRIT1'))
#		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_LIFE3'))		# resurrection
#		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_LIFE2'))
		"""
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_METAMAGIC2'))	# dispel
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_METAMAGIC1'))
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_WATER1'))		# spring
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_SUN1'))			# scorch
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_LIFE1'))		# sanctify
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_MOBILITY2'))
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_MOBILITY1'))
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_NATURE3'))		# vitalize
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_NATURE2'))
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_NATURE1'))
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_BODY1'))		# haste
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_EARTH2'))		# thaw
		self.leTerraformingPromotions.append(gc.getInfoTypeForString('PROMOTION_EARTH1'))		# wall of stone

		self.dWeights = [{}, {}, {}, {}]
		self.dWeights[0] =	{
								'PROMOTION_MOBILITY1'	: [gc.getInfoTypeForString('PROMOTION_MOBILITY1')	,100, 0],
								'PROMOTION_COMBAT5'		: [gc.getInfoTypeForString('PROMOTION_COMBAT5')		, 90, 0],
								'PROMOTION_COMBAT4'		: [gc.getInfoTypeForString('PROMOTION_COMBAT4')		, 80, 0],
								'PROMOTION_COMBAT3'		: [gc.getInfoTypeForString('PROMOTION_COMBAT3')		, 70, 0],
								'PROMOTION_COMBAT2'		: [gc.getInfoTypeForString('PROMOTION_COMBAT2')		, 60, 0],
								'PROMOTION_COMBAT1'		: [gc.getInfoTypeForString('PROMOTION_COMBAT1')		, 50, 0],
								'PROMOTION_EXTENSION3'	: [gc.getInfoTypeForString('PROMOTION_EXTENSION3')	,  0, 0],	# more consider
								'PROMOTION_EXTENSION2'	: [gc.getInfoTypeForString('PROMOTION_EXTENSION2')	,  0, 0],	# more consider
								'PROMOTION_EXTENSION1'	: [gc.getInfoTypeForString('PROMOTION_EXTENSION1')	,  0, 0],	# more consider
#								'PROMOTION_MOBILITY2'	: [gc.getInfoTypeForString('PROMOTION_MOBILITY2')	, 10, 0],
							}

		"""
		self.dWeights[1] =	{
								'PROMOTION_AIR'			: [gc.getInfoTypeForString('PROMOTION_AIR1')		, 80, 70],	# fair wind
								'PROMOTION_BODY'		: [gc.getInfoTypeForString('PROMOTION_BODY1')		, 90, 70],	# haste
								'PROMOTION_CHAOS'		: [gc.getInfoTypeForString('PROMOTION_CHAOS1')		, 60, 70],	# dance of blade
								'PROMOTION_DEATH'		: [gc.getInfoTypeForString('PROMOTION_DEATH1')		,100,  0],	# raise skeleton
								'PROMOTION_EARTH'		: [gc.getInfoTypeForString('PROMOTION_EARTH1')		, 30, 90],	# wall of stone
								'PROMOTION_ENTROPY'		: [gc.getInfoTypeForString('PROMOTION_ENTROPY1')	, 70,  0],	# summon pit beast
								'PROMOTION_ENCHANTMENT'	: [gc.getInfoTypeForString('PROMOTION_ENCHANTMENT1'), 70, 90],	# enchanted blade
								'PROMOTION_FIRE'		: [gc.getInfoTypeForString('PROMOTION_FIRE1')		,150,  0],	# blaze
								'PROMOTION_ICE'			: [gc.getInfoTypeForString('PROMOTION_ICE1')		, 80,  0],	# slow
								'PROMOTION_LAW'			: [gc.getInfoTypeForString('PROMOTION_LAW1')		, 50, 70],	# loyality
								'PROMOTION_LIFE'		: [gc.getInfoTypeForString('PROMOTION_LIFE1')		, 10, 80],	# sanctify
								'PROMOTION_METAMAGIC'	: [gc.getInfoTypeForString('PROMOTION_METAMAGIC1')	, 40, 60],	# summon floating eye
								'PROMOTION_MIND'		: [gc.getInfoTypeForString('PROMOTION_MIND1')		, 30, 30],	# charm person
								'PROMOTION_NATURE'		: [gc.getInfoTypeForString('PROMOTION_NATURE1')		, 20, 80],	# treetop defense
								'PROMOTION_SHADOW'		: [gc.getInfoTypeForString('PROMOTION_SHADOW1')		, 60, 70],	# blur
								'PROMOTION_SPIRIT'		: [gc.getInfoTypeForString('PROMOTION_SPIRIT1')		, 50, 70],	# courage
								'PROMOTION_SUN'			: [gc.getInfoTypeForString('PROMOTION_SUN1')		, 10, 80],	# scorch
								'PROMOTION_WATER'		: [gc.getInfoTypeForString('PROMOTION_WATER1')		,  0,  0],	# walter walking
							}
		"""
		self.dWeights[1] =	{
								'PROMOTION_AIR'			: [gc.getInfoTypeForString('PROMOTION_AIR1')		,100, 70],	# fair wind, maelstrom
								'PROMOTION_BODY'		: [gc.getInfoTypeForString('PROMOTION_BODY1')		, 90, 70],	# haste
								'PROMOTION_CHAOS'		: [gc.getInfoTypeForString('PROMOTION_CHAOS1')		, 60, 70],	# dance of blade
								'PROMOTION_DEATH'		: [gc.getInfoTypeForString('PROMOTION_DEATH1')		,100,  0],	# raise skeleton
								'PROMOTION_EARTH'		: [gc.getInfoTypeForString('PROMOTION_EARTH1')		,100, 90],	# wall of stone, stoneskin
								'PROMOTION_ENTROPY'		: [gc.getInfoTypeForString('PROMOTION_ENTROPY1')	, 70,  0],	# summon pit beast
								'PROMOTION_ENCHANTMENT'	: [gc.getInfoTypeForString('PROMOTION_ENCHANTMENT1'), 70, 90],	# enchanted blade
								'PROMOTION_FIRE'		: [gc.getInfoTypeForString('PROMOTION_FIRE1')		,150,  0],	# blaze, fireball
								'PROMOTION_ICE'			: [gc.getInfoTypeForString('PROMOTION_ICE1')		,100,  0],	# slow, summon ice elemental
								'PROMOTION_LAW'			: [gc.getInfoTypeForString('PROMOTION_LAW1')		, 50, 70],	# loyality
								'PROMOTION_LIFE'		: [gc.getInfoTypeForString('PROMOTION_LIFE1')		, 10, 80],	# sanctify
								'PROMOTION_METAMAGIC'	: [gc.getInfoTypeForString('PROMOTION_METAMAGIC1')	, 40, 60],	# summon floating eye
								'PROMOTION_MIND'		: [gc.getInfoTypeForString('PROMOTION_MIND1')		, 30, 30],	# charm person
								'PROMOTION_NATURE'		: [gc.getInfoTypeForString('PROMOTION_NATURE1')		, 20, 80],	# treetop defense
								'PROMOTION_SHADOW'		: [gc.getInfoTypeForString('PROMOTION_SHADOW1')		, 60, 70],	# blur
								'PROMOTION_SPIRIT'		: [gc.getInfoTypeForString('PROMOTION_SPIRIT1')		, 50, 70],	# courage
								'PROMOTION_SUN'			: [gc.getInfoTypeForString('PROMOTION_SUN1')		, 10, 80],	# scorch
								'PROMOTION_WATER'		: [gc.getInfoTypeForString('PROMOTION_WATER1')		, 50,  0],	# spring, walter walking
								'PROMOTION_DIMENSIONAL'	: [gc.getInfoTypeForString('PROMOTION_DIMENSIONAL1'), 10, 70],	# escape
								'PROMOTION_DARK_MAGIC'	: [gc.getInfoTypeForString('PROMOTION_DARK_MAGIC1')	, 70,  0],	# hell worm
							}

		"""
		self.dWeights[2] =	{
								'PROMOTION_AIR'			: [gc.getInfoTypeForString('PROMOTION_AIR2')		, 90, 10],	# maelstrom
								'PROMOTION_BODY'		: [gc.getInfoTypeForString('PROMOTION_BODY2')		, 60, 50],	# regeneration
								'PROMOTION_CHAOS'		: [gc.getInfoTypeForString('PROMOTION_CHAOS2')		, 10, 90],	# mutation
								'PROMOTION_DEATH'		: [gc.getInfoTypeForString('PROMOTION_DEATH2')		, 80,  0],	# summon spectre
								'PROMOTION_EARTH'		: [gc.getInfoTypeForString('PROMOTION_EARTH2')		, 20,  0],	# stoneskin
								'PROMOTION_ENTROPY'		: [gc.getInfoTypeForString('PROMOTION_ENTROPY2')	, 80, 20],	# rust
								'PROMOTION_ENCHANTMENT'	: [gc.getInfoTypeForString('PROMOTION_ENCHANTMENT2'), 50, 90],	# flaming arrow
								'PROMOTION_FIRE'		: [gc.getInfoTypeForString('PROMOTION_FIRE2')		,200,  0],	# fireball
								'PROMOTION_ICE'			: [gc.getInfoTypeForString('PROMOTION_ICE2')		,100,  0],	# summon ice elemental
								'PROMOTION_LAW'			: [gc.getInfoTypeForString('PROMOTION_LAW2')		, 70,  0],	# summon host of the einherjar
								'PROMOTION_LIFE'		: [gc.getInfoTypeForString('PROMOTION_LIFE2')		, 50, 20],	# destroy undead
								'PROMOTION_METAMAGIC'	: [gc.getInfoTypeForString('PROMOTION_METAMAGIC2')	, 40, 80],	# dispel
								'PROMOTION_MIND'		: [gc.getInfoTypeForString('PROMOTION_MIND2')		, 70, 30],	# inspiration
								'PROMOTION_NATURE'		: [gc.getInfoTypeForString('PROMOTION_NATURE2')		, 40, 90],	# poisoned blade
								'PROMOTION_SHADOW'		: [gc.getInfoTypeForString('PROMOTION_SHADOW2')		, 90, 60],	# shadowwalk
								'PROMOTION_SPIRIT'		: [gc.getInfoTypeForString('PROMOTION_SPIRIT2')		, 10, 90],	# hope
								'PROMOTION_SUN'			: [gc.getInfoTypeForString('PROMOTION_SUN2')		, 60, 20],	# blinding light
								'PROMOTION_WATER'		: [gc.getInfoTypeForString('PROMOTION_WATER2')		,  0, 90],	# spring
							}
		"""
		self.dWeights[2] =	{
								'PROMOTION_AIR'			: [gc.getInfoTypeForString('PROMOTION_AIR2')		,100, 10],	# summon air elemental, balmy breeze
								'PROMOTION_BODY'		: [gc.getInfoTypeForString('PROMOTION_BODY2')		, 80, 70],	# regeneration
								'PROMOTION_CHAOS'		: [gc.getInfoTypeForString('PROMOTION_CHAOS2')		, 50, 90],	# mutation
								'PROMOTION_DEATH'		: [gc.getInfoTypeForString('PROMOTION_DEATH2')		,150,  0],	# summon spectre, exhoustion
								'PROMOTION_EARTH'		: [gc.getInfoTypeForString('PROMOTION_EARTH2')		, 80,  0],	# summon earth elemental, thaw
								'PROMOTION_ENTROPY'		: [gc.getInfoTypeForString('PROMOTION_ENTROPY2')	, 80, 20],	# rust
								'PROMOTION_ENCHANTMENT'	: [gc.getInfoTypeForString('PROMOTION_ENCHANTMENT2'), 50, 90],	# flaming arrow
								'PROMOTION_FIRE'		: [gc.getInfoTypeForString('PROMOTION_FIRE2')		,200,  0],	# summon fire elemental
								'PROMOTION_ICE'			: [gc.getInfoTypeForString('PROMOTION_ICE2')		,130,  0],	# icicle arrow
								'PROMOTION_LAW'			: [gc.getInfoTypeForString('PROMOTION_LAW2')		, 80, 40],	# summon host of the einherjar, sealed
								'PROMOTION_LIFE'		: [gc.getInfoTypeForString('PROMOTION_LIFE2')		, 50, 20],	# destroy undead
								'PROMOTION_METAMAGIC'	: [gc.getInfoTypeForString('PROMOTION_METAMAGIC2')	, 40, 80],	# dispel
								'PROMOTION_MIND'		: [gc.getInfoTypeForString('PROMOTION_MIND2')		, 80, 50],	# inspiration, tranquilizing
								'PROMOTION_NATURE'		: [gc.getInfoTypeForString('PROMOTION_NATURE2')		, 40, 90],	# poisoned blade, summon griffon
								'PROMOTION_SHADOW'		: [gc.getInfoTypeForString('PROMOTION_SHADOW2')		,120, 60],	# shadowwalk, blindness
								'PROMOTION_SPIRIT'		: [gc.getInfoTypeForString('PROMOTION_SPIRIT2')		, 10, 90],	# hope
								'PROMOTION_SUN'			: [gc.getInfoTypeForString('PROMOTION_SUN2')		, 60, 20],	# blinding light
								'PROMOTION_WATER'		: [gc.getInfoTypeForString('PROMOTION_WATER2')		, 50, 90],	# summon water elemental
								'PROMOTION_DIMENSIONAL'	: [gc.getInfoTypeForString('PROMOTION_DIMENSIONAL2'), 30, 90],	# differentlayer transition
								'PROMOTION_DARK_MAGIC'	: [gc.getInfoTypeForString('PROMOTION_DARK_MAGIC2')	, 90, 20],	# hypnotism
							}

		"""
		self.dWeights[3] =	{
								'PROMOTION_AIR'			: [gc.getInfoTypeForString('PROMOTION_AIR3')		, 50,  0],	# summon air elemental
								'PROMOTION_BODY'		: [gc.getInfoTypeForString('PROMOTION_BODY3')		, 60,  0],	# graft flesh
								'PROMOTION_CHAOS'		: [gc.getInfoTypeForString('PROMOTION_CHAOS3')		, 10,  0],	# wonder
								'PROMOTION_DEATH'		: [gc.getInfoTypeForString('PROMOTION_DEATH3')		,200,  0],	# lichdom
								'PROMOTION_EARTH'		: [gc.getInfoTypeForString('PROMOTION_EARTH3')		, 70,  0],	# summon earth elemental
								'PROMOTION_ENTROPY'		: [gc.getInfoTypeForString('PROMOTION_ENTROPY3')	, 90, 10],	# wither
								'PROMOTION_ENCHANTMENT'	: [gc.getInfoTypeForString('PROMOTION_ENCHANTMENT3'), 50,  0],	# create spellstaff
								'PROMOTION_FIRE'		: [gc.getInfoTypeForString('PROMOTION_FIRE3')		, 60,  0],	# summon fire elemental
								'PROMOTION_ICE'			: [gc.getInfoTypeForString('PROMOTION_ICE3')		,150,  0],	# snowfall
								'PROMOTION_LAW'			: [gc.getInfoTypeForString('PROMOTION_LAW3')		, 80, 90],	# valor
								'PROMOTION_LIFE'		: [gc.getInfoTypeForString('PROMOTION_LIFE3')		, 40, 90],	# resurrection
								'PROMOTION_METAMAGIC'	: [gc.getInfoTypeForString('PROMOTION_METAMAGIC3')	, 50,  0],	# summon djinn
								'PROMOTION_MIND'		: [gc.getInfoTypeForString('PROMOTION_MIND3')		,100,  0],	# domination
								'PROMOTION_NATURE'		: [gc.getInfoTypeForString('PROMOTION_NATURE3')		,  0, 90],	# vitalize
								'PROMOTION_SHADOW'		: [gc.getInfoTypeForString('PROMOTION_SHADOW3')		, 50,  0],	# summon mistform
								'PROMOTION_SPIRIT'		: [gc.getInfoTypeForString('PROMOTION_SPIRIT3')		,  0, 90],	# trust
								'PROMOTION_SUN'			: [gc.getInfoTypeForString('PROMOTION_SUN3')		, 50,  0],	# summon aurealis
								'PROMOTION_WATER'		: [gc.getInfoTypeForString('PROMOTION_WATER3')		, 50,  0],	# summon water elemental
							}
		"""
		self.dWeights[3] =	{
								'PROMOTION_AIR'			: [gc.getInfoTypeForString('PROMOTION_AIR3')		,200,  0],	# thunder
								'PROMOTION_BODY'		: [gc.getInfoTypeForString('PROMOTION_BODY3')		,100, 30],	# graft flesh, restoration
								'PROMOTION_CHAOS'		: [gc.getInfoTypeForString('PROMOTION_CHAOS3')		,150,  0],	# wonder, death cloud
								'PROMOTION_DEATH'		: [gc.getInfoTypeForString('PROMOTION_DEATH3')		,200,  0],	# lichdom, sumon wraith, hand of the death
								'PROMOTION_EARTH'		: [gc.getInfoTypeForString('PROMOTION_EARTH3')		,  0,  0],	# soil preparation
								'PROMOTION_ENTROPY'		: [gc.getInfoTypeForString('PROMOTION_ENTROPY3')	,100, 10],	# wither, summon ahalpuh
								'PROMOTION_ENCHANTMENT'	: [gc.getInfoTypeForString('PROMOTION_ENCHANTMENT3'), 70, 50],	# create spellstaff, activation
								'PROMOTION_FIRE'		: [gc.getInfoTypeForString('PROMOTION_FIRE3')		,150,  0],	# fire storm
								'PROMOTION_ICE'			: [gc.getInfoTypeForString('PROMOTION_ICE3')		,150,  0],	# snowfall
								'PROMOTION_LAW'			: [gc.getInfoTypeForString('PROMOTION_LAW3')		,100, 90],	# valor, control
								'PROMOTION_LIFE'		: [gc.getInfoTypeForString('PROMOTION_LIFE3')		, 40,100],	# resurrection, revival of onetime only
								'PROMOTION_METAMAGIC'	: [gc.getInfoTypeForString('PROMOTION_METAMAGIC3')	,150,  0],	# summon djinn, tiltowaito
								'PROMOTION_MIND'		: [gc.getInfoTypeForString('PROMOTION_MIND3')		,200,  0],	# domination, depression
								'PROMOTION_NATURE'		: [gc.getInfoTypeForString('PROMOTION_NATURE3')		,150, 90],	# vitalize, poison cloud
								'PROMOTION_SHADOW'		: [gc.getInfoTypeForString('PROMOTION_SHADOW3')		, 80,  0],	# summon mistform, hidden
								'PROMOTION_SPIRIT'		: [gc.getInfoTypeForString('PROMOTION_SPIRIT3')		, 80, 90],	# trust, ire
								'PROMOTION_SUN'			: [gc.getInfoTypeForString('PROMOTION_SUN3')		,100,  0],	# summon aurealis, prismic missile
								'PROMOTION_WATER'		: [gc.getInfoTypeForString('PROMOTION_WATER3')		,100,  0],	# landfill, hurricane
								'PROMOTION_DIMENSIONAL'	: [gc.getInfoTypeForString('PROMOTION_DIMENSIONAL3'), 90, 50],	# teleport, transfer
								'PROMOTION_DARK_MAGIC'	: [gc.getInfoTypeForString('PROMOTION_DARK_MAGIC3')	,200,100],	# feral
							}
# Kaijin <<< --- OAC magic promotions ------------------------------------------------

		self.dCivWeights = [[{}, {}, {}, {}] for iCivilization in xrange(gc.getNumCivilizationInfos())]

		dCivWeight = self.dCivWeights[gc.getInfoTypeForString('CIVILIZATION_LUCHUIRP')]
		dCivWeight[1]['PROMOTION_ENCHANTMENT'] = [70, 0]

		dCivWeight = self.dCivWeights[gc.getInfoTypeForString('CIVILIZATION_BALSERAPHS')]
		dCivWeight[1]['PROMOTION_MIND'] = [100, 0]
		dCivWeight[2]['PROMOTION_MIND'] = [100, 0]

# Kaijin >>> --- OAC magic promotions ------------------------------------------------
		dCivWeight = self.dCivWeights[gc.getInfoTypeForString('CIVILIZATION_SHEAIM')]
		dCivWeight[1]['PROMOTION_DEATH'] = [100, 0]
		dCivWeight[2]['PROMOTION_DEATH'] = [100, 0]

		dCivWeight = self.dCivWeights[gc.getInfoTypeForString('CIVILIZATION_DROAUM')]
		dCivWeight[1]['PROMOTION_DEATH'] = [100, 0]
		dCivWeight[2]['PROMOTION_DEATH'] = [100, 0]

		dCivWeight = self.dCivWeights[gc.getInfoTypeForString('CIVILIZATION_DESPIEL')]
		dCivWeight[1]['PROMOTION_ENTROPY'] = [150, 0]
		dCivWeight[1]['PROMOTION_DIMENSIONAL'] = [100, 0]
		dCivWeight[2]['PROMOTION_DIMENSIONAL'] = [100, 0]
		dCivWeight[3]['PROMOTION_DIMENSIONAL'] = [100, 0]

#		dCivWeight = self.dCivWeights[gc.getInfoTypeForString('CIVILIZATION_ALTAIR')]
#		dCivWeight[1]['PROMOTION_NATURE'] = [100, 0]

		dCivWeight = self.dCivWeights[gc.getInfoTypeForString('CIVILIZATION_SCIONS')]
		dCivWeight[1]['PROMOTION_BODY'] = [100, 0]
		dCivWeight[2]['PROMOTION_BODY'] = [100, 0]
		dCivWeight[3]['PROMOTION_BODY'] = [100, 0]

		dCivWeight = self.dCivWeights[gc.getInfoTypeForString('CIVILIZATION_NOUGBII')]
		dCivWeight[1]['PROMOTION_ENCHANTMENT'] = [70, 0]
# Kaijin <<< --- OAC magic promotions ------------------------------------------------

##--------	Advanced Rules: End Modify

	def isVictoryTest(self):
		if ( gc.getGame().getElapsedGameTurns() > 10 ):
			return True
		else:
			return False

	def isVictory(self, argsList):
		eVictory = argsList[0]
		return True

	def isPlayerResearch(self, argsList):
		ePlayer = argsList[0]
		return True

	def getExtraCost(self, argsList):
		ePlayer = argsList[0]
		return 0

	def createBarbarianCities(self):
		return False

	def createBarbarianUnits(self):
		return False

	def skipResearchPopup(self,argsList):
		ePlayer = argsList[0]
# ent >>>
		# Reserve Research Into
		if gc.getGame().getElapsedGameTurns() <= 4:
			if gc.getGame().getHandicapType() > gc.getInfoTypeForString('HANDICAP_NOBLE'):
				return True
# ent <<<
		return False

	def showTechChooserButton(self,argsList):
		ePlayer = argsList[0]
		return True

	def getFirstRecommendedTech(self,argsList):
		ePlayer = argsList[0]
		return TechTypes.NO_TECH

	def getSecondRecommendedTech(self,argsList):
		ePlayer = argsList[0]
		eFirstTech = argsList[1]
		return TechTypes.NO_TECH

	def canRazeCity(self,argsList):
		iRazingPlayer, pCity = argsList
		return True

	def canDeclareWar(self,argsList):
		iAttackingTeam, iDefendingTeam = argsList
		return True

	def skipProductionPopup(self,argsList):
		pCity = argsList[0]
		return False

	def showExamineCityButton(self,argsList):
		pCity = argsList[0]
		return True

	def getRecommendedUnit(self,argsList):
		pCity = argsList[0]
		return UnitTypes.NO_UNIT

	def getRecommendedBuilding(self,argsList):
		pCity = argsList[0]
		return BuildingTypes.NO_BUILDING

	def updateColoredPlots(self):
		return False

	def isActionRecommended(self,argsList):
		pUnit = argsList[0]
		iAction = argsList[1]
		return False

	def unitCannotMoveInto(self,argsList):
		ePlayer = argsList[0]
		iUnitId = argsList[1]
		iPlotX = argsList[2]
		iPlotY = argsList[3]
# Kaijin Start
		pPlayer = gc.getPlayer(ePlayer)
		pUnit = pPlayer.getUnit(iUnitId)
		pPlot = CyMap().plot(iPlotX,iPlotY)

		if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_TROLL'):
			if pPlot.isWater():
				if not pPlot.isLake():
					return True

		if not pPlayer.isHuman():

			if pPlot.getFeatureType() in (gc.getInfoTypeForString('FEATURE_VOID'), gc.getInfoTypeForString('FEATURE_DISTORTION')):
				if not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_KODS_ITEMS')):
					return True

			if pPlot.isWater():
				if pUnit.getUnitCombatType() != gc.getInfoTypeForString('UNITCOMBAT_NAVAL'):
					if pUnit.getDomainType() != gc.getInfoTypeForString('DOMAIN_SEA'):
						if pPlot.getTerrainType() == gc.getInfoTypeForString('TERRAIN_COAST'):
							if	(	pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_AMPHIBIOUS'))
								or	pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_WATER2'))
								or	pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_WATER_WALKING'))
								or	pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BRACELET_OF_NIGHTMARE'))	):
								if not pUnit.isFlying() and not pUnit.canMoveAllTerrain():
									if not pPlot.isVisibleEnemyUnit(ePlayer):
										return True

# Kaijin End
# ent start
		if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_BASQUE')):
			return True
# ent end
		return False

	def cannotHandleAction(self,argsList):
		pPlot = argsList[0]
		iAction = argsList[1]
		bTestVisible = argsList[2]
		return False

	def canBuild(self,argsList):
		iX, iY, iBuild, iPlayer = argsList
##--------	Unofficial Bug Fix: Modified by Denev 2012/05/26
#		return -1	# Returning -1 means ignore; 0 means Build cannot be performed; 1 or greater means it can
		return False
##--------	Unofficial Bug Fix: End Modify

##--------	Unofficial Bug Fix: Added by Denev 2012/05/26
	def cannotBuild(self,argsList):
		iX, iY, iBuild, iPlayer = argsList
		return False
##--------	Unofficial Bug Fix: End Modify

	def cannotFoundCity(self,argsList):
		iPlayer, iPlotX, iPlotY = argsList
#Kaijin >>>
		pPlot = CyMap().plot(iPlotX,iPlotY)
		pPlayer = gc.getPlayer(iPlayer)

	# scions start
		if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_SETTLERS):
			if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_SCIONS'):
				if pPlayer.getNumCities() > 0:
					return True
	# scions end
#Kaijin <<<
		return False

	def cannotSelectionListMove(self,argsList):
		pPlot = argsList[0]
		bAlt = argsList[1]
		bShift = argsList[2]
		bCtrl = argsList[3]
		return False

	def cannotSelectionListGameNetMessage(self,argsList):
		eMessage = argsList[0]
		iData2 = argsList[1]
		iData3 = argsList[2]
		iData4 = argsList[3]
		iFlags = argsList[4]
		bAlt = argsList[5]
		bShift = argsList[6]
		return False

	def cannotDoControl(self,argsList):
		eControl = argsList[0]
		return False

	def canResearch(self,argsList):
		ePlayer = argsList[0]
		eTech = argsList[1]
		bTrade = argsList[2]
		return False

	def cannotResearch(self,argsList):
		ePlayer = argsList[0]
		eTech = argsList[1]
		bTrade = argsList[2]
		pPlayer = gc.getPlayer(ePlayer)

		if eTech == gc.getInfoTypeForString('TECH_ORDERS_FROM_HEAVEN'):
			if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_RELIGION_1):
				return True
#			if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGNOSTIC')):
#				return True
			if not pPlayer.isHuman():
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getReligionWeightModifier(gc.getInfoTypeForString('RELIGION_THE_ORDER')) < 0:
					return True

		elif eTech == gc.getInfoTypeForString('TECH_WAY_OF_THE_EARTHMOTHER'):
			if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_RELIGION_3):
				return True
#			if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGNOSTIC')):
#				return True
			if not pPlayer.isHuman():
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getReligionWeightModifier(gc.getInfoTypeForString('RELIGION_RUNES_OF_KILMORPH')) < 0:
					return True

		elif eTech == gc.getInfoTypeForString('TECH_WAY_OF_THE_FORESTS'):
			if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_RELIGION_0):
				return True
#			if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGNOSTIC')):
#				return True
			if not pPlayer.isHuman():
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getReligionWeightModifier(gc.getInfoTypeForString('RELIGION_FELLOWSHIP_OF_LEAVES')) < 0:
					return True

		elif eTech == gc.getInfoTypeForString('TECH_MESSAGE_FROM_THE_DEEP'):
			if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_RELIGION_2):
				return True
#			if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGNOSTIC')):
#				return True
			if not pPlayer.isHuman():
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getReligionWeightModifier(gc.getInfoTypeForString('RELIGION_OCTOPUS_OVERLORDS')) < 0:
					return True

		elif eTech == gc.getInfoTypeForString('TECH_CORRUPTION_OF_SPIRIT'):
			if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_RELIGION_4):
				return True
#			if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGNOSTIC')):
#				return True
			if not pPlayer.isHuman():
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getReligionWeightModifier(en.eReligionAshenVeil) < 0:
					return True

##--------	Advanced Rules: Deleted by Denev 2011/01/10
					"""
		elif eTech == gc.getInfoTypeForString('TECH_HONOR'):
			if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGNOSTIC')):
				return True
			if not pPlayer.isHuman():
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getReligionWeightModifier(gc.getInfoTypeForString('RELIGION_THE_EMPYREAN')) < 0:
					return True

		elif eTech == gc.getInfoTypeForString('TECH_DECEPTION'):
			if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGNOSTIC')):
				return True
			if not pPlayer.isHuman():
				if gc.getLeaderHeadInfo(pPlayer.getLeaderType()).getReligionWeightModifier(gc.getInfoTypeForString('RELIGION_COUNCIL_OF_ESUS')) < 0:
					return True
					"""
##--------	Advanced Rules: End Delete

#Kaijin >>>
				"""
##--------	Advanced Rules: Added by Denev 2011/05/16
		elif eTech == gc.getInfoTypeForString('TECH_MALEVOLENT_DESIGNS'):
			if pPlayer.getAlignment() == en.eAlignmentGood:
				return True
			if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_RIGHTEOUSNESS')):
				return True

		elif eTech == gc.getInfoTypeForString('TECH_RIGHTEOUSNESS'):
			if pPlayer.getAlignment() == en.eAlignmentEvil:
				return True
			if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_MALEVOLENT_DESIGNS')):
				return True
##--------	Advanced Rules: End Add
				"""

		if eTech == gc.getInfoTypeForString('TECH_SEAFARING'):
			return True
		elif eTech == gc.getInfoTypeForString('TECH_DISCOVERY_OF_TRAIL'):
			return True
		elif eTech == gc.getInfoTypeForString('TECH_THE_GIFT'):
			return True
#Kaijin <<<

		if CyGame().getWBMapScript():
			bBlock = sf.cannotResearch(ePlayer, eTech, bTrade)
			if bBlock:
				return True

		return False

	def canDoCivic(self,argsList):
		ePlayer = argsList[0]
		eCivic = argsList[1]
		return False

	def cannotDoCivic(self,argsList):
		ePlayer = argsList[0]
		eCivic = argsList[1]

# Kaijin OAC >>>
		pPlayer = gc.getPlayer(ePlayer)
		if not pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_AGNOSTIC')):
			if eCivic == gc.getInfoTypeForString('CIVIC_HUMANISM'):
				return True
			elif eCivic == gc.getInfoTypeForString('CIVIC_PRINCIPLE_OF_THE_OLD'):
				return True
# Kaijin OAC <<<
		return False

	def canTrain(self,argsList):
		pCity = argsList[0]
		eUnit = argsList[1]
		bContinue = argsList[2]
		bTestVisible = argsList[3]
		bIgnoreCost = argsList[4]
		bIgnoreUpgrades = argsList[5]
		return False

	def cannotTrain(self,argsList):
		pCity = argsList[0]
		eUnit = argsList[1]
		bContinue = argsList[2]
		bTestVisible = argsList[3]
		bIgnoreCost = argsList[4]
		bIgnoreUpgrades = argsList[5]
		ePlayer = pCity.getOwner()
		pPlayer = gc.getPlayer(ePlayer)
		eUnitClass = gc.getUnitInfo(eUnit).getUnitClassType()
		pTeam = gc.getTeam(pPlayer.getTeam())

		if eUnitClass == gc.getInfoTypeForString('UNITCLASS_BEAST_OF_AGARES'):
			if pCity.getPopulation() <= 5:
				return True

		elif eUnitClass == gc.getInfoTypeForString('UNITCLASS_ACHERON'):
			if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_ACHERON):
				return True

		elif eUnitClass == gc.getInfoTypeForString('UNITCLASS_DUIN'):
			if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_DUIN):
				return True

		if pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_CULTURAL_VALUES')) == gc.getInfoTypeForString('CIVIC_CRUSADE'):
			if eUnitClass == gc.getInfoTypeForString('UNITCLASS_WORKER'):
				return True
			elif eUnitClass == gc.getInfoTypeForString('UNITCLASS_SETTLER'):
				return True
			elif eUnitClass == gc.getInfoTypeForString('UNITCLASS_WORKBOAT'):
				return True

#Kaijin >>>
	# Define
		eCiv = pCity.getCivilizationType()
		infoCiv = gc.getCivilizationInfo(pPlayer.getCivilizationType())
		iNumCities = pPlayer.getNumCities()

# Limit of the units.
	## Cult of the Dragon
		if eUnit == gc.getInfoTypeForString('UNIT_DISCIPLE_OF_THE_DRAGON'):
			if not eCiv in (gc.getInfoTypeForString('CIVILIZATION_SHEAIM'),
							gc.getInfoTypeForString('CIVILIZATION_KURIOTATES'),
							gc.getInfoTypeForString('CIVILIZATION_MAZATL')):
				return True

	## Illians - Priest of Winter
		if eUnit == gc.getInfoTypeForString('UNIT_PRIEST_OF_WINTER'):
			if not CyGame().getProjectCreatedCount(gc.getInfoTypeForString('PROJECT_THE_WHITE_HAND')) > 0:
				return True

	## Echigo - Haisui-no-zin
		if pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_CULTURAL_VALUES')) == gc.getInfoTypeForString('CIVIC_CRUSADE_ECHIGO'):
			if eUnitClass == gc.getInfoTypeForString('UNITCLASS_WORKER'):
				return True
			elif eUnitClass == gc.getInfoTypeForString('UNITCLASS_SETTLER'):
				return True
			elif eUnitClass == gc.getInfoTypeForString('UNITCLASS_WORKBOAT'):
				return True

	## Tiger - Smiley
		if pPlayer.getLeaderType() == gc.getInfoTypeForString('LEADER_SMILEY'):
			if eUnit in (	gc.getInfoTypeForString('UNIT_FOX'), 
							gc.getInfoTypeForString('UNIT_HOUND'), 
							gc.getInfoTypeForString('UNIT_EIN'), 
							gc.getInfoTypeForString('UNIT_LOUISA'), 
							gc.getInfoTypeForString('UNIT_ANTONIO'), 
							gc.getInfoTypeForString('UNIT_CORTEZ')		):
				return True

	## Xoth - Sanity-Point
		if eUnitClass in (	gc.getInfoTypeForString('UNITCLASS_NIGGURATH'), 
							gc.getInfoTypeForString('UNITCLASS_NYARLATHOTEP'), 
							gc.getInfoTypeForString('UNITCLASS_SOTHOTH')		):
			if pPlayer.getGuildPlusCounter(50) >= 20:
				return True

	## AI only - Start
		if not pPlayer.isHuman():

			if pCity.getOwner() == gc.getBARBARIAN_PLAYER():
				return False
			if pPlayer.AI_isFinancialTrouble():
				return False

		## City population num
			if pPlayer.getGuildPlusCounter(2) == 1:
				iPopLevel = (pCity.getPopulation())
			else:
				iPopLevel = (pCity.getPopulation() // 3)

		## General Combat Units
			## Combat Adept
			eAdept = gc.getInfoTypeForString('UNITCLASS_ADEPT')
			eAdeptCiv = infoCiv.getCivilizationUnits(eAdept)
			iAdeptNum = pPlayer.getUnitClassCountPlusMaking(eAdept)
			if eUnit == eAdeptCiv:
				if not eCiv in (gc.getInfoTypeForString('CIVILIZATION_AMURITES'),
								gc.getInfoTypeForString('CIVILIZATION_SHEAIM'),
								gc.getInfoTypeForString('CIVILIZATION_DESPIEL')):
					if (	pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_ARCANE')) 
							or pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_SUMMONER')) 
							or pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_CHANTER'))	):
						if ((iPopLevel * iNumCities) + 2) < (2 * (iAdeptNum)):
							return True
					else:
						if ((iPopLevel * iNumCities) + 2) < (3 * (iAdeptNum)):
							return True

# ent >>>
			## Lunatic - SlaveTrade
			eLunatic = gc.getInfoTypeForString('UNITCLASS_LUNATIC')
			eLunaticCiv = infoCiv.getCivilizationUnits(eLunatic)
			iLunaticNum = pPlayer.getUnitClassCountPlusMaking(eLunatic)
			if eUnit == eLunaticCiv:
				if iLunaticNum > iNumCities:
					return True
# ent <<<

	## AI only - End

#Kaijin <<<

		if CyGame().getWBMapScript():
			bBlock = sf.cannotTrain(pCity, eUnit, bContinue, bTestVisible, bIgnoreCost, bIgnoreUpgrades)
			if bBlock:
				return True

		return False

	def canConstruct(self,argsList):
		pCity = argsList[0]
		eBuilding = argsList[1]
		bContinue = argsList[2]
		bTestVisible = argsList[3]
		bIgnoreCost = argsList[4]
		return False

	def cannotConstruct(self,argsList):
		pCity = argsList[0]
		eBuilding = argsList[1]
		bContinue = argsList[2]
		bTestVisible = argsList[3]
		bIgnoreCost = argsList[4]
		pPlayer = gc.getPlayer(pCity.getOwner())
		eBuildingClass = gc.getBuildingInfo(eBuilding).getBuildingClassType()

		"""
		if pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_CULTURAL_VALUES')) == gc.getInfoTypeForString('CIVIC_CRUSADE'):
			if eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_ELDER_COUNCIL'):
				return True
			elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_MARKET'):
				return True
			elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_MONUMENT'):
				return True
			elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_MONEYCHANGER'):
				return True
			elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_THEATRE'):
				return True
			elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_AQUEDUCT'):
				return True
			elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_PUBLIC_BATHS'):
				return True
			elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_HERBALIST'):
				return True
			elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_CARNIVAL'):
				return True
			elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_COURTHOUSE'):
				return True
			elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_GAMBLING_HOUSE'):
				return True
			elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_GRANARY'):
				return True
			elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_SMOKEHOUSE'):
				return True
			elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_LIBRARY'):
				return True
			elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_HARBOR'):
				return True
			elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_ALCHEMY_LAB'):
				return True
			elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_BREWERY'):
				return True
		"""

		if eBuilding == gc.getInfoTypeForString('BUILDING_SHRINE_OF_THE_CHAMPION'):
			# Denev ToDo: team civilization can not construct. (splitted palace)
			"""
			iHero = gc.getCivilizationInfo(pPlayer.getCivilizationType()).getHero()
			if iHero == UnitTypes.NO_UNIT:
				return True
			if gc.getUnitInfo(iHero).isMechUnit():
				return True
			iHeroClass = gc.getUnitInfo(iHero).getUnitClassType()
			if not CyGame().isUnitClassMaxedOut(iHeroClass, 0):
				return True
			for iLoopPlayer in xrange(gc.getMAX_PLAYERS()):
				if pPlayer.getUnitClassCount(iHeroClass) > 0:
					return True
			"""
			eHero = cf.getDeadHero(pCity.getOwner())
			if eHero == UnitTypes.NO_UNIT:
				return True

		elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_MERCURIAN_GATE'):
			if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_NO_HYBOREM_OR_BASIUM):
				return True
			if pPlayer.getStateReligion() == en.eReligionAshenVeil:
				return True
			if pCity.isCapital():
				return True
##--------	Advanced Rules: Added by Denev
			if CyGame().getGlobalCounter() < 30:
				for eLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
					pLoopPlayer = gc.getPlayer(eLoopPlayer)
					if pLoopPlayer.isAlive():
						if pLoopPlayer.getCivilizationType() == en.eCivilizationInfernal:
							break
				else:
					return True
##--------	Advanced Rules: End Add
			if not pPlayer.isHuman():
				"""
				if pPlayer.getAlignment() == en.eAlignmentEvil:
					return True
				"""
##--------	Better AI: Added by Denev 2010/08/12
				if pCity.getID() == pPlayer.AI_getBestGreatPeopleFarm().getID():
					return True
##--------	Better AI: End Add
# Kaijin OAC >>>
		## When A.I. controled, Xoth do not build Mercurian Gate.
				if pPlayer.getCivilizationType() == en.eCivilizationXoth:
					return True

# ent >>>
				if pPlayer.isIgnoreFood():
					return True
				if pPlayer.getNumCities() < gc.getWorldInfo(CyMap().getWorldSize()).getTargetNumCities():
					return True
				if CyGame().getPlayerRank(pCity.getOwner()) > 3:
					return True
# ent <<<

# Kaijin OAC <<<

		if eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_SMUGGLERS_PORT'):
			if not pPlayer.isSmugglingRing():
				return True

		leAltar = [	gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR'),
					gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_ANOINTED'),
					gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_BLESSED'),
					gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_CONSECRATED'),
					gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_DIVINE'),
					gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_EXALTED'),
					gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_FINAL')	]
		iNumAltar = len(leAltar)
		for i in range(iNumAltar):
			if eBuilding == leAltar[i]:
				if pPlayer.getAlignment() == en.eAlignmentEvil:
					return True
				for j in range(i+1, iNumAltar):
					if pPlayer.countNumBuildings(leAltar[j]) > 0:
						return True
				break
		"""
		iAltar1 = gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR')
		iAltar2 = gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_ANOINTED')
		iAltar3 = gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_BLESSED')
		iAltar4 = gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_CONSECRATED')
		iAltar5 = gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_DIVINE')
		iAltar6 = gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_EXALTED')
		iAltar7 = gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_LUONNOTAR_FINAL')
		if eBuilding in (iAltar1, iAltar2, iAltar3, iAltar4, iAltar5, iAltar6, iAltar7):
			if pPlayer.getAlignment() == en.eAlignmentEvil:
				return True
			if eBuilding == iAltar1:
				if (pPlayer.countNumBuildings(iAltar2) > 0 or pPlayer.countNumBuildings(iAltar3) > 0 or pPlayer.countNumBuildings(iAltar4) > 0 or pPlayer.countNumBuildings(iAltar5) > 0 or pPlayer.countNumBuildings(iAltar6) > 0 or pPlayer.countNumBuildings(iAltar7) > 0):
					return True
			elif eBuilding == iAltar2:
				if (pPlayer.countNumBuildings(iAltar3) > 0 or pPlayer.countNumBuildings(iAltar4) > 0 or pPlayer.countNumBuildings(iAltar5) > 0 or pPlayer.countNumBuildings(iAltar6) > 0 or pPlayer.countNumBuildings(iAltar7) > 0):
					return True
			elif eBuilding == iAltar3:
				if (pPlayer.countNumBuildings(iAltar4) > 0 or pPlayer.countNumBuildings(iAltar5) > 0 or pPlayer.countNumBuildings(iAltar6) > 0 or pPlayer.countNumBuildings(iAltar7) > 0):
					return True
			elif eBuilding == iAltar4:
				if (pPlayer.countNumBuildings(iAltar5) > 0 or pPlayer.countNumBuildings(iAltar6) > 0 or pPlayer.countNumBuildings(iAltar7) > 0):
					return True
			elif eBuilding == iAltar5:
				if (pPlayer.countNumBuildings(iAltar6) > 0 or pPlayer.countNumBuildings(iAltar7) > 0):
					return True
			elif eBuilding == iAltar6:
				if pPlayer.countNumBuildings(iAltar7) > 0:
					return True
		"""

		if not pPlayer.isHuman():
			if eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_PROPHECY_OF_RAGNAROK'):
				if pPlayer.getAlignment() != en.eAlignmentEvil:
					return True

# Kaijin >>>
# Wonder to be limited by the alignment.
		if eBuilding == gc.getInfoTypeForString('BUILDING_SHRINE_OF_JUNIL'):
			if pPlayer.getAlignment() != en.eAlignmentGood:
				return True

		if eBuilding == gc.getInfoTypeForString('BUILDING_WINTER_PALACE'):
			if pPlayer.getAlignment() != en.eAlignmentGood:
				return True

# 勝利条件：終末への導き関係
		leMagicCircle = [	gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_CURSE'),
							gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_SADNESS'),
							gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_DEVASTATION'),
							gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_CALAMITY'),
							gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_RAGE'),
							gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_BLACK_DEATH'),
							gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_HOLLOW'),
							gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_END')	]
		iNumMagicCircle = len(leMagicCircle)
		for i in range(iNumMagicCircle):
			if eBuilding == leMagicCircle[i]:
				if pPlayer.getAlignment() != en.eAlignmentEvil:
					return True
				if not pPlayer.isHuman():
					if not pPlayer.getGuildPlusCounter(2) in (0, 6):
						return True
				for j in range(i+1, iNumMagicCircle):
					if pPlayer.countNumBuildings(leMagicCircle[j]) > 0:
						return True
				break
		"""
		iMagicCircle1 = gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_CURSE')
		iMagicCircle2 = gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_SADNESS')
		iMagicCircle3 = gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_DEVASTATION')
		iMagicCircle4 = gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_CALAMITY')
		iMagicCircle5 = gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_RAGE')
		iMagicCircle6 = gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_BLACK_DEATH')
		iMagicCircle7 = gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_HOLLOW')
		iMagicCircle8 = gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_END')
		if eBuilding in (iMagicCircle1, iMagicCircle2, iMagicCircle3, iMagicCircle4, iMagicCircle5, iMagicCircle6, iMagicCircle7, iMagicCircle8):
			if pPlayer.getAlignment() != en.eAlignmentEvil:
				return True
			if not pPlayer.isHuman():
				if not pPlayer.getGuildPlusCounter(2) in (0, 6):
					return True
			if eBuilding == iMagicCircle1:
				if (pPlayer.countNumBuildings(iMagicCircle2) > 0 or pPlayer.countNumBuildings(iMagicCircle3) > 0 or pPlayer.countNumBuildings(iMagicCircle4) > 0 or pPlayer.countNumBuildings(iMagicCircle5) > 0 or pPlayer.countNumBuildings(iMagicCircle6) > 0 or pPlayer.countNumBuildings(iMagicCircle7) > 0 or pPlayer.countNumBuildings(iMagicCircle8) > 0):
					return True
			elif eBuilding == iMagicCircle2:
				if (pPlayer.countNumBuildings(iMagicCircle3) > 0 or pPlayer.countNumBuildings(iMagicCircle4) > 0 or pPlayer.countNumBuildings(iMagicCircle5) > 0 or pPlayer.countNumBuildings(iMagicCircle6) > 0 or pPlayer.countNumBuildings(iMagicCircle7) > 0 or pPlayer.countNumBuildings(iMagicCircle8) > 0):
					return True
			elif eBuilding == iMagicCircle3:
				if (pPlayer.countNumBuildings(iMagicCircle4) > 0 or pPlayer.countNumBuildings(iMagicCircle5) > 0 or pPlayer.countNumBuildings(iMagicCircle6) > 0 or pPlayer.countNumBuildings(iMagicCircle7) > 0 or pPlayer.countNumBuildings(iMagicCircle8) > 0):
					return True
			elif eBuilding == iMagicCircle4:
				if (pPlayer.countNumBuildings(iMagicCircle5) > 0 or pPlayer.countNumBuildings(iMagicCircle6) > 0 or pPlayer.countNumBuildings(iMagicCircle7) > 0 or pPlayer.countNumBuildings(iMagicCircle8) > 0):
					return True
			elif eBuilding == iMagicCircle5:
				if (pPlayer.countNumBuildings(iMagicCircle6) > 0 or pPlayer.countNumBuildings(iMagicCircle7) > 0 or pPlayer.countNumBuildings(iMagicCircle8) > 0):
					return True
			elif eBuilding == iMagicCircle6:
				if (pPlayer.countNumBuildings(iMagicCircle7) > 0 or pPlayer.countNumBuildings(iMagicCircle8) > 0):
					return True
			elif eBuilding == iMagicCircle7:
				if pPlayer.countNumBuildings(iMagicCircle8) > 0:
					return True
		"""
		if not pPlayer.isHuman():
			if eBuildingClass in (	gc.getInfoTypeForString('BUILDINGCLASS_ALCHEMY_LAB'),
									gc.getInfoTypeForString('BUILDINGCLASS_FORGE'),
									gc.getInfoTypeForString('BUILDINGCLASS_BASILICA'),
									gc.getInfoTypeForString('BUILDINGCLASS_GROVE'),
									gc.getInfoTypeForString('BUILDINGCLASS_INFIRMARY'),
									gc.getInfoTypeForString('BUILDINGCLASS_INN'),
									gc.getInfoTypeForString('BUILDINGCLASS_MONEYCHANGER'),
									gc.getInfoTypeForString('BUILDINGCLASS_OBSIDIAN_GATE'),
									gc.getInfoTypeForString('BUILDINGCLASS_SHIPYARD'),
									gc.getInfoTypeForString('BUILDINGCLASS_TAVERN'),
									gc.getInfoTypeForString('BUILDINGCLASS_TAX_OFFICE'),
									gc.getInfoTypeForString('BUILDINGCLASS_THEATRE'),
									gc.getInfoTypeForString('BUILDINGCLASS_ASTROLOGICAL_OBSERVATORY'),
									gc.getInfoTypeForString('BUILDINGCLASS_CUSTOM_HOUSE')	):
				if pCity.getPopulation() < 6:
					return True
			elif eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_PALACE'):
# ent >>>
				pCapital = pPlayer.getCapitalCity()
				if pCapital is not None:
					iValue = 0
					eCivicGovernment = pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_GOVERNMENT'))
					if pCity.getPopulation() - pCapital.getPopulation() > 3:
						iValue += 1
					if pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) < pCapital.findYieldRateRank(YieldTypes.YIELD_PRODUCTION):
						iValue += 1
						if eCivicGovernment == gc.getInfoTypeForString('CIVIC_GOD_KING'):
							iValue += 1
					if pCity.findYieldRateRank(YieldTypes.YIELD_COMMERCE) < pCapital.findYieldRateRank(YieldTypes.YIELD_COMMERCE):
						iValue += 1
						if eCivicGovernment == gc.getInfoTypeForString('CIVIC_ARISTOCRACY'):
							iValue += 1
					if pCity.findCommerceRateRank(CommerceTypes.COMMERCE_RESEARCH) < pCapital.findCommerceRateRank(CommerceTypes.COMMERCE_RESEARCH):
						iValue += 1
					if pCity.findCommerceRateRank(CommerceTypes.COMMERCE_GOLD) < pCapital.findCommerceRateRank(CommerceTypes.COMMERCE_GOLD):
						iValue += 1
						if eCivicGovernment == gc.getInfoTypeForString('CIVIC_GOD_KING'):
							iValue += 1
					if pCity.plot().getArea() != pCapital.plot().getArea():
						iValue += 1
						if pCity.area().getCitiesPerPlayer(pCity.getOwner()) > pCapital.area().getCitiesPerPlayer(pCity.getOwner()):
							iValue += 1
					if pPlayer.getCivilizationType() in (en.eCivilizationMercurians, en.eCivilizationInfernal, en.eCivilizationXoth):
						iValue -= 1
					if iValue < 4:
						return True
# ent <<<
# Kaijin <<<
# Kaijin >>>	patch29 expansion - Start -
		if eBuildingClass == gc.getInfoTypeForString('BUILDINGCLASS_DRUID_RUNES'):
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_MACHINISTS_SHOP')) or pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_ENERGY_PLANT')):
				return True
		if eBuildingClass in (	gc.getInfoTypeForString('BUILDINGCLASS_MACHINISTS_SHOP'),
								gc.getInfoTypeForString('BUILDINGCLASS_ENERGY_PLANT')	):
			if pCity.isHasActiveBuilding(gc.getInfoTypeForString('BUILDING_DRUID_RUNES')):
				return True
# Kaijin <<<	patch29 expansion - End -
		return False

	def canCreate(self,argsList):
		pCity = argsList[0]
		eProject = argsList[1]
		bContinue = argsList[2]
		bTestVisible = argsList[3]
		return False

	def cannotCreate(self,argsList):
		pCity = argsList[0]
		eProject = argsList[1]
		bContinue = argsList[2]
		bTestVisible = argsList[3]
		pPlayer = gc.getPlayer(pCity.getOwner())

		iGameProgress = pPlayer.getGameProgressPercent()

		if eProject == gc.getInfoTypeForString('PROJECT_PURGE_THE_UNFAITHFUL'):
			if not pPlayer.isHuman():
				return True
			if pPlayer.getStateReligion() == -1:
				return True

		elif eProject == gc.getInfoTypeForString('PROJECT_BIRTHRIGHT_REGAINED'):
			if not pPlayer.isFeatAccomplished(FeatTypes.FEAT_GLOBAL_SPELL):
				return True

		elif eProject == gc.getInfoTypeForString('PROJECT_THE_DEEPENING'):
			leUniqueImprovmemnts = [eImprovement for eImprovement in xrange(gc.getNumImprovementInfos()) if gc.getImprovementInfo(eImprovement).isUnique() and pPlayer.getImprovementCount(eImprovement) > 0]
			if len(leUniqueImprovmemnts) < 2 and gc.getInfoTypeForString('IMPROVEMENT_LETUM_FRIGUS') not in leUniqueImprovmemnts:
				return True

		elif eProject == gc.getInfoTypeForString('PROJECT_STIR_FROM_SLUMBER'):
			if pPlayer.getPlayersKilled() == 0:
				return True
# ent >>>
		elif eProject == gc.getInfoTypeForString('PROJECT_THE_DRAW'):
			if not pPlayer.isHuman():
				if not pPlayer.isHasTech(gc.getInfoTypeForString('TECH_OMNISCIENCE')):
					return True
# ent <<<
		elif eProject == gc.getInfoTypeForString('PROJECT_GENESIS'):
			if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ILLIANS'):
				return True
# Kaijin >>>
			if not pPlayer.isHuman():
				if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_NIVAL'):
					return True
# Kaijin <<<

# Kaijin >>>
		elif eProject == gc.getInfoTypeForString('PROJECT_GLORY_EVERLASTING'):
			if not pPlayer.isHuman():
				if pPlayer.getCivilizationType() in (	gc.getInfoTypeForString('CIVILIZATION_SHEAIM'),
														gc.getInfoTypeForString('CIVILIZATION_INFERNAL'),
														gc.getInfoTypeForString('CIVILIZATION_DROAUM'),
														gc.getInfoTypeForString('CIVILIZATION_DARK'),
														gc.getInfoTypeForString('CIVILIZATION_SCIONS'),
														gc.getInfoTypeForString('CIVILIZATION_RARNA'),
														gc.getInfoTypeForString('CIVILIZATION_XOTH'),
														gc.getInfoTypeForString('CIVILIZATION_ARISTRAKH')		):
					return True
				if pPlayer.getStateReligion() in (en.eReligionAshenVeil, en.eReligionOctopusOverlords):
					return True
# Kaijin <<<

# Kaijin - May Sickness
		elif eProject == gc.getInfoTypeForString('PROJECT_MAY_SICKNESS'):
			if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_CURSE')) < 1:
				return True
			if not pPlayer.isHuman():
				if not CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_LED_TO_THE_END')) or CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_GLOBAL_COUNTER):
					return True
				if not pPlayer.getGuildPlusCounter(2) in (0, 6):
					return True
# Kaijin - Black Rain
		elif eProject == gc.getInfoTypeForString('PROJECT_BLACK_RAIN'):
			if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_SADNESS')) < 1:
				return True
			if not pPlayer.isHuman():
				if not CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_LED_TO_THE_END')) or CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_GLOBAL_COUNTER):
					return True
				if not pPlayer.getGuildPlusCounter(2) in (0, 6):
					return True
# Kaijin - Return Soul
		elif eProject == gc.getInfoTypeForString('PROJECT_RETURN_SOUL'):
			if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_DEVASTATION')) < 1:
				return True
			if not pPlayer.isHuman():
				if not CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_LED_TO_THE_END')) or CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_GLOBAL_COUNTER):
					return True
				if not pPlayer.getGuildPlusCounter(2) in (0, 6):
					return True
# Kaijin - Disaster
		elif eProject == gc.getInfoTypeForString('PROJECT_DISASTER'):
			if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_CALAMITY')) < 1:
				return True
			if not pPlayer.isHuman():
				if not CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_LED_TO_THE_END')) or CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_GLOBAL_COUNTER):
					return True
				if not pPlayer.getGuildPlusCounter(2) in (0, 6):
					return True
# Kaijin - Festival of the Berserkers
		elif eProject == gc.getInfoTypeForString('PROJECT_FESTIVAL_OF_THE_BERSERKERS'):
			if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_RAGE')) < 1:
				return True
			if not pPlayer.isHuman():
				if not CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_LED_TO_THE_END')) or CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_GLOBAL_COUNTER):
					return True
				if not pPlayer.getGuildPlusCounter(2) in (0, 6):
					return True
# Kaijin - Stigma the Brack
		elif eProject == gc.getInfoTypeForString('PROJECT_STIGMA_THE_BLACK'):
			if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_BLACK_DEATH')) < 1:
				return True
			if not pPlayer.isHuman():
				if not CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_LED_TO_THE_END')) or CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_GLOBAL_COUNTER):
					return True
				if not pPlayer.getGuildPlusCounter(2) in (0, 6):
					return True
# Kaijin - Dark Gate
		elif eProject == gc.getInfoTypeForString('PROJECT_DARK_GATE'):
			if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_HOLLOW')) < 1:
				return True
			if not pPlayer.isHuman():
				if not CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_LED_TO_THE_END')) or CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_GLOBAL_COUNTER):
					return True
				if not pPlayer.getGuildPlusCounter(2) in (0, 6):
					return True
# Kaijin - Led to the End
		elif eProject == gc.getInfoTypeForString('PROJECT_LED_TO_THE_END'):
			if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_END')) < 1:
				return True
			if not pPlayer.isHuman():
				if not CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_LED_TO_THE_END')) or CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_GLOBAL_COUNTER):
					return True
				if not pPlayer.getGuildPlusCounter(2) in (0, 6):
					return True

# Kaijin - Fire Inheritance
		elif eProject == gc.getInfoTypeForString('PROJECT_FIRE_INHERITANCE'):
			if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and pPlayer.isHuman():
				iNumNeeded = 1
			else:
				iNumNeeded = 6
			if pPlayer.countNumBuildings(gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_INHERITANCE')) < iNumNeeded:
				return True

# Kaijin - Princess of Darkness
		elif eProject == gc.getInfoTypeForString('PROJECT_PRINCESS_OF_DARKNESS'):
			if gc.getGame().isOption(GameOptionTypes.GAMEOPTION_ONE_CITY_CHALLENGE) and pPlayer.isHuman():
				iNumNeeded = 1
			else:
				iNumNeeded = 6
			if pPlayer.countNumBuildings(gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_IMPORTANCE')) < iNumNeeded:
				return True

# Kaijin - Death pact
		elif eProject == gc.getInfoTypeForString('PROJECT_DEATH_PACT_1'):
			if pCity.getPopulation() >= 5:
				return True
			if not pPlayer.isHuman():
				if not pCity.happyLevel() - pCity.unhappyLevel(0) > 0:
					return True

		elif eProject == gc.getInfoTypeForString('PROJECT_DEATH_PACT_2'):
			if pCity.getPopulation() >= 10 or pCity.getPopulation() < 5:
				return True
			if not pPlayer.isHuman():
				if not pCity.happyLevel() - pCity.unhappyLevel(0) > 0:
					return True

		elif eProject == gc.getInfoTypeForString('PROJECT_DEATH_PACT_3'):
			if pCity.getPopulation() >= 15 or pCity.getPopulation() < 10:
				return True
			if not pPlayer.isHuman():
				if not pCity.happyLevel() - pCity.unhappyLevel(0) > 0:
					return True

		elif eProject == gc.getInfoTypeForString('PROJECT_DEATH_PACT_4'):
			if pCity.getPopulation() >= 20 or pCity.getPopulation() < 15:
				return True
			if not pPlayer.isHuman():
				if not pCity.happyLevel() - pCity.unhappyLevel(0) > 0:
					return True

		elif eProject == gc.getInfoTypeForString('PROJECT_DEATH_PACT_5'):
			if pCity.getPopulation() < 20:
				return True
			if cf.getFertileTerrain(pCity):
				return True
			if not pPlayer.isHuman():
				if not pCity.happyLevel() - pCity.unhappyLevel(0) > 0:
					return True

# Kaijin - Death ritual
		elif eProject == gc.getInfoTypeForString('PROJECT_DEATH_RITUAL'):
			if not pPlayer.isHuman():
				if pPlayer.getNumCities() < 4:
					return True

# Kaijin - AI
		if not pPlayer.isHuman():
			## Droaum - Secret of evolution
			if eProject == gc.getInfoTypeForString('PROJECT_SECRET_OF_EVOLUTION_DROAUM'):
				if not pPlayer.isSlaveTrade():
					if not (CyGame().getGlobalCounter() > 70 and not pPlayer.isEventOccured(gc.getInfoTypeForString('EVENT_ARMAGEDDON_APOCALYPSE'))):
						if not pPlayer.getAveragePopulation() > 20:
							return True

			## Statue of Laxury
			elif eProject in (#gc.getInfoTypeForString('PROJECT_FLYING_TO_THE_SKY'), 
							gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_COCKPIT'), 
							gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_LIFE_SUPPORT'), 
							gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_STASIS_CHAMBER'), 
							gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_DOCKING_BAY'), 
							gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_ENGINE'), 
							gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_CASING'), 
							gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_THRUSTERS'), 
							gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_CORE')			):

				if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_MERCURIANS'):
					return True
				if not pPlayer.getGuildPlusCounter(2) in (0, 7):
					# except for stalemate in other victories
					if not (iGameProgress > 90 or gc.getGame().getGameTurn >= 250):
						return True
# ent >>>
			elif eProject == gc.getInfoTypeForString('PROJECT_ETHER_TO_COLLAPSE'):
				if pPlayer.getGuildPlusCounter(2) != 1:
					return True
			elif eProject == gc.getInfoTypeForString('PROJECT_ELEGY_OF_THE_SHEAIM'):
				if cf.AI_hasRoomForFound(pCity.getOwner()):
					return True
			elif eProject == gc.getInfoTypeForString('PROJECT_HALLOWING_OF_THE_ELOHIM'):
				if cf.AI_hasRoomForFound(pCity.getOwner()):
					return True
			elif eProject == gc.getInfoTypeForString('PROJECT_SAMHAIN'):
				if cf.AI_hasRoomForFound(pCity.getOwner()):
					return True
			elif eProject == gc.getInfoTypeForString('PROJECT_SPREAD_CORRUPTION'):
				if cf.AI_hasRoomForFound(pCity.getOwner()):
					return True
# ent <<<
# Kaijin <<<

		return False

	def canMaintain(self,argsList):
		pCity = argsList[0]
		eProcess = argsList[1]
		bContinue = argsList[2]
		return False

	def cannotMaintain(self,argsList):
		pCity = argsList[0]
		eProcess = argsList[1]
		bContinue = argsList[2]
		return False

	def AI_chooseTech(self,argsList):
		ePlayer = argsList[0]
		bFree = argsList[1]
# Kaijin OAC - AI choose Tech Start
##--------	Better AI: Added by Denev 2011/04/29

# ent - Except for Free Technology >>>
		if bFree:
			return TechTypes.NO_TECH
# ent <<<
		pPlayer = gc.getPlayer(ePlayer)
		pTeam = gc.getTeam(pPlayer.getTeam())

		iNumCities = pPlayer.getNumCities()
		iGameProgress = pPlayer.getGameProgressPercent()

# ent >>>
		## Choose Early Military Tech
		if not pPlayer.isHasTech(gc.getInfoTypeForString('TECH_ARCHERY')):
			pBarbarianPlayer = gc.getPlayer(gc.getBARBARIAN_PLAYER())
			eArchery = gc.getInfoTypeForString('TECH_ARCHERY')
			eBronzeWorking = gc.getInfoTypeForString('TECH_BRONZE_WORKING')
			if (pBarbarianPlayer.isHasTech(eArchery) or pBarbarianPlayer.isHasTech(eBronzeWorking) or
				iNumCities >= 3 or iGameProgress > 8 or pPlayer.getCurrentEra() > gc.getInfoTypeForString('ERA_ANCIENT')):

				leMilitaryTechs = []
				eCiv = pPlayer.getCivilizationType()
				iThreshold = 15
				if pBarbarianPlayer.isHasTech(eArchery):
					iThreshold += 5
				if pBarbarianPlayer.isHasTech(eBronzeWorking):
					iThreshold += 5
				iThreshold = cyFlatValue(iThreshold, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)

				def isReachableTech(eTech):
					if pPlayer.isHasTech(eTech):
						return True
					if pPlayer.canResearch(eTech, False):
						if pPlayer.getResearchTurnsLeft(eTech, False) < iThreshold:
							return True
					return False

				# TECH_ARCHERY
				if isReachableTech(eArchery):
					leMilitaryTechs.append(eArchery)
					if eCiv in (gc.getInfoTypeForString('CIVILIZATION_LJOSALFAR'), 
								gc.getInfoTypeForString('CIVILIZATION_ILLIANS'), 
								gc.getInfoTypeForString('CIVILIZATION_MAZATL'), 
								gc.getInfoTypeForString('CIVILIZATION_CUALLI'),
								gc.getInfoTypeForString('CIVILIZATION_BALDRALFAR')):
						leMilitaryTechs.append(eArchery)
					if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_DEFENDER')):
						leMilitaryTechs.append(eArchery)
					if pPlayer.countOwnedBonuses(gc.getInfoTypeForString('BONUS_DUSKWOOD')) > 0:
						leMilitaryTechs.append(eArchery)
				# TECH_BRONZE_WORKING
				if isReachableTech(eBronzeWorking):
					leMilitaryTechs.append(eBronzeWorking)
					if eCiv in (gc.getInfoTypeForString('CIVILIZATION_LUCHUIRP'), 
								gc.getInfoTypeForString('CIVILIZATION_NIRAIKANAI'), 
								gc.getInfoTypeForString('CIVILIZATION_NIVAL'), 
								gc.getInfoTypeForString('CIVILIZATION_XOTH'), 
								gc.getInfoTypeForString('CIVILIZATION_MEGISUS')):
						leMilitaryTechs.remove(eBronzeWorking)
					elif eCiv == gc.getInfoTypeForString('CIVILIZATION_LINEAGE') and pPlayer.countOwnedBonuses(gc.getInfoTypeForString('BONUS_COPPER')) == 0:
						leMilitaryTechs.remove(eBronzeWorking)
					else:
						if eCiv in (gc.getInfoTypeForString('CIVILIZATION_KHAZAD'), 
									gc.getInfoTypeForString('CIVILIZATION_DOVIELLO'), 
									gc.getInfoTypeForString('CIVILIZATION_CLAN_OF_EMBERS'), 
									gc.getInfoTypeForString('CIVILIZATION_SHEAIM'), 
									gc.getInfoTypeForString('CIVILIZATION_DARK'), 
									gc.getInfoTypeForString('CIVILIZATION_ECHIGO'), 
									gc.getInfoTypeForString('CIVILIZATION_LINEAGE'), 
									gc.getInfoTypeForString('CIVILIZATION_ALTAIR'),
									gc.getInfoTypeForString('CIVILIZATION_MECHANOS')):
							leMilitaryTechs.append(eBronzeWorking)
						if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_MILITARISTIC')):
							leMilitaryTechs.append(eBronzeWorking)
						for i in xrange(pPlayer.countOwnedBonuses(gc.getInfoTypeForString('BONUS_COPPER'))):
							leMilitaryTechs.append(eBronzeWorking)
				# OTHERS
				if eCiv in (	gc.getInfoTypeForString('CIVILIZATION_KURIOTATES'), 
								gc.getInfoTypeForString('CIVILIZATION_HIPPUS')):
					if isReachableTech(gc.getInfoTypeForString('TECH_HORSEBACK_RIDING')):
						leMilitaryTechs.append(gc.getInfoTypeForString('TECH_HORSEBACK_RIDING'))
				elif eCiv in (	gc.getInfoTypeForString('CIVILIZATION_SHEAIM'), 
								gc.getInfoTypeForString('CIVILIZATION_DARK'), 
								gc.getInfoTypeForString('CIVILIZATION_DESPIEL'), 
								gc.getInfoTypeForString('CIVILIZATION_SCIONS')):
					if isReachableTech(gc.getInfoTypeForString('TECH_KNOWLEDGE_OF_THE_ETHER')):
						leMilitaryTechs.append(gc.getInfoTypeForString('TECH_KNOWLEDGE_OF_THE_ETHER'))
						if CyGame().countKnownTechNumTeams(gc.getInfoTypeForString('TECH_KNOWLEDGE_OF_THE_ETHER')) == 0:
							leMilitaryTechs.append(gc.getInfoTypeForString('TECH_KNOWLEDGE_OF_THE_ETHER'))
				elif eCiv ==	gc.getInfoTypeForString('CIVILIZATION_NIRAIKANAI'):
					if isReachableTech(gc.getInfoTypeForString('TECH_TRACKING')):
						leMilitaryTechs.append(gc.getInfoTypeForString('TECH_TRACKING'))
				elif eCiv == 	gc.getInfoTypeForString('CIVILIZATION_LUCHUIRP'):
					if isReachableTech(gc.getInfoTypeForString('TECH_MASONRY')):
						leMilitaryTechs.append(gc.getInfoTypeForString('TECH_MASONRY'))

				if len(leMilitaryTechs) > 0:
					for eTech in leMilitaryTechs:
						if pPlayer.isHasTech(eTech):
							break
					else:
						return leMilitaryTechs[CyGame().getSorenRandNum(len(leMilitaryTechs), "Choose Early Military Tech")]
				else:
					# Prereq TECH_ARCHERY
					if not pPlayer.isHasTech(gc.getInfoTypeForString('TECH_CRAFTING')):
						if pPlayer.canResearch(gc.getInfoTypeForString('TECH_CRAFTING'), False):
							return gc.getInfoTypeForString('TECH_CRAFTING')
					if not pPlayer.isHasTech(gc.getInfoTypeForString('TECH_HUNTING')):
						if pPlayer.canResearch(gc.getInfoTypeForString('TECH_HUNTING'), False):
							return gc.getInfoTypeForString('TECH_HUNTING')

		"""
		if iNumCities >= 3 or pPlayer.countTotalHasReligion() > 0 or iGameProgress > 8:
			if (	not pPlayer.isHasTech(gc.getInfoTypeForString('TECH_BRONZE_WORKING')) 
					and not pPlayer.isHasTech(gc.getInfoTypeForString('TECH_ARCHERY')) 
					and not pPlayer.isHasTech(gc.getInfoTypeForString('TECH_TRACKING')) 
					and not pPlayer.isHasTech(gc.getInfoTypeForString('TECH_HORSEBACK_RIDING')) 
					and not pPlayer.isHasTech(gc.getInfoTypeForString('TECH_KNOWLEDGE_OF_THE_ETHER'))	):
				if pPlayer.getCivilizationType() in (	gc.getInfoTypeForString('CIVILIZATION_BANNOR'), 
														gc.getInfoTypeForString('CIVILIZATION_KHAZAD'), 
														gc.getInfoTypeForString('CIVILIZATION_DOVIELLO'), 
														gc.getInfoTypeForString('CIVILIZATION_CLAN_OF_EMBERS'), 
														gc.getInfoTypeForString('CIVILIZATION_SHEAIM'), 
														gc.getInfoTypeForString('CIVILIZATION_ECHIGO'), 
														gc.getInfoTypeForString('CIVILIZATION_ALTAIR'), 
														gc.getInfoTypeForString('CIVILIZATION_CUALLI')		):
					if pPlayer.canResearch(gc.getInfoTypeForString('TECH_BRONZE_WORKING'), False):
						return gc.getInfoTypeForString('TECH_BRONZE_WORKING')

				elif pPlayer.getCivilizationType() in (	gc.getInfoTypeForString('CIVILIZATION_LJOSALFAR'), 
														gc.getInfoTypeForString('CIVILIZATION_LINEAGE'), 
														gc.getInfoTypeForString('CIVILIZATION_MAZATL'), 
														gc.getInfoTypeForString('CIVILIZATION_BALDRALFAR')		):
					if pPlayer.canResearch(gc.getInfoTypeForString('TECH_ARCHERY'), False):
						return gc.getInfoTypeForString('TECH_ARCHERY')

				elif pPlayer.getCivilizationType() in (	gc.getInfoTypeForString('CIVILIZATION_SIDAR'), 
														gc.getInfoTypeForString('CIVILIZATION_SVARTALFAR'), 
														gc.getInfoTypeForString('CIVILIZATION_RARNA')		):
					if pPlayer.canResearch(gc.getInfoTypeForString('TECH_TRACKING'), False):
						return gc.getInfoTypeForString('TECH_TRACKING')

				elif pPlayer.getCivilizationType() in (	gc.getInfoTypeForString('CIVILIZATION_KURIOTATES'), 
														gc.getInfoTypeForString('CIVILIZATION_HIPPUS'), 
														gc.getInfoTypeForString('CIVILIZATION_NIRAIKANAI')		):
					if pPlayer.canResearch(gc.getInfoTypeForString('TECH_HORSEBACK_RIDING'), False):
						return gc.getInfoTypeForString('TECH_HORSEBACK_RIDING')

				elif pPlayer.getCivilizationType() in (	gc.getInfoTypeForString('CIVILIZATION_DROAUM'), 
														gc.getInfoTypeForString('CIVILIZATION_DESPIEL'), 
														gc.getInfoTypeForString('CIVILIZATION_SCIONS'), 
														gc.getInfoTypeForString('CIVILIZATION_NIVAL')		):
					if pPlayer.canResearch(gc.getInfoTypeForString('TECH_KNOWLEDGE_OF_THE_ETHER'), False):
						return gc.getInfoTypeForString('TECH_KNOWLEDGE_OF_THE_ETHER')

				else:
					if CyGame().getSorenRandNum(2, "Choose Early Military Tech") == 0:
						return gc.getInfoTypeForString('TECH_BRONZE_WORKING')
					else:
						return gc.getInfoTypeForString('TECH_ARCHERY')

		if iNumCities >= 4 or iGameProgress > 15:
			if pPlayer.getCivilizationType() in (	gc.getInfoTypeForString('CIVILIZATION_MECHANOS'), 
													gc.getInfoTypeForString('CIVILIZATION_NOUGBII')		):
				if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_KNOWLEDGE_OF_THE_ETHER')):
					if not pPlayer.isHasTech(gc.getInfoTypeForString('TECH_STEAM_POWER')):
						if pPlayer.canResearch(gc.getInfoTypeForString('TECH_STEAM_POWER'), False):
							return gc.getInfoTypeForString('TECH_STEAM_POWER')

		if iNumCities >= 4 or iGameProgress > 20:
			if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_ARISTRAKH'):
				if not pPlayer.isHasTech(gc.getInfoTypeForString('TECH_NECROMANCY')):
					if pPlayer.canResearch(gc.getInfoTypeForString('TECH_NECROMANCY'), False):
						return gc.getInfoTypeForString('TECH_NECROMANCY')

		if iNumCities >= 5 or iGameProgress > 50:
			if not pPlayer.isHasTech(gc.getInfoTypeForString('TECH_MILITARY_STRATEGY')):
				if pPlayer.canResearch(gc.getInfoTypeForString('TECH_MILITARY_STRATEGY'), False):
					return gc.getInfoTypeForString('TECH_MILITARY_STRATEGY')
		"""
# ent <<<

		if iNumCities >= 5 or iGameProgress > 50:
			if pPlayer.getStateReligion() == gc.getInfoTypeForString('RELIGION_THE_ORDER'):
				if pPlayer.isHasTech(gc.getInfoTypeForString('TECH_PRIESTHOOD')):
					if not pPlayer.isHasTech(gc.getInfoTypeForString('TECH_RELIGIOUS_LAW')):
						if pPlayer.canResearch(gc.getInfoTypeForString('TECH_RELIGIOUS_LAW'), False):
							return gc.getInfoTypeForString('TECH_RELIGIOUS_LAW')

		if pPlayer.AI_getTowerVictoryStage() > 0:
			if pPlayer.canResearch(gc.getInfoTypeForString('TECH_SORCERY'), False):
				return gc.getInfoTypeForString('TECH_SORCERY')
			if iGameProgress > 45:
				if pPlayer.canResearch(gc.getInfoTypeForString('TECH_STRENGTH_OF_WILL'), False):
					return gc.getInfoTypeForString('TECH_STRENGTH_OF_WILL')
# ent >>>
		## World heritage
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_CRAZY_BY_WORLDHERITAGE')) and CyGame().getSorenRandNum(100, "World heritage") < 70:
			infoCiv = gc.getCivilizationInfo(pPlayer.getCivilizationType())
			iBestTurn = cyFlatValue(6, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
			eBestTech = TechTypes.NO_TECH
			for eBuildingClass in xrange(gc.getNumBuildingClassInfos()):
				if isWorldWonderClass(eBuildingClass) and not CyGame().isBuildingClassMaxedOut(eBuildingClass, 0):
					eBuilding = infoCiv.getCivilizationBuildings(eBuildingClass)
					if eBuilding != BuildingTypes.NO_BUILDING:
						eTech = gc.getBuildingInfo(eBuilding).getPrereqAndTech()
						if eTech != TechTypes.NO_TECH:
							if not pPlayer.isHasTech(eTech) and pPlayer.canResearch(eTech, False):
								if CyGame().countKnownTechNumTeams(eTech) > 0:
									iTurn = pPlayer.getResearchTurnsLeft(eTech, False)
									if iTurn < iBestTurn:
										iBestTurn = iTurn
										eBestTech = eTech
			if eBestTech != TechTypes.NO_TECH:
				return eBestTech

		if iGameProgress > 30:
			infoLeader = gc.getLeaderHeadInfo(pPlayer.getLeaderType())
			## Victory: Statue of Luxury
			if pPlayer.getGuildPlusCounter(2) == 7:
				leImportantTechs = [gc.getInfoTypeForString('TECH_MERCANTILISM'), 
									gc.getInfoTypeForString('TECH_GUILDS'), 
									gc.getInfoTypeForString('TECH_BLASTING_POWDER'), 
									gc.getInfoTypeForString('TECH_MACHINERY'), 
									gc.getInfoTypeForString('TECH_LUXURY'), 
									gc.getInfoTypeForString('TECH_STEAM_POWER'), 
									gc.getInfoTypeForString('TECH_ASTRONOMY')		]
				iBestTurn = cyFlatValue(10, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
				eBestTech = TechTypes.NO_TECH
				for eTech in leImportantTechs:
					if not pPlayer.isHasTech(eTech) and pPlayer.canResearch(eTech, False):
						iTurn = pPlayer.getResearchTurnsLeft(eTech, False)
						if iTurn < iBestTurn:
							iBestTurn = iTurn
							eBestTech = eTech
				if eBestTech != TechTypes.NO_TECH:
					return eBestTech

			## Victory: Religious
			elif pPlayer.getGuildPlusCounter(2) == 3:
				# Select victorious religion.
				eReligion = ReligionTypes.NO_RELIGION
				iBestPercent = 0
				for eLoopReligion in xrange(gc.getNumReligionInfos()):
					if eLoopReligion == en.eReligionCultoftheDragon:
						continue
					if pTeam.hasHolyCity(eLoopReligion) and infoLeader.getReligionWeightModifier(eLoopReligion) >= 0:
						iReligionPercent = CyGame().calculateReligionPercent(eLoopReligion)
						if iReligionPercent > iBestPercent:
							iBestPercent = iReligionPercent
							eReligion = eLoopReligion
				if eReligion != ReligionTypes.NO_RELIGION:
					eTech = gc.getReligionInfo(eReligion).getTechPrereq()
					if eTech != TechTypes.NO_TECH:
						if not pPlayer.isHasTech(eTech) and pPlayer.canResearch(eTech, False):
							return eTech

			## Several Religions
			bIgnoreFounded = False
			if pPlayer.getGuildPlusCounter(2) == 2 or pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_SPIRITUAL')) or pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_IRON_WILL')):
				bIgnoreFounded = True
			if (bIgnoreFounded or pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_FAITH'))) and not pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_FANATIC')):
				iBestTurn = cyFlatValue(4, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
				eBestTech = TechTypes.NO_TECH
				for eReligion in xrange(gc.getNumReligionInfos()):
					eTech = gc.getReligionInfo(eReligion).getTechPrereq()
					if eTech != TechTypes.NO_TECH:
						if bIgnoreFounded or not CyGame().isReligionFounded(eReligion):
							if not pPlayer.isHasTech(eTech) and pPlayer.canResearch(eTech, False):
								if infoLeader.getReligionWeightModifier(eReligion) < 0:
									break
								iTurn = pPlayer.getResearchTurnsLeft(eTech, False)
								if iTurn < iBestTurn:
									iBestTurn = iTurn
									eBestTech = eTech
				if eBestTech != TechTypes.NO_TECH:
					return eBestTech
# ent <<<
##--------	Better AI: End Add
# Kaijin OAC - AI choose Tech End
		return TechTypes.NO_TECH

##--------	Better AI: Added by Denev 2011/04/29
	def AI_chooseAutomatedProduction(self,argsList):
		pCity = argsList[0]
		return False

	def AI_chooseBarbarianProduction(self,argsList):
		pCity = argsList[0]
		return False

	def AI_chooseBestMilitaryFactoryProduction(self,argsList):
		pCity = argsList[0]
		bDanger = argsList[1]
		bDefenseWar = argsList[2]
		bLandWar = argsList[3]
		bAssault = argsList[4]
		bWarPlan = argsList[5]
		iUnitCostPercentage = argsList[6]

		pPlayer = gc.getPlayer(pCity.getOwner())

		if pCity.AI_chooseHeroUnit():
			return True

		leMilitaryBuildingClasses = [	gc.getInfoTypeForString('BUILDINGCLASS_HEROIC_EPIC'),
										gc.getInfoTypeForString('BUILDINGCLASS_SHRINE_OF_THE_CHAMPION'),
										gc.getInfoTypeForString('BUILDINGCLASS_TRAINING_YARD'),
										gc.getInfoTypeForString('BUILDINGCLASS_ARCHERY_RANGE')	]
		for eMilitaryBuildingClass in leMilitaryBuildingClasses:
			if pCity.canConstructClass(eMilitaryBuildingClass):
				eMilitaryBuilding = gc.getCivilizationInfo(pCity.getCivilizationType()).getCivilizationBuildings(eMilitaryBuildingClass)
				if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eMilitaryBuilding, -1, False, False, False, False):
					CvUtil.pyPrint('Player %d started to construct %s' % (pCity.getOwner(), gc.getBuildingInfo(eMilitaryBuilding).getDescription()))
					return True

		if pCity.isHasBuildingClass(gc.getInfoTypeForString('BUILDINGCLASS_HEROIC_EPIC')):
			leMilitaryBuildingClasses = [	gc.getInfoTypeForString('BUILDINGCLASS_HUNTING_LODGE'),
											gc.getInfoTypeForString('BUILDINGCLASS_STABLE'),
											gc.getInfoTypeForString('BUILDINGCLASS_MAGE_GUILD'),
											gc.getInfoTypeForString('BUILDINGCLASS_SIEGE_WORKSHOP'),
											gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_EMPYREAN'),
											gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_LEAVES'),
											gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_KILMORPH'),
											gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_ORDER'),
											gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_OVERLORDS'),
											gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_VEIL'),
											gc.getInfoTypeForString('BUILDINGCLASS_COMMAND_POST'),
											gc.getInfoTypeForString('BUILDINGCLASS_SHIPYARD')	]

			for eMilitaryBuildingClass in leMilitaryBuildingClasses:
				if pCity.canConstructClass(eMilitaryBuildingClass):
					eMilitaryBuilding = gc.getCivilizationInfo(pCity.getCivilizationType()).getCivilizationBuildings(eMilitaryBuildingClass)
					if gc.getBuildingInfo(eMilitaryBuilding).getPrereqReligion() in (ReligionTypes.NO_RELIGION, pPlayer.getStateReligion()):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eMilitaryBuilding, -1, False, False, False, False):
							return True

			if bLandWar and not bDefenseWar:
				if CyGame().getSorenRandNum(3, "Choose Invader Unit") < 2:
					if pCity.AI_chooseInvaderUnit(False):
						return True
			elif bWarPlan:
				if CyGame().getSorenRandNum(3, "Choose Invader Unit") < 1:
					if pCity.AI_chooseInvaderUnit(False):
						return True

		if not pPlayer.AI_isFinancialTrouble():
			if bWarPlan or bLandWar and not bDefenseWar:
				if CyGame().getSorenRandNum(100, "Choose Invader Unit") < 40:
					if pCity.AI_chooseInvaderUnit(False):
						return True

		return False
##--------	Better AI: End Add

	def AI_chooseProduction(self,argsList):
		pCity = argsList[0]
##--------	Better AI: Added by Denev 2011/04/29
		ePlayer = pCity.getOwner()
		pPlayer = gc.getPlayer(ePlayer)
		pTeam = gc.getTeam(pPlayer.getTeam())

#Kaijin >>>

		eCiv = pCity.getCivilizationType()
		infoCiv = gc.getCivilizationInfo(pPlayer.getCivilizationType())
		eDefaultRace = gc.getCivilizationInfo(eCiv).getDefaultRace()
		infoLeader = gc.getLeaderHeadInfo(pPlayer.getLeaderType())
		pPlot = pCity.plot()
		iNumCities = pPlayer.getNumCities()
		iNumCoastalCities = pPlayer.countNumCoastalCities()
		iGameProgress = pPlayer.getGameProgressPercent()
		iThresholdTurn = cyFlatValue(5, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)

		if ePlayer == gc.getBARBARIAN_PLAYER():
			return False
		if pPlayer.AI_isFinancialTrouble():
			return False
#Kaijin <<<
# ent >>>
		if pCity.getCultureLevel() < 2: # under CULTURELEVEL_FLEDGLING
			if pCity.getBaseCommerceRateTimes100(CommerceTypes.COMMERCE_CULTURE) < 10 * gc.getCultureLevelInfo(gc.getInfoTypeForString('CULTURELEVEL_FLEDGLING')).getSpeedThreshold(CyGame().getGameSpeedType()):
				return False
		for iUnitIndex in xrange(pPlot.getNumUnits()):
			pUnit = pPlot.getUnit(iUnitIndex)
			if pUnit.getOwner() == ePlayer:
				if pUnit.isMilitaryHappiness():
					break
		else:
			return False
		iThreat = pCity.AI_cityThreat()
		if iThreat > 150:
			return False
		bCapital = pCity.isCapital()
		bBestMilitaryFactory = (pCity.getID() == pPlayer.AI_getBestMilitaryFactory().getID())
# ent <<<

# ent - Define Order Tool >>>
		def pushOrderConstructBuildingRandom(pCity, eBuilding, iMaxTurn):
			if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
				if pCity.getBuildingProductionTurnsLeft(eBuilding, 0) < cyFlatValue(iMaxTurn, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False):
					if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBuilding, -1, False, False, False, False):
						return True
			return False
# ent <<<

# ent - Production Modifiers >>>
		if cf.AI_getWarSuccessCapitulationRatio(ePlayer) > -20 and iThreat < 100:
			ltProductionAssists =	 [	#eBuildingClass,												iPop,	iMaxTurn
										(gc.getInfoTypeForString('BUILDINGCLASS_FORGE'),				8,		6),
										(gc.getInfoTypeForString('BUILDINGCLASS_ENERGY_PLANT'),			12,		4),
										(gc.getInfoTypeForString('BUILDINGCLASS_MACHINISTS_SHOP'),		12,		4),
										(gc.getInfoTypeForString('BUILDINGCLASS_ALCHEMY_LAB'),			10,		4),
										(gc.getInfoTypeForString('BUILDINGCLASS_LEUCETIOUS_ATELIER'),	15,		10),
										(gc.getInfoTypeForString('BUILDINGCLASS_GUILD_OF_HAMMERS'),		15,		12),
										(gc.getInfoTypeForString('BUILDINGCLASS_HERON_THRONE'),			15,		10)
										]
			for eBuildingClass, iPop, iMaxTurn in ltProductionAssists:
				eBuilding = infoCiv.getCivilizationBuildings(eBuildingClass)
				if eBuilding != BuildingTypes.NO_BUILDING and pCity.canConstruct(eBuilding, False, False, False) and pCity.getPopulation() >= iPop:
					if pushOrderConstructBuildingRandom(pCity, eBuilding, iMaxTurn):
						return True
# ent <<<

		if pTeam.getAtWarCount(True) == 0 and pTeam.getAnyWarPlanCount(True) == 0:
			if pTeam.isHasTech(gc.getInfoTypeForString('TECH_FEUDALISM')):
				ePrereqBuildingClass = gc.getInfoTypeForString('BUILDINGCLASS_INN')
				eBuildingWonder = gc.getInfoTypeForString('BUILDING_EYES_AND_EARS_NETWORK')
				eOrderBuilding = infoCiv.getCivilizationBuildings(ePrereqBuildingClass)
# ent - Bug Fix >>>
#				if pPlayer.getBuildingClassCount(ePrereqBuildingClass) < pPlayer.getBuildingClassPrereqBuilding(eBuildingWonder, ePrereqBuildingClass, pPlayer.getBuildingClassMaking(ePrereqBuildingClass)):
				if eOrderBuilding != -1 and pPlayer.getBuildingClassCount(ePrereqBuildingClass) < pPlayer.getBuildingClassPrereqBuilding(eBuildingWonder, ePrereqBuildingClass, pPlayer.getBuildingClassMaking(ePrereqBuildingClass)):
# ent <<<
# ent - Use Order Tool >>>
					if pushOrderConstructBuildingRandom(pCity, eOrderBuilding, 8):
						return True
					"""
					if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eOrderBuilding, -1, False, False, False, False):
							return True
					"""
# ent <<<
				else:
# ent - Use Order Tool >>>
					if pushOrderConstructBuildingRandom(pCity, eBuildingWonder, 20):
						return True
					"""
					if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBuildingWonder, -1, False, False, False, False):
							return True
					"""
# ent <<<
##--------	Better AI: End Add

#Kaijin >>>
## Buildings and Projects
	## Aristrakh - Death pact
		if eCiv == gc.getInfoTypeForString('CIVILIZATION_ARISTRAKH'):

			eDeathPact1 = gc.getInfoTypeForString('PROJECT_DEATH_PACT_1')
			eDeathPact2 = gc.getInfoTypeForString('PROJECT_DEATH_PACT_2')
			eDeathPact3 = gc.getInfoTypeForString('PROJECT_DEATH_PACT_3')
			eDeathPact4 = gc.getInfoTypeForString('PROJECT_DEATH_PACT_4')
			eDeathPact5 = gc.getInfoTypeForString('PROJECT_DEATH_PACT_5')
			eDeathRitual = gc.getInfoTypeForString('PROJECT_DEATH_RITUAL')

			if pCity.canCreate(eDeathPact1, False, False):
				if pCity.pushOrder(OrderTypes.ORDER_CREATE, eDeathPact1, -1, False, False, False, False):
					return True
			if bCapital or cf.AI_getWarSuccessCapitulationRatio(ePlayer) > -30:
				if CyGame().getSorenRandNum(100 + (iThreat // 2), "City Growth assist") < 10 * (pCity.happyLevel() - pCity.unhappyLevel(0)):

					if pCity.canCreate(eDeathPact2, False, False) and pCity.healthRate(False, 0) > -3:
						if pCity.pushOrder(OrderTypes.ORDER_CREATE, eDeathPact2, -1, False, False, False, False):
							return True

					leUniqueBuilding = []
					for eBuildingClass in xrange(gc.getNumBuildingClassInfos()):
						eBuilding = infoCiv.getCivilizationBuildings(eBuildingClass)
						if eBuilding != BuildingTypes.NO_BUILDING and eBuilding != gc.getBuildingClassInfo(eBuildingClass).getDefaultBuildingIndex():
							if pCity.canConstruct(eBuilding, False, False, False) and pCity.getBuildingProductionTurnsLeft(eBuilding, 0) < iThresholdTurn:
								leUniqueBuilding.append(eBuilding)
					if len(leUniqueBuilding) > 0:
						eOrderBuilding = leUniqueBuilding[CyGame().getSorenRandNum(len(leUniqueBuilding), "Pick UniqueBuilding")]
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eOrderBuilding, -1, False, False, False, False):
							return True

					if pCity.getPopulation() >= 15 or not cf.AI_hasRoomForFound(ePlayer):
						if pCity.canCreate(eDeathRitual, False, False):
							if pCity.getProjectProductionTurnsLeft(eDeathRitual, 0) < iThresholdTurn * 3:
								if pTeam.getProjectMaking(eDeathRitual) == 0:
									if pCity.pushOrder(OrderTypes.ORDER_CREATE, eDeathRitual, -1, False, False, False, False):
										return True

					if pCity.canCreate(eDeathPact3, False, False) and pCity.healthRate(False, 0) > -2:
						if pCity.pushOrder(OrderTypes.ORDER_CREATE, eDeathPact3, -1, False, False, False, False):
							return True
					if pCity.canCreate(eDeathPact4, False, False) and pCity.healthRate(False, 0) == 0:
						if pCity.pushOrder(OrderTypes.ORDER_CREATE, eDeathPact4, -1, False, False, False, False):
							return True
					if pCity.canCreate(eDeathPact5, False, False) and pCity.healthRate(False, 0) == 0:
						for eSpecialist in range(gc.getNumSpecialistInfos()):
							if eSpecialist != gc.getDefineINT("DEFAULT_SPECIALIST"):
								if pCity.isSpecialistValid(eSpecialist, 0) or pCity.getMaxSpecialistCount(eSpecialist) > pCity.getSpecialistCount(eSpecialist):
									if pCity.pushOrder(OrderTypes.ORDER_CREATE, eDeathPact5, -1, False, False, False, False):
										return True
# ent - Anti-Strike >>>
		## Infernal
		elif eCiv == en.eCivilizationInfernal:
			if pPlayer.isCivic(gc.getInfoTypeForString('CIVIC_SCHOLARSHIP')) and not pPlayer.isCivic(gc.getInfoTypeForString('CIVIC_GUILDS')):
				leAntiStrikeAssists =	 [	gc.getInfoTypeForString('BUILDING_MONEYCHANGER'),
											gc.getInfoTypeForString('BUILDING_SMUGGLERS_PORT'),
											gc.getInfoTypeForString('BUILDING_DEMONS_ALTAR'),
											gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_VEIL'),
											gc.getInfoTypeForString('BUILDING_GAMBLING_HOUSE'),
											gc.getInfoTypeForString('BUILDING_TAX_OFFICE')]
				for eBuilding in leAntiStrikeAssists:
					if pCity.canConstruct(eBuilding, False, False, False):
						if pushOrderConstructBuildingRandom(pCity, eBuilding, iThresholdTurn):
							return True
# ent <<<

	## World heritage
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_CRAZY_BY_WORLDHERITAGE')):
			if (bCapital or pCity.getPopulation() >= 10) and not bBestMilitaryFactory:
				if bCapital or (pTeam.getAtWarCount(True) == 0 or cf.AI_getWarSuccessCapitulationRatio(ePlayer) > -20 and iThreat < 80):
					iBestTurn = cyFlatValue(15, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
					eBestBuilding = BuildingTypes.NO_BUILDING
					for eBuildingClass in xrange(gc.getNumBuildingClassInfos()):
						if isWorldWonderClass(eBuildingClass):
							eBuilding = infoCiv.getCivilizationBuildings(eBuildingClass)
							if eBuilding != BuildingTypes.NO_BUILDING and pCity.canConstruct(eBuilding, False, False, False):
								iTurn = pCity.getBuildingProductionTurnsLeft(eBuilding, 0)
								if iTurn < iBestTurn:
									iBestTurn = iTurn
									eBestBuilding = eBuilding
					if eBestBuilding != BuildingTypes.NO_BUILDING:
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBestBuilding, -1, False, False, False, False):
							return True
			leEarlyWonders = [	gc.getInfoTypeForString('BUILDING_GOODREAU_STATUE'), 
								gc.getInfoTypeForString('BUILDING_VACANT_MAUSOLEUM'), 
								gc.getInfoTypeForString('BUILDING_TEMPLE_OF_DAGDA')]
			for eBuilding in leEarlyWonders:
				if pCity.canConstruct(eBuilding, False, False, False):
					iTurn = pCity.getBuildingProductionTurnsLeft(eBuilding, 0)
					if iTurn < cyFlatValue(10, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBuilding, -1, False, False, False, False):
							return True
	## Great library
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pTeam.isHasTech(gc.getInfoTypeForString('TECH_WRITING')):
				ePrereqBuildingClass = gc.getInfoTypeForString('BUILDINGCLASS_LIBRARY')
				eBuildingWonder = gc.getInfoTypeForString('BUILDING_GREAT_LIBRARY')
				eOrderBuilding = infoCiv.getCivilizationBuildings(ePrereqBuildingClass)
				if eOrderBuilding != BuildingTypes.NO_BUILDING and pPlayer.getBuildingClassCount(ePrereqBuildingClass) < pPlayer.getBuildingClassPrereqBuilding(eBuildingWonder, ePrereqBuildingClass, pPlayer.getBuildingClassMaking(ePrereqBuildingClass)):
					if pushOrderConstructBuildingRandom(pCity, eOrderBuilding, 8):
						return True
					"""
					if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eOrderBuilding, -1, False, False, False, False):
							return True
					"""
				else:
					if pushOrderConstructBuildingRandom(pCity, eBuildingWonder, 20):
						return True
					"""
					if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBuildingWonder, -1, False, False, False, False):
							return True
					"""

	## Great brewery
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pTeam.isHasTech(gc.getInfoTypeForString('TECH_SANITATION')):
				ePrereqBuildingClass = gc.getInfoTypeForString('BUILDINGCLASS_BREWERY')
				eBuildingWonder = gc.getInfoTypeForString('BUILDING_GREAT_BREWERY')
				eOrderBuilding = infoCiv.getCivilizationBuildings(ePrereqBuildingClass)
				if eOrderBuilding != BuildingTypes.NO_BUILDING and pPlayer.getBuildingClassCount(ePrereqBuildingClass) < pPlayer.getBuildingClassPrereqBuilding(eBuildingWonder, ePrereqBuildingClass, pPlayer.getBuildingClassMaking(ePrereqBuildingClass)):
					if pushOrderConstructBuildingRandom(pCity, eOrderBuilding, 4):
						return True
					"""
					if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eOrderBuilding, -1, False, False, False, False):
							return True
					"""
				else:
					if pushOrderConstructBuildingRandom(pCity, eBuildingWonder, 10):
						return True
					"""
					if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBuildingWonder, -1, False, False, False, False):
							return True
					"""

	## Ratcatchers guild
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pTeam.isHasTech(gc.getInfoTypeForString('TECH_POISONS')):
				ePrereqBuildingClass = gc.getInfoTypeForString('BUILDINGCLASS_HUNTING_LODGE')
				eBuildingWonder = gc.getInfoTypeForString('BUILDING_RATCATCHERS_GUILD')
				eOrderBuilding = infoCiv.getCivilizationBuildings(ePrereqBuildingClass)
				if eOrderBuilding != BuildingTypes.NO_BUILDING and pPlayer.getBuildingClassCount(ePrereqBuildingClass) < pPlayer.getBuildingClassPrereqBuilding(eBuildingWonder, ePrereqBuildingClass, pPlayer.getBuildingClassMaking(ePrereqBuildingClass)):
					if pushOrderConstructBuildingRandom(pCity, eOrderBuilding, 4):
						return True
					"""
					if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eOrderBuilding, -1, False, False, False, False):
							return True
					"""
				else:
					if pushOrderConstructBuildingRandom(pCity, eBuildingWonder, 10):
						return True
					"""
					if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBuildingWonder, -1, False, False, False, False):
							return True
					"""

	## Command post
		if pTeam.getAtWarCount(True) <= 3 and pTeam.getAnyWarPlanCount(True) <= 3:
			if pTeam.isHasTech(gc.getInfoTypeForString('TECH_MILITARY_STRATEGY')) and pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_ORGANIZED')):
				ePrereqBuildingClass = gc.getInfoTypeForString('BUILDINGCLASS_TRAINING_YARD')
				eBuildingWonder = gc.getInfoTypeForString('BUILDING_COMMAND_POST')
				eOrderBuilding = infoCiv.getCivilizationBuildings(ePrereqBuildingClass)
				if eOrderBuilding != BuildingTypes.NO_BUILDING and pPlayer.getBuildingClassCount(ePrereqBuildingClass) < pPlayer.getBuildingClassPrereqBuilding(eBuildingWonder, ePrereqBuildingClass, pPlayer.getBuildingClassMaking(ePrereqBuildingClass)):
					if pushOrderConstructBuildingRandom(pCity, eOrderBuilding, 4):
						return True
					"""
					if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eOrderBuilding, -1, False, False, False, False):
							return True
					"""
				else:
					if pushOrderConstructBuildingRandom(pCity, eBuildingWonder, 10):
						return True
					"""
					if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBuildingWonder, -1, False, False, False, False):
							return True
					"""

	## Order of the One Creator
		if pTeam.getAtWarCount(True) <= 3 and pTeam.getAnyWarPlanCount(True) <= 3:
			if pTeam.isHasTech(gc.getInfoTypeForString('TECH_DIVINE_ESSENCE')):
				ePrereqBuildingClass = gc.getInfoTypeForString('BUILDINGCLASS_COURTHOUSE')
				eBuildingWonder = gc.getInfoTypeForString('BUILDING_ORDER_OF_THE_ONE_CREATOR')
				eOrderBuilding = infoCiv.getCivilizationBuildings(ePrereqBuildingClass)
				if eOrderBuilding != BuildingTypes.NO_BUILDING and pPlayer.getBuildingClassCount(ePrereqBuildingClass) < pPlayer.getBuildingClassPrereqBuilding(eBuildingWonder, ePrereqBuildingClass, pPlayer.getBuildingClassMaking(ePrereqBuildingClass)):
					if pushOrderConstructBuildingRandom(pCity, eOrderBuilding, 6):
						return True
					"""
					if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eOrderBuilding, -1, False, False, False, False):
							return True
					"""
				else:
					if pushOrderConstructBuildingRandom(pCity, eBuildingWonder, 15):
						return True
					"""
					if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBuildingWonder, -1, False, False, False, False):
							return True
					"""

	## Cathedral Rebirth
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pTeam.isHasTech(gc.getInfoTypeForString('TECH_CURRENCY')):
				ePrereqBuildingClass = gc.getInfoTypeForString('BUILDINGCLASS_MARKET')
				eBuildingWonder = gc.getInfoTypeForString('BUILDING_PATRIAN_BAZAAR')
				eOrderBuilding = infoCiv.getCivilizationBuildings(ePrereqBuildingClass)
				if eOrderBuilding != BuildingTypes.NO_BUILDING and pPlayer.getBuildingClassCount(ePrereqBuildingClass) < pPlayer.getBuildingClassPrereqBuilding(eBuildingWonder, ePrereqBuildingClass, pPlayer.getBuildingClassMaking(ePrereqBuildingClass)):
					if pushOrderConstructBuildingRandom(pCity, eOrderBuilding, 6):
						return True
					"""
					if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eOrderBuilding, -1, False, False, False, False):
							return True
					"""
				else:
					if pushOrderConstructBuildingRandom(pCity, eBuildingWonder, 15):
						return True
					"""
					if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBuildingWonder, -1, False, False, False, False):
							return True
					"""

	## Patrian Bazzar
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pTeam.isHasTech(gc.getInfoTypeForString('TECH_RELIGIOUS_LAW')):
				ePrereqBuildingClass = gc.getInfoTypeForString('BUILDINGCLASS_MARKET')
				eBuildingWonder = gc.getInfoTypeForString('BUILDING_CATHEDRAL_OF_REBIRTH')
				eOrderBuilding = infoCiv.getCivilizationBuildings(ePrereqBuildingClass)
				if eOrderBuilding != BuildingTypes.NO_BUILDING and pPlayer.getBuildingClassCount(ePrereqBuildingClass) < pPlayer.getBuildingClassPrereqBuilding(eBuildingWonder, ePrereqBuildingClass, pPlayer.getBuildingClassMaking(ePrereqBuildingClass)):
					if pushOrderConstructBuildingRandom(pCity, eOrderBuilding, 6):
						return True
					"""
					if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eOrderBuilding, -1, False, False, False, False):
							return True
					"""
				else:
					if pushOrderConstructBuildingRandom(pCity, eBuildingWonder, 15):
						return True
					"""
					if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBuildingWonder, -1, False, False, False, False):
							return True
					"""

		if pTeam.getAtWarCount(True) == 0 and pTeam.getAnyWarPlanCount(True) == 0 and iThreat < 50 and not bBestMilitaryFactory:
			eBuilding = gc.getInfoTypeForString('BUILDING_BAZAAR_OF_MAMMON')
			if pCity.canConstruct(eBuilding, False, False, False) and pCity.getPopulation() >= 8:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - (pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) + pCity.findCommerceRateRank(CommerceTypes.COMMERCE_GOLD) * 2) * 10):
					if pCity.getBuildingProductionTurnsLeft(eBuilding, 0) < cyFlatValue(15, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False):
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBuilding, -1, False, False, False, False):
							return True
			ltWonderAssists =	 [	#eBuilding,														iPop,	iMaxTurn
									(gc.getInfoTypeForString('BUILDING_FORBIDDEN_PALACE'),			8,		15),
									(gc.getInfoTypeForString('BUILDING_MOAI_STATUES'),				8,		15)
									]
			for eBuilding, iPop, iMaxTurn in ltWonderAssists:
				if pCity.canConstruct(eBuilding, False, False, False) and pCity.getPopulation() >= iPop:
					if pushOrderConstructBuildingRandom(pCity, eBuilding, iMaxTurn):
						return True

		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2 and iThreat < 100 and not bBestMilitaryFactory:
			ltWonderAssists =	 [	#eBuilding,														iPop,	iMaxTurn
									(gc.getInfoTypeForString('BUILDING_HERON_THRONE'),				8,		15),
									(gc.getInfoTypeForString('BUILDING_GREAT_LIGHTHOUSE'),			8,		15),
									(gc.getInfoTypeForString('BUILDING_GREED_OF_VELGYR'),			8,		15),
									(gc.getInfoTypeForString('BUILDING_SHRINE_OF_JUNIL'),			8,		15)
									]
			for eBuilding, iPop, iMaxTurn in ltWonderAssists:
				if pCity.canConstruct(eBuilding, False, False, False) and pCity.getPopulation() >= iPop:
					if pushOrderConstructBuildingRandom(pCity, eBuilding, iMaxTurn):
						return True
		if iThreat < 100 and not bBestMilitaryFactory:
			ltWonderAssists =	 [	#eBuilding,														iPop,	iMaxTurn
									(gc.getInfoTypeForString('BUILDING_MILITALY_ACADEMY'),			8,		15),
									(gc.getInfoTypeForString('BUILDING_CRAFTMAN_STUDIO'),			8,		15),
									(gc.getInfoTypeForString('BUILDING_GREAT_DINING'),				8,		15),
									(gc.getInfoTypeForString('BUILDING_TOWER_OF_MARTYR'),			8,		15),
									(gc.getInfoTypeForString('BUILDING_TOWER_OF_MOBIUS'),			8,		15),
									(gc.getInfoTypeForString('BUILDING_SPRING_OF_GHNUKE'),			8,		15),
									(gc.getInfoTypeForString('BUILDING_FORNACE_OF_MIDAS'),			8,		15),
									(gc.getInfoTypeForString('BUILDING_CIRCLE_OF_MONSOON'),			8,		15),
									(gc.getInfoTypeForString('BUILDING_HEART_OF_THE_CHAOS'),		8,		15),
									(gc.getInfoTypeForString('BUILDING_FOREST_ECLIPSE'),			8,		15),
									(gc.getInfoTypeForString('BUILDING_FORCE_FIELD_OF_CREATION'),	8,		15)
									]
			for eBuilding, iPop, iMaxTurn in ltWonderAssists:
				if pCity.canConstruct(eBuilding, False, False, False) and pCity.getPopulation() >= iPop:
					if pushOrderConstructBuildingRandom(pCity, eBuilding, iMaxTurn):
						return True
		
		"""
	## Shrine of the Champion
		if pTeam.getAtWarCount(True) == 0 and pTeam.getAnyWarPlanCount(True) == 0:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_SHRINE_OF_THE_CHAMPION'), False, False, False) and pCity.getPopulation() >= 8:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_SHRINE_OF_THE_CHAMPION'), -1, False, False, False, False)
					return True

	## Bazzar of Mammon
		if pTeam.getAtWarCount(True) == 0 and pTeam.getAnyWarPlanCount(True) == 0:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_BAZAAR_OF_MAMMON'), False, False, False) and pCity.getPopulation() >= 8:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_BAZAAR_OF_MAMMON'), -1, False, False, False, False)
					return True

	## Forbidden Palace
		if pTeam.getAtWarCount(True) == 0 and pTeam.getAnyWarPlanCount(True) == 0:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_FORBIDDEN_PALACE'), False, False, False) and pCity.getPopulation() >= 8:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_FORBIDDEN_PALACE'), -1, False, False, False, False)
					return True

	## Moai Statues
		if pTeam.getAtWarCount(True) == 0 and pTeam.getAnyWarPlanCount(True) == 0:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_MOAI_STATUES'), False, False, False) and pCity.getPopulation() >= 8:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_MOAI_STATUES'), -1, False, False, False, False)
					return True

	## Heron Throne
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_HERON_THRONE'), False, False, False) and pCity.getPopulation() >= 8:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_HERON_THRONE'), -1, False, False, False, False)
					return True

	## The Great Lighthouse
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_GREAT_LIGHTHOUSE'), False, False, False) and pCity.getPopulation() >= 8:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_GREAT_LIGHTHOUSE'), -1, False, False, False, False)
					return True

	## Greed of Velgyr
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_GREED_OF_VELGYR'), False, False, False) and pCity.getPopulation() >= 8:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_GREED_OF_VELGYR'), -1, False, False, False, False)
					return True

	## Shrine of Junil
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pPlayer.getStateReligion() == gc.getInfoTypeForString('RELIGION_THE_ORDER'):
				if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_SHRINE_OF_JUNIL'), False, False, False) and pCity.getPopulation() >= 8:
					if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_SHRINE_OF_JUNIL'), -1, False, False, False, False)
						return True

	## Lineage - Militaly academy
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_MILITALY_ACADEMY'), False, False, False) and pCity.getPopulation() >= 8:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_MILITALY_ACADEMY'), -1, False, False, False, False)
					return True
	## Lineage - Craftman studio
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_CRAFTMAN_STUDIO'), False, False, False) and pCity.getPopulation() >= 5:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_CRAFTMAN_STUDIO'), -1, False, False, False, False)
					return True
	## Lineage - Great dining
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_GREAT_DINING'), False, False, False) and pCity.getPopulation() >= 8:
				if pCity.getID() == pPlayer.AI_getBestGreatPeopleFarm().getID():
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_GREAT_DINING'), -1, False, False, False, False)
					return True

	## Rarna - Tower of martyr
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_TOWER_OF_MARTYR'), False, False, False) and pCity.getPopulation() >= 5:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_TOWER_OF_MARTYR'), -1, False, False, False, False)
					return True
	## Rarna - Tower of mobius
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_TOWER_OF_MOBIUS'), False, False, False) and pCity.getPopulation() >= 5:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_TOWER_OF_MOBIUS'), -1, False, False, False, False)
					return True

	## Megisus - Spring of ghnuke
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_SPRING_OF_GHNUKE'), False, False, False) and pCity.getPopulation() >= 8:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_SPRING_OF_GHNUKE'), -1, False, False, False, False)
					return True
	## Megisus - Fornace of midas
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_FORNACE_OF_MIDAS'), False, False, False) and pCity.getPopulation() >= 8:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_FORNACE_OF_MIDAS'), -1, False, False, False, False)
					return True
	## Megisus - Circle of monsoon
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_CIRCLE_OF_MONSOON'), False, False, False) and pCity.getPopulation() >= 8:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_CIRCLE_OF_MONSOON'), -1, False, False, False, False)
					return True
	## Megisus - Heart of the chaos
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_HEART_OF_THE_CHAOS'), False, False, False) and pCity.getPopulation() >= 8:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_HEART_OF_THE_CHAOS'), -1, False, False, False, False)
					return True
	## Megisus - Forest exlipse
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_FOREST_ECLIPSE'), False, False, False) and pCity.getPopulation() >= 8:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_FOREST_ECLIPSE'), -1, False, False, False, False)
					return True
	## Megisus - Force field of creation
		if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_FORCE_FIELD_OF_CREATION'), False, False, False) and pCity.getPopulation() >= 8:
				if CyGame().getSorenRandNum(50, "Construct Wonder assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_FORCE_FIELD_OF_CREATION'), -1, False, False, False, False)
					return True
		"""
	## Led to the End
		if CyGame().isVictoryValid(gc.getInfoTypeForString('VICTORY_LED_TO_THE_END')) and not CyGame().isOption(GameOptionTypes.GAMEOPTION_NO_GLOBAL_COUNTER) and pCity.getPopulation() >= 8 and iThreat < 50 and not bBestMilitaryFactory:
			## Projects
			eProject = gc.getInfoTypeForString('PROJECT_LED_TO_THE_END')
			if pCity.canCreate(eProject, False, False):
				if pCity.getProjectProductionTurnsLeft(eProject, 0) < cyFlatValue(40, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False):
					if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
						return True
			eProject = gc.getInfoTypeForString('PROJECT_DARK_GATE')
			if pCity.canCreate(eProject, False, False):
				if pCity.getProjectProductionTurnsLeft(eProject, 0) < cyFlatValue(20, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False):
					if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
						return True
			eProject = gc.getInfoTypeForString('PROJECT_STIGMA_THE_BLACK')
			if pCity.canCreate(eProject, False, False):
				if pCity.getProjectProductionTurnsLeft(eProject, 0) < cyFlatValue(20, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False):
					if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
						return True
			eProject = gc.getInfoTypeForString('PROJECT_FESTIVAL_OF_THE_BERSERKERS')
			if pCity.canCreate(eProject, False, False):
				if pCity.getProjectProductionTurnsLeft(eProject, 0) < cyFlatValue(20, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False):
					if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
						return True
			eProject = gc.getInfoTypeForString('PROJECT_DISASTER')
			if pCity.canCreate(eProject, False, False):
				if pCity.getProjectProductionTurnsLeft(eProject, 0) < cyFlatValue(20, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False):
					if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
						return True
			eProject = gc.getInfoTypeForString('PROJECT_RETURN_SOUL')
			if pCity.canCreate(eProject, False, False):
				if pCity.getProjectProductionTurnsLeft(eProject, 0) < cyFlatValue(10, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False):
					if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
						return True
			eProject = gc.getInfoTypeForString('PROJECT_BLACK_RAIN')
			if pCity.canCreate(eProject, False, False):
				if pCity.getProjectProductionTurnsLeft(eProject, 0) < cyFlatValue(10, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False):
					if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
						return True
			eProject = gc.getInfoTypeForString('PROJECT_MAY_SICKNESS')
			if pCity.canCreate(eProject, False, False):
				if pCity.getProjectProductionTurnsLeft(eProject, 0) < cyFlatValue(10, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False):
					if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
						return True

			## Magic Circles
			eMagicCircle8 = gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_END')
			eMagicCircle6 = gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_BLACK_DEATH')
			eMagicCircle4 = gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_CALAMITY')
			eMagicCircle2 = gc.getInfoTypeForString('BUILDING_MAGIC_CIRCLE_OF_THE_SADNESS')
			if pCity.canConstruct(eMagicCircle8, False, False, False):
				if pCity.getBuildingProductionTurnsLeft(eMagicCircle8, 0) < cyFlatValue(30, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False):
					if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eMagicCircle8, -1, False, False, False, False):
						return True
			elif pCity.canConstruct(eMagicCircle6, False, False, False):
				if pCity.getBuildingProductionTurnsLeft(eMagicCircle6, 0) < cyFlatValue(20, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False):
					if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eMagicCircle6, -1, False, False, False, False):
						return True
			elif pCity.canConstruct(eMagicCircle4, False, False, False):
				if pCity.getBuildingProductionTurnsLeft(eMagicCircle4, 0) < cyFlatValue(20, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False):
					if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eMagicCircle4, -1, False, False, False, False):
						return True
			elif pCity.canConstruct(eMagicCircle2, False, False, False):
				if pCity.getBuildingProductionTurnsLeft(eMagicCircle2, 0) < cyFlatValue(10, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False):
					if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eMagicCircle2, -1, False, False, False, False):
						return True

# ent >>>
	## Statue of Luxury >>>
		if iGameProgress > 30 and pPlayer.getGuildPlusCounter(2) == 7 and not bBestMilitaryFactory:
			if iThreat < 100:
				if CyGame().getSorenRandNum(100, "Luxury Victory assist") < (50 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					eBuilding = gc.getInfoTypeForString('BUILDING_CELESTIAL_COMPASS')
					if pCity.canConstruct(eBuilding, False, False, False):
						if pCity.getBuildingProductionTurnsLeft(eBuilding, 0) < iThresholdTurn * 3:
							if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBuilding, -1, False, False, False, False):
								return True
					eBuilding = gc.getInfoTypeForString('BUILDING_ASTROLOGICAL_OBSERVATORY')
					if pCity.canConstruct(eBuilding, False, False, False):
						if pCity.getBuildingProductionTurnsLeft(eBuilding, 0) < iThresholdTurn:
							if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBuilding, -1, False, False, False, False):
								return True
					leStatueProjects = [gc.getInfoTypeForString('PROJECT_FLYING_TO_THE_SKY'), 
										gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_COCKPIT'), 
										gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_LIFE_SUPPORT'), 
										gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_STASIS_CHAMBER'), 
										gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_DOCKING_BAY'), 
										gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_ENGINE'), 
										gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_CASING'), 
										gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_THRUSTERS'), 
										gc.getInfoTypeForString('PROJECT_STATUE_OF_LUXURY_CORE')			]
					for eProject in leStatueProjects:
						if pCity.canCreate(eProject, False, False):
							if pCity.getProjectProductionTurnsLeft(eProject, 0) < iThresholdTurn * 2:
								if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
									return True

	## Assist Cultural or Religious Victories and Religous Leaders >>>
		if iGameProgress > 30 and cf.AI_getWarSuccessCapitulationRatio(ePlayer) > -20 and iThreat < 80 and not bBestMilitaryFactory:
		## Construct Cultural Building.
			if pPlayer.getGuildPlusCounter(2) == 2:
				leCulturalVictoryAssists = []
				if CyGame().getSorenRandNum(100, "Cultural Victory assist") < (50 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					leCulturalVictoryAssists += [
												gc.getInfoTypeForString('BUILDINGCLASS_THEATRE_OF_DREAMS'), 
												gc.getInfoTypeForString('BUILDINGCLASS_HALL_OF_KINGS'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_TEMPORENCE'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TOWER_OF_HERVE')
												]
				"""
				if CyGame().getSorenRandNum(100, "Cultural Victory assist") < (50 - pCity.findCommerceRateRank(CommerceTypes.COMMERCE_CULTURE) * 10):
					leCulturalVictoryAssists += [
												gc.getInfoTypeForString('BUILDINGCLASS_MONUMENT'), 
												gc.getInfoTypeForString('BUILDINGCLASS_THEATRE'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_OVERLORDS'), 
												gc.getInfoTypeForString('BUILDINGCLASS_CARNIVAL'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_ORDER'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_EMPYREAN'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_KILMORPH'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_LEAVES'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_VEIL'), 
												gc.getInfoTypeForString('BUILDINGCLASS_PAGAN_TEMPLE'), 
												gc.getInfoTypeForString('BUILDINGCLASS_SYLIVENS_PERFECT_LYRE')
												]
				"""
				if CyGame().getSorenRandNum(100, "Cultural Victory assist") < (50 - pCity.findYieldRateRank(YieldTypes.YIELD_COMMERCE) * 10):
					leCulturalVictoryAssists += [
												gc.getInfoTypeForString('BUILDINGCLASS_MONUMENT'), 
												gc.getInfoTypeForString('BUILDINGCLASS_THEATRE'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_OVERLORDS'), 
												gc.getInfoTypeForString('BUILDINGCLASS_CARNIVAL'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_ORDER'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_EMPYREAN'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_KILMORPH'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_LEAVES'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_VEIL'), 
												gc.getInfoTypeForString('BUILDINGCLASS_PAGAN_TEMPLE'), 
												gc.getInfoTypeForString('BUILDINGCLASS_SYLIVENS_PERFECT_LYRE')
												]

				def findCultureTimesRank(pCity, ePlayer):
					iCulture = pCity.getCultureTimes100(ePlayer)
					iRank = 1
					for pyCity in PyPlayer(ePlayer).getCityList():
						pLoopCity = pyCity.GetCy()
						if (pLoopCity.getCultureTimes100(ePlayer) > iCulture or
						   (pLoopCity.getCultureTimes100(ePlayer) == iCulture and pLoopCity.getID() < pCity.getID())):
							iRank = iRank + 1
					return iRank

				if CyGame().getSorenRandNum(100, "Cultural Victory assist") < (50 - findCultureTimesRank(pCity, ePlayer) * 10):
					leCulturalVictoryAssists += [
												gc.getInfoTypeForString('BUILDINGCLASS_MONUMENT'), 
												gc.getInfoTypeForString('BUILDINGCLASS_THEATRE'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_OVERLORDS'), 
												gc.getInfoTypeForString('BUILDINGCLASS_CARNIVAL'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_ORDER'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_EMPYREAN'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_KILMORPH'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_LEAVES'), 
												gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_VEIL'), 
												gc.getInfoTypeForString('BUILDINGCLASS_PAGAN_TEMPLE'), 
												gc.getInfoTypeForString('BUILDINGCLASS_SYLIVENS_PERFECT_LYRE')
												]

				for eBuildingClass in leCulturalVictoryAssists:
					eBuilding = infoCiv.getCivilizationBuildings(eBuildingClass)
					if eBuilding != BuildingTypes.NO_BUILDING and pCity.canConstruct(eBuilding, False, False, False):
						if isWorldWonderClass(eBuildingClass):
							if pCity.getBuildingProductionTurnsLeft(eBuilding, 0) < iThresholdTurn * 3:
								if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBuilding, -1, False, False, False, False):
									return True
						else:
							if pCity.getBuildingProductionTurnsLeft(eBuilding, 0) < iThresholdTurn:
								if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBuilding, -1, False, False, False, False):
									return True

		## Spread Victorious Religion across the world.
			if pPlayer.getGuildPlusCounter(2) == 3:
				if CyGame().getSorenRandNum(200, "Religious Victory assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
					# Select victorious religion.
					eReligion = ReligionTypes.NO_RELIGION
					iBestPercent = 0
					for eLoopReligion in xrange(gc.getNumReligionInfos()):
						if eLoopReligion == en.eReligionCultoftheDragon:
							continue
						if pTeam.hasHolyCity(eLoopReligion) and infoLeader.getReligionWeightModifier(eLoopReligion) >= 0:
							iReligionPercent = CyGame().calculateReligionPercent(eLoopReligion)
							if iReligionPercent > iBestPercent:
								iBestPercent = iReligionPercent
								eReligion = eLoopReligion
					# Train missionary or Build temple of the religion.
					if eReligion != ReligionTypes.NO_RELIGION:
						if pCity.isHasReligion(eReligion):
							eTech = gc.getReligionInfo(eReligion).getTechPrereq()
							if eTech != TechTypes.NO_TECH and pPlayer.isHasTech(eTech):
								eSpreadUnitClass = gc.getReligionInfo(eReligion).getFreeUnitClass()
								if eSpreadUnitClass != UnitClassTypes.NO_UNITCLASS and pPlayer.getUnitClassCountPlusMaking(eSpreadUnitClass) < 2:
									eSpreadUnit = infoCiv.getCivilizationUnits(eSpreadUnitClass)
									if eSpreadUnit != UnitTypes.NO_UNIT:
										if pCity.canTrain(eSpreadUnit, False, False):
											if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eSpreadUnit, UnitAITypes.UNITAI_MISSIONARY, False, False, False, False):
												return True
										else:
											eTempleBuilding = gc.getUnitInfo(eSpreadUnit).getPrereqBuilding()
											if eTempleBuilding != BuildingTypes.NO_BUILDING and pCity.canConstruct(eTempleBuilding, False, False, False):
												if pCity.getBuildingProductionTurnsLeft(eTempleBuilding, 0) < iThresholdTurn:
													if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eTempleBuilding, -1, False, False, False, False):
														return True

			elif CyGame().getSorenRandNum(100, "Spread Religion assist") < 40:
		## Spread StateReligion among own city.
				def loveStateReligion():
					if pPlayer.getStateReligion() == ReligionTypes.NO_RELIGION:
						return False
					if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_SPIRITUAL')):
						return True
					if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_FANATIC')):
						return True
					if eCiv == gc.getInfoTypeForString('CIVILIZATION_MALAKIM'):
						return True
					if pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_GOVERNMENT')) == gc.getInfoTypeForString('CIVIC_THEOCRACY'):
						return True
					if pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_CULTURAL_VALUES')) in (gc.getInfoTypeForString('CIVIC_RELIGION'), gc.getInfoTypeForString('CIVIC_CRUSADE')):
						return True
					if pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_RELIGION')) in (gc.getInfoTypeForString('CIVIC_SLUMBERING_COVEN'), gc.getInfoTypeForString('CIVIC_SOCIAL_ORDER')):
						return True
					if pPlayer.getNumBuilding(gc.getInfoTypeForString('BUILDING_TEMPLE_OF_TEMPORENCE')) > 0:
						return True
					return False

				if loveStateReligion() or CyGame().getSorenRandNum(100, "Spread StateReligion assist") < 20:
					eStateReligion = pPlayer.getStateReligion()
					if eStateReligion != ReligionTypes.NO_RELIGION:
						if pCity.isHasReligion(eStateReligion):
							eTech = gc.getReligionInfo(eStateReligion).getTechPrereq()
							if eTech != TechTypes.NO_TECH and pPlayer.isHasTech(eTech):
								eSpreadUnitClass = gc.getReligionInfo(eStateReligion).getFreeUnitClass()
								if eSpreadUnitClass != UnitClassTypes.NO_UNITCLASS and pPlayer.getUnitClassCountPlusMaking(eSpreadUnitClass) < 2:
									eSpreadUnit = infoCiv.getCivilizationUnits(eSpreadUnitClass)
									if eSpreadUnit != UnitTypes.NO_UNIT:
										if pCity.canTrain(eSpreadUnit, False, False):
											for pyCity in PyPlayer(ePlayer).getCityList():
												pLoopCity = pyCity.GetCy()
												if pCity.plot().getArea() == pLoopCity.plot().getArea():
													if not pLoopCity.isHasReligion(eStateReligion):
														if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eSpreadUnit, UnitAITypes.UNITAI_MISSIONARY, False, False, False, False):
															return True
										else:
											eTempleBuilding = gc.getUnitInfo(eSpreadUnit).getPrereqBuilding()
											if eTempleBuilding != BuildingTypes.NO_BUILDING and pCity.canConstruct(eTempleBuilding, False, False, False):
												if pCity.getBuildingProductionTurnsLeft(eTempleBuilding, 0) < iThresholdTurn:
													if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eTempleBuilding, -1, False, False, False, False):
														return True

		## Spread Several Religion among own cultural city.
				if (pPlayer.getGuildPlusCounter(2) == 2 or pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_IRON_WILL'))) and not pPlayer.isNoNonStateReligionSpread():
					for eReligion in xrange(gc.getNumReligionInfos()):
						if eReligion in (en.eReligionCouncilofEsus, en.eReligionCultoftheDragon):
							continue
						if pCity.isHasReligion(eReligion):
							eTech = gc.getReligionInfo(eReligion).getTechPrereq()
							if eTech != TechTypes.NO_TECH and pPlayer.isHasTech(eTech):
								eSpreadUnitClass = gc.getReligionInfo(eReligion).getFreeUnitClass()
								if eSpreadUnitClass != UnitClassTypes.NO_UNITCLASS and pPlayer.getUnitClassCountPlusMaking(eSpreadUnitClass) < 2:
									eSpreadUnit = infoCiv.getCivilizationUnits(eSpreadUnitClass)
									if eSpreadUnit != UnitTypes.NO_UNIT and pCity.canTrain(eSpreadUnit, False, False):
										for pyCity in PyPlayer(ePlayer).getCityList():
											pLoopCity = pyCity.GetCy()
											if pCity.plot().getArea() == pLoopCity.plot().getArea():
												if pLoopCity.findCommerceRateRank(CommerceTypes.COMMERCE_CULTURE) < 5 and not pLoopCity.isHasReligion(eReligion):
													if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eSpreadUnit, UnitAITypes.UNITAI_MISSIONARY, False, False, False, False):
														return True

		## Spread the Religion who has HolyCity across the world.
				for eReligion in xrange(gc.getNumReligionInfos()):
					if pCity.isHolyCityByType(eReligion) and infoLeader.getReligionWeightModifier(eReligion) >= 0 and CyGame().getSorenRandNum(100, "Spread HolyCity assist") < 30:
						bValid = False
						for eBuilding in xrange(gc.getNumBuildingInfos()):
							if pCity.isHasBuilding(eBuilding):
								if gc.getBuildingInfo(eBuilding).getGlobalReligionCommerce() == eReligion:
									bValid = True
									break
						if bValid:
							eTech = gc.getReligionInfo(eReligion).getTechPrereq()
							if eTech != TechTypes.NO_TECH and pPlayer.isHasTech(eTech):
								eSpreadUnitClass = gc.getReligionInfo(eReligion).getFreeUnitClass()
								if eSpreadUnitClass != UnitClassTypes.NO_UNITCLASS and pPlayer.getUnitClassCountPlusMaking(eSpreadUnitClass) < 2:
									eSpreadUnit = infoCiv.getCivilizationUnits(eSpreadUnitClass)
									if eSpreadUnit != UnitTypes.NO_UNIT:
										if pCity.canTrain(eSpreadUnit, False, False):
											if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eSpreadUnit, UnitAITypes.UNITAI_MISSIONARY, False, False, False, False):
												return True
										else:
											eTempleBuilding = gc.getUnitInfo(eSpreadUnit).getPrereqBuilding()
											if eTempleBuilding != BuildingTypes.NO_BUILDING and pCity.canConstruct(eTempleBuilding, False, False, False):
												if pCity.getBuildingProductionTurnsLeft(eTempleBuilding, 0) < iThresholdTurn:
													if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eTempleBuilding, -1, False, False, False, False):
														return True

	## Unique Projects
		if pCity.getPopulation() >= 8 and iThreat < 100 and not bBestMilitaryFactory:
		## Elohim
			if eCiv == en.eCivilizationElohim:
				eProject = gc.getInfoTypeForString('PROJECT_HALLOWING_OF_THE_ELOHIM')
				if CyGame().getSorenRandNum(100, "Hallowing of the Elohim") < CyGame().getGlobalCounter() - 10:
					if pCity.canCreate(eProject, False, False):
						if pTeam.getProjectMaking(eProject) == 0:
							if pCity.getProjectProductionTurnsLeft(eProject, 0) < iThresholdTurn:
								if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
									return True

		## Sheaim
			elif eCiv == en.eCivilizationSheaim:
				eProject = gc.getInfoTypeForString('PROJECT_ELEGY_OF_THE_SHEAIM')
				ePlanarGate = gc.getInfoTypeForString('BUILDING_PLANAR_GATE')
				if pCity.isHasActiveBuilding(ePlanarGate):
					if pPlayer.countNumBuildings(ePlanarGate) * 10 > CyGame().getGlobalCounter() and pTeam.getAtWarCount(True) == 0:
						if pCity.canCreate(eProject, False, False):
							if pTeam.getProjectMaking(eProject) == 0:
								if pCity.getProjectProductionTurnsLeft(eProject, 0) < iThresholdTurn:
									if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
										return True
				else:
					if pPlayer.countNumBuildings(ePlanarGate) * 10 < CyGame().getGlobalCounter():
						if pCity.canConstruct(ePlanarGate, False, False, False):
							if pPlayer.getBuildingClassMaking(ePlanarGate) == 0:
								if pCity.getBuildingProductionTurnsLeft(ePlanarGate, 0) < iThresholdTurn:
									if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, ePlanarGate, -1, False, False, False, False):
										return True

		## Illians
			elif eCiv == en.eCivilizationIllians:
				eTempleHand = gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_HAND')
				if pCity.canConstruct(eTempleHand, False, False, False):
					if pCity.getBuildingProductionTurnsLeft(eTempleHand, 0) < iThresholdTurn:
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eTempleHand, -1, False, False, False, False):
							return True
				eProject = gc.getInfoTypeForString('PROJECT_ASCENSION')
				if pCity.canCreate(eProject, False, False):
					if pCity.getProjectProductionTurnsLeft(eProject, 0) < iThresholdTurn * 3:
						if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
							return True
				eProject = gc.getInfoTypeForString('PROJECT_THE_WHITE_HAND')
				if pCity.canCreate(eProject, False, False):
					if pCity.getProjectProductionTurnsLeft(eProject, 0) < iThresholdTurn * 3:
						if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
							return True
				eProject = gc.getInfoTypeForString('PROJECT_STIR_FROM_SLUMBER')
				if pCity.canCreate(eProject, False, False):
					if pCity.getProjectProductionTurnsLeft(eProject, 0) < iThresholdTurn * 3:
						if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
							return True
				eProject = gc.getInfoTypeForString('PROJECT_SAMHAIN')
				if pCity.canCreate(eProject, False, False):
					if pCity.getProjectProductionTurnsLeft(eProject, 0) < iThresholdTurn * 2:
						if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
							return True
				eProject = gc.getInfoTypeForString('PROJECT_THE_DEEPENING')
				if pCity.canCreate(eProject, False, False):
					if pCity.getProjectProductionTurnsLeft(eProject, 0) < iThresholdTurn * 2:
						if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
							return True
				if pPlayer.getGuildPlusCounter(2) == 1 and pPlayer.isHasTech(gc.getInfoTypeForString('TECH_OMNISCIENCE')):
					eProject = gc.getInfoTypeForString('PROJECT_THE_DRAW')
					if pCity.canCreate(eProject, False, False):
						if pCity.getProjectProductionTurnsLeft(eProject, 0) < iThresholdTurn * 2:
							if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
								return True

		## Niraikanai
			elif eCiv == en.eCivilizationNiraikanai:
				eProject = gc.getInfoTypeForString('PROJECT_NATURES_REVOLT')
				if pCity.canCreate(eProject, False, False):
					if pCity.getProjectProductionTurnsLeft(eProject, 0) < iThresholdTurn * 2:
						if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
							return True

		## Droaum
			elif eCiv == en.eCivilizationDroaum:
				eProject = gc.getInfoTypeForString('PROJECT_SECRET_OF_EVOLUTION_DROAUM')
				if pPlayer.isSlaveTrade() or (CyGame().getGlobalCounter() > 70 and not pPlayer.isEventOccured(gc.getInfoTypeForString('EVENT_ARMAGEDDON_APOCALYPSE'))) or pPlayer.getAveragePopulation() > 20:
					if pCity.canCreate(eProject, False, False):
						if pCity.getProjectProductionTurnsLeft(eProject, 0) < iThresholdTurn * 2:
							if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
								return True

		## Despiel
			elif eCiv == en.eCivilizationDespiel:
				eProject = gc.getInfoTypeForString('PROJECT_LIFE_OF_THE_IMMORTAL')
				if pCity.canCreate(eProject, False, False):
					if pCity.getProjectProductionTurnsLeft(eProject, 0) < iThresholdTurn * 4:
						if pCity.pushOrder(OrderTypes.ORDER_CREATE, eProject, -1, False, False, False, False):
							return True

		## Rarna
			elif eCiv == en.eCivilizationRarna:
				iNeedPrereqBuildings = 6
				if iNumCities >= iNeedPrereqBuildings:
					if pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2:
						eSpreadCorruption = gc.getInfoTypeForString('PROJECT_SPREAD_CORRUPTION')
						eFireInheritance = gc.getInfoTypeForString('PROJECT_FIRE_INHERITANCE')
						ePrincessofDarkness = gc.getInfoTypeForString('PROJECT_PRINCESS_OF_DARKNESS')

						if CyGame().getProjectCreatedCount(eSpreadCorruption) == 0:
							iWorldAlignmentTrend = 0
							for eLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
								pLoopPlayer = gc.getPlayer(eLoopPlayer)
								if pLoopPlayer.isAlive():
									if pLoopPlayer.getAlignment() == en.eAlignmentGood:
										iWorldAlignmentTrend += CyGame().getPlayerScore(eLoopPlayer)
									elif pLoopPlayer.getAlignment() == en.eAlignmentEvil:
										iWorldAlignmentTrend -= CyGame().getPlayerScore(eLoopPlayer)
							if (2 * iWorldAlignmentTrend < -3 * CyGame().getPlayerScore(CyGame().getRankPlayer(1))) or CyGame().getGlobalCounter() > 25:
								if pCity.canCreate(eSpreadCorruption, False, False):
									if pCity.getProjectProductionTurnsLeft(eSpreadCorruption, 0) < iThresholdTurn * 3:
										if pCity.pushOrder(OrderTypes.ORDER_CREATE, eSpreadCorruption, -1, False, False, False, False):
											return True
						elif CyGame().getProjectCreatedCount(eFireInheritance) == 0:
							if not pPlayer.isFeatAccomplished(FeatTypes.FEAT_GLOBAL_SPELL) or CyGame().getGlobalCounter() > 50 or pPlayer.isHasTech(gc.getInfoTypeForString('TECH_DIVINE_ESSENCE')):
								if pCity.canCreate(eFireInheritance, False, False):
									if pCity.getProjectProductionTurnsLeft(eFireInheritance, 0) < iThresholdTurn * 2:
										if pCity.pushOrder(OrderTypes.ORDER_CREATE, eFireInheritance, -1, False, False, False, False):
											return True
							ePrereqBuilding = gc.getInfoTypeForString('BUILDING_TEMPLE_OF_THE_INHERITANCE')
							eFreeWonder = gc.getInfoTypeForString('BUILDING_TEMPLE_OF_TEMPORENCE')
							if pPlayer.countNumBuildings(ePrereqBuilding) < iNeedPrereqBuildings:
								if pCity.canConstruct(eFreeWonder, False, False, False):
									if pushOrderConstructBuildingRandom(pCity, eFreeWonder, 12):
										return True
								if pCity.canConstruct(ePrereqBuilding, False, False, False):
									if pushOrderConstructBuildingRandom(pCity, ePrereqBuilding, 6):
										return True
						elif CyGame().getProjectCreatedCount(ePrincessofDarkness) == 0:
							if pCity.canCreate(ePrincessofDarkness, False, False):
								if pCity.pushOrder(OrderTypes.ORDER_CREATE, ePrincessofDarkness, -1, False, False, False, False):
									return True
							ePrereqBuilding = gc.getInfoTypeForString('BUILDING_ALTAR_OF_THE_IMPORTANCE')
							eFreeWonder = gc.getInfoTypeForString('BUILDING_THE_NEXUS')
							if pPlayer.countNumBuildings(ePrereqBuilding) < iNeedPrereqBuildings:
								if pCity.canConstruct(eFreeWonder, False, False, False):
									if pushOrderConstructBuildingRandom(pCity, eFreeWonder, 16):
										return True
								if pCity.canConstruct(ePrereqBuilding, False, False, False):
									if pushOrderConstructBuildingRandom(pCity, ePrereqBuilding, 8):
										return True
	## World Wonders
		eMercurianGate = gc.getInfoTypeForString('BUILDINGCLASS_MERCURIAN_GATE')
		if pCity.getPopulation() >= 10 and not bBestMilitaryFactory:
			if CyGame().getSorenRandNum(10000, "Build Wonder assist") < infoLeader.getWonderConstructRand() * (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 20):
				if ((pTeam.getAtWarCount(True) <= 1 and pTeam.getAnyWarPlanCount(True) <= 2) or
					(CyGame().getPlayerRank(ePlayer) <= 2 and cf.AI_getWarSuccessCapitulationRatio(ePlayer) > -20)):
					eBestBuilding = BuildingTypes.NO_BUILDING
					iBestTurn = iThresholdTurn
					for eBuildingClass in xrange(gc.getNumBuildingClassInfos()):
						if isWorldWonderClass(eBuildingClass) and eBuildingClass != eMercurianGate:
							eBuilding = infoCiv.getCivilizationBuildings(eBuildingClass)
							if eBuilding != BuildingTypes.NO_BUILDING and pCity.canConstruct(eBuilding, False, False, False):
								iFlavorModifier = 100
								infoBuilding = gc.getBuildingInfo(eBuilding)
								for eFlavorType in xrange(gc.getNumFlavorTypes()):
									iFlavorModifier += infoLeader.getFlavorValue(eFlavorType) * infoBuilding.getFlavorValue(eFlavorType) // 2
								if iFlavorModifier > 0:
									iTurn = pCity.getBuildingProductionTurnsLeft(eBuilding, 0) * 100 // iFlavorModifier
									if iTurn < iBestTurn:
										iBestTurn = iTurn
										eBestBuilding = eBuilding
					if eBestBuilding != BuildingTypes.NO_BUILDING:
						if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBestBuilding, -1, False, False, False, False):
							return True

		if not CyGame().isBuildingClassMaxedOut(eMercurianGate, 0):
			if pCity.getPopulation() >= 10 and iThreat > 40:
				if CyGame().getSorenRandNum(100, "Mercurian Gate") < iThreat - 40:
					def isAtWarWithInfernal():
						for eLoopPlayer in xrange(gc.getMAX_CIV_PLAYERS()):
							pLoopPlayer = gc.getPlayer(eLoopPlayer)
							if pLoopPlayer.isAlive() and eLoopPlayer != ePlayer:
								if pLoopPlayer.getCivilizationType() == en.eCivilizationInfernal:
									if pTeam.isAtWar(pLoopPlayer.getTeam()):
										return True
						return False

					if pTeam.getAtWarCount(True) == 0 or isAtWarWithInfernal():
						iThreshold = 0
						eAlignment = pPlayer.getAlignment()
						if eAlignment == en.eAlignmentGood:
							iThreshold += 10
						elif eAlignment == en.eAlignmentNeutral:
							iThreshold += 5
						eStateReligion = pPlayer.getStateReligion()
						if eStateReligion != ReligionTypes.NO_RELIGION and gc.getReligionInfo(eStateReligion).getAlignment() == en.eAlignmentGood:
							iThreshold += 10
						if iThreshold > 0:
							eBuilding = infoCiv.getCivilizationBuildings(eMercurianGate)
							if eBuilding != BuildingTypes.NO_BUILDING and pCity.canConstruct(eBuilding, False, False, False):
								iThreshold = cyFlatValue(iThreshold, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
								if pCity.getBuildingProductionTurnsLeft(eBuilding, 0) < iThreshold:
									if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eBuilding, -1, False, False, False, False):
										return True
# ent <<<

## Civil Units
		## Scions - Awakened
		if eCiv == en.eCivilizationScions:
# ent >>>
#			if pTeam.getAtWarCount(True) == 0 and pTeam.getAnyWarPlanCount(True) == 0:
			if (pTeam.getAtWarCount(True) == 0 or cf.AI_getWarSuccessCapitulationRatio(ePlayer) > -20) and iThreat < 80 and pPlayer.getNumCities() > 1:
# ent <<<
				eAwakened = gc.getInfoTypeForString('UNIT_AWAKENED')
				eReborn = gc.getInfoTypeForString('UNIT_REBORN')
				if (pCity.canTrain(eAwakened, False, False) or pCity.canTrain(eReborn, False, False)):
# ent >>>
					bValid = False
					# 都市開発も大事
					if (bCapital and CyGame().getSorenRandNum(100, "Awakened assist") < 70) or bBestMilitaryFactory:
						if cf.doAddPopValid(pCity):
							bValid = True
					else:
						for pyCity in PyPlayer(ePlayer).getCityList():
							pLoopCity = pyCity.GetCy()
							if pCity.plot().getArea() == pLoopCity.plot().getArea():
								if cf.doAddPopValid(pLoopCity):
									bValid = True
									break
					if bValid and CyGame().getSorenRandNum(100, "Awakened assist") < 80:
						iBestModifier = -100
						eBestSettler = UnitTypes.NO_UNIT
						leSettlers = [eAwakened, eReborn]
						for eSettler in leSettlers:
							if pCity.canTrain(eSettler, False, False):
								iModifier = pCity.getUnitProductionModifier(eSettler)
								if iModifier > iBestModifier:
									eBestSettler = eSettler
									iBestModifier = iModifier
						if eBestSettler != UnitTypes.NO_UNIT:
							if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eBestSettler, -1, False, False, False, False):
								return True

# ent <<<

## Combat Units
	## Units definition
		eHunter = gc.getInfoTypeForString('UNITCLASS_HUNTER')
		eHunterCiv = infoCiv.getCivilizationUnits(eHunter)
		iHunterNum = pPlayer.getUnitClassCountPlusMaking(eHunter)
		eRanger = gc.getInfoTypeForString('UNITCLASS_RANGER')
		eRangerCiv = infoCiv.getCivilizationUnits(eRanger)
		iRangerNum = pPlayer.getUnitClassCountPlusMaking(eRanger)
		eAssassin = gc.getInfoTypeForString('UNITCLASS_ASSASSIN')
		eAssassinCiv = infoCiv.getCivilizationUnits(eAssassin)
		iAssassinNum = pPlayer.getUnitClassCountPlusMaking(eAssassin)
		eBeastmaster = gc.getInfoTypeForString('UNITCLASS_BEASTMASTER')
		eBeastmasterCiv = infoCiv.getCivilizationUnits(eBeastmaster)
		iBeastmasterNum = pPlayer.getUnitClassCountPlusMaking(eBeastmaster)

		eWarrior = gc.getInfoTypeForString('UNITCLASS_WARRIOR')
		eWarriorCiv = infoCiv.getCivilizationUnits(eWarrior)
		iWarriorNum = pPlayer.getUnitClassCountPlusMaking(eWarrior)
		eAxeman = gc.getInfoTypeForString('UNITCLASS_AXEMAN')
		eAxemanCiv = infoCiv.getCivilizationUnits(eAxeman)
		iAxemanNum = pPlayer.getUnitClassCountPlusMaking(eAxeman)
		eChampion = gc.getInfoTypeForString('UNITCLASS_CHAMPION')
		eChampionCiv = infoCiv.getCivilizationUnits(eChampion)
		iChampionNum = pPlayer.getUnitClassCountPlusMaking(eChampion)
		eBerserker = gc.getInfoTypeForString('UNITCLASS_BERSERKER')
		eBerserkerCiv = infoCiv.getCivilizationUnits(eBerserker)
		iBerserkerNum = pPlayer.getUnitClassCountPlusMaking(eBerserker)

		eArcher = gc.getInfoTypeForString('UNITCLASS_ARCHER')
		eArcherCiv = infoCiv.getCivilizationUnits(eArcher)
		iArcherNum = pPlayer.getUnitClassCountPlusMaking(eArcher)
		eLongbowman = gc.getInfoTypeForString('UNITCLASS_LONGBOWMAN')
		eLongbowmanCiv = infoCiv.getCivilizationUnits(eLongbowman)
		iLongbowmanNum = pPlayer.getUnitClassCountPlusMaking(eLongbowman)
		eArquebus = gc.getInfoTypeForString('UNITCLASS_ARQUEBUS')
		eArquebusCiv = infoCiv.getCivilizationUnits(eArquebus)
		iArquebusNum = pPlayer.getUnitClassCountPlusMaking(eArquebus)

		eHorseman = gc.getInfoTypeForString('UNITCLASS_HORSEMAN')
		eHorsemanCiv = infoCiv.getCivilizationUnits(eHorseman)
		iHorsemanNum = pPlayer.getUnitClassCountPlusMaking(eHorseman)
		eHorsearcher = gc.getInfoTypeForString('UNITCLASS_HORSE_ARCHER')
		eHorsearcherCiv = infoCiv.getCivilizationUnits(eHorsearcher)
		iHorsearcherNum = pPlayer.getUnitClassCountPlusMaking(eHorsearcher)
		eChariot = gc.getInfoTypeForString('UNITCLASS_CHARIOT')
		eChariotCiv = infoCiv.getCivilizationUnits(eChariot)
		iChariotNum = pPlayer.getUnitClassCountPlusMaking(eChariot)

		eAdept = gc.getInfoTypeForString('UNITCLASS_ADEPT')
		eAdeptCiv = infoCiv.getCivilizationUnits(eAdept)
		iAdeptNum = pPlayer.getUnitClassCountPlusMaking(eAdept)
		eMage = gc.getInfoTypeForString('UNITCLASS_MAGE')
		eMageCiv = infoCiv.getCivilizationUnits(eMage)
		iMageNum = pPlayer.getUnitClassCountPlusMaking(eMage)
		eMobiuswitch = gc.getInfoTypeForString('UNITCLASS_MOBIUS_WITCH')
		eMobiuswitchCiv = infoCiv.getCivilizationUnits(eMobiuswitch)
		iMobiuswitchNum = pPlayer.getUnitClassCountPlusMaking(eMobiuswitch)

		eCatapult = gc.getInfoTypeForString('UNITCLASS_CATAPULT')
		eCatapultCiv = infoCiv.getCivilizationUnits(eCatapult)
		iCatapultNum = pPlayer.getUnitClassCountPlusMaking(eCatapult)
		eCannon = gc.getInfoTypeForString('UNITCLASS_CANNON')
		eCannonCiv = infoCiv.getCivilizationUnits(eCannon)
		iCannonNum = pPlayer.getUnitClassCountPlusMaking(eCannon)

		eGalley = gc.getInfoTypeForString('UNITCLASS_GALLEY')
		eGalleyCiv = infoCiv.getCivilizationUnits(eGalley)
		iGalleyNum = pPlayer.getUnitClassCountPlusMaking(eGalley)
		eTrireme = gc.getInfoTypeForString('UNITCLASS_TRIREME')
		eTriremeCiv = infoCiv.getCivilizationUnits(eTrireme)
		iTriremeNum = pPlayer.getUnitClassCountPlusMaking(eTrireme)
		eCaravel = gc.getInfoTypeForString('UNITCLASS_CARAVEL')
		eCaravelCiv = infoCiv.getCivilizationUnits(eCaravel)
		iCaravelNum = pPlayer.getUnitClassCountPlusMaking(eCaravel)
		ePrivateer = gc.getInfoTypeForString('UNITCLASS_PRIVATEER')
		ePrivateerCiv = infoCiv.getCivilizationUnits(ePrivateer)
		iPrivateerNum = pPlayer.getUnitClassCountPlusMaking(ePrivateer)
		eGalleon = gc.getInfoTypeForString('UNITCLASS_GALLEON')
		eGalleonCiv = infoCiv.getCivilizationUnits(eGalleon)
		iGalleonNum = pPlayer.getUnitClassCountPlusMaking(eGalleon)
		eFrigate = gc.getInfoTypeForString('UNITCLASS_FRIGATE')
		eFrigateCiv = infoCiv.getCivilizationUnits(eFrigate)
		iFrigateNum = pPlayer.getUnitClassCountPlusMaking(eFrigate)
		eQueenoftheline = gc.getInfoTypeForString('UNITCLASS_QUEEN_OF_THE_LINE')
		eQueenofthelineCiv = infoCiv.getCivilizationUnits(eQueenoftheline)
		iQueenofthelineNum = pPlayer.getUnitClassCountPlusMaking(eQueenoftheline)
		eArcanebarge = gc.getInfoTypeForString('UNITCLASS_ARCANE_BARGE')
		eArcanebargeCiv = infoCiv.getCivilizationUnits(eArcanebarge)
		iArcanebargeNum = pPlayer.getUnitClassCountPlusMaking(eArcanebarge)
		eManowar = gc.getInfoTypeForString('UNITCLASS_MAN_O_WAR')
		eManowarCiv = infoCiv.getCivilizationUnits(eManowar)
		iManowarNum = pPlayer.getUnitClassCountPlusMaking(eManowar)

		eHawk = gc.getInfoTypeForString('UNITCLASS_HAWK')
		eHawkCiv = infoCiv.getCivilizationUnits(eHawk)
		iHawkNum = pPlayer.getUnitClassCountPlusMaking(eHawk)

		iCityDefendersNum = iAxemanNum + iChampionNum + iBerserkerNum + iArcherNum + iLongbowmanNum + iArquebusNum

		## City population num
		if pPlayer.getGuildPlusCounter(2) == 1:
			iPopLevel = (pCity.getPopulation())
		else:
			iPopLevel = (pCity.getPopulation() // 3)

	## Train Units assist Valid
		if not pCity.getPopulation() >= 8:
			return False
		if not CyGame().getSorenRandNum(50, "Train Unit assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
			return False
	## General Combat Units
		## Combat Naval - Construction of warships.
		"""
		iThreshold = iPopLevel * iNumCities // 16
		if iCityDefendersNum * iNumCoastalCities > (iManowarNum + iFrigateNum + iPrivateerNum + iTriremeNum) * iNumCities:
			eShipyard = gc.getInfoTypeForString('BUILDING_SHIPYARD')
			if pCity.canConstruct(eShipyard, False, False, False):
				if pCity.getBuildingProductionTurnsLeft(eShipyard, 0) < iThresholdTurn:
					if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eShipyard, -1, False, False, False, False):
						return True
			elif pCity.canTrain(eManowarCiv, False, False) and (iThreshold > 1 * (iManowarNum + iFrigateNum + iPrivateerNum)):
				if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eManowarCiv, -1, False, False, False, False):
					return True
			elif pCity.canTrain(eFrigateCiv, False, False) and (iThreshold > 1 * (iManowarNum + iFrigateNum + iPrivateerNum)):
				if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eFrigateCiv, -1, False, False, False, False):
					return True
			elif pCity.canTrain(ePrivateerCiv, False, False) and (iThreshold > 1 * (iManowarNum + iFrigateNum + iPrivateerNum + iTriremeNum)):
				if pCity.pushOrder(OrderTypes.ORDER_TRAIN, ePrivateerCiv, -1, False, False, False, False):
					return True
			elif pCity.canTrain(eTriremeCiv, False, False) and (iThreshold > 1 * (iManowarNum + iFrigateNum + iPrivateerNum + iTriremeNum)):
				if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eTriremeCiv, -1, False, False, False, False):
					return True
		"""

	## Train Land Units assist Valid
		if pCity.area().getTargetCity(ePlayer).isNone():
			return False

		## Combat Adept
		if (	pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_ARCANE')) 
				or pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_SUMMONER')) 
				or pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_CHANTER'))	):
			if iCityDefendersNum > 5 * (iMageNum + iAdeptNum):
				if pCity.canTrain(eAdeptCiv, False, False):
					if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eAdeptCiv, -1, False, False, False, False):
						return True

		## Stable - Lineage
		if eCiv == gc.getInfoTypeForString('CIVILIZATION_LINEAGE'):
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_STABLE_OF_LINEAGE'), False, False, False):
				if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_STABLE_OF_LINEAGE'), -1, False, False, False, False):
					return True
# ent >>>
		## Citadel of Light - Malakim
		if eCiv == gc.getInfoTypeForString('CIVILIZATION_MALAKIM'):
			if iThreat > 50:
				if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_CITADEL_OF_LIGHT'), False, False, False):
					if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_CITADEL_OF_LIGHT'), -1, False, False, False, False):
						return True

		## Hall of Mirrors - Balseraphs
		if eCiv == gc.getInfoTypeForString('CIVILIZATION_BALSERAPHS'):
			if iThreat > 50:
				if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_HALL_OF_MIRRORS'), False, False, False):
					if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_HALL_OF_MIRRORS'), -1, False, False, False, False):
						return True

		## Dragon's Nest - Altair
		if eCiv == gc.getInfoTypeForString('CIVILIZATION_ALTAIR'):
			if pCity.canConstruct(gc.getInfoTypeForString('BUILDING_DRAGONS_NEST'), False, False, False):
				if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, gc.getInfoTypeForString('BUILDING_DRAGONS_NEST'), -1, False, False, False, False):
					return True

		## Vampire - Calabim
		if eCiv == gc.getInfoTypeForString('CIVILIZATION_CALABIM') and pPlayer.isHasTech(gc.getInfoTypeForString('TECH_FEUDALISM')):
			eGovernorsManor = gc.getInfoTypeForString('BUILDING_GOVERNORS_MANOR')
			if pCity.isHasActiveBuilding(eGovernorsManor):
				if iCityDefendersNum > 4 * (iAxemanNum + iChampionNum + iBerserkerNum):
					if pCity.canTrain(eChampionCiv, False, False):
						if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eChampionCiv, -1, False, False, False, False):
							return True
			elif pCity.canConstruct(eGovernorsManor, False, False, False):
				if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eGovernorsManor, -1, False, False, False, False):
					return True

		## Combat Siege
		if pTeam.getAtWarCount(True) > 0 and cf.AI_getWarSuccessCapitulationRatio(ePlayer) > 50:
			if iCityDefendersNum > 8 * (iCatapultNum + iCannonNum):
				eSiegeWorkshop = infoCiv.getCivilizationBuildings(gc.getInfoTypeForString('BUILDINGCLASS_SIEGE_WORKSHOP'))
				if eSiegeWorkshop == BuildingTypes.NO_BUILDING or pCity.isHasActiveBuilding(eSiegeWorkshop):
					if pCity.canTrain(eCannonCiv, False, False):
						if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eCannonCiv, -1, False, False, False, False):
							return True
					elif pCity.canTrain(eCatapultCiv, False, False):
						if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eCatapultCiv, -1, False, False, False, False):
							return True
				elif eSiegeWorkshop != BuildingTypes.NO_BUILDING and pCity.canConstruct(eSiegeWorkshop, False, False, False):
					if pCity.pushOrder(OrderTypes.ORDER_CONSTRUCT, eSiegeWorkshop, -1, False, False, False, False):
						return True

		## Combat Melee
		if eCiv == gc.getInfoTypeForString('CIVILIZATION_DOVIELLO'):
			if iCityDefendersNum > 2 * (iAxemanNum + iChampionNum + iBerserkerNum):
				if pCity.canTrain(eBerserkerCiv, False, False):
					if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eBerserkerCiv, -1, False, False, False, False):
						return True
				elif pCity.canTrain(eChampionCiv, False, False):
					if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eChampionCiv, -1, False, False, False, False):
						return True
				elif pCity.canTrain(eAxemanCiv, False, False):
					if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eAxemanCiv, -1, False, False, False, False):
						return True

# ent <<<

		## Combat Archer
		if eCiv == gc.getInfoTypeForString('CIVILIZATION_LJOSALFAR'):
			if iCityDefendersNum > 3 * (iArcherNum + iLongbowmanNum):
				if pCity.canTrain(eLongbowmanCiv, False, False):
					if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eLongbowmanCiv, -1, False, False, False, False):
						return True

		## Combat Mounted
		if eCiv in (gc.getInfoTypeForString('CIVILIZATION_HIPPUS'), gc.getInfoTypeForString('CIVILIZATION_XOTH')):
			if iCityDefendersNum > 2 * (iHorsemanNum + iHorsearcherNum):
				if pCity.canTrain(eHorsearcherCiv, False, False):
					if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eHorsearcherCiv, -1, False, False, False, False):
						return True

		## Combat Recon
		if iCityDefendersNum > 6 * (iBeastmasterNum + iRangerNum + iHunterNum + iAssassinNum):
			if pCity.canTrain(eHunterCiv, False, False):
				if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eHunterCiv, -1, False, False, False, False):
					return True
		if iCityDefendersNum > 4 * (iBeastmasterNum + iRangerNum + iHunterNum):

			if pCity.canTrain(eBeastmasterCiv, False, False):
				if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eBeastmasterCiv, -1, False, False, False, False):
					return True
			elif pCity.canTrain(eRangerCiv, False, False):
				if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eRangerCiv, -1, False, False, False, False):
					return True
		if iCityDefendersNum > 6 * (iAssassinNum):
			if pCity.canTrain(eAssassinCiv, False, False):
				if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eAssassinCiv, -1, False, False, False, False):
					return True

	## National and Combat Melee
		## National Units - General
		if pPlayer.getGuildPlusCounter(2) <= 1 and not gc.getGame().isOption(gc.getInfoTypeForString('GAMEOPTION_AI_NO_UNIT_LIMITATION')):
			for eUnitClass in range(gc.getNumUnitClassInfos()):
				if isNationalUnitClass(eUnitClass):
					eUniqueUnit = infoCiv.getCivilizationUnits(eUnitClass)
					if CyGame().getSorenRandNum(300, "Train Unit assist") < (100 - pCity.findYieldRateRank(YieldTypes.YIELD_PRODUCTION) * 10):
						if eUniqueUnit != -1 and pCity.canTrain(eUniqueUnit, False, False):
# ent >>>
							"""
							if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eUniqueUnit, -1, False, False, False, False):
								return True
							"""
							if pCity.getUnitProductionTurnsLeft(eUniqueUnit, 0) < iThresholdTurn:
								if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eUniqueUnit, -1, False, False, False, False):
									return True
# ent <<<
		## Luchuirp
		if eCiv == gc.getInfoTypeForString('CIVILIZATION_LUCHUIRP'):
			eClockwork = gc.getInfoTypeForString('UNIT_CLOCKWORK_GOLEM')
			eIron = gc.getInfoTypeForString('UNIT_IRON_GOLEM')
			eGargoyle = gc.getInfoTypeForString('UNIT_GARGOYLE')
			eWood = gc.getInfoTypeForString('UNIT_WOOD_GOLEM')

			if pCity.canTrain(eClockwork, False, False) and (iPopLevel * iNumCities) > (8 * (iBerserkerNum)):
				if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eClockwork, -1, False, False, False, False):
					return True
			elif pCity.canTrain(eIron, False, False) and (iPopLevel * iNumCities) > (8 * (iChampionNum + iBerserkerNum)):
				if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eIron, -1, False, False, False, False):
					return True
			elif pCity.canTrain(eGargoyle, False, False) and (iPopLevel * iNumCities) > (8 * (iLongbowmanNum + iBerserkerNum)):
				if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eGargoyle, -1, False, False, False, False):
					return True
			elif pCity.canTrain(eWood, False, False) and (iPopLevel * iNumCities) > (8 * (iAxemanNum + iLongbowmanNum + iChampionNum + iBerserkerNum)):
				if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eWood, -1, False, False, False, False):
					return True

		## Nival
		elif eCiv == gc.getInfoTypeForString('CIVILIZATION_NIVAL'):
			eIcestatue = gc.getInfoTypeForString('UNIT_ICE_STATUE')
			eFrost = gc.getInfoTypeForString('UNIT_FROST_GIANT')

			if pCity.canTrain(eIcestatue, False, False) and (iPopLevel * iNumCities) > (8 * (iBerserkerNum)):
				if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eIcestatue, -1, False, False, False, False):
					return True
			elif pCity.canTrain(eFrost, False, False) and (iPopLevel * iNumCities) > (8 * (iChampionNum + iBerserkerNum)):
				if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eFrost, -1, False, False, False, False):
					return True

		## Nougbii
		elif eCiv == gc.getInfoTypeForString('CIVILIZATION_NOUGBII'):
			eWandern = gc.getInfoTypeForString('UNIT_WANDERN_PANTZER')
			eTank = gc.getInfoTypeForString('UNIT_TANK_GOLEM')

			if pCity.canTrain(eWandern, False, False) and (iPopLevel * iNumCities) > (8 * (iBerserkerNum)):
				if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eWandern, -1, False, False, False, False):
					return True
			elif pCity.canTrain(eTank, False, False) and (iPopLevel * iNumCities) > (8 * (iChampionNum + iBerserkerNum)):
				if pCity.pushOrder(OrderTypes.ORDER_TRAIN, eTank, -1, False, False, False, False):
					return True

#Kaijin <<<
# ent >>>
		if pPlayer.getGuildPlusCounter(2) == 1:
			if CyGame().getSorenRandNum(100, "Choose Invader Unit") < 40:
				if pCity.AI_chooseInvaderUnit(False):
					return True
# ent <<<

		return False

	def AI_unitUpdate(self,argsList):
	# USE_ON_UNIT_UPDATE_CALLBACK turn off
		pUnit = argsList[0]
		pPlot = pUnit.plot()

		iPlayer = pUnit.getOwner()
		pPlayer = gc.getPlayer(iPlayer)
		eTeam = gc.getTeam(pPlayer.getTeam())
		iUnitClass = pUnit.getUnitClassType()
		AIType = pUnit.getUnitAIType()

		iWar = 1
		if eTeam.getAtWarCount(True) == 0:
			iWar = 0

		"""
		if pUnit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_GIANT_SPIDER'):
			iX = pUnit.getX()
			iY = pUnit.getY()
			for iiX in xrange(iX-1, iX+2, 1):
				for iiY in xrange(iY-1, iY+2, 1):
					pLoopPlot = CyMap().plot(iiX,iiY)
					for i in xrange(pLoopPlot.getNumUnits()):
						if pLoopPlot.getUnit(i).getOwner() != pUnit.getOwner():
							return 0
			pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, False, False, MissionAITypes.NO_MISSIONAI, pUnit.plot(), pUnit)
			return 1

		elif pUnit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_ACHERON'):
			if pPlot.isVisibleEnemyUnit(pUnit.getOwner()):
				pUnit.cast(gc.getInfoTypeForString('SPELL_BREATH_FIRE'))

		iImprovement = pPlot.getImprovementType()
		if iImprovement != ImprovementTypes.NO_IMPROVEMENT:
			if iImprovement in (gc.getInfoTypeForString('IMPROVEMENT_BARROW'), gc.getInfoTypeForString('IMPROVEMENT_RUINS'), gc.getInfoTypeForString('IMPROVEMENT_HELLFIRE')):
				if not pUnit.isAnimal():
					if pPlot.getNumUnits() - pPlot.getNumAnimalUnits() == 1:
						pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, False, False, MissionAITypes.MISSIONAI_GUARD_BONUS, pUnit.plot(), pUnit)
						return 1
			if (iImprovement == gc.getInfoTypeForString('IMPROVEMENT_BEAR_DEN') or iImprovement == gc.getInfoTypeForString('IMPROVEMENT_LION_DEN')):
				if pUnit.isAnimal():
					if pPlot.getNumAnimalUnits() == 1:
						pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, False, False, MissionAITypes.MISSIONAI_GUARD_BONUS, pUnit.plot(), pUnit)
						return 1
			if iImprovement == gc.getInfoTypeForString('IMPROVEMENT_GOBLIN_FORT'):
				if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ARCHER'):
					pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, False, False, MissionAITypes.MISSIONAI_GUARD_BONUS, pUnit.plot(), pUnit)
					return 1
				if not pUnit.isAnimal():
					if pPlot.getNumUnits() - pPlot.getNumAnimalUnits() <= 2:
						pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, False, False, MissionAITypes.MISSIONAI_GUARD_BONUS, pUnit.plot(), pUnit)
						return 1
		"""


# Kaijin OAC >>>
		"""
	##蛮族
		if iPlayer == gc.getBARBARIAN_PLAYER():
			## 追加の巣窟の守備ユニット
			iImprovement = pPlot.getImprovementType()
			if iImprovement != ImprovementTypes.NO_IMPROVEMENT:
				if iImprovement in (gc.getInfoTypeForString('IMPROVEMENT_HAUNTED_RUINS'), gc.getInfoTypeForString('IMPROVEMENT_DARKGATE'), gc.getInfoTypeForString('IMPROVEMENT_DARKGATE2')):
					if not pUnit.isAnimal():
						if pPlot.getNumUnits() - pPlot.getNumAnimalUnits() == 1:
							pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, False, False, MissionAITypes.MISSIONAI_GUARD_BONUS, pUnit.plot(), pUnit)
							return 1
				if iImprovement in (gc.getInfoTypeForString('IMPROVEMENT_DEN_WOLF'), gc.getInfoTypeForString('IMPROVEMENT_DEN_GORILLA'), gc.getInfoTypeForString('IMPROVEMENT_DEN_TIGER'), 
									gc.getInfoTypeForString('IMPROVEMENT_DEN_SPIDER'), gc.getInfoTypeForString('IMPROVEMENT_HILLGIANT_STEADING'), gc.getInfoTypeForString('IMPROVEMENT_GRIFFIN_NEST'), gc.getInfoTypeForString('IMPROVEMENT_TROLL_CAVE')):
					if pUnit.isAnimal():
						if pPlot.getNumAnimalUnits() == 1:
							pUnit.getGroup().pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, False, False, MissionAITypes.MISSIONAI_GUARD_BONUS, pUnit.plot(), pUnit)
							return 1
			## リザードマンと狼の騎乗兵
			iGameTurn = CyGame().getGameTurn()
			iOrthusTurn = cyFlatValue(75, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
			if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_LIZARDMAN') or pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_WOLF_RIDER'):
				if iGameTurn >= iOrthusTurn:
					if AIType != UnitAITypes.UNITAI_ANIMAL:
						pUnit.setUnitAIType(UnitAITypes.UNITAI_ANIMAL)
				else:
					if AIType == UnitAITypes.UNITAI_ANIMAL:
						pUnit.setUnitAIType(UnitAITypes.UNITAI_ATTACK)
	## 海賊
		if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_PIRATES'):
			if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_NAVAL') and not AIType == UnitAITypes.UNITAI_PIRATE_SEA:
				pUnit.setUnitAIType(UnitAITypes.UNITAI_PIRATE_SEA)
				return 1
			if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_MELEE'):
				if AIType != UnitAITypes.UNITAI_PILLAGE:
					pUnit.setUnitAIType(UnitAITypes.UNITAI_PILLAGE)
				if pPlot.isOwned():
					pPlotOwner = gc.getPlayer(pPlot.getOwner())
					if pPlot.isWater() and (pPlotOwner.getCivilizationType() != gc.getInfoTypeForString('CIVILIZATION_LANUN') and pPlotOwner.getCivilizationType() != gc.getInfoTypeForString('CIVILIZATION_XOTH')):
						iX = pPlot.getX()
						iY = pPlot.getY()
						for iiX in xrange(iX-1, iX+2, 1):
							for iiY in xrange(iY-1, iY+2, 1):
								pLoopPlot = CyMap().plot(iiX,iiY)
								if pLoopPlot != pPlot and pLoopPlot.isCoastalLand() and not pLoopPlot.isWater():
									pGroup = pUnit.getGroup()
									pGroup.clearMissionQueue()
									pGroup.pushMission(MissionTypes.MISSION_MOVE_TO, 0, 0, 0, False, False, MissionAITypes.NO_MISSIONAI, pLoopPlot, pUnit)
									pGroup.pushMoveToMission(pLoopPlot.getX(), pLoopPlot.getY())
									return 1
		"""
# Kaijin OAC <<<

#英雄強化AI
# Kaijin >>>

	##国籍秘匿関連
		"""
		#国籍宣言
		if pUnit.canCast(gc.getInfoTypeForString('SPELL_DECLARE_NATIONALITY'), False):
#			if not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_HIDDEN')) and not pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_INVISIBLE')):
			if not pUnit.isInvisible(gc.getPlayer(gc.getGame().getActivePlayer()).getTeam(), True):
				if pUnit.getReligion() == gc.getInfoTypeForString('RELIGION_COUNCIL_OF_ESUS'):
					pUnit.cast(gc.getInfoTypeForString('SPELL_DECLARE_NATIONALITY'))
					pUnit.setHasCasted(True)
		"""
		"""
		#仮面
#		if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_HIDDEN')) or pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_INVISIBLE')):
		if pUnit.isInvisible(gc.getPlayer(gc.getGame().getActivePlayer()).getTeam(), True):
			if pUnit.canCast(gc.getInfoTypeForString('SPELL_MASK'), False):
				pUnit.cast(gc.getInfoTypeForString('SPELL_MASK'))
				pUnit.setHasCasted(True)
			elif pUnit.canCast(gc.getInfoTypeForString('SPELL_MASK_ECHIGO'), False):
				pUnit.cast(gc.getInfoTypeForString('SPELL_MASK_ECHIGO'))
				pUnit.setHasCasted(True)
		"""
		"""
		#国籍秘匿＆隠密のユニット
		if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_HIDDEN_NATIONALITY')):
#			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_HIDDEN')) or pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_INVISIBLE')):
			if pUnit.isInvisible(gc.getPlayer(gc.getGame().getActivePlayer()).getTeam(), True):
				if AIType != UnitAITypes.UNITAI_ATTACK:
					pUnit.setUnitAIType(UnitAITypes.UNITAI_ATTACK)
		"""
# ent >>>
		"""
		move to UnitInfos
	##冒険者
		#AI更新
		if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_ADVENTURER'):
			if not AIType == UnitAITypes.UNITAI_CITY_SPECIAL:
				pUnit.setUnitAIType(UnitAITypes.UNITAI_CITY_SPECIAL)
		"""
# ent <<<
# Kaijin <<<
# ent >>>
		"""
		move to CvUnitAIInterface
	##バルナクサス
		if pUnit.getUnitType() == gc.getInfoTypeForString('UNIT_BARNAXUS'):
			bReserve = 0
	##昇進したら首都で隠居
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_COMBAT2')):
				bReserve = 1
			if bReserve == 1:
				pMovePlotX = pPlayer.getCapitalCity().getX()
				pMovePlotY = pPlayer.getCapitalCity().getY()
				if pUnit.getX() == pMovePlotX and pUnit.getY() == pMovePlotY:
					if AIType != UnitAITypes.UNITAI_RESERVE:
						pUnit.setUnitAIType(UnitAITypes.UNITAI_RESERVE)
					pGroup = pUnit.getGroup()
					pGroup.clearMissionQueue()
					pGroup.pushMission(MissionTypes.MISSION_SKIP, 0, 0, 0, False, False, MissionAITypes.NO_MISSIONAI, pUnit.plot(), pUnit)
					return 1
				else:
					pGroup = pUnit.getGroup()
					pGroup.clearMissionQueue()
					pGroup.pushMoveToMission(pMovePlotX, pMovePlotY)
					pUnit.finishMoves()
					return 1
		"""
# ent <<<

		"""
		## ラーナ - 魂の飢餓
		if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_RARNA') and pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_SOUL_HUNGER')):
			if AIType != UnitAITypes.UNITAI_ATTACK:
				pUnit.setUnitAIType(UnitAITypes.UNITAI_ATTACK)
		"""

		"""
		## ニバル - いたずら
		if iWar == 0:
			if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_NIVAL') and eTeam.isHasTech(gc.getInfoTypeForString('TECH_BRONZE_WORKING')):
				if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_FROSTLING')) and (AIType == UnitAITypes.UNITAI_ATTACK or AIType == UnitAITypes.UNITAI_EXPLORE):
					if pUnit.canCast(gc.getInfoTypeForString('SPELL_PRANK_NIVAL'), False):
						pUnit.cast(gc.getInfoTypeForString('SPELL_PRANK_NIVAL'))
						pUnit.setHasCasted(True)
					else:
					#プロット移動
						pBestPlot = -1
						iBestPlot = 0
						for i in xrange (CyMap().numPlots()):
							pLoopPlot = CyMap().plotByIndex(i)
							iPlot = 0
							if pLoopPlot.getOwner() != iPlayer and pLoopPlot.isPeak() == False and pLoopPlot.isWater() == False and pUnit.canMoveInto(pLoopPlot, False, False, False) == True:
					#実行可能地形
								iXprank = pPlot.getX()
								iYprank = pPlot.getY()
								for iiXprank in xrange(iXprank-1, iXprank+2, 1):
									for iiYprank in xrange(iYprank-1, iYprank+2, 1):
										if not (iiXprank == iXprank and iiYprank == iYprank):
											pLoopPlotPrank = CyMap().plot(iiXprank,iiYprank)
											if pUnit.getOwner() == pLoopPlotPrank.getOwner():
												iPlot += 1
					#近場優先
							if iPlot != 0:
								iX2 = pLoopPlot.getX()
								iY2 = pLoopPlot.getY()
								for iiX2 in xrange(iX2-4, iX2+5, 1):
									for iiY2 in xrange(iY2-4, iY2+5, 1):
										if pPlot.getX() == iiX2 and pPlot.getY() == iiY2:
											iPlot += 10
							if iPlot > iBestPlot:
								iBestPlot = iPlot
								pBestPlot = pLoopPlot
						if pBestPlot != -1:
							pGroup = pUnit.getGroup()
							pGroup.clearMissionQueue()
							pGroup.pushMoveToMission(pBestPlot.getX(), pBestPlot.getY())
							pUnit.finishMoves()
							return 1
		"""

# Kaijin End
		return False

	def AI_doWar(self,argsList):
		eTeam = argsList[0]
		return False

	def AI_doDiplo(self,argsList):
		ePlayer = argsList[0]
		return False

	def calculateScore(self,argsList):
		ePlayer = argsList[0]
		bFinal = argsList[1]
		bVictory = argsList[2]

		iPopulationScore = CvUtil.getScoreComponent(gc.getPlayer(ePlayer).getPopScore(), gc.getGame().getInitPopulation(), gc.getGame().getMaxPopulation(), gc.getDefineINT("SCORE_POPULATION_FACTOR"), True, bFinal, bVictory)
		iLandScore = CvUtil.getScoreComponent(gc.getPlayer(ePlayer).getLandScore(), gc.getGame().getInitLand(), gc.getGame().getMaxLand(), gc.getDefineINT("SCORE_LAND_FACTOR"), True, bFinal, bVictory)
		iTechScore = CvUtil.getScoreComponent(gc.getPlayer(ePlayer).getTechScore(), gc.getGame().getInitTech(), gc.getGame().getMaxTech(), gc.getDefineINT("SCORE_TECH_FACTOR"), True, bFinal, bVictory)
		iWondersScore = CvUtil.getScoreComponent(gc.getPlayer(ePlayer).getWondersScore(), gc.getGame().getInitWonders(), gc.getGame().getMaxWonders(), gc.getDefineINT("SCORE_WONDER_FACTOR"), False, bFinal, bVictory)
		return int(iPopulationScore + iLandScore + iWondersScore + iTechScore)

##--------	Advanced Rules: Added by Denev 2010/02/29
	def calculateTechScore(self,argsList):
		ePlayer = argsList[0]
		bFinal = argsList[1]
		bVictory = argsList[2]

		iTechScore = CvUtil.getScoreComponent(gc.getPlayer(ePlayer).getTechScore(), gc.getGame().getInitTech(), gc.getGame().getMaxTech(), gc.getDefineINT("SCORE_TECH_FACTOR"), True, bFinal, bVictory)
		return int(iTechScore)
##--------	Advanced Rules: End Add

	def doHolyCity(self):
		return False

	def doHolyCityTech(self,argsList):
		eTeam = argsList[0]
		ePlayer = argsList[1]
		eTech = argsList[2]
		bFirst = argsList[3]
		return False

	def doGold(self,argsList):
		ePlayer = argsList[0]
		return False

	def doResearch(self,argsList):
		ePlayer = argsList[0]
		return False

	def doGoody(self,argsList):
		ePlayer = argsList[0]
		pPlot = argsList[1]
		pUnit = argsList[2]
		return False

	def doGrowth(self,argsList):
		pCity = argsList[0]
		return False

	def doProduction(self,argsList):
		pCity = argsList[0]
		return False

	def doCulture(self,argsList):
		pCity = argsList[0]
		return False

	def doPlotCulture(self,argsList):
		pCity = argsList[0]
		bUpdate = argsList[1]
		ePlayer = argsList[2]
		iCultureRate = argsList[3]
		return False

	def doReligion(self,argsList):
		pCity = argsList[0]
		return False

	def cannotSpreadReligion(self,argsList):
		iOwner, iUnitID, iReligion, iX, iY = argsList[0]
		return False

	def doGreatPeople(self,argsList):
		pCity = argsList[0]
		return False

	def doMeltdown(self,argsList):
		pCity = argsList[0]
		return False

	def doReviveActivePlayer(self,argsList):
		"allows you to perform an action after an AIAutoPlay"
		iPlayer = argsList[0]
		return False

	def doPillageGold(self, argsList):
		"controls the gold result of pillaging"
		pPlot = argsList[0]
		pUnit = argsList[1]

		iPillageGold = 0
		iPillageGold = CyGame().getSorenRandNum(gc.getImprovementInfo(pPlot.getImprovementType()).getPillageGold(), "Pillage Gold 1")
		iPillageGold += CyGame().getSorenRandNum(gc.getImprovementInfo(pPlot.getImprovementType()).getPillageGold(), "Pillage Gold 2")

		iPillageGold += (pUnit.getPillageChange() * iPillageGold) / 100

		return iPillageGold

	def doCityCaptureGold(self, argsList):
		"controls the gold result of capturing a city"

		pOldCity = argsList[0]
##--------	Advanced Rules: Added by Denev 2012/04/14
		eNewPlayer = argsList[1]
##--------	Advanced Rules: End Add

		iCaptureGold = 0

		iCaptureGold += gc.getDefineINT("BASE_CAPTURE_GOLD")
		iCaptureGold += (pOldCity.getPopulation() * gc.getDefineINT("CAPTURE_GOLD_PER_POPULATION"))
		iCaptureGold += CyGame().getSorenRandNum(gc.getDefineINT("CAPTURE_GOLD_RAND1"), "Capture Gold 1")
		iCaptureGold += CyGame().getSorenRandNum(gc.getDefineINT("CAPTURE_GOLD_RAND2"), "Capture Gold 2")

		if (gc.getDefineINT("CAPTURE_GOLD_MAX_TURNS") > 0):
			iCaptureGold *= cyIntRange((CyGame().getGameTurn() - pOldCity.getGameTurnAcquired()), 0, gc.getDefineINT("CAPTURE_GOLD_MAX_TURNS"))
			iCaptureGold /= gc.getDefineINT("CAPTURE_GOLD_MAX_TURNS")

##--------	Advanced Rules: Added by Denev 2012/04/14
		if gc.getPlayer(eNewPlayer).isCivic(gc.getInfoTypeForString('CIVIC_CONQUEST')):
			iCaptureGold *= 2
#			pOldCity.changePopulation(-1)
##--------	Advanced Rules: End Add

		return iCaptureGold

	def citiesDestroyFeatures(self,argsList):
		iX, iY= argsList
		return True

	def canFoundCitiesOnWater(self,argsList):
		iX, iY= argsList
		return False

	def doCombat(self,argsList):
		pSelectionGroup, pDestPlot = argsList
		return False

	def getConscriptUnitType(self, argsList):
		iPlayer = argsList[0]
		iConscriptUnitType = -1 #return this with the value of the UNIT TYPE you want to be conscripted, -1 uses default system

		return iConscriptUnitType

	def getCityFoundValue(self, argsList):
		iPlayer, iPlotX, iPlotY = argsList
		iFoundValue = -1 # Any value besides -1 will be used

		return iFoundValue

	def canPickPlot(self, argsList):
		pPlot = argsList[0]
		return True

	def getUnitCostMod(self, argsList):
		iPlayer, iUnit = argsList
		iCostMod = -1 # Any value > 0 will be used

		return iCostMod

	def getBuildingCostMod(self, argsList):
		iPlayer, iCityID, iBuilding = argsList
		pPlayer = gc.getPlayer(iPlayer)
		pCity = pPlayer.getCity(iCityID)

#Kaijin >>>
#		iCostMod = -1 # Any value > 0 will be used
		iCostMod = 100

		if iBuilding == gc.getInfoTypeForString('BUILDING_GAMBLING_HOUSE'):
			if pPlayer.isGamblingRing():
##--------	Unofficial Bug Fix: Modified by Denev 2011/09/18
				"""
#				iCostMod = gc.getBuildingInfo(iBuilding).getProductionCost() / 4
				iCostMod = 100 // 4
				"""
				iCostMod = iCostMod // 4
##--------	Unofficial Bug Fix: End Modify

	## CivGoldEmpires - Trait Construction [Old:Trait Hillman] - reduction cost
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_CONSTRUCTION')):
			iCostMod = iCostMod * 4 // 5

	## AI Handicap
		if not pPlayer.isHuman():
			leMilitaryBuildingClasses = [	gc.getInfoTypeForString('BUILDINGCLASS_HUNTING_LODGE'),
											gc.getInfoTypeForString('BUILDINGCLASS_TRAINING_YARD'),
											gc.getInfoTypeForString('BUILDINGCLASS_ARCHERY_RANGE'),
											gc.getInfoTypeForString('BUILDINGCLASS_STABLE'),
											gc.getInfoTypeForString('BUILDINGCLASS_MAGE_GUILD'),
											gc.getInfoTypeForString('BUILDINGCLASS_SIEGE_WORKSHOP'),
											gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_EMPYREAN'),
											gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_LEAVES'),
											gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_KILMORPH'),
											gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_ORDER'),
											gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_OVERLORDS'),
											gc.getInfoTypeForString('BUILDINGCLASS_TEMPLE_OF_THE_VEIL'),
											gc.getInfoTypeForString('BUILDINGCLASS_COMMAND_POST'),
											gc.getInfoTypeForString('BUILDINGCLASS_GROVE'),
											gc.getInfoTypeForString('BUILDINGCLASS_SHIPYARD')	]
			if gc.getBuildingInfo(iBuilding).getBuildingClassType() in leMilitaryBuildingClasses:
				iCostMod = iCostMod // 4

		if iCostMod == 100:
			iCostMod = -1
#Kaijin <<<

		return iCostMod

##--------	Advanced Rules: Added by ent
	def getProjectCostMod(self, argsList):
		iPlayer, iCityID, iProject = argsList
		pPlayer = gc.getPlayer(iPlayer)
		pCity = pPlayer.getCity(iCityID)

#		iCostMod = -1 # Any value > 0 will be used
		iCostMod = 100

##--------	Advanced Winter Projects: Added by ent
	## Illians - Winter Projects
		def isWinterProject(eProject):
			if gc.getProjectInfo(eProject).getPrereqCivilization() == en.eCivilizationIllians:
				return True
			return False

		if isWinterProject(iProject):
			iIlliansCostMod = -10 # Max -60
			for eLoopProjests in xrange(gc.getNumProjectInfos()):
				if isWinterProject(eLoopProjests):
					if gc.getGame().isProjectMaxedOut(eLoopProjests, 0):
						iCostMod += iIlliansCostMod
			if pPlayer.isCivic(gc.getInfoTypeForString('CIVIC_FAITH_OF_WINTER')):
				iCostMod += iIlliansCostMod

##--------	Advanced Winter Projects: End Add

##--------	Advanced Convert Life Force: Added by ent
	## Aristrakh - Death pact
		if iProject in [gc.getInfoTypeForString('PROJECT_DEATH_PACT_1'),
						gc.getInfoTypeForString('PROJECT_DEATH_PACT_2'),
						gc.getInfoTypeForString('PROJECT_DEATH_PACT_3'),
						gc.getInfoTypeForString('PROJECT_DEATH_PACT_4'),
						gc.getInfoTypeForString('PROJECT_DEATH_PACT_5')]:
			iUnhealthRate = -1 * pCity.healthRate(False, 0)
			if iUnhealthRate > 0:
				iUnHealthCostMod = 10
				iCostMod += iUnhealthRate * iUnHealthCostMod
##--------	Advanced Convert Life Force: End Add

		if iCostMod == 100:
			iCostMod = -1

		return iCostMod
##--------	Advanced Rules: End Add

	def canUpgradeAnywhere(self, argsList):
		pUnit = argsList

		bCanUpgradeAnywhere = 0

		return bCanUpgradeAnywhere

	def getWidgetHelp(self, argsList):
		eWidgetType, iData1, iData2, bOption = argsList

		return u""

	def getUpgradePriceOverride(self, argsList):
		iPlayer, iUnitID, iUnitTypeUpgrade = argsList

		return -1	# Any value 0 or above will be used

	def getExperienceNeeded(self, argsList):
		# use this function to set how much experience a unit needs
		iLevel, iOwner = argsList

		iExperienceNeeded = 0

		# regular epic game experience
		iExperienceNeeded = iLevel * iLevel + 1

		iModifier = gc.getPlayer(iOwner).getLevelExperienceModifier()
		if (0 != iModifier):
			iExperienceNeeded += (iExperienceNeeded * iModifier + 99) / 100   # ROUND UP

		return iExperienceNeeded

##--------	Unofficial Bug Fix: Added by Denev 2009/12/31
	def applyBuildEffects(self, argsList):
		pUnit, pCity = argsList
# Kaijin >>>
		pPlayer = gc.getPlayer(pUnit.getOwner())
		eTeam = gc.getTeam(pPlayer.getTeam())
# Kaijin <<<
		"""
		"Moved to XML"
		if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_CHANCEL_OF_GUARDIANS')) > 0:
			if not pUnit.noDefensiveBonus() and pUnit.baseCombatStrDefense() > 0:
				if CyGame().getSorenRandNum(100, "Chancel of Guardians") < 20:
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_DEFENSIVE'), True)
		"""

		if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_CAVE_OF_ANCESTORS')) > 0:
			if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_ADEPT'):
				iNumManaKinds = 0
				for iBonus in xrange(gc.getNumBonusInfos()):
					if pCity.hasBonus(iBonus):
						if gc.getBonusInfo(iBonus).getBonusClassType() == gc.getInfoTypeForString('BONUSCLASS_MANA'):
							iNumManaKinds += 1
				if iNumManaKinds > 0:
					pUnit.changeExperience(iNumManaKinds, -1, False, False, False)

		if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_ASYLUM')) > 0:
			if pUnit.isAlive():
				if not isWorldUnitClass(pUnit.getUnitClassType()):
					if CyGame().getSorenRandNum(100, "Asylum") < 10:
						pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_CRAZED'), True)
						pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_ENRAGED'), True)

# Kaijin >>>
		## Ys - Ark of Napishtim.
		if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_ARK_OF_NAPISHTIM')) > 0:
			liSelectedPromotion = []

			liChosenPromRank1 = []
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING1')):
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
					if not pUnit.isHasPromotion(iPromotion):
						liChosenPromRank1.append(iPromotion)
				liChosenPromRank1.sort()
				liSelectedPromotion.append(liChosenPromRank1.pop( CyGame().getSorenRandNum(len(liChosenPromRank1), "Ark of napishtim") ))
				liSelectedPromotion.sort()

			liChosenPromRank2 = []
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING2')):
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
					if not pUnit.isHasPromotion(iPromotion):
						liChosenPromRank2.append(iPromotion)
				liChosenPromRank2.sort()
				liSelectedPromotion.append(liChosenPromRank2.pop( CyGame().getSorenRandNum(len(liChosenPromRank2), "Ark of napishtim") ))
				liSelectedPromotion.sort()

			liChosenPromRank3 = []
			if pUnit.isHasPromotion(gc.getInfoTypeForString('PROMOTION_CHANNELING3')):
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
					if not pUnit.isHasPromotion(iPromotion):
						liChosenPromRank3.append(iPromotion)
				liChosenPromRank3.sort()
				liSelectedPromotion.append(liChosenPromRank3.pop( CyGame().getSorenRandNum(len(liChosenPromRank3), "Ark of napishtim") ))
				liSelectedPromotion.sort()

			if len(liSelectedPromotion) > 0:
				for iSelectedPromotion in liSelectedPromotion:
					if not pUnit.isHasPromotion(iSelectedPromotion):
						pUnit.setHasPromotion(iSelectedPromotion, True)

		## Despiel - Unit is mutated by espiel Citizens.
		if pCity.getNumRealBuilding(gc.getInfoTypeForString('BUILDING_DESPIEL_CITIZENS')) > 0:
			if pUnit.isAlive():
				if pUnit.getUnitCombatType() != gc.getInfoTypeForString('UNITCOMBAT_MELEE'):
					if CyGame().getSorenRandNum(100, "Despiel Citizens") < 10:
						pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_KAIJIN_MUTANT'), True)

# Kaijin <<<
		eRace = pUnit.getRace()
		if eRace == gc.getInfoTypeForString('PROMOTION_GOLEM'):
			if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_BLASTING_WORKSHOP')) > 0:
# ent >>>
#				pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FIRE1'), True)
				if pUnit.getUnitType() not in (gc.getInfoTypeForString('UNIT_WOOD_GOLEM'), gc.getInfoTypeForString('UNIT_MUD_GOLEM')):
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FIRE1'), True)
# ent <<<
			if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_PALLENS_ENGINE')) > 0:
				pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_PERFECT_SIGHT'), True)
# Kaijin >>>
				pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MAGIC_RESISTANCE'), True)
# Kaijin <<<
			if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_ADULARIA_CHAMBER')) > 0:
# Kaijin >>>
#				pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_HIDDEN'), True)
				pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_INVISIBLE'), True)
# Kaijin <<<

		elif eRace == gc.getInfoTypeForString('PROMOTION_DWARF'):
			if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_BREWERY')) > 0:
				pUnit.changeExperience(2, -1, False, False, False)

		elif eRace == gc.getInfoTypeForString('PROMOTION_DEMON'):
			if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_DEMONS_ALTAR')) > 0:
				pUnit.changeExperience(2, -1, False, False, False)

# Kaijin >>>
		elif eRace == gc.getInfoTypeForString('PROMOTION_UNDEAD'):
			if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_DARK_ALCHEMY_LAB')) > 0:
				pUnit.changeExperience(CyGame().getSorenRandNum(9, "Undead Experience"), -1, False, False, False)

		elif eRace == gc.getInfoTypeForString('PROMOTION_KAIJIN_RACE'):
			if pCity.getNumBuilding(gc.getInfoTypeForString('BUILDING_HOUSE_OF_TRUTH')) > 0:
				if CyGame().getSorenRandNum(100, "Despiel Citizens") < 25:
					pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_FAST_CHANT'), True)

		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_GENERAL')):
			if pUnit.canFight():
				iPromotion = 1 + CyGame().getSorenRandNum(2, "Trait General")
				pUnit.changeFreePromotionPick(iPromotion)

		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_UNREASONABLE')):
			if pUnit.canFight():
				if pUnit.getFreePromotionPick() >= 1:
					if gc.getGame().getSorenRandNum(100, "Free Promotion Unpick") < 10:
						pUnit.changeFreePromotionPick(-1)
				if gc.getGame().getSorenRandNum(100, "Free Promotion Pick") < 10:
					pUnit.changeFreePromotionPick(1)

		if pPlayer.getCivics(gc.getInfoTypeForString('CIVICOPTION_ECONOMY')) == gc.getInfoTypeForString('CIVIC_CONQUEST'):
			if pUnit.canFight():
				pUnit.changeFreePromotionPick(1)
# Delete by ent >>>
		"""
		if eTeam.isHasTech(gc.getInfoTypeForString('TECH_CONSTRUCTION')):
			if pUnit.getUnitCombatType() == gc.getInfoTypeForString('UNITCOMBAT_SIEGE'):
				pUnit.setHasPromotion(gc.getInfoTypeForString('PROMOTION_MOBILITY1'), True)
		"""
# <<<
# Kaijin <<<

##--------	Unofficial Bug Fix: End Add

##--------	BUGFfH: Added by Denev 2010/08/29
		return False
##--------	BUGFfH: End Add

##--------	Choose Trait: Added by Denev 2011/04/11
	def applyChooseTrait(self, argsList):
		iButtonId, iData1, iData2, iData3, iFlags, szText, bOption1, bOption2 = argsList

		ePlayer = iData1
		pPlayer = gc.getPlayer(ePlayer)

		leTraits = [eTrait for eTrait in xrange(gc.getNumTraitInfos()) if gc.getTraitInfo(eTrait).isSelectable() and not gc.getLeaderHeadInfo(pPlayer.getLeaderType()).hasTrait(eTrait)]

		pPlayer.clearTrait(TraitSourceTypes.TRAITSOURCE_ADAPTIVE)
		pPlayer.setHasTraitWithSource(leTraits[iButtonId], True, TraitSourceTypes.TRAITSOURCE_ADAPTIVE)

		return False
##--------	Choose Trait: End Modify			--------##

##--------	Dungeon Explorer: Added by Denev 2014/04/26
	def canExploreLair(self, argsList):
		pCaster, pPlot = argsList

		eImprovement = pPlot.getImprovementType()

		if not pPlot.isWater():
			if not gc.getImprovementInfo(eImprovement).isUnique():
				eLairBarbarian = gc.getImprovementInfo(eImprovement).getSpawnBarbarianType()
				if eLairBarbarian != BarbarianTypes.NO_BARBARIAN:
					eLairPlayer = CyGame().getBarbarianPlayer(eLairBarbarian)
					eLairTeam = gc.getPlayer(eLairPlayer).getTeam()
					if not gc.getTeam(eLairTeam).isAtWar(pCaster.getTeam()):
						return ReasonTypes.REASON_DISABLED_BARBARIAN_IS_NOT_ENEMY

		if not pCaster.isHuman():
			iRestrictTurns = cyFlatValue(70, gc.getGameSpeedInfo(CyGame().getGameSpeedType()).getVictoryDelayPercent(), False)
			if eImprovement != ImprovementTypes.NO_IMPROVEMENT:
				if gc.getImprovementInfo(eImprovement).isUnique():
					if pCaster.getCivilizationType() == en.eCivilizationElohim:
						return False
					iRestrictTurns *= 2
			if CyGame().getGameTurn() < iRestrictTurns:
# ent >>>
				if not pCaster.isHasPromotion(gc.getInfoTypeForString('PROMOTION_ADVENTURER')):
# ent <<<
					return False
		return True

	def exploreLair(self, argsList):
		pCaster = argsList[0]
		pPlot = pCaster.plot()

		iDestroyLair = 0
		if pCaster.getUnitCombatType() == en.eUnitCombatSiege:
			iDestroyLair = 100
		else:
# Kaijin >>>
# Kaijin - Orbis Adventurer - Start
			"""
			iRnd = CyGame().getSorenRandNum(100, 'Explore Lair') + pCaster.getLevel()
			iDestroyLair = 0
			"""
			iAdventurer = gc.getInfoTypeForString('PROMOTION_ADVENTURER')
			if pCaster.isHasPromotion(iAdventurer):
# ent >>>
##				iRnd = CyGame().getSorenRandNum(85, 'Explore Lair') + pCaster.getLevel()
##				iRnd += 15
				iRnd = CyGame().getSorenRandNum(55, 'Explore Lair') + pCaster.getLevel()
				iRnd += 45
			else:
				iRnd = CyGame().getSorenRandNum(100, 'Explore Lair') + pCaster.getLevel()
##			if pCaster.isHasPromotion(iAdventurer):
##				if iRnd < 74:
##					iRnd = CyGame().getSorenRandNum(85, 'Explore Lair') + pCaster.getLevel()
##					iRnd += 15
# ent <<<
# Kaijin - Orbis Adventurer - End
# Kaijin <<<
			if iRnd < 14:
				iDestroyLair = cf.exploreLairBigBad(pCaster)
			elif iRnd < 44:
				iDestroyLair = cf.exploreLairBad(pCaster)
			elif iRnd < 74:
				iDestroyLair = cf.exploreLairNeutral(pCaster)
			elif iRnd < 94:
				iDestroyLair = cf.exploreLairGood(pCaster)
			else:
				iDestroyLair = cf.exploreLairBigGood(pCaster)

		if iDestroyLair > CyGame().getSorenRandNum(100, 'Explore Lair'):
			pLair = gc.getImprovementInfo(pPlot.getImprovementType())
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_LAIR_DESTROYED', (pLair.getDescription(), ))
			CyInterface().addMessage(pCaster.getOwner(), False, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_PILLAGE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pLair.getButton(), en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)

		pCaster.changeExperience(1, -1, False, False, False)

		return True

	def exploreLairEpic(self, argsList):
		pCaster = argsList[0]
		pPlot = pCaster.plot()

		iDestroyLair = 0
		if pCaster.getUnitCombatType() == en.eUnitCombatSiege:
			iDestroyLair = 100
		else:
# Kaijin >>>
# Kaijin - Orbis Adventurer - Start
			iRnd = CyGame().getSorenRandNum(100, 'Explore Lair') + pCaster.getLevel()
			"""
			iDestroyLair = 0
			if iRnd < 54:
				iDestroyLair = cf.exploreLairBigBad(pCaster)
			else:
				iDestroyLair = cf.exploreLairBigGood(pCaster)
			"""
			iAdventurer = gc.getInfoTypeForString('PROMOTION_ADVENTURER')
			if pCaster.isHasPromotion(iAdventurer):
				iDestroyLair = cf.exploreLairBigGood(pCaster)
			else:
				if iRnd < 54:
					iDestroyLair = cf.exploreLairBigBad(pCaster)
				else:
					iDestroyLair = cf.exploreLairBigGood(pCaster)
# Kaijin - Orbis Adventurer - End
# Kaijin <<<

		if iDestroyLair > CyGame().getSorenRandNum(100, 'Explore Lair'):
			pLair = gc.getImprovementInfo(pPlot.getImprovementType())
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_LAIR_DESTROYED', (pLair.getDescription(), ))
			CyInterface().addMessage(pCaster.getOwner(), False, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_PILLAGE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pLair.getButton(), en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			# Orbis >>>
			"""
			pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)
			"""
			cf.doRemoveEpicLair(pPlot)
			# Orbis <<<

		pCaster.changeExperience(1, -1, False, False, False)

		return True

# Kaijin >>>
	def exploreDen(self, argsList):
		pCaster = argsList[0]
		pPlot = pCaster.plot()

		iDestroyLair = 0
		if pCaster.getUnitCombatType() == en.eUnitCombatSiege:
			iDestroyLair = 100
		else:
# Kaijin - Orbis Adventurer - Start
			"""
			iRnd = CyGame().getSorenRandNum(100, 'Explore Lair') + pCaster.getLevel()
			iDestroyLair = 0
			"""
			iAdventurer = gc.getInfoTypeForString('PROMOTION_ADVENTURER')
			if pCaster.isHasPromotion(iAdventurer):
# ent >>>
##				iRnd = CyGame().getSorenRandNum(80, 'Explore Lair') + pCaster.getLevel()
##				iRnd += 20
				iRnd = CyGame().getSorenRandNum(55, 'Explore Lair') + pCaster.getLevel()
				iRnd += 45
			else:
				iRnd = CyGame().getSorenRandNum(100, 'Explore Lair') + pCaster.getLevel()
##			if pCaster.isHasPromotion(iAdventurer):
##				if iRnd < 79:
##					iRnd = CyGame().getSorenRandNum(85, 'Explore Lair') + pCaster.getLevel()
##					iRnd += 20
# ent <<<
# Kaijin - Orbis Adventurer - End
			if iRnd < 14:
				iDestroyLair = cf.exploreLairBigBad(pCaster)
			elif iRnd < 44:
				iDestroyLair = cf.exploreLairBad(pCaster)
			elif iRnd < 74:
				iDestroyLair = cf.exploreLairNeutral(pCaster)
			elif iRnd < 94:
				iDestroyLair = cf.exploreLairGood(pCaster)
			else:
				iDestroyLair = cf.exploreLairBigGood(pCaster)

		if iDestroyLair > CyGame().getSorenRandNum(100, 'Explore Lair'):
			pLair = gc.getImprovementInfo(pPlot.getImprovementType())
			szMessage = CyTranslator().getText('TXT_KEY_MESSAGE_LAIR_DESTROYED', (pLair.getDescription(), ))
			CyInterface().addMessage(pCaster.getOwner(), False, gc.getEVENT_MESSAGE_TIME(), szMessage, 'AS2D_PILLAGE', InterfaceMessageTypes.MESSAGE_TYPE_INFO, pLair.getButton(), en.eColorGreen, pPlot.getX(), pPlot.getY(), True, True)
			pPlot.setImprovementType(ImprovementTypes.NO_IMPROVEMENT)

		pCaster.changeExperience(1, -1, False, False, False)

		return True
# Kaijin <<<
##--------	Dungeon Explorer: End Add

##--------	Better AI: Added by Denev 2011/04/11
	def AI_getGoldReserve(self, argsList):
		iPlayer = argsList[0]
		pPlayer = gc.getPlayer(iPlayer)

		iGoldReserve = 0

# Kaijin >>>
#		if pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_KHAZAD'):
		if pPlayer.hasTrait(gc.getInfoTypeForString('TRAIT_RICHES')):
			iNumCities = pPlayer.getNumCities()
			iRichesVaultUnitaryThreshold = cf.getRichesVaultUnitaryThreshold(iNumCities)

			iVaultLevel = 2 + pPlayer.getCurrentPeriod()
			iGoldReserve += cf.getRichesVaultRequired(iNumCities, iVaultLevel)

		elif pPlayer.getCivilizationType() == gc.getInfoTypeForString('CIVILIZATION_KHAZAD'):
			iNumCities = pPlayer.getNumCities()
			iDwarvenVaultUnitaryThreshold = cf.getDwarvenVaultUnitaryThreshold(iNumCities)

			iVaultLevel = 2 + pPlayer.getCurrentPeriod()
			iGoldReserve += cf.getDwarvenVaultRequired(iNumCities, iVaultLevel)
# Kaijin <<<

		return iGoldReserve
##--------	Better AI: End Add

# Returns Promotiontype or -1 for no Promotion
	def AI_MagePromotion(self, argsList):
		pUnit = argsList[0]
		pPlot = pUnit.plot()
		pPlayer = gc.getPlayer(pUnit.getOwner())
		pTeam = gc.getTeam(pPlayer.getTeam())
		eUnitAIType = pUnit.getUnitAIType()

		if pUnit.getLevel() >= 4:
			if pUnit.getUnitClassType() == gc.getInfoTypeForString('UNITCLASS_ADEPT'):
				return -101	# keep promotion

		def getBestPromotion(iRank):
			iBestValue = 0
			eBestPromotion = PromotionTypes.NO_PROMOTION
			for key, value in self.dWeights[iRank].items():
				ePromotion, iPromotionValue, iStackWeight = value

#------------
#Specific modifiers start
#------------
				dCivWeights = self.dCivWeights[eCivilization][iRank]
				if key in dCivWeights:
					iPromotionValue = dCivWeights[key][0]
					iStackWeight = dCivWeights[key][1]

				if iRank == 0:
					if key == 'PROMOTION_EXTENSION2':
						if pUnit.AI_isDamageDealer():
							iPromotionValue = 70
# ent >>>
#					elif key == 'PROMOTION_EXTENSION1':
					elif key in ('PROMOTION_EXTENSION1', 'PROMOTION_EXTENSION3'):
# ent <<<
						if pUnit.AI_isSummoner():
							iPromotionValue = 70

					elif key in ('PROMOTION_METAMAGIC1', 'PROMOTION_METAMAGIC2'):
						if pPlayer.AI_getTowerVictoryStage() > 0:
							iPromotionValue = 70

				elif iRank == 1:
					if key == 'PROMOTION_LIFE':
						if pPlayer.getAlignment() == en.eAlignmentGood:
							iPromotionValue = 70

				elif iRank == 2:
					if key == 'PROMOTION_MIND':
						if pPlayer.getStateReligion() == en.eReligionOctopusOverlords:
							iPromotionValue = 150

				if pPlayer.isFeatAccomplished(FeatTypes.FEAT_TRUST):
					if iRank == 3 and key == 'PROMOTION_SPIRIT':
						continue
				if not pUnit.canPromote(ePromotion, -1):
					continue
#------------
#Specific modifiers end
#------------

				iNumSameCaster = 0
				for iIndex in xrange(pPlot.getNumUnits()):
					if pPlot.getUnit(iIndex).isHasPromotion(ePromotion):
						iNumSameCaster += 1
				iValue = iPromotionValue * max(0, 100 - iStackWeight * iNumSameCaster) + CyGame().getSorenRandNum(20, "sphere weight")

				if iBestValue < iValue:
					if pUnit.canPromote(ePromotion, -1):
						iBestValue = iValue
						eBestPromotion = ePromotion
					elif iRank == 2:
						ePrereqPromotion = self.dWeights[iRank - 1][key]
						if pUnit.canPromote(ePrereqPromotion, -1):
							iBestValue = iValue
							eBestPromotion = ePrereqPromotion

			return eBestPromotion

		if eUnitAIType in self.leCombatUnitAIs:
			for eCombatImportantPromotion in self.leCombatImportantPromotions:
				if pUnit.canPromote(eCombatImportantPromotion, -1):
					return eCombatImportantPromotion

#------------
#UNITAI_MAGE
#------------
		elif eUnitAIType == gc.getInfoTypeForString('UNITAI_MAGE'):

			eCivilization = pPlayer.getCivilizationType()

			if pUnit.isHasPromotion(en.ePromotionChanneling3):
				eBestPromotion = getBestPromotion(3)
				if eBestPromotion != PromotionTypes.NO_PROMOTION:
					return eBestPromotion

			if pUnit.isHasPromotion(en.ePromotionChanneling2):
				iCount = 0
				for eRank2SpellPromotion in self.leRank2SpellPromotions:
					if pUnit.isHasPromotion(eRank2SpellPromotion):
						iCount += 1
				if iCount < self.iSphereLimit:
					eBestPromotion = getBestPromotion(2)
					if eBestPromotion != PromotionTypes.NO_PROMOTION:
						return eBestPromotion

			if pUnit.isHasPromotion(en.ePromotionChanneling1):
				iCount = 0
				for eRank1SpellPromotion in self.leRank1SpellPromotions:
					if pUnit.isHasPromotion(eRank1SpellPromotion):
						iCount += 1
				if iCount < self.iSphereLimit:
					eBestPromotion = getBestPromotion(1)
					if eBestPromotion != PromotionTypes.NO_PROMOTION:
						return eBestPromotion

			eBestPromotion = getBestPromotion(0)
			if eBestPromotion != PromotionTypes.NO_PROMOTION:
				return eBestPromotion

#------------
#UNITAI_TERRAFORMER
#------------
		elif eUnitAIType == gc.getInfoTypeForString('UNITAI_MAGE_WORKER'):
			if CyGame().getGlobalCounter() > 15:
				if pUnit.canPromote(gc.getInfoTypeForString('PROMOTION_LIFE1'), -1):
					return gc.getInfoTypeForString('PROMOTION_LIFE1')

			for eTerraformingPromotion in self.leTerraformingPromotions:
				if pUnit.canPromote(eTerraformingPromotion, -1):
					return eTerraformingPromotion

		return PromotionTypes.NO_PROMOTION
