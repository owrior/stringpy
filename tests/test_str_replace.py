import pytest
import pandas as pd
from pandas._testing import assert_frame_equal
from stringpy.str_replace import str_replace


def test_str_replace_str():
    string = "The cat sat in the hat."
    pattern = r'at'
    final = str_replace(string, r'at', "")
    print(final)
    assert str_replace(string, r'at', "") == "The c sat in the hat."
    