from unittest import TestCase
from main import TicTacGame


class TestTicTacGame(TestCase):
    def setUp(self):
        self.game = TicTacGame(30)
        self.game.game = [['x', '1', '2'],
                          ['3', '4', '5'],
                          ['6', '7', '8']]

    def test_validate_input(self):
        self.assertEqual(self.game.validate_input('rebeebr'), False)
        self.assertEqual(self.game.validate_input('-100'), False)
        self.assertEqual(self.game.validate_input('30'), False)
        self.assertEqual(self.game.validate_input('1.5'), False)
        self.assertEqual(self.game.validate_input('2'), 2)
        self.assertEqual(self.game.validate_input('0'), False)

    def test_insert_into_field(self):
        self.game.insert_into_field("x", 4)
        self.assertEqual(self.game.game, [['x', '1', '2'], ['3', 'x', '5'], ['6', '7', '8']])
        self.game.insert_into_field("o", 8)
        self.assertEqual(self.game.game, [['x', '1', '2'], ['3', 'x', '5'], ['6', '7', 'o']])

    def test_check_winner(self):
        self.game.game = [['x', '1', 'o'],
                          ['3', 'x', '5'],
                          ['o', '7', 'x']]
        self.assertEqual(self.game.check_winner(4), True)
        self.game.game = [['x', '1', 'o'],
                          ['3', 'x', 'x'],
                          ['o', '7', '8']]
        self.assertEqual(self.game.check_winner(4), False)
        self.game.game = [['o', 'o', 'o'],
                          ['3', 'x', 'x'],
                          ['x', '7', 'x']]
        self.assertEqual(self.game.check_winner(0), True)
        self.game.game = [['o', 'o', 'x'],
                          ['3', 'o', 'x'],
                          ['x', '7', 'x']]
        self.assertEqual(self.game.check_winner(2), True)
        self.game.game = [['o', 'o', 'x'],
                          ['3', 'x', 'x'],
                          ['x', '7', 'o']]
        self.assertEqual(self.game.check_winner(2), True)
