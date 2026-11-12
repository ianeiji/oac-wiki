# OAC/効果（0.57、XMLから生成）

- 対象: OAC 0.57（インストール済みのゲームファイル `Assets/XML` から自動生成）
- 生成元: `Misc/CIV4EffectInfos.xml`
- 読み方: 主要な項目は日本語ラベル付きで先頭に、それ以外の既定値でない設定は「その他の設定」にXMLのタグ名のまま列挙する。値の内部名は日本語名に置き換えている。Pythonで実装された効果はXMLにないため含まない（ゲーム内ヘルプの説明文があれば載せている）。

### Blood splatter effect - Blood splatter effect

- 内部名: `EFFECT_BLOOD_THRUST`
- その他の設定:
  - `fScale`: 5.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/fx_sword_hit_thrust.nif

### Blood spray effect - Blood spray effect

- 内部名: `EFFECT_BLOOD_SLASH`
- その他の設定:
  - `fScale`: 4.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/fx_sword_hit_slash.nif

### Ice Summon Effect - Ice Summon Effect

- 内部名: `EFFECT_ICE_SUMMON`
- その他の設定:
  - `fScale`: 1.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/alb_iceshield_hit.nif

### Slow Effect - Slow Effect

- 内部名: `EFFECT_SLOW`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/alb_coldring_hit.nif

### Pit Beast Spell Effect - Pit Beast Spell Effect

- 内部名: `EFFECT_PIT_BEAST_SUMMON`
- その他の設定:
  - `fScale`: 30.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/Rebirth.nif

### Wraith Spell Effect - Wraith Spell Effect

- 内部名: `EFFECT_WRAITH_SUMMON`
- その他の設定:
  - `fScale`: 30.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/ArmyOfDarknessStart.nif

### Spores Effect - Spores Effect

- 内部名: `EFFECT_SPORES`
- その他の設定:
  - `fScale`: 4.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/alb_acidmist_hit.nif

### Volcano Effect - Volcano Effect

- 内部名: `EFFECT_VOLCANO`
- その他の設定:
  - `fScale`: 3.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/lava2_sfx.NIF

### Death Portal - Death Portal

- 内部名: `EFFECT_PORTAL_DEATH`
- その他の設定:
  - `fScale`: 3.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/burstaura_fiery1.NIF

### Bloodthirster Hoof Print - Bloodthirster Hoof Print

- 内部名: `EFFECT_BT_FOOTPRINT`
- その他の設定:
  - `fScale`: 0.045
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/BT_FOOTPRINT.nif

### EFFECT_ABADDON_BIRTH - EFFECT_ABADDON_BIRTH

- 内部名: `EFFECT_ABADDON_BIRTH`
- その他の設定:
  - `fScale`: 15.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Heroes/Avatar of Wrath/AbaddonBirthEffect.nif

### EFFECT_ABADDON_DEATH - EFFECT_ABADDON_DEATH

- 内部名: `EFFECT_ABADDON_DEATH`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Heroes/Avatar of Wrath/AbaddonDeathEffect.nif

### EFFECT_ABADDON_DEVASTATE - EFFECT_ABADDON_DEVASTATE

- 内部名: `EFFECT_ABADDON_DEVASTATE`
- その他の設定:
  - `fScale`: 15.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Heroes/Avatar of Wrath/AbaddonDevastateEffect.nif

### Crush - Crush

- 内部名: `EFFECT_CRUSH`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/mid_ehand_hit.nif

### Maelstrom - Maelstrom

- 内部名: `EFFECT_MAELSTROM`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/statictempest350.nif

### Air Summon - Air Summon

- 内部名: `EFFECT_AIR_SUMMON`
- その他の設定:
  - `fScale`: 3.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/zapsphere_hit.nif

### Charm Person - Charm Person

- 内部名: `EFFECT_CHARM_PERSON`
- その他の設定:
  - `fScale`: 2.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/shear_Acuity_hit.nif

### Burning Blood - Burning Blood

- 内部名: `EFFECT_BURNING_BLOOD`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/BoilingBlood_Fire.nif

### Scorch - Scorch

- 内部名: `EFFECT_SCORCH`
- その他の設定:
  - `fScale`: 1.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/groundsplash_soft_fire.nif

### Wither - Wither

- 内部名: `EFFECT_WITHER`
- その他の設定:
  - `fScale`: 2.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/skullswirl_hit.nif

### Sacrifice - Sacrifice

- 内部名: `EFFECT_SACRIFICE`
- その他の設定:
  - `fScale`: 2.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/scareface1_hit.nif

### Spiritual Hammer - Spiritual Hammer

- 内部名: `EFFECT_SPIRITUAL_HAMMER`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/mid_mjolnir2_hit.nif

### Vitalize - Vitalize

- 内部名: `EFFECT_VITALIZE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/dewdrop1_hit.nif

### Nature Summon - Nature Summon

- 内部名: `EFFECT_NATURE_SUMMON`
- その他の設定:
  - `fScale`: 2.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/leafshield1_hit.nif

### Stoneskin - Stoneskin

- 内部名: `EFFECT_STONESKIN`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/fungshld_hit.nif

### Spring - Spring

- 内部名: `EFFECT_SPRING`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/coldball_explo.nif

### Snowfall - Snowfall

- 内部名: `EFFECT_SNOWFALL`
- その他の設定:
  - `fScale`: 3.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/blastripple_sound.nif

### Snowfall Greator - Snowfall Greator

- 内部名: `EFFECT_SNOWFALL_GREATOR`
- その他の設定:
  - `fScale`: 4.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/blastripple_sound.nif

### Contagion - Contagion

- 内部名: `EFFECT_CONTAGION`
- その他の設定:
  - `fScale`: 2.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/skullcloud1_hit.nif

### Pillar of Fire - Pillar of Fire

- 内部名: `EFFECT_PILLAR_OF_FIRE`
- その他の設定:
  - `fScale`: 3.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/alb_clstrbuff3_hit.nif

### Entangle - Entangle

- 内部名: `EFFECT_ENTANGLE`
- その他の設定:
  - `fScale`: 3.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/hib_thornwrap_hit.nif

### Destroy Undead - Destroy Undead

- 内部名: `EFFECT_DESTROY_UNDEAD`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/hib_mexplo4_hit.nif

### Bloom - Bloom

- 内部名: `EFFECT_BLOOM`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/leafswirl1_sfx.nif

### Fire Summon - Fire Summon

- 内部名: `EFFECT_FIRE_SUMMON`
- その他の設定:
  - `fScale`: 2.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/lavapuddle_crackle.nif

### Entropy Summon - Entropy Summon

- 内部名: `EFFECT_ENTROPY_SUMMON`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/hib_vexplo5_hit.nif

### Hellfire - Hellfire

- 内部名: `EFFECT_HELLFIRE`
- その他の設定:
  - `fScale`: 3.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/groundsplash_heat_fire.nif

### Resurrection - Resurrection

- 内部名: `EFFECT_RESURRECTION`
- その他の設定:
  - `fScale`: 3.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/burstaura_holy3.nif

### Water Summon - Water Summon

- 内部名: `EFFECT_WATER_SUMMON`
- その他の設定:
  - `fScale`: 3.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/bluringbeam1_hit.nif

### Bless - Bless

- 内部名: `EFFECT_BLESS`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/alb_palgrpheal_hit.nif

### Enchanted Blade - Enchanted Blade

- 内部名: `EFFECT_ENCHANTED_BLADE`
- その他の設定:
  - `fScale`: 2.0
  - `fUpdateRate`: 2.0
  - `Path`: Art/Effects/Spell Effects/alb_palgrpstrength_hit.nif

### Meteor Swarm - Meteor Swarm

- 内部名: `EFFECT_METEOR_SWARM`
- その他の設定:
  - `fScale`: 3.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/alb_meteors1_hit.nif

### Dispel Magic - Dispel Magic

- 内部名: `EFFECT_DISPEL_MAGIC`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/alb_coldring_hit.nif

### Life Summon - Life Summon

- 内部名: `EFFECT_LIFE_SUMMON`
- その他の設定:
  - `fScale`: 3.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/alb_clstrbuff1_hit.nif

### Ring of Flames - Ring of Flames

- 内部名: `EFFECT_RING_OF_FLAMES`
- その他の設定:
  - `fScale`: 3.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/alb_firesplash_hit.nif

### Swords Sparks - Swords Sparks

- 内部名: `EFFECT_SWORDS_SPARKS`
- その他の設定:
  - `fScale`: 15.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/fx_swords_sparks/fx_swords_sparks.nif

### Silk of the Giant Spider - Silk of the Giant Spider

- 内部名: `EFFECT_SPIDERSILK`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Giant Spider/spidersilk.nif

### Dragon Footprint - Dragon Footprint

- 内部名: `EFFECT_DRAGONPRINT`
- その他の設定:
  - `fScale`: 2.00
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/dragon/Dragonstep.nif

### Hoof dust for a running Dragon - Hoof dust for a running Dragon

- 内部名: `EFFECT_DRAGONFOOTDUST`
- その他の設定:
  - `fScale`: 2.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/dust_impact_002/fx_dust_impact_002.nif

### Dragon Smoky Breath - Dragon Smoky Breath

- 内部名: `EFFECT_SMOKECLOUD`
- その他の設定:
  - `fScale`: 0.6
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/dragon/smokecloud.nif

### Dragon Steam Breath - Dragon Steam Breath

- 内部名: `EFFECT_STEAMCLOUD`
- その他の設定:
  - `fScale`: 0.6
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/dragon/steamcloud.nif

### Acid Rain - Acid Rain

- 内部名: `EFFECT_ACID_RAIN`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/AcidRain.nif

### Banish Angel - Banish Angel

- 内部名: `EFFECT_BANISH_ANGEL`
- その他の設定:
  - `fScale`: 10
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/BanishAngels.nif

### Banish Demon - Banish Demon

- 内部名: `EFFECT_BANISH_DEMON`
- その他の設定:
  - `fScale`: 8
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/BanishDemons.nif

### Blinding Light - Blinding Light

- 内部名: `EFFECT_BLINDING_LIGHT`
- その他の設定:
  - `fScale`: 1.8
  - `fUpdateRate`: 2.0
  - `Path`: Art/Effects/Spell Effects/BlindingLight.nif

### Dark Hole - Dark Hole

- 内部名: `EFFECT_DARK_HOLE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/DarkHole_hit.nif

### Firestorm - Firestorm

- 内部名: `EFFECT_FIRESTORM`
- その他の設定:
  - `fScale`: 0.8
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/FlameStrike_hit.nif

### Meteor - Meteor

- 内部名: `EFFECT_METEOR`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/Meteor.nif

### Nether Blade - Nether Blade

- 内部名: `EFFECT_NETHER_BLADE`
- その他の設定:
  - `fScale`: 1
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/NetherBlade_hit.nif

### Storm - Storm

- 内部名: `EFFECT_STORM`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.6
  - `Path`: Art/Effects/Spell Effects/Storm_hit.nif

### Storm Cloud - Storm Cloud

- 内部名: `EFFECT_STORMCLOUD`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/StormCloud_hit.nif

### Sun Light - Sun Light

- 内部名: `EFFECT_SUNLIGHT`
- その他の設定:
  - `fScale`: 3.2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/Sunlight.nif

### Turn Undead - Turn Undead

- 内部名: `EFFECT_TURN_UNDEAD`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/TurnUndead.nif

### Frosty swirling air flow - Frosty swirling air flow

- 内部名: `EFFECT_WIND_SWIRL2`
- その他の設定:
  - `fScale`: 2.4
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/wind_swirl/fx_wind_swirl_01.nif

### Dragon Firebreath - Dragon Firebreath

- 内部名: `EFFECT_FIREBURST`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/dragon/fireburst.nif

### Dragon Fireball - Dragon Fireball

- 内部名: `EFFECT_DRAGON_FIREBALL`
- その他の設定:
  - `fScale`: 1.4
  - `fUpdateRate`: 0.5
  - `Path`: Art/Effects/dragon/fireball/grenadiergrenade.kfm
  - `bIsProjectile`: 1
  - `fSpeed`: 400.0

### Dragon Fireball Explosion - Dragon Fireball Explosion

- 内部名: `EFFECT_DFIREBALL_EXPLOSION`
- その他の設定:
  - `fScale`: 0.8
  - `fUpdateRate`: .8
  - `Path`: Art/Effects/dragon/fireball/fireball_explosion.nif

### Toxic Fumes - Toxic Fumes

