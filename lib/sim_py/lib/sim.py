import cv2
import numpy as np
import matplotlib.pyplot as plt


def load_image(handle, size=256):
    ret, frame = handle.read()
    if not ret:
        return None
    resize_frame = cv2.resize(frame, (size, size))
    gray_frame = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2GRAY)
    return gray_frame


class Display:
    def __init__(self, title):
        self.title = title
        self.fig, self.ax = plt.subplots()
        self.fig.canvas.manager.set_window_title(title)

    def show_image(self, image):
        self.ax.clear()
        self.ax.imshow(image, cmap='gray', vmin=-127, vmax=256)
        self.ax.axis('off')
        plt.draw()
        plt.pause(0.001)
        self.fig.canvas.mpl_connect('close_event', self.on_close)

    def on_close(self, event):
        plt.ioff()
        plt.close('all')
        exit(0)


if __name__ == "__main__":
    pass

