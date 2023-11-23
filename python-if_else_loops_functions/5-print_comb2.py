#!/usr/bin/python3

# A program that prints numbers from 0 to 99
for num in range(100): 
    if not num == 99:
        print('{0:0>2d}, '.format(num), end='')
    else:
        print('99')
