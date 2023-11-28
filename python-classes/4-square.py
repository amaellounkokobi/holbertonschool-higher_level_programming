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

    def __init__(self, size=0):

        """ Initializing a square.

        Args:
           size (void): Size of the square.
           the size must be a positive int value

        Raise:
           TypeError, Size must be an integer
           ValueError, Size must be >= 0

        """
        self.__size = size

    def area(self):
        """ Calculate the area of a square

        Args:
           No args.

        Returns:
           A number equals to the area of the square

        """
        return self.__size * self.__size

    @property
    def size(self):
        """ Get the size attribut

        Args:
           No args.

        Returns:
           Size value.

        """
        return self.__size

    @__size.setter
    def size(self, value):
        """ Set the value of the size

        Args:
           size (void): Size of the square.
           the size must be a positive int value

        Raise:
           TypeError, Size must be an integer
           ValueError, Size must be >= 0

        """
        if not type(value) is int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
