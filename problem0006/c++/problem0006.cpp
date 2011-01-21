/**
 * Problem: http://projecteuler.net/index.php?section=problems&id=6
 * Author: Elie De Brauwer <elie @ de-brauwer.be>
 * License: Simplified BSD
 * Date: January 21, 2011
 */

#include <iostream>

/**
 * Calculates the square of the sum of all digits <= max
 * @param max Upper boundary, inclusive.
 * @return The sum of the natural numbers squared in O(1).
 */
unsigned int squareOfSum(unsigned int max)
{
    int sum = max * (max + 1) / 2;
    return sum*sum;
}

/**
 * Calculates the sum of all squares <= max*max
 * @param max Upper boundary, inclusieve
 * @return The sum of all squares <= than max*max
 */
unsigned int sumOfSquares(unsigned int max)
{
    return max * (max + 1) * (2 * max + 1) / 6;
}

int main()
{
    std::cout << squareOfSum(100) - sumOfSquares(100) << std::endl;
    return 0;
}
