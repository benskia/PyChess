from board import Board
from command import Command
from piece import Piece


def validate_move(cmd: Command, board: Board) -> bool:
    source: Piece | None = board._grid[cmd._y1][cmd._x1]
    if not isinstance(source, Piece):
        print("Source piece doesn't exist.")
        return False
    target: Piece | None = board._grid[cmd._y2][cmd._x2]
    if friendly_firing(source, target):
        return False
    movement: tuple[int, int] = (abs(cmd._x1 - cmd._x2), abs(cmd._y1 - cmd._y2))
    pattern: tuple[int, int] = movement_to_pattern(movement, source)
    if not validate_pattern(pattern, source):
        return False
    if not moving_within_range(movement, source):
        return False
    if source._moves_once:
        return True
    return in_line_of_sight(pattern, cmd, board)


def friendly_firing(source: Piece | None, target: Piece | None) -> bool:
    if isinstance(source, Piece) and isinstance(target, Piece):
        if source._is_white == target._is_white:
            print("Abandoning command that results in friendly fire.")
            return True
    return False


def movement_to_pattern(movement: tuple[int, int], pc: Piece) -> tuple[int, int]:
    if pc._id == "N":
        return movement
    pattern_x: int = 0 if movement[0] == 0 else 1
    pattern_y: int = 0 if movement[1] == 0 else 1
    return (pattern_x, pattern_y)


def validate_pattern(pattern: tuple[int, int], pc: Piece) -> bool:
    if pattern not in pc._movement_patterns:
        print(f"{pattern} not found in {pc} movement patterns")
        return False
    return True


def moving_within_range(movement: tuple[int, int], pc: Piece) -> bool:
    # Patterns are just (x,y) of single-space moves. If the movement doesn't
    # match any of the piece's patterns, it's a multi-space movement.
    if pc._moves_once and movement not in pc._movement_patterns:
        print(f"{pc} can only move once, but {movement} is more than one square away.")
        return False
    return True


# TODO: indexing goes out of bounds
def in_line_of_sight(pattern: tuple[int, int], cmd: Command, board: Board) -> bool:
    current_file: int = min(cmd._x1, cmd._x2) + pattern[0]
    end_file: int = max(cmd._x1, cmd._x2)
    current_rank: int = min(cmd._y1, cmd._y2) + pattern[1]
    end_rank: int = max(cmd._y1, cmd._y2)
    while (current_file, current_rank) is not (end_file, end_rank):
        if isinstance(board._grid[current_rank][current_file], Piece):
            print(f"Collided with piece at row {current_rank}, col {current_file}")
            return False
        current_file += pattern[0]
        current_rank += pattern[1]
    return True
