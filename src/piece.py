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
        self.id: str = ""
        self.is_white: bool = is_white
        self.moves_once: bool = moves_once
        self.movement_patterns: list[tuple[int, int]]

    def __repr__(self) -> str:
        return self.id


class Pawn(Piece):

    def __init__(self, is_white: bool, moves_once: bool = True) -> None:
        super().__init__(is_white, moves_once)
        self.id = "P"
        if self.is_white:
            self.movement_patterns.append((0, 1))
        else:
            self.movement_patterns.append((0, -1))


class Knight(Piece):

    def __init__(self, is_white: bool, moves_once: bool = True) -> None:
        super().__init__(is_white, moves_once)
        self.id = "N"
        self.movement_patterns = L_PATTERNS


class Rook(Piece):

    def __init__(self, is_white: bool, moves_once: bool = False) -> None:
        super().__init__(is_white, moves_once)
        self.id = "R"
        self.movement_patterns = STRAIGHT_PATTERNS


class Bishop(Piece):

    def __init__(self, is_white: bool, moves_once: bool = False) -> None:
        super().__init__(is_white, moves_once)
        self.id = "B"
        self.movement_patterns = DIAGONAL_PATTERNS


class Queen(Piece):

    def __init__(self, is_white: bool, moves_once: bool = False) -> None:
        super().__init__(is_white, moves_once)
        self.id = "Q"
        self.movement_patterns = STRAIGHT_PATTERNS + DIAGONAL_PATTERNS


class King(Piece):

    def __init__(self, is_white: bool, moves_once: bool = True) -> None:
        super().__init__(is_white, moves_once)
        self.id = "K"
        self.movement_patterns = STRAIGHT_PATTERNS + DIAGONAL_PATTERNS
