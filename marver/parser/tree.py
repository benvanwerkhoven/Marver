import re

class Node(object):
    """Main tree class for the code block tree

    This class is the backbone of the code block tree.
    To keep things simple I have so far not made any special
    types of nodes for different types of code blocks, such as
    loops, if-then-else, and so on
    """

    def __init__(self, value):
        self.child = []
        self.parent = None
        self.value = value.strip()

    def add_child(self, c):
        self.child.append(c)
        c.parent = self
        return c

    def set_children(self, children):
        self.child = children
        for c in self.child:
            c.parent = self

    def __str__(self):
        """simple output formatter function"""
        string = "-> " + self.value + "\n"
        for c in self.child:
            string += "   " + re.sub(r"\n", r"\n   ", str(c)).strip() + "\n"
        return string

