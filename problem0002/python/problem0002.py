#!/usr/bin/env python
'''
Problem: http://projecteuler.net/index.php?section=problems&id=2
Author: Elie De Brauwer <elie @ de-brauwer.be>
License: Simplified BSD
Date: December 12, 2010
'''

def problem0002():
    '''
    Solves project Euler problem 2
    '''
    fib_prev = 1
    fib_cur = 2
    result = 2
    while fib_cur < 4000000:
        tmp = fib_cur
        fib_cur = fib_cur + fib_prev
        fib_prev = tmp
        if fib_cur % 2 == 0:
            result = result + fib_cur
    print "Result: %d" % result

if __name__ == "__main__":
    problem0002()


