{-
Problem: http://projecteuler.net/index.php?section=problems&id=6
Author: Elie De Brauwer <elie @ de-brauwer.be>
License: Simplified BSD
Date: January 21, 2011
-}

squareOfSum :: Integer -> Integer 
squareOfSum x = sum [1..x] ^ 2

sumOfSquare :: Integer -> Integer 
sumOfSquare x = sum $ map (^2) [1..x]

main = print $ squareOfSum(100) - sumOfSquare(100)