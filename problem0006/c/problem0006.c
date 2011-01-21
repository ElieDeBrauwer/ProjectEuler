/**
 * Problem: http://projecteuler.net/index.php?section=problems&id=6
 * Author: Elie De Brauwer <elie @ de-brauwer.be>
 * License: Simplified BSD
 * Date: January 21, 2011
 */

#include <assert.h>
#include <stdio.h>

/**
 * Calculates the square of the sum of all digits <= max
 * @param max Upper boundary, inclusive.
 * @return The sum of the natural numbers squared in O(1).
 */
static unsigned int squareOfSum(unsigned int max)
{
    unsigned int sum = max * (max + 1) / 2;
    return sum*sum;
}

/**
 * Calculates the sum of all squares <= max*max
 * @param max Upper boundary, inclusieve
 * @return The sum of all squares <= than max*max
 */
static unsigned int sumOfSquares(unsigned int max)
{
    return max * (max + 1) * (2 * max + 1) / 6;
}

int main()
{
    assert(squareOfSum(10) == 3025);
    assert(sumOfSquares(10) == 385);

    printf("%u\n", squareOfSum(100) - sumOfSquares(100));
    return 0;
}
