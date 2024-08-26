from lib.sim_py.scamp5 import Scamp5


def median_filter():
    scamp5.A = scamp5.load_value(127)
    scamp5.B = scamp5.load_value(127)
    scamp5.C = scamp5.load_value(127)
    scamp5.F = scamp5.F.north()
    scamp5.where(scamp5.F <= scamp5.A)
    scamp5.C = scamp5.B
    scamp5.B = scamp5.A
    scamp5.A = scamp5.F
    scamp5.all()

    scamp5.where(scamp5.F >= scamp5.A) & scamp5.where(scamp5.F <= scamp5.B)
    scamp5.C = scamp5.B
    scamp5.B = scamp5.F
    scamp5.all()

    scamp5.where(scamp5.B <= scamp5.F)
    scamp5.where(scamp5.F <= scamp5.C)
    scamp5.C = scamp5.F
    scamp5.all()

    scamp5.F = scamp5.F.south_south()
    scamp5.where(scamp5.F <= scamp5.A)
    scamp5.C = scamp5.B
    scamp5.B = scamp5.A
    scamp5.A = scamp5.F
    scamp5.all()

    scamp5.where(scamp5.A <= scamp5.F) & scamp5.where(scamp5.F <= scamp5.B)
    scamp5.C = scamp5.B
    scamp5.B = scamp5.F
    scamp5.all()

    scamp5.where(scamp5.B <= scamp5.F) & scamp5.where(scamp5.F <= scamp5.C)
    scamp5.C = scamp5.F
    scamp5.all()

    scamp5.F = scamp5.F.north_west()
    scamp5.where(scamp5.F <= scamp5.A)
    scamp5.C = scamp5.B
    scamp5.B = scamp5.A
    scamp5.A = scamp5.F
    scamp5.all()

    scamp5.where(scamp5.A <= scamp5.F) & scamp5.where(scamp5.F <= scamp5.B)
    scamp5.C = scamp5.B
    scamp5.B = scamp5.F
    scamp5.all()

    scamp5.where(scamp5.B <= scamp5.F)
    scamp5.where(scamp5.F <= scamp5.C)
    scamp5.C = scamp5.F
    scamp5.all()

    scamp5.F = scamp5.F.east_east()
    scamp5.where(scamp5.F <= scamp5.A)
    scamp5.C = scamp5.B
    scamp5.B = scamp5.A
    scamp5.A = scamp5.F
    scamp5.all()

    scamp5.where(scamp5.A <= scamp5.F) & scamp5.where(scamp5.F <= scamp5.B)
    scamp5.C = scamp5.B
    scamp5.B = scamp5.F
    scamp5.all()

    scamp5.where(scamp5.B <= scamp5.F)
    scamp5.where(scamp5.F <= scamp5.C)
    scamp5.C = scamp5.F
    scamp5.all()

    scamp5.F = scamp5.F.west()
    scamp5.where(scamp5.F <= scamp5.A)
    scamp5.C = scamp5.B
    scamp5.B = scamp5.A
    scamp5.A = scamp5.F
    scamp5.all()

    scamp5.where(scamp5.A <= scamp5.F) & scamp5.where(scamp5.F <= scamp5.B)
    scamp5.C = scamp5.B
    scamp5.B = scamp5.F
    scamp5.all()

    scamp5.where(scamp5.B <= scamp5.F)
    scamp5.where(scamp5.F <= scamp5.C)
    scamp5.C = scamp5.F
    scamp5.all()


if __name__ == '__main__':
    scamp5 = Scamp5()
    scamp5.init(1)
    dis1 = scamp5.add_display(1, 2, 10)
    while True:
        scamp5.F = scamp5.get_image()
        median_filter()
        scamp5.plot(scamp5.F, 0, 0, "original")
        scamp5.plot(scamp5.C, 1, 2, "median filter")
