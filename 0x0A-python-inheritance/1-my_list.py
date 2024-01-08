#!/usr/bin/python3
"""Defi inherited lList."""


class MyList(list):
    """Implements sorted lt-in list class."""

    def print_sorted(self):
        """Print a list in ending order."""
        print(sorted(self))
