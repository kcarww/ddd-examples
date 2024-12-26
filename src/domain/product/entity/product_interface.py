from abc import ABC
from dataclasses import dataclass

@dataclass
class ProductInterface(ABC):
    id: str
    name: str
    price: float