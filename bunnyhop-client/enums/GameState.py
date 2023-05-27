from enum import Enum, auto


class GameState(Enum):
    Idle = auto()       # before playing, everything in starting position
    Running = auto()    # bunny was moved at least once
    Paused = auto()     # user paused
    Over = auto()       # bunny reached the carrot
