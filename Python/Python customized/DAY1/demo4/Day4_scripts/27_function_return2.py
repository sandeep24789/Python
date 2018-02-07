import os
os.system('cls')
def Welcome(name):
    """This function welcomes the person(name) passed in as Parameter """
    print("Hello, " + name + ". Welcome to Python functions!")
    print("Inside Function.....");
    print("End of Function.....");
    return ;
print("Outside Function........");
Message = Welcome("ACCENTURE");# Function Call
print (Message);