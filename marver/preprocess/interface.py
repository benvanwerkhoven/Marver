from fortran90 import *
from generic import *



class Fortran90Preprocessor(object):
    """Implements the Fortran90 preprocessor"""

    def preprocess(inputstring):

        get_rid_of_carriage_returns(inputstring)

        separate_comment_starter(inputstring)

        move_comments(inputstring)

        remove_comments(inputstring)

        separate_parenthesis(inputsting)

        simplify_keywords(inputstring)

        merge_multiline_statements(inputstring)

        rename_type_casts(inputstring)

        rename_typedefs(inputstring)

        correct_oneliner_if(inputstring)

        correct_oneliner_where(inputstring)

        collapse_whitespace(inputstring)

        return inputstring

