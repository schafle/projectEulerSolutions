'''
Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
import math

def isCuriousNum(Num):
	strNum = str(Num)
	sumOfFact = 0
	for c in strNum:
		sumOfFact += math.factorial(int(c))
	if sumOfFact == Num:
		return True
	return False

num=3
sumOfCuriousNum=0
while num < 100000:
	if isCuriousNum(num):
		sumOfCuriousNum += num
	num+=1
print(sumOfCuriousNum)