# Responsibilities -----
# board shape
# piece positions


from piece import *

BOARD_SIZE: int = 8
EMPTY_RANK: list[Piece | None] = [None] * BOARD_SIZE


class Board:

    def __init__(self) -> None:
        self._grid: list[list[Piece | None]]
        self.__default_start()

    def __default_start(self) -> None:
        self._grid = []
        self._grid.append(self.__default_rows(True, True))
        self._grid.append(self.__default_rows(False, True))
        self._grid.extend([EMPTY_RANK] * 4)
        self._grid.append(self.__default_rows(False, False))
        self._grid.append(self.__default_rows(True, False))

    def __default_rows(self, is_back_rank: bool, is_white: bool) -> list[Piece | None]:
        if is_back_rank:
            return [
                Rook(is_white),
                Knight(is_white),
                Bishop(is_white),
                King(is_white),
                Queen(is_white),
                Bishop(is_white),
                Knight(is_white),
                Rook(is_white),
            ]
        return [Pawn(is_white)] * BOARD_SIZE

    def __repr__(self) -> str:
        output: str = "\n"
        for rank in self._grid:
            for file in rank:
                if file:
                    output += f" {file} "
                else:
                    output += f" * "
            output += "\n\n"

        return output
