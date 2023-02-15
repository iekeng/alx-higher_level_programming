#!/usr/bin/python3

"""
Defines a rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize a Rectangle

        Args:
        width(int): width of the rectangle
        height(int): height of the rectangle
        x(int): the x coordinate of the rectangle
        y(int): the y coordinate of the rectangle
        id(int): rectangle's identity
        Raises:
        TypeError:If the any of the values excluding id is not an int
        ValueError: If the width of height is <= 0
        ValueError: If either x or y < 0
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """set width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Get width of rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Get height of rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the value of the x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of the x coordinate"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the x coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
