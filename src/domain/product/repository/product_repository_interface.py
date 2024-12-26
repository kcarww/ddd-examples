from abc import ABC, abstractmethod
from domain.product.entity.product import Product
from domain._shared.repository.repository_interface import RepositoryInterface

class ProductRepositoryInterface(ABC, RepositoryInterface[Product]):
    ...