'''
Problem-8
Find the greatest product of five consecutive digits in the 1000-digit number.
'''

f = open("100DigitNumber.txt",'r')
content = f.readlines()
con=str(content)
con=con[2:-2]
greatestgreatestProduct = 1

for pos in range(0, len(con)-4):
	greatestProduct = 1
	product = 1
	for innerPos in range(pos,pos+5):
		product = product * int(con[innerPos])
		if greatestProduct < product:
			greatestProduct = product
	if greatestgreatestProduct < greatestProduct:
			greatestgreatestProduct = greatestProduct
			
print("greatest product %d")%(greatestgreatestProduct)
