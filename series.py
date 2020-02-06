fileread = open("data.txt", "r")
filewrite = open("data2.txt", "w")

for line in fileread:
	for chr in line:
		if chr == "e":
			chr = "*"
		print(chr, file = filewrite)
