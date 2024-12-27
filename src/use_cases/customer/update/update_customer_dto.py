from dataclasses import dataclass

from domain.costumer.entity.value_object.address import Address

@dataclass
class UpdateCustomerInput:
    id: str
    name: str
    address: Address


@dataclass
class UpdateCustomerOutput:
    id: str
    name: str
    address: Address