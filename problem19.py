''' ProjectEuler: Problem 19
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''

def isLeapYear(year):
	if year%4 == 0 and (year%100 != 0 or year%400 == 0):
		return True
	return False

def firstSundays(year, Month):
	jan,mar,may,jul,aug,oct,dec = 31,31,31,31,31,31,31
	apr,jun,sep,nov = 30, 30, 30, 30
	if isLeapYear(year):
		feb= 29
	else:
		feb=28
	
	if Month == feb:
		feb = jan+4
	elif Month == mar:
		if isLeapYear(year):
			mar = feb+1
		
	
	

def nextDay(year, firstDay):
	if year%4 == 0 and (year%100 != 0 or year%400 == 0):
		return(firstDay-6) if (firstDay+2)>6 else (firstDay+2)	
	return 1 if (firstDay+1)> 6 else (firstDay+1)

firstDay = 2
sundays = 0
for year in range(1901,2001):
	sundays += firstSundays(year,firstDay)
	firstDay = nextDay(year,firstDay)

print(sundays)	
#print(calcSundays(1901,1))
#print(nextDay(1901,1))