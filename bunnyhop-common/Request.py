from dataclasses import dataclass


@dataclass(frozen=True)
class Request:
    request_type: str
    pickled_data: bytes

