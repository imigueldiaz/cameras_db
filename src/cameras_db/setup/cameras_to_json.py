import os.path
import sqlite3
import json

def main():
    
    # Create a connection to the database
    camera_db = sqlite3.connect("../cameras_db.db")
    cursor = camera_db.cursor()

    #get field names
    cursor.execute("PRAGMA table_info(cameras)")
    field_names = cursor.fetchall()

    cursor.execute("SELECT * FROM cameras")
    rows = cursor.fetchall()

    # Dump the data to a JSON file avoiding nulls
    with open("cameras.json", "w") as f:
        json.dump(
            [
                {
                    field[1]: value
                    for field, value in zip(field_names, row)
                    if value is not None
                }
                for row in rows
            ],
            f,
            indent=4,
            sort_keys=True,
        )
    cursor.close()
    camera_db.close()

    print(f"Data dumped to cameras.json, {len(rows)} rows.")

if __name__ == '__main__':
    main()
