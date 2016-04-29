""" Marver's main user interface module

"""


def open_file(filename):
    """just reads the file contents into a string"""
    with open(filename, 'r') as f:
        return f.read()






