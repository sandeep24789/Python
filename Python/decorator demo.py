def mydec(f):
    def wrapper():
        print("Before calling the function from decorator")
        f()
        print("After calling the function from decorator")

    return wrapper

@mydec
def disp():
    print("welcome to python decorator")

disp()
    
