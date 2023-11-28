#!/usr/bin/python3

""" Square module

This module descibe a class that represents a square.

Exemples:
   Create a square:

      my_square = Square(3,0,0)

Attributes:
   No attributes.

Classes:
   Square: Represent a square.

"""


class Square():
    """ Empty class that represents a square.

    Atributes:
       size (void): Private size of the square.

    """

    def __init__(self, size=0, position=(0, 0)):

        """ Initializing a square.

        Args:
           size (void): Size of the square.
           the size must be a positive int value

           position (tuple): X , y coordinate of the square

        """
        self.size = size
        self.position = position

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
        """ Get property to the size attribut

        Args:
           No args.

        Returns:
           Int size value.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set property to the size attribut

        Args:
           value (int): Size of the square.
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


    @property
    def position(self):
        """ getting the tuple of x and y coordinate

        Returns:
           position(tuple)tuple x and y coordinate
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setting the x and y coordinate  of the square

        Args:
           x(int): x coordinate, must be int and superior to zero
           y(int): y coordinate, must be int and superior to zero

        Raise:
           TypeError, Size x or y must be an integer
           ValueError, Size x or y must be >= 0

        """

        if not type(value) is tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif (not type(value[0]) is int) or (not type(value[1] is int)):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """ Printing a visual version of the square
        using private parameter size and positions

        """
        x = self.__position[0]
        y = self.__position[1]

        if not self.size == 0:
            if not self.__position == (0, 0):
                print('\n'*y, end='')

            for line in range(self.__size):
                if not self.__position == (0, 0):
                    print(' '*x, end='')

                for column in range(self.__size):
                    print('#', end='')
                print('')

        else:
            print('')
