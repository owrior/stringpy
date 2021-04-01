import pandas as _pd
import re as _re


def str_replace(string, pattern, replace):
    if isinstance(pattern, dict):
        pattern = dict((_re.escape(k), v) for k, v in pattern.items()) 
        pattern = _re.compile("|".join(pattern.keys()))
        string = pattern.sub(lambda m: _rep[_re.escape(m.group(0))], string, 1)
    elif isinstance(pattern, str):
        string = _re.sub(pattern, replace, string, 1)
    else:
        raise ValueError("Please enter either a string or dict for pattern.")
    return string

def str_replace_all(string, pattern, replace):
    if isinstance(pattern, dict):
        pattern = dict((_re.escape(k), v) for k, v in pattern.items()) 
        pattern = _re.compile("|".join(pattern.keys()))
        string = pattern.sub(lambda m: rep[_re.escape(m.group(0))], string)
    elif isinstance(pattern, str):
        string = _re.sub(pattern, replace, string)
    else:
        raise ValueError("Please enter either a string or dict for pattern.")
    return string