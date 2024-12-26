from abc import ABC, abstractmethod
from domain.checkout.entity.order import Order
from domain._shared.repository.repository_interface import RepositoryInterface

class OrderRepositoryInterface(ABC, RepositoryInterface[Order]):
    ...