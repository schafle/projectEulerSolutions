'''
Project Euler Problem 7: 

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

def isPrime(number):
    """Return True if *number* is prime."""
    if number in (0, 1):
        return False

    for element in xrange(2, (number/2)):
		if number % element == 0:
			return False
    return True

element = 1
primeNum=0
while element:
	if isPrime(element):
		#print("%d is prime")%(element)
		primeNum=primeNum+1
		if primeNum > 10001:
			print("%d is 10001st prime Number")%(element)
			break
	element=element+1
		
		
		
	
