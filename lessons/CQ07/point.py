"""Defining a class."""

from __future__ import annotations


class Point: 
    """Define a class."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
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