#!/usr/bin/python3

"""Defines a g function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a N representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
