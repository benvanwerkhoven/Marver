from __future__ import print_function
import re

from ..context import marver
from marver.preprocess import generic

def test_get_rid_of_carriage_returns():
    string = "this is some text with \r carriage returns \r\n"
    expect = "this is some text with  carriage returns \n"
    output = generic.get_rid_of_carriage_returns(string)
    print(output)
    assert output == expect

def test_collapse_whitespace():
    string = " this     is \t \t  my  \t fancy \t string \n\n\n with \n \t \n \t \n \t lots of whitespace"
    expect = " this is my fancy string\nwith\nlots of whitespace"
    output = generic.collapse_whitespace(string)
    print(output)
    assert output == expect
