# Responsibilities -----
# piece mechanics
# piece color

STRAIGHT_PATTERNS: list[tuple[int, int]] = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]
DIAGONAL_PATTERNS: list[tuple[int, int]] = [
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]
L_PATTERNS: list[tuple[int, int]] = [
    (1, 2),
    (1, -2),
    (-1, 2),
    (-1, -2),
    (2, 1),
    (2, -1),
    (-2, 1),
    (-2, -1),
]


class Piece:

    def __init__(self, is_white: bool, moves_once: bool = False) -> None:
        self._id: str = ""
        self._is_white: bool = is_white
        self._moves_once: bool = moves_once
        self._movement_patterns: list[tuple[int, int]] = []

    def __repr__(self) -> str:
        return self._id


class Pawn(Piece):

    def __init__(self, is_white: bool, moves_once: bool = True) -> None:
        super().__init__(is_white, moves_once)
        self._id = "P"
        self._movement_patterns = [(0, 1)]


class Knight(Piece):

    def __init__(self, is_white: bool, moves_once: bool = True) -> None:
        super().__init__(is_white, moves_once)
        self._id = "N"
        self._movement_patterns.extend(L_PATTERNS)


class Rook(Piece):

    def __init__(self, is_white: bool, moves_once: bool = False) -> None:
        super().__init__(is_white, moves_once)
        self._id = "R"
        self._movement_patterns.extend(STRAIGHT_PATTERNS)


class Bishop(Piece):

    def __init__(self, is_white: bool, moves_once: bool = False) -> None:
        super().__init__(is_white, moves_once)
        self._id = "B"
        self._movement_patterns.extend(DIAGONAL_PATTERNS)


class Queen(Piece):

    def __init__(self, is_white: bool, moves_once: bool = False) -> None:
        super().__init__(is_white, moves_once)
        self._id = "Q"
        self._movement_patterns.extend(STRAIGHT_PATTERNS + DIAGONAL_PATTERNS)


class King(Piece):

    def __init__(self, is_white: bool, moves_once: bool = True) -> None:
        super().__init__(is_white, moves_once)
        self._id = "K"
        self._movement_patterns.extend(STRAIGHT_PATTERNS + DIAGONAL_PATTERNS)
