"""Practice QZ02 Function Writing - Odd and Even."""

def odd_and_even(list_1: list[int]) -> list[int]: 
    """Return new list with elements of input list that are odd and have an even index"""
    new_list: list[int] = list()
    for index, value in list_1:
        if key % 2 == 0 and list_1[key] % 2 != 0:
            new_list.append(list_1[key])
            key += 1
    return new_list

def odd_and_even(list1: list[int]) -> list[int]: 
    """Return list"""
    i: int = 1
    new_list: list[int] = ()
    while i < len(new_list):
        if list1[i] % 2 == 1 and i % 2 == 0:
            new_list.append(list1[i])
        i += 1

    return new_list
