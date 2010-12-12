{-
Problem: http://projecteuler.net/index.php?section=problems&id=2
Author: Elie De Brauwer <elie @ de-brauwer.be>
License: Simplified BSD
Date: December 12, 2010
-}

-- Generate a Fibonacci sequence starting with 1,2,3,5,8,...
fibo :: [Integer]
fibo = 1 : 2 : zipWith (+) fibo (tail fibo)

-- Get the sum of all even value not exceeding 4 million.
prob2 :: Integer
prob2 = sum (filter even (takeWhile (<4000000) fibo))

