x={ 'test1':1, 'test2':2, 'test3':3 }
my_keys = ('test1','test2')
y=dict(filter(lambda t: t[0] in my_keys, x.items()))
print(y)
