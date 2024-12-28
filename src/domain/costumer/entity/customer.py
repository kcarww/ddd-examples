from dataclasses import dataclass, field
from uuid import uuid4

from domain._shared.entity.entity import Entity
from domain.costumer.entity.value_object.address import Address

@dataclass(kw_only=True)
class Customer(Entity):
    name: str
    address: Address
    active: bool = True
    rewards_points: int = 0


    def __post_init__(self):
        self.validate()

    def validate(self):
        if not self.id:
            self.notification.add_error("ID is required")
        if not self.name:
            self.notification.add_error("Name is required")
        if not self.address:
            self.notification.add_error("Address is required")
        
        if self.notification.has_errors:
            raise ValueError(self.notification.messages)
    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def add_rewards_points(self, points: int):
        self.rewards_points += points

