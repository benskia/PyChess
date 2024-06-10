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

    def get_movement_patterns(self) -> list[tuple[int, int]]:
        return self._movement_patterns

    def __repr__(self) -> str:
        return self._id


class Pawn(Piece):

    def __init__(self, is_white: bool, moves_once: bool = True) -> None:
        super().__init__(is_white, moves_once)
        self._id = "P"
        self._first_move: bool = True
        self.rebuild_movement_patterns(False)

    def rebuild_movement_patterns(self, is_attacking: bool) -> None:
        new_movement_patterns: list[list[int]] = [[0, 1]]
        if self._first_move:
            new_movement_patterns.append([0, 2])
        if is_attacking:
            new_movement_patterns.extend([[1, 1], [1, -1]])
        if not self._is_white:
            for i in range(len(new_movement_patterns)):
                new_movement_patterns[i][1] *= -1
        self._movement_patterns = [
            (pattern[0], pattern[1]) for pattern in new_movement_patterns
        ]

    def toggle_first_move(self) -> None:
        self._first_move = False


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
