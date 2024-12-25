from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime as Date

@dataclass
class EventInterface(ABC):
    data_time_occurred: Date
    event_data: any