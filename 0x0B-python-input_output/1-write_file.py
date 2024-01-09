#!/usr/bin/python3

"""Defineg function."""


def write_file(filename="", text=""):
    """Wrg to a UTF8 text file.
    Args:
        f of the file to write.
        ttext to write to the file.
    Returns:
        Taracters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

