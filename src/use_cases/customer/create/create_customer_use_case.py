from dataclasses import dataclass

from domain.costumer.entity.customer import Customer
from domain.costumer.entity.value_object.address import Address
from domain.costumer.repository.costumer_repository_interface import CustomerRepositoryInterface
from use_cases.customer.create.create_customer_dto import CreateCustomerInput, CreateCustomerOutput

@dataclass
class CreateCustomerUseCase:
    customer_repository: CustomerRepositoryInterface

    def execute(self, input: CreateCustomerInput) -> CreateCustomerOutput:
        try:
            customer = Customer(
                name=input.name,
                address=Address(
                    street=input.street,
                    city=input.city,
                    state=input.state,
                    zip_code=input.zip_code,
                    country=input.country
                )
            )
        except Exception as e:
            raise e
        self.customer_repository.create(customer)
        return CreateCustomerOutput(
            id=customer.id,
            name=customer.name,
            active=customer.active,
            rewards_points=customer.rewards_points,
            address=Address(
                street=customer.address.street,
                city=customer.address.city,
                state=customer.address.state,
                zip_code=customer.address.zip_code,
                country=customer.address.country
            ),
        )