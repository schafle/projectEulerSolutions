'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

import math

def isPrime(number):
	if number in (0, 1):
		return False
	for element in range(2, int(math.sqrt(number))+1):
		if number % element == 0:
			return False
	return True
	
def isPandigital(number):
	num_str=str(number)
	length = len(num_str)
	if length == 10: 
		num_array = range(0,10)
	else: num_array = range(1,length+1)
	for digit in num_array:
		if not(str(digit) in num_str):
			return False
	return True

num = 9876543201

while num:
	if isPandigital(num) and isPrime(num):
		print("Here it comes")
		break
	num = num-2

print(num)