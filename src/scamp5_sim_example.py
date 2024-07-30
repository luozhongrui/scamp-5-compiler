from lib.sim_py.scamp5 import Scamp5

if __name__ == '__main__':
    scamp5 = Scamp5()
    scamp5.init(1)
    dis1 = scamp5.add_display(1,1, 10)
    while True:

        scamp5.C = scamp5.get_image()
        scamp5.B = scamp5.C.north().north()
        scamp5.plot(scamp5.C, 0, 0, "original")
        # scamp5.plot(scamp5.B, 1, 0, "north")