import numpy as np
import unittest
from lib.sim_py.lib.reg import Register


class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 初始化一个3x3的测试图像，仅执行一次
        cls.image = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], dtype=np.uint8)
        cls.initial_mask = np.full((3, 3), 1)
        cls.reg = Register(cls.image.copy())
        cls.reg.set_mask(cls.initial_mask)

    def setUp(self):
        pass

    def test_north_movement(self):
        # 测试向北移动
        print("original:\n", self.reg.image)
        north_image = self.reg.north()
        expected_north = np.array([
            [4, 5, 6],
            [7, 8, 9],
            [0, 0, 0]  # 最后一行应填充为0
        ], dtype=np.uint8)
        print("north:\n", north_image.image)
        self.assertTrue(np.array_equal(north_image.image, expected_north), "North movement failed")
        self.assertEqual(len(self.reg.up_row), 0, "Up row stack should have 1 item")
        self.assertEqual(len(north_image.up_row), 1, "Up row stack should have 1 item")

    def test_south_movement(self):
        # 测试向南移动
        print("original:\n", self.reg.image)
        expected_south = np.array([
            [0, 0, 0],
            [1, 2, 3],
            [4, 5, 6]  # 最后一行应填充为0
        ], dtype=np.uint8)
        south_image = self.reg.south()
        print("south:\n", south_image.image)
        self.assertTrue(np.array_equal(south_image.image, expected_south), "South movement did not restore correctly")
        self.assertEqual(len(self.reg.down_row), 0, "Down row stack should have 1 item")
        self.assertEqual(len(south_image.down_row), 1, "Down row stack should have 1 item")

    def test_west_movement(self):
        # 测试向西移动
        print("original:\n", self.reg.image)
        west_image = self.reg.west()
        expected_west = np.array([
            [2, 3, 0],
            [5, 6, 0],
            [8, 9, 0]
        ], dtype=np.uint8)
        print("west:\n", west_image.image)
        self.assertTrue(np.array_equal(west_image.image, expected_west), "West movement failed")
        self.assertEqual(len(self.reg.left_column), 0, "Left column stack should have 1 item")
        self.assertEqual(len(west_image.left_column), 1, "Left column stack should have 1 item")

    def test_east_movement(self):
        print("original:\n", self.reg.image)
        expected_east = np.array([
            [0, 1, 2],
            [0, 4, 5],
            [0, 7, 8]
        ], dtype=np.uint8)
        # 测试向东移动
        east_image = self.reg.east()
        print("east:\n", east_image.image)
        self.assertTrue(np.array_equal(east_image.image, expected_east), "East movement did not restore correctly")
        self.assertEqual(len(self.reg.right_column), 0, "Right column stack should have 1 item")
        self.assertEqual(len(east_image.right_column), 1, "Right column stack should have 1 item")


if __name__ == '__main__':
    unittest.main()
