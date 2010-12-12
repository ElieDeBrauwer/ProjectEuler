/**
 * Problem: http://projecteuler.net/index.php?section=problems&id=3
 * Author: Elie De Brauwer <elie @ de-brauwer.be>
 * License: Simplified BSD
 * Date: December 12, 2010
 */

#include <stdio.h>

int main()
{
    unsigned long long val = 600851475143ULL;
    unsigned long long cur = 2;
    // No prime factors larger than the square root
    while (cur * cur <= val)
    {
        while( val % cur == 0)
        {
            printf("%llu ", cur);
            val /= cur;
        }
        cur++;
    }
    printf("%llu \n", val);
    return 0;
}
