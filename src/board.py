# Responsibilities -----
# board shape
# piece positions


from piece import Piece

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


    def get_default_rows(self, is_back_rank: bool, is_white: bool) -> list[Piece | None]:
        default_front_rank: list[Piece | None] = [Piece(is_white, True)] * BOARD_SIZE
        default_back_rank: list[Piece | None] = [
            Piece(is_white),
            Piece(is_white, True),
            Piece(is_white),
            Piece(is_white, True),
            Piece(is_white),
            Piece(is_white),
            Piece(is_white, True),
            Piece(is_white),
        ]
        if is_back_rank: return default_back_rank
        return default_front_rank

