from dataclasses import dataclass
from address import Address

@dataclass(kw_only=True)
class Customer:
    id: str
    name: str
    address: Address
    active: bool
    rewards_points: int = 0


    def __post_init__(self):
        self.validate()

    def validate(self):
        if not self.id:
            raise ValueError("ID is required")
        if not self.name:
            raise ValueError("Name is required")
        if not self.address:
            raise ValueError("Address is required")
        
    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def add_rewards_points(self, points: int):
        self.rewards_points += points

