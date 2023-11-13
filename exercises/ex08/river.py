"""File to define River class."""

__author__ = "730477957"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """River Class."""
    # Attributes
    day: int 
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes animals as they age."""
        fish_surviving: list[Fish] = []
        bears_surviving: list[Bear] = []
        # Copy and check the surviving bears.
        for bears in self.bears:
            if bears.age <= 5: 
                bears_surviving.append(bears)
        # Copy and check the surviving fish.
        for fish in self.fish:
            if fish.age <= 3:
                fish_surviving.append(fish)
        # Update both lists. 
        self.bears = bears_surviving
        self.fish = fish_surviving

    def bears_eating(self):
        """As the bear eats, updates the number of fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
    
    def check_hunger(self):
        """Checks the hunger score of bears, and removes hungry bears."""
        surviving_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        
    def repopulate_fish(self):
        """Function for the reproduction of fish."""
        total_fish: int = len(self.fish)
        new_fish: int = (total_fish // 2) * 4
        for i in range(0, new_fish):
            self.fish.append(Fish)
        
    def repopulate_bears(self):
        """Function for the reproduction of bears."""
        total_bears: int = len(self.bears)
        new_bears: int = (total_bears // 2) * 1
        for i in range(0, new_bears):
            self.bears.append(Bear)
       
    def view_river(self):
        """Print the current river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Calls one_river_day seven times."""
        for i in range(0, 7):
            self.one_river_day()
    
    def remove_fish(self, amount: int) -> None: 
        """Removes fish from the river."""
        i: int = 0
        while i < amount:
            self.fish.pop(0)
            i += 1
        return None
            
