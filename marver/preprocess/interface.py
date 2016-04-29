from fortran90 import *
from generic import *


def preprocess(inputstring):
    """Implements the Fortran90 preprocessor"""

    inputstring = get_rid_of_carriage_returns(inputstring)

    inputstring = separate_comment_starter(inputstring)

    inputstring = remove_comments(inputstring)

    inputstring = separate_parenthesis(inputstring)

    inputstring = simplify_keywords(inputstring)

    inputstring = merge_multiline_statements(inputstring)

    inputstring = rename_type_casts(inputstring)

    inputstring = rename_typedefs(inputstring)

    inputstring = correct_oneliner_if(inputstring)

    inputstring = correct_oneliner_where(inputstring)

    inputstring = collapse_whitespace(inputstring)

    return inputstring

