# Responsibilities -----
# start game
# which player
# parse input


from board import Board
from command import Command
from command_validators import validate_command


class Game:

    def __init__(self) -> None:
        self.is_white: bool = True
        self.board = Board()

    def parse_command(self, command: str) -> Command | None:
        if not validate_command(command):
            return None
        x1: int = ord(command[1]) - 97
        y1: int = int(command[2])
        x2: int = ord(command[3]) - 97
        y2: int = int(command[4])
        return Command(command[0], x1, y1, x2, y2)
