#!/usr/bin/python3
""" This module containes a function that allows you to add two integers

examples:
   >>> print(add_integer(1, 2))
   3
   >>> print(add_integer(100, -2))
   98
   >>> print(add_integer(2))
   100
   >>> print(add_integer(100.3, -2))
   98
   >>> try:
   ...     print(add_integer(4, "School"))
   ... except Exception as e:
   ...     print(e)
   b must be an integer

   >>> try:
   ...     print(add_integer(None))
   ... except Exception as e:
   ...     print(e)
   a must be an integer

"""
def add_integer(a, b=98):
    """ add_integer :This function adds two integers

    Args:
       a(int/float): must be integers or floats.
       b(int/float): must be integers or floats 98 default value.

    Returns:
       (int): the addition of a and b

    Raise:
       if a or b are not integers: TypeError exception with
       the message a must be an integer or b must be an integer
       if a is empty : TypeError exception with the message
       a must be an integer

    """
    if a in locals():
        raise TypeError('a must be an integer')

    if not type(a) is int and not type(a) is float:
        raise TypeError('a must be an integer')

    if not type(b) is int and not type(a) is float:
        raise TypeError('b must be an integer')

    if abs(a) == float('inf'):
        raise TypeError('a must be an integer')

    if abs(b) == float('inf'):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
