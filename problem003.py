''' Project Euler Problem 3: 

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''
import math

def isPrime(number):
	if number in (0, 1):
		return False
	for element in range(2, int(math.sqrt(number))+1):
		if number % element == 0:
			return False
	return True

	
divident=600851475143
numPrime =2
	
def nextPrime(number):
	while(not (isPrime(number))):
		number=number+1
	return number


while True:
	if(isPrime(numPrime)):
		#print("is %d Prime? %d \n")%(numPrime,isPrime(numPrime))
		while(divident%numPrime == 0):
			#print("divident %d \n divisor %d")%(divident, numPrime)
			quotient=divident/numPrime
			divident=quotient
			if isPrime(divident):
				print("the largest prime factor of 600851475143 is  %d")%(divident)
				break
	if isPrime(divident):
		break
	numPrime=nextPrime(numPrime+1)
	#print("nextPrime %d")%(numPrime)
