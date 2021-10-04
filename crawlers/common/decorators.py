import functools
import re


def sanitize(func):
    def replace_space(t):
        if t.isspace() and t != ' ':
            return ' '
        return t

    def sanitized(t):
        if type(t) == list:
            return list(map(sanitized, t))
        elif type(t) == dict:
            tt = {}
            for k in t:
                tt[sanitized(k)] = sanitized(t[k])
            return tt
        elif type(t) == str:
            t = ''.join(map(replace_space, t))
            t = t.strip()
            t = t.replace('\n', ' ').replace('\t', ' ').replace('\r', ' ').replace('\xa0', ' ')
            t = re.sub(' +', ' ', t)
            return t
        else:
            return t

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)
        modified_result = sanitized(original_result)
        return modified_result

    return wrapper