- 内部名: `EFFECT_TOXICBREATH_PURPLE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/dragon/toxic_breath_purple.nif

### Dragon Toxicball - Dragon Toxicball

- 内部名: `EFFECT_DRAGON_TOXICBALL_PURPLE`
- その他の設定:
  - `fScale`: 1.6
  - `fUpdateRate`: 0.5
  - `Path`: Art/Effects/dragon/toxicball_purple/GrenadierGrenade.kfm
  - `bIsProjectile`: 1
  - `fSpeed`: 400.0

### Dragon Fireball Explosion - Dragon Fireball Explosion

- 内部名: `EFFECT_TOXICPURP_EXPLOSION`
- その他の設定:
  - `fScale`: 0.8
  - `fUpdateRate`: .8
  - `Path`: Art/Effects/dragon/toxicball_purple/toxicball_explosion.nif

### Toxic Fumes - Toxic Fumes

- 内部名: `EFFECT_TOXICBREATH_GREEN`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/dragon/toxic_breath_green.nif

### Dragon Toxicball - Dragon Toxicball

- 内部名: `EFFECT_DRAGON_TOXICBALL_GREEN`
- その他の設定:
  - `fScale`: 1.6
  - `fUpdateRate`: 0.5
  - `Path`: Art/Effects/dragon/toxicball_green/GrenadierGrenade.kfm
  - `bIsProjectile`: 1
  - `fSpeed`: 400.0

### Dragon Fireball Explosion - Dragon Fireball Explosion

- 内部名: `EFFECT_TOXICGREE_EXPLOSION`
- その他の設定:
  - `fScale`: 0.8
  - `fUpdateRate`: .8
  - `Path`: Art/Effects/dragon/toxicball_green/toxicball_explosion.nif

### Icy Breath - Icy Breath

- 内部名: `EFFECT_ICEBURST`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/dragon/iceburst.nif

### Dragon Iceball - Dragon Iceball

- 内部名: `EFFECT_DRAGON_ICEBALL`
- その他の設定:
  - `fScale`: 1.4
  - `fUpdateRate`: 0.5
  - `Path`: Art/Effects/dragon/iceball/GrenadierGrenade.kfm
  - `bIsProjectile`: 1
  - `fSpeed`: 400.0

### Dragon Fireball Explosion - Dragon Fireball Explosion

- 内部名: `EFFECT_DRICEBALL_EXPLOSION`
- その他の設定:
  - `fScale`: 0.8
  - `fUpdateRate`: .8
  - `Path`: Art/Effects/dragon/iceball/iceball_explosion.nif

### Golden Breath with stars - Golden Breath with stars

- 内部名: `EFFECT_HOLYBURST`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/dragon/holyburst.nif

### Air Elemental effect - Air Elemental effect

- 内部名: `EFFECT_AIRDUST`
- その他の設定:
  - `fScale`: 3.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/dust_impact_002/fx_dust_impact_002.nif

### Footprint - Footprint

- 内部名: `EFFECT_NOFPRINT`
- その他の設定:
  - `fScale`: 0.85
  - `fUpdateRate`: 1.0
  - `Path`: Art/Shared/nostep.nif

### Catapult Rock - Catapult Rock

- 内部名: `EFFECT_CATAPULT_COW1`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Civs/Balseraphs/Catapult/CatapultRock.kfm
  - `bIsProjectile`: 1
  - `fSpeed`: 400.0
  - `fArcValue`: 4.0

### Boulder Explosion for Catapult Attack - Boulder Explosion for Catapult Attack

- 内部名: `EFFECT_CATAPULT_COW1_EXPLODE`
- その他の設定:
  - `fScale`: 0.6
  - `fUpdateRate`: 2.5
  - `Path`: Art/Effects/explosion_dirt_02/fx_explosion_dirt_02.nif

### ArcherArrow - ArcherArrow

- 内部名: `EFFECT_DEMON_ARROW`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Civs/Infernal/Longbowman/archerarrow.nif
  - `bIsProjectile`: 1
  - `fSpeed`: 500.0

### Grenadier Grenade - Grenadier Grenade

- 内部名: `EFFECT_FIRLICH_THROW`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Lich/GrenadierGrenade.kfm
  - `bIsProjectile`: 1
  - `fSpeed`: 350.0
  - `fArcValue`: 4.0

### Grenadier grenade explosion - Grenadier grenade explosion

- 内部名: `EFFECT_FIREBLICH_EXPLOSION`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: .8
  - `Path`: Art/Effects/fx_firelich_explosion.nif

### Grenadier Grenade - Grenadier Grenade

- 内部名: `EFFECT_FIRBLUE_THROW`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/mage/GrenadierGrenade.kfm
  - `bIsProjectile`: 1
  - `fSpeed`: 350.0
  - `fArcValue`: 4.0

### Grenadier grenade explosion - Grenadier grenade explosion

- 内部名: `EFFECT_FIREBBLUE_EXPLOSION`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: .8
  - `Path`: Art/Effects/fx_fireblue_explosion.nif

### Footprint - Footprint

- 内部名: `INFEPRINT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Shared/Infestep.nif

### Footprint - Footprint

- 内部名: `EFFECT_INFEPRINT`
- その他の設定:
  - `fScale`: 0.85
  - `fUpdateRate`: 1.0
  - `Path`: Art/Shared/Infestep.nif

### Mali Spear - Mali Spear

- 内部名: `EFFECT_DEMOSPEAR`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Civs/Infernal/Huntingdemon/MaliSkirmisherSpear.nif
  - `bIsProjectile`: 1
  - `fSpeed`: 500.0

### Grenadier Grenade - Grenadier Grenade

- 内部名: `EFFECT_FIRBALL_THROW`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/FireballThrow/GrenadierGrenade.kfm
  - `bIsProjectile`: 1
  - `fSpeed`: 350.0
  - `fArcValue`: 4.0

### Footprint - Footprint

- 内部名: `EARTPRINT`
- その他の設定:
  - `fScale`: 1.6
  - `fUpdateRate`: 1.0
  - `Path`: Art/Shared/Earthstep.nif

### Longbow Arrow - Longbow Arrow

- 内部名: `EFFECT_FIREBOWARROW`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Effects/FirebowArrow/LongbowArrow.nif
  - `bIsProjectile`: 1
  - `fSpeed`: 500.0

### Catapult Rock - Catapult Rock

- 内部名: `EFFECT_CATAPULT_SKUL`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Civs/Doviello/Catapult/CatapultRock.kfm
  - `bIsProjectile`: 1
  - `fSpeed`: 500.0
  - `fArcValue`: 4.0

### Horse Hoof Print - Horse Hoof Print

- 内部名: `EFFECT_WARMACHIPRINT`
- その他の設定:
  - `fScale`: 3.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Shared/WarmachinePrint.nif

### Boom - Boom

- 内部名: `EFFECT_SPELL1`
- その他の設定:
  - `fScale`: 0.2
  - `fUpdateRate`: 1.2
  - `Path`: Art/Interface/Effects/EmpBlast.nif

### Fizzle - Fizzle

- 内部名: `EFFECT_SPELL2`
- その他の設定:
  - `fScale`: 0.8
  - `fUpdateRate`: 1.0
  - `Path`: Art/Interface/Effects/Stasis.nif

### EFFECT_FOOTSTEP_ON - EFFECT_FOOTSTEP_ON

- 内部名: `EFFECT_FOOTSTEP_ON`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Interface/Effects/FootStep_ON.nif

### Footstep - Footstep

- 内部名: `EFFECT_FOOTSTEP`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Interface/Effects/FootStep.nif

### Ping - Ping

- 内部名: `EFFECT_PING`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Interface/Effects/EmpBlast.nif

### Res Bomb - Res Bomb

- 内部名: `EFFECT_RES_BOMB`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Interface/Effects/ResourceBOMB.nif

### Stasis - Stasis

- 内部名: `EFFECT_STASIS`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Interface/Effects/Stasis.nif

### Waypoint - Waypoint

- 内部名: `EFFECT_WAYPOINT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Interface/Effects/Waypoint.nif

### Laser Hit - Laser Hit

- 内部名: `EFFECT_LASER_HIT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Interface/Effects/LaserHit.nif

### Mine - Mine

- 内部名: `EFFECT_MINE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Interface/Effects/Mine.nif

### Mutiny - Mutiny

- 内部名: `EFFECT_MUTINY`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Interface/Effects/Mutiny.nif

### Candle flame for religion popup cinematic - Candle flame for religion popup cinematic

- 内部名: `EFFECT_CANDLE_FLAME_FOR_RELIGION_POPUP`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/fire_candle_flame/fx_fire_candle_flame.nif

### Candle flame hardware light for religion popup cinematic - Candle flame hardware light for religion popup cinematic

- 内部名: `EFFECT_CANDLE_HWLIGHT_FOR_RELIGION_POPUP`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/fire_candle_flame/fx_fire_candle_hardware_light.nif

### Footprint - Footprint

- 内部名: `EFFECT_FOOTPRINT`
- その他の設定:
  - `fScale`: 0.85
  - `fUpdateRate`: 1.0
  - `Path`: Art/Shared/Footstep.nif

### Footprint Medium - Footprint Medium

- 内部名: `EFFECT_FOOTPRINT_80`
- その他の設定:
  - `fScale`: 0.75
  - `fUpdateRate`: 1.0
  - `Path`: Art/Shared/Footstep.nif

### Footprint Small - Footprint Small

- 内部名: `EFFECT_FOOTPRINT_60`
- その他の設定:
  - `fScale`: 0.65
  - `fUpdateRate`: 1.0
  - `Path`: Art/Shared/Footstep.nif

### Horse Hoof Print - Horse Hoof Print

- 内部名: `EFFECT_HORSEPRINT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Shared/HorsePrint.nif

### Horse Hoof Print - Horse Hoof Print

- 内部名: `EFFECT_BIGHORSEPRINT`
- その他の設定:
  - `fScale`: 2.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Shared/HorsePrint.nif

### Wild Animal Paw Print - Wild Animal Paw Print

- 内部名: `EFFECT_PAWPRINT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Shared/PawPrint.nif

### Assault Mech Print - Assault Mech Print

- 内部名: `EFFECT_MECHPRINT`
- その他の設定:
  - `fScale`: 5.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Shared/MechPrint.nif

### Footprint - Footprint

- 内部名: `FOOTPRINT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Shared/Footstep.nif

### Longbow Arrow - Longbow Arrow

- 内部名: `EFFECT_LONGBOWARROW`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Longbowman/LongbowArrow.nif
  - `bIsProjectile`: 1
  - `fSpeed`: 500.0

### Crossbow bolt - Crossbow bolt

- 内部名: `EFFECT_CROSSBOWBOLT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Crossbowman/CrossbowBolt.nif
  - `bIsProjectile`: 1
  - `fSpeed`: 500.0

### ArcherArrow - ArcherArrow

- 内部名: `EFFECT_ARCHERARROW`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Archer/ArcherArrow.nif
  - `bIsProjectile`: 1
  - `fSpeed`: 500.0

### ChineseArcherArrow - ChineseArcherArrow

- 内部名: `EFFECT_CHINESEARROW`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Archer_Chinese/Archer_Chinese_Arrow.nif
  - `bIsProjectile`: 1
  - `fSpeed`: 500.0

### EgyptianArcherArrow - EgyptianArcherArrow

- 内部名: `EFFECT_EGYPTIANARROW`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Archer_Egyptian/Archer_Egyptian_Arrow.nif
  - `bIsProjectile`: 1
  - `fSpeed`: 500.0

### EurasianArcherArrow - EurasianArcherArrow

- 内部名: `EFFECT_EURASIANARROW`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Archer_Eurasian/Archer_Eurasian_Arrow.nif
  - `bIsProjectile`: 1
  - `fSpeed`: 500.0

### Galley Fire Arrow Effect - Galley Fire Arrow Effect

- 内部名: `EFFECT_GALLEY_FIREARROW`
- その他の設定:
  - `fScale`: 0.7
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/fire_arrow/fx_Galley_FireArrow.nif
  - `bIsProjectile`: 1
  - `fSpeed`: 300.00
  - `fArcValue`: 3.0

### CamelArcherArrow - CamelArcherArrow

- 内部名: `EFFECT_CAMELARCHERARROW`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Unique/Arabia/CamelArcher/ArabiaCamelArcherArrow.nif
  - `bIsProjectile`: 1
  - `fSpeed`: 500.0

### HorseArcherArrow - HorseArcherArrow

- 内部名: `EFFECT_HORSEARCHERARROW`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/HorseArcher/HorseArcherArrow.nif
  - `bIsProjectile`: 1
  - `fSpeed`: 500.0

### Mali Spear - Mali Spear

- 内部名: `EFFECT_MALISPEAR`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Unique/Mali/Skirmisher/MaliSkirmisherSpear.nif
  - `bIsProjectile`: 1
  - `fSpeed`: 500.0

### Catapult Rock - Catapult Rock

- 内部名: `EFFECT_CATAPULT_ROCK`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Catapult/CatapultRock.kfm
  - `bIsProjectile`: 1
  - `fSpeed`: 500.0
  - `fArcValue`: 4.0

### Grenadier Grenade - Grenadier Grenade

- 内部名: `EFFECT_GRENADE_THROW`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Grenadier/GrenadierGrenade.kfm
  - `bIsProjectile`: 1
  - `fSpeed`: 350.0
  - `fArcValue`: 4.0

### Flamethrower Canon - Flamethrower Canon

- 内部名: `EFFECT_HWACHA_ROCKET`
- その他の設定:
  - `fScale`: 2.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/FlameThrower/firespray_sfx.nif

### Sam_Infantry missle - Sam_Infantry missle

- 内部名: `EFFECT_SAM_ANTI_AIR_MISSLE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/SAMInfantry/SAMInfantry_missile.kfm
  - `bIsProjectile`: 1
  - `fSpeed`: 600.0

