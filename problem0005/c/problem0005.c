/**
 * Problem: http://projecteuler.net/index.php?section=problems&id=5
 * Author: Elie De Brauwer <elie @ de-brauwer.be>
 * License: Simplified BSD
 * Date: December 26, 2010
 */

#include <stdio.h>

int main()
{
    // Take jumps of size 20, could be enhanced by jumping 
    // in terms of 20*19*17.... but when we could just as well
    // just echo the solution ;-)
    for(int val = 20; ; val+=20)
    {
        int div = 20;
        while (div != 1 && val % div == 0)
        {
            div--;
        }
        if (div == 1)
        {
            printf("Result: %d\n", val);
            return 0;
        }
    } 
    return 1;
}
