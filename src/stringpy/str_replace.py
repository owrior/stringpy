import pandas as _pd
import re as _re

def _compile(pattern):
    if isinstance(pattern, dict):
        pattern = dict((_re.escape(k), v) for k, v in pattern.items()) 
        _pattern = _re.compile("|".join(pattern.keys()))
    elif isinstance(pattern, str):
        _pattern = _re.compile(pattern)
    else:
        raise ValueError("Please enter either a string or dict for pattern.")
    return _pattern

def _replace(string, pattern, _pattern, replace, count):
    if isinstance(pattern, dict):
        string = _pattern.sub(lambda m: _rep[_re.escape(m.group(0))], string, count)
    elif isinstance(pattern, str):
        string = _pattern.sub(replace, string, count)
    else:
        raise ValueError("Please enter either a string or dict for pattern.")
    return string

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
