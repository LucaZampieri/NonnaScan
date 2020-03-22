#!/usr/bin/env python
from distutils.core import setup
from setuptools import setup, find_namespace_packages, wheel

NAME = "nonnascan"

with open("VERSION") as f:
    version = f.readline()

setup(
    name=NAME,
    version=version,
    description="Package to digitalize nonna's recipees.",
    author=["LucaZampieri"],
    author_email="luca.zampieri@protonmail.com",
    python_requires=">=3.6",
    package_data={"": ["*.o", "*.so", "*.cu.o", "*.pyc"]},
    packages=find_namespace_packages(include=[NAME, f"{NAME}.*"]),
    install_requires=["numpy", "sklearn", "pandas"],
)
