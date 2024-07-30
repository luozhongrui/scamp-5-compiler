import unittest
from unittest.mock import MagicMock, patch
import numpy as np
from lib.sim_py.scamp5 import Scamp5, Display, Register


class TestScamp5(unittest.TestCase):

    def test_init(self):
        with patch('cv2.VideoCapture') as MockCapture:
            s = Scamp5()
            self.assertIsNone(s.cap)
            self.assertIsNone(s.A)
            self.assertIsNone(s.B)

    def test_load_value(self):
        value = 10
        reg = Scamp5.load_value(value)
        self.assertTrue(np.array_equal(reg.image, np.full((256, 256), value, dtype=np.int8)))

    @patch('lib.sim_py.scamp5.Display')
    def test_add_display(self, MockDisplay):
        title = 'Test Display'
        display = Scamp5.add_display(title)
        MockDisplay.assert_called_with(title)

    def test_init_video_capture(self):
        with patch('cv2.VideoCapture') as MockCapture:
            s = Scamp5()
            s.init(1)
            MockCapture.assert_called_with(1)
            self.assertIsNotNone(s.cap)

    @patch('lib.sim_py.lib.sim.load_image')
    @patch('cv2.VideoCapture')
    def test_get_image(self, MockCapture, mock_load_image):
        mock_capture_instance = MockCapture.return_value
        mock_capture_instance.read.return_value = (True, np.random.randint(0, 255, (256, 256, 3), dtype=np.uint8))
        mock_load_image.return_value = np.random.randint(0, 255, (256, 256), dtype=np.uint8)

        s = Scamp5()
        s.init(1)
        image = s.get_image()
        self.assertIsInstance(image, Register)

    def test_mov(self):
        s = Scamp5()
        s.FLAG = Register(np.ones((256, 256), dtype=np.uint8))
        src = Register(np.full((256, 256), 5, dtype=np.int8))
        des = Register(np.zeros((256, 256), dtype=np.int8))
        s.mov(des, src)
        self.assertTrue(np.array_equal(des.image, src.image))

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

    def test_all(self):
        s = Scamp5()
        s.all()
        self.assertTrue(np.array_equal(s.FLAG, np.full((256, 256), 1, dtype=np.int8)))

    def test_NOT(self):
        reg = Register(np.array([[0, 1], [1, 0]], dtype=np.int8))
        result = Scamp5.NOT(reg)
        expected = Register(np.array([[1, 0], [0, 1]], dtype=np.int8))
        self.assertTrue(np.array_equal(result.image, expected.image))

    def test_AND(self):
        reg1 = Register(np.array([[1, 0], [1, 0]], dtype=np.int8))
        reg2 = Register(np.array([[1, 1], [0, 0]], dtype=np.int8))
        result = Scamp5.AND(reg1, reg2)
        expected = Register(np.array([[1, 0], [0, 0]], dtype=np.int8))
        self.assertTrue(np.array_equal(result.image, expected.image))

    def test_OR(self):
        reg1 = Register(np.array([[1, 0], [1, 0]], dtype=np.int8))
        reg2 = Register(np.array([[1, 1], [0, 0]], dtype=np.int8))
        result = Scamp5.OR(reg1, reg2)
        expected = Register(np.array([[1, 1], [1, 0]], dtype=np.int8))
        self.assertTrue(np.array_equal(result.image, expected.image))

    def test_XOR(self):
        reg1 = Register(np.array([[1, 0], [1, 0]], dtype=np.int8))
        reg2 = Register(np.array([[1, 1], [0, 0]], dtype=np.int8))
        result = Scamp5.XOR(reg1, reg2)
        expected = Register(np.array([[0, 1], [1, 0]], dtype=np.int8))
        self.assertTrue(np.array_equal(result.image, expected.image))


if __name__ == '__main__':
    unittest.main()

