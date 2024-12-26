from dataclasses import dataclass, field

from domain.event._shared.event_dispatcher_interface import EventDispatcherInterface
from domain.event._shared.event_handler_interface import EventHandler
from domain.event._shared.event_interface import EventInterface

@dataclass
class EventDispatcher(EventDispatcherInterface):
    _event_handlers: dict[str, list[EventInterface]] = field(default_factory=dict)

    def get_event_handlers(self) -> dict[str, list[EventInterface]]:
        return self._event_handlers
    
    def notify(self, event: EventInterface) -> None:
        event_name = event.__class__.__name__
        if event_name in self._event_handlers:
            for handler in self._event_handlers[event_name]:
                handler.handle(event)

    def register(self, event_name: str, event_handler: EventHandler) -> None:
        if not event_name in self._event_handlers:
            self._event_handlers[event_name] = []
        self._event_handlers[event_name].append(event_handler)

    def unregister(self, event_name: str, event_handler: EventHandler) -> None:
        if event_name in self._event_handlers:
            self._event_handlers[event_name].remove(event_handler)

    def unregister_all(self) -> None:
        self._event_handlers = {}