### Peltast Sling Stone - Peltast Sling Stone

- 内部名: `EFFECT_STONE_THROW`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Peltast/Peltast_Stone_Throw.kfm
  - `bIsProjectile`: 1
  - `fSpeed`: 350.0
  - `fArcValue`: 4.0

### Mongolian Javelin - Mongolian Javelin

- 内部名: `EFFECT_MONGOL_JAV`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Mongolian_JavelinThrower/Mongolian_Javelin.nif
  - `bIsProjectile`: 1
  - `fSpeed`: 500.0
  - `fArcValue`: 2.0

### Trebuchet Rock - Trebuchet Rock

- 内部名: `EFFECT_TREBUCHET_ROCK`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Trebuchet/TrebuchetRock.kfm
  - `bIsProjectile`: 1
  - `fSpeed`: 400
  - `fArcValue`: 6

### Dust Cloud - Dust Cloud

- 内部名: `EFFECT_SETTLERSMOKE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/settler_smoke/SettlerSmoke.nif

### Goody hut pop dust and hay Used for Yert to Mongol Settler - Goody hut pop dust and hay Used for Yert to Mongol Settler

- 内部名: `EFFECT_PACK_UP`
- その他の設定:
  - `fScale`: 1.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/improvement_goody_hut_pop/fx_goodyhut_pop.nif

### Hot Sparks - Hot Sparks

- 内部名: `EFFECT_MININGSPARK`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/work_mine/MiningSpark.nif

### Quick Puff of Dirt - Quick Puff of Dirt

- 内部名: `EFFECT_DIGDIRT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/work_dig/DigDirt.nif

### Quick Clump of Dirt - Quick Clump of Dirt

- 内部名: `EFFECT_THROWDIRT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/work_dig/ThrowDirt.nif

### Creation Effect - Creation Effect

- 内部名: `EFFECT_FLINTSPARK`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/weapon_flintspark/fx_weapon_flintspark.nif

### Spy Sabotaging Production - Spy Sabotaging Production

- 内部名: `EFFECT_SPY_SABOTAGE`
- その他の設定:
  - `fScale`: .2
  - `fUpdateRate`: 2.0
  - `Path`: Art/Effects/explosion_large_001/fx_explosion_large_001.NIF

### Omen Horsemen attack - Omen Horsemen attack

- 内部名: `EFFECT_OMEN_HORSEMAN`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Omen_Horseman/OMEN_HORSEMAN_EFFECT.nif

### Dust as the Siege tower dies - Dust as the Siege tower dies

- 内部名: `EFFECT_SIEGE_TOWER_DIE`
- その他の設定:
  - `fScale`: 2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/settler_smoke/SettlerSmoke.nif

### B-52's bomb explosion - B-52's bomb explosion

- 内部名: `EFFECT_B52_BOMB_EXPLODE`
- その他の設定:
  - `fScale`: 0.4
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_large_001/fx_explosion_large_001.NIF
  - `fSpeed`: 400.0

### Jet Fighter Missile - Jet Fighter Missile

- 内部名: `EFFECT_JETFIGHTER_MISSILE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/JetFighter/JetFighterMissile.NIF
  - `bIsProjectile`: 1
  - `fSpeed`: 800.0

### Jet Fighter Bomb Animations - Jet Fighter Bomb Animations

- 内部名: `EFFECT_JETFIGHTER_BOMB`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/JetFighter/JetFighterBomb.kfm
  - `bIsProjectile`: 1
  - `fSpeed`: 400.0

### Bomber Bomb Animations - Bomber Bomb Animations

- 内部名: `EFFECT_BOMBER_BOMB`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Bomber/BomberBomb.kfm
  - `bIsProjectile`: 1
  - `fSpeed`: 400.0

### Stealth Bomber Bomb Animations - Stealth Bomber Bomb Animations

- 内部名: `EFFECT_STEALTHBOMBER_BOMB`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/StealthBomber/StealthBomberBomb.kfm
  - `bIsProjectile`: 1
  - `fSpeed`: 400.0

### Jet Fighter Bomb Explosion - Jet Fighter Bomb Explosion

- 内部名: `EFFECT_JETFIGHTER_BOMB_EXPLODE`
- その他の設定:
  - `fScale`: 0.1
  - `fUpdateRate`: 1.5
  - `Path`: Art/Effects/explosion_large_001/fx_explosion_large_001.NIF

### Stealth BomberBomb Explosion - Stealth BomberBomb Explosion

- 内部名: `EFFECT_STEALTHBOMBER_BOMB_EXPLODE`
- その他の設定:
  - `fScale`: 0.15
  - `fUpdateRate`: 1.2
  - `Path`: Art/Effects/explosion_large_001/fx_explosion_large_001.NIF

### Bomber Bomb Explosion - Bomber Bomb Explosion

- 内部名: `EFFECT_BOMBER_BOMB_EXPLODE`
- その他の設定:
  - `fScale`: 0.05
  - `fUpdateRate`: 1.7
  - `Path`: Art/Effects/explosion_large_001/fx_explosion_large_001.NIF

### Stealth Bomber's bomb explosion - Stealth Bomber's bomb explosion

- 内部名: `EFFECT_STEALTH_BOMB_EXPLODE`
- その他の設定:
  - `fScale`: 0.6
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_large_001/fx_explosion_large_001.NIF

### Stealth Bomber's bomb explosion - Stealth Bomber's bomb explosion

- 内部名: `EFFECT_STEALTH_BOMB_EXPLODE_2`
- その他の設定:
  - `fScale`: 0.4
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_large_001/fx_explosion_large_001.NIF

### Jet Fighter's missile explosion - Jet Fighter's missile explosion

- 内部名: `EFFECT_JET_MISSILE_EXPLODE`
- その他の設定:
  - `fScale`: 0.4
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_large_001/fx_explosion_large_001.NIF

### The Nuclear Explosion - The Nuclear Explosion

- 内部名: `EFFECT_ICBM_NUCLEAR_EXPLOSION`
- その他の設定:
  - `fScale`: 0.6
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_nuke/fx_explosion_nuke.nif

### Small fire ball for on ICBM - Small fire ball for on ICBM

- 内部名: `EFFECT_ICBM_FIREBALL_SMALL`
- その他の設定:
  - `fScale`: 0.20
  - `fUpdateRate`: 2.0
  - `Path`: Art/Effects/fireball_airplane/fx_fireball_airplane.nif

### Large fire ball for on ICBM - Large fire ball for on ICBM

- 内部名: `EFFECT_ICBM_FIREBALL_LARGE`
- その他の設定:
  - `fScale`: 0.4
  - `fUpdateRate`: 1.6
  - `Path`: Art/Effects/fireball_airplane/fx_fireball_airplane.nif

### Laser Effect for a Blocked ICBM - Laser Effect for a Blocked ICBM

- 内部名: `EFFECT_ICBM_SW_LASER`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/ICBM_Laser/ICBM_Laser.nif

### Boulder explosion in Dirt - Boulder explosion in Dirt

- 内部名: `EFFECT_BOULDER_IMPACT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_dirt_02/fx_explosion_dirt_02.nif

### Small Rock explosion for a Hit Catapult - Small Rock explosion for a Hit Catapult

- 内部名: `EFFECT_CATAPULT_HIT_SMALL`
- その他の設定:
  - `fScale`: 0.20
  - `fUpdateRate`: 3.0
  - `Path`: Art/Effects/explosion_dirt_02/fx_explosion_dirt_02.nif

### Boulder explosion for Catapult Death - Boulder explosion for Catapult Death

- 内部名: `EFFECT_CATAPULT_HIT_LARGE`
- その他の設定:
  - `fScale`: 0.32
  - `fUpdateRate`: 2.7
  - `Path`: Art/Effects/explosion_dirt_02/fx_explosion_dirt_02.nif

### Artillery's Shell explosion - Artillery's Shell explosion

- 内部名: `EFFECT_ARTILLERY_SHELL_EXPLODE`
- その他の設定:
  - `fScale`: 0.4
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_large_001/fx_explosion_large_001.NIF

### Death fire for wooden cannon - Death fire for wooden cannon

- 内部名: `EFFECT_CANNON_DEATH_FIRE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/fire_dead_cannon/fx_fire_dead_cannon.nif

### large fire ball for on airplanes - large fire ball for on airplanes

- 内部名: `EFFECT_AIRPLANE_FIREBALL_LARGE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/fireball_airplane/fx_fireball_airplane.nif
  - `bSticky`: 1

### Small fire ball for on airplanes - Small fire ball for on airplanes

- 内部名: `EFFECT_AIRPLANE_FIREBALL_SMALL`
- その他の設定:
  - `fScale`: 0.7
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/fireball_airplane/fx_fireball_airplane.nif
  - `bSticky`: 1

### Small fire ball for on Fighter - Small fire ball for on Fighter

- 内部名: `EFFECT_FIGHTER_FIREBALL_SMALL`
- その他の設定:
  - `fScale`: 0.25
  - `fUpdateRate`: 1.5
  - `Path`: Art/Effects/fireball_airplane/fx_fireball_airplane.nif
  - `bSticky`: 1

### large fire ball for on Fighter - large fire ball for on Fighter

- 内部名: `EFFECT_FIGHTER_FIREBALL_LARGE`
- その他の設定:
  - `fScale`: .6
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/fireball_airplane/fx_fireball_airplane.nif
  - `bSticky`: 1

### Small fire ball for on Bomber - Small fire ball for on Bomber

- 内部名: `EFFECT_BOMBER_FIREBALL_SMALL`
- その他の設定:
  - `fScale`: 0.4
  - `fUpdateRate`: 1.4
  - `Path`: Art/Effects/fireball_airplane/fx_fireball_airplane.nif
  - `bSticky`: 1

### large fire ball for on Bomber - large fire ball for on Bomber

- 内部名: `EFFECT_BOMBER_FIREBALL_LARGE`
- その他の設定:
  - `fScale`: .9
  - `fUpdateRate`: 1.2
  - `Path`: Art/Effects/fireball_airplane/fx_fireball_airplane.nif
  - `bSticky`: 1

### Small fire ball for on Jet Fighter - Small fire ball for on Jet Fighter

- 内部名: `EFFECT_JETFIGHTER_FIREBALL_SMALL`
- その他の設定:
  - `fScale`: 0.8
  - `fUpdateRate`: 1.4
  - `Path`: Art/Effects/fireball_airplane/fx_fireball_airplane.nif
  - `bSticky`: 1

### large fire ball for on Jet Fighter - large fire ball for on Jet Fighter

- 内部名: `EFFECT_JETFIGHTER_FIREBALL_LARGE`
- その他の設定:
  - `fScale`: 1.4
  - `fUpdateRate`: 0.9
  - `Path`: Art/Effects/fireball_airplane/fx_fireball_airplane.nif
  - `bSticky`: 1

### Small fire ball for on Stealth Bomber - Small fire ball for on Stealth Bomber

- 内部名: `EFFECT_STEALTHBOMBER_FIREBALL_SMALL`
- その他の設定:
  - `fScale`: 0.45
  - `fUpdateRate`: 1.3
  - `Path`: Art/Effects/fireball_airplane/fx_fireball_airplane.nif
  - `bSticky`: 1

### large fire ball for on Stealth Bomber - large fire ball for on Stealth Bomber

- 内部名: `EFFECT_STEALTHBOMBER_FIREBALL_LARGE`
- その他の設定:
  - `fScale`: .85
  - `fUpdateRate`: .8
  - `Path`: Art/Effects/fireball_airplane/fx_fireball_airplane.nif
  - `bSticky`: 1

### Variation 01 for Gunship - Variation 01 for Gunship

- 内部名: `EFFECT_GUNSHIPSMALLEXPLODE01`
- その他の設定:
  - `fScale`: 0.35
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_on_vehicle/fx_explosion_on_vehicle_01.nif

### Variation 02 for Gunship - Variation 02 for Gunship

- 内部名: `EFFECT_GUNSHIPSMALLEXPLODE02`
- その他の設定:
  - `fScale`: 0.3
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_on_vehicle/fx_explosion_on_vehicle_01.nif

### Large Explosion for the death of the Gunship - Large Explosion for the death of the Gunship

- 内部名: `EFFECT_GUNSHIP_DEATH_EXPLOSION`
- その他の設定:
  - `fScale`: 0.15
  - `fUpdateRate`: 0.8
  - `Path`: Art/Effects/Unit_Explosion_Oil/fx_UNIT_oil_death_explosion.nif

### Grenadier grenade explosion - Grenadier grenade explosion

- 内部名: `EFFECT_GRENADIER_EXPLOSION`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: .8
  - `Path`: Art/Effects/ShipExplosion_gunpowder_hit/fx_ship_gunpowder_small_explosion.nif

### Small oily hit explosion - Small oily hit explosion

- 内部名: `EFFECT_OILY_HIT`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/ShipExplosion_Oil_Hit/fx_ship_oil_small_explosion.nif

### Larger Oily hit explosion for Transport Version 1 - Larger Oily hit explosion for Transport Version 1

- 内部名: `EFFECT_TRANSPORT_HIT01`
- その他の設定:
  - `fScale`: 0.12
  - `fUpdateRate`: 1.4
  - `Path`: Art/Effects/ShipExplosion_Oil_Hit/fx_ship_oil_small_explosion.nif

### Smaller Oily hit explosion for Transport Version 2 - Smaller Oily hit explosion for Transport Version 2

- 内部名: `EFFECT_TRANSPORT_HIT02`
- その他の設定:
  - `fScale`: 0.1
  - `fUpdateRate`: 1.2
  - `Path`: Art/Effects/ShipExplosion_Oil_Hit/fx_ship_oil_small_explosion.nif

### Larger Oily hit explosion for Destroyer - Larger Oily hit explosion for Destroyer

- 内部名: `EFFECT_DESTROYER_HIT01`
- その他の設定:
  - `fScale`: 0.15
  - `fUpdateRate`: 1.5
  - `Path`: Art/Effects/ShipExplosion_Oil_Hit/fx_ship_oil_small_explosion.nif

### Smaller Oily hit explosion for Destroyer - Smaller Oily hit explosion for Destroyer

- 内部名: `EFFECT_DESTROYER_HIT02`
- その他の設定:
  - `fScale`: 0.1
  - `fUpdateRate`: 1.8
  - `Path`: Art/Effects/ShipExplosion_Oil_Hit/fx_ship_oil_small_explosion.nif

### Larger Oily hit explosion for Destroyer - Larger Oily hit explosion for Destroyer

- 内部名: `EFFECT_BATTLESHIP_HIT01`
- その他の設定:
  - `fScale`: 0.17
  - `fUpdateRate`: 1.3
  - `Path`: Art/Effects/ShipExplosion_Oil_Hit/fx_ship_oil_small_explosion.nif

### Smaller Oily hit explosion for Destroyer - Smaller Oily hit explosion for Destroyer

- 内部名: `EFFECT_BATTLESHIP_HIT02`
- その他の設定:
  - `fScale`: 0.12
  - `fUpdateRate`: 1.6
  - `Path`: Art/Effects/ShipExplosion_Oil_Hit/fx_ship_oil_small_explosion.nif

### Larger Oily hit explosion for Carrier - Larger Oily hit explosion for Carrier

- 内部名: `EFFECT_CARRIER_HIT01`
- その他の設定:
  - `fScale`: 0.19
  - `fUpdateRate`: 1.2
  - `Path`: Art/Effects/ShipExplosion_Oil_Hit/fx_ship_oil_small_explosion.nif

### Smaller Oily hit explosion for Carrier - Smaller Oily hit explosion for Carrier

- 内部名: `EFFECT_CARRIER_HIT02`
- その他の設定:
  - `fScale`: 0.14
  - `fUpdateRate`: 1.5
  - `Path`: Art/Effects/ShipExplosion_Oil_Hit/fx_ship_oil_small_explosion.nif

### Oily smoke for high damage on late vehicles - Oily smoke for high damage on late vehicles

- 内部名: `EFFECT_UNIT_DESTRUCTION_OILY_SMOKE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_damage_smoke_oily/fx_unit_damage_oily_smoke.nif

