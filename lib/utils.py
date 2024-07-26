import ctypes


class AREG(ctypes.Structure):
    _fields_ = [
        ("index", ctypes.c_uint16),
        ("name", ctypes.c_char_p)
    ]
    __scamp5lib = ctypes.CDLL(r'D:\dissertation\sourceCode\scamp5_project\scamp5lib.dll')

    def __init__(self, index, name):
        super(AREG, self).__init__()
        self.index = index
        self.name = name
        self.__scamp5lib.c_add.argtypes = [ctypes.POINTER(AREG), ctypes.POINTER(AREG), ctypes.POINTER(AREG)]
        self.__scamp5lib.c_add.restype = None

        self.__scamp5lib.c_sub.argtypes = [ctypes.POINTER(AREG), ctypes.POINTER(AREG), ctypes.POINTER(AREG)]
        self.__scamp5lib.c_sub.restype = None

        self.__scamp5lib.analog_where.argtypes = [ctypes.POINTER(AREG)]
        self.__scamp5lib.analog_where.restype = None

        self.__scamp5lib.digit_where.argtypes = [ctypes.POINTER(AREG)]
        self.__scamp5lib.digit_where.restype = None

        self.__scamp5lib.c_gt.argtypes = [ctypes.POINTER(AREG), ctypes.POINTER(AREG)]
        self.__scamp5lib.c_gt.restype = None

        self.__scamp5lib.c_lt.argtypes = [ctypes.POINTER(AREG), ctypes.POINTER(AREG)]
        self.__scamp5lib.c_lt.restype = None

    def __add__(self, other):
        if isinstance(other, AREG):
            self.__scamp5lib.c_add(self, self, other)
            return self
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, AREG):
            self.__scamp5lib.c_sub(self, self, other)
            return self
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, AREG):
            self.__scamp5lib.c_gt(self, other)

    def __lt__(self, other):
        if isinstance(other, AREG):
            self.__scamp5lib.c_lt(self, other)


class Reg:
    _instance = None
    __scamp5lib = ctypes.CDLL(r'D:\dissertation\sourceCode\scamp5_project\scamp5lib.dll')

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Reg, cls).__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        self.A = AREG(index=10, name=b"A")
        self.B = AREG(index=11,name= b"B")
        self.C = AREG(index=12, name=b"C")
        self.D = AREG(index=13, name=b"D")
        self.E = AREG(index=14, name=b"E")
        self.F = AREG(index=15, name=b"F")

        self.R0 = AREG(index=3, name=b"R0")
        self.R1 = AREG(index=4, name=b"R1")
        self.R2 = AREG(index=5, name=b"R2")
        self.R3 = AREG(index=6, name=b"R3")
        self.R4 = AREG(index=7, name=b"R4")
        self.R5 = AREG(index=8, name=b"R5")
        self.R6 = AREG(index=9, name=b"R6")
        self.R7 = AREG(index=10,name=b"R7")
        self.R8 = AREG(index=11,name=b"R8")
        self.R9 = AREG(index=12, name=b"R9")
        self.R10 = AREG(index=13, name=b"R10")
        self.R11 = AREG(index=14, name=b"R11")
        self.R12 = AREG(index=15, name=b"R12")
        
        self.FLAG = AREG(index=1, name=b"FLAG")

        # self.__scamp5lib.moveDir.argtypes = [ctypes.POINTER(AREG), ctypes.POINTER(AREG), ctypes.c_int]
        # self.__scamp5lib.moveDir.restype = None

    # def __setattr__(self, name, value):
    #     self.__scamp5lib.moveDir(name, value)
    #     super.__setattr__(self, name, value)


class Direction(ctypes.c_int):
    NORTH = 1
    EAST = 2
    SOUTH = 4
    WEST = 8

    def __str__(self):
        if self.value == self.NORTH:
            return "north"
        elif self.value == self.EAST:
            return "east"
        elif self.value == self.SOUTH:
            return "south"
        elif self.value == self.WEST:
            return "west"
        else:
            return "unknown direction"
