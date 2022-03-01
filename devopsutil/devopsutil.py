import re


def number(str):
    try:
        if re.match("^[-]?\d*\.\d*$", str):  # int(str) == float(str):
            return float(str)
        else:
            return int(str)
    except ValueError:
        return str
