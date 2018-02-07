class Sample:
    def __init__(self,empId,empName):
        self.empId=empId
        self.empName=empName
    def getdata(self):
        print(self.empId)
        print(self.empName)

    def __del__(self):
        print("object deleted")

obj=Sample(101,"Mathan")
obj.getdata()

print(hasattr(obj,"getdata"))
print(getattr(obj,"getdata"))
print(getattr(obj,"empId"))

print(dir(Sample))

print(Sample.__doc__)
print(Sample.__name__)
print(Sample.__module__)


print(dir(obj))
print(obj.__class__)

obj.__del__()


