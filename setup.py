"""
Install this library locally without copying files by running this pip command:

pip install -e /path/to/the/folder/with/this/file

On Linux you might want to install for the local user only:

pip install --user -e /path/to/the/folder/with/this/file

"""

import setuptools


setuptools.setup(
    name="myproject",
    version="0.1",
    packages=setuptools.find_packages(),
)
