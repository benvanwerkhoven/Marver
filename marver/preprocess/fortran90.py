import re
import os


def separate_comment_starter(inputstring):
    return inputstring.replace("!", "! ")

def move_comments(inputstring):
    """move comments around a bit to simplify parsing

    Move comments that have non-whitespace characters before them
    on the same line to some place that makes sense

    do not forget about full-line comments taht follow a line continuation &, example
    A = 174.5 * Year   &
    !  this is a comment line
    + Count / 100


    """
    pass

def remove_comments(inputstring):
    """removes all comments, intended for testing during development"""
    return re.sub("!.*", "", inputstring)

def separate_parenthesis(inputstring):
    return inputstring.replace("(", " ( ").replace(")", " ) ")

def simplify_keywords(inputstring):
    """reduce the number of allowed keywords in Fortran 90"""
    dirname = os.path.dirname(os.path.abspath(__file__)) + "/files/"
    with open(dirname + 'fortran90_keywords_wrong.txt', 'r') as f:
        wrong = f.read().strip().split('\n')
    with open(dirname + 'fortran90_keywords_right.txt', 'r') as f:
        right = f.read().strip().split('\n')

    #replace all instances of wrong keywords with the right keywords
    for (old,new) in zip(wrong,right):
        inputstring = re.sub(r"(\s)" + old + r"(\s)", r"\1" + new + r"\2", inputstring, flags=re.IGNORECASE)

    return inputstring


def merge_multiline_statements(inputstring):
    #remove comments that are mid-statement due to line continuation
    inputstring = re.sub(r"&\s*(!.*\s*)+", "&\n", inputstring)
    #remove continuation pairs
    inputstring = re.sub(r"&(\s*)&", "", inputstring)
    #finally, replace line continuation marker and end-of-line pair with space
    inputstring = re.sub(r"&\s*", " ", inputstring)

    return inputstring

def rename_type_casts(inputstring):
    pass

def rename_typedefs(inputstring):
    """rename typedefs from 'type' to 'typedef', don't forget 'end typedef' """
    pass

def correct_oneliner_if(inputstring):
    """oneliner ifs is a code style we avoid as it complicates parsing"""
    pass

def correct_oneliner_where(inputstring):
    pass

def tokenize(inputstring):
    """tokenize based on space, retain end-of-line somehow"""
    pass


