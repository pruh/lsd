from drawable import Drawable
from typing import Iterator, List


class FrameGenerator():

    def __init__(self, w: int, h: int):
        self._matrix_width = w
        self._matrix_height = h
    
    def get_frames(self, drawable: Drawable) -> Iterator[List[List[int]]]:
        pass

class ScrollingFrameGenerator(FrameGenerator):

    def __init__(self, w, h):
        super().__init__(w, h)
    
    def get_frames(self, drawable: Drawable) -> Iterator[List[List[int]]]:
        current_frame = [[0 for x in range(self._matrix_width)] for y in range(self._matrix_height)]
        for y in range(len(drawable.pixels)):
            current_frame = self._shift_frame(current_frame)
            new_last_column = self._get_column(drawable, y)
            current_frame = self._append_last_column(current_frame, new_last_column)
            yield current_frame

    def _shift_frame(self, frame: List[List[int]]) -> List[List[int]]:
        for x in range(self._matrix_width - 1):
            for y in range(self._matrix_height):
                frame[y][x] = frame[y][x + 1]

        for y in range(self._matrix_height):
            frame[y][self._matrix_width - 1] = 0

        return frame

    def _get_column(self, drawable: Drawable, col_id: int) -> List[int]:
        col = [0 for y in range(self._matrix_height)]
        for y in range(self._matrix_height):
            col[y] = drawable.pixels[col_id][y]

        return col

    def _append_last_column(self, frame: List[List[int]], new_last_column: List[int]) -> List[List[int]]:
        for y in range(self._matrix_height):
            frame[y][self._matrix_width - 1] = new_last_column[y]

        return frame