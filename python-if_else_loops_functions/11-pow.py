#!/usr/bin/python3

# A function that computes a to the power of b and return the value
def pow(a, b):
    result = 1
    
    if b > 0:
        for index in range(b):
            result = result * a
    elif b == 0:
        pass
    else:
        for index in range(abs(b)):
            result = result * a
        result = 1 / result

    return result
