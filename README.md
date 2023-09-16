

# cameras-db

## About

`cameras-db` is a Python package that offers a powerful SQLite3 database stocked with technical specifications for roughly 3,500 DSLR and mirrorless cameras. Out of the box, you get a `Camera` class and a `CamerasController` for effortless, search-only database interaction. Extend your data collection effortlessly with CSV imports.

## Topics

`python` `pip-package` `sqlite3` `dslr` `mirrorless-cameras` `camera-specifications` `search-api` `csv-import` `data-management`

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Extending the Database](#extending-the-database)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

To install `cameras-db`, run the following command:

```bash
pip install cameras-db
```

## Usage

Initializing the `CamerasController` and searching is straightforward:

```python
from cameras_db.controllers import CamerasController

# Initialize the controller
controller = CamerasController()

# Search by brand and model
camera = controller.get_by_fields_like_and({"brand": "Canon", "model": "EOS 5D"})
```
The controller search API is a bit rough still, but I plan to improve it to be more human-like. 

---

## Extending the Database

Have a CSV file with fresh camera models and specs? Extend the database pasting it at the `setup` folder and executing from the command line:

```shell
python ./setup_db.py
```
A `README.md` file is provided within the folder with more precise instructions.

---

## Contributing

All contributions are welcome. To get started, fork this repository and submit your pull request.

---

## License

This project is licensed under the GNU General Public License v3.0. For full license information, please see the `LICENSE` file.

