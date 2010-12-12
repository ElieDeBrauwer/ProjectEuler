/**
 * Problem: http://projecteuler.net/index.php?section=problems&id=3
 * Author: Elie De Brauwer <elie @ de-brauwer.be>
 * License: Simplified BSD
 * Date: December 12, 2010
 * Note: this gives the full factorization instead of just the prime factors.
 */
#include <iostream>

int main()
{
    unsigned long long val = 600851475143ULL;
    unsigned long long cur = 2;
    // No prime factors larger than the square root
    while (cur * cur <= val)
    {
        while( val % cur == 0)
        {
            std::cout << cur << " " << std::flush;
            val /= cur;
        }
        cur++;
    }
    std::cout << val << std::endl;
    return 0;
}
