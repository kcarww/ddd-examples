from dataclasses import dataclass

from domain.costumer.repository.costumer_repository_interface import CustomerRepositoryInterface
from use_cases.customer.update.update_customer_dto import UpdateCustomerInput, UpdateCustomerOutput

@dataclass
class UpdateCustomerUseCase:
    customer_repository: CustomerRepositoryInterface

    def execute(self, input: UpdateCustomerInput) -> UpdateCustomerOutput:
        customer = self.customer_repository.find(input.id)
        if not customer:
            raise Exception('Customer not found')
        
        customer.name = input.name
        customer.address = input.address
        return UpdateCustomerOutput(
            id=customer.id,
            name=customer.name,
            address=customer.address
        )