### Oily smoke and fire for high damage on late vehicles - Oily smoke and fire for high damage on late vehicles

- 内部名: `EFFECT_UNIT_DESTRUCTION_OILY_FIRE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_damage_smoke_oily/fx_unit_damage_oily_fire_and_smoke.nif

### explosion when late modern mechanical units bite the dust - explosion when late modern mechanical units bite the dust

- 内部名: `EFFECT_LARGE_OILY_DEATH`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Unit_Explosion_Oil/fx_UNIT_oil_death_explosion.nif

### explosion when early modern mechanical units bite the dust - explosion when early modern mechanical units bite the dust

- 内部名: `EFFECT_LARGE_GUNPOWDER_DEATH`
- その他の設定:
  - `fScale`: 0.2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Unit_Explosion_gunpowdery/fx_unit_gunpowdery_death_explosion.nif

### Shockwave to add to specific unit explosion - Shockwave to add to specific unit explosion

- 内部名: `EFFECT_EXPLOSION_SHOCKWAVE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_shockwave/fx_explosion_shockwave.nif

### Large death explosion for gunpowder water-vehicles - Large death explosion for gunpowder water-vehicles

- 内部名: `EFFECT_SHIP_GUNPOWDER_DEATH`
- その他の設定:
  - `fScale`: 0.2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/ShipExplosion/fx_ship_destruction_explosion.nif

### Large death explosion for Caravel - Large death explosion for Caravel

- 内部名: `EFFECT_SHIP_CARAVEL_DEATH`
- その他の設定:
  - `fScale`: 0.15
  - `fUpdateRate`: 1.2
  - `Path`: Art/Effects/ShipExplosion/fx_ship_destruction_explosion.nif

### Large death explosion for Galleon - Large death explosion for Galleon

- 内部名: `EFFECT_SHIP_GALLEON_DEATH`
- その他の設定:
  - `fScale`: 0.3
  - `fUpdateRate`: 1.1
  - `Path`: Art/Effects/ShipExplosion/fx_ship_destruction_explosion.nif

### Large death explosion for Frigate - Large death explosion for Frigate

- 内部名: `EFFECT_SHIP_FRIGATE_DEATH`
- その他の設定:
  - `fScale`: 0.26
  - `fUpdateRate`: 1.2
  - `Path`: Art/Effects/ShipExplosion/fx_ship_destruction_explosion.nif

### Large death explosion for Ironclad - Large death explosion for Ironclad

- 内部名: `EFFECT_SHIP_IRONCLAD_DEATH`
- その他の設定:
  - `fScale`: 0.08
  - `fUpdateRate`: 1.4
  - `Path`: Art/Effects/ShipExplosion/fx_ship_destruction_explosion.nif

### Large death explosion for WorkBoat Modern - Large death explosion for WorkBoat Modern

- 内部名: `EFFECT_SHIP_WORKBOATMODERN_DEATH`
- その他の設定:
  - `fScale`: 0.16
  - `fUpdateRate`: 1.4
  - `Path`: Art/Effects/ShipExplosion/fx_ship_destruction_explosion.nif

### Large death explosion for Destroyer - Large death explosion for Destroyer

- 内部名: `EFFECT_SHIP_TRANSPORT_DEATH`
- その他の設定:
  - `fScale`: 0.04
  - `fUpdateRate`: 1.4
  - `Path`: Art/Effects/ShipExplosion/fx_ship_destruction_explosion.nif

### Large death explosion for Destroyer - Large death explosion for Destroyer

- 内部名: `EFFECT_SHIP_DESTROYER_DEATH`
- その他の設定:
  - `fScale`: 0.05
  - `fUpdateRate`: 1.2
  - `Path`: Art/Effects/ShipExplosion/fx_ship_destruction_explosion.nif

### Large death explosion for Battleship - Large death explosion for Battleship

- 内部名: `EFFECT_SHIP_BATTLESHIP_DEATH`
- その他の設定:
  - `fScale`: 0.06
  - `fUpdateRate`: 1.1
  - `Path`: Art/Effects/ShipExplosion/fx_ship_destruction_explosion.nif

### Large death explosion for Battleship - Large death explosion for Battleship

- 内部名: `EFFECT_SHIP_CARRIER_DEATH01`
- その他の設定:
  - `fScale`: 0.07
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/ShipExplosion/fx_ship_destruction_explosion.nif

### Large death explosion for Battleship - Large death explosion for Battleship

- 内部名: `EFFECT_SHIP_CARRIER_DEATH02`
- その他の設定:
  - `fScale`: 0.05
  - `fUpdateRate`: 1.2
  - `Path`: Art/Effects/ShipExplosion/fx_ship_destruction_explosion.nif

### Large death explosion for Oil water-vehicles - Large death explosion for Oil water-vehicles

- 内部名: `EFFECT_SHIP_OIL_DEATH`
- その他の設定:
  - `fScale`: 0.2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/ShipExplosion_Oil/fx_ship_oil_death_explosion.nif

### Explosion in Dirt - Explosion in Dirt

- 内部名: `EFFECT_EXPLOSION_DIRT`
- その他の設定:
  - `fScale`: 0.6
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_dirt_01/fx_explosion_dirt_01.nif

### Explosion for on hard surfaces like modern vehicles - Explosion for on hard surfaces like modern vehicles

- 内部名: `EFFECT_EXPLOSION_ON_VEHICLE`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_on_vehicle/fx_explosion_on_vehicle_01.nif

### Variation 01 for Tanks - Variation 01 for Tanks

- 内部名: `EFFECT_TANKSMALLEXPLODE01`
- その他の設定:
  - `fScale`: 0.3
  - `fUpdateRate`: 0.9
  - `Path`: Art/Effects/explosion_on_vehicle/fx_explosion_on_vehicle_01.nif

### Variation 02 for Tanks - Variation 02 for Tanks

- 内部名: `EFFECT_TANKSMALLEXPLODE02`
- その他の設定:
  - `fScale`: 0.2
  - `fUpdateRate`: 0.9
  - `Path`: Art/Effects/explosion_on_vehicle/fx_explosion_on_vehicle_01.nif

### Variation 03 for Tanks - Variation 03 for Tanks

- 内部名: `EFFECT_TANKSMALLEXPLODE03`
- その他の設定:
  - `fScale`: 0.15
  - `fUpdateRate`: 0.9
  - `Path`: Art/Effects/explosion_on_vehicle/fx_explosion_on_vehicle_01.nif

### Large Explosion for the death of a tank - Large Explosion for the death of a tank

- 内部名: `EFFECT_PANZER_DEATH_EXPLOSION`
- その他の設定:
  - `fScale`: 0.1
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Unit_Explosion_Oil/fx_UNIT_oil_death_explosion.nif

### Variation 01 for Artillery - Variation 01 for Artillery

- 内部名: `EFFECT_ARTILLERY_HIT_SMALL01`
- その他の設定:
  - `fScale`: 0.25
  - `fUpdateRate`: 1.1
  - `Path`: Art/Effects/explosion_on_vehicle/fx_explosion_on_vehicle_01.nif

### Variation 02 for Artillery - Variation 02 for Artillery

- 内部名: `EFFECT_ARTILLERY_HIT_SMALL02`
- その他の設定:
  - `fScale`: 0.16
  - `fUpdateRate`: 1.2
  - `Path`: Art/Effects/explosion_on_vehicle/fx_explosion_on_vehicle_01.nif

### Large Explosion for the death of Artillery - Large Explosion for the death of Artillery

- 内部名: `EFFECT_ARTILLERY_DEATH_EXPLOSION`
- その他の設定:
  - `fScale`: 0.08
  - `fUpdateRate`: 1.2
  - `Path`: Art/Effects/Unit_Explosion_Oil/fx_UNIT_oil_death_explosion.nif

### Variation 01 for MachineGunner - Variation 01 for MachineGunner

- 内部名: `EFFECT_MACHINEGUNNER_HIT_SMALL01`
- その他の設定:
  - `fScale`: 0.22
  - `fUpdateRate`: 1.3
  - `Path`: Art/Effects/explosion_on_vehicle/fx_explosion_on_vehicle_01.nif

### Variation 02 for MachineGunner - Variation 02 for MachineGunner

- 内部名: `EFFECT_MACHINEGUNNER_HIT_SMALL02`
- その他の設定:
  - `fScale`: 0.13
  - `fUpdateRate`: 1.4
  - `Path`: Art/Effects/explosion_on_vehicle/fx_explosion_on_vehicle_01.nif

### Large Explosion for the death of MachineGunner - Large Explosion for the death of MachineGunner

- 内部名: `EFFECT_MACHINEGUNNER_DEATH_EXPLOSION`
- その他の設定:
  - `fScale`: 0.05
  - `fUpdateRate`: 1.5
  - `Path`: Art/Effects/Unit_Explosion_Oil/fx_UNIT_oil_death_explosion.nif

### Explosion for on surface of plane before fireball - Explosion for on surface of plane before fireball

- 内部名: `EFFECT_EXPLOSION_ON_PLANE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_on_vehicle/fx_explosion_on_vehicle_01.nif

### explosion when small planes hit the ground - explosion when small planes hit the ground

- 内部名: `EFFECT_SMALL_PLANE_DEATH`
- その他の設定:
  - `fScale`: 0.3
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_large_001/fx_explosion_large_001.NIF

### explosion when large planes hit the ground - explosion when large planes hit the ground

- 内部名: `EFFECT_LARGE_PLANE_DEATH`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_large_001/fx_explosion_large_001.NIF

### Machine gun shot hitting vehicle or unit - Machine gun shot hitting vehicle or unit

- 内部名: `EFFECT_MACHINEGUN_VEHICLE_HIT`
- その他の設定:
  - `fScale`: 0.3
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_on_vehicle/fx_explosion_on_vehicle_01.nif

### Machine gun shot hitting dirt - Machine gun shot hitting dirt

- 内部名: `EFFECT_MACHINEGUN_DIRT_HIT`
- その他の設定:
  - `fScale`: 0.3
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_dirt_01/fx_explosion_dirt_01.nif

### aircraft machine gun impact explosion with dirt flying up - aircraft machine gun impact explosion with dirt flying up

- 内部名: `EFFECT_AIRCRAFT_MACHINE_GUN_IMPACT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_dirt_01/fx_explosion_dirt_01.nif

