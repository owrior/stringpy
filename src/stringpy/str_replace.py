import pandas as _pd
import re as _re
from .util import _compile, _replace

def str_replace(string, pattern, replace, count=1):
    if isinstance(string, _pd.Series):
        _pattern = _compile(pattern)
        def _pd_rep(x):
            return _replace(x, pattern, _pattern, replace, count)
        return string.apply(_pd_rep)
    elif isinstance(string, str):
        _pattern = _compile(pattern)
        string = _replace(string, pattern, _pattern, replace, count)
        return string
    else:
        raise ValueError("Please enter either a pandas series or a string.")

def str_replace_all(string, pattern, replace):
    if isinstance(string, _pd.Series):
        _pattern = _compile(pattern)
        def _pd_rep(x):
            return _replace(x, pattern, _pattern, replace, 0)
        return string.apply(_pd_rep)
    elif isinstance(string, str):
        _pattern = _compile(pattern)
        string = _replace(string, pattern, _pattern, replace, 0)
        return string
    else:
        raise ValueError("Please enter either a pandas series or a string.")
