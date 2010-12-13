#!/usr/bin/env python
'''
Problem: http://projecteuler.net/index.php?section=problems&id=3
Author: Elie De Brauwer <elie @ de-brauwer.be>
License: Simplified BSD
Date: December 13, 2010
'''

def factors(val):
    '''
    Calculate the prime factors for a value. Returns the
    prime factorization as a list.
    '''
    factor_list = []
    cnt = 2
    while cnt <= val:
        while val % cnt == 0:
            val = val / cnt
            factor_list.append(cnt)
        cnt = cnt + 1
    return factor_list 

if __name__ == "__main__":
    print factors(600851475143)



