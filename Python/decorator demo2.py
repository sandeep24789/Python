import time

def calctime(f):
    def wrap(*arg,** kwargs):
        start=time.time()
        result=f(*arg,** kwargs)
        end=time.time()
        print(f.__name__+" took "+ str((end-start)*1000))
        return result
    return wrap

    

@calctime
def calcsum(a,b):
    
    result =a+b
    print(result)
    
    
@calctime
def calcsub(a,b):
    
    result= a-b
    print(result)
    

    
calcsum(10,20)
calcsub(10,20)
