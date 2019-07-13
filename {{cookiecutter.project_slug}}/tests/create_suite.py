#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
{% if cookiecutter.use_pytest == "y" -%}
import pytest
{% else %}
import unittest
{%- endif %}
import os


DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")


def main():
    """Create the test files needed."""
    pass


if __name__ == '__main__':
    main()
