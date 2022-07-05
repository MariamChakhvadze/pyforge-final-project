import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

import pytest
import requests

from compound_loader import CompoundLoader
from main import get
from utils import available_compounds


@pytest.fixture
def default_compound_loader() -> CompoundLoader:
    """Creates CompoundLoader instance for testing purposes.

    Returns:
        CompoundLoader: instance of compound loader
    """
    return CompoundLoader(available_compounds)


def test_empty_input(default_compound_loader):
    with pytest.raises(SystemExit):
        default_compound_loader.get_compound_summary("")


def test_correct_input(requests_mock):
    url = "https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/ADP"
    requests_mock.get(url, text="passed")
    assert "passed" == requests.get(url).text


def test_incorrect_input(default_compound_loader):
    with pytest.raises(SystemExit):
        default_compound_loader.get_compound_summary("INC")
