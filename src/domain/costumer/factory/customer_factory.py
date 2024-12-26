from dataclasses import dataclass
from uuid import uuid4

from domain.costumer.entity.customer import Customer
from domain.costumer.entity.value_object.address import Address

@dataclass
class CustomerFactory:


    def create(name: str) -> Customer:
        return Customer(
            id=uuid4(),
            name=name
        )
    
    def create_with_address(name: str, address: Address) -> Customer:
        customer = Customer(
            id=uuid4(),
            name=name,
            address=address
        )

        return customer