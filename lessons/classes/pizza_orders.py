"""Initializing a class."""

# This is where we initialize the class we defined in classes.py. In other words, we're creating objects that belong to that class. 

# Import the class 
# from <filename>.<modeulename> import <class>
from lessons.classes.pizza import Pizza

# Calling its constructor
my_pizza: Pizza = Pizza("large", 10, True) 

# Assessing/setting attributes 
# my_pizza.size = "large"
my_pizza.size = "large"
my_pizza.toppings = 10
my_pizza.gluten_free = True


# Printing out some values. 
print("my_pizza: ")
print(my_pizza)

print("Pizza.")
print(Pizza)

print("Size Attribute")
print(my_pizza.size)

print("Toppings")
print(my_pizza.toppings)

# creating a new pizza, sals_pizza 
sals_pizza: Pizza = Pizza("medium", 5, False)
print(sals_pizza.size)


# Class object can be input to a fucntion. 
def price(input_pizza: Pizza) -> float:
    """Calculate price of pizza"""
    if input_pizza.size == "large":
        price: float = 6.25
    else: 
        price: float = 5.00 
    price += .75 * input_pizza.toppings
    if input_pizza.gluten_free:
        price += 1.00
    return price 

# Calling the price function.
print(price(sals_pizza))
print(price(my_pizza))

# Calling the price method. 
print(sals_pizza.price)

my_pizza.toppings =+ 2
my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price()) 

my_other_pizza: Pizza = my_pizza.make_new_pizza_add_toppings(2)
print(my_other_pizza.toppings)
print(my_pizza.toppings)
