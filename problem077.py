''' 

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''
import math

def isPrime(number):
	if number in (0, 1):
		return False
	for element in range(2, int(math.sqrt(number))+1):
		if number % element == 0:
			return False
	return True

def primeNumberGenerator():
	x=1
	sumOfPrime = 5
	currentPrimeNum = 5
	while currentPrimeNum < 2000000:
		if isPrime(currentPrimeNum):
			print(currentPrimeNum)
			sumOfPrime = sumOfPrime + currentPrimeNum
		currentPrimeNum = 6*x+1
		if isPrime(currentPrimeNum) and currentPrimeNum < 2000000:
			print(currentPrimeNum)
			sumOfPrime = sumOfPrime + currentPrimeNum
		x += 1
		currentPrimeNum = 6*x-1
	return sumOfPrime

	
print(primeNumberGenerator())
