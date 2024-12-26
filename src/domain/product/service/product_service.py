from dataclasses import dataclass
from domain.product.entity.product import Product

@dataclass
class ProductService:
    
    @staticmethod
    def incrise_price(products: list[Product], percentage: float) -> list[Product]:
        result = []
        for prod in products:
            prod.price = prod.price + (prod.price * percentage / 100)
            result.append(prod)
        return result