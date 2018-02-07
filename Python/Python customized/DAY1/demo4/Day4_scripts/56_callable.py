class MyCallable:

    def __init__(self, value):
        self.value = value

    def __call__(self):
        y=2
        return 'The value is %s'% (self.value+y)

if __name__ == '__main__':
    # Construct an instance
    obj = MyCallable(88)
    # Call the instance, invoke __call__()
    print(obj())  # Output: The value is 88