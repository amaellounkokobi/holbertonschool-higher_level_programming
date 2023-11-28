#!/usr/bin/python3

""" Square module

This module descibe a class that represents a square.

Exemples:
   Verifying if the classsquare exists:

      my_square = Square()
      print(type(my_square))
      print(my_square.__dict__)

Attributes
   No attributes.

Classes
   Square: Represent a square.



"""


class Square():
    """ Empty class that represents a square.

    Atributes:
       size (void): Private size of the square.

    """

    def __init__(self, size):

        """ Initializing a square.

        Args: 
           size (void): Size of the square.

        """
        self.__size = size
    
    
    @property
    def size(self):
        """ Get the size of the square.
        
        Args:
           No args.

        """
        return __size




my_square = Square(3)

print(type(my_square))

print(my_square.__dict__)


try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
