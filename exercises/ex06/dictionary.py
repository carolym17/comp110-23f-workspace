"""EX06 - Practice with Dictionary Fucntions Exercise!"""

__author__ = "730477957"


def invert(input: dict[str, str]) -> dict[str, str]: 
    """Function that inverts the keys and the values.""" 
    # Create an empty dictionary. 
    inverted = dict[str, str] = dict()
    # Iterate over the key, value pairs of dictionary x. 
    for key in input():
        # If there is a dumplicate, raise KeyError. 
        if input[key] in inverted:
            raise KeyError("KeyError: There is a duplicate key.")
        # Inverts the dictionary. 
        inverted[input[key]] = key
    # Return the inverted dictionary. 
    return inverted


def favorite_colors(input_1: dict[str, str]) -> str:
    """Returns favorite color- the color that appears most frequently."""
    # Create empty string to return favorite color. 
    most_popular_color: str = ""
    # Create empty dictionary
    colors_list: list[str] = list()
    max_number: int = 0 
    # Iterate through names and favorite colors. 
    for name, color in input:
        colors_list.append[input[name]]
    # Count the times color appears. 
    number_of_time_color_appeared: dict[str, int] = ()
    for color in number_of_time_color_appeared:
        if color in number_of_time_color_appeared:
            number_of_time_color_appeared[color] += 1
        else: number_of_time_color_appeared[color] = 1
        return number_of_time_color_appeared
    # To find the max.
    for color in number_of_time_color_appeared:
        if number_of_time_color_appeared > max_number:
            max_number = number_of_time_color_appeared[color]
            most_popular_color = color
    return most_popular_color


def count(input: list[str]) -> dict[str, int]:
    """Count of the number of times that a value appeared in the input list."""
    # Create an empty dictionary to store built-up result.
    final_list: dict[str, int] = ()
    # Iterate over each item in input list.
    for str in input:
        # Check to see if that item has already been established as a key in your dictionary.
        if str in final_list:
            # Item is found in the dict- means there is already a key/value pair where the item is a key. 
            final_list[str] += 1
        # Item is not found in the dict, that means this is the first time you are encountering the value. 
        else: final_list[str] = 1
    # Return resulting dictionary. 
    return final_list


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Function  where each key is a unique letter in the alphabet and each value is a list of the words that begin with that letter."""
    order_words: dict[str, list[str]] = dict()
    word: str = ""
    for word in input:
        # Takes in no arguments and returns the lower cased string of a given string. 
        letter = word[0].lower()
        if letter in order_words:
                order_words[letter].append(word)
        else: order_words[letter] = [word]


def update_attendance(list_attendance: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates the attendance log."""
    # Updates the attendance list with the new attendance information, then return it. 
    if day in list_attendance:
        list_attendance[day].append[student]
    else: list_attendance[day] = [student]
    return list_attendance
