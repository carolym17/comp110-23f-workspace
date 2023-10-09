"""Things I will be importing."""

# Defining a function
def addition(x: int, y: int): 
    return x + y

# Defining a variable.
my_variable: str = "Hello!"

# If not running main file, it prints else message 
if __name__ == "__main__":
    print("This should only print when running my_functions")
else: 
    print("my_functions is being imported")


