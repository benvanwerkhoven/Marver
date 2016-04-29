import re

def get_rid_of_carriage_returns(inputstring):
    return inputstring.replace("\r", "")

def collapse_whitespace(inputstring):
    """merge all consecutive whitespace into single space or end-of-line"""
    inputstring = re.sub(r"[ \t]+", r" ", inputstring)
    inputstring = re.sub(r"[ \t]*\n", r"\n", inputstring)
    inputstring = re.sub("\n[ \t]+", "\n", inputstring)
    inputstring = re.sub("\n+", "\n", inputstring)
    return inputstring
