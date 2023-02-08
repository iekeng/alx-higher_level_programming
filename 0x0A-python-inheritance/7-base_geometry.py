#!/usr/bin/python3
'''
BaseGeometry() has area() and integer_validator public instance method.
'''


class BaseGeometry():
    '''
    The public instance method of this class
    raises an exception error
    '''
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Checks if 'value' gets an int data type

        Args:
            name - str
            value - int

        Raises:
        TypeError: If value is not an integer
        ValueError: If value is <= 0

        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
