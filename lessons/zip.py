"""Combining two lists into a dictionary!"""

__author__ = "730477957"


def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Produce a dictionary where the keys are the items of the first list and the values are the corresponding items at the same index of the second list."""
    zipped_dict: dict[str, int] = dict() 
    if len(str_list) != len(int_list) or str_list == [] or int_list == []: 
        return dict()
    for elem in range(0, len(str_list)):
        zipped_dict[str_list[elem]] = int_list[elem]
    return zipped_dict


print(zip(["Happy", "Tuesday"], [1, 2]))
