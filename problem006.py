'''
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def sumOfSquares(lastNum):
	sumOfSquares=0
	for num in range(1,lastNum+1):
		sumOfSquares=sumOfSquares+(num*num)
	return sumOfSquares

def squareOfSum(lastNum):
	sumOfNum=0
	for num in range(1,lastNum+1):
		sumOfNum=sumOfNum+num
	return sumOfNum*sumOfNum

print("The difference is %d")%(squareOfSum(100)-sumOfSquares(100))