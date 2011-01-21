#include <assert.h>
#include <stdio.h>

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
    assert(squareOfSum(10) == 3025);
    assert(sumOfSquares(10) == 385);

    printf("%u\n", squareOfSum(100) - sumOfSquares(100));
    return 0;
}
