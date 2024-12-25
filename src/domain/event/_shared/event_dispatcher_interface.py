from dataclasses import dataclass
from abc import ABC, abstractmethod

from domain.event._shared.event_handler_interface import EventHandler
from domain.event._shared.event_interface import EventInterface

@dataclass
class EventDispatcherInterface(ABC):
    
    @abstractmethod
    def notify(self, event: EventInterface) -> None:
        pass

    @abstractmethod
    def register(self, event_name: str, event_handler: EventHandler) -> None:
        pass

    @abstractmethod
    def unregister(self, event_name: str, evnet_handler: EventHandler) -> None:
        pass

    @abstractmethod
    def unregister_all(self) -> None:
        pass