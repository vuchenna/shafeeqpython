import pymysql as mysql

db = mysql.connect("localhost","root","", "qa")
c= db.cursor()

while True:
	regno = input("insert your reg number: ")
	name = input("what is your name: ")
	subject = input("what subject: ")
	mark = input("what is your mark: ")

	save = input("do you want to save the record Y/N")

	if save == "Y" or save == "y":
		c.execute("insert into school values("+regno+", '"+name+"', '"+subject+"', "+mark+")")

		again = input("do you want to add another record Y/N").upper()

		if again =="N":
			break
db.commit()