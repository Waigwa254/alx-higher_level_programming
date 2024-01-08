#!/usr/bin/python3
"""Defines auare."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represquare."""

    def __init__(self, size):
        """I square.

        Args:
            size (int): ew square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
