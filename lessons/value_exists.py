"""Quiz 02 Practice Function Writing"""

def value_exists(dict1: dict[str, int], value: int) -> bool:
    """Return True if the int exists as a value in the dictionary, and False otherwise."""
    if "value" in dict1:
        return True 
    else: 
        False 


        