#!/usr/bin/python3
"""
Defines a base model class
"""


class Base:
    """
    Base model for all classes

    Private class Atribute:
    __nb_objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id == Base.__nb_objects
