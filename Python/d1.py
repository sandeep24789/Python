class emp:
    empcount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        emp.empcount += 1
    def displaycount(self):
        print("total employees: %d" %emp.empcount)
    def displayEmployee(self):
        print("Name: ",self.name)
        print("salary: ",self.salary)
    def __del__(self):
        class_name=self.__class__.__name__
        print("Destroyed",class_name)


emp1=emp("Deepa",20000)
emp2=emp("Ragavi",20000)

emp1.displayEmployee()
emp2.displayEmployee()

emp1.age=7
emp2.age=8
