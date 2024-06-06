# Responsibilities -----
# start game
# which player
# parse input


from board import Board


class Game:

    def __init__(self) -> None:
        self.is_white: bool = True
        self.board = Board()

    def parse_command(self, command: str) -> None:
        pass
