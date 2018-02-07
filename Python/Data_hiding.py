#Data_hiding

class justcounter:
    __secretcount =0

    def count(self):
        self.__secretcount +=1
        print(self.__secretcount)

counter=justcounter()
counter.count()
counter.count()

print(counter.__secretcount)
