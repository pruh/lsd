import time
from typing import Tuple

from model import Notification


class Controller:

    def __init__(self):
        super().__init__()

    def start_polling(self) -> None:
        """
        Start periodic polling for new data.
        """
        while True:
            data = self.__poll()
            self.__display(data)
            time.sleep(60)

    def __poll(self) -> Tuple[Notification, ...]:
        """
        Poll data from API.
        """
        # TODO mock data
        return (Notification(),)

    def __display(self, notifications: Tuple[Notification, ...]) -> None:
        """
        Non-blocking display data on LED dot matrix.
        """
        # TODO debug output
        notif_str = ", ".join(str(item) for item in notifications)
        print(f"({notif_str})")
