from tkinter import *
import tkinter

top = tkinter.Tk()

B1 = tkinter.Button(top, text ="circle", relief=RAISED,\
                         cursor="circle")
B2 = tkinter.Button(top, text ="plus", relief=RAISED,\
                         cursor="plus")
B3 = tkinter.Button(top, text ="watch", relief=RAISED,\
                         cursor="watch")
B4 = tkinter.Button(top, text ="trek", relief=RAISED,\
                         cursor="trek")
B5 = tkinter.Button(top, text ="star", relief=RAISED,\
                         cursor="star")
B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
top.mainloop()
