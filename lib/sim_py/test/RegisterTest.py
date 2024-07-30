import unittest
import numpy as np
from lib.sim_py.lib.reg import Register


class TestRegister(unittest.TestCase):
    def setUp(self):
        self.image1 = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], dtype=np.int8)

        self.image2 = np.array([
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ], dtype=np.int8)
        Register.set_mask(np.ones((3, 3), dtype=np.uint8))

        self.register1 = Register(self.image1)
        self.register2 = Register(self.image2)

    def test_sub(self):
        result = self.register1 - self.register2
        expected = Register(np.array([
            [-8, -6, -4],
            [-2, 0, 2],
            [4, 6, 8]
        ], dtype=np.int8))
        np.testing.assert_array_equal(result.image, expected.image)

    def test_add(self):
        result = self.register1 + self.register2
        expected = Register(np.array([
            [10, 10, 10],
            [10, 10, 10],
            [10, 10, 10]
        ], dtype=np.int8))
        np.testing.assert_array_equal(result.image, expected.image)

    def test_gt(self):
        result = self.register1 > self.register2
        expected_result = np.array([
            [False, False, False],
            [False, False, True],
            [True, True, True]
        ], dtype=bool)
        expected_mask = np.array([
            [0, 0, 0],
            [0, 0, 1],
            [1, 1, 1]
        ], dtype=np.uint8)
        np.testing.assert_array_equal(result, expected_result)
        np.testing.assert_array_equal(Register.get_mask(), expected_mask)

    def test_lt(self):
        result = self.register1 < self.register2
        expected_result = np.array([
            [True, True, True],
            [True, False, False],
            [False, False, False]
        ], dtype=bool)
        expected_mask = np.array([
            [1, 1, 1],
            [1, 0, 0],
            [0, 0, 0]
        ], dtype=np.uint8)
        np.testing.assert_array_equal(result, expected_result)
        np.testing.assert_array_equal(Register.get_mask(), expected_mask)

    def test_north(self):
        result = self.register1.north()
        expected_image = np.array([
            [4, 5, 6],
            [7, 8, 9],
            [0, 0, 0]
        ], dtype=np.int8)
        np.testing.assert_array_equal(result.image, expected_image)

    def test_south(self):
        result = self.register1.south()
        expected_image = np.array([
            [0, 0, 0],
            [1, 2, 3],
            [4, 5, 6]
        ], dtype=np.int8)
        np.testing.assert_array_equal(result.image, expected_image)

    def test_west(self):
        result = self.register1.west()
        expected_image = np.array([
            [2, 3, 0],
            [5, 6, 0],
            [8, 9, 0]
        ], dtype=np.int8)
        np.testing.assert_array_equal(result.image, expected_image)

    def test_east(self):
        result = self.register1.east()
        expected_image = np.array([
            [0, 1, 2],
            [0, 4, 5],
            [0, 7, 8]
        ], dtype=np.int8)
        np.testing.assert_array_equal(result.image, expected_image)


if __name__ == '__main__':
    unittest.main()

