from dataclasses import dataclass
from email.headerregistry import Address

from domain.costumer.entity.customer import Customer

@dataclass
class ListCustomerInput:
    pass

@dataclass
class TypeCustomer:
    id: int
    name: str
    address: Address

@dataclass
class ListCustomerOutput:
    customers: list[TypeCustomer]