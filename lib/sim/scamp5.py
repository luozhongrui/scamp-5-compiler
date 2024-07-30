import ctypes
from ctypes import c_uint8, c_int, c_char_p, c_void_p
from .utils import AREG, Direction, Reg
"""
1 python sim version
2 compile to c code using flex and bsion
"""


class Scamp5:
    vs_handle = ctypes.c_uint32
    __scamp5lib = ctypes.CDLL(r'D:\dissertation\sourceCode\scamp5_project\scamp5lib.dll')

    def __init__(self) -> None:
        self.reg = Reg()
        self.__scamp5lib.my_vs_gui_add_display.argtypes = [c_char_p, c_uint8, c_uint8, c_int, c_char_p]
        self.__scamp5lib.my_vs_gui_add_display.restype = self.vs_handle

        self.__scamp5lib.my_scamp5_output_image.argtypes = [ctypes.POINTER(AREG), self.vs_handle]
        self.__scamp5lib.my_scamp5_output_image.restype = None

        self.__scamp5lib.vsInit.argtypes = []
        self.__scamp5lib.vsInit.restype = None

        self.__scamp5lib.vsGuiSetInfo.argtypes = []
        self.__scamp5lib.vsGuiSetInfo.restype = None

        self.__scamp5lib.vsFrameLoopControl.argtypes = []
        self.__scamp5lib.vsFrameLoopControl.restype = None

        self.__scamp5lib.getImage.argtypes = [ctypes.POINTER(AREG)]
        self.__scamp5lib.getImage.restype = None

        self.__scamp5lib.load_value.argtypes = [ctypes.POINTER(AREG), ctypes.c_int8]
        self.__scamp5lib.load_value.restype = None

        self.__scamp5lib.c_add.argtypes = [ctypes.POINTER(AREG), ctypes.POINTER(AREG), ctypes.POINTER(AREG)]
        self.__scamp5lib.c_add.restype = None

        self.__scamp5lib.c_sub.argtypes = [ctypes.POINTER(AREG), ctypes.POINTER(AREG), ctypes.POINTER(AREG)]
        self.__scamp5lib.c_sub.restype = None

        self.__scamp5lib.moveDir.argtypes = [ctypes.POINTER(AREG), ctypes.POINTER(AREG), ctypes.c_int]
        self.__scamp5lib.moveDir.restype = None

        self.__scamp5lib.move2Dir.argtypes = [ctypes.POINTER(AREG), ctypes.POINTER(AREG), ctypes.c_int, ctypes.c_int]
        self.__scamp5lib.move2Dir.restype = None

        self.__scamp5lib.analog_where.argtypes = [ctypes.POINTER(AREG)]
        self.__scamp5lib.analog_where.restype = None

        self.__scamp5lib.c_all.argtypes = []
        self.__scamp5lib.c_all.restype = None

        self.__scamp5lib.digit_where.argtypes = [ctypes.POINTER(AREG)]
        self.__scamp5lib.digit_where.restype = None

        self.__scamp5lib.medianFilter.argtypes = [ctypes.POINTER(AREG)]
        self.__scamp5lib.medianFilter.restype = None

        self.__scamp5lib.sobel_filter.argtypes = [ctypes.POINTER(AREG)]
        self.__scamp5lib.sobel_filter.restype = None

        self.__scamp5lib.laplacian_filter.argtypes = [ctypes.POINTER(AREG)]
        self.__scamp5lib.laplacian_filter.restype = None


    """
        init option
    """
    def vs_init(self):
        self.__scamp5lib.vsInit()
    
    def vs_gui_set_info(self):
        self.__scamp5lib.vsGuiSetInfo()
    
    def add_display(self, title, row=0, col=0, size=1):
        display = self.__scamp5lib.my_vs_gui_add_display(title, row, col, size, None)
        return display
    
    def plot(self, reg, display):
        self.__scamp5lib.my_scamp5_output_image(reg, display)

    def vs_frame_loop_control(self):
        self.__scamp5lib.vsFrameLoopControl()
    
    def load_value(self, reg, val):
        self.__scamp5lib.load_value(reg, val)

    def get_image(self, reg):
        self.__scamp5lib.getImage(reg)

    def end(self):
        self.__scamp5lib.c_all()

    """ 
     add sub multiply
    """

    def add(self, reg1, reg2, reg3):
        self.__scamp5lib.c_add(reg1, reg2, reg3)

    def sub(self, reg1, reg2, reg3):
        self.__scamp5lib.c_sub(reg1, reg2, reg3)

    def multiply(self, reg1, reg2, num):
        for _ in range(num):
            self.__scamp5lib.c_add(reg1, reg2, reg2)

    """
     direction operation
    """
    def north(self, src):
        self.__scamp5lib.moveDir(self.reg.A, src, Direction.NORTH)
        return self.reg.A

    def south(self, src):
        self.__scamp5lib.moveDir(self.reg.A, src, Direction.SOUTH)
        return self.reg.A

    def east(self, src):
        self.__scamp5lib.moveDir(self.reg.A, src, Direction.EAST)
        return self.reg.A

    def west(self, src):
        self.__scamp5lib.moveDir(self.reg.A, src, Direction.WEST)
        return self.reg.A

    def north_east(self, dest, src):
        self.__scamp5lib.move2Dir(dest, src, Direction.NORTH, Direction.EAST)

    def north_west(self, dest, src):
        self.__scamp5lib.move2Dir(dest, src, Direction.NORTH, Direction.WEST)

    def south_east(self, dest, src):
        self.__scamp5lib.move2Dir(dest, src, Direction.SOUTH, Direction.EAST)

    def south_west(self, dest, src):
        self.__scamp5lib.move2Dir(dest, src, Direction.SOUTH, Direction.WEST)

    """
        library function
    """

    def median_filter(self, reg):
        self.__scamp5lib.medianFilter(reg)
        return scamp5.reg.C

    def edge_detection(self, reg, method='sobel'):
        if method == 'sobel':
            self.__scamp5lib.sobel_filter(reg)
            return self.reg.E
        if method == 'laplacian':
            self.__scamp5lib.laplacian_filter(reg)
            return self.reg.E
        return None


# example
if __name__ == "__main__":
    scamp5 = Scamp5()
    scamp5.vs_init()
    scamp5.vs_gui_set_info()
    dis1 = scamp5.add_display(b"origin", 0, 0, 1)
    dis2 = scamp5.add_display(b"median", 1, 0, 1)
    while True:
        scamp5.vs_frame_loop_control()
        # scamp5.get_image(scamp5.reg.F)
        scamp5.load_value(scamp5.reg.F, 50)
        scamp5.load_value(scamp5.reg.E, 50)
        scamp5.reg.A = scamp5.reg.E - scamp5.reg.F
        scamp5.plot(scamp5.reg.F, dis1)

        
