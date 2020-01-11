import requests
from typing import Tuple

from model import Notification


class Repo():

    def __init__(self):
        self.__api_base = "https://naboo.space/api/v1/notifications"

    def query_notifications(self) -> Tuple[Notification, ...]:
        # TODO mock data
        return (Notification(),)