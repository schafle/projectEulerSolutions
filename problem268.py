'''

Problem 268: Counting numbers with at least four distinct prime factors less than 100

It can be verified that there are 23 positive integers less than 1000 that are divisible by at least four distinct primes less than 100.

Find how many positive integers less than 1016 are divisible by at least four distinct primes less than 100.

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
	while currentPrimeNum < 100:
		if isPrime(currentPrimeNum):
			listOfPrimes.append(currentPrimeNum)
		currentPrimeNum = 6*x+1
		if isPrime(currentPrimeNum) and currentPrimeNum < 100:
			listOfPrimes.append(currentPrimeNum)
		x += 1
		currentPrimeNum = 6*x-1

listOfPrimes=[2, 3]
primeNumberGenerator()
countOfNumbers = 0

num = 1
while num < math.pow(10,16):
	numOfPrimes = 0
	for primes in listOfPrimes:
		if num % primes == 0:
			numOfPrimes += 1
			if numOfPrimes > 3:
				countOfNumbers += 1
				break
	num += 1
print(countOfNumbers)