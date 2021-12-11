import pytest
from what_is_year import what_is_year_now
from unittest.mock import patch
import urllib.request
import json


def test_year():
    exp_year = 2021
    with patch.object(urllib.request, 'urlopen'):
        with patch.object(json, 'load', return_value={'currentDateTime': '2021-12-11'}):
            actual = what_is_year_now()

    assert actual == exp_year


def test_exception():
    with patch.object(urllib.request, 'urlopen'):
        with patch.object(json, 'load', return_value={'currentDateTime': '2021.12.11'}):
            with pytest.raises(ValueError):
                what_is_year_now()
