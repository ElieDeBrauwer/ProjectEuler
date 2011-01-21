{-
Problem: http://projecteuler.net/index.php?section=problems&id=5
Author: Elie De Brauwer <elie @ de-brauwer.be>
License: Simplified BSD
Date: December 26, 2010
-}


{- canBeDivided checks if an integer can be divided by all values lesser 
   than a given argument-}
canBeDivided :: Integer -> Integer -> Bool
canBeDivided x 1 = True
canBeDivided x y = if x `mod` y == 0 then canBeDivided x (y-1) else False


main = print $  head [x*20 | x <- [1..], canBeDivided (x*20)  20 ]