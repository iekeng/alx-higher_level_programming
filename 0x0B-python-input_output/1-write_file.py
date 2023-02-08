#!/usr/bin/python3
"""Defines a file writing function"""


def write_file(filename="", text=""):
    """
    Args:
    filename - file to write to
    text - file to write from

    Return number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
