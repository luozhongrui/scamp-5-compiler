import cv2
import numpy as np
from .lib.sim import load_image, Display
from .lib.reg import Register


# The Scamp5 class is a wrapper around the cv2.VideoCapture class
# It has a method init that initializes the camera
# It has a method get_image that returns the image from the camera
class Scamp5:
    def __init__(self):
        self.cap = None
        # analog register
        self.A = self.load_value(0)
        self.B = self.load_value(0)
        self.C = self.load_value(0)
        self.D = self.load_value(0)
        self.E = self.load_value(0)
        self.F = self.load_value(0)

        # digital register
        self.R0 = self.load_value(0)
        self.R1 = self.load_value(0)
        self.R2 = self.load_value(0)
        self.R3 = self.load_value(0)
        self.R4 = self.load_value(0)
        self.R5 = self.load_value(0)
        self.R6 = self.load_value(0)
        self.R7 = self.load_value(0)
        self.R8 = self.load_value(0)
        self.R9 = self.load_value(0)
        self.R10 = self.load_value(0)
        self.R11 = self.load_value(0)
        self.R12 = self.load_value(0)
        # self.FLAG = None
        self.display = None

    @staticmethod
    def load_value(value):
        return Register(np.full((256, 256), value, dtype=np.int8))


    def add_display(self, row, col, size):
        self.display = Display.initialize_window(row, col, size, size)


    def init(self, index=0):
        self.cap = cv2.VideoCapture(index)

    def get_image(self):
        frame = load_image(self.cap)
        return Register(frame)

    def mov(self, des, src):
        np.putmask(des.image, self.flag, src.image)

    def plot(self, reg, row, col, title="image"):
        self.display.show_image(reg.image, row, col, title)

    @staticmethod
    def printf(reg):
        print(reg.image)

    @property
    def flag(self):
        return Register.get_mask()

    def all(self):
        self.FLAG = np.full((256, 256), 1, dtype=np.int8)
        Register.set_mask(self.FLAG)

    @staticmethod
    def NOT(reg):
        return Register(np.logical_not(reg.image))

    @staticmethod
    def AND(reg1, reg2):
        return Register(np.logical_and(reg1.image, reg2.image))

    @staticmethod
    def OR(reg1, reg2):
        return Register(np.logical_or(reg1.image, reg2.image))

    @staticmethod
    def XOR(reg1, reg2):
        return Register(np.logical_xor(reg1.image, reg2.image))





