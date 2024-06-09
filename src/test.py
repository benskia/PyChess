import unittest

from chess import Game
from command import Command, validate_command


class TestChess(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Game()

    # Command Parsing

    def test_invalid_cmdstr(self):
        invalid_cmdstr: str = "Nf5"
        self.assertEqual(validate_command(invalid_cmdstr), False)

    def test_valid_cmdstr(self):
        valid_cmdstr: str = "Nb1c3"
        self.assertEqual(validate_command(valid_cmdstr), True)

    def test_parse_command(self):
        valid_cmdstr: str = "Nb1c3"
        expected_cmd: Command = Command("N", 1, 0, 2, 2)
        test_cmd: Command = self.game.__parse_command(valid_cmdstr)
        self.assertEqual(str(test_cmd), str(expected_cmd))


if __name__ == "__main__":
    unittest.main()
