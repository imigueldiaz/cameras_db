from typing import List, Tuple
from unittest import TestCase
from unittest.mock import MagicMock, patch

from cameras_db.controllers import CamerasController
from cameras_db.constants import CREATE_CAMERA_TABLE_QUERY


class TestCamerasController(TestCase):
    from unittest.mock import patch

    def setUp(self):
        mock_cursor = MagicMock()

        mock_description = [
            (key,)
            for key in [
                "brand",
                "model",
                "sensor_size_w",
                "sensor_size_h",
                "sensor_px_w",
                "sensor_px_h",
            ]
        ]
        mock_cursor.configure_mock(description=mock_description)

        # Mock the execute and fetchall/one methods if needed
        mock_cursor.execute.return_value = None
        mock_cursor.fetchall.return_value = []  # Or mock data you expect to fetch

        self.controller = CamerasController(":memory:", cursor=mock_cursor)

        # Initialize the database schema
        mock_cursor.execute(CREATE_CAMERA_TABLE_QUERY)

    def test_row_to_camera(self):
        mock_description: list[tuple[str]] = [
            (key,)
            for key in [
                "brand",
                "model",
                "sensor_size_w",
                "sensor_size_h",
                "sensor_px_w",
                "sensor_px_h",
            ]
        ]

        mock_row = (
            "Canon",
            "EOS 5D",
            36.0,
            24.0,
            6720,
            4480,
        )

        camera = self.controller.row_to_camera(mock_row)

        self.assertEqual(camera.brand, "Canon")
        self.assertEqual(camera.model, "EOS 5D")
        self.assertEqual(camera.sensor_size_w, 36.0)
        self.assertEqual(camera.sensor_size_h, 24.0)
        self.assertEqual(camera.sensor_px_w, 6720)
        self.assertEqual(camera.sensor_px_h, 4480)

    def test_get_by_field(self):
        # Arrange

        def fetchall_side_effect(*args, **kwargs):
            query, params = args
            field, value = params
            return [row for row in mock_data if row[field] == value]

        mock_data = [
            {
                "brand": "Canon",
                "model": "EOS R6",
                "sensor_size_w": 36,
                "sensor_size_h": 24,
                "sensor_px_w": 6720,
                "sensor_px_h": 4480,
            },
            {
                "brand": "Nikon",
                "model": "D750",
                "sensor_size_w": 36,
                "sensor_size_h": 24,
                "sensor_px_w": 6720,
                "sensor_px_h": 4480,
            },
        ]

        self.controller.cursor.execute.side_effect = (
            lambda *args: None
        )  # Clear any existing side_effect or return_value
        self.controller.cursor.fetchall.side_effect = fetchall_side_effect

        # Act
        result = self.controller.get_by_field("brand", "Canon")

        # Assert
        self.assertEqual(len(result), 1)  # We expect one camera with the brand "Canon"
        self.assertEqual(
            result[0].brand, "Canon"
        )  # Assuming Camera objects have a 'brand' attribute
        self.assertEqual(
            result[0].model, "EOS R6"
        )  # Assuming Camera objects have a 'model' attribute

    def test_get_by_field_like(self):
        self.fail()

    def test_get_by_fields_like_and(self):
        self.fail()

    def test_get_by_fields_like_or(self):
        self.fail()

    def test_get_by_fields_with_operators(self):
        self.fail()

    def test_close(self):
        self.fail()
