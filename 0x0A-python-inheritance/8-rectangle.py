#!/usr/bin/python3
"""Defines a class from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent aaseGeometry."""

    def __init__(self, width, height):
        """Intiali Rectangle.

        Args:
            width ): The width of the new Rectangle.
            height height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
