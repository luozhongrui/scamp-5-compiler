from lib.sim_py.scamp5 import Scamp5

def edge_detection():
    scamp5.A = scamp5.C.north()
    scamp5.B = scamp5.C.south()
    scamp5.A = scamp5.A + scamp5.B
    scamp5.A = scamp5.A + scamp5.C
    scamp5.A = scamp5.A + scamp5.C

    scamp5.B = scamp5.A.east()
    scamp5.A = scamp5.A.west()

    scamp5.B = scamp5.B - scamp5.A
    scamp5.D = scamp5.abs(scamp5.B)

    scamp5.A = scamp5.C.east()
    scamp5.B = scamp5.C.west()
    scamp5.A = scamp5.A + scamp5.B
    scamp5.A = scamp5.A + scamp5.C
    scamp5.A = scamp5.A + scamp5.C

    scamp5.B = scamp5.A.south()
    scamp5.A = scamp5.A.north()

    scamp5.B = scamp5.B - scamp5.A
    scamp5.A = scamp5.abs(scamp5.B)

    scamp5.E = scamp5.A + scamp5.D


if __name__ == '__main__':
    scamp5 = Scamp5()
    scamp5.init(1)
    dis1 = scamp5.add_display(1, 2, 10)
    while True:
        scamp5.C = scamp5.get_image()
        edge_detection()
        scamp5.plot(scamp5.C, 0, 0, "original")
        scamp5.plot(scamp5.E, 1, 2, "edge detection")
