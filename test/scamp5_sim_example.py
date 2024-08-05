from lib.sim_py.scamp5 import Scamp5
import numpy as np
import random


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


def salt_and_pepper_noise(image, prob):
    """
    Add salt and pepper noise to an image.
    image: OpenCV image in grayscale or BGR
    prob: Probability of noise
    """
    output = np.copy(image)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rand = random.random()
            if rand < prob:
                output[i][j] = 0  # black pixel
            elif rand > thres:
                output[i][j] = 127  # white pixel
    return output


if __name__ == '__main__':
    scamp5 = Scamp5()
    scamp5.init(1)
    dis1 = scamp5.add_display(2, 3, 10)
    while True:
        scamp5.F = scamp5.get_image()
        scamp5.F.image = salt_and_pepper_noise(scamp5.F.image, 0.05)
        median_filter(scamp5.F)

        scamp5.plot(scamp5.A, 0, 0, "A")
        scamp5.plot(scamp5.B, 0, 1, "B")
        scamp5.plot(scamp5.C, 0, 2, "C")
        scamp5.plot(scamp5.F, 1, 0, "F")