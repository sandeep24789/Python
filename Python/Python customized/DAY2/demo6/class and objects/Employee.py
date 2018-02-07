class Employee:
    empCount = 0 #instance variable

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Totoal Employees : %d"%Employee.empCount)

    def displayEmployee(self):
        print("Name : ",self.name)
        print("Salary : ",self.salary)
        

    def __del__(self):
        class_name = self.__class__.__name__
        print("Destroyed",class_name)

# create objects

emp1 = Employee("Ajay",2000)
emp2 = Employee("Vikas",3000)

#display Objects

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employees : %d"%Employee.empCount)

# add or remove attributes at anytime

emp1.age = 7
emp2.age = 8




        
    
