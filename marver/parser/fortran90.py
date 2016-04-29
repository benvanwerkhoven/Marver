import re

from generic import starts_with
from tree import Node

def parse(inputstring, root=None):
    root = root or Node("root")

    inputstring = inputstring.strip()
    statements = inputstring.split("\n")

    last = root

    for line in statements:

        if starts_with(["if", "subroutine", "module", "do", "program"], line):
            n = Node(line)
            last.add_child(n)
            last = n

        elif re.search(r"^\s*end\s+.*", line):
            n = Node(line)
            last.add_child(n)
            last = last.parent

        else:
            last.add_child(Node(line))


    return root
