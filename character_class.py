# Battle magi is a turn based text game with a complex battle system and modular magic system.

import random
import time

# parent class for all characters
class Character():
    name = ""
    health_points = 100 # Health points
    mana_points = 100
    stamina_points = 100

    # Attributes
    strength = 1 # Physical power
    dexterity = 1 # Physical accuracy
    endurance = 1 # Physical efficiency
    intelligence = 1 # Magic power
    focus = 1 # Magic accuracy
    wisdom = 1 # Magic efficiency
    constitution = 1 # Physical defense
    spirit = 1 # Magic defense
    agility = 1 # Physical evasion
    cunning = 1 # Magic evasion
    luck = 1 # Random chance of good things happening

    # Derived Attributes
    max_health = health_points + (2 * constitution) # Maximum health points
    health_regen = (health_points / 100) + constitution # Health points regenerated per turn
    max_mana = mana_points + (2 * wisdom) # Maximum mana points
    mana_regen = (mana_points / 100) + wisdom # Mana points regenerated per turn
    max_stamina = 100 + (2 * endurance) # Maximum stamina points
    stamina_regen = (stamina_points / 100) + endurance # Stamina points regenerated per turn
    phys_crit_chance = 1 * dexterity # Physical critical hit chance
    phys_crit_damage = 1 * strength # Physical critical hit damage
    mag_crit_chance = 1 * focus # Magic critical hit chance
    mag_crit_damage = 1 * intelligence # Magic critical hit damage
    block_chance = 1 * constitution # Block chance is a chance to reduce damage by 50% if player has a shield equipped
    mag_block_chance = 1 * spirit # Magic block chance is a chance to reduce damage by 50% if player has a magic shield equipped
    parry_chance = 1 * dexterity # Parry chance is a chance to reduce damage by 100% if player has two weapons equipped
    magic_parry_chance = 1 * cunning # Magic parry chance is a chance to reduce damage by 100% if player has two magic weapons equipped
    dodge_chance = 1 * agility # Dodge chance is a chance to avoid damage entirely if player has no shield equipped
    magic_dodge_chance = 1 * cunning # Magic dodge chance is a chance to avoid damage entirely if player has no magic shield equipped
    turn_priority = 1 * agility # Turn priority determines who goes first in battle each turn
    bonus_rewards = 1 * luck # Bonus rewards are extra gold or experience gained after battle

class Player(Character):
    pass

class Enemy(Character):
    mob_type = ""