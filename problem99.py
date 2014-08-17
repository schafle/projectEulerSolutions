'''

Project Euler Problem 99: 

Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.

'''

# Open a file
fo = open("C:\Users\scf4kor\Desktop\\base_exp.txt", "r")
#print "Name of the file: ", fo.name
line = fo.readline()
largestExponential=0
while (line):
	lineElements=line.split(',')
	print "Read Line: %s" % (line)
	#print "First: %s" % (lineElements[0])
	#print "Second: %s" % (lineElements[1])
	print "The current largestExponential is: %d" % (int(lineElements[0])**int(lineElements[1]))
	if int(lineElements[0])**int(lineElements[1]) > largestExponential:
		largestExponential=int(lineElements[0])**int(lineElements[1])
		print "Largest Exponential is: %s" % (largestExponential)
	break
	line = fo.readline()

