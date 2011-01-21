/**
 * Problem: http://projecteuler.net/index.php?section=problems&id=6
 * Author: Elie De Brauwer <elie @ de-brauwer.be>
 * License: Simplified BSD
 * Date: January 21, 2011
 */
class Problem0006{
    
    /**
     * Calculates the square of the sum of all digits <= max
     * @param max Upper boundary, inclusive.
     * @return The sum of the natural numbers squared in O(1).
     */
    static int squareOfSum(int max){
	int sum = max * (max + 1) / 2;
	return sum*sum;
    }

    
    /**
     * Calculates the sum of all squares <= max*max
     * @param max Upper boundary, inclusieve
     * @return The sum of all squares <= than max*max
     */
    static int sumOfSquares(int max){
	return max * (max + 1) * (2 * max + 1) / 6;
    }

    public static void main(String [] args){
	System.out.println(squareOfSum(100) - sumOfSquares(100));
    }
}
