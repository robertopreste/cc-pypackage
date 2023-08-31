{% if cookiecutter.use_pytest == "y" -%}
import pytest
{%- endif %}
import os


DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")


{% if cookiecutter.use_pytest == "y" -%}
@pytest.fixture
def df():
    """Test df."""
    pass
{%- endif %}
