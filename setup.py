# setup.py  
# This file is part of pyguinea.
# pyguinea is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.

# pyguinea is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with Frommle; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

# Author Amin Shakya (a.shakya@utwente.nl), 2023
import setuptools
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pyguinea",
    author="Amin Shakya",
    author_email="aminshk50@gmail.com",
    version="0.0.1",
    description="pyguinea: a test python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mn5hk/pyguinea",
    packages=find_packages("."),
    package_dir={"":"."},
    #scripts=['clitools/geoslurper.py'],
    install_requires=['numpy', 'SQLAlchemy', 'pycurl', 'cryptography', 'PyYAML','lxml','keyring','pandas','motuclient','netCDF4','Shapely', 'GeoAlchemy2', 'psycopg2'],
    classifiers=["Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Science/Research",
        "Development Status :: 4 - Beta"]
    
)
