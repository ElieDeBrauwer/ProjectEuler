#include <iostream>
/**
 * Problem: http://projecteuler.net/index.php?section=problems&id=1
 * Author: Elie De Brauwer <elie @ de-brauwer.be>
 * License: Simplified BSD
 * Date: December 11, 2010
 */

int main()
{
    int total = 0;
    for (int i = 0; i < 1000; i++)
    {
        if ((i%3 == 0) || (i%5 == 0))
        {
            total += i;
        }
    }
    std::cout << "Total: " << total << std::endl;
    return 0;
}
