"""EX07 - Practice with Dictionary Unit Tests!"""

__author__ = "730477957"

# Importing the functions to write tests for them. 
from dictionary import invert
from dictionary import favorite_color
from dictionary import count
from dictionary import alphabetizer
from dictionary import update_attendance

# Importing pytest to test KeyError. 
import pytest

# Writing three test to test invert. 
# Edge case for function invert, this case will have duplicate keys and should return a key error.  
def test_invert_edge_case() -> None: 
    """Unit test if there are two duplicated keys."""
    test_dict: dict[str, str] = {"Antonio": "Seat 1", "Josh": "Seat 3", "Layla": "Seat 2", "Carrie": "Seat 3"}
    with pytest.raises(KeyError):
          invert(test_dict)


# Use case #1 for invert function. 
def test_invert_use_case1() -> None: 
    """Unit test for dict with 3 keys, should return the dictionary inverted."""
    test_dict: dict[str, str] = {"Antonio": "Seat 1", "Josh": "Seat 2", "Layla": "Seat 3"}
    assert invert(test_dict) == {"Seat 1": "Antonio", "Seat 2": "Josh", "Seat 3": "Layla"}


# Use case #2 for invert function. 
def test_invert_use_case2() -> None: 
    """Unit test for dict with 5 keys, should return the dictionary inverted."""
    test_dict: dict[str, str] = {"Dish 1": "Pasta", "Dish 2": "Salad", "Dish 3": "Oatmeal", "Dish 4": "Chicken", "Dish 5": "Tofu"}
    assert invert(test_dict) == {"Pasta": "Dish 1", "Salad": "Dish 2", "Oatmeal": "Dish 3", "Chicken": "Dish 4", "Tofu": "Dish 5"}


# Writing three test to test invert. 
# Edge case for function favorite_color. 
def test_favorite_color_edge_case() -> None: 
    """Unit test for favorite_color with no most popular color."""
    color_list: dict[str, str] = {"Albert": "Blue", "Makenna": "Yellow", "Alice": "Red"}
    expected_result: list() = ("Blue, Yellow", "Red")
    assert favorite_color(color_list) == expected_result


# Use case for function favorite_color. 
def test_favorite_color_use_case1() -> None: 
    """Use test case for inputed dictionary length of only one key"""
    input_dict: dict[str, str] = {"Albert": "Blue"}
    assert favorite_color(input_dict) == ("Blue")


# Use case for function favorite_color. 
def test_favorite_color_use_case2() -> None: 
    """Use test case for when there is a clear majority for favorite color."""
    input: dict[str, str] = {"Albert": "Blue", "Makenna": "Blue", "Alice": "Red", "Keegan": "Blue", "Ben": "Red", "Carrie": "Blue", "Michael": "Blue", "Chris": "Blue"}
    assert favorite_color(input) == ("Blue")


# Writing three test to test count. 
# Edge case for function count. 
def test_count_edge_case() -> None: 
    """Edge case for when the list is empty."""
    input_list: list[str] = ()
    assert count(input_list) == {}

# Use case for function count. 
def test_count_case1() -> None: 
    """A use case with 7 intems in the list."""
    list_items: list[str] = ["apple", "banana", "apple", "orange", "banana", "apple", "grape"]
    assert count(list_items) == {'apple': 3, 'banana': 2, 'orange': 1, 'grape': 1}


# Use case for function count. 
def test_count_use_case2() -> None: 
    """A use case, where the list is letters in a word at each index instead of a list of words at each index."""
    list_letters: list[str] = ["h", "a", "p", "p", "y"]
    assert count(list_letters) == {"h": 1, "a": 1, "p": 2, "y": 1}


# Writing three test to test alphabetizer. 
# Edge case for function alphabetizer. 
def test_alphabetizer_edge() -> None:
    """A edge case, where the input list contains contains words that start with characters other than alphabetical letters."""
    word_list: list[str] = ["apple", "123yay"]
    assert alphabetizer(word_list) == {"a": ["apple"], "1": ["123yay"]}


# Use case for function alphabetizer. 
def test_alphabetizer_use1() -> None:
    """A use case, where there are words that begin with the same letter."""
    word_list: list[str] = ["apple", "apricot", "berries", "bacon", "cherries"]
    assert alphabetizer(word_list) == {"a": ["apple", "apricot"], "b": ["berries", "bacon"], "c": ["cherries"]}


# Use case for function alphabetizer. 
def test_alphabetizer_use1() -> None:
    """A use case where the words begin with the first and last letters of the alphabet."""
    list_input: list[str] = ["apple", "zebra"]
    assert alphabetizer(list_input) == {"a": ["apple"], "z": ["zebra"]}


# Writing three test to test update_attendance. 
# Edge case for function update_attendance. 
def test_update_attendance_edge() -> None:
    """Updating attendance for a day that has no students present"""
    attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"], "Wednesday": []}
    assert update_attendance(attendance_log, "Wednesday", []) == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"], "Wednesday": []}

# Use case for function alphabetizer. 
def test_update_attendance_use1() -> None:
    """Updates attedance for Tuesday to add the student Craig."""
    attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Tuesday" 
    student: str = "Craig"
    assert update_attendance(attendance_log, day, student) == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Craig"]}


# Use case for function alphabetizer. 
def test_update_attendace_use2() -> None:
    """Updates attendance log to the day Wednesday with Kyle."""
    attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Wednesday" 
    student: str = "Kyle"
    assert update_attendance(attendance_log, day, student) == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Craig"], "Wednesday": ["Kyle"]}
    
