from src.tableau_sql_parser.recursive_search import RecursiveSearch
import pytest
import sqlfluff


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (["1", "2", "foo"], "1 2 foo"),
        (["1", "2", "   foo  ", "", " "], "1 2 foo"),
        (["  foo", "bar  ", "1"], "foo bar 1")
    ],
)
def test__get_dict_values(test_input, expected):
    assert RecursiveSearch._get_dict_values(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ([{'foo': '1'}, {'bar': '2'}, {'test': '3'}], "123"),
        ([{'foo': '1 '}, {'bar': ' 2'}, {'test': ' 3 '}], "123"),
        ({'foo': 'bar'}, "bar")
    ],
)
def test__extract_elements(test_input, expected):
    assert RecursiveSearch._extract_elements(test_input) == expected

sql_query = """
WITH cte AS (
    SELECT
        t.foo,
        t.test
    FROM
        schema.table AS t
)

SELECT
    c.foo,
    c.test,
    tt.bar
FROM
    cte AS c
    LEFT JOIN schema.table2 AS tt ON c.foo = tt.foo
"""
parsed_query = sqlfluff.parse(sql=sql_query)
expected_output = {
    40: ['t.foo', 'column'],
    55: ['t.test', 'column'],
    69: ['schema.table AS t', 'table'],
    102: ['c.foo', 'column'],
    117: ['c.test', 'column'],
    132: ['tt.bar', 'column'],
    145: ['cte AS c', 'table'],
    166: ['schema.table2 AS tt', 'table'],
    188: ['c.foo', 'column'],
    203: ['tt.foo', 'column'],
 }

def test__recursive_search():
    search_sql = RecursiveSearch()
    search_sql.recursive_depth(file_to_parse=parsed_query)
    assert search_sql.stock == expected_output
