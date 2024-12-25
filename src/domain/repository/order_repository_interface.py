from abc import ABC, abstractmethod
from domain.entity.order import Order
from domain.repository.repository_interface import RepositoryInterface

class OrderRepositoryInterface(ABC, RepositoryInterface[Order]):
    ...