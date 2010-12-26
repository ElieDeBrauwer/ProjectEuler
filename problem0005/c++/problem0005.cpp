/**
 * Problem: http://projecteuler.net/index.php?section=problems&id=5
 * Author: Elie De Brauwer <elie @ de-brauwer.be>
 * License: Simplified BSD
 * Date: December 26, 2010
 */

#include <iostream>

int main()
{
    // As boring as the c solution ...
    for(int val = 20; ; val+=20)
    {
        int div = 20;
        while (div != 1 && val % div == 0)
        {
            div--;
        }
        if (div == 1)
        {
            std::cout << "Result: " << val << std::endl;
            return 0;
        }
    } 
    return 1;
}
