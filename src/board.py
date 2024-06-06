# Responsibilities -----
# board shape
# piece positions


from piece import ChessPiece

BOARD_SIZE: int = 8
EMPTY_RANK: list[ChessPiece | None] = [None] * BOARD_SIZE

class ChessBoard:

    def __init__(self) -> None:
        self._board: list[list[ChessPiece | None]]
        self.default_start()

    def default_start(self) -> None:
        self._board = []
        self._board.append(self.get_default_rows(True, True))
        self._board.append(self.get_default_rows(False, True))
        self._board.extend([EMPTY_RANK] * 4)
        self._board.append(self.get_default_rows(False, False))
        self._board.append(self.get_default_rows(True, False))


    def get_default_rows(self, is_back_rank: bool, is_white: bool) -> list[ChessPiece | None]:
        default_front_rank: list[ChessPiece | None] = [ChessPiece(is_white)] * BOARD_SIZE
        default_back_rank: list[ChessPiece | None] = [
            ChessPiece(is_white),
            ChessPiece(is_white),
            ChessPiece(is_white),
            ChessPiece(is_white),
            ChessPiece(is_white),
            ChessPiece(is_white),
            ChessPiece(is_white),
            ChessPiece(is_white),
        ]
        if is_back_rank: return default_back_rank
        return default_front_rank

