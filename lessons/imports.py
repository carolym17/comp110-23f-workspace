"""Practice importing from other modules!"""

# Importing the module my_functions
from lessons.my_functions import my_functions

#Calling the function
print(my_functions.addition(1,2))

# Import variable from my functions
print(my_functions.my_variable)

if __name__ == "__main__":
    print("Howdy!")

print(my_functions.addition(1,2))