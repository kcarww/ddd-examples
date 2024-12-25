from dataclasses import dataclass
from typing import List, Optional
from sqlalchemy.orm import Session
from domain.entity.address import Address
from domain.entity.customer import Customer
from domain.entity.order import Order
from domain.entity.order_item import OrderItem
from domain.repository.order_repository_interface import OrderRepositoryInterface
from infrastructure.db.alchemy_orm.model import customer_model
from infrastructure.db.alchemy_orm.model.customer_model import CustomerModel
from infrastructure.db.alchemy_orm.model.order_item import OrderItemModel
from infrastructure.db.alchemy_orm.model.order_model import OrderModel

@dataclass
class OrderRepository(OrderRepositoryInterface):
    session: Session

    def create(self, order: Order) -> None:
        order_model = OrderModel(
            id=order.id,
            customer_id=order.customer_id,
            total=order.total,
            items=[
                OrderItemModel(
                    id=item.id,
                    product_id=item.product_id,
                    quantity=item.quantity,
                    name=item.name,
                    price=item.price
                ) for item in order.items
            ]

        )
        self.session.add(order_model)
        self.session.commit()

    def update(self, order: Order) -> None:
        pass

    def find_by_id(self, id: str) -> Optional[Order]:
        order_model = self.session.query(OrderModel).filter_by(id=id).first()
        if order_model:
            return Order(
                id=order_model.id,
                customer_id=order_model.customer_id,
                total=order_model.total,
                items=[
                    OrderItem(
                        id=item.id,
                        product_id=item.product_id,
                        quantity=item.quantity,
                        name=item.name,
                        price=item.price
                    ) for item in order_model.items
                ]
            )
        return None

    def find_all(self) -> List[Order]:
        orders_model = self.session.query(OrderModel).all()
        return [
            Order(
                id=order_model.id,
                customer_id=order_model.customer_id,
                total=order_model.total,
                items=[
                    OrderItem(
                        id=item.id,
                        product_id=item.product_id,
                        quantity=item.quantity,
                        name=item.name,
                        price=item.price
                    ) for item in order_model.items
                ]
            ) for order_model in orders_model
        ]
