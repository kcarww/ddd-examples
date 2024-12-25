from abc import ABC, abstractmethod
from domain.entity.customer import Customer
from domain.repository.repository_interface import RepositoryInterface

class CustomerRepositoryInterface(ABC, RepositoryInterface[Customer]):
    ...