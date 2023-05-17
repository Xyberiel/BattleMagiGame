# Battle magi is a turn based text game with a complex battle system and modular magic system.

import random
import time

# parent class for all characters
class Character():

    # Constructor for the character class that takes an optional name parameter
    # Check if name is provided, if not, set name to "unnamed"
    # Initialize base stats and derived stats
    # Initialize base HP, MP, and SP
    def __init__(self, name = ""):
        if name != "":
            self.name = name
        else:
            self.name = "unnamed"

        self.base_stats = {
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

        self.derived_stats = {
            'HP': { 'value' : 100, 'description' : "Health Points"},
            'MP': { 'value' : 100, 'description' : "Mana Points"},
            'SP': { 'value' : 100, 'description' : "Stamina Points"},
            'DEF': { 'value' : 1, 'description' : "Physical Defense"},
            'MAG_DEF': { 'value' : 1, 'description' : "Magic Defense"},
            'PHY_ACC': { 'value' : 1, 'description' : "Physical Accuracy"},
            'MAG_ACC': { 'value' : 1, 'description' : "Magic Accuracy"},
            'PHY_EVA': { 'value' : 1, 'description' : "Physical Evasion"},
            'MAG_EVA': { 'value' : 1, 'description' : "Magic Evasion"},
            'PHY_CRIT': { 'value' : 1, 'description' : "Physical Critical Hit Chance"},
            'MAG_CRIT': { 'value' : 1, 'description' : "Magic Critical Hit Chance"},
            'PHY_CRIT_DMG': { 'value' : 1, 'description' : "Physical Critical Hit Damage"},
            'MAG_CRIT_DMG': { 'value' : 1, 'description' : "Magic Critical Hit Damage"},
            'BLK': { 'value' : 1, 'description' : "Block Chance"},
            'MAG_BLK': { 'value' : 1, 'description' : "Magic Block Chance"},
            'PARRY': { 'value' : 1, 'description' : "Parry Chance"},
            'MAG_PARRY': { 'value' : 1, 'description' : "Magic Parry Chance"},
            'DODGE': { 'value' : 1, 'description' : "Dodge Chance"},
            'MAG_DODGE': { 'value' : 1, 'description' : "Magic Dodge Chance"},
            'TURN_PRIORITY': { 'value' : 1, 'description' : "Turn Priority"},
            'BONUS_REWARDS': { 'value' : 1, 'description' : "Bonus Rewards"}
            }

        # Initialize base HP, MP, and SP
        self.base_hp = self.base_stats['END']['value'] * 10
        self.base_mp = self.base_stats['WIS']['value'] * 10
        self.base_sp = self.base_stats['CON']['value'] * 10


    # getter for base stats and derived stats
    def get_stat(self, stat):
        if stat in self.base_stats:
            return self.base_stats[stat]['value']
        elif stat in self.derived_stats:
            return self.derived_stats[stat]['value']
        else:
            raise ValueError(f"Stat {stat} not found")
    # A sample call for the getter would be: player.get_stat('STR')
    # A sample bad call for the getter would be: player.get_stat('str') and would return the error message "Stat str not found"

    # setter for base stats and derived stats
    def set_stat(self, stat, value):
        # Check if the value being set is a non-negative integer
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"Value {value} is not a non-negative integer")
        # Check if stat is in base stats or derived stats
        if stat in self.base_stats:
            self.base_stats[stat]['value'] = value
        elif stat in self.derived_stats:
            self.derived_stats[stat]['value'] = value
        else:
            raise ValueError(f"Stat {stat} not found")
    # a sample call for the setter would be: player.set_stat('STR', 10)
    # a sample bad call for the setter would be: player.set_stat('str', 10) and would return the error message "Stat str not found"
    # a sample bad call for the setter would be: player.set_stat('STR', -10) and would return the error message "Value -10 is not a non-negative integer"


# subclass for the player character
class Player(Character):

    def __init__(self, name=""):
        super().__init__(name)
        # TODO: Initialize player-specific attributes here


# subclass for enemies and bosses
class Enemy(Character):

    def __init__(self, name=""):
        super().__init__(name)
        self.mob_type = ""
        # TODO: Initialize enemy-specific attributes here


# subclass for summoned creatures and familiars
class Summon(Character):

    def __init__(self, name=""):
        super().__init__(name)
        self.summon_type = ""
        # TODO: Initialize summon-specific attributes here