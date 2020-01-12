import uuid
import datetime
from typing import Optional


class Notification:
    """
    Data class to describe data received from API.
    """

    def __init__(self, id: uuid, title: str, message: Optional[str],
            start_time: datetime, end_time: datetime, source: Optional[str]):
        self.id = id
        self.title = title
        self.message = message
        self.start_time = start_time
        self.end_time = end_time
        self.source = source

    def __str__(self) -> str:
        props = ', '.join(f"{name}={value}" for name, value in vars(self).items())
        return f"{type(self).__name__}({props})"