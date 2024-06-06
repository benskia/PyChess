# Responsibilities -----
# board shape
# piece positions


from piece import *

BOARD_SIZE: int = 8
EMPTY_RANK: list[Piece | None] = [None] * BOARD_SIZE


class Board:

    def __init__(self) -> None:
        self.grid: list[list[Piece | None]]
        self.default_start()

    def default_start(self) -> None:
        self.grid = []
        self.grid.append(self.get_default_rows(True, True))
        self.grid.append(self.get_default_rows(False, True))
        self.grid.extend([EMPTY_RANK] * 4)
        self.grid.append(self.get_default_rows(False, False))
        self.grid.append(self.get_default_rows(True, False))

    def get_default_rows(
        self, is_back_rank: bool, is_white: bool
    ) -> list[Piece | None]:
        default_front_rank: list[Piece | None] = [Pawn(is_white)] * BOARD_SIZE
        default_back_rank: list[Piece | None] = [
            Rook(is_white),
            Knight(is_white),
            Bishop(is_white),
            King(is_white),
            Queen(is_white),
            Bishop(is_white),
            Knight(is_white),
            Rook(is_white),
        ]
        if is_back_rank:
            return default_back_rank
        return default_front_rank

    def __repr__(self) -> str:
        output: str = "\n"
        for rank in self.grid:
            for file in rank:
                if file:
                    output += f" {file} "
                else:
                    output += f" * "
            output += "\n\n"

        return output
