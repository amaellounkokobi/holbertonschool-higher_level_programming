#!/usr/bin/python3

# A function that computes a to the power of b and return the value
def pow(a, b):
    for index in range(b):
        a *= a
    return a
