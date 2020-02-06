singledig = ["one", "two", "three", "four", "five", "six"]

num = int(input("Enter a number: "))

singledigs = {
	1 : "one",
	2 : "two",
	3 : "three",
	4 : "four",
	5 : "five",
	6 : "six",
	7 : "seven",
	8 : "eight",
	9: "nine"
}

tens = {
	10 : "ten",
	20 : "twenty",
	30 : "thirty",
	40 : "fourty",
	50 : "fifty",
	60 : "sixty",
	70 : "seventy",
	80 : "eighty",
	90: "ninety"
}

def numtens(n):
	for i in tens:
		if i == str(num):
			return(tens.values([i]))


if len(str(num)) == 2:
	if str(num)[1] == "0":
		numtens(num)




