#!/usr/bin/env python
'''
Problem: http://projecteuler.net/index.php?section=problems&id=3
Author: Elie De Brauwer <elie @ de-brauwer.be>
License: Simplified BSD
Date: December 24, 2010
'''

def find_largest_palindrome():
    ''' 
    Calculate the largest palindrom which is a product of two three
    digit integers.
    The double for makes optimum use of lazy evaluation and the 
    [::-1] is stepping through the string with a negative stepvalue.
    '''
    maximum = 0
    for val_1 in range(999, 0, -1):
        for val_2 in range(999, 0, -1):
            prod = val_1 * val_2
            if prod > maximum and prod == int(str(prod)[::-1]):
                maximum = prod
    return maximum

if __name__ == "__main__":
    print find_largest_palindrome()
