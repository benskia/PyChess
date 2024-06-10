# Responsibilities -----
# start game
# which player
# parse input


from board import Board
from command import Command, validate_command
from movement import validate_move
from piece import King, Piece


class Game:

    def __init__(self) -> None:
        self._input_prompt: str = (
            "Input command in algebraic notation (ex: Nb1c3) (Q to quit): "
        )
        self._game_complete: bool = False
        self._is_white: bool = True
        self._board = Board()

    def get_player_color(self, is_white: bool) -> str:
        if is_white:
            return "White"
        else:
            return "Black"

    def run_game(self) -> None:
        while not self._game_complete:
            print(f"\n {self.get_player_color(self._is_white)}'s Turn")
            print(self._board)
            user_input: str = input(self._input_prompt)
            if user_input == "Q":
                break
            cmd: Command | None = self.__get_command(user_input)
            if cmd and validate_move(cmd, self._board):
                self.__execute_command(cmd)
        print("Ending game...")

    def __parse_command(self, command: str) -> Command:
        x1: int = ord(command[1]) - 97
        y1: int = int(command[2]) - 1
        x2: int = ord(command[3]) - 97
        y2: int = int(command[4]) - 1
        return Command(command[0], x1, y1, x2, y2)

    def __get_command(self, potential_cmd: str) -> Command | None:
        if not validate_command(potential_cmd):
            return None
        return self.__parse_command(potential_cmd)

    def __execute_command(self, cmd: Command) -> None:
        source: Piece | None = self._board._grid[cmd._y1][cmd._x1]
        if source is None or source._id != cmd._id:
            print(f"'{cmd._id}' not found at origin square")
            return
        if source._is_white != self._is_white:
            print("Player and piece colors don't match.")
            return
        target: Piece | None = self._board._grid[cmd._y2][cmd._x2]
        self._board._grid[cmd._y2][cmd._x2] = source
        self._board._grid[cmd._y1][cmd._x1] = None
        if isinstance(target, Piece):
            print(f"{self.get_player_color(self._is_white)}'s '{source}'", end="")
            print(f" captures {self.get_player_color(not self._is_white)}'s '{target}'")
            if isinstance(target, King):
                print(f"{self.get_player_color(self._is_white)} wins!")
                self._game_complete = True
        self._is_white = not self._is_white
