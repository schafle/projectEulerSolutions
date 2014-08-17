'''

Problem 44: Pentagon numbers

Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk - Pj| is minimised; what is the value of D?

'''

def generatePentagonal():
	for num in range(1, 100000):
		listOfPentagonalNumbers.append(num*(3*num-1)/2)
		
listOfPentagonalNumbers = []

j = 1
k = 1
out=0
generatePentagonal()

for j in range(1,10000):
	for k in range(1,10000):
		if ((listOfPentagonalNumbers[j]+listOfPentagonalNumbers[k]) in listOfPentagonalNumbers) and ((listOfPentagonalNumbers[j]-listOfPentagonalNumbers[k]) in listOfPentagonalNumbers):
			print("Pk=%d and Pj=%d")%(listOfPentagonalNumbers[j],listOfPentagonalNumbers[k])
			out=1
			break
		k=k+1
	if out==1:break
	j=j+1


#print(listOfPentagonalNumbers)
