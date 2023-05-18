# This module will handle all functions related to generating names for allies, summons, and enemies.

import random

# A list of all the races
races = ["human", "elf", "dwarf", "orc", "goblin", "troll", "dragon", "demon", "angel", "undead", "beast", "elemental", "unknown"]

# A function that will look at a characters race and run a name generator based on that race.
def generate_name(character):
    if character.race == "human":
        human_name_generator(character)
    elif character.race == "elf":
        elf_name_generator(character)
    elif character.race == "dwarf":
        dwarf_name_generator(character)
    elif character.race == "orc":
        orc_name_generator(character)
    elif character.race == "goblin":
        goblin_name_generator(character)
    elif character.race == "troll":
        troll_name_generator(character)
    elif character.race == "dragon":
        dragon_name_generator(character)
    elif character.race == "demon":
        demon_name_generator(character)
    elif character.race == "angel":
        angel_name_generator(character)
    elif character.race == "undead":
        undead_name_generator(character)
    elif character.race == "beast":
        beast_name_generator(character)
    elif character.race == "elemental":
        elemental_name_generator(character)
    elif character.race == "unknown":
        unknown_name_generator(character)

# A function that will generate a human name.
def human_name_generator(character):
    character.name = random.choice(["Anthony", "Bob", "Charlie", "David", "Ethan", "Frank", "George", "Henry", "Isaac", "John", "Kevin", "Larry", "Michael", "Nathan", "Oscar", "Peter", "Quinn", "Robert", "Steven", "Thomas", "Ulysses", "Victor", "William", "Xavier", "Yuri", "Zachary"])
    pass

# A function that will generate an elf name.
def elf_name_generator(character):
    character.name = random.choice([""])
    pass

# A function that will generate a dwarf name.
def dwarf_name_generator(character):
    pass

# A function that will generate an orc name.
def orc_name_generator(character):
    pass

# A function that will generate a goblin name.
def goblin_name_generator(character):
    pass

# A function that will generate a troll name.
def troll_name_generator(character):
    pass

# A function that will generate a dragon name.
def dragon_name_generator(character):
    pass

# A function that will generate a demon name.
def demon_name_generator(character):
    pass

# A function that will generate an angel name.
def angel_name_generator(character):
    pass

# A function that will generate an undead name.
def undead_name_generator(character):
    pass

# A function that will generate a beast name.
def beast_name_generator(character):
    pass

# A function that will generate an elemental name.
def elemental_name_generator(character):
    pass

# A function that will generate an unknown name.
def unknown_name_generator(character):
    pass

