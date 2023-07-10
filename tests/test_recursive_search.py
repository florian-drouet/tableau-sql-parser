from src.recursive_search import RecursiveSearch
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ({"foo": 1, "bar": 2, "bip": "test"}, "foo bar bip"),
        ({"  foo ": 1, " bar   ": 2, "bip": "test"}, "foo bar bip"),
    ],
)
def test_get_dict_values(test_input, expected):
    assert RecursiveSearch._get_dict_values(test_input) == expected
