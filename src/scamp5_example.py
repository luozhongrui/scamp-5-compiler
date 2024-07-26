from lib.scamp5 import Scamp5

if __name__ == '__main__':
    scamp5 = Scamp5()
    scamp5.vs_init()
    scamp5.vs_gui_set_info()
    dis1 = scamp5.add_display(b"origin", 0, 0, 1)
    dis2 = scamp5.add_display(b"median", 1, 0, 1)
    while True:
        scamp5.vs_frame_loop_control()
        scamp5.get_image(scamp5.reg.F)
        scamp5.load_value(scamp5.reg.A, 20)
        scamp5.load_value(scamp5.reg.E, 50)
        scamp5.reg.B = scamp5.reg.E - scamp5.reg.A
        # res = scamp5.edge_detection(scamp5.reg.F)
        # scamp5.plot(res, dis1)

