'''
Problems 241: Perfection Quotients

For a positive integer n, let s(n) be the sum of all divisors of n, so e.g. s(6) = 1 + 2 + 3 + 6 = 12.

A perfect number, as you probably know, is a number with s(n) = 2n.

Let us define the perfection quotient of a positive integer as	p(n)	=  	s(n)/n.

Find the sum of all positive integers n = 10^18 for which p(n) has the form k + 1/2, where k is an integer.
'''
import math
def sumOfDivisors(divident):
	sum = 0
	for num in range(1, int(divident/2)+1):
		if divident%num == 0:
			sum += num
	return sum+divident

posNum = 1 
sumOfPerf = 0
while posNum < 10**18:
	sum = sumOfDivisors(posNum)
	perfectionQuotient = float(sum)/posNum
	if(perfectionQuotient-(math.floor(perfectionQuotient))== 0.5):
		print(posNum)
		sumOfPerf += posNum
	posNum += 1
print(sumOfPerf)
