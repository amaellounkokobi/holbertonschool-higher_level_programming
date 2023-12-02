#!/usr/bin/python3
""" Print square module

This module descibe a function that prints a square.

Exemples:
   Print a square:

>>> print_square(4)
####
####
####
####

"""


def print_square(size):
    """ Printing a visual version of the square
        parameter size

    Args:
           size (void): Size of the square.
           the size must be a positive int value
    Raise:
           TypeError, Size must be an integer
           TypeError, Size must be >= 0

    """

    """ Exception handling """

    if not type(size) is int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    """ Function """

    for line in range(size):
        for column in range(size):
            print('#', end='')
        print('')
