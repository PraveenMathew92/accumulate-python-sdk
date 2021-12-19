from dataclasses import dataclass

@dataclass
class Error(Exception):
    code: int
    message: str
    data: int