from dataclasses import dataclass, field
from uuid import UUID, uuid4

from domain._shared.notification.notification import Notification


@dataclass(kw_only=True)
class Entity:
    id: UUID = field(default_factory=uuid4)
    notification: Notification = field(default_factory=Notification)