from notification import Notification
from queue import Queue


class DrawController():

    def __init__(self):
        self.__queue = Queue()
    
    def add_to_queue(self, notif: Notification):
        drawable = self._convert_notification(notif)
        self.__queue.put(drawable)

    def _convert_notification(self, notif: Notification):
        w, h = 32, 16
        pixels = [[0 for x in range(w)] for y in range(h)]
        return Drawable(pixels=pixels)
