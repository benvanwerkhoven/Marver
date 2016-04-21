from __future__ import print_function

from ..context import fortran90
import re

def test_separate_comment_starter():
    my_string = "fancy fortran90 code with a !comment"
    output = fortran90.separate_comment_starter(my_string)

    assert "! " in output
    #test for non-whitespace chars directly following !-char
    assert re.search("!\S+", output) is None

def test_move_comments():
    pass

def test_remove_comments():
    my_string = """
    fancy Fortran90 code with ! a fancy comment
    ! every here and ! there
    """
    output = fortran90.remove_comments(my_string)

    #test no comments left
    assert re.search("!", output) is None
    #test if "fancy Fortran90 code with" is still in there along with whitespace
    assert re.search("\s+fancy Fortran90 code with\s+", output) is not None

def test_separate_parenthesis():
    my_string = "th()is is s(o((m))e) c(o+)mp(lic)))ated code"
    output = fortran90.separate_parenthesis(my_string)
    assert len(re.findall("\s\(\s", output)) == 6
    assert len(re.findall("\s\)\s", output)) == 8
    assert re.search("\S+\(\S+", output) is None
    assert re.search("\S+\)\S+", output) is None

def test_simplify_keywords():
    fortran_code = """
    do k=1, 10
      DO i=55, -1000
        if (do_not_replace_this->if) then
            call some_fancy_subroutine()
        else if (go else where ) then
            call someone_elses_subroutine()
        endif
      ENDDO
    enddo
    """
    output = fortran90.simplify_keywords(fortran_code)
    assert len(re.findall("\s\end\s", output)) == 3
    assert "END" not in output
    assert "elsewhere" in output
    assert "else where" not in output
    assert "elseif" in output
    assert "else if" not in output
    assert "(do_not_replace_this->if)" in output


def test_merge_multiline_statements():
    fortran_code = """ this is my&
    ! with a comment in between to make things even harder

    ! and some more, empty lines don't count either

    fancy multi-line s&
    &tatement, and I'm cool&   ! comments yo!
    with it&
    &"""
    fortran_code = re.sub(r"\r", "", fortran_code)

    expected = " this is my fancy multi-line statement, and I'm cool with it"

    output = fortran90.merge_multiline_statements(fortran_code)
    assert output == expected
    assert "&" not in output


def test_rename_type_casts():
    pass

def test_rename_typedefs():
    pass

def test_correct_oneliner_if():
    pass

def test_correct_oneliner_where():
    pass

def test_tokenize():
    pass

