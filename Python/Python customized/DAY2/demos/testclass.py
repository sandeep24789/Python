class Sample:
	def setdata(self,empId,empName):
 	    self.empId=empId
 	    self.empName=empName
	def getdata(self):
	    print(self.empId)
	    print(self.empName)

obj=Sample()
obj.setdata(101,"Mathan")
obj.getdata()
print(hasattr(obj,"getdata"))
print(getattr(obj,"getdata"))
print(getattr(obj,"empId"))
