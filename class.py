class results:
	phy = 0
	che = 0
	mat = 0
	def showresults(self):
		total = self.phy + self.che+ self.mat
		print("result ", total)


peter = results()
peter.phy = 100
peter.che = 100
peter.mat = 100

peter.showresults()

