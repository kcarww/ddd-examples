from dataclasses import dataclass, field

@dataclass(kw_only=True)
class NotificationError:
    message: str
    context: str


@dataclass(kw_only=True)
class Notification:
    errors: list[NotificationError] = field(default_factory=list)

    def add_error(self, error: NotificationError):
        self.errors.append(error)

    @property
    def messages(self, context: str):
        return ','.join([error.message for error in self.errors if error.context == context])
    
    @property
    def has_errors(self):
        return bool(self.errors)
    
    def __str__(self) -> str:
        return self.messages