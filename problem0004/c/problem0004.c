/**
 * Problem: http://projecteuler.net/index.php?section=problems&id=4
 * Author: Elie De Brauwer <elie @ de-brauwer.be>
 * License: Simplified BSD
 * Date: December 24, 2010
 */

#include <assert.h>
#include <stdio.h>

/**
 * Check if a value is a palindrome.
 * @param val The value which needs to be checked, should be 
 * smaller than 1.000.000
 * @return 1 When the value is a palindrome, 0 otherwise.
 */
int isPalindrome(int val)
{
    char buf[7];
    int num = snprintf(buf,sizeof(buf),"%d",val);
    assert(val < 1000000);
    for (int i=0; i<num/2; i++)
    {
        if (buf[i] != buf[num-i-1])
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    int max = 0;
    for (int i=999; i>0; i--)
    {
        for (int j=999; j>0; j--)
        {
            int prod = i * j;
            if (prod > max && isPalindrome(prod))
            {
                max = prod;
            }
        }
    }
    printf("Largest palindrome %d\n", max);
    return 0;
}
