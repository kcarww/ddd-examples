from dataclasses import dataclass

@dataclass
class OrderItem:
    id: str
    name: str
    price: float
    product_id: str
    quantity: int

    

    