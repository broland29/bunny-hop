from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Game:
    gid: int = None
    uid: int = None
    date: datetime = None
    time: int = None
    difficulty: int = None
    optimal_path_length: int = None
    actual_path_length: int = None
