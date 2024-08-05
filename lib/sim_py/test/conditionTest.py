import unittest
import numpy as np
from lib.sim_py.lib.reg import Register


class TestRegister(unittest.TestCase):

    def setUp(self):
        self.image1 = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], dtype=np.uint8)

        self.image2 = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [3, 2, 1]
        ], dtype=np.uint8)
        Register.set_mask(np.ones((3, 3), dtype=np.uint8))

        self.register1 = Register(self.image1)
        self.register2 = Register(self.image2)

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

    def test_lt_consecutive(self):
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

        result = self.register1 > self.register2
        expected_result = np.array([
            [False, False, False],
            [False, False, False],
            [False, False, False]
        ], dtype=bool)

        expected_mask = np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ], dtype=np.uint8)
        np.testing.assert_array_equal(result, expected_result)
        np.testing.assert_array_equal(Register.get_mask(), expected_mask)

    def test_equal(self):
        result = self.register1 > self.register2
        print(result)
        expected_result = np.array([
            [False, False, False],
            [False, False, False],
            [True, True, True]
        ], dtype=bool)
        np.testing.assert_array_equal(result, expected_result)




if __name__ == '__main__':
    unittest.main()
