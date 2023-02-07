#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a given class.

    Args:
        obj - object
        a_class - class

    Returns:
        True if object is an instance of a_class
        Otherwise it returns False.
    """
    if type(obj) == a_class:
        return True
    return False
