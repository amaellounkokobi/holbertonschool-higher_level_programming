#!/usr/bin/python3
""" 
This module contains a function that  prints My name is <first name> <last name>


Examples:
>>> say_my_name("John", "Smith")
My name is John Smith

>>> say_my_name("Walter", "White")
My name is Walter White

>>> say_my_name("Bob")
My name is Bob 


"""


def say_my_name(first_name, last_name=""):
    """
    This fuction prints 'My name is <first name> <lastname>'

    Args:
       first_name(string): Must be a string
       last_name(string): Must be a string and has a default value to "" 
    
    Returns:
       Prints 'My name is <first name> <lastname>'

    Raise: 
       TypeError 'first_name must be a string' when not a string and empty
       TypeError 'last_name must be a string' when not a string

    """

    first_name_err = 'first_name must be a string'
    last_name_err = 'last_name must be a string'
    
    if not type(first_name) is str:
        raise TypeError(first_name_err)

    if not type(last_name) is str:
        raise TypeError(last_name_err)

    output = "My name is {} {}".format(first_name, last_name) 

    print(output)


