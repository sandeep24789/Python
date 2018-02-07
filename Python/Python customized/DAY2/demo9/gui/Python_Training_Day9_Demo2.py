
from tkinter import *

root = Tk()

w = Label(root, text="Enter your details in below text field")
w.pack()



T = Text(root, height=5, width=30)
T.pack()


T.insert(END, "Just a text Widget\nin five lines\n")


root.mainloop()
