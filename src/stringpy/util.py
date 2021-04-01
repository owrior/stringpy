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