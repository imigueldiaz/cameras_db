# Camera Database Setup Module

This Python package provides a module for setting up a SQLite database of DSLR and mirror-less cameras using a CSV file. The package is installable via `pip`.

## Generating a New Database

To generate a new SQLite database, follow these steps:

1. **Place the CSV file**: Copy the `cameras-all.csv` file into the `setup` module directory.

2. **Backup the existing database (recommended)**: Before generating a new database, it's recommended to create a backup of the existing `../cameras_db.db` file, as the database will be deleted and recreated from scratch during the process.

3. **Run the setup script**: Execute the `setup_db.py` script using Python:

```bash
python setup_db.py
```

This script uses `CameraCSVProcessor.py` and `CameraDBFiller.py` to generate a new SQLite database file named `cameras_db.db` in the parent directory.

## Customizing the Setup

If you want to change the names of the input CSV file, output database file, or table name, you can modify the following line in `setup_db.py`:

```python
main_workflow("cameras-all.csv", "../cameras_db.db", "cameras")
```

Make sure you know what you're doing before making any changes, as the author is not responsible for any consequences.

