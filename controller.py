import time
from typing import Tuple
import logging

from notification import Notification
from repository import Repository
from draw_controller import DrawController


log = logging.getLogger(__name__)


class Controller:

    def __init__(self, repo: Repository, dc: DrawController):
        self.__repo = repo
        self.__dc = dc

    def start_polling(self) -> None:
        """
        Start periodic polling for new data.
        """
        while True:
            try:
                data = self.__poll()
                self.__display(data)
            except:
                logging.exception('Error while querying for notifications')

            time.sleep(60)

    def __poll(self) -> Tuple[Notification, ...]:
        """
        Poll data from API.
        """
        return self.__repo.get_notifications()

    def __display(self, notifications: Tuple[Notification, ...]) -> None:
        """
        Non-blocking display data on LED dot matrix.
        """
        [self.__dc.add_to_queue(notif) for notif in notifications]
