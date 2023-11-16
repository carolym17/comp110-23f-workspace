"""Defining a class."""

from __future__ import annotations


class Point: 
    """Define a class."""
    x: float
    y: float 

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """My Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutates a Point."""
        self.x = self.x * factor 
        self.y = self.y * factor 

    def scale(self, factor: int) -> Point:
        """A method that belongs to the Point class and instead of mutating a Point, it creates a new Point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Print out points in a readable way."""
        x: float = self.x
        y: float = self.y
        output: str = f"x: {x}; y: {y}"
        return output
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiplication operator overload."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point

    def __add__(self, factor: int | float) -> Point:
        """Addition operator overload."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point
