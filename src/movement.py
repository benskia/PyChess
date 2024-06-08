from command import Command
from piece import Piece


def validate_move(cmd: Command, board: list[list[Piece | None]]) -> bool:
    source: Piece | None = board[cmd._y1][cmd._x1]
    if not isinstance(source, Piece):
        return False
    print(source._movement_patterns)
    # TODO: Need some logic for determining valid movements. Perhaps comparing
    # the difference between origin and destination x:y values.
    return True

