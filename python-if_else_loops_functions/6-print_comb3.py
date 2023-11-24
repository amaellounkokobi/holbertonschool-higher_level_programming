#!/usr/bin/python3

# All possible different combinations of two digits
for digit_one in range(10):
    for digit_two in range(10):
        if digit_one < digit_two:
            print('{0}{1}'.format(digit_one, digit_two), end='')
            if digit_one < 8:
                print(', ',end='')
print('')
