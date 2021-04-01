import pytest
import pandas as pd
from pandas._testing import assert_frame_equal
from stringpy.str_detect import *


def test_str_replace_str():
    string = "The cat sat in the hat."
    assert str_detect(string, r'at')
    
def test_str_replace_df():
    df = pd.DataFrame({
        'A': ["Cat hat", "Fat cat", "Foot hoot"]
    })
    df_test = pd.DataFrame({
        'A': ["Cat hat", "Fat cat", "Foot hoot"],
        'B': [True, True, False]
    })
    df['B'] = str_detect(df['A'], r'at')
    assert assert_frame_equal(df, df_test) is None