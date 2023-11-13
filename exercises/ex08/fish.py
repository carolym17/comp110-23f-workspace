"""File to define Fish class."""


class Fish:
    """Fish class."""
    # Attributes 
    age: int 

    def __init__(self, initial_age: int = 0):
        """Constructor for fish."""
        self.age = initial_age
        return None
    
    def one_day(self):
        """Increases age by one."""
        self.age += 1
        