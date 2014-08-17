''' 

Problem 60 : Prime pair sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

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
	while currentPrimeNum < 1000000:
		if isPrime(currentPrimeNum):
			listOfPrimes.append(currentPrimeNum)
		currentPrimeNum = 6*x+1
		if isPrime(currentPrimeNum) and currentPrimeNum < 1000000:
			listOfPrimes.append(currentPrimeNum)
		x += 1
		currentPrimeNum = 6*x-1

listOfPrimes=[3]
primeNumberGenerator()
num = 0
for prime in listOfPrimes:
	for pos in range (0, len(listOfPrimes)):
		if isPrime(int(str(listOfPrimes[pos])+str(prime))) and isPrime(int(str(prime)+str(listOfPrimes[pos]))) and int(str(listOfPrimes[pos])+str(prime)) != int(str(prime)+str(listOfPrimes[pos])):
			print("...........")
			print(int(str(listOfPrimes[pos])+str(prime)))
			print(int(str(prime)+str(listOfPrimes[pos])))
			print("...........")
			print (prime)
			num += 1
			break
	if num == 5:
		break