### Cannonball impact - Cannonball impact

- 内部名: `EFFECT_CANNONBALL_IMPACT`
- その他の設定:
  - `fScale`: 0.6
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_dirt_01/fx_explosion_dirt_01.nif

### Small Gunpowdery hit explosion for water-vehicles - Small Gunpowdery hit explosion for water-vehicles

- 内部名: `EFFECT_SHIP_GUNPOWDER_HIT`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/ShipExplosion_gunpowder_hit/fx_ship_gunpowder_small_explosion.nif

### Small Gunpowdery hit explosion for Caravel Version 1 - Small Gunpowdery hit explosion for Caravel Version 1

- 内部名: `EFFECT_CARAVEL_HIT01`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.5
  - `Path`: Art/Effects/ShipExplosion_gunpowder_hit/fx_ship_gunpowder_small_explosion.nif

### Small Gunpowdery hit explosion for Caravel Version 2 - Small Gunpowdery hit explosion for Caravel Version 2

- 内部名: `EFFECT_CARAVEL_HIT02`
- その他の設定:
  - `fScale`: 0.55
  - `fUpdateRate`: 1.4
  - `Path`: Art/Effects/ShipExplosion_gunpowder_hit/fx_ship_gunpowder_small_explosion.nif

### Small Gunpowdery hit explosion for Galleon Version 1 - Small Gunpowdery hit explosion for Galleon Version 1

- 内部名: `EFFECT_GALLEON_HIT01`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.4
  - `Path`: Art/Effects/ShipExplosion_gunpowder_hit/fx_ship_gunpowder_small_explosion.nif

### Small Gunpowdery hit explosion for Galleon Version 2 - Small Gunpowdery hit explosion for Galleon Version 2

- 内部名: `EFFECT_GALLEON_HIT02`
- その他の設定:
  - `fScale`: 1.1
  - `fUpdateRate`: 1.3
  - `Path`: Art/Effects/ShipExplosion_gunpowder_hit/fx_ship_gunpowder_small_explosion.nif

### Small Gunpowdery hit explosion for Frigate Version 1 - Small Gunpowdery hit explosion for Frigate Version 1

- 内部名: `EFFECT_FRIGATE_HIT01`
- その他の設定:
  - `fScale`: 0.85
  - `fUpdateRate`: 1.5
  - `Path`: Art/Effects/ShipExplosion_gunpowder_hit/fx_ship_gunpowder_small_explosion.nif

### Small Gunpowdery hit explosion for Frigate Version 2 - Small Gunpowdery hit explosion for Frigate Version 2

- 内部名: `EFFECT_FRIGATE_HIT02`
- その他の設定:
  - `fScale`: 0.98
  - `fUpdateRate`: 1.4
  - `Path`: Art/Effects/ShipExplosion_gunpowder_hit/fx_ship_gunpowder_small_explosion.nif

### Small Gunpowdery hit explosion for Ironclad Version 1 - Small Gunpowdery hit explosion for Ironclad Version 1

- 内部名: `EFFECT_IRONCLAD_HIT01`
- その他の設定:
  - `fScale`: 0.22
  - `fUpdateRate`: 1.6
  - `Path`: Art/Effects/ShipExplosion_gunpowder_hit/fx_ship_gunpowder_small_explosion.nif

### Small Gunpowdery hit explosion for Ironclad Version 2 - Small Gunpowdery hit explosion for Ironclad Version 2

- 内部名: `EFFECT_IRONCLAD_HIT02`
- その他の設定:
  - `fScale`: 0.25
  - `fUpdateRate`: 1.5
  - `Path`: Art/Effects/ShipExplosion_gunpowder_hit/fx_ship_gunpowder_small_explosion.nif

### Small Gunpowdery hit explosion for WorkboatModernVersion 1 - Small Gunpowdery hit explosion for WorkboatModernVersion 1

- 内部名: `EFFECT_WORKBOATMODERN_HIT01`
- その他の設定:
  - `fScale`: 0.4
  - `fUpdateRate`: 1.6
  - `Path`: Art/Effects/ShipExplosion_gunpowder_hit/fx_ship_gunpowder_small_explosion.nif

### Small Gunpowdery hit explosion for WorkboatModernVersion 2 - Small Gunpowdery hit explosion for WorkboatModernVersion 2

- 内部名: `EFFECT_WORKBOATMODERN_HIT02`
- その他の設定:
  - `fScale`: 0.45
  - `fUpdateRate`: 1.5
  - `Path`: Art/Effects/ShipExplosion_gunpowder_hit/fx_ship_gunpowder_small_explosion.nif

### Small oily hit explosion for water-vehicles - Small oily hit explosion for water-vehicles

- 内部名: `EFFECT_SHIP_OIL_HIT`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/ShipExplosion_Oil_Hit/fx_ship_oil_small_explosion.nif

### pre gunpowder small flash impact on early vessels - pre gunpowder small flash impact on early vessels

- 内部名: `EFFECT_IMPACT_FLASH`
- その他の設定:
  - `fScale`: 6
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/kapow_003/fx_kapow_003.nif

### Small splashy hit for submarine - Small splashy hit for submarine

- 内部名: `EFFECT_SHIP_SUBMARINE_HIT`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Water_Splash_Submarine_Hit/fx_water_splash_submarine_hit.nif

### Small splash hit for submarine - Small splash hit for submarine

- 内部名: `EFFECT_SUBMARINE_HIT_SPLASH`
- その他の設定:
  - `fScale`: 0.4
  - `fUpdateRate`: 2.0
  - `Path`: Art/Effects/Water_Splash_Submarine_Hit/fx_water_splash_submarine_hit.nif

### Small explosion hit for submarine - Small explosion hit for submarine

- 内部名: `EFFECT_SUBMARINE_HIT_EXPLODE`
- その他の設定:
  - `fScale`: 0.25
  - `fUpdateRate`: 6.0
  - `Path`: Art/Effects/water_submerged_explosion/fx_water_submerged_explosion.nif

### Large Death Explosion for Submarine - Large Death Explosion for Submarine

- 内部名: `EFFECT_SUBMARINE_DEATH`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 2.5
  - `Path`: Art/Effects/water_submerged_explosion/fx_water_submerged_explosion.nif

### Explosion Over Land - Explosion Over Land

- 内部名: `EFFECT_EXPLOSION_LARGE_001`
- その他の設定:
  - `fScale`: 0.2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_large_001/fx_explosion_large_001.NIF

### One big city sized explosion - One big city sized explosion

- 内部名: `EFFECT_EXPLOSION_CITY`
- その他の設定:
  - `fScale`: 0.2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_large_001/fx_explosion_large_001.NIF

### OLD Bombard - OLD Bombard

- 内部名: `EFFECT_BOMBARD`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/ShipExplosion/fx_ship_destruction_explosion.nif

### OLD Ship Explosion Over Water - OLD Ship Explosion Over Water

- 内部名: `EFFECT_EXPLOSION_02`
- その他の設定:
  - `fScale`: 0.2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/ShipExplosion/fx_ship_destruction_explosion.nif

### OLD Ship Explosion Over Water - OLD Ship Explosion Over Water

- 内部名: `EFFECT_EXPLOSION_01`
- その他の設定:
  - `fScale`: 0.4
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/ShipExplosion/fx_ship_destruction_explosion.nif

### Small Gunpowdery hit explosion for Cannon Version 1 - Small Gunpowdery hit explosion for Cannon Version 1

- 内部名: `EFFECT_CANNON_HIT_SMALL01`
- その他の設定:
  - `fScale`: 0.35
  - `fUpdateRate`: 1.6
  - `Path`: Art/Effects/ShipExplosion_gunpowder_hit/fx_ship_gunpowder_small_explosion.nif

### Small Gunpowdery hit explosion for Cannon Version 2 - Small Gunpowdery hit explosion for Cannon Version 2

- 内部名: `EFFECT_CANNON_HIT_SMALL02`
- その他の設定:
  - `fScale`: 0.3
  - `fUpdateRate`: 1.5
  - `Path`: Art/Effects/ShipExplosion_gunpowder_hit/fx_ship_gunpowder_small_explosion.nif

### Large death explosion for Cannon - Large death explosion for Cannon

- 内部名: `EFFECT_CANNON_DEATH_EXPLOSION`
- その他の設定:
  - `fScale`: 0.05
  - `fUpdateRate`: 1.4
  - `Path`: Art/Effects/ShipExplosion/fx_ship_destruction_explosion.nif

### Frosty swirling air flow - Frosty swirling air flow

- 内部名: `EFFECT_WIND_SWIRL`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/wind_swirl/fx_wind_swirl_01.nif

### aircraft jet engine contrail smoke - aircraft jet engine contrail smoke

- 内部名: `EFFECT_SMOKE_JET_CONTRAIL`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Smoke_Contrail/fx_smoke_contrail.nif

### missile contrail smoke - missile contrail smoke

- 内部名: `EFFECT_SMOKE_PROJECTILE_CONTRAIL`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/smoke_missile_contrail/fx_smoke_missile_contrail.nif

### Jet afterburn - Jet afterburn

- 内部名: `EFFECT_JET_AFTERBURN`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/fire_afterburn/fx_fire_afterburn.nif

### Jet afterburn - Jet afterburn

- 内部名: `EFFECT_MISSILE_AFTERBURN`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/fire_afterburn/fx_fire_afterburn.nif

### air flow behind bomb - air flow behind bomb

- 内部名: `EFFECT_BOMBER_BOMB_WIND`
- その他の設定:
  - `fScale`: 0.7
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/wind_swirl/fx_wind_swirl_01.nif

### Cannonball smoke trail - Cannonball smoke trail

- 内部名: `EFFECT_SMOKETRAIL`
- その他の設定:
  - `fScale`: 0.7
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Smoke_Contrail/fx_smoke_contrail.nif

### Catapult Boulder smoke trail - Catapult Boulder smoke trail

- 内部名: `EFFECT_BOULDER_SMOKETRAIL`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Smoke_Contrail/fx_smoke_contrail.nif

### Ironclad smokestack smoke - Ironclad smokestack smoke

- 内部名: `EFFECT_SMOKESTACK_SMOKE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/smokestack_smoke/smokestack_smoke.nif

### Hoof dust for a running horse - Hoof dust for a running horse

- 内部名: `EFFECT_HORSEHOOFDUST`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/dust_impact_002/fx_dust_impact_002.nif

### Tank Unit Exhaust - Tank Unit Exhaust

- 内部名: `EFFECT_TANK_EXHAUST`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/smoke_tank_exhaust/fx_smoke_tank_exhaust.nif

### Gunpowdery smoke for high damage on water-vehicles - Gunpowdery smoke for high damage on water-vehicles

- 内部名: `EFFECT_SHIP_DAMAGE_GUNPOWDER_SMOKE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/ship_damage_smoke_gunpowder/fx_ship_damage_gunpowder_smoke.nif

### Gunpowdery smoke and fire for high damage on water-vehicles - Gunpowdery smoke and fire for high damage on water-vehicles

- 内部名: `EFFECT_SHIP_DAMAGE_FIREY_GUNPOWDER_SMOKE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/ship_damage_smoke_gunpowder/fx_ship_damage_gunpowder_fire_and_smoke.nif

### Oily smoke for high damage on water-vehicles - Oily smoke for high damage on water-vehicles

- 内部名: `EFFECT_SHIP_DAMAGE_OILY_SMOKE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/ship_damage_smoke_oily/fx_ship_damage_oily_smoke.nif

### OIly smoke and fire for high damage on water-vehicles - OIly smoke and fire for high damage on water-vehicles

- 内部名: `EFFECT_SHIP_DAMAGE_FIREY_OILY_SMOKE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/ship_damage_smoke_oily/fx_ship_damage_oily_fire_and_smoke.nif

### Smokey discharge for highest level of unit damage - Smokey discharge for highest level of unit damage

- 内部名: `EFFECT_UNIT_DESTRUCTION_SMOKEY`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_damage_smoke/fx_unit_damage_smokey.nif

### Fire with smoke for highest level of unit damage - Fire with smoke for highest level of unit damage

- 内部名: `EFFECT_UNIT_DESTRUCTION_FIRE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_damage_smoke/fx_unit_damage_fire_and_smoke.nif

### Dark Smoke - Dark Smoke

