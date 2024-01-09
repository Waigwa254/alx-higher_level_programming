#!/usr/bin/python3

"""Define file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Pya JSON file."""
    with open(filename) as f:
        return json.load(f)
