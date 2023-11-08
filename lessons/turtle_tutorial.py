"""Turtle Tutorial for COMP 110."""

__author__ = "730477957"

# Import the library to set up turtle object. 
from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

# Exercise one, two, and three. 
leo.penup()
leo.goto(-130,-90)
leo.pendown()

colormode(255)

1

# Mini Project.
bob: Turtle = Turtle()
bob.penup()
bob.goto(45,60)
bob.pendown()

colormode(255)
bob.begin_fill()
bob.color("blue", "green")
bob.speed(7)
bob.hideturtle()
i: int = 0
while (i < 3):
    bob.forward(300)
    bob.left(120)
    i = i + 1
bob.end_fill()



