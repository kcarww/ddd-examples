from dataclasses import dataclass

from domain.costumer.entity.value_object.address import Address

@dataclass(kw_only=True)
class CreateCustomerInput:
    name: str
    street: str
    city: str
    state: str
    zip_code: str
    country: str
    active: bool = True
    rewards_points: int = 0

@dataclass
class CreateCustomerOutput:
    id: str
    name: str
    address: Address
    active: bool
    rewards_points: int