#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import setuptools
from distutils.core import setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

setup(  # pragma: no cover
    name="cc-pypackage",
    packages=[],
    version='0.2.3',
    description="My custom Cookiecutter template for a Python package.",
    long_description=readme,
    long_description_content_type="text/x-rst",
    author="Roberto Preste",
    license="BSD",
    author_email="roberto.preste@gmail.com",
    url="https://github.com/robertopreste/cc-pypackage",
    keywords=["cookiecutter", "template", "package", ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development",
    ],
)
