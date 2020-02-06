class maths:
	result=0
	def docalculation(self,a,b):
		self.result = a+b
	def showresult(self):
		print("result ", self.result)

m = maths()
m.docalculation(10,20)
m.showresult()