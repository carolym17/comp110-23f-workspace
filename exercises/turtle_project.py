"""My happy place, my house! Challenge parts: I broke up the complex function to draw the house and I did the try something fun by using the random module to randomly place the sun each time."""
 
__author__ = "730477957"
 
from turtle import Turtle, done 
import random
 
# Main function to call to put it all together. 
def main() -> None:
    """The entrypoint of my scene."""
    random_sun = random.randint(-400, 250)
    turtle_1: Turtle = Turtle()
    turtle_1.speed(3)
    turtle_1.hideturtle()
    draw_rectangle(turtle_1, -400, 400, 0, 1000, 1000, "Green", "Green")
    draw_house(turtle_1)
    draw_circle(turtle_1, random_sun, 200, 0, "Yellow", "Yellow", 50, 360) 
    draw_line(turtle_1, -400, -210, 0, 1200, "Black")
    done()


# Fucntion to draw a rectangle. 
def draw_rectangle(turtle_1: Turtle, x: float, y: float, orientation: float, width: float, length: float, color_1: str, color_2: str) -> None:
    """Draws a rectangle.""" 
    turtle_1.penup()
    turtle_1.goto(x, y)
    turtle_1.setheading(orientation)
    turtle_1.pendown()
    turtle_1.begin_fill()
    turtle_1.color(color_1, color_2)
    i: int = 0
    while i < 2:
        turtle_1.forward(length)
        turtle_1.right(90)
        turtle_1.forward(width)
        turtle_1.right(90)
        i = i + 1 
    turtle_1.end_fill()

# Function to draw a line. 
def draw_line(turtle_1: Turtle, x: float, y: float, orientation: float, length: float, color_1: str) -> None:
    """Draws a line."""
    turtle_1.penup()
    turtle_1.goto(x, y)
    turtle_1.setheading(orientation)
    turtle_1.pendown()
    turtle_1.pencolor(color_1)
    turtle_1.forward(length)


# Function to draw a triangle roof. 
def draw_triangle(turtle_1: Turtle, x: float, y: float, orientation: float, length: float, color_1: str, color_2: str) -> None:
    """Draws a triangle."""
    turtle_1.begin_fill()
    turtle_1.color(color_1, color_2)
    turtle_1.penup()
    turtle_1.goto(x, y)
    turtle_1.setheading(orientation)
    turtle_1.pendown()
    i: int = 0
    while (i < 3):
        turtle_1.forward(length)
        turtle_1.left(120)
        i = i + 1
    turtle_1.end_fill()


# Function to draw the sun. 
def draw_circle(turtle_1: Turtle, x: float, y: float, orientation: float, color_1: str, color_2: str, radius: float, angle: float) -> None:
    """Draws a circle."""
    turtle_1.begin_fill()
    turtle_1.color(color_1, color_2)
    turtle_1.penup()
    turtle_1.goto(x, y)
    turtle_1.setheading(orientation)
    turtle_1.pendown()
    turtle_1.circle(radius, angle)
    turtle_1.end_fill()


# Function to draw the house. 
def draw_house(turtle_1: Turtle) -> None:
    """Puts together the house."""
    draw_rectangle(turtle_1, -30, -10, 0, 200, 200, "Pink", "Red")
    draw_triangle(turtle_1, -30, -10, 0, 200, "Blue", "Orange")
    draw_rectangle(turtle_1, 50, -170, 0, 40, 20, "Black", "White")
    

# Use the __name__ is "__main__" to call main. 
if __name__ == "__main__": 
    main()