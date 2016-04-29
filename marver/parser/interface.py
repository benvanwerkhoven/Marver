
import fortran90


def parse(inputstring, lang="Fortran90"):
    if lang == "Fortran90":
        return fortran90.parse(inputstring)
