#!/usr/bin/python3
"""Defines a class ReseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rery."""

    def __init__(self, width, height):
        """Intialize ectangle.

        Args:
            width (in Rectangle.
            height (i new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return theation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
