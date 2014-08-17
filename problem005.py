''' Project Euler Problem 5: 

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Remarks: The program is working as expected and the answer calculated is also right.
But the program is taking too long to finish.
'''
smallestMultiple=2
element=2

smallestMultiple = 0
multiple =3
while multiple:
	for num in range(2,21):
		if multiple % num != 0:
			break
		if num == 20:
			smallestMultiple = multiple		
			break
	if smallestMultiple == multiple:
		break
	multiple += 1
print(smallestMultiple)