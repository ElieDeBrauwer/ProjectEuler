{-
Problem: http://projecteuler.net/index.php?section=problems&id=4
Author: Elie De Brauwer <elie @ de-brauwer.be>
License: Simplified BSD
Date: December 25, 2010
-}


{- Checks if a number is a palindrome -}
isPalindrome :: Integer -> Bool
isPalindrome x = (show x) == (reverse $ show x)

problem0004 :: Integer
problem0004 = maximum [x*y | x <- [1..999], y <- [1..999], isPalindrome(x*y)]