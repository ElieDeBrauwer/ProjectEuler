#!/usr/bin/env python
'''
Problem: http://projecteuler.net/index.php?section=problems&id=6
Author: Elie De Brauwer <elie @ de-brauwer.be>
License: Simplified BSD
Date: January 21, 2011
'''

def square_of_sum(upper):
    '''
    Calculate the square of the sum of all integers smaller or equals to
    upper.
    '''
    sum_of_digits = upper * (upper + 1) / 2
    return sum_of_digits * sum_of_digits

def sum_of_squares(upper):
    '''
    Calculate the sum of all squares <= upper * upper
    '''
    return upper * (upper + 1) * (2 * upper + 1) / 6

if __name__ == "__main__":
    print square_of_sum(100) - sum_of_squares(100)
