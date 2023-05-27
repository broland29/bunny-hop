from enum import Enum, auto


class CellType(Enum):
    E = Empty = auto()
    B = Bunny = auto()
    T = Trap = auto()
    C = Carrot = auto()

    def __str__(self):
        return self.name
