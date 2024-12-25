from dataclasses import dataclass
from typing import List, Optional
from sqlalchemy.orm import Session
from domain.entity.address import Address
from domain.entity.customer import Customer
from domain.entity.product import Product
from domain.repository.costumer_repository_interface import CustomerRepositoryInterface
from infrastructure.db.alchemy_orm.model import customer_model
from infrastructure.db.alchemy_orm.model.customer_model import CustomerModel

@dataclass
class CustomerRepository(CustomerRepositoryInterface):
    session: Session

    def create(self, customer: Customer) -> None:
        customer_model = CustomerModel(
            id=customer.id,
            name=customer.name,
            active=customer.active,
            rewards_points=customer.rewards_points,
            street=customer.address.street,
            city=customer.address.city,
            state=customer.address.state,
            zip_code=customer.address.zip_code,
            country=customer.address.country

        )
        self.session.add(customer_model)
        self.session.commit()

    def update(self, customer: Customer) -> None:
        customer_model = self.session.query(CustomerModel).filter_by(id=customer.id).first()
        if customer_model:
            customer_model.name = customer.name
            customer_model.active = customer.active
            customer_model.rewards_points = customer.rewards_points
            customer_model.street = customer.address.street
            customer_model.city = customer.address.city
            customer_model.state = customer.address.state
            customer_model.zip_code = customer.address.zip_code
            customer_model.country = customer.address.country
            self.session.commit()
        else:
            raise ValueError(f"Product with id {customer.id} not found")

    def find_by_id(self, id: str) -> Optional[Customer]:
        customer_model = self.session.query(CustomerModel).filter_by(id=id).first()
        if customer_model:
            return Customer(
                id=customer_model.id,
                name=customer_model.name,
                active=customer_model.active,
                rewards_points=customer_model.rewards_points,
                address=Address(
                    street=customer_model.street,
                    city=customer_model.city,
                    state=customer_model.state,
                    zip_code=customer_model.zip_code,
                    country=customer_model.country
                )
            )
        return None

    def find_all(self) -> List[Customer]:
        customers_model = self.session.query(CustomerModel).all()
        return [
            Customer(
                id=customer_model.id,
                name=customer_model.name,
                active=customer_model.active,
                rewards_points=customer_model.rewards_points,
                address=Address(
                    street=customer_model.street,
                    city=customer_model.city,
                    state=customer_model.state,
                    zip_code=customer_model.zip_code,
                    country=customer_model.country
                )
            ) for customer_model in customers_model
        ]
