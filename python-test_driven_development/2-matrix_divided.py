#!/usr/bin/python3
"""  This module contains a function that divides all elements of a matrix.

Examples:
   >>> matrix = [
       [1, 2, 3],
       [4, 5, 6]
   ]
   ... print(matrix_divided(matrix, 3))
   [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

"""


def matrix_divided(matrix, div):
    """ This function that divides all elements of a matrix
    
    Args:
       matrix(list[lists[int/float]]): Matrix must be a list of lists of integers or floats.
       div(int/floar): The divided number must be an integer or a float. div can’t be equal to 0.

    Returns:
       A new matrix of the same size,
       All elements of the matrix should be divided by div, rounded to 2 decimal places
       
    Raise:
       TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
       ZeroDivisionError exception with the message division by zero

    """
    pass
