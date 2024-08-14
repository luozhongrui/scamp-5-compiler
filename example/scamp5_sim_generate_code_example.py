from lib.sim_py.scamp5 import Scamp5


def init():
    scamp5.A = scamp5.load_value(127)
    scamp5.B = scamp5.load_value(127)
    scamp5.C = scamp5.load_value(127)


def median_filter(reg):
    init()
    reg = reg.north()
    scamp5.where(reg <= scamp5.A)
    scamp5.mov(scamp5.C, scamp5.B)
    scamp5.mov(scamp5.B, scamp5.A)
    scamp5.mov(scamp5.A, reg)
    scamp5.all()

    scamp5.where(reg >= scamp5.A) & scamp5.where(reg <= scamp5.B)
    scamp5.mov(scamp5.C, scamp5.B)
    scamp5.mov(scamp5.B, reg)
    scamp5.all()

    scamp5.where(scamp5.B <= reg)
    scamp5.where(reg <= scamp5.C)
    scamp5.mov(scamp5.C, reg)
    scamp5.all()

    reg = reg.south().south()
    scamp5.where(reg <= scamp5.A)
    scamp5.mov(scamp5.C, scamp5.B)
    scamp5.mov(scamp5.B, scamp5.A)
    scamp5.mov(scamp5.A, reg)
    scamp5.all()

    scamp5.where(scamp5.A <= reg) & scamp5.where(reg <= scamp5.B)
    scamp5.mov(scamp5.C, scamp5.B)
    scamp5.mov(scamp5.B, reg)
    scamp5.all()

    scamp5.where(scamp5.B <= reg) & scamp5.where(reg <= scamp5.C)
    scamp5.mov(scamp5.C, reg)
    scamp5.all()

    reg = reg.north().west()
    scamp5.where(reg <= scamp5.A)
    scamp5.mov(scamp5.C, scamp5.B)
    scamp5.mov(scamp5.B, scamp5.A)
    scamp5.mov(scamp5.A, reg)
    scamp5.all()

    scamp5.where(scamp5.A <= reg) & scamp5.where(reg <= scamp5.B)
    scamp5.mov(scamp5.C, scamp5.B)
    scamp5.mov(scamp5.B, reg)
    scamp5.all()

    scamp5.where(scamp5.B <= reg)
    scamp5.where(reg <= scamp5.C)
    scamp5.mov(scamp5.C, reg)
    scamp5.all()

    reg = reg.east().east()
    scamp5.where(reg <= scamp5.A)
    scamp5.mov(scamp5.C, scamp5.B)
    scamp5.mov(scamp5.B, scamp5.A)
    scamp5.mov(scamp5.A, reg)
    scamp5.all()

    scamp5.where(scamp5.A <= reg) & scamp5.where(reg <= scamp5.B)
    scamp5.mov(scamp5.C, scamp5.B)
    scamp5.mov(scamp5.B, reg)
    scamp5.all()

    scamp5.where(scamp5.B <= reg)
    scamp5.where(reg <= scamp5.C)
    scamp5.mov(scamp5.C, reg)
    scamp5.all()

    reg = reg.west()
    scamp5.where(reg <= scamp5.A)
    scamp5.mov(scamp5.C, scamp5.B)
    scamp5.mov(scamp5.B, scamp5.A)
    scamp5.mov(scamp5.A, reg)
    scamp5.all()

    scamp5.where(scamp5.A <= reg) & scamp5.where(reg <= scamp5.B)
    scamp5.mov(scamp5.C, scamp5.B)
    scamp5.mov(scamp5.B, reg)
    scamp5.all()

    scamp5.where(scamp5.B <= reg)
    scamp5.where(reg <= scamp5.C)
    scamp5.mov(scamp5.C, reg)
    scamp5.all()


if __name__ == '__main__':
    scamp5 = Scamp5()
    scamp5.init(1)
    dis1 = scamp5.add_display(2, 3, 10)
    while True:
        scamp5.F = scamp5.get_image()
        median_filter(scamp5.F)

        scamp5.plot(scamp5.A, 0, 0, "A")
        scamp5.plot(scamp5.B, 0, 1, "B")
        scamp5.plot(scamp5.C, 0, 2, "C")
        scamp5.plot(scamp5.F, 1, 0, "F")
