class Parent:
    parentAttr = 100
    def __init__(self):
        print("Calling parent init")

    def parentMethod(self):
        print("Calling parent method")

    def setAtt(self,attr):
        Parent.parentAttr = attr

    def getAtt(self):
        print("Parent Attribute : ", Parent.parentAttr)

    def myMethod(self):
        print("Calling parent myMethod")


class Child(Parent):
    def __init__(self):
        print("Calling child init")

    def childMethod(self):
        print("Calling child method")

    def myMethod(self):
        print("Calling child myMethod")



c = Child()
c.myMethod()
c.childMethod() # class child
c.parentMethod() #parent class
c.setAtt(100)
c.getAtt()

