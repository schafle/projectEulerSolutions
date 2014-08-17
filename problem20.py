'''

http://projecteuler.net/problem=20

'''

def sumOfDigit(number):
	numString = str(number)
	sum = 0
	for pos in range(0, len(numString)):
		sum = sum + int(numString[pos])
	return sum

factorial = 1
num = 100
while num > 1:
	factorial = factorial * num
	num = num - 1
	
print(sumOfDigit(factorial))