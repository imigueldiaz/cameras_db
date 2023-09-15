import unittest
from math import sqrt
from cameras_db.models.Camera import Camera


class TestCameraMethods(unittest.TestCase):

    def setUp(self):
        self.camera = Camera(
            brand='Canon',
            model='EOS 5D',
            sensor_size_w=36.0,
            sensor_size_h=24.0,
            sensor_px_w=6720,
            sensor_px_h=4480,
            # Add other attributes as required
        )

    def test_diagonal_size_mm(self):
        expected_diagonal_mm = sqrt(36.0 ** 2 + 24.0 ** 2)
        self.assertEqual(self.camera.diagonal_size_mm(), expected_diagonal_mm)

    def test_diagonal_size_px(self):
        expected_diagonal_px = sqrt(6720 ** 2 + 4480 ** 2)
        self.assertEqual(self.camera.diagonal_size_px(), expected_diagonal_px)

    def test_sensor_property(self):
        expected_sensor_tuple = (36.0, 24.0, 6720, 4480)
        self.assertEqual(self.camera.sensor, expected_sensor_tuple)


if __name__ == '__main__':
    unittest.main()
