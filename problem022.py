
file = open("names.txt", "r")

data = file.read()

list_names = data.split(",")
list_names = sorted(list_names)

i=1
total = 0
for name in list_names:
	name = name[1:-1]
	temp = 0
	for char in name:
		temp = temp + ord(char)-64
	total += temp*i
	i=i+1
	
print total
	

	