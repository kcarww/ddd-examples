from dataclasses import dataclass
from entity.order import Order
from entity.order_item import OrderItem
from entity.customer import Customer
import uuid

@dataclass
class OrderService:
    
    @staticmethod
    def calculate_total(order: list[Order]) -> float:
        total = 0
        for item in order:
            total += item.price * item.quantity
        return total
    
    @staticmethod
    def place_order(customer: Customer, items: list[OrderItem]) -> Order:
        if len(items) == 0:
            raise ValueError("Cannot place an order without items")
        
        order = Order(id=str(uuid.uuid4()), customer_id=customer.id, items=items)
        customer.add_rewards_points(OrderService.calculate_total(order) / 2)
        return order
    