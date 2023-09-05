# CameraCSVProcessor.py
# ... Your existing CameraCSVProcessor class
import os.path

# CameraDB.py
# ... Your existing CameraDB class

# utility.py
from CameraCSVProcessor import CameraCSVProcessor
from CameraDBFiller import CameraDBFiller
import json


def main_workflow(csv_file_path, db_name, table_name):
    # Step 1: Process the CSV file
    csv_processor = CameraCSVProcessor(csv_file_path)
    csv_processor.open_csv()
    json_string = csv_processor.convert_to_json()

    # Convert the JSON string back to a Python list
    camera_data = json.loads(json_string)

    # Step 2: Insert data into the database
    camera_db = CameraDBFiller(db_name, table_name, csv_file_path)
    camera_db.connect_db()
    camera_db.create_camera_table()
    camera_db.read_json_and_insert(camera_data)
    camera_db.close_db()
    camera_db.vacuum_db()


if __name__ == "__main__":
    if os.path.exists("../cameras_db.db"):
        os.remove("../cameras_db.db")
        print("Database removed")

    main_workflow("cameras-all.csv", "../cameras_db.db", "cameras")
