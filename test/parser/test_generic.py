from __future__ import print_function
import re

from ..context import marver
from marver.parser import generic


def test_read_away_parenthesized():

    fortran_code = "if (C(i) - D(i) > 1e-6) write (*,*) 'error at ', i, 'C(i)=', C(i), 'D(i)=', D(i)"
    expected1 = "if (C(i) - D(i) > 1e-6)"
    expected2 = " write (*,*) 'error at ', i, 'C(i)=', C(i), 'D(i)=', D(i)"

    output1, output2 = generic.read_away_parenthesized(fortran_code)
    print(output1)
    print(output2)

    assert output1 == expected1
    assert output2 == expected2
