# Responsibilities -----
# start game
# which player
# parse input


from board import Board
from command_validators import validate_command
from move_validators import validate_move


class Command:

    def __init__(self, target_id: str, x1: int, y1: int, x2: int, y2: int) -> None:
        self._id: str = target_id
        self._x1: int = x1
        self._y1: int = y1
        self._x2: int = x2
        self._y2: int = y2


class Game:

    def __init__(self) -> None:
        self._input_prompt: str = "Input command in algebraic notation (ex: Nb1e3): "
        self._is_white: bool = True
        self._board = Board()

    def run_game(self) -> None:
        print(self._board)
        cmd: Command | None = None
        while not cmd:
            cmd = self.__get_command(input(self._input_prompt))

    def __get_command(self, potential_cmd: str) -> Command | None:
        if not validate_command(potential_cmd):
            return None
        cmd = self.__parse_command(potential_cmd)
        if not validate_move(cmd, self._board):
            return None
        return cmd

    def __parse_command(self, command: str) -> Command:
        x1: int = ord(command[1]) - 97
        y1: int = int(command[2])
        x2: int = ord(command[3]) - 97
        y2: int = int(command[4])
        return Command(command[0], x1, y1, x2, y2)
