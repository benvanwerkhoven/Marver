from __future__ import print_function
import re

from ..context import marver
from marver.parser.tree import Node

def test_init():
    n = Node("test")
    assert isinstance(n, Node)

def test_add_child():
    p = Node("parent")
    c = Node("child")
    p.add_child(c)
    assert c.parent == p
    assert c in p.child

def test_set_children():
    p = Node("parent")
    c1 = Node("child")
    c2 = Node("child")
    p.set_children([c1,c2])
    assert c1.parent == p
    assert c2.parent == p
    assert c1 in p.child
    assert c2 in p.child

def test_str():
    p = Node("parent")
    c1 = Node("child")
    p.child = [c1]
    expect = "-> parent\n   -> child\n"
    output = str(p)
    print(output)
    assert output == expect
