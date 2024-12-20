from dataclasses import dataclass, field
from order_item import OrderItem

@dataclass(kw_only=True)
class Order:
    id: str
    customer_id: str
    items: list[OrderItem] = field(default_factory=list)

