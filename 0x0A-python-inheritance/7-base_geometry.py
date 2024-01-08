#!/usr/bin/python3
"""Defines a baseeGeometry."""


class BaseGeometry:
    """Reprsent b geometry."""

    def area(self):
        """Not yelemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a er as an integer.

        Args:
            name (str) parameter.
            value (int validate.
        Raises:
        TypeEue is not an integer.
            Value: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
