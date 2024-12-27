from dataclasses import dataclass

from domain.costumer.repository.costumer_repository_interface import CustomerRepositoryInterface
from use_cases.customer.create.create_customer_dto import CreateCustomerInput, CreateCustomerOutput

@dataclass
class CreateCustomerUseCase:
    customer_repository: CustomerRepositoryInterface

    def execute(self, input: CreateCustomerInput) -> CreateCustomerOutput:
        customer = self.customer_repository.create(input.name, input.address)
        return CreateCustomerOutput(
            id=customer.id,
            name=customer.name,
            address=customer.address
        )