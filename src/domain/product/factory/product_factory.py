from dataclasses import dataclass
from uuid import uuid4

from domain.product.entity.product import Product
from domain.product.entity.product_interface import ProductInterface

@dataclass
class ProductFactory:
    def create(name: str, price: float) -> ProductInterface:
        return Product(id=uuid4(), name=name, price=price)