''' Project Euler Problem 35: 

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''
import math
def isCircularPrime(number):
	numInString=str(number)
	rotatedNum=int(number)
	for digits in range(0, len(numInString)):
		#print(rotatedNum)
		if(not isPrime(rotatedNum)): #check if the number is prime
			return False
		rotatedNum=rotateNum(rotatedNum) #rotate it
	return True

def isPrime(number):
	if number in (0, 1):
		return False
	for element in range(2, int(math.sqrt(number))+1):
		if number % element == 0:
			return False
	return True

def rotateNum(number):
	numInString=str(number)
	rotatedString=""
	for pos in range(0,len(numInString)-1):
		rotatedString =  rotatedString + numInString[pos]
		
	rotatedString = numInString[len(numInString)-1] + rotatedString
	#print(" Rotated number = %s")%(rotatedString)
	return(int(rotatedString))


#print(isPrime(77))
#print(isCircularPrime(197))

numOfCircularPrime = 0
for num in range(2, 1000000):
	if(isCircularPrime(num)):
		numOfCircularPrime += 1
	
print(numOfCircularPrime)