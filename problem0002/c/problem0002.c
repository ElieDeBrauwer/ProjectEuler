/**
 * Problem: http://projecteuler.net/index.php?section=problems&id=2
 * Author: Elie De Brauwer <elie @ de-brauwer.be>
 * License: Simplified BSD
 * Date: December 12, 2010
 */

#include <stdio.h>

int main()
{
    int fib_prev = 1;
    int fib_cur = 2;
    int sum = 2;
    while(fib_cur < 4000000)
    {
        int tmp = fib_cur;
        fib_cur += fib_prev;
        fib_prev = tmp;
        if (fib_cur % 2 == 0)
        {
            sum += fib_cur;
        }
    }
    printf("%d\n", sum);
    return 0;
}
