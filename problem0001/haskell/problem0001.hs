{-
Problem: http://projecteuler.net/index.php?section=problems&id=1
Author: Elie De Brauwer <elie @ de-brauwer.be>
License: Simplified BSD
Date: December 11, 2010
-}

problem0001 :: Integer
problem0001 = sum [ x | x <- [0..999], x `mod` 5 == 0 ||   x `mod` 3 == 0  ]

main = print problem0001