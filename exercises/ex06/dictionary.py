"""EX06 - Practice with Dictionary Fucntions Exercise!"""

__author__ = "730477957"


def invert(input: dict[str, str]) -> dict[str, str]: 
    """Function that inverts the keys and the values.""" 
    # Create an empty dictionary. 
    inverted: dict[str, str] = {}
    # Iterate over the key, value pairs of dictionary x. 
    for key in input:
        # If there is a dumplicate, raise KeyError. 
        if input[key] in inverted:
            raise KeyError("KeyError: There is a duplicate key.")
        # Inverts the dictionary. 
        inverted[input[key]] = key
    # Return the inverted dictionary. 
    return inverted


def favorite_color(input: dict[str, str]) -> str:
    """Returns favorite color- the color that appears most frequently."""
    # Create empty dictionary
    colors_list: list[str] = list()
    # Iterate through names and favorite colors. 
    for name in input:
        colors_list.append(input[name])
    # Count the times color appears. 
    color_counter_dict: dict[str, int] = {}
    for color in colors_list:
        if color in color_counter_dict:
            color_counter_dict[color] += 1
        else: 
            color_counter_dict[color] = 1
    # To find the max.
    max_number: int = 0 
    most_popular_color: str = ""  
    for color in colors_list:
        if color_counter_dict[color] > max_number:
            most_popular_color = color
            max_number = color_counter_dict[color]
    return most_popular_color


def count(input: list[str]) -> dict[str, int]:
    """Count of the number of times that a value appeared in the input list."""
    # Create an empty dictionary to store built-up result.
    final_list: dict[str, int] = {}
    # Iterate over each item in input list.
    for str_value in input:
        # Check to see if that item has already been established as a key in your dictionary.
        if str_value in final_list:
            # Item is found in the dict- means there is already a key/value pair where the item is a key. 
            final_list[str_value] += 1
        # Item is not found in the dict, that means this is the first time you are encountering the value. 
        else: 
            final_list[str_value] = 1
    # Return resulting dictionary. 
    return final_list


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Function  where each key is a unique letter in the alphabet and each value is a list of the words that begin with that letter."""
    order_words: dict[str, list[str]] = {}
    word: str = ""
    for word in input:
        # Takes in no arguments and returns the lower cased string of a given string. 
        letter = word[0].lower()
        if letter in order_words:
            order_words[letter].append(word)
        else: 
            order_words[letter] = [word]
    return order_words


def update_attendance(list_attendance: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates the attendance log."""
    # Updates the attendance list with the new attendance information, then return it. 
    if day in list_attendance:
        list_attendance[day].append(student)
    else: 
        list_attendance[day] = [student]
    return list_attendance
