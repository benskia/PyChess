class Command:

    def __init__(self, target_id: str, x1: int, y1: int, x2: int, y2: int) -> None:
        self.id: str = target_id
        self.x1: int = x1
        self.y1: int = y1
        self.x2: int = x2
        self.y2: int = y2
