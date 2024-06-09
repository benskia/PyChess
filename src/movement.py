from command import Command
from piece import Piece


def validate_move(cmd: Command, board: list[list[Piece | None]]) -> bool:
    source: Piece | None = board[cmd._y1][cmd._x1]
    if not isinstance(source, Piece):
        return False
    movement: tuple[int, int] = (abs(cmd._x1 - cmd._x2), abs(cmd._y1 - cmd._y2))
    if not validate_pattern(movement_to_pattern(movement), source):
        return False
    if not validate_piece_range(movement, source):
        return False
    if not validate_line_of_site(cmd, board):
        return False
    return True


def movement_to_pattern(movement: tuple[int, int]) -> tuple[int, int]:
    pattern_x: int = 0 if movement[0] == 0 else 1
    pattern_y: int = 0 if movement[1] == 0 else 1
    return (pattern_x, pattern_y)


def validate_pattern(pattern: tuple[int, int], pc: Piece) -> bool:
    if pattern not in pc._movement_patterns:
        print(f"{pattern} not found in {pc} movement patterns")
        return False
    return True


def validate_piece_range(movement: tuple[int, int], pc: Piece) -> bool:
    # Patterns are just (x,y) of single-space moves. If the movement doesn't
    # match any of the piece's patterns, it's a multi-space movement.
    if pc._moves_once and movement not in pc._movement_patterns:
        print(f"{pc} can only move once, but {movement} is more than one square away.")
        return False
    return True


def validate_line_of_site(cmd: Command, board: list[list[Piece | None]]) -> bool:
    current_rank: int = min(cmd._y1, cmd._y2)
    end_rank: int = max(cmd._y1, cmd._y2)
    current_file: int = min(cmd._x1, cmd._x2)
    end_file: int = max(cmd._x1, cmd._x2)
    while current_rank < end_rank and current_file < end_file:
        current_rank +
    return True
