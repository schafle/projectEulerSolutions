'''

Problem 131: Prime cube partnership

'''

import math

def isPrime(number):
	if number in (0, 1):
		return False
	for element in range(2, int(math.sqrt(number))+1):
		if number % element == 0:
			return False
	return True
	
def isPerfectCube(num):
	if num in listOfCubes:
		return True
	return False

def cubeGenerator():
	cube = 0
	num = 0
	while cube < 1000000:
		cube = math.pow(num, 3)
		listOfCubes.append(cube)
		num += 1

def primeNumberGenerator():
	x=1
	currentPrimeNum = 5
	while currentPrimeNum < 1000000:
		if isPrime(currentPrimeNum):
			listOfPrimes.append(currentPrimeNum)
		currentPrimeNum = 6*x+1
		if isPrime(currentPrimeNum) and currentPrimeNum < 1000000:
			listOfPrimes.append(currentPrimeNum)
		x += 1
		currentPrimeNum = 6*x-1

		
listOfCubes=[]
listOfPrimes=[2, 3]
cubeGenerator()
primeNumberGenerator()
primeWithThisProperty = 0

for primes in listOfPrimes:
	if primes > 1000000:
		break
	for num in range(1, 1000000):
		if ((math.pow(num,3))+ math.pow(num,2)*primes) in listOfCubes:
			print(primes)
			primeWithThisProperty += 1
			
print(primeWithThisProperty)


























