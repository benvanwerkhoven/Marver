""" Marver's main user interface module

"""
import parser.fortran90


def open_file(filename):
    """just reads the file contents into a string"""
    with open(filename, 'r') as f:
        return f.read()


def parse(inputstring, lang="Fortran90"):
    if lang == "Fortran90":
        return parser.fortran90.parse(inputstring)



