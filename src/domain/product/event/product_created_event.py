from dataclasses import dataclass, field
from datetime import datetime
from domain.event._shared.event_interface import EventInterface

@dataclass(kw_only=True)
class ProductCreatedEvent(EventInterface):
    data_time_occurred: datetime = field(default_factory=datetime.now)
    event_data: any
    
