"""File to define Bear class."""


class Bear:
    """Bear class."""
    # Attributes 
    age: int 
    hunger_score: int 

    def __init__(self, initial_age: int = 0, initial_hunger_score: int = 0):
        """Constructor for Bear."""
        self.age = initial_age
        self.hunger_score = initial_hunger_score
        return None
    
    def one_day(self):
        """Increases the age value by one."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """Update the Bears hunger_score so that it increases by num_fish."""
        self.hunger_score += num_fish