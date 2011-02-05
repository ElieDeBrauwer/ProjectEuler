{-
Problem: http://projecteuler.net/index.php?section=problems&id=7
Author: Elie De Brauwer <elie @ de-brauwer.be>
License: Simplified BSD
Date: February 5, 2011
-}


{- Inspired upon: http://www.haskell.org/haskellwiki/Prime_numbers called
'the Classic Turner's Sieve. -}
primes = sieve [ 2.. ]
  where 
    sieve (p:xs) = p : sieve [ x | x <- xs, rem x p /= 0]


main = print $  primes !! 10000