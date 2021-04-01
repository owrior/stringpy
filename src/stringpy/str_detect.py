import pandas as _pd
import re as _re
from .util import _compile, _detect

def str_detect(string, pattern):
    if isinstance(pattern, dict):
        raise ValueError("Dict cannot be used for detect.")

    if isinstance(string, _pd.Series):
        _pattern = _compile(pattern)
        def _pd_det(x):
            return _detect(x, _pattern)
        return string.apply(_pd_det)
    elif isinstance(string, str):
        _pattern = _compile(pattern)
        string = _detect(string, _pattern)
        return string
    else:
        raise ValueError("Please enter either a pandas series or a string.")