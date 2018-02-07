class Employee:
    'Employee Class responsible for storing individual employee info'

    count=0 #Static Variable In Python Class

    def __init__(self, id,name,salary):
         self.id=id
         self.name=name
         self.salary=salary
         Employee.count+=1

    def displayEmpInfo(self):
         print("ID     :",self.id)
         print("Name   :",self.name)
         print("Salary :",self.salary)


e1=Employee(100,"Rama",33333.33)
e1.displayEmpInfo()
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print("No of Employee Objects : ",Employee.count)

print(e1.__class__)



print(getattr(e1,"id"))
print(getattr(e1,"name"))
print(getattr(e1,"salary"))

print(getattr(e1,"displayEmpInfo"))
getattr(e1,"displayEmpInfo")()

print(hasattr(e1,"getsalary"))

getattr(e1,"getsalary")
