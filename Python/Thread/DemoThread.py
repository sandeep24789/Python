from threading import Thread

class MyThread(Thread):

    def __init__(self):
        Thread.__init__(self,name="My Thread")


    def run(self):
        print("My name is :",self.getName())



t1=MyThread()
t1.start()
