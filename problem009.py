'''

Project Euler Problem 9: 

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''
m=1
while m:
	n=m+1
	while n:
		FTP=n*n-m*m
		STP=2*n*m
		TTP=n*n+m*m
		print("Three pythagorean triplets are %d %d %d")%(FTP, STP, TTP)
		if FTP+STP+TTP == 1000:
			print("Product of Pythagorean triplet with sum 1000 is %d")%(FTP*STP*TTP)
			break
		if FTP+STP+TTP > 1000:
			break
		n=n+1
	if FTP+STP+TTP == 1000:
		break
	m=m+1

