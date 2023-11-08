"""Test my zip function."""

__author__ = "730477957"

from lessons.zip import zip


def test_edge_case() -> None: 
    """Unit test for not same length- edge case."""
    test_list: list[str] = []
    int_list: list[int] = [1, 1]
    assert zip(test_list, int_list) == {}


def test_use_case_1() -> None:
    """Unit test for one use case- same length."""
    test_list: list[str] = ["Happy"]
    int_list: list[int] = [1]
    assert zip(test_list, int_list) == {"Happy": 1}


def test_use_case_2() -> None:
    """Unit test for one use case- same length."""
    test_list: list[str, str] = ["Happy", "Life"]
    int_list: list[int, int] = [1, 2]
    assert zip(test_list, int_list) == {"Happy": 1, "Life": 2}
