from dataclasses import dataclass

@dataclass
class OrderItem:
    id: str
    name: str
    price: float

    