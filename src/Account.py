from dataclasses import dataclass

@dataclass
class Account:
    type: str
    url: str
    balance: int