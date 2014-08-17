'''

Problem 164: Numbers for which no three consecutive digits have a sum greater than a given value

How many 20 digit numbers n (without any leading zero) exist such that no three consecutive digits of n have a sum greater than 9?

'''

import math

num = int(math.pow(10,19))
#print(num)
stop = int(math.pow(10,20))-1
#print(stop)

numLikeThis = 0
while num < stop:
	numStr = str(num)
	for pos in range(0, len(numStr)-2):
		if (int(numStr[pos])+int(numStr[pos+1])+int(numStr[pos+2])) < 10:
			#print(num)
			numLikeThis += 1
			break
	num += 1

print(numLikeThis)


			
