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
        self._A = self.load_value(0)
        self._B = self.load_value(0)
        self._C = self.load_value(0)
        self._D = self.load_value(0)
        self._E = self.load_value(0)
        self._F = self.load_value(0)

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

    @property
    def A(self):
        return self._A

    @A.setter
    def A(self, value):
        self._A = value

    @property
    def B(self):
        return self._B

    @B.setter
    def B(self, value):
        self._B = value

    @property
    def C(self):
        return self._C

    @C.setter
    def C(self, value):
        self._C = value

    @property
    def D(self):
        return self._D

    @D.setter
    def D(self, value):
        self._D = value

    @property
    def E(self):
        return self._E

    @E.setter
    def E(self, value):
        self._E = value

    @property
    def F(self):
        return self._F

    @F.setter
    def F(self, value):
        self._F = value

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

    def abs(self, reg):
        return Register(np.abs(reg.image))

    def plot(self, reg, row, col, title="image"):
        self.display.show_image(reg.image, row, col, title)

    @staticmethod
    def printf(reg):
        print(reg.image)

    @property
    def flag(self):
        return Register.get_mask()

    @staticmethod
    def all():
        flg = np.full((256, 256), 1, dtype=np.int8)
        Register.set_mask(flg)

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

    def where(self, condition):
        flg = condition
        Register.set_mask(flg)
        return True





