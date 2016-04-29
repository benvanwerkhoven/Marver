from __future__ import print_function
import re

from ..context import marver
from marver.preprocess import fortran90

def test_separate_comment_starter():
    my_string = "fancy fortran90 code with a !!comment"
    output = fortran90.separate_comment_starter(my_string)
    print(output)
    assert "! " in output
    #test for non-whitespace non-! chars directly following !-char
    assert re.search("!\[^ \t\n\r\f\v!]+", output) is None

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
    expected = "th (  ) is is s ( o (  ( m )  ) e )  c ( o+ ) mp ( lic )  )  ) ated code"
    output = fortran90.separate_parenthesis(my_string)
    assert len(re.findall("\s\(\s", output)) == 6
    assert len(re.findall("\s\)\s", output)) == 8
    assert re.search("\S+\(\S+", output) is None
    assert re.search("\S+\)\S+", output) is None
    assert output == expected

def test_simplify_keywords():
    fortran_code = """ fortran
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
    fortran_code = """ fortran
    real (c_double) :: a, b, c
    a = b*real(c)
    d = my_fortran_is_surreal(b)
    """
    expected = """ fortran
    real (c_double) :: a, b, c
    a = b* real_cast(c)
    d = my_fortran_is_surreal(b)
    """
    output = fortran90.rename_type_casts(fortran_code)
    print(output)
    assert output == expected

def test_rename_typedefs():
    fortran_code = """ fancy Fortran type def
    TYPE :: fancy_type
      CHARACTER(15) :: name
      REAL ::          f        ! real in my fancy type
      INTEGER ::       i
    END TYPE fancy_type
    type(fancy_type) :: array_of_my_cool_type(30)
    """
    expected = """ fancy Fortran type def
    typedef :: fancy_type
      CHARACTER(15) :: name
      REAL ::          f        ! real in my fancy type
      INTEGER ::       i
    end typedef fancy_type
    type(fancy_type) :: array_of_my_cool_type(30)
    """
    output = fortran90.rename_typedefs(fortran_code)
    print(output)
    assert output == expected

def test_correct_oneliner_if():
    fortran_code = """ fortran
    if (nice) then
        do something awesome
    endif
    if (not_ ( so ) ( ) _nice) do something evil
    """
    expected = """ fortran
    if (nice) then
        do something awesome
    endif
    if (not_ ( so ) ( ) _nice) then
 do something evil
end if
    """
    output = fortran90.correct_oneliner_if(fortran_code)
    print(output)
    assert output == expected

def test_correct_oneliner_if2():
    fortran_code = "\nif (C(i) - D(i) > 1e-6) write (*,*) 'error at ', i, 'C(i)=', C(i), 'D(i)=', D(i)"
    expected = "\nif (C(i) - D(i) > 1e-6) then\n write (*,*) 'error at ', i, 'C(i)=', C(i), 'D(i)=', D(i)\nend if"

    output = fortran90.correct_oneliner_if(fortran_code)
    print(output)
    assert output == expected

def test_correct_oneliner_where():
    fortran_code = """ fortran
    where (mask_expression)
        do something in construct
    elsewhere (mask_expression)
        do something else
    end where
    where (mask_expression) do something in statement
    where (mask_expression) ! comment
        do something in construct
    end where
    """
    expected = """ fortran
    where (mask_expression)
        do something in construct
    elsewhere (mask_expression)
        do something else
    end where
    where (mask_expression)
  do something in statement
 end where
    where (mask_expression) ! comment
        do something in construct
    end where
    """
    output = fortran90.correct_oneliner_where(fortran_code)
    print(output)
    assert output == expected


def test_tokenize():
    pass











