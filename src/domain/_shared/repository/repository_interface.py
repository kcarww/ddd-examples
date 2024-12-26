from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")

class RepositoryInterface(ABC, Generic[T]):
    @abstractmethod
    def create(self, entity: T) -> None:
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        pass

    @abstractmethod
    def find(self, id: int) -> T:
        pass

    @abstractmethod
    def find_all(self) -> list[T]:
        pass