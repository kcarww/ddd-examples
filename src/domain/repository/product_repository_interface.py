from abc import ABC, abstractmethod
from domain.entity.product import Product
from domain.repository.repository_interface import RepositoryInterface

class ProductRepositoryInterface(ABC, RepositoryInterface[Product]):
    ...