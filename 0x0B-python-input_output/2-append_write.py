"""Defines a file writing function which appends to an existing file"""


def append_write(filename="", text=""):
    """
    Args:
    filename - file to write to
    text - file to write from

    Return number of characters written
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
