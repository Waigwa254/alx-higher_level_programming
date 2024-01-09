#!/usr/bin/python3

"""Defineunction."""


def append_write(filename="", text=""):
    """Apg to the end of a UTF8 text file.
    Args:       he file to append to.
         text (str): Tto append to the file.
    Reurns
    pended.
    """
with open(filename, "a", encoding="utf-8") as f:
return f.write(text)

