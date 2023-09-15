import csv
import sqlite3
from typing import Dict

from cameras_db import CREATE_CAMERA_TABLE_QUERY


class CameraDBFiller:
    def __init__(self, db_name, table_name, csv_file_path):
        self.db_name = db_name
        self.table_name = table_name
        self.csv_file_path = csv_file_path
        self.conn = None
        self.cursor = None

    def connect_db(self) -> None:
        """
        Connects to the database specified by `db_name`.

        :return: None
        """
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        print(f"Connected to {self.db_name}")

    def create_camera_table(self) -> None:
        """
        Creates a camera table in the database.

        This function executes a SQL query to create a table named {self.table_name} in the database. The table has the following columns:

        - url: TEXT
        - image_url: TEXT
        - brand: TEXT
        - model: TEXT
        - also_known_as: TEXT
        - year: INTEGER
        - megapixels: REAL
        - effective_megapixels: REAL
        - total_megapixels: REAL
        - sensor_size: TEXT
        - sensor_type: TEXT
        - sensor_resolution: TEXT
        - max_image_resolution: TEXT
        - crop_factor: REAL
        - optical_zoom: REAL
        - digital_zoom: INTEGER
        - iso: TEXT
        - raw_support: INTEGER
        - manual_focus: INTEGER
        - normal_focus_range: TEXT
        - macro_focus_range: TEXT
        - focal_length_35mm_equiv: TEXT
        - aperture_priority: INTEGER
        - max_aperture: TEXT
        - max_aperture_35mm_equiv: TEXT
        - depth_of_field: TEXT
        - metering: TEXT
        - exposure_compensation: TEXT
        - shutter_priority: INTEGER
        - min_shutter_speed: TEXT
        - max_shutter_speed: TEXT
        - built_in_flash: INTEGER
        - external_flash: INTEGER
        - viewfinder: TEXT
        - white_balance_presets: INTEGER
        - screen_size: TEXT
        - screen_resolution: TEXT
        - video_capture: INTEGER
        - max_video_resolution: TEXT
        - storage_types: TEXT
        - usb: TEXT
        - hdmi: INTEGER
        - wireless: INTEGER
        - gps: TEXT
        - battery: TEXT
        - weight: REAL
        - dimensions: TEXT
        - sensor_size_w: REAL
        - sensor_size_h: REAL
        - sensor_px_w: INTEGER
        - sensor_px_h: INTEGER

        This function does not return anything.
        """

        self.cursor.execute(CREATE_CAMERA_TABLE_QUERY)
        print(f"Created table {self.table_name}")

    def read_csv_and_insert(self) -> None:
        """
        Reads a CSV file and inserts its contents into a database table.

        Returns:
            None
        """
        with open(self.csv_file_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            row: Dict[str, str]
            for row in reader:
                self.insert_camera(row)
        print(
            f"Read {self.csv_file_path} and inserted into {self.table_name} {reader.line_num} rows"
        )

    def read_json_and_insert(self, json_cameras_data) -> None:
        """
        Reads a JSON object containing camera data and inserts it into the database.

        Parameters:
            json_cameras_data (List[Dict[str, str]]): A list of dictionaries representing camera data.

        Returns:
            None
        """
        camera_dict: Dict[str, str]
        for camera_dict in json_cameras_data:
            self.insert_camera(camera_dict)
        self.conn.commit()
        print(
            f"Read json data and inserted into {self.table_name} {len(json_cameras_data)} rows"
        )

    def insert_camera(self, camera_dict) -> None:
        """
        Insert a camera into the database.

        Args:
            camera_dict (dict): A dictionary containing the camera information.

        Returns:
            None
        """
        # Remove special characters and quote column names
        columns = [
            f'"{col.replace(".", "").replace("(", "").replace(")", "").replace("-", "_")}"'
            for col in camera_dict.keys()
        ]

        # Convert lists to comma-separated strings
        values = [
            ",".join(val) if isinstance(val, list) else val
            for val in camera_dict.values()
        ]

        placeholders = ", ".join("?" * len(columns))
        query = f"INSERT INTO {self.table_name} ({', '.join(columns)}) VALUES ({placeholders})"

        self.cursor.execute(query, tuple(values))

    def close_db(self):
        """
        Closes the database connection and cursor.
        """
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

        print(f"Closed {self.db_name}")

    def vacuum_db(self) -> None:
        """
        Vacuum the database.

        This function vacuums the database specified by `self.db_name`. It first checks if a connection to the database
        has been established using `self.conn`. If a connection does not exist, it calls `self.connect_db()` to establish
        a connection.

        VACUUM is a SQLite command that reclaims storage occupied by dead tuples. It is used to optimize database
        performance by freeing up space and improving query execution time. By default, VACUUM runs in a transaction,
        but we disable transactions for VACUUM by setting `self.conn.isolation_level` to `None`. After executing the
        VACUUM command, we enable transactions back by setting `self.conn.isolation_level` to an empty string.

        Parameters:
        - None

        Returns:
        - None
        """
        print(f"Vacuuming {self.db_name}")
        self.connect_db()

        self.conn.isolation_level = None  # Disable transactions for VACUUM
        self.conn.execute("VACUUM")
        self.conn.isolation_level = ""  # Enable transactions back
        print(f"Vacuumed {self.db_name}")
