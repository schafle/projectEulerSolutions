'''

The following iterative sequence is defined for the set of positive integers:

n --> n/2 (n is even)
n --> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 ? 40 ? 20 ? 10 ? 5 ? 16 ? 8 ? 4 ? 2 ? 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''
def lengthOfSequenceCalc(start_num):
	num = start_num
	length =1
	while num>1:
		if num%2 == 0: next_num = num/2
		else: next_num = 3*num+1
		length += 1
		num=next_num
	return length

start_num = 2
lengthOfSequence = 1

while start_num < 1000000:
	newLengthOfSequence = lengthOfSequenceCalc(start_num)
	if (lengthOfSequence < newLengthOfSequence):
		lengthOfSequence = newLengthOfSequence
		max_start_num = start_num
	start_num += 1

print(max_start_num)