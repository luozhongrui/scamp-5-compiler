import numpy as np


class Register:
    mask = np.full((256, 256), 1, dtype=np.uint8)
    # up_row = []
    # down_row = []
    # left_column = []
    # right_column = []

    def __init__(self, image=None):

        self.image = image
        self.height, self.width = image.shape[:2]
        self.flag = np.full((self.height, self.width), 1, dtype=np.int8)
        self.up_row = []
        self.down_row = []
        self.left_column = []
        self.right_column = []

    def __sub__(self, other):
        result_image = self.image.copy()
        np.putmask(result_image, Register.mask, self.image - other.image)
        return Register(result_image)

    def __add__(self, other):
        result_image = self.image.copy()
        np.putmask(result_image, Register.mask, self.image + other.image)
        return Register(result_image)

    def __gt__(self, other):
        # result = np.zeros_like(self.image, dtype=bool)
        result = Register.mask.copy()
        if isinstance(other, Register):

            np.putmask(result, Register.mask,
                       np.greater(self.image, other.image))
        elif isinstance(other, (int, float)):
            np.putmask(result, Register.mask, np.greater(self.image, other))
        else:
            raise ValueError("Unsupported type for comparison with Register")
        new_mask = np.where(result, 1, 0).astype(np.uint8)
        Register.set_mask(new_mask)
        return result

    def __lt__(self, other):
        # result = np.zeros_like(self.image, dtype=bool)
        result = Register.mask.copy()
        if isinstance(other, Register):
            np.putmask(result, Register.mask, np.less(self.image, other.image))
        elif isinstance(other, (int, float)):
            np.putmask(result, Register.mask, np.less(self.image, other))
        else:
            raise ValueError("Unsupported type for comparison with Register")
        new_mask = np.where(result, 1, 0).astype(np.uint8)
        Register.set_mask(new_mask)
        return result

    def __le__(self, other):
        result = Register.mask.copy()
        if isinstance(other, Register):
            np.putmask(result, Register.mask, np.less_equal(self.image, other.image))
        elif isinstance(other, (int, float)):
            np.putmask(result, Register.mask, np.less_equal(self.image, other))
        else:
            raise ValueError("Unsupported type for comparison with Register")
        new_mask = np.where(result, 1, 0).astype(np.uint8)
        Register.set_mask(new_mask)
        return result

    def __ge__(self, other):
        result = Register.mask.copy()
        if isinstance(other, Register):

            np.putmask(result, Register.mask,
                       np.greater_equal(self.image, other.image))
        elif isinstance(other, (int, float)):
            np.putmask(result, Register.mask, np.greater_equal(self.image, other))
        else:
            raise ValueError("Unsupported type for comparison with Register")
        new_mask = np.where(result, 1, 0).astype(np.uint8)
        Register.set_mask(new_mask)
        return result


    @classmethod
    def set_mask(cls, mask):
        cls.mask = mask

    @classmethod
    def get_mask(cls):
        return cls.mask

    def north(self):
        img_copy = self.image.copy()
        new_up_row = self.up_row.copy()
        new_down_row = self.down_row.copy()
        new_left_column = self.left_column.copy()
        new_right_column = self.right_column.copy()

        new_up_row.append(img_copy[0, :].copy())
        img_copy[:-1] = img_copy[1:]
        if self.down_row:
            img_copy[-1, :] = self.down_row.pop()
        else:
            img_copy[-1, :] = np.full((self.width,), 0, dtype=np.int8)
        new_register = Register(img_copy)
        new_register.up_row = new_up_row.copy()
        new_register.down_row = new_down_row.copy()
        new_register.left_column = new_left_column.copy()
        new_register.right_column = new_right_column.copy()
        return new_register

    def south(self):
        img_copy = self.image.copy()
        new_up_row = self.up_row.copy()
        new_down_row = self.down_row.copy()
        new_left_column = self.left_column.copy()
        new_right_column = self.right_column.copy()

        new_down_row.append(img_copy[-1, :].copy())
        img_copy[1:] = img_copy[:-1]
        if self.up_row:
            img_copy[0, :] = self.up_row.pop()
        else:
            img_copy[0, :] = np.full((self.width,), 0, dtype=np.int8)
        new_register = Register(img_copy)
        new_register.up_row = new_up_row.copy()
        new_register.down_row = new_down_row.copy()
        new_register.left_column = new_left_column.copy()
        new_register.right_column = new_right_column.copy()
        return new_register

    def west(self):
        img_copy = self.image.copy()
        new_up_row = self.up_row.copy()
        new_down_row = self.down_row.copy()
        new_left_column = self.left_column.copy()
        new_right_column = self.right_column.copy()
        new_left_column.append(img_copy[:, 0].copy())
        img_copy[:, :-1] = img_copy[:, 1:]
        if self.right_column:
            img_copy[:, -1] = self.right_column.pop()
        else:
            img_copy[:, -1] = np.full((self.height,), 0, dtype=np.uint8)

        new_register = Register(img_copy)
        new_register.up_row = new_up_row.copy()
        new_register.down_row = new_down_row.copy()
        new_register.left_column = new_left_column.copy()
        new_register.right_column = new_right_column.copy()
        return new_register

    def east(self):
        img_copy = self.image.copy()
        new_up_row = self.up_row.copy()
        new_down_row = self.down_row.copy()
        new_left_column = self.left_column.copy()
        new_right_column = self.right_column.copy()
        new_right_column.append(img_copy[:, -1].copy())
        img_copy[:, 1:] = img_copy[:, :-1]
        if self.left_column:
            img_copy[:, 0] = self.left_column.pop()
        else:
            img_copy[:, 0] = np.full((self.height,), 0, dtype=np.int8)
        new_register = Register(img_copy)
        new_register.up_row = new_up_row.copy()
        new_register.down_row = new_down_row.copy()
        new_register.left_column = new_left_column.copy()
        new_register.right_column = new_right_column.copy()
        return new_register

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
