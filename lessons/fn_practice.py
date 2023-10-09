"""Example functions to learn defintion and calling syntax!"""

#defining a fucntion
#creating a function called my_max. 
#give it two numbers and it will tell us the maximum
def my_max(number1: int, number2: int) -> int:
    """Returns the maximum value out of two numbers"""
    if number1 >= number2:
        return number1
    else: #number1 < number2
        return number2
    
#calling my fucntion 
max_number: int = my_max(1,10)
other_max_number: int = my_max(11,3)
print(max_number)
print(other_max_number)