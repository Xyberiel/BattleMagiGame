# This module will handle all functions related to generating names for allies, summons, and enemies.
# This module will also handle all functions related to generating names for places and magic items.
import random

# A list of all the races
races = ["human", "elf", "dwarf", "orc", "goblin", "troll", "dragon", "demon", "angel", "undead", "beast", "elemental", "insectoid", "atlantian", "anthro", "unknown"]

# A dictionary containing subraces
subraces = {
    "human": ["highlander", "islander", "sandwalker", "plainsmen", "mirefolk"],
    "elf": ["high elf", "wood elf", "dark elf", "grey elf", "wild elf", "drow", "blood elf"],
    "dwarf": ["hill dwarf", "mountain dwarf", "deep dwarf", "steppe dwarf"],
    "orc": ["bloodforged", "ironhide", "frostborn", "felltusk", "scorchedclaw", "stonefist"],
    "goblin": ["forest goblin", "mountain goblin", "swamp goblin"],
    "troll": ["mossback", "cave troll", "mountain troll", "swamp troll"],
    "dragon": ["red dragon", "blue dragon", "green dragon", "black dragon", "white dragon", "gold dragon", "silver dragon", "bronze dragon", "copper dragon", "brass dragon", "purple dragon"],
    "demon": ["imp", "succubus", "incubus", "devil", "fiend", "abomination", "hellspawn", "archdemon"],
    "angel": ["cherubim", "seraphim", "authority", "principalities", "powers", "virtues", "dominions", "thrones"],
    "undead": ["skeleton", "zombie", "ghost", "vampire", "lich"],
    "giants": ["hill giant", "mountain giant", "frost giant", "fire giant", "storm giant", "cloud giant", "stone giant", "titan"],
    "beast": ["aquatic", "flying", "subterranean", "arctic", "mythical", "prehistoric", "volcanic", "apex"],
    "elemental": ["pyromorph", "hydromorph", "aeromorph", "lithomorph", "cryomorph", "electromorph", "dendromorph"],
    "insectoid": ["beetle", "spider", "mantis", "ant", "bee"],
    "atlantian": ["shark", "squid", "jellyfish", "crustatean", "walrus"],
    "anthro": ["feline", "canine", "primate", "rodent", "rabbit"],
    "unknown": ["unknown"]
}

# A list of all the biomes
biomes = ["forest", "mountain", "desert", "swamp", "tundra", "plains", "jungle", "cave", "city", "dungeon", "castle", "unknown"]

# A list of all the weapons
weapons = ["sword", "axe", "hammer", "bow", "spear", "dagger", "staff", "wand", "mace", "flail", "scythe", "whip", "fist", "unknown"]


