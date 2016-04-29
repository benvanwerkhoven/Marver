import re
import os

from marver.parser.generic import read_away_parenthesized

def separate_comment_starter(inputstring):
    inputstring = re.sub(r"(!+)\S+", r"\1 ", inputstring)
    return inputstring

def move_comments(inputstring):
    """move comments around a bit to simplify parsing

    Move comments that have non-whitespace characters before them
    on the same line to some place that makes sense

    do not forget about full-line comments that follow a line continuation &, example
    A = 174.5 * Year   &
    !  this is a comment line
    + Count / 100
    if not moved here they will be removed by continuation character removal

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
    """type casts can be confused with variable declaration without lookahead"""
    def cast_or_not(matchobj):
        line = matchobj.group(0)
        #check if it is a declaration
        if re.search(r"\n\s*real", line, flags=re.IGNORECASE):
            return line
        else:
            #else, there are non-whitespace characters between 'real' and start of line
            #assume it is a type cast
            #check that no a-z0-9 char is right before 'real(' as a way to ensure 'real('
            #is not a substring of some variable or function name
            return re.sub(r"\n(.*?[^a-z0-9])real([ \t]*\()", r"\n\1 real_cast\2", line, flags=re.IGNORECASE)
    inputstring = re.sub(r"\n.*real[ \t]*\(", cast_or_not, inputstring, flags=re.IGNORECASE)

    return inputstring


def rename_typedefs(inputstring):
    """rename derived type definitions from type to typedef"""
    #replace variable declaration using a derived datatype with typeuse
    inputstring = re.sub(r"(\n[ \t]*)type([ \t]*\()", r"\1typeuse\2", inputstring, flags=re.IGNORECASE)
    #replace other occurences of type, that must be typedefs, with typedef
    inputstring = re.sub(r"(\n[ \t]*)type([ \t]+)", r"\1typedef\2", inputstring, flags=re.IGNORECASE)
    #also replace end type occurences with end typedef
    inputstring = re.sub(r"(\n[ \t]*)end type([ \t]+)", r"\1end typedef\2", inputstring, flags=re.IGNORECASE)
    #revert the temporary change from type to typeuse
    inputstring = re.sub(r"(\n[ \t]*)typeuse([ \t]*\()", r"\1type\2", inputstring, flags=re.IGNORECASE)

    return inputstring

def correct_oneliner_if(inputstring):
    """oneliner ifs is a code style we avoid as it complicates parsing"""
    #is it possible to have a oneliner elseif in fortran? not sure yet
    def one_liner(matchobject):
        line = matchobject.group(0)
        if re.search(r"\n\s*if[ \t]\(.*\).*then.*", line):
            return line
        else:
            if_and_condition, rest = read_away_parenthesized(line)
            return if_and_condition + " then\n " + rest + "\n end if"

    inputstring = re.sub(r"\n\s*if[ \t]\(.*\).*", one_liner, inputstring, flags=re.IGNORECASE)

    return inputstring

def correct_oneliner_where(inputstring):
    """oneliner where statement is a code style we avoid as it complicates parsing"""
    def check_non_whitespace(match):
        line = match.group(0)
        where_and_mask, rest = read_away_parenthesized(line)
        #if rest only contains white space or a comment
        if re.search(r"^\s*$", rest) or re.search(r"^\s*!.*$", rest):
            return line
        else:
            return where_and_mask + "\n " + rest + "\n end where"
    inputstring = re.sub(r"\n\s*where[ \t]*\(.*\).*", check_non_whitespace, inputstring, flags=re.IGNORECASE)

    return inputstring



