import time
from typing import Tuple
import logging

from model import Notification
from repository import Repository


log = logging.getLogger(__name__)


class Controller:

    def __init__(self, repo: Repository):
        self.__repo = repo

    def start_polling(self) -> None:
        """
        Start periodic polling for new data.
        """
        while True:
            try:
                data = self.__poll()
                self.__display(data)
            except ApiError:
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
        # TODO debug output
        log.debug(", ".join(str(item) for item in notifications))
