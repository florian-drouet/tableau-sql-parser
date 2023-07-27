from tableau_sql_parser.utils import tree_output

test_input = [
    "a.b",
    "a.b.c",
    "a.b.c.d",
    "f",
    "f.g",
    "h.i.j",
]

expected = """a
|--b
|--|--c
|--|--|--d
f
|--g
h
|--i
|--|--j
"""


def test__flatten_values():
    assert tree_output(test_input) == expected
