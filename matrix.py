from typing import List

class Matrix():

    def __init__(self, width: int, hieght: int):
        self.width = width
        self.height = hieght

    def draw(self, frame: List[List[int]]):
        print("drawing frame")