import logging
from notification import Notification
from queue import Queue
from threading import Thread
from drawable import Drawable
from frames_generator import FrameGenerator, ScrollingFrameGenerator
from matrix import Matrix
import time
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from typing import Callable, Iterable


log = logging.getLogger(__name__)


class DrawController():

    def __init__(self, matrix: Matrix, refresh_rate: float):
        self.__queue = Queue()
        self.__matrix = matrix
        frame_generator = ScrollingFrameGenerator(self.__matrix.width, self.__matrix.height)
        self.__font_path = 'fonts/arial.ttf'
        self.__font_size = 16
        self.__thread = Thread(
            name='draw_thread',
            target=self.__draw,
            args=(self.__queue, frame_generator.get_frames, refresh_rate,),
            daemon=True)

        self.__thread.start()
    
    def add_to_queue(self, notif: Notification) -> None:
        log.debug(f"queued: {notif}")
        drawable = self._convert_notification(notif)
        self.__queue.put(drawable)

    def _convert_notification(self, notif: Notification) -> Drawable:
        text = notif.title
        if notif.message:
            text += f". {notif.message}"
        color = 2

        font = ImageFont.truetype(self.__font_path, self.__font_size)
        w = font.getsize(text)[0]
        image = Image.new('L', (w, self.__matrix.height), 1)
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), text, font=font)
        arr = np.asarray(image)
        arr = np.where(arr, 0, color)

        return Drawable(pixels=arr)

    def __draw(self, queue: Queue, frame_gen: Callable[[Drawable], Iterable[np.ndarray]], refresh_rate: float) -> None:
        while True:
            self.__matrix.reset()
            drawable = queue.get()
            for frame in frame_gen(drawable):
                self.__matrix.draw(frame)
                time.sleep(refresh_rate)
            queue.task_done()
