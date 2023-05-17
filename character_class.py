# Battle magi is a turn based text game with a complex battle system and modular magic system.

import random
import time

# parent class for all characters
class Character():
    name = ""
    base_hp = 100 # Base value for other Health points calculations
    max_hp = 100  # TODO create a function to calculate max_hp
    current_hp = 100 # TODO create a function to calculate current_hp
    base_mp = 100 # Base value for other Mana points calculations
    max_mp = 100 # TODO create a function to calculate max_mp
    current_mp = 100 # TODO create a function to calculate current_mp
    base_sp = 100 # Base value for other Stamina points calculations
    max_sp = 100 # TODO create a function to calculate max_sp
    current_sp = 100 # TODO create a function to calculate current_sp

    # Dictionary for base stats with their values and descriptions
    base_stats = {
        'STR' : { 'value' : 1, 'description' : "Physical Power"},
        'DEX' : { 'value' : 1, 'description' : "Physical Accuracy"},
        'END' : { 'value' : 1, 'description' : "Physical Efficiency"},
        'INT' : { 'value' : 1, 'description' : "Magic Power"},
        'FOC' : { 'value' : 1, 'description' : "Magic Accuracy"},
        'WIS' : { 'value' : 1, 'description' : "Magic Efficiency"},
        'CON' : { 'value' : 1, 'description' : "Physical Defense"},
        'SPI' : { 'value' : 1, 'description' : "Magic Defense"},
        'AGI' : { 'value' : 1, 'description' : "Physical Evasion"},
        'CUN' : { 'value' : 1, 'description' : "Magic Evasion"},
        'LUC' : { 'value' : 1, 'description' : "Random Chance of Good Things Happening"}
        }

    # Dictionary for derived stats with their values and descriptions
    derived_stats = {
        'HP' : { 'value' : 100, 'description' : "Health Points"},
        'MP' : { 'value' : 100, 'description' : "Mana Points"},
        'SP' : { 'value' : 100, 'description' : "Stamina Points"},
        'DEF' : { 'value' : 1, 'description' : "Physical Defense"},
        'MAG_DEF' : { 'value' : 1, 'description' : "Magic Defense"},
        'PHY_ACC' : { 'value' : 1, 'description' : "Physical Accuracy"},
        'MAG_ACC' : { 'value' : 1, 'description' : "Magic Accuracy"},
        'PHY_EVA' : { 'value' : 1, 'description' : "Physical Evasion"},
        'MAG_EVA' : { 'value' : 1, 'description' : "Magic Evasion"},
        'PHY_CRIT' : { 'value' : 1, 'description' : "Physical Critical Hit Chance"},
        'MAG_CRIT' : { 'value' : 1, 'description' : "Magic Critical Hit Chance"},
        'PHY_CRIT_DMG' : { 'value' : 1, 'description' : "Physical Critical Hit Damage"},
        'MAG_CRIT_DMG' : { 'value' : 1, 'description' : "Magic Critical Hit Damage"},
        'BLK' : { 'value' : 1, 'description' : "Block Chance"},
        'MAG_BLK' : { 'value' : 1, 'description' : "Magic Block Chance"},
        'PARRY' : { 'value' : 1, 'description' : "Parry Chance"},
        'MAG_PARRY' : { 'value' : 1, 'description' : "Magic Parry Chance"},
        'DODGE' : { 'value' : 1, 'description' : "Dodge Chance"},
        'MAG_DODGE' : { 'value' : 1, 'description' : "Magic Dodge Chance"},
        'TURN_PRIORITY' : { 'value' : 1, 'description' : "Turn Priority"},
        'BONUS_REWARDS' : { 'value' : 1, 'description' : "Bonus Rewards"}        
        }

    
    # TODO create a getter that checks if base stats or derived stats are being requested and returns the value
    def get_stat(self, stat):
        if stat in self.base_stats:
            return self.base_stats[stat]['value']
        elif stat in self.derived_stats:
            return self.derived_stats[stat]['value']
        else:
            return "Stat not found"
    # A sample call for the getter would be: player.get_stat('STR')

    # TODO create a setter that checks if base stats or derived stats are being set and sets the value
    def set_stat(self, stat, value):
        if stat in self.base_stats:
            self.base_stats[stat]['value'] = value
        elif stat in self.derived_stats:
            self.derived_stats[stat]['value'] = value
        else:
            return "Stat not found"
    # a sample call for the setter would be: player.set_stat('STR', 10)


# subclass for the player character
class Player(Character):
    # TODO create a container for the player's inventory
    # TODO create a container for the player's equipment
    # TODO create a container for the player's spells
    # TODO create a container for the player's skills
    pass


# subclass for enemies and bosses
class Enemy(Character):
    # TODO create a list of random names for enemies
    # TODO create a list of random mob types for enemies
    # TODO create a list of random mob descriptions for enemies
    mob_type = ""
    pass
    

# subclass for summoned creatures and familiars
class Summon(Character):
    # TODO create a list of random names for summons
    # TODO create a list of random summon types for summons
    # TODO create a list of random summon descriptions for summons
    summon_type = ""
    pass