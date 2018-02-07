import os
os.system('cls')
def Welcome(name):
    """This function welcomes the person(name) passed in as Parameter """
    print("Hello, " + name + ". Welcome to Python functions!")
    print("Inside Function.....");
    print("End of Function.....");
print("Outside Function........");
Welcome("ACCENTURE");
print("DOCSTRING = "+Welcome.__doc__);