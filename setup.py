#!/usr/bin/env python3

from setuptools import setup
import setuptools
from setuptools.command.install_lib import install_lib
import distutils
import os
import sys


PACKAGE_NAME = "python_example_project_boilerplate"
AUTHORS = ""
MAIl = ""
# We store our version number in a simple text file:
# version_path = os.path.abspath(os.path.join(os.path.dirname(__file__), PACKAGE_NAME, "version.txt"))
# with open(version_path, "r") as version_file:
#    version = version_file.read().strip()


setup(
    name=PACKAGE_NAME,
    #    version=version,
    packages=[PACKAGE_NAME],
    package_dir={PACKAGE_NAME: ""},
    description="",
    package_data={},
    exclude_package_data={"": ["Documentation"]},
    requires=[],
    long_description="",
    author=AUTHORS,
    author_email=MAIl,
    url="",
    license="",
    platforms="",
    classifiers=["Development Status :: 4 - Beta", "Environment :: Console"],
)
