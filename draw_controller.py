import logging
from notification import Notification
from queue import Queue
from threading import Thread
from drawable import Drawable
from frames_generator import FrameGenerator, ScrollingFrameGenerator


log = logging.getLogger(__name__)


class DrawController():

    def __init__(self, matrix_width: int, matrix_hieght: int):
        self.__queue = Queue()
        self.__matrix_width = matrix_width
        self.__matrix_height = matrix_hieght
        frame_generator = ScrollingFrameGenerator(matrix_width, matrix_hieght)
        self.__thread = Thread(name='draw_thread', target=self.__draw, args=(self.__queue, frame_generator.get_frames,), daemon=True)

        self.__thread.start()
    
    def add_to_queue(self, notif: Notification) -> None:
        drawable = self._convert_notification(notif)
        self.__queue.put(drawable)

    def _convert_notification(self, notif: Notification) -> Drawable:
        w, h = self.__matrix_width, self.__matrix_height
        pixels = [[0 for y in range(h)] for x in range(w)]
        return Drawable(pixels=pixels)

    def __draw(self, queue: Queue, frame_gen) -> None:
        while True:
            drawable = queue.get()
            log.debug(f"drawing {drawable}")
            print(type(frame_gen(drawable)))
            for frame in frame_gen(drawable):
                pass
            queue.task_done()
