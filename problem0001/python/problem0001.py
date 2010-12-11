#!/usr/bin/env python
'''
Problem: http://projecteuler.net/index.php?section=problems&id=1
Author: Elie De Brauwer <elie @ de-brauwer.be>
License: Simplified BSD
Date: December 11, 2010
'''

if __name__ == "__main__":
    TOTAL = 0
    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            TOTAL = TOTAL + i

    print TOTAL
