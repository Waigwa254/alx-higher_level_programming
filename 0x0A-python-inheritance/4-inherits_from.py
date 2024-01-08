#!/usr/bin/python3
"""Definunction."""


def inherits_from(obj, a_class):
    """Cerited instance of a class.

    Args:
        to check.
        o match the type of obj to.
    Returns:
        instance of a_class - True.
        erwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
