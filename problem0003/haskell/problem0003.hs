{-
Problem: http://projecteuler.net/index.php?section=problems&id=3
Author: Elie De Brauwer <elie @ de-brauwer.be>
License: Simplified BSD
Date: December 14, 2010
-}

{- n = candidate divisor, a = divident -}
factor :: Integer -> Integer -> [Integer]
factor _ 1 = []
factor n a = if (a `mod` n == 0) then n : factor n (a `div` n) else factor (n+1) a

problem0003 :: [Integer]
problem0003 = factor 2 600851475143

main = print problem0003