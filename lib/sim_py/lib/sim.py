import cv2
import numpy as np
import matplotlib.pyplot as plt


def load_image(handle, size=256):
    ret, frame = handle.read()
    if not ret:
        return None
    resize_frame = cv2.resize(frame, (size, size))
    gray_frame = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2GRAY)
    map_frame = np.round((gray_frame / 255.0) * 127).astype(np.int8)
    return map_frame


# class Display:
#     def __init__(self, title):
#         self.title = title
#         self.closed = False
#         self.fig, self.ax = plt.subplots()
#         self.fig.canvas.manager.set_window_title(title)
#         self.fig.canvas.mpl_connect('close_event', self.on_close)
#
#     def show_image(self, image):
#         if not self.closed:
#             self.ax.clear()
#             self.ax.imshow(image, cmap='gray', vmin=-128, vmax=127)
#             self.ax.axis('off')
#             plt.draw()
#             plt.pause(0.000001)
#
#     def on_close(self, event):
#         self.closed = True
#         plt.close(self.fig)
class Display:
    _instance = None  # 单例实例

    @classmethod
    def initialize_window(cls, rows, cols, width, height):
        if cls._instance is None:
            cls._instance = cls(rows, cols, width, height)
        return cls._instance

    def __init__(self, rows=None, cols=None, width=None, height=None):
        if Display._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Display._instance = self
            self.fig, self.axs = plt.subplots(rows, cols, figsize=(width, height))
            self.fig.canvas.manager.set_window_title("Display Window")
            self.closed = False
            self.fig.canvas.mpl_connect('close_event', self.on_close)

    @staticmethod
    def on_close(event):
        Display._instance.closed = True
        plt.close(Display._instance.fig)
        exit(0)

    def show_image(self, image, row, col, title=None):
        if not self.closed:
            if isinstance(self.axs, np.ndarray):
                if self.axs.ndim == 2:
                    ax = self.axs[row, col]
                elif self.axs.ndim == 1:
                    ax = self.axs[row]
                else:
                    ax = self.axs
            else:
                ax = self.axs

            ax.clear()
            ax.imshow(image, cmap='gray', vmin=-128, vmax=127)
            ax.axis('off')
            if title:
                ax.set_title(title)
            self.fig.canvas.draw()  # 使用 draw 而不是 draw_idle
            plt.pause(0.001)  # 增加一些延时以确保图像刷新

