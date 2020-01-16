import logging
from notification import Notification
from queue import Queue
from threading import Thread
from drawable import Drawable
from frames_generator import FrameGenerator, ScrollingFrameGenerator
from matrix import Matrix
import time


log = logging.getLogger(__name__)


class DrawController():

    def __init__(self, matrix: Matrix, refresh_rate: float):
        self.__queue = Queue()
        self.__matrix = matrix
        frame_generator = ScrollingFrameGenerator(self.__matrix.width, self.__matrix.height)
        self.__thread = Thread(
            name='draw_thread',
            target=self.__draw,
            args=(self.__queue, frame_generator.get_frames, refresh_rate,),
            daemon=True)

        self.__thread.start()
    
    def add_to_queue(self, notif: Notification) -> None:
        drawable = self._convert_notification(notif)
        self.__queue.put(drawable)

    def _convert_notification(self, notif: Notification) -> Drawable:
        w, h = self.__matrix.width, self.__matrix.height
        # TODO convert text to pixels
        pixels = [[0 for y in range(h)] for x in range(w)]
        return Drawable(pixels=pixels)

    def __draw(self, queue: Queue, frame_gen, refresh_rate: float) -> None:
        while True:
            drawable = queue.get()
            for frame in frame_gen(drawable):
                self.__matrix.draw(frame)
                time.sleep(refresh_rate)
            queue.task_done()
