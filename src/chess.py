# Responsibilities -----
# start game
# which player
# parse input


from board import Board
from command import Command, validate_command
from movement import validate_move
from piece import Piece




class Game:

    def __init__(self) -> None:
        self._input_prompt: str = "Input command in algebraic notation (ex: Nb1e3) (Q to quit): "
        self._is_white: bool = True
        self._board = Board()

    def run_game(self) -> None:
        while True:
            print(self._board)
            user_input: str = input(self._input_prompt)
            if user_input == "Q":
                break
            cmd: Command | None = self.__get_command(user_input)
            if cmd:
                print(f"executing command ({cmd._x1, cmd._y1}) to ({cmd._x2, cmd._y2})")
                self.__execute_command(cmd)
        print("ending game...")

    def __parse_command(self, command: str) -> Command:
        x1: int = ord(command[1]) - 97
        y1: int = int(command[2]) - 1
        x2: int = ord(command[3]) - 97
        y2: int = int(command[4]) - 1
        return Command(command[0], x1, y1, x2, y2)

    def __get_command(self, potential_cmd: str) -> Command | None:
        if not validate_command(potential_cmd):
            return None
        cmd = self.__parse_command(potential_cmd)
        if not validate_move(cmd, self._board._grid):
            return None
        return cmd

    def __execute_command(self, cmd: Command) -> None:
        source: Piece | None = self._board._grid[cmd._y1][cmd._x1]
        # target: Piece | None = self._board._grid[cmd._y2][cmd._x2]
        if source is None or source._id != cmd._id:
            print(f"'{cmd._id}' not found at origin square")
            return
        self._board._grid[cmd._y2][cmd._x2] = source
        self._board._grid[cmd._y1][cmd._x1] = None
