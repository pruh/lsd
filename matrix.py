import RPi.GPIO as GPIO
from typing import List, Tuple
import numpy as np


class Matrix():
    """
    Class represents LED dot matrix. Currently only support 16x32 matrices.

    The following pin connection is expected:
    OE     : 12
    CLK    : 11
    LAT    : 7
    A      : 15
    B      : 16
    C      : 18
    RED1   : 23
    GREEN1 : 13
    BLUE1  : 26
    RED2   : 24
    GREEN2 : 21
    BLUE2  : 19
    """

    def __init__(self, width: int, hieght: int):
        self.width = width
        self.height = hieght

        GPIO.setmode(GPIO.BCM)
        self._setup_pins()

        self.reset()

    def _setup_pins(self):
        self._oe_pin = Pin(pin_number=12)
        self._clk_pin = Pin(pin_number=11)
        self._lat_pin = Pin(pin_number=7)
        self._a_pin = Pin(pin_number=15)
        self._b_pin = Pin(pin_number=16)
        self._c_pin = Pin(pin_number=18)
        self._red1_pin = Pin(pin_number=23)
        self._green1_pin = Pin(pin_number=13)
        self._blue1_pin = Pin(pin_number=26)
        self._red2_pin = Pin(pin_number=24)
        self._green2_pin = Pin(pin_number=21)
        self._blue2_pin = Pin(pin_number=19)

    def draw(self, frame: np.ndarray) -> None:
        if frame.shape[0] != self.height:
            raise MatrixError(f"frame height should be equal to {self.height}")
        if frame.shape[1] != self.width:
            raise MatrixError(f"frame width should be equal to {self.width}")

        half_screen_size = int(self.height / 2)
        for y in range(half_screen_size):
            # set row
            self._set_row(y)

            # enable LEDs
            self._oe_pin.set_low()

            for x in range(self.width):
                self._set_top_row_color(frame[y, x])
                self._set_bottom_row_color(frame[y + half_screen_size, x])

                # move to next column
                self._clk_pin.set_high()
                self._clk_pin.set_low()

            # disable LEDs
            self._oe_pin.set_high()

            # load registers to LEDs
            self._lat_pin.set_high()
            self._lat_pin.set_low()

    def _set_row(self, row: int) -> None:
        a_bit, b_bit, c_bit = self._bits_from_int(row)
        self._a_pin.set_bit(a_bit)
        self._b_pin.set_bit(b_bit)
        self._c_pin.set_bit(c_bit)

    def _set_top_row_color(self, color: int) -> None:
        red, green, blue = self._bits_from_int(color)
        self._red1_pin.set_bit(red)
        self._green1_pin.set_bit(green)
        self._blue1_pin.set_bit(blue)

    def _set_bottom_row_color(self, color: int) -> None:
        red, green, blue = self._bits_from_int(color)
        self._red2_pin.set_bit(red)
        self._green2_pin.set_bit(green)
        self._blue2_pin.set_bit(blue)

    def _bits_from_int(self, x: int) -> Tuple[int, int, int]:
        first = 1 if x & 1 != 0 else 0
        second = 1 if x & 2 != 0 else 0
        third = 1 if x & 4 != 0 else 0
        return (first, second, third)

    def reset(self):
        self._oe_pin.set_low()
        self._clk_pin.set_low()
        self._lat_pin.set_low()


class Pin():

    def __init__(self, pin_number: int):
        self.__pin_number = pin_number
        GPIO.setup(pin_number, GPIO.OUT)

    def set_low(self) -> None:
        self.set_bit(0)

    def set_high(self) -> None:
        self.set_bit(1)

    def set_bit(self, bit: int) -> None:
        GPIO.output(self.__pin_number, bit)
        pass


class MatrixError(BaseException):
    pass
