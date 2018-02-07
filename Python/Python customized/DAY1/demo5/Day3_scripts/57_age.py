from datetime import date
bday=int(input("Enter your year of birth"))
today1=date.today()
age=today1.year-bday
print("age is :",age)