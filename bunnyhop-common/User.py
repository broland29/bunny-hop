from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    uid: int = None
    username: str = None
    password: str = None       # passwords stored should already be encrypted, but in string format! (not bytes).
    is_admin: bool = None      # use .decode('UTF-8')
