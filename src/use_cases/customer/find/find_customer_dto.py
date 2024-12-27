from dataclasses import dataclass

from domain.costumer.entity.value_object.address import Address

@dataclass
class InputFindCustomer:
    id: str

@dataclass
class OutputFindCustomer:
    id: str
    name: str
    address: Address