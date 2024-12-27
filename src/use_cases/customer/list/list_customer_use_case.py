from dataclasses import dataclass

from domain.costumer.repository.costumer_repository_interface import CustomerRepositoryInterface
from use_cases.customer.list.list_customer_dto import ListCustomerInput, ListCustomerOutput, TypeCustomer

@dataclass
class ListCustomerUseCase:
    customer_repository: CustomerRepositoryInterface

    def execute(self, input: ListCustomerInput) -> ListCustomerOutput:
        customers = self.customer_repository.find_all()
        return ListCustomerOutput(
            customers=[
                TypeCustomer(
                    id=customer.id,
                    name=customer.name,
                    address=customer.address
                ) for customer in customers
            ]
        )