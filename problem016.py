'''

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000

'''

def sumOfDigits(num):
	sumOfDigits = 0
	strNum = str(num)
	for digit in strNum:
		sumOfDigits += int(digit)
	return sumOfDigits
	
print(sumOfDigits(2**1000))