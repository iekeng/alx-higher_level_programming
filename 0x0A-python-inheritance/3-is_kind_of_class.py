#!/usr/bin/python3
"""Module verifies an objects instance"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a super or a sub class"""

    """
    Args:
    obj: an insantiated object of a_class
    a_class: Could be a sub class or a super class

    Returns:
    True: If obj is an instance or inherited instance of a_class
    Otherwise, False.
    """
    if isinstance(obj, a_class):
        return True
    return False
