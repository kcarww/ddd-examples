from dataclasses import dataclass

from domain.costumer.entity.value_object.address import Address

@dataclass
class CreateCustomerInput:
    name: str
    address: Address

@dataclass
class CreateCustomerOutput:
    id: str
    name: str
    address: Address