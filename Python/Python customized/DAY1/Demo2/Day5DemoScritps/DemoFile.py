def demofile(file):

    file=open(file,'r');

    print ("Name of the file: ", file.name)
    print ("Closed or not : ", file.closed)
    print ("Opening mode : ", file.mode)

    file.close()

demofile('c:/sfdclab/file.txt')
