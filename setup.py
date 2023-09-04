from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.1"
DESCRIPTION = "A simple package to maintain and search over a SQLite database of DSLR and mirror-less cameras."

# Setting up
setup(
    name="cameras_db",
    version=VERSION,
    author="imigueldiaz (Ignacio de Miguel Diaz)",
    author_email="<imigueldiaz@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["sqlite3", "csv", "html", "re", "json"],
    keywords=[
        "python",
        "photography",
        "DSLR cameras",
        "mirror-less cameras",
        "database",
        "technical specifications",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
