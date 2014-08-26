'''
problem:145
Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (109)?
'''

def isReversible(num):
	strNum=str(num)
	reversedNumStr=strNum[::-1]
	reversedNum=int(reversedNumStr)
	sum= reversedNum+num
	sumStr=str(sum)
	for c in sumStr:
	if int(c)%2==0:
	return False
	return True

count=0
for n in range(1,10**9):
	nstr=str(n)
	if n%10 != 0 :
	if int(nstr[0])%2==0 and int(nstr[-1])%2!=0:
	if isReversible(n):
	count+=1
	elif int(nstr[0])%2!=0 and int(nstr[-1])%2==0:
	if isReversible(n):
	count+=1
print(count)
