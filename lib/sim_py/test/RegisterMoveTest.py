import numpy as np
import unittest
from lib.sim_py.lib.reg import Register  # 确保这里正确导入你的 Register 类


class TestRegister(unittest.TestCase):
    def setUp(self):
        # 初始化一个3x3的测试图像
        self.image = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], dtype=np.uint8)
        self.reg = Register(self.image.copy())
        self.reg.set_mask(np.full((3, 3), 1))

    def test_north_movement(self):
        # 测试向北移动
        north_image = self.reg.north()
        expected_north = np.array([
            [4, 5, 6],
            [7, 8, 9],
            [0, 0, 0]  # 最后一行应填充为0
        ], dtype=np.uint8)
        self.assertTrue(np.array_equal(north_image.image, expected_north), "North movement failed")
        self.assertEqual(len(self.reg.up_row), 1, "Up row stack should have 1 item")

    def test_south_movement(self):
        # 测试向南移动
        expected_south = np.array([
            [0, 0, 0],
            [1, 2, 3],
            [4, 5,  6]  # 最后一行应填充为0
        ], dtype=np.uint8)
        south_image = self.reg.south()
        # 应该恢复到原始状态
        self.assertTrue(np.array_equal(south_image.image, expected_south), "South movement did not restore correctly")
        self.assertEqual(len(self.reg.down_row), 1, "Down row stack should have 1 item")

    def test_west_movement(self):
        # 测试向西移动
        west_image = self.reg.west()
        expected_west = np.array([
            [2, 3, 0],
            [5, 6, 0],
            [8, 9, 0]
        ], dtype=np.uint8)
        self.assertTrue(np.array_equal(west_image.image, expected_west), "West movement failed")
        self.assertEqual(len(self.reg.left_column), 1, "Left column stack should have 1 item")

    def test_east_movement(self):
        expected_east = np.array([
            [0, 1, 2],
            [0, 4, 5],
            [0, 7, 8]
        ], dtype=np.uint8)
        # 测试向东移动
        east_image = self.reg.east()
        # 应该恢复到原始状态
        self.assertTrue(np.array_equal(east_image.image, expected_east), "East movement did not restore correctly")
        self.assertEqual(len(self.reg.right_column), 1, "Right column stack should have 1 item")


if __name__ == '__main__':
    unittest.main()