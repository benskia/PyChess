from command import Command
from piece import Piece


def validate_move(cmd: Command, board: list[list[Piece | None]]) -> bool:
    source: Piece | None = board[cmd._y1][cmd._x1]
    if not isinstance(source, Piece):
        return False
    print(source._movement_patterns)
    # TODO: Need some logic for determining valid movements. Perhaps comparing
    # the (origin x:y - destination x:y) and piece movement patterns.
    x_diff: int = abs(cmd._x1 - cmd._x2)
    y_diff: int = abs(cmd._y1 - cmd._y2)
    return True


def validate_pattern(cmd_pattern: tuple[int, int], pc: Piece) -> bool:
    if cmd_pattern not in pc._movement_patterns:
        print(f"{cmd_pattern} not found in {pc} movement patterns")
        return False
    return True
