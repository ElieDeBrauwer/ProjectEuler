/**
 * Problem: http://projecteuler.net/index.php?section=problems&id=7
 * Author: Elie De Brauwer <elie @ de-brauwer.be>
 * License: Simplified BSD
 * Date: January 21, 2011
 */

class Problem0007{

   /**
    * Checks is a given integer is prime, scales O(n).
    * @param candidate - The number to check for being prime.
    * @return True if the digit is prime, False otherwise
    */
    static boolean isPrime(int candidate){
	for (int i = 2; i * i <= candidate; i++){
	    if (candidate % i == 0){
		return false;
	    }
	}
	return true;
    }

    public static void main(String [] args){
	int i = 3;
	int num = 2;
	while (num != 10001){
	    i+=2;
	    if (isPrime(i)){
		num++;
	    }
	}
	System.out.println(i);
    }
}
