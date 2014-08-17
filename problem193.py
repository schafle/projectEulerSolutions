'''

Problem 193: Squarefree Numbers

A positive integer n is called squarefree, if no square of a prime divides n, thus 1, 2, 3, 5, 6, 7, 10, 11 are squarefree, but not 4, 8, 9, 12.

How many squarefree numbers are there below 250?

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
	currentPrimeNum = 5
	while currentPrimeNum < math.sqrt(math.pow(2,25)):
		if isPrime(currentPrimeNum):
			listOfPrimes.append(currentPrimeNum)
		currentPrimeNum = 6*x+1
		if isPrime(currentPrimeNum) and currentPrimeNum < math.sqrt(math.pow(2,25)):
			listOfPrimes.append(currentPrimeNum)
		x += 1
		currentPrimeNum = 6*x-1
		
def isSquareFree(number):
	for primes in listOfPrimes:
		if number % math.pow(primes,2) == 0 :
			return False
	return True
	
listOfPrimes=[2, 3]
primeNumberGenerator()
numOfSquareFreeNumbers = 0
num = 1

while num < math.pow(2,50):
	if isSquareFree(num):
		numOfSquareFreeNumbers += 1
	num += 1
print(numOfSquareFreeNumbers)