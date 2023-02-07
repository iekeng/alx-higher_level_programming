#!/usr/bin/python3
'''
The lookup module checks all attributes of an object
'''


def lookup(obj):
    '''
    Returns a list of available attributes and methods of obj
    '''
    return list(dir(obj))
