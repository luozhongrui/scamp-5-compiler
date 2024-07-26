import unittest
from unittest.mock import MagicMock, patch
import numpy as np
import cv2
from lib.sim_py.scamp5 import Scamp5, Display, Register


class TestScamp5(unittest.TestCase):

    def test_init(self):
        with patch('cv2.VideoCapture') as MockCapture:
            s = Scamp5()
            self.assertIsNone(s.cap)
            self.assertIsNone(s.A)
            self.assertIsNone(s.B)
            # 更多属性的检查...

    def test_load_value(self):
        value = 10
        reg = Scamp5.load_value(value)
        self.assertTrue(np.array_equal(reg.image, np.full((256, 256), value, dtype=np.int8)))

    def test_add_display(self):
        with patch('lib.sim.Display') as MockDisplay:
            title = 'Test Display'
            display = Scamp5.add_display(title)
            MockDisplay.assert_called_with(title)

    def test_init_video_capture(self):
        with patch('cv2.VideoCapture') as MockCapture:
            s = Scamp5()
            s.init(1)
            MockCapture.assert_called_with(1)
            self.assertIsNotNone(s.cap)

    def test_get_image(self):
        with patch('lib.sim.load_image') as mock_load_image, \
             patch('cv2.VideoCapture') as MockCapture:
            mock_load_image.return_value = np.random.randint(0, 255, (256, 256), dtype=np.uint8)
            s = Scamp5()
            s.init(1)
            image = s.get_image()
            self.assertIsInstance(image, Register)

    def test_plot(self):
        reg = Scamp5.load_value(0)
        with patch.object(Display, 'show_image') as mock_show_image:
            disp = Display('test')
            Scamp5.plot(reg, disp)
            mock_show_image.assert_called_with(reg.image)

    def test_printf(self):
        reg = Scamp5.load_value(-10)
        with patch('builtins.print') as mock_print:
            Scamp5.printf(reg)
            mock_print.assert_called_with(reg.image)

    def test_where(self):
        s = Scamp5()
        s.where(np.array([[True, False], [False, True]]))
        self.assertTrue(np.array_equal(s.FLAG, np.array([[1, 0], [0, 1]], dtype=np.int8)))

    def test_all(self):
        s = Scamp5()
        s.all()
        self.assertTrue(np.array_equal(s.FLAG, np.full((256, 256), 1, dtype=np.int8)))


if __name__ == '__main__':
    unittest.main()
