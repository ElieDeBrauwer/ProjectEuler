/**
 * Problem: http://projecteuler.net/index.php?section=problems&id=4
 * Author: Elie De Brauwer <elie @ de-brauwer.be>
 * License: Simplified BSD
 * Date: December 24, 2010
 */

import java.lang.StringBuffer;

class Problem0004{

    /**
     * Check if a given value is a palindrome.
     * @param val The value which needs to be checked.
     * @return True when value is a palindrome.
     */
    public static boolean isPalindrome(int val){
	String normal = Integer.toString(val);
	String reverse = new StringBuffer(Integer.toString(val)).reverse().toString();
	return normal.compareTo(reverse) == 0;
    }

    public static void main(String [] args){
	int max = 0;
	for (int a = 999; a > 0; a--){
	    for (int b = 999; b >= a; b--){
		int prod = a*b;
		if (prod > max && isPalindrome(prod)){
		    max = prod;
		}
	    }
	}
	System.out.println("Largest palindrome is " + max);
    }
}
