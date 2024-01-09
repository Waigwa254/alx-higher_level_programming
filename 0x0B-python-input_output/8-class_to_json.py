#!/usr/bin/python3

"""Defines a -JSON function."""


def class_to_json(obj):
    """Return the of a simple data structure."""
    return obj.__dict__
