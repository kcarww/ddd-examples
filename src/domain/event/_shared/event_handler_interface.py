from abc import ABC, abstractmethod
from dataclasses import dataclass
from domain.event._shared.event_interface import EventInterface
from typing import Generic, TypeVar

T = TypeVar('T', bound=EventInterface)

@dataclass
class EventHandler(ABC, Generic[T]):

    @abstractmethod
    def handler(event: T) -> None:
        pass