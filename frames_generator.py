from drawable import Drawable
from typing import Iterator
import numpy as np


class FrameGenerator():

    def __init__(self, w: int, h: int):
        self._matrix_width = w
        self._matrix_height = h
    
    def get_frames(self, drawable: Drawable) -> Iterator[np.ndarray]:
        pass

class ScrollingFrameGenerator(FrameGenerator):

    def __init__(self, w: int, h: int):
        super().__init__(w, h)
    
    def get_frames(self, drawable: Drawable) -> Iterator[np.ndarray]:
        current_frame = np.zeros(shape=(self._matrix_height, self._matrix_width), dtype=int)
        for y in range(drawable.pixels.shape[1]):
            new_last_column = self._get_column(drawable, y)
            current_frame = self._shift_frame(current_frame, new_last_column)
            yield current_frame

        # make the area after the text blank
        empty_column = np.zeros(shape=(self._matrix_height, 1), dtype=int)
        for y in range(self._matrix_width):
            current_frame = self._shift_frame(current_frame, empty_column)
            yield current_frame

    def _shift_frame(self, frame: np.ndarray, new_last_column: np.ndarray) -> np.ndarray:
        # delete first column
        frame = np.delete(frame, 0, axis=1)

        return np.concatenate((frame, new_last_column), axis=1)

    def _get_column(self, drawable: Drawable, col_id: int) -> np.ndarray:
        col = np.ndarray(self._matrix_height)
        col = drawable.pixels[:, col_id]
        return np.reshape(col, (-1, 1))
