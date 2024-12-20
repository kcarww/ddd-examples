from dataclasses import dataclass
from typing import List, Optional
from sqlalchemy.orm import Session
from domain.entity.product import Product
from domain.repository.product_repository_interface import ProductRepositoryInterface
from infrastructure.db.alchemy_orm.model.product_model import ProductModel

@dataclass
class ProductRepository(ProductRepositoryInterface):
    session: Session

    def create(self, product: Product) -> None:
        product_model = ProductModel(
            id=product.id,
            name=product.name,
            price=product.price
        )
        self.session.add(product_model)
        self.session.commit()

    def update(self, product: Product) -> None:
        product_model = self.session.query(ProductModel).filter_by(id=product.id).first()
        if product_model:
            product_model.name = product.name
            product_model.price = product.price
            self.session.commit()
        else:
            raise ValueError(f"Product with id {product.id} not found")

    def find_by_id(self, id: str) -> Optional[Product]:
        product_model = self.session.query(ProductModel).filter_by(id=id).first()
        if product_model:
            return Product(
                id=product_model.id,
                name=product_model.name,
                price=product_model.price
            )
        return None

    def find_all(self) -> List[Product]:
        product_models = self.session.query(ProductModel).all()
        return [
            Product(
                id=product_model.id,
                name=product_model.name,
                price=product_model.price
            ) for product_model in product_models
        ]