- 内部名: `LOOPINGEFFECT_SMOKE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/chimney_smoke/fx_chimneysmoke_01.nif

### aircraft machine gun fire - aircraft machine gun fire

- 内部名: `EFFECT_AIRCRAFT_MACHINE_GUN`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/weapon_rifleblast_modern/fx_rifleblast_modern.nif

### Gunship machine gun fire - Gunship machine gun fire

- 内部名: `EFFECT_GUNSHIP_MACHINE_GUN`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 2.0
  - `Path`: Art/Effects/weapon_rifleblast_modern/fx_rifleblast_modern.nif

### Boulder Explosion for Catapult Attack - Boulder Explosion for Catapult Attack

- 内部名: `EFFECT_CATAPULT_ROCK_EXPLODE`
- その他の設定:
  - `fScale`: 0.6
  - `fUpdateRate`: 2.5
  - `Path`: Art/Effects/explosion_dirt_02/fx_explosion_dirt_02.nif

### Fighter machine gun fire - Fighter machine gun fire

- 内部名: `EFFECT_MACHINEGUNFIRE_AIR`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.2
  - `Path`: Art/Effects/weapon_rifleblast_modern/fx_rifleblast_modern.nif
  - `bSticky`: 1

### Fighter machine gun fire - Fighter machine gun fire

- 内部名: `EFFECT_FIGHTER_MACHINE_GUN_BOMB`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.2
  - `Path`: Art/Effects/weapon_machinegun_flash/fx_weapon_machinegun_flash.nif

### Rifleblast for flintlock rifle - Rifleblast for flintlock rifle

- 内部名: `EFFECT_RIFLEBLAST`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/weapon_rifleblast_old/fx_rifleblast_old.nif

### Rifleblast for flintlock rifle - Rifleblast for flintlock rifle

- 内部名: `EFFECT_RIFLEBLAST_MUSKETEER`
- その他の設定:
  - `fScale`: .8
  - `fUpdateRate`: 1.3
  - `Path`: Art/Effects/weapon_rifleblast_old/fx_rifleblast_old.nif

### Old rifleblast more powerful - Old rifleblast more powerful

- 内部名: `EFFECT_RIFLEBLAST_OLD_POWERFUL`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/weapon_rifleblast_old_powerful/fx_rifleblast_old_powerful.nif

### Rifleblast for modern rifle - Rifleblast for modern rifle

- 内部名: `EFFECT_RIFLEBLAST_MODERN`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/weapon_rifleblast_modern/fx_rifleblast_modern.nif

### Rifleblast for Flamethrower - Rifleblast for Flamethrower

- 内部名: `EFFECT_RIFLEBLAST_FLAMES`
- その他の設定:
  - `fScale`: 2.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/FlameThrower/firespray_sfx.nif

### MachineGun Blast for Transport - MachineGun Blast for Transport

- 内部名: `EFFECT_TRANSPORT_MACHINEGUN`
- その他の設定:
  - `fScale`: 0.3
  - `fUpdateRate`: 1.4
  - `Path`: Art/Effects/weapon_rifleblast_modern/fx_rifleblast_modern.nif

### smokeblast for front of SAM launcher as it fires - smokeblast for front of SAM launcher as it fires

- 内部名: `EFFECT_SAM_FRONT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/weapon_sam_launcher/fx_weapon_sam_front.nif

### Exhaust for rear of SAM launcher as it fires - Exhaust for rear of SAM launcher as it fires

- 内部名: `EFFECT_SAM_EXHAUST`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/weapon_sam_launcher/fx_weapon_sam_exhaust.nif

### ancient cannonfire - ancient cannonfire

- 内部名: `EFFECT_WEAPON_CANNONFIRE`
- その他の設定:
  - `fScale`: 0.2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/weapon_cannonfire/fx_weapon_cannonfire_01.nif

### a variant of ancient cannonfire - a variant of ancient cannonfire

- 内部名: `EFFECT_WEAPON_CANNONFIRE_2`
- その他の設定:
  - `fScale`: 0.2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/weapon_cannonfire/fx_weapon_cannonfire_02.nif

### yet another variant of ancient cannonfire - yet another variant of ancient cannonfire

- 内部名: `EFFECT_WEAPON_CANNONFIRE_3`
- その他の設定:
  - `fScale`: 0.2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/weapon_cannonfire/fx_weapon_cannonfire_03.nif

### Caravel Cannon Fire Version 1 - Caravel Cannon Fire Version 1

- 内部名: `EFFECT_WEAPON_CARAVEL_CANNON_01`
- その他の設定:
  - `fScale`: 0.2
  - `fUpdateRate`: 2.5
  - `Path`: Art/Effects/weapon_cannonfire/fx_weapon_cannonfire_01.nif

### Caravel Cannon Fire Version 2 - Caravel Cannon Fire Version 2

- 内部名: `EFFECT_WEAPON_CARAVEL_CANNON_02`
- その他の設定:
  - `fScale`: 0.16
  - `fUpdateRate`: 2.5
  - `Path`: Art/Effects/weapon_cannonfire/fx_weapon_cannonfire_02.nif

### Galleon Cannon Fire Version 1 - Galleon Cannon Fire Version 1

- 内部名: `EFFECT_WEAPON_GALLEON_CANNON_01`
- その他の設定:
  - `fScale`: 0.4
  - `fUpdateRate`: 2.5
  - `Path`: Art/Effects/weapon_cannonfire/fx_weapon_cannonfire_01.nif

### Galleon Cannon Fire Version 2 - Galleon Cannon Fire Version 2

- 内部名: `EFFECT_WEAPON_GALLEON_CANNON_02`
- その他の設定:
  - `fScale`: 0.32
  - `fUpdateRate`: 2.5
  - `Path`: Art/Effects/weapon_cannonfire/fx_weapon_cannonfire_02.nif

### Caravel Cannon Fire Version 3 - Caravel Cannon Fire Version 3

- 内部名: `EFFECT_WEAPON_GALLEON_CANNON_03`
- その他の設定:
  - `fScale`: 0.36
  - `fUpdateRate`: 2.5
  - `Path`: Art/Effects/weapon_cannonfire/fx_weapon_cannonfire_03.nif

### Frigate Cannon Fire Version 1 - Frigate Cannon Fire Version 1

- 内部名: `EFFECT_WEAPON_FRIGATE_CANNON_01`
- その他の設定:
  - `fScale`: 0.34
  - `fUpdateRate`: 2.7
  - `Path`: Art/Effects/weapon_cannonfire/fx_weapon_cannonfire_01.nif

### Frigate Cannon Fire Version 2 - Frigate Cannon Fire Version 2

- 内部名: `EFFECT_WEAPON_FRIGATE_CANNON_02`
- その他の設定:
  - `fScale`: 0.27
  - `fUpdateRate`: 2.7
  - `Path`: Art/Effects/weapon_cannonfire/fx_weapon_cannonfire_02.nif

### Frigate Cannon Fire Version 3 - Frigate Cannon Fire Version 3

- 内部名: `EFFECT_WEAPON_FRIGATE_CANNON_03`
- その他の設定:
  - `fScale`: 0.31
  - `fUpdateRate`: 2.7
  - `Path`: Art/Effects/weapon_cannonfire/fx_weapon_cannonfire_03.nif

### Ironclad Cannon Fire Version 1 - Ironclad Cannon Fire Version 1

- 内部名: `EFFECT_WEAPON_IRONCLAD_CANNON_01`
- その他の設定:
  - `fScale`: 0.08
  - `fUpdateRate`: 2.7
  - `Path`: Art/Effects/weapon_cannonfire/fx_weapon_cannonfire_01.nif

### Ironclad Cannon Fire Version 2 - Ironclad Cannon Fire Version 2

- 内部名: `EFFECT_WEAPON_IRONCLAD_CANNON_02`
- その他の設定:
  - `fScale`: 0.07
  - `fUpdateRate`: 2.5
  - `Path`: Art/Effects/weapon_cannonfire/fx_weapon_cannonfire_02.nif

### Ironclad Cannon Fire Version 3 - Ironclad Cannon Fire Version 3

- 内部名: `EFFECT_WEAPON_IRONCLAD_CANNON_03`
- その他の設定:
  - `fScale`: 0.07
  - `fUpdateRate`: 2.6
  - `Path`: Art/Effects/weapon_cannonfire/fx_weapon_cannonfire_03.nif

### Modern cannonfire for Armoured vehicles - Modern cannonfire for Armoured vehicles

- 内部名: `EFFECT_WEAPON_CANNONFIRE_MODERN_TANKS`
- その他の設定:
  - `fScale`: 1.2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/weapon_cannonfire_modern/fx_weapon_cannonfire_modern.nif

### Modern Cannonfire For Naval ships - Modern Cannonfire For Naval ships

- 内部名: `EFFECT_WEAPON_CANNONFIRE_MODERN_SHIPS`
- その他の設定:
  - `fScale`: 0.6
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/weapon_cannonfire_modern/fx_weapon_cannonfire_modern.nif

### Modern Cannonfire For Destroyer Version 1 - Modern Cannonfire For Destroyer Version 1

- 内部名: `EFFECT_WEAPON_DESTROYER01`
- その他の設定:
  - `fScale`: 0.02
  - `fUpdateRate`: 2.2
  - `Path`: Art/Effects/weapon_cannonfire_modern/fx_weapon_cannonfire_modern.nif

### Modern Cannonfire For Destroyer Version 2 - Modern Cannonfire For Destroyer Version 2

- 内部名: `EFFECT_WEAPON_DESTROYER02`
- その他の設定:
  - `fScale`: 0.018
  - `fUpdateRate`: 2.4
  - `Path`: Art/Effects/weapon_cannonfire_modern/fx_weapon_cannonfire_modern.nif

### Modern Cannonfire For Battleship Version 1 - Modern Cannonfire For Battleship Version 1

- 内部名: `EFFECT_WEAPON_BATTLESHIP01`
- その他の設定:
  - `fScale`: 0.022
  - `fUpdateRate`: 2.0
  - `Path`: Art/Effects/weapon_cannonfire_modern/fx_weapon_cannonfire_modern.nif

### Modern Cannonfire For Battleship Version 2 - Modern Cannonfire For Battleship Version 2

- 内部名: `EFFECT_WEAPON_BATTLESHIP02`
- その他の設定:
  - `fScale`: 0.019
  - `fUpdateRate`: 2.2
  - `Path`: Art/Effects/weapon_cannonfire_modern/fx_weapon_cannonfire_modern.nif

### Modern Weapon Fire for Carrier attacks - Modern Weapon Fire for Carrier attacks

- 内部名: `EFFECT_WEAPON_CARRIER_BLAST`
- その他の設定:
  - `fScale`: 0.01
  - `fUpdateRate`: 1.8
  - `Path`: Art/Effects/weapon_cannonfire_modern/fx_weapon_cannonfire_modern.nif

### Torpedo for Submarine - Torpedo for Submarine

- 内部名: `EFFECT_WEAPON_TORPEDO`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/Submarine/SubmarineTorpedo.nif
  - `bIsProjectile`: 1

### Panzer Tank Cannon Fire - Panzer Tank Cannon Fire

- 内部名: `EFFECT_WEAPON_PANZER_FIRE`
- その他の設定:
  - `fScale`: .05
  - `fUpdateRate`: 2.5
  - `Path`: Art/Effects/weapon_cannonfire_modern/fx_weapon_cannonfire_modern.nif

### Cannon Fire - Cannon Fire

- 内部名: `EFFECT_WEAPON_CANNON_FIRE`
- その他の設定:
  - `fScale`: 0.3
  - `fUpdateRate`: 2.8
  - `Path`: Art/Effects/weapon_cannonfire/fx_weapon_cannonfire_01.nif

### Artillery Cannon Fire - Artillery Cannon Fire

- 内部名: `EFFECT_WEAPON_ARTILLERY`
- その他の設定:
  - `fScale`: .04
  - `fUpdateRate`: 2.0
  - `Path`: Art/Effects/weapon_cannonfire_modern/fx_weapon_cannonfire_modern.nif

### MachineGunner Fire - MachineGunner Fire

- 内部名: `EFFECT_WEAPON_MACHINEGUNNERY_FIRE`
- その他の設定:
  - `fScale`: 1.2
  - `fUpdateRate`: 2.0
  - `Path`: Art/Effects/weapon_rifleblast_modern/fx_rifleblast_modern.nif

### Modern Cannonfire for Howitzer type cannons - Modern Cannonfire for Howitzer type cannons

- 内部名: `EFFECT_WEAPON_CANNONFIRE_MODERN_HOWITZER`
- その他の設定:
  - `fScale`: 0.2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/weapon_cannonfire_modern/fx_weapon_cannonfire_modern.nif

### Machanized Infantry Shell Blast - Machanized Infantry Shell Blast

- 内部名: `EFFECT_WEAPON_MECHANIZED_INFANTRY_BLAST`
- その他の設定:
  - `fScale`: 0.6
  - `fUpdateRate`: 1.0
  - `Path`: Art/Units/MachineGun/MachineGun_Fire.nif

### Unit Healing effect - Unit Healing effect

- 内部名: `EFFECT_HEALSPARKLE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_healing/fx_unit_healing.nif

### Lotus Appearing Effect in the Buddhist Animations - Lotus Appearing Effect in the Buddhist Animations

- 内部名: `EFFECT_LOTUS_BLOOM`
- その他の設定:
  - `fScale`: 0.3
  - `fUpdateRate`: 1.5
  - `Path`: Art/Effects/unit_healing/fx_unit_healing.nif

### Promotion for unit - Promotion for unit

- 内部名: `EFFECT_PROMOTION_UNIT`
- その他の設定:
  - `fScale`: 0.6
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_promotion/fx_unit_promotion_01.nif

### Enemy glow for unit - Enemy glow for unit

- 内部名: `EFFECT_ENEMY_GLOW_UNIT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Unit_Enemy_Presence/fx_Unit_Enemy_Presence.nif

### Promotion for Interface - Promotion for Interface

