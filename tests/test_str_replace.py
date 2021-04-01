import pytest
import pandas as pd
from pandas._testing import assert_frame_equal
from stringpy.str_replace import str_replace


def test_str_replace_str():
    string = "The cat sat in the hat."
    pattern = r'at'
    final = str_replace(string, r'at', "")
    assert str_replace(string, r'at', "") == "The c sat in the hat."
    
def test_str_replace_df():
    df = pd.DataFrame({
        'A': ["Cat", "Fat", "Foot"]
    })
    df_test = pd.DataFrame({
        'A': ["Cat", "Fat", "Foot"],
        'B': ["C", "F", "Foot"]
    })
    pattern = r'at'
    df['B'] = str_replace(df['A'], r'at', "")
    assert assert_frame_equal(df, df_test) is None