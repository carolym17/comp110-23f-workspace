"""EX04 - List Utility Functions."""

__author__ = "730477957"

# Importing randint to generate random numbers. 
from random import randint

# Defining a function named all that checks numbers at each index. 
def all(list_numbers: list[int], number: int) -> bool: 
    """Returns True if all numbers match at indicated number."""
# If the length of the list is empty, returns False. 
    if len(list_numbers) <= 0:
        return False 
    idx: int = 0
# Checks for number mathes at each index. 
    while idx < len(list_numbers):
        if list_numbers(idx) != number:
            return False 
        idx += 1
    return True

# Defining a fucntion max to find the highest number when provided a list of numbers. 
def max(list_num2: list[int]) -> int:
    """Returns highest integer."""
# raises an error if the list is empty. 
    if len(list_num2) == 0:
        raise ValueError("max() arg is an empty List")
# Creating a variable to store the max number and searching for the max number. 
    highest_number: int = list_num2[0]
    idx: int = 1
    while idx < len(list_num2):
        if highest_number < len(list_num2): 
            highest_number = list_num2[idx]
        idx += 1
    return highest_number
    
# Defining a fucntion called is_equal to check if the list fo numbers are the same in each index. 
def is_equal(list_num3: list[int], list_num4: list[int]):
    """Returns True if every element at each index is equal in both lists."""
    idx: int = 0
# If the lengths of the list do not match, returns False. 
    if len(list_num3) != len(list_num4):
        return False
# Checks if lists match at each index. 
    while idx < len(list_num3): 
        if list_num3[idx] != list_num4[idx]:
            idx += 1
        else: 
            return False 
    return True
