from dataclasses import dataclass
from typing import List

from domain.checkout.entity.order import Order

@dataclass
class OrderItem:
    id: str
    name: str
    product_id: str
    quantity: int
    price: float

@dataclass
class OrderFactoryProps:
    id: str
    customer_id: str
    items: List[OrderItem]


@dataclass
class OrderFactory:
    def create(props: OrderFactoryProps) -> Order:
        items = [
            OrderItem(
                id=item.id,
                name=item.name,
                product_id=item.product_id,
                quantity=item.quantity,
                price=item.price
            )
            for item in props.items
        ]

        return Order(
            id=props.id,
            customer_id=props.customer_id,
            items=items
        )