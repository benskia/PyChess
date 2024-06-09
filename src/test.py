import unittest

from chess import Game
from command import Command, validate_command
from board import Board
from movement import validate_move
from piece import *


class TestChess(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Game()

    def test_invalid_cmdstr(self):
        invalid_cmdstr: str = "Nf5"
        self.assertFalse(validate_command(invalid_cmdstr))

    def test_valid_cmdstr(self):
        valid_cmdstr: str = "Nb1c3"
        self.assertTrue(validate_command(valid_cmdstr))

    def test_parse_command(self):
        valid_cmdstr: str = "Nb1c3"
        test_cmd: Command = self.game._Game__parse_command(valid_cmdstr)
        valid_cmd: Command = Command("N", 1, 0, 2, 2)
        self.assertEqual(str(test_cmd), str(valid_cmd))

    def test_invalid_move(self):
        invalid_cmd: Command = Command("N", 1, 0, 2, 5)
        self.assertFalse(validate_move(invalid_cmd, self.game._board))

    def test_valid_move(self):
        valid_cmd: Command = Command("N", 1, 0, 2, 2)
        expected_board: Board = Board()
        expected_board._grid[0][1] = None
        expected_board._grid[2][2] = Knight(True)
        self.game._Game__execute_command(valid_cmd)
        self.assertEqual(str(self.game._board), str(expected_board))


if __name__ == "__main__":
    unittest.main()
