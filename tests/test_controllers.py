from math import sqrt
from unittest import TestCase

from cameras_db.controllers import CamerasController
from cameras_db.constants import CREATE_CAMERA_TABLE_QUERY
from cameras_db.models.Camera import Camera


class TestCamerasController(TestCase):
    from unittest.mock import patch

    def setUp(self):
        # Create an in-memory SQLite3 database
        self.controller = CamerasController(":memory:")

        # Create the cameras table
        self.controller.cursor.execute(CREATE_CAMERA_TABLE_QUERY)

        # Insert mock data into the cameras table
        mock_data = [
            ("Canon", "EOS R6", 36, 24, 6720, 4480),
            ("Nikon", "D750", 36, 24, 6720, 4480),
            ("Sony", "A7 III", 35.6, 23.8, 6000, 4000),
        ]

        self.controller.cursor.executemany(
            """
            INSERT INTO cameras (brand, model, sensor_size_w, sensor_size_h, sensor_px_w, sensor_px_h)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            mock_data,
        )

        # Save the changes to the database
        self.controller.conn.commit()

    def test_row_to_camera(self):
        # Insert a test row into the database
        mock_row = (
            "Canon",
            "EOS 5D",
            36.0,
            24.0,
            6720,
            4480,
        )
        self.controller.cursor.execute(
            """
                INSERT INTO cameras (brand, model, sensor_size_w, sensor_size_h, sensor_px_w, sensor_px_h)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
            mock_row,
        )
        self.controller.conn.commit()

        # Fetch the test row from the database
        self.controller.cursor.execute(
            "SELECT * FROM cameras WHERE brand = 'Canon' AND model = 'EOS 5D'"
        )
        fetched_row = self.controller.cursor.fetchone()

        # Get the column names from the cursor's description
        columns = [desc[0] for desc in self.controller.cursor.description]

        # Call the row_to_camera method with the fetched row and columns
        camera = self.controller.row_to_camera(fetched_row, columns)

        # Assert the camera object has the correct attributes
        self.assertEqual(camera.brand, "Canon")
        self.assertEqual(camera.model, "EOS 5D")
        self.assertEqual(camera.sensor_size_w, 36.0)
        self.assertEqual(camera.sensor_size_h, 24.0)
        self.assertEqual(camera.sensor_px_w, 6720)
        self.assertEqual(camera.sensor_px_h, 4480)

    def test_get_by_field(self):
        # Call the method under test
        result = self.controller.get_by_field("brand", "Canon")

        # Assert we got the expected camera
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].brand, "Canon")
        self.assertEqual(result[0].model, "EOS R6")

    def test_get_by_field_like(self):
        # Call the method under test
        result = self.controller.get_by_field_like("brand", "Can")

        # Assert we got the expected camera
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].brand, "Canon")
        self.assertEqual(result[0].model, "EOS R6")

    def test_get_by_fields_like_and(self):
        # Call the method under test
        result = self.controller.get_by_fields_like_and(
            {"brand": "Can", "model": "EOS"}
        )

        # Assert we got the expected camera
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].brand, "Canon")
        self.assertEqual(result[0].model, "EOS R6")

    def test_get_by_fields_like_or(self):
        # Call the method under test
        result = self.controller.get_by_fields_like_or(
            {"brand": "Can", "model": "D750"}
        )

        # Assert we got the expected cameras
        self.assertEqual(len(result), 2)
        self.assertIn(result[0].model, ["EOS R6", "D750"])
        self.assertIn(result[0].brand, ["Canon", "Nikon"])

    def test_get_by_fields_with_operators(self):
        # Define the conditions for the query
        conditions = [
            ("brand", "=", "Canon"),
            ("sensor_size_w", ">", 35),
        ]

        # Call the method under test
        result = self.controller.get_by_fields_with_operators(conditions)

        # Assert we got the expected camera
        self.assertEqual(len(result), 1)
        camera = result[0]
        self.assertEqual(camera.brand, "Canon")
        self.assertEqual(camera.model, "EOS R6")
        self.assertEqual(camera.sensor_size_w, 36)
        self.assertEqual(camera.sensor_size_h, 24)
        self.assertEqual(camera.sensor_px_w, 6720)
        self.assertEqual(camera.sensor_px_h, 4480)






