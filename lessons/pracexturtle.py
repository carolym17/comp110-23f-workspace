
from turtle import Turtle, colormode, done
turtle_1: Turtle = Turtle()


turtle_1.penup()
turtle_1.goto(-300, 300)
turtle_1.setheading(0.0)
turtle_1.pendown()
turtle_1.begin_fill()
turtle_1.color("blue", "blue")
turtle_1.speed(3)
turtle_1.hideturtle()
i: int = 0
while i < 4:
    turtle_1.forward(600)
    turtle_1.right(90)
    i = i + 1
turtle_1.end_fill()