/**
 * Problem: http://projecteuler.net/index.php?section=problems&id=3
 * Author: Elie De Brauwer <elie @ de-brauwer.be>
 * License: Simplified BSD
 * Date: December 12, 2010
 */

import java.math.BigInteger;

class Problem0003{
    public static void main(String [] args){
	BigInteger val = new BigInteger("600851475143");
	BigInteger cur = new BigInteger("2");
	cur = cur.nextProbablePrime();
	while(val.compareTo(cur.multiply(cur)) != -1){
	    while(val.mod(cur) == BigInteger.ZERO){
		val = val.divide(cur);
		System.out.println(cur.toString());
	    }
	    cur = cur.nextProbablePrime();
	}
	System.out.println(val.toString());
    }
}