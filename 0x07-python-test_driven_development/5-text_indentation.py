#!/usr/bin/python3
"""
Moduleindentation
Contains meer each ".", "?", and ":"
Takes in a g
"""


def text_indentation(text):
    """
    Prints tter each ".", "?", and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    revised = "\n".join(list_lines)
    print(revised, end="")
