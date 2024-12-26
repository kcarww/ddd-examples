from dataclasses import dataclass
from domain.event._shared.event_handler_interface import EventHandler
from domain.product.event.product_created_event import ProductCreatedEvent

@dataclass
class SendEmailWhenProductIsCreatedHandler(EventHandler[ProductCreatedEvent]):
    def handler(self, event: ProductCreatedEvent):
        print('Sending email to....')