#!/usr/bin/python3
'''
BaseGeometry() has area() public instance method.
'''


class BaseGeometry():
    '''
    The public instance method of this class
    raises an exception error
    '''
    def area(self):
        raise Exception("area() is not implemented")
