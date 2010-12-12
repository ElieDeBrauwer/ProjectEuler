#!/bin/bash 

# Problem: http://projecteuler.net/index.php?section=problems&id=3
# Author: Elie De Brauwer <elie @ de-brauwer.be>
# License: Simplified BSD
# Date: December 12, 2010

# Lazy Unix hackers solution, jus make use of the 'factor' binary.
factor 600851475143 | sed 's/.* //'