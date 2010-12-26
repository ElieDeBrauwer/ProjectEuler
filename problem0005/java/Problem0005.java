/**
 * Problem: http://projecteuler.net/index.php?section=problems&id=5
 * Author: Elie De Brauwer <elie @ de-brauwer.be>
 * License: Simplified BSD
 * Date: December 26, 2010
 */


class Problem0005{

    public static void main(String [] args){
	for(int val = 20; ; val+=20)
	{
	    int div = 20;
	    while (div != 1 && val % div == 0)
	    {
		div--;
	    }
	    if (div == 1)
	    {
		System.out.println("Result: " + val );
		System.exit(0);
	    }
	} 
    }
}
