/**
 * Problem: http://projecteuler.net/index.php?section=problems&id=7
 * Author: Elie De Brauwer <elie @ de-brauwer.be>
 * License: Simplified BSD
 * Date: January 21, 2011
 */

#include <stdio.h>

/**
 * Checks is a given integer is prime, scales O(n).
 * @param candidate - The number to check for being prime.
 * @return 1 if the digit is prime, 0 otherwise
 */
static int isPrime(unsigned int candidate)
{
    unsigned int i = 0;
    for (i = 2; i * i <= candidate; i++)
    {
        if (candidate % i == 0)
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    unsigned int i = 3;
    int num = 2;
    while (num != 10001)
    {
        i+=2;
        if (isPrime(i) == 1)
        {
            num++;
        }
    }
    printf("%u\n", i);
    return 0;
}
