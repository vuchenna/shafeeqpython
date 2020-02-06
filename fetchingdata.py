import pymysql as mysql


class datahandling:

	def __init__(self):
		self.db = mysql.connect("localhost", "root", "", "QA")
		self.c = self.db.cursor()


	def main(self):
		print("1. Entry")
		print("2. Delete")
		print("3. View")

		choice = int(input("enter your choice"))
		if choice == 1:
			self.dataentry()

		if choice == 2:
			self.deleteentry()

		if choice == 3:
			self.viewentry()

	def dataentry(self):
		while True:
			regno = input("insert your reg number: ")
			name = input("what is your name: ")
			grp = input("what group are you in: ")
			client = input("who is your client: ")
			marks = input("what is your mark: ")

			save = input("do you want to save the record Y/N")

			if save == "Y" or save == "y":
				self.c.execute("insert into consultant values("+regno+",'"+name+"', '"+grp+"','"+client+"', "+marks+")")
				self.db.commit()
				again = input("do you want to add another record Y/N").upper()

				if again =="N":
					break
		self.main()

	def deleteentry(self):
		rec = (input("Enter Registration to delete: "))
		self.c.execute("select * from consultant where regno =" +rec)
		datadel = self.c.fetchall()

		if len(datadel)!= 0:


			for field in datadel:
				print(field[0])
				print(field[1])
				print(field[2])
				print(field[4])
				
			question = input("do you want to delete this record YES/No").upper()

			if question == "YES":
				confirm = input("are you sure? YES/NO").upper()

				if confirm == "YES":
					deletequery="delete from consultant where regno="+rec
					print(deletequery)
					self.c.execute(deletequery)
					self.db.commit()
					print("record deleted")
		
		else:
			print("record does not exist")
			self.main()

	def viewentry(self):

		print("1. View all records")
		print("2. View Specific Group")
		print("3. View specific client")
		print("4. View specific Registration number")
		answer = int(input("enter your number"))

		if answer == 1:
			self.c.execute("select * from consultant")
			allrec = self.c.fetchall()


			for field in allrec:
				print(field[0])
				print(field[1])
				print(field[2])
				print(field[4])

			self.main()

		if answer == 2:
			grp = input("Please type in the specific group you want to view")
			self.c.execute("select * from consultant where grp ='"+grp+"'")
			specgrp = self.c.fetchall()

			for field in specgrp:
				print(field[0])
				print(field[1])
				print(field[2])
				print(field[4])

			self.main()

		if answer == 3:
			client = input("Please type in the specific client you want to view")
			self.c.execute("select * from consultant where client ='"+client+"'")
			speccli = self.c.fetchall()

			for field in speccli:
				print(field[0])
				print(field[1])
				print(field[2])
				print(field[4])

			self.main()

		if answer == 4:
			regnum = input("Please type in the specific registration number you want to view")
			self.c.execute("select * from consultant where regno = " + regnum)
			specreg = self.c.fetchall()

			for field in specreg:
				print(field[0])
				print(field[1])
				print(field[2])
				print(field[4])



		

			self.main()





m = datahandling()
m.main()
