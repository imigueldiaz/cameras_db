from sqlite3 import Connection, Cursor
from unittest.mock import Mock

import cameras_db.models.Camera
import sqlite3
from typing import List, Union, Dict, Optional

from cameras_db.models.Camera import Camera


class CamerasController:
    cursor: Cursor
    conn: Connection

    def __init__(self, db_path: str, cursor: Optional[Cursor] = None):
        self.conn = sqlite3.connect(db_path)
        self.cursor = cursor if cursor is not None else self.conn.cursor()

    def row_to_camera(self, row, columns) -> Camera:
        row_dict = dict(zip(columns, row))
        print("Row dict:", row_dict)
        return Camera(**row_dict)

    def get_by_field(self, field: str, value: Union[str, int, float]) -> List[Camera]:
        query = f"SELECT * FROM cameras WHERE {field} = ?"
        self.cursor.execute(
            query,
            (value,),
        )
        rows = self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        cameras = [self.row_to_camera(row, columns) for row in rows]
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
        cameras = [self.row_to_camera(row, columns) for row in rows]
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

        return [self.row_to_camera(row, columns) for row in rows] if rows else []

    def get_by_fields_like_or(self, field_value_dict: Dict[str, str]) -> List[Camera]:
        query_fields = [
            f"{field} LIKE ? COLLATE NOCASE" for field in field_value_dict.keys()
        ]
        query = "SELECT * FROM cameras WHERE " + " OR ".join(query_fields)
        params = [f"%{value}%" for value in field_value_dict.values()]

        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()
        columns = [column[0] for column in self.cursor.description]

        return [self.row_to_camera(row, columns) for row in rows] if rows else []

    def get_by_fields_with_operators(
        self, field_value_dict: Dict[str, str], operators: Dict[str, str]
    ) -> List[Camera]:
        """
        Retrieves a list of Camera objects from the database based on the given field-value dictionary and operators.

        Parameters:
            field_value_dict (Dict[str, str]): A dictionary mapping field names to their corresponding values.
            operators (Dict[str, str]): A dictionary mapping field names to their corresponding operators.

        Returns:
            List[Camera]: A list of Camera objects that match the given field-value criteria.
            If no cameras match the criteria, an empty list is returned.
        """
        query_fields = []
        params = []

        for field, value in field_value_dict.items():
            operator = operators.get(field, "LIKE")  # Default operator is 'LIKE'
            if "LIKE" in operator.upper():
                value = f"%{value}%"  # Add wildcards for LIKE operator
            query_fields.append(f"{field} {operator} %s")
            params.append(value)

        query = "SELECT * FROM cameras WHERE " + " AND ".join(query_fields)

        self.cursor.execute(query, params)
        rows = self.cursor.fetchall()

        return [self.row_to_camera(row) for row in rows] if rows else []

    def close(self):
        """
        Closes the connection.

        This function closes the connection to the database.

        Returns:
            None
        """
        self.conn.close()
