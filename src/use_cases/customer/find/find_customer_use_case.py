from dataclasses import dataclass

from domain.costumer.repository.costumer_repository_interface import CustomerRepositoryInterface
from use_cases.customer.find.find_customer_dto import InputFindCustomer, OutputFindCustomer

@dataclass
class FindCustomerUseCase:
    customer_repository: CustomerRepositoryInterface

    def execute(self, input: InputFindCustomer) -> OutputFindCustomer:
        customer = self.customer_repository.find(input.id)
        return OutputFindCustomer(
            id=customer.id,
            name=customer.name,
            address=customer.address
        )
    