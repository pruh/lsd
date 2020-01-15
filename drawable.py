from typing import List


class Drawable():
    """
    Model that holds object to draw.
    Object is represented by two-dimensional matrix,
    where each item contains color of current pixel.
    Pixel color is an int number from 0 to 7 (inclusive),
    where each bit of the int is color in RGB format.
    """
    def __init__(self, pixels: List[List[int]]):
        self.pixels = pixels
