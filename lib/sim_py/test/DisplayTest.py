import unittest
from unittest.mock import patch, MagicMock
import numpy as np
from lib.sim_py.lib.sim import Display


class TestDisplay(unittest.TestCase):

    @patch('matplotlib.pyplot.subplots')
    def test_display_initialization(self, mock_subplots):
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_subplots.return_value = (mock_fig, mock_ax)

        display = Display('Test Display')
        self.assertEqual(display.title, 'Test Display')
        self.assertFalse(display.closed)
        self.assertEqual(display.fig, mock_fig)
        self.assertEqual(display.ax, mock_ax)

    @patch('matplotlib.pyplot.pause')
    @patch('matplotlib.pyplot.draw')
    @patch('matplotlib.pyplot.subplots')
    def test_show_image(self, mock_subplots, mock_draw, mock_pause):
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_subplots.return_value = (mock_fig, mock_ax)

        display = Display('Test Display')
        test_image = np.random.randint(-128, 127, (256, 256), dtype=np.int8)

        display.show_image(test_image)

        # Ensure ax.imshow is called with correct parameters
        display.ax.imshow.assert_called_with(test_image, cmap='gray', vmin=-128, vmax=127)
        mock_draw.assert_called_once()
        mock_pause.assert_called_once_with(0.000001)

    @patch('matplotlib.pyplot.close')
    def test_on_close(self, mock_close):
        display = Display('Test Display')
        mock_event = MagicMock()
        display.on_close(mock_event)
        self.assertTrue(display.closed)
        mock_close.assert_called_with(display.fig)


if __name__ == '__main__':
    unittest.main()

