"""Defining a class"""

from __future__ import annotations


# Think of a class definition as a "roadmap" for objects that belong to the class. You are defining the underlying structure every instance of the class will have.
 

class Pizza: 

    #atrributes 
    # Think if these as the variables each instance of my class will have. 
    # <name> : <type>
    size: str
    toppings: int
    gluten_free: bool


    def __init___(self, input_size: str, input_toppings: int, input_gf: bool):
        """My Constructor"""
        self.size = input_size
        self.toppings = input_toppings
        self.gluten_free = input_gf
        # Return type =  pizza object. Don't need to declare a return type. 


    def price(self) -> float:
        """Calculate price of pizza."""
        if self.size == "large":
            price: float = 6.25
        else: 
            price: float = 5.00 
        price += .75 * self.toppings
        if self.gluten_free:
            price += 1.00
        return price 
    

    def add_toppings(self, num_toppings: int) -> None:
        """Add toppings to exisating pizza."""
        self.toppings += num_toppings


    def make_new_pizza_add_toppings(self, num_toppings: int) -> Pizza: 
        """Make a new pizza with existing pizza's properties and add toppings"""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza

    # Magic Method CL10 Lesson examples in VSCode. 
    def __str__(self) -> str:
        pizza_info: str = f"PIZZA ORDER: size {self.size}, toppings: {self.toppings}, GF: {self.gluten_free}"
        return pizza_info

# Magiv Method CL10 Lesson examples in VSCode. 
my_pizza: Pizza = Pizza("medium", 3, False)
print(str(my_pizza))
sals_pizza: Pizza = Pizza("large", 1, True)
print(sals_pizza)
print(1.0)