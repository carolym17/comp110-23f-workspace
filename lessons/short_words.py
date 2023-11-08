"""Practice Cide Writing Quiz 2."""

def short_words(list1: list[str]) -> list[str]:
    """Return a new list [str] of the words from the input list that are shorter than 5 characters."""
    new_list: list[str] = list()
    for x in list1:
        if len(x) < 5:
            new_list.append(x)
    else: 
        print(f"{x} is too long!")
    return new_list


