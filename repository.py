import json
import requests
from typing import Tuple, Optional, Dict
import urllib.parse
from requests.auth import HTTPBasicAuth
from notification import Notification

import uuid
import dateutil.parser


class Repository():

    def __init__(self, base_url: str, username: Optional[str], password: Optional[str]):
        self.__base_url = base_url
        self.__auth = None
        if username and password:
            self.__auth = HTTPBasicAuth(username=username, password=password)

    def get_notifications(self) -> Tuple[Notification, ...]:
        url = urllib.parse.urljoin(self.__base_url, 'notifications')
        response = requests.get(url, auth=self.__auth)
        if response.status_code != 200:
            raise ApiError(f"failed to query for notifications {response}")

        payload = json.loads(response.content.decode('utf-8'))
        return (self.__to_notification(item) for item in payload)

    def __to_notification(self, notif_dict: Dict[str, str]) -> Notification:
        return Notification(
            id=uuid.UUID(notif_dict.get("_id")),
            title=notif_dict.get("title"),
            message=notif_dict.get("message"),
            start_time=dateutil.parser.parse(notif_dict.get("start_time")),
            end_time=dateutil.parser.parse(notif_dict.get("end_time")),
            source=notif_dict.get("source"),
        )


class ApiError(BaseException):
    pass
