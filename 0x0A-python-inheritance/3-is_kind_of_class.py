#!/usr/bin/python3
"""Defininherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Cnherited instance of a class.

    Args:
        object to check.
        s to match the type of obj to.
    Returns:
        ited instance of a_class - True.
        Otherwis
        """
    if isinstance(obj, a_class):
        return True
    return False
