#!/usr/bin/python3
""" This module contains a function that divides all elements of a matrix.

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
       matrix(list[lists[int/float]]): Matrix must be a list
       of lists of integers or floats.

       div(int/floar): The divided number must be an
       integer or a float. div can’t be equal to 0.

    Returns:
       A new matrix of the same size,
       All elements of the matrix should be divided by div,
       rounded to 2 decimal places

    Raise:
       TypeError exception with the message matrix must be
       a matrix (list of lists) of integers/floats
       ZeroDivisionError exception with the message division by zero

    """

    """ Div exception """
    err_msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    err_msg2 = "Each row of the matrix must have the same size"
    err_msg3 = "division by zero"
    err_msg4 = "div must be a number"

    if div == 0:
        raise ZeroDivisionError(err_msg3)

    if not type(div) is int and not type(div) is float:
        raise TypeError(err_msg4)

    if div is None:
        raise TypeError(err_msg3)

    """ Matrix exception """
    line_len = len(matrix)

    if line_len == 0:
        raise TypeError(err_msg1)

    for line in range(1, line_len):
        c_num = len(matrix[line])
        c_num_prev = len(matrix[line - 1])

        if not c_num == c_num_prev:
            raise TypeError(err_msg2)

    column_len = len(matrix[0])

    for line in range(line_len):
        for col in range(column_len):
            value = matrix[line][col]

            if not type(value) is int and not type(value) is float:
                raise TypeError(err_msg1)

    """ Function """
    new_matrix = []

    for line in range(line_len):
        new_matrix.append([])
        for col in range(column_len):
            new_matrix[line].append(round(matrix[line][col] / div, 2))

    return new_matrix
