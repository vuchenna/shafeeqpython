
add = "Y"
file = open("save.txt", "a")

while True:

	regno = input("enter your registration number: ")
	name = input("Enter your name: ")
	address = input("Enter your address: ")

	save = input("Do you wantm to save the record Y/N")

	if save == "Y" or save == "y":
		print(regno, name, address, sep=",", file = file)

	again = input("Do you want to add another record (Yes/No)")
	if again.upper() != "Yes":
		break


