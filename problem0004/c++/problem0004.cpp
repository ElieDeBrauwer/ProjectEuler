/**
 * Problem: http://projecteuler.net/index.php?section=problems&id=4
 * Author: Elie De Brauwer <elie @ de-brauwer.be>
 * License: Simplified BSD
 * Date: December 24, 2010
 */

#include <algorithm>
#include <iostream>
#include <string>
#include <boost/lexical_cast.hpp>

/**
 * Check if a value is a palindrome.
 * @param val - The value which needs to be checked.
 * @return True when the value is a palindrome.
 */ 
bool isPalindrome(int val)
{
    std::string a = boost::lexical_cast<std::string>(val);
    std::string b = std::string(a);
    std::reverse(b.begin(),b.end());
    return a == b;
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
    std::cout << "Largest palindrome " << max << std::endl;
    return 0;
}
