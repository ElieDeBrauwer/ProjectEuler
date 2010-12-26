#!/usr/bin/env python
'''
Problem: http://projecteuler.net/index.php?section=problems&id=5
Author: Elie De Brauwer <elie @ de-brauwer.be>
License: Simplified BSD
Date: December 26, 2010
'''

def problem0005():
    '''
    Finds the smallest value which is divisible by [1..20]
    ''' 
    val = 20
    while True:
        val = val + 20
        for div in range(20, 1, -1):
            if val % div != 0:
                break
            elif div == 2:
                return val

if __name__ == "__main__":
    print problem0005()
