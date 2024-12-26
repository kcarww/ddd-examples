from abc import ABC, abstractmethod
from domain.costumer.entity.customer import Customer
from domain._shared.repository.repository_interface import RepositoryInterface

class CustomerRepositoryInterface(ABC, RepositoryInterface[Customer]):
    ...