import numpy as np


class Register:
    mask = np.full((256, 256), 1, dtype=np.uint8)

    def __init__(self, image):
        self.image = image
        self.height, self.width = image.shape[:2]
        self.flag = np.full((self.height, self.width), 1, dtype=np.int8)
        self.up_row = []
        self.down_row = []
        self.left_column = []
        self.right_column = []

    def __eq__(self, other):
        return np.array_equal(self.image[Register.mask == 1], other.image[Register.mask == 1])

    def __ne__(self, other):
        return not self.__eq__(other)

    def __sub__(self, other):
        result_image = self.image.copy()
        np.putmask(result_image, Register.mask, self.image - other.image)
        return Register(result_image)

    def __add__(self, other):
        result_image = self.image.copy()
        np.putmask(result_image, Register.mask, self.image + other.image)
        return Register(result_image)

    def __gt__(self, other):
        result = np.zeros_like(self.image, dtype=bool)
        if isinstance(other, Register):
            np.putmask(result, Register.mask, np.greater(self.image, other.image))
        elif isinstance(other, (int, float)):
            np.putmask(result, Register.mask, np.greater(self.image, other))
        else:
            raise ValueError("Unsupported type for comparison with Register")
        return result

    def __lt__(self, other):
        result = np.zeros_like(self.image, dtype=bool)
        if isinstance(other, Register):
            np.putmask(result, Register.mask, np.less(self.image, other.image))
        elif isinstance(other, (int, float)):
            np.putmask(result, Register.mask, np.less(self.image, other))
        else:
            raise ValueError("Unsupported type for comparison with Register")
        return result

    @classmethod
    def set_mask(cls, mask):
        cls.mask = mask

    @classmethod
    def get_mask(cls):
        return cls.mask

    def north(self):
        # 创建图像的副本
        img_copy = self.image.copy()
        new_image = np.zeros_like(self.image)
        self.up_row.append(img_copy[0, :].copy())
        new_image[:-1] = img_copy[1:]
        if self.down_row:
            new_image[-1, :] = self.down_row.pop()
        else:
            new_image[-1, :] = np.full((self.width,), 0, dtype=np.int8)
        np.putmask(img_copy, Register.mask, new_image)
        return Register(img_copy)

    def south(self):
        img_copy = self.image.copy()
        new_image = np.zeros_like(self.image)
        self.down_row.append(img_copy[-1, :].copy())
        new_image[1:] = img_copy[:-1]
        if self.up_row:
            new_image[0, :] = self.up_row.pop()
        else:
            new_image[0, :] = np.full((self.width,), 0, dtype=np.int8)
        np.putmask(img_copy, Register.mask, new_image)
        return Register(img_copy)

    def west(self):
        img_copy = self.image.copy()
        new_image = np.zeros_like(self.image)
        self.left_column.append(img_copy[:, 0].copy())
        new_image[:, :-1] = img_copy[:, 1:]
        if self.right_column:
            new_image[:, -1] = self.right_column.pop()
        else:
            new_image[:, -1] = np.full((self.height,), 0, dtype=np.uint8)
        np.putmask(img_copy, Register.mask, new_image)
        return Register(img_copy)

    def east(self):
        img_copy = self.image.copy()
        new_image = np.zeros_like(self.image)
        self.right_column.append(img_copy[:, -1].copy())
        new_image[:, 1:] = img_copy[:, :-1]
        if self.left_column:
            new_image[:, 0] = self.left_column.pop()
        else:
            new_image[:, 0] = np.full((self.height,), 0, dtype=np.int8)
        np.putmask(img_copy, Register.mask, new_image)
        return Register(img_copy)

    def north_east(self):
        return self.north().east()

    def north_west(self):
        return self.north().west()

    def south_east(self):
        return self.south().east()

    def south_west(self):
        return self.south().west()

    def north_north(self):
        return self.north().north()

    def south_south(self):
        return self.south().south()

    def east_east(self):
        return self.east().east()

    def west_west(self):
        return self.west().west()


if __name__ == "__main__":
    image = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ], dtype=np.uint8)
    mask = np.full((256, 256), 1, dtype=np.uint8)
    print(mask.shape)



