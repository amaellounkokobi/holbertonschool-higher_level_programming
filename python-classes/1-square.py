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

