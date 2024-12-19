from dataclasses import dataclass
from address import Address

@dataclass
class Customer:
    id: str
    name: str
    address: Address
    active: bool


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

