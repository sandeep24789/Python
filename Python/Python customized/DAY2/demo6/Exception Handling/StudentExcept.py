#Exception Handling

class StudExcept(Exception):
    def __init__(self,msg='Unknown Error', errnum = -1):
        self.msg = msg
        self.errnum = errnum

    def printDetails(self):
        print(self.msg,self.errnum)
        return self.errnum

class Student:
    def __init__(self,*p):
        if len(p) == 0: #default initializer
            self.marks = 0
            self.grade = 0
            self.name = ''
            self.id = ''
        elif len(p)<4: raise IndexError('Not enough Values')
        else:
            if p[0]<0: raise StudExcept('Marks are Negative',1)
            else : self.marks = p[0]

            if p[1]<1: raise StudExcept('Grade is less than 1st std',2)
            else : self.grade = p[1]

            if not isinstance(p[2],str): raise StudExcept('Name is not a string',3)
            else: self.name = p[2]

            if not isinstance(p[3],str): raise StudExcept('ID is not a string',4)
            else: self.id = p[3]

    def printDetails(self):
        print(self.marks,self.grade,self.name,self.id)




            
            
