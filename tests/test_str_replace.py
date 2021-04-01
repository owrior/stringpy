import pytest
import pandas as pd
from pandas._testing import assert_frame_equal
from stringpy.str_replace import *


def test_str_replace_str():
    string = "The cat sat in the hat."
    pattern = r'at'
    assert str_replace(string, r'at', "") == "The c sat in the hat."
    
def test_str_replace_df():
    df = pd.DataFrame({
        'A': ["Cat hat", "Fat cat", "Foot hoot"]
    })
    df_test = pd.DataFrame({
        'A': ["Cat hat", "Fat cat", "Foot hoot"],
        'B': ["C hat", "F cat", "Foot hoot"]
    })
    pattern = r'at'
    df['B'] = str_replace(df['A'], r'at', "")
    assert assert_frame_equal(df, df_test) is None

def test_str_replace_all_str():
    string = "The cat sat in the hat."
    pattern = r'at'
    assert str_replace_all(string, r'at', "") == "The c s in the h."
    
def test_str_replace_all_df():
    df = pd.DataFrame({
        'A': ["Cat hat", "Fat cat", "Foot hoot"]
    })
    df_test = pd.DataFrame({
        'A': ["Cat hat", "Fat cat", "Foot hoot"],
        'B': ["C h", "F c", "Foot hoot"]
    })
    pattern = r'at'
    df['B'] = str_replace_all(df['A'], r'at', "")
    assert assert_frame_equal(df, df_test) is None