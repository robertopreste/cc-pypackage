#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import os


DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")


@pytest.fixture
def df():
    """Test df."""
    pass