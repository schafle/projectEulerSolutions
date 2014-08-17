''' 

Problem 52 : Permuted multiples

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

'''

def doesMultiplesHaveSameDigit(number):
	numString = str(number)
	for times in range(2, 7):
		multiple = times*number
		multipleString = str(multiple)
		#print(multipleString)
		for digit in range(0,len(multipleString)):
			if not multipleString[digit] in numString:
				return False
	return True

num = 1;
while num:
	if(doesMultiplesHaveSameDigit(num)):
		print(num)
		break
	num += 1
	
				
			
			
			
			
			
			
			