- 内部名: `EFFECT_PROMOTION_INTERFACE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_promotion/fx_unit_promotion_02.nif

### Creation Effect Dim - Creation Effect Dim

- 内部名: `EFFECT_CREATION`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/creation/fx_creation_dim.nif

### Creation Effect Bright - Creation Effect Bright

- 内部名: `EFFECT_CREATION_BIG`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/creation/fx_creation_bright.nif

### Creation Effect Bright Fast - Creation Effect Bright Fast

- 内部名: `EFFECT_CREATION_BIG_FAST`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 6.6
  - `Path`: Art/Effects/creation/fx_creation_bright.nif

### Activation effect for Buddhist missionary - Activation effect for Buddhist missionary

- 内部名: `EFFECT_MISSIONARY_ACTIVE_BUDDHISM`
- その他の設定:
  - `fScale`: 1.3
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_missionary_activation/fx_missionary_activate_buddhism.nif

### Activation effect for Confuscian missionary - Activation effect for Confuscian missionary

- 内部名: `EFFECT_MISSIONARY_ACTIVE_CONFUSCIAN`
- その他の設定:
  - `fScale`: 1.2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_missionary_activation/fx_missionary_activate_confuscian.nif

### Activation effect for Christian missionary - Activation effect for Christian missionary

- 内部名: `EFFECT_MISSIONARY_ACTIVE_CHRISTIANITY`
- その他の設定:
  - `fScale`: 1.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_missionary_activation/fx_missionary_activate_christianity.nif

### Activation effect for Hindu missionary - Activation effect for Hindu missionary

- 内部名: `EFFECT_MISSIONARY_ACTIVE_HINDUISM`
- その他の設定:
  - `fScale`: 1.2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_missionary_activation/fx_missionary_activate_hinduism.nif

### Activation effect for Islamic missionary - Activation effect for Islamic missionary

- 内部名: `EFFECT_MISSIONARY_ACTIVE_ISLAM`
- その他の設定:
  - `fScale`: 1.2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_missionary_activation/fx_missionary_activate_islam.nif

### Activation effect for Jewish missionary - Activation effect for Jewish missionary

- 内部名: `EFFECT_MISSIONARY_ACTIVE_JEWISH`
- その他の設定:
  - `fScale`: 1.2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_missionary_activation/fx_missionary_activate_jewish.nif

### Activation effect for Tao missionary - Activation effect for Tao missionary

- 内部名: `EFFECT_MISSIONARY_ACTIVE_TAOISM`
- その他の設定:
  - `fScale`: 1.2
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_missionary_activation/fx_missionary_activate_taoism.nif

### Activation effect for the King Baby! - Activation effect for the King Baby!

- 内部名: `EFFECT_GREATPEOPLE_ACTIVE_ARTIST`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Artist_Activate.nif

### The King is Born Baby! - The King is Born Baby!

- 内部名: `EFFECT_GREATPEOPLE_BIRTH_ARTIST`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 2.5
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Artist_Birth.nif

### Highlight effect for the King. That's right little mama! - Highlight effect for the King. That's right little mama!

- 内部名: `EFFECT_GREATPEOPLE_HIGHLIGHT_ARTIST`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Artist_Highlight.nif

### Activation effect for Engineer - Activation effect for Engineer

- 内部名: `EFFECT_GREATPEOPLE_ACTIVE_ENGINEER`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Engineer_Activation.nif

### Birth effect for the engineer - Birth effect for the engineer

- 内部名: `EFFECT_GREATPEOPLE_BIRTH_ENGINEER`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 2.5
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Engineer_Birth.nif

### Highlight effect for the Engineer - Highlight effect for the Engineer

- 内部名: `EFFECT_GREATPEOPLE_HIGHLIGHT_ENGINEER`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Engineer_Highlight.nif

### Gear effect for the Engineer - Gear effect for the Engineer

- 内部名: `EFFECT_ENGINEER_GEARS`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_ModernEngineer_Gears.nif

### Activation effect for Prophet - Activation effect for Prophet

- 内部名: `EFFECT_GREATPEOPLE_ACTIVE_PROPHET`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Prophet_Activation.nif

### Birth effect for the Prophet - Birth effect for the Prophet

- 内部名: `EFFECT_GREATPEOPLE_BIRTH_PROPHET`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 2.5
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Prophet_Birth.nif

### Highlight effect for the Prophet - Highlight effect for the Prophet

- 内部名: `EFFECT_GREATPEOPLE_HIGHLIGHT_PROPHET`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Prophet_Highlight.nif

### Activation effect for Scientist - Activation effect for Scientist

- 内部名: `EFFECT_GREATPEOPLE_ACTIVE_SCIENTIST`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Scientist_Activation.nif

### Birth effect for the Scientist - Birth effect for the Scientist

- 内部名: `EFFECT_GREATPEOPLE_BIRTH_SCIENTIST`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 2.5
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Scientist_Birth.nif

### Highlight effect for the Scientist - Highlight effect for the Scientist

- 内部名: `EFFECT_GREATPEOPLE_HIGHLIGHT_SCIENTIST`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Scientist_Highlight.nif

### Activation effect for Merchant - Activation effect for Merchant

- 内部名: `EFFECT_GREATPEOPLE_ACTIVE_MERCHANT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Tycoon_Activation.nif

### Birth effect for Merchant - Birth effect for Merchant

- 内部名: `EFFECT_GREATPEOPLE_BIRTH_MERCHANT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 2.5
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Tycoon_Birth.nif

### Highlight effect for the Merchant - Highlight effect for the Merchant

- 内部名: `EFFECT_GREATPEOPLE_HIGHLIGHT_MERCHANT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Tycoon_Highlight.nif

### Activation effect for the warlord general - Activation effect for the warlord general

- 内部名: `EFFECT_GREATPEOPLE_ACTIVE_WARLORD`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 2.5
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Warlord_Activate.nif

### Birth of the Warlord - Birth of the Warlord

- 内部名: `EFFECT_GREATPEOPLE_BIRTH_WARLORD`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 2.5
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Warlord_Birth.nif

### Highlight effect for the Warlord - Highlight effect for the Warlord

- 内部名: `EFFECT_GREATPEOPLE_HIGHLIGHT_WARLORD`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/unit_greatpeople/fx_GreatPeople_Warlord_Highlight.nif

### water submerged explosion for submarine death - water submerged explosion for submarine death

- 内部名: `EFFECT_WATER_SUBMARINE_DEATH`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/water_submerged_explosion/fx_water_submerged_explosion.nif

### Ship_Bow_Froth - Ship_Bow_Froth

- 内部名: `EFFECT_SHIP_BOW_FROTH`
- その他の設定:
  - `fScale`: 0.15
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/water_ship_bow_froth/fx_water_ship_bow_froth.nif

### Ship_Side_Froth - Ship_Side_Froth

- 内部名: `EFFECT_SHIP_SIDE_FROTH`
- その他の設定:
  - `fScale`: 0.15
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/water_ship_side_froth/fx_water_ship_side_froth.nif

### Ship_Sinking_Froth - Ship_Sinking_Froth

- 内部名: `EFFECT_SHIP_SINKING_FROTH`
- その他の設定:
  - `fScale`: 0.1
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/water_ship_sinking_froth/fx_water_ship_sinking_froth.nif

### Galley_Sinking_Froth - Galley_Sinking_Froth

- 内部名: `EFFECT_GALLEY_SINKING_FROTH`
- その他の設定:
  - `fScale`: 0.25
  - `fUpdateRate`: 2.0
  - `Path`: Art/Effects/water_ship_sinking_froth/fx_water_ship_sinking_froth.nif

### Water Plume Splash Small - Water Plume Splash Small

- 内部名: `EFFECT_GALLEY_SPLASH_PLUME_LRG`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 2.0
  - `Path`: Art/Effects/water_splash_plume/fx_water_plume01.nif

### Caravel Sinking_Froth - Caravel Sinking_Froth

- 内部名: `EFFECT_CARAVEL_SINKING_FROTH`
- その他の設定:
  - `fScale`: 0.20
  - `fUpdateRate`: 2.2
  - `Path`: Art/Effects/water_ship_sinking_froth/fx_water_ship_sinking_froth.nif

### Galleon Sinking_Froth - Galleon Sinking_Froth

- 内部名: `EFFECT_GALLEON_SINKING_FROTH`
- その他の設定:
  - `fScale`: 0.40
  - `fUpdateRate`: 2.0
  - `Path`: Art/Effects/water_ship_sinking_froth/fx_water_ship_sinking_froth.nif

### Ironclad Sinking_Froth - Ironclad Sinking_Froth

- 内部名: `EFFECT_IRONCLAD_SINKING_FROTH`
- その他の設定:
  - `fScale`: 0.1
  - `fUpdateRate`: 2.0
  - `Path`: Art/Effects/water_ship_sinking_froth/fx_water_ship_sinking_froth.nif

### Transport_Sinking_Froth - Transport_Sinking_Froth

- 内部名: `EFFECT_TRANSPORT_SINKING_FROTH`
- その他の設定:
  - `fScale`: 0.06
  - `fUpdateRate`: 2.0
  - `Path`: Art/Effects/water_ship_sinking_froth/fx_water_ship_sinking_froth.nif

### Frigate Sinking_Froth - Frigate Sinking_Froth

- 内部名: `EFFECT_FRIGATE_SINKING_FROTH`
- その他の設定:
  - `fScale`: 0.35
  - `fUpdateRate`: 2.0
  - `Path`: Art/Effects/water_ship_sinking_froth/fx_water_ship_sinking_froth.nif

### Ironclad Sinking_Froth - Ironclad Sinking_Froth

- 内部名: `EFFECT_DESTROYER_SINKING_FROTH`
- その他の設定:
  - `fScale`: 0.06
  - `fUpdateRate`: 1.8
  - `Path`: Art/Effects/water_ship_sinking_froth/fx_water_ship_sinking_froth.nif

### Battleship Sinking_Froth - Battleship Sinking_Froth

- 内部名: `EFFECT_BATTLESHIP_SINKING_FROTH`
- その他の設定:
  - `fScale`: 0.07
  - `fUpdateRate`: 1.6
  - `Path`: Art/Effects/water_ship_sinking_froth/fx_water_ship_sinking_froth.nif

### Carrier Sinking_Froth - Carrier Sinking_Froth

- 内部名: `EFFECT_CARRIER_SINKING_FROTH`
- その他の設定:
  - `fScale`: 0.08
  - `fUpdateRate`: 1.5
  - `Path`: Art/Effects/water_ship_sinking_froth/fx_water_ship_sinking_froth.nif

### WorkBoat_Sinking_Froth - WorkBoat_Sinking_Froth

- 内部名: `EFFECT_WORKBOAT_SINKING_FROTH`
- その他の設定:
  - `fScale`: 0.15
  - `fUpdateRate`: 2.0
  - `Path`: Art/Effects/water_ship_sinking_froth/fx_water_ship_sinking_froth.nif

### Workboat Water Plume Splash - Workboat Water Plume Splash

- 内部名: `EFFECT_WORKBOAT_SPLASH_PLUME`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 2.0
  - `Path`: Art/Effects/water_splash_plume/fx_water_plume01.nif

### Water Plume Splash Small - Water Plume Splash Small

- 内部名: `EFFECT_SPLASH_PLUME_SML`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/water_splash_plume/fx_water_plume01.nif

### Water plume splash Large - Water plume splash Large

- 内部名: `EFFECT_SPLASH_PLUME_LRG`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/water_splash_plume/fx_water_plume01.nif

### water bubbles for submarine etc - water bubbles for submarine etc

- 内部名: `EFFECT_PROPELLER_BUBBLES`
- その他の設定:
  - `fScale`: 0.8
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/water_propeller_bubbles/fx_water_propeller_bubbles.nif

### One fog emiter to create a bank of them with - One fog emiter to create a bank of them with

- 内部名: `EFFECT_FOG_EMITER`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/fog_01/fx_fog_01.nif

### Birds flying out and fading. - Birds flying out and fading.

- 内部名: `EFFECT_BIRDSCATTER`
- その他の設定:
  - `fScale`: 0.4
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Magpie/Flock.nif

### RED firework large slow - RED firework large slow

- 内部名: `FIREWORKS_RED_LARGE_SLOW`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.5
  - `Path`: Art/Effects/fireworks/fx_fireworks_red.nif

### RED firework large slow - RED firework large slow

- 内部名: `FIREWORKS_RED_SMALL_FAST`
- その他の設定:
  - `fScale`: 0.3
  - `fUpdateRate`: 4.0
  - `Path`: Art/Effects/fireworks/fx_fireworks_red.nif

### GREEN firework large slow - GREEN firework large slow

- 内部名: `FIREWORKS_GREEN_LARGE_SLOW`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.5
  - `Path`: Art/Effects/fireworks/fx_fireworks_green.nif

### GREEN firework large slow - GREEN firework large slow

- 内部名: `FIREWORKS_GREEN_SMALL_FAST`
- その他の設定:
  - `fScale`: 0.3
  - `fUpdateRate`: 4.0
  - `Path`: Art/Effects/fireworks/fx_fireworks_green.nif

### PURPLE firework large slow - PURPLE firework large slow

