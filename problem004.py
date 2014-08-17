'''

http://projecteuler.net/problem=4

'''
def isPalindrome(number):
	stringNum = str(number)
	pos = int(len(stringNum)/2)
	for pos in range(0,pos):
		if not stringNum[pos] == stringNum[-pos-1]:
			return False
			break
	return True

firstNum = 999
largestPalindromeProduct = 1
while firstNum > 99:
	secondNum = 999
	while secondNum > 99:
		product = secondNum*firstNum
		if isPalindrome(product):
			if largestPalindromeProduct < product:
				largestPalindromeProduct = product
				print("The current largest palindrome product for two three digit numbers is %d")%(product)
		secondNum = secondNum - 1
	firstNum = firstNum - 1
print("The largest palindrome product for two three digit numbers is %d")%(largestPalindromeProduct)



	
	

