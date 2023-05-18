
import unittest
from character_classes import Character, Player, Enemy, Summon

class TestCharacterClass(unittest.TestCase):
    def setUp(self):
        self.character = Character("TestCharacter")
        self.player = Player("TestPlayer")
        self.enemy = Enemy("TestEnemy")
        self.summon = Summon("TestSummon")

    def test_initialization(self):
        self.assertEqual(self.character.name, "TestCharacter")
        self.assertEqual(self.player.name, "TestPlayer")
        self.assertEqual(self.enemy.name, "TestEnemy")
        self.assertEqual(self.summon.name, "TestSummon")

    def test_set_and_get_stat(self):
        self.player.set_stat('STR', 5)
        self.assertEqual(self.player.get_stat('STR'), 5)

        # try setting an invalid stat
        with self.assertRaises(ValueError):
            self.player.set_stat('STR', -1)

    def test_stat_initial_values(self):
        for char in [self.character, self.player, self.enemy, self.summon]:
            for stat in char.base_stats.keys():
                self.assertEqual(char.get_stat(stat), 1)

    def test_invalid_stat(self):
        with self.assertRaises(ValueError):
            self.player.get_stat('INVALID_STAT')

        with self.assertRaises(ValueError):
            self.player.set_stat('INVALID_STAT', 1)


if __name__ == '__main__':
    unittest.main()
