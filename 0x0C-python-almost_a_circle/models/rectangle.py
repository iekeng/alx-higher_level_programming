#!/usr/bin/python3
"""
Defines a rectangle class
"""
from .base import Base
"""
Represent a rectangle
"""


class Rectangle(Base):
    """
    Initialize a Rectangle

    Args:
    width(int): width of the rectangle
    height(int): height of the rectangle
    x(int): the x coordinate of the rectangle
    y(int): the y coordinate of the rectangle
    id(int): rectangle's identity

    """
    def __init__(self, width, height, x=0, y=0, id=None):

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            self.__y = value
