# Responsibilities -----
# piece mechanics
# piece color


class Piece:

    def __init__(self, is_white: bool, moves_once: bool = False) -> None:
        self.id: str = ""
        self.is_white: bool = is_white
        self.moves_once: bool = moves_once

    def __repr__(self) -> str:
        return self.id
