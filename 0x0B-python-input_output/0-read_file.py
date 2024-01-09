#!/usr/bin/python3

"""Defines a tction."""


def read_file(filename=""):
    """Print the contdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
