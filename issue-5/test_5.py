from what_is_year_now import what_is_year_now
import pytest


def test_norm():
    actual = what_is_year_now()
    exp = 2021
    assert actual == exp


def test_ex():
    with pytest.raises(Exception):
        what_is_year_now(2)
