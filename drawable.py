import numpy as np


class Drawable():
    """
    Model that holds object to draw.
    Object is represented by two-dimensional matrix,
    where each item is a color of current pixel.
    Pixel color is an int number from 0 to 7 (inclusive),
    where each bit of the int number is RGB color.
    """
    def __init__(self, pixels: np.ndarray):
        self.pixels = pixels
