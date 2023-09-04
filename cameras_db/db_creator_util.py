import sqlite3
import json

JSON_FILE_PATH = "cameras.json"
DB_NAME = "cameras.db"
TABLE_NAME = "cameras"


def read_json():
    with open(JSON_FILE_PATH, "r") as f:
        cameras = json.load(f)
    return cameras


# Connect to the SQLite database (this will create a new file called "cameras.db")
conn = sqlite3.connect("cameras.db")
c = conn.cursor()

# Create the table schema for the camera data
c.execute(
    """
CREATE TABLE cameras (
    url TEXT,
    image_url TEXT,
    brand TEXT,
    model TEXT,
    also_known_as TEXT,
    year INTEGER,
    megapixels REAL,
    effective_megapixels REAL,
    total_megapixels REAL,
    sensor_size TEXT,
    sensor_type TEXT,
    sensor_resolution TEXT,
    max_image_resolution TEXT,
    crop_factor REAL,
    optical_zoom REAL,
    digital_zoom INTEGER,
    iso TEXT,
    raw_support INTEGER,
    manual_focus INTEGER,
    normal_focus_range TEXT,
    macro_focus_range TEXT,
    focal_length_35mm_equiv TEXT,
    aperture_priority INTEGER,
    max_aperture TEXT,
    max_aperture_35mm_equiv TEXT,
    depth_of_field TEXT,
    metering TEXT,
    exposure_compensation TEXT,
    shutter_priority INTEGER,
    min_shutter_speed TEXT,
    max_shutter_speed TEXT,
    built_in_flash INTEGER,
    external_flash INTEGER,
    viewfinder TEXT,
    white_balance_presets INTEGER,
    screen_size TEXT,
    screen_resolution TEXT,
    video_capture INTEGER,
    max_video_resolution TEXT,
    storage_types TEXT,
    usb TEXT,
    hdmi INTEGER,
    wireless INTEGER,
    gps TEXT,
    battery TEXT,
    weight REAL,
    dimensions TEXT,
    sensor_size_w REAL,
    sensor_size_h REAL,
    sensor_px_w INTEGER,
    sensor_px_h INTEGER
)
"""
)


def insert_cameras(cameras):
    for camera in cameras:
        c.execute(
            """
        INSERT INTO cameras 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                camera["url"],
                camera["image_url"],
                camera["brand"],
                camera["model"],
                camera["also_known_as"],
                camera["year"],
                camera["megapixels"],
                camera["effective_megapixels"],
                camera["total_megapixels"],
                camera["sensor_size"],
                camera["sensor_type"],
                camera["sensor_resolution"],
                camera["max_image_resolution"],
                camera["crop_factor"],
                camera["optical_zoom"],
                camera["digital_zoom"],
                camera["iso"],
                camera["raw_support"],
                camera["manual_focus"],
                camera["normal_focus_range"],
                camera["macro_focus_range"],
                camera["focal_length_35mm_equiv"],
                camera["aperture_priority"],
                camera["max_aperture"],
                camera["max_aperture_35mm_equiv"],
                camera["depth_of_field"],
                camera["metering"],
                camera["exposure_compensation"],
                camera["shutter_priority"],
                camera["min_shutter_speed"],
                camera["max_shutter_speed"],
                camera["built_in_flash"],
                camera["external_flash"],
                camera["viewfinder"],
                camera["white_balance_presets"],
                camera["screen_size"],
                camera["screen_resolution"],
                camera["video_capture"],
                camera["max_video_resolution"],
                camera["storage_types"],
                camera["usb"],
                camera["hdmi"],
                camera["wireless"],
                camera["gps"],
                camera["battery"],
                camera["weight"],
                camera["dimensions"],
                camera["sensor_size_w"],
                camera["sensor_size_h"],
                camera["sensor_px_w"],
                camera["sensor_px_h"],
            ),
        )

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