- 内部名: `FIREWORKS_PURPLE_LARGE_SLOW`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.5
  - `Path`: Art/Effects/fireworks/fx_fireworks_purple.nif

### PURPLE firework large slow - PURPLE firework large slow

- 内部名: `FIREWORKS_PURPLE_SMALL_FAST`
- その他の設定:
  - `fScale`: 0.3
  - `fUpdateRate`: 4.0
  - `Path`: Art/Effects/fireworks/fx_fireworks_purple.nif

### YELLOW firework large slow - YELLOW firework large slow

- 内部名: `FIREWORKS_YELLOW_LARGE_SLOW`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.5
  - `Path`: Art/Effects/fireworks/fx_fireworks_yellow.nif

### YELLOW firework large slow - YELLOW firework large slow

- 内部名: `FIREWORKS_YELLOW_SMALL_FAST`
- その他の設定:
  - `fScale`: 0.3
  - `fUpdateRate`: 4.0
  - `Path`: Art/Effects/fireworks/fx_fireworks_yellow.nif

### BLUE firework large slow - BLUE firework large slow

- 内部名: `FIREWORKS_BLUE_LARGE_SLOW`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.5
  - `Path`: Art/Effects/fireworks/fx_fireworks_blue.nif

### BLUE firework large slow - BLUE firework large slow

- 内部名: `FIREWORKS_BLUE_SMALL_FAST`
- その他の設定:
  - `fScale`: 0.3
  - `fUpdateRate`: 4.0
  - `Path`: Art/Effects/fireworks/fx_fireworks_blue.nif

### Goody hut pop dust and hay - Goody hut pop dust and hay

- 内部名: `EFFECT_IMPROVEMENT_GOODYHUT_POP`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/improvement_goody_hut_pop/fx_goodyhut_pop.nif

### improvements campfire - improvements campfire

- 内部名: `EFFECT_IMPROVEMENT_CAMPFIRE`
- その他の設定:
  - `fScale`: 100.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/improvement_campfire/fx_fire_campfire.nif

### Fire blowing out of top of Mine smelter - Fire blowing out of top of Mine smelter

- 内部名: `EFFECT_IMPROVEMENT_FIRE_FOOMP`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/improvement_fire_foomp/fx_improvement_fire_foomp.nif

### STEAM - STEAM

- 内部名: `EFFECT_IMPROVEMENT_STEAM`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/improvement_steam/fx_improvement_steam.nif

### Chimney smoke for improvements - Chimney smoke for improvements

- 内部名: `EFFECT_IMPROVEMENT_CHIMNEY_SMOKE_03`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/smoke_chimney_02/fx_chimneysmoke_03.nif

### Fire for improvement fire place - Fire for improvement fire place

- 内部名: `EFFECT_IMPROVEMENT_FIREPLACE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/fire_torch/fx_fire_torch.nif

### Torchfire made for the colossus - Torchfire made for the colossus

- 内部名: `EFFECT_FIRE_TORCH`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/fire_torch/fx_fire_torch.nif

### fake event so that spyxml doesnt freak out - fake event so that spyxml doesnt freak out

- 内部名: `EFFECT_FAKE_EVENT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/fire_torch/fx_fire_torch.nif

### Fire for AGE OF GODS Ianna shrine - Fire for AGE OF GODS Ianna shrine

- 内部名: `EFFECT_SHRINE_FLAMES`
- その他の設定:
  - `fScale`: 3.5
  - `fUpdateRate`: 0.8
  - `Path`: Art/Effects/fire_torch/fx_fire_torch.nif

### Chimney smoke for cities (variation) - Chimney smoke for cities (variation)

- 内部名: `EFFECT_CHIMNEY_SMOKE_01`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/smoke_chimney_02/fx_chimneysmoke_01.nif

### Chimney smoke for cities (variation) - Chimney smoke for cities (variation)

- 内部名: `EFFECT_CHIMNEY_SMOKE_02`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/smoke_chimney_02/fx_chimneysmoke_02.nif

### Chimney smoke for cities (variation) - Chimney smoke for cities (variation)

- 内部名: `EFFECT_CHIMNEY_SMOKE_03`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/smoke_chimney_02/fx_chimneysmoke_03.nif

### Smoke for destroyed cities (variation) - Smoke for destroyed cities (variation)

- 内部名: `EFFECT_CITY_SMOKING_01`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/cities_smoking/fx_cities_smoking_01.nif

### Smoke for destroyed cities (variation) - Smoke for destroyed cities (variation)

- 内部名: `EFFECT_CITY_SMOKING_02`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/cities_smoking/fx_cities_smoking_02.nif

### underlit smoke for unhappy cities (variation) - underlit smoke for unhappy cities (variation)

- 内部名: `EFFECT_CITY_BURNING_SMOKE`
- その他の設定:
  - `fScale`: 0.1
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/cities_unhappy_burning/fx_unhappy_burning.nif

### underlit smoke for occupied cities - underlit smoke for occupied cities

- 内部名: `EFFECT_CITY_BIG_BURNING_SMOKE`
- その他の設定:
  - `fScale`: 0.4
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/cities_occupied_burning/fx_occupied_burning.nif

### Fire for zoomed out unhappy citees - Fire for zoomed out unhappy citees

- 内部名: `EFFECT_CITY_FIRE`
- その他の設定:
  - `fScale`: 3.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/fire_torch/fx_fire_torch.nif

### Fumes for diseased citees - Fumes for diseased citees

- 内部名: `EFFECT_CITY_DISEASED`
- その他の設定:
  - `fScale`: 4.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/cities_sickly_fumes/fx_cities_sickly_fumes.nif

### Pulsing glow for irradiated citees - Pulsing glow for irradiated citees

- 内部名: `EFFECT_CITY_IRRADIATED`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/cities_irradiated/fx_cities_irradiated.nif

### Air to Ground Machine Gun - Air to Ground Machine Gun

- 内部名: `EFFECT_MACHINEGUNFIRE_GROUND`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/PrototypeEffects/MachineGunFire/MachineGunFire_Ground.kfm
  - `bIsProjectile`: 1

### Air to Air Machine Gun - Air to Air Machine Gun

- 内部名: `EFFECT_MACHINEGUNFIRE_AIR___UNNEEDED`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/PrototypeEffects/MachineGunFire/MachineGunFire_Air.nif
  - `bIsProjectile`: 1

### Stealh Bomber Bomb - Stealh Bomber Bomb

- 内部名: `EFFECT_STEALTHBOMB`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/PrototypeEffects/StealthBombs/Bombs/StealthBombs.kfm
  - `bIsProjectile`: 1

### Galley Arrows - Galley Arrows

- 内部名: `EFFECT_GALLEY_ARROWS`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/PrototypeEffects/Galley/GalleyArrows.nif

### Small explosion for Invasion Ship - Small explosion for Invasion Ship

- 内部名: `EFFECT_MISSILE_LARGE_HIT`
- その他の設定:
  - `fScale`: 3.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/FF_explosion_large/FF_explosion_large.nif

### Large explosion for Invasion Ship - Large explosion for Invasion Ship

- 内部名: `EFFECT_INVASIONSHIP_SMALL_HIT`
- その他の設定:
  - `fScale`: 0.3
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/FF_explosion_large/FF_explosion_large.nif

### Small explosion for Invasion Ship - Small explosion for Invasion Ship

- 内部名: `EFFECT_INVASIONSHIP_LARGE_HIT`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/FF_explosion_large/FF_explosion_large.nif

### Powerup laser effect - Powerup laser effect

- 内部名: `EFFECT_INVASIONSHIP_LASER`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/FF_powerUp_laser/FF_powerUp_laser.nif

### Powerup laser effect - Powerup laser effect

- 内部名: `EFFECT_INVASIONSHIP_FLAK`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/FF_Flak_Fire/fx_weapon_flak.nif

### Powerup laser effect - Powerup laser effect

- 内部名: `EFFECT_INVASIONSHIP_LASERBEAM`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/FF_Laserbeam/fx_laserbeam.nif

### Powerup laser effect - Powerup laser effect

- 内部名: `EFFECT_INVASIONSHIP_TORPEDO`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/FF_Torpedo/fx_torpedo.nif

### Standard laser effect - Standard laser effect

- 内部名: `EFFECT_INVASIONSHIP_LASERFIRE`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/FF_Laser_Fire/fx_laser_fire.nif

### Smaller laser effect - Smaller laser effect

- 内部名: `EFFECT_INVASIONSHIP_LASERFIRESMALL`
- その他の設定:
  - `fScale`: 0.6
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/FF_Laser_Fire/fx_laser_fire_small.nif

### Standard laser effect - Standard laser effect

- 内部名: `EFFECT_INVASIONSHIP_LASERFIRE_BIG`
- その他の設定:
  - `fScale`: 2.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/FF_Laser_Fire/fx_laser_fire.nif

### Red pulse cannon - Red pulse cannon

- 内部名: `EFFECT_RED_EYELASER`
- その他の設定:
  - `fScale`: 0.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Red_Laser/fx_redlaser.nif

### Space radio signals - Space radio signals

- 内部名: `EFFECT_FRONTIER_SIGNAL`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/FF_Signal/ff_signal.nif

### Colony settling effect - Colony settling effect

- 内部名: `EFFECT_FF_TRANSPORT`
- その他の設定:
  - `fScale`: 0.3
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/FF_Transporter/fx_transporter.nif

### Drake Frost Breath - Drake Frost Breath

- 内部名: `EFFECT_DRAKE_FROST_BREATH`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art_Kaijin/Effects/Drake/frostburst.nif

### Drake Poison Breath - Drake Poison Breath

- 内部名: `EFFECT_DRAKE_POISON_BREATH`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art_Kaijin/Effects/Drake/poisonburst.nif

### Drake Firebreath - Drake Firebreath

- 内部名: `EFFECT_DRAKE_FIREBURST`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art_Kaijin/Effects/Drake/fireburst.nif

### Drake Lightning Breath - Drake Lightning Breath

- 内部名: `EFFECT_LIGHTNING_BURST`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art_Kaijin/Effects/Drake/lightningburst.nif

### Balmy Breeze - Balmy Breeze

- 内部名: `EFFECT_BALMY_BREEZE`
- その他の設定:
  - `fScale`: 4.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/blastripple_sound.nif

### Spores Effect - Spores Effect

- 内部名: `EFFECT_DEATH_CLOUD`
- その他の設定:
  - `fScale`: 6.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/alb_acidmist_hit.nif

### Fire Storm - Fire Storm

- 内部名: `EFFECT_FIRE_STORM`
- その他の設定:
  - `fScale`: 6.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/alb_firesplash_hit.nif

### Poison Cloud - Poison Cloud

- 内部名: `EFFECT_POISON_CLOUD`
- その他の設定:
  - `fScale`: 6.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/blastripple_sound.nif

### Tiltowaito - Tiltowaito

- 内部名: `EFFECT_TILTOWAITO`
- その他の設定:
  - `fScale`: 9.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/zapsphere_hit.nif

### Creation Effect Dim - Creation Effect Dim

- 内部名: `EFFECT_MIRACLE`
- その他の設定:
  - `fScale`: 2.5
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/creation/fx_creation_dim.nif

### Blade of thunder Effect - Blade of thunder Effect

- 内部名: `EFFECT_BLADE_OF_THUNDER`
- その他の設定:
  - `fScale`: 2.5
  - `fUpdateRate`: 1.0
  - `Path`: Art_Kaijin/Effects/drake/lightningburst.nif

### Spores Effect - Spores Effect

- 内部名: `EFFECT_DEATH_AND_DECAY`
- その他の設定:
  - `fScale`: 12.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/alb_acidmist_hit.nif

### Awakening - Awakening

- 内部名: `EFFECT_AWAKENING`
- その他の設定:
  - `fScale`: 18.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/zapsphere_hit.nif

### Annihilation - Annihilation

- 内部名: `EFFECT_ANNIHILATION`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/explosion_nuke/fx_explosion_nuke.nif

### Magic Arrow - Magic Arrow

- 内部名: `EFFECT_MAGIC_ARROW`
- その他の設定:
  - `fScale`: 1.0
  - `fUpdateRate`: 1.0
  - `Path`: Art_Kaijin/Units/Momiji_Werdandi/Magic_Arrow_Effect/magic_arrow.nif
  - `bIsProjectile`: 1
  - `fSpeed`: 400.0

### Worm Dust - Worm Dust

- 内部名: `EFFECT_WORM_DUST1`
- その他の設定:
  - `fScale`: 0.8
  - `fUpdateRate`: 0.3
  - `Path`: Art_Kaijin/Effects/Xoth_SandFX/SettlerSmoke.nif

### Worm Dust - Worm Dust

- 内部名: `EFFECT_WORM_DUST2`
- その他の設定:
  - `fScale`: 0.75
  - `fUpdateRate`: 0.9
  - `Path`: Art_Kaijin/Effects/Xoth_SandFX/SettlerSmoke.nif

### Holy Grenade Explode - Holy Grenade Explode

- 内部名: `EFFECT_HOLY_GRENADE_EXPLODE`
- その他の設定:
  - `fScale`: 6.0
  - `fUpdateRate`: 1.0
  - `Path`: Art/Effects/Spell Effects/hib_vexplo5_hit.nif
