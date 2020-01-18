import time
from typing import Tuple
import logging

from notification import Notification
from repository import Repository
from draw_controller import DrawController
from queue import Queue


log = logging.getLogger(__name__)


class Controller:

    def __init__(self, repo: Repository, queue: Queue):
        self.__repo = repo
        self.__queue = queue

    def start_polling(self) -> None:
        """
        Start periodic polling for new data.
        """
        while True:
            self.__queue.join()
            notifications = None
            try:
                notifications = self.__repo.get_notifications()
                log.debug(f"queried: {', '.join([str(n) for n in notifications])}")
            except:
                logging.exception('Error while querying for notifications')

            if notifications and len(notifications) > 0:
                self.__display(notifications)
            else:
                time.sleep(60)

    def __display(self, notifications: Tuple[Notification, ...]) -> None:
        """
        Non-blocking display data on LED dot matrix.
        """
        [self.__queue.put(notif) for notif in notifications]
