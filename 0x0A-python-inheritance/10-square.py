#!/usr/bin/python3
"""Defines a ss Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Repressquare."""

    def __init__(self, size):
        """Initisquare.

        Args:
            size (int): The new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
