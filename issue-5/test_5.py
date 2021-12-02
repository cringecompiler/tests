import io
from unittest.mock import patch

import pytest

from what_is_year_now import what_is_year_now
import urllib.request


def test_ymd():
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO('{"currentDateTime": "2019-03-01"}')):
        actual = what_is_year_now()
        exp = 2019
        assert actual == exp


def test_dmy():
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO('{"currentDateTime": "01.03.2019"}')):
        actual = what_is_year_now()
        exp = 2019
        assert actual == exp


def test_ex():
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO('{"currentDateTime": "20190303"}')):
        with pytest.raises(ValueError):
            what_is_year_now()