# name generator class that will handle all name generation
class NameGenerator:
    # constructor
    def __init__(self):
        # dictionary of possible character names based on race
        self.character_name_library = {
            'orc': {
                'first_names': ['Grim', 'Gore', 'Cold', 'Iron'],
                'last_names': ['Tooth', 'Flesh', 'Hide', 'Bash', 'Snarl'],
                'titles': ['the Greedy', 'the Brutal', 'the Coward', 'the Wise'],
            },
            'elf': {
                'first_names': ['Aer', 'Ili', 'Eol', 'Ori'],
                'last_names': ['wind', 'shadow', 'light', 'fire'],
                'titles': ['the Swift', 'the Beautiful', 'the Wise', 'the Cunning'],
            },
            'human': {
                'first_names': ['John', 'Jane', 'Jack', 'Jill'],
                'last_names': ['Smith', 'Johnson', 'Williams', 'Jones'],
                'titles': ['the Brave', 'the Wise', 'the Strong', 'the Cunning'],
            },
            'dwarf': {
                'first_names': ['Thorin', 'Gimli', 'Balin', 'Dwalin'],
                'last_names': ['Stone', 'Iron', 'Gold', 'Silver'],
                'titles': ['the Brave', 'the Wise', 'the Strong', 'the Cunning'],
            },
            'goblin': {
                'first_names': ['Gnarl', 'Grim', 'Gore', 'Cold'],
                'last_names': ['Tooth', 'Flesh', 'Hide', 'Bash', 'Snarl'],
                'titles': ['the Greedy', 'the Brutal', 'the Coward', 'the Wise'],
            },
            'troll': {
                'first_names': ['Gnarl', 'Grim', 'Gore', 'Cold'],
                'last_names': ['Tooth', 'Flesh', 'Hide', 'Bash', 'Snarl'],
                'titles': ['the Greedy', 'the Brutal', 'the Coward', 'the Wise'],
            },
            'dragon': {
                'first_names': ['Aer', 'Ili', 'Eol', 'Ori'],
                'last_names': ['wind', 'shadow', 'light', 'fire'],
                'titles': ['the Swift', 'the Beautiful', 'the Wise', 'the Cunning'],
            },
            'demon': {
                'first_names': ['Grim', 'Gore', 'Cold', 'Iron'],
                'last_names': ['Tooth', 'Flesh', 'Hide', 'Bash', 'Snarl'],
                'titles': ['the Greedy', 'the Brutal', 'the Coward', 'the Wise'],
            },
            'angel': {
                'first_names': ['Aer', 'Ili', 'Eol', 'Ori'],
                'last_names': ['wind', 'shadow', 'light', 'fire'],
                'titles': ['the Swift', 'the Beautiful', 'the Wise', 'the Cunning'],
            },
            'undead': {
                'first_names': ['Grim', 'Gore', 'Cold', 'Iron'],
                'last_names': ['Tooth', 'Flesh', 'Hide', 'Bash', 'Snarl'],
                'titles': ['the Greedy', 'the Brutal', 'the Coward', 'the Wise'],
            },
            'beast': {
                'first_names': ['Gnarl', 'Grim', 'Gore', 'Cold'],
                'last_names': ['Tooth', 'Flesh', 'Hide', 'Bash', 'Snarl'],
                'titles': ['the Greedy', 'the Brutal', 'the Coward', 'the Wise'],
            },
            'elemental': {
                'first_names': ['Aer', 'Ili', 'Eol', 'Ori'],
                'last_names': ['wind', 'shadow', 'light', 'fire'],
                'titles': ['the Swift', 'the Beautiful', 'the Wise', 'the Cunning'],
            },
            'unknown': {
                'first_names': ['Gnarl', 'Grim', 'Gore', 'Cold'],
                'last_names': ['Tooth', 'Flesh', 'Hide', 'Bash', 'Snarl'],
                'titles': ['the Greedy', 'the Brutal', 'the Coward', 'the Wise'],
            },
        }

        # dictionary of possible place names based on biome
        self.place_name_library = {
            'forest': {
                'first_parts': ['Sunny', 'Shady', 'Windy', 'Quiet'],
                'second_parts': ['Vale', 'Glen', 'Thicket', 'Grove'],
            },
            'mountain': {
                'first_parts': ['Jagged', 'Snowy', 'Searing', 'Calm'],
                'second_parts': ['Peak', 'Range', 'Point', 'Cliff'],
            },
            # Add more biomes here...
        }

        # dictionary of possible magic item names based on weapon type
        self.magic_item_name_library = {
            'sword': {
                'adjectives': ['Fire', 'Ice', 'Wind', 'Earth'],
                'suffixes': ['of Power', 'of Speed', 'of Wisdom', 'of Fury'],
            },
            'axe': {
                'adjectives': ['Berserker\'s', 'Executioner\'s', 'Warrior\'s', 'Defender\'s'],
                'suffixes': ['of Might', 'of Precision', 'of Fortitude', 'of the Bear'],
            },
            # Add more weapon types here...
        }

        # A set of all the generated names
        self.generated_names = set()

    # function to generate a character name
    def generate_character_name(self, race):
        if race not in self.character_name_library:
            raise ValueError('Unsupported race')
        
        while True:
            first_name = random.choice(self.character_name_library[race]['first_names'])
            last_name = random.choice(self.character_name_library[race]['last_names'])
            title = random.choice(self.character_name_library[race]['titles'])

            name = f'{first_name}{last_name} {title}'

            if name not in self.generated_names:
                self.generated_names.add(name)
                return name

    def generate_place_name(self, biome):
        if biome not in self.place_name_library:
            raise ValueError('Unsupported biome')

        while True:
            first_part = random.choice(self.place_name_library[biome]['first_parts'])
            second_part = random.choice(self.place_name_library[biome]['second_parts'])
            
            name = f'{first_part} {second_part}'

            if name not in self.generated_names:
                self.generated_names.add(name)
                return name

    def generate_magic_item_name(self, weapon_type):
        if weapon_type not in self.magic_item_name_library:
            raise ValueError('Unsupported weapon type')

        while True:
            adjective = random.choice(self.magic_item_name_library[weapon_type]['adjectives'])
            suffix = random.choice(self.magic_item_name_library[weapon_type]['suffixes'])
            
            name = f'{adjective} {weapon_type.capitalize()} {suffix}'

            if name not in self.generated_names:
                self.generated_names.add(name)
                return name
