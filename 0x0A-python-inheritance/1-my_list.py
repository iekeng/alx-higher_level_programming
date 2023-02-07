#!/usr/bin/python3
'''
MyList class inherits a list.
'''


class MyList(list):
    '''
    Sorts the list in ascending order and prints it.  
    '''
    def print_sorted(self):
        print(sorted(self))

