import csv
import json
import re
from html import unescape
from typing import Dict


class CameraCSVProcessor:
    def __init__(self, csv_file_path: str):
        self.csv_file_path = csv_file_path
        self.json_data = []
        self.fieldnames = []

    def open_csv(self) -> None:
        """
        Opens a CSV file and reads its contents.

        Parameters:
            self (CameraCSVProcessor): The instance of the class.

        Returns:
            None
        """
        with open(self.csv_file_path, mode="r", encoding="utf-8") as csvfile:
            csvreader = csv.DictReader(csvfile, delimiter=";")
            self.fieldnames = [
                field.lower().replace(" ", "_") for field in csvreader.fieldnames
            ]

            row: Dict[str, str]
            for row in csvreader:
                self.treat_fields(row)

        print(f"File opened and read: {self.csv_file_path}")

    def treat_fields(self, row: Dict[str, str]) -> None:
        """
        Treats the fields of a given row dictionary.

        Args:
            row (Dict[str, str]): The dictionary representing a row of data, with field names as keys and values
            as values.

        Returns:
            None

        Description:
            This function treats the fields of the given row dictionary by performing various transformations
            on specific fields.

            The function creates a new dictionary, `new_row`, where each field name is transformed according
            to the specific rules.

            The function performs the following transformations:

            1. Focal Length Transformation:
               - If the field "focal_length_(35mm_equiv.)" exists in `row`, the function stores its value
               in the field "focal_length_35" of `new_row` and deletes the original field.

            2. Max Aperture Transformation:
               - If the field "max._aperture_(35mm_equiv.)" exists in `row`, the function stores its value
               in the field "max_aperture_35" of `new_row` and deletes the original field.

            3. Sensor Size Transformation:
               - If the field "sensor_size" exists in `new_row`, the function searches for a pattern of
               two decimal numbers separated by "x" in the field's value.
               - If a match is found, the function stores the first decimal number
               in the field "sensor_size_w" of `new_row`
               and the second decimal number in the field "sensor_size_h" of `new_row`.

            4. Sensor Resolution Transformation:
               - If the field "sensor_resolution" exists in `new_row`, the function searches for all decimal numbers
                in the field's value.
               - If at least two decimal numbers are found, the function stores the first decimal number
               in the field "sensor_px_w" of `new_row` and the second decimal number in the field "sensor_px_h" of `new_row`.

            5. ISO Transformation:
               - If the field "iso" exists in `new_row`, the function splits its value by commas
               and stores the resulting list in the field "iso" of `new_row`.

            6. Boolean Transformations:
               - For each key-value pair in `new_row`, if the value is "Yes" or "yes",
               the function replaces the value with `True`.
               - If the value is "No" or "no", the function replaces the value with `False`.

            Finally, the function appends `new_row` to the `json_data` list of the calling object.
        """
        new_row = {
            self.fieldnames[int(i)]: unescape(value.strip()) if value else None
            for i, (key, value) in enumerate(row.items())
        }

        # Focal Length Transformation
        focal_length = row.get("focal_length_(35mm_equiv.)")
        if focal_length:
            new_row["focal_length_35"] = focal_length
            del new_row["focal_length_(35mm_equiv.)"]

        # Max Aperture Transformation
        max_aperture = row.get("max._aperture_(35mm_equiv.)")
        if max_aperture:
            new_row["max_aperture_35"] = max_aperture
            del new_row["max._aperture_(35mm_equiv.)"]

        # Sensor Size Transformation
        sensor_size = new_row.get("sensor_size")
        if sensor_size:
            sensor_size_match = re.search(r"([\d.]+) x ([\d.]+)", sensor_size)
            if sensor_size_match:
                new_row["sensor_size_w"] = float(sensor_size_match.group(1))
                new_row["sensor_size_h"] = float(sensor_size_match.group(2))

        # Sensor Resolution Transformation
        sensor_resolution = new_row.get("sensor_resolution")
        if sensor_resolution:
            matches = re.findall(r"\d+\.\d+|\d+", sensor_resolution)
            if len(matches) > 1:
                new_row["sensor_px_w"] = int(matches[0])
                new_row["sensor_px_h"] = int(matches[1])

        # ISO Transformation
        iso = new_row.get("iso")
        if iso:
            new_row["iso"] = [x.strip() for x in iso.split(",")]

        # Boolean Transformations
        for key, value in new_row.items():
            if value == "Yes" or value == "yes":
                new_row[key] = True
            elif value == "No" or value == "no":
                new_row[key] = False

        self.json_data.append(new_row)

    def convert_to_json(self) -> str:
        """
        Convert the object to a JSON string representation.

        Returns:
            str: The JSON string representation of the object.
        """
        return json.dumps(self.json_data, ensure_ascii=False, indent=4)
