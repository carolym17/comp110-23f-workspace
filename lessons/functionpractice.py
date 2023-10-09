"""Demonstrates fucntions!"""

#input a str and it prints the str - input hello, it prints hello
print("Hello!")

#Round function
#functions return something, they don't necessarily print something, so you need print in front 
print(round(10.25))

#a different way to write round fucntion, save as integer, then print
#10 is not being printed by the fucntion, it is being returned by the function 
#10 is output assigned to x, when you print x, it returns as 10
x: int = round(10.25)
print(x)

#making print "hello" equal to something 
#print function prints something, but doesn't return anything- in terminal see none (pyton tells us)
y: str = print("Hello!")
print(y)

#randint is stored in python library, we are importing it 
#randint generates a new random number inbetween range 
from random import randint
z: int = randint(1,7)
print(z)


