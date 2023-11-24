#!/usr/bin/python3

# character is a char

def isLower(c):
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False

# String in uppercase

def uppercase(string):
    for c in string:
        print('{}'.format(c if not isLower(c) else chr(ord(c) - 32)), end='')
    print('')
