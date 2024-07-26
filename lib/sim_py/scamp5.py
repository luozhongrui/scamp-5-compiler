import cv2
import numpy as np
from lib.sim import load_image, Display
from lib.reg import Register


# The Scamp5 class is a wrapper around the cv2.VideoCapture class
# It has a method init that initializes the camera
# It has a method get_image that returns the image from the camera

class Scamp5:
    def __init__(self):
        self.cap = None
        # analog register
        self.A = None
        self.B = None
        self.C = None
        self.D = None
        self.E = None
        self.F = None

        # digital register
        self.R0 = None
        self.R1 = None
        self.R2 = None
        self.R3 = None
        self.R4 = None
        self.R5 = None
        self.R6 = None
        self.R7 = None
        self.R8 = None
        self.R9 = None
        self.R10 = None
        self.R11 = None
        self.R12 = None
        self.FLAG = None

    @staticmethod
    def load_value(value):
        return Register(np.full((256, 256), value, dtype=np.int8))

    @staticmethod
    def add_display(title):
        return Display(title)

    def init(self, index=0):
        self.cap = cv2.VideoCapture(index)

    def get_image(self):
        frame = load_image(self.cap)
        return Register(frame)

    @staticmethod
    def plot(reg, handle):
        image = reg.image
        handle.show_image(image)

    @staticmethod
    def printf(reg):
        print(reg.image)

    def where(self, condition):
        self.FLAG = np.where(condition, 1, 0)
        Register.set_mask(self.FLAG)
    
    def all(self):
        self.FLAG = np.full((256, 256), 1, dtype=np.int8)
        Register.set_mask(self.FLAG)


if __name__ == '__main__':
    scamp5 = Scamp5()
    scamp5.init(1)
    dis1 = scamp5.add_display('north')
    dis2 = scamp5.add_display("original")

    while True:
        scamp5.A = scamp5.get_image()
        scamp5.B = scamp5.load_value(-100)

        scamp5.plot(scamp5.A, dis1)
        scamp5.plot(scamp5.B, dis2)




