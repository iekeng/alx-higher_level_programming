#!/usr/bin/python3
"""Checks for indirect or direct inheritance"""


def inherits_from(obj, a_class):
    """
    Args:
    obj - object
    a_class - class

    Returns: True if obj inherits from a_class
    Otherwise: False
    """
    if isinstance(a_class, obj):
        return True
    return False
