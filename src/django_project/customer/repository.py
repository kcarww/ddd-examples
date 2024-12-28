from uuid import UUID

from domain.costumer.entity.customer import Customer
from domain.costumer.entity.value_object.address import Address
from domain.costumer.repository.costumer_repository_interface import CustomerRepositoryInterface
from django_project.customer.models import Customer as CustomerModel
from dataclasses import dataclass


@dataclass
class DjangoORMCustomerRepository(CustomerRepositoryInterface):
    customer_model: CustomerModel = None

    def __post_init__(self):
        self.customer_model = CustomerModel()

    def create(self, customer: Customer) -> None:
        customer_orm = CustomerModelMapper.to_model(customer)
        customer_orm.save()

    def find(self, id: str) -> Customer:
        pass

    def find_all(self) -> list[Customer]:
        pass

    def update(self, customer: Customer) -> None:
        pass


class CustomerModelMapper:
    @staticmethod
    def to_entity(customer_model: CustomerModel) -> Customer:
        return Customer(
            id=UUID(customer_model.id),
            name=customer_model.name,
            address=Address(
                street=customer_model.street,
                city=customer_model.city,
                state=customer_model.state,
                zip_code=customer_model.zip_code,
                country=customer_model.country,
            ),
            active=customer_model.active,
            rewards_points=customer_model.rewards_points
        )

    @staticmethod
    def to_model(customer: Customer) -> CustomerModel:
        return CustomerModel(
            id=customer.id,
            name=customer.name,
            street=customer.address.street,
            city=customer.address.city,
            state=customer.address.state,
            zip_code=customer.address.zip_code,
            country=customer.address.country,
            active=customer.active,
            rewards_points=customer.rewards_points
        )