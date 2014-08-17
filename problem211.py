'''

Problem 211: Divisor Square Sum

For a positive integer n, let s2(n) be the sum of the squares of its divisors. For example,

s2(10) = 1 + 4 + 25 + 100 = 130.

Find the sum of all n, 0 < n < 64,000,000 such that s2(n) is a perfect square.

'''

import math

def sumOfSquaresOfDivisors(divident):
	sumOfSquaresOfDivisors = 0
	for num in range(1, int(divident/2)+1):
		if divident%num == 0:
			sumOfSquaresOfDivisors += num*num
	return sumOfSquaresOfDivisors+divident

def isPerfectSquare(apositiveint):
	root = math.sqrt(apositiveint)
	rootstr = str(root)
	if rootstr[rootstr.index(".")+1:] == "0":
		return True
	return False

sumOfAlln = 0
for num in range(1, 64000000):
	rootstr = str(math.sqrt(sumOfSquaresOfDivisors(num)))
	if rootstr[rootstr.index(".")+1:] == "0":
		sumOfAlln += num

print(sumOfAlln)
	
	
	
	
	
	