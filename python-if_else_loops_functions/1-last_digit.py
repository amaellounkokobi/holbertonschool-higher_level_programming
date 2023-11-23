#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Getting the last digit
if number >= 0:
    last_digit = abs(number) % 10
else:
    last_digit = -(abs(number) % 10)

# End sentece conditionals
if last_digit > 5:
    end_sentence = 'is greater than 5'
elif last_digit < 6 and not last_digit == 0:
    end_sentence = 'is less than 6 and not 0'
else:
    end_sentence = 'is 0'

# Building the final output
print('Last digit of {} is {} and {}'.format(number, last_digit, end_sentence))
