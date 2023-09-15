from sqlite3 import Connection, Cursor
import sqlite3
from typing import List, Union, Dict, Optional

from cameras_db.models.Camera import Camera


class CamerasController:
    cursor: Cursor
    conn: Connection

    def __init__(self, db_path: str, cursor: Optional[Cursor] = None):
        self.conn = sqlite3.connect(db_path)
        self.cursor = cursor if cursor is not None else self.conn.cursor()

    @staticmethod
    def row_to_camera(row=None, columns=None, row_dict=None) -> Camera:
        if row_dict is None:
            row_dict = {}
            for column_name, value in zip(columns, row):
                row_dict[column_name] = value
        else:
            corrected_row_dict = {}
            for column_tuple in columns:
                column_name = column_tuple[0]
                corrected_row_dict[column_name] = row_dict[column_tuple[0]]

            row_dict = corrected_row_dict

        return Camera(**row_dict)

    def get_by_field(self, field: str, value: Union[str, int, float]) -> List[Camera]:
        query = f"SELECT * FROM cameras WHERE {field} = ?"
        self.cursor.execute(
            query,
            (value,),
        )
        rows = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        cameras = [CamerasController.row_to_camera(row, columns) for row in rows]
        return cameras if cameras else []

    def get_by_field_like(self, field: str, value: str) -> List[Camera]:
        query = f"SELECT * FROM cameras WHERE {field} LIKE ?"
        self.cursor.execute(
            query,
            (
                "%{}%".format(value),
            ),  # Pass only one value with the % wildcard characters
        )
        rows = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        cameras = [CamerasController.row_to_camera(row, columns) for row in rows]
        return cameras if cameras else []

    def get_by_fields_like_and(self, field_value_dict: Dict[str, str]) -> List[Camera]:
        query_fields = [
            f"{field} LIKE ? COLLATE NOCASE" for field in field_value_dict.keys()
        ]
        query = "SELECT * FROM cameras WHERE " + " AND ".join(query_fields)
        params = [f"%{value}%" for value in field_value_dict.values()]

        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()
        columns = [column[0] for column in self.cursor.description]

        return [CamerasController.row_to_camera(row, columns) for row in rows] if rows else []

    def get_by_fields_like_or(self, field_value_dict: Dict[str, str]) -> List[Camera]:
        query_fields = [
            f"{field} LIKE ? COLLATE NOCASE" for field in field_value_dict.keys()
        ]
        query = "SELECT * FROM cameras WHERE " + " OR ".join(query_fields)
        params = [f"%{value}%" for value in field_value_dict.values()]

        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()
        columns = [column[0] for column in self.cursor.description]

        return [CamerasController.row_to_camera(row, columns) for row in rows] if rows else []

    def get_by_fields_with_operators(self, conditions):
        query = "SELECT * FROM cameras WHERE "
        query_conditions = []
        query_values = []

        for field, operator, value in conditions:
            query_conditions.append(f"{field} {operator} ?")
            query_values.append(value)

        query += " AND ".join(query_conditions)
        self.cursor.execute(query, query_values)

        # Fetch the rows and create a list to store the Camera objects
        cameras = []
        for row in self.cursor.fetchall():
            # Ensure column_name is a string

            row_dict = {str(column_name): row[i] for i, (column_name, *_) in enumerate(self.cursor.description)}

            camera = CamerasController.row_to_camera(row_dict=row_dict, columns=self.cursor.description)

            cameras.append(camera)

        return cameras

    def close(self):
        """
        Closes the connection.

        This function closes the connection to the database.

        Returns:
            None
        """
        self.conn.close()
