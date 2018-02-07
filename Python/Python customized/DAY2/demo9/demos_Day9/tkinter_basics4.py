#Grid Layout

from tkinter import *
root = Tk()

label1 = Label(root,text ='Name')  
label2 = Label(root,text ='Password')
entry_1 = Entry(root)
entry_2 = Entry(root)

label1.grid(row = 0,sticky = 'E')  #be on top
label2.grid(row = 1,sticky ='E')                #be on bottom

entry_1.grid(row = 0,column =1)     #column is 2ndcolumn and row is 1st row
entry_2.grid(row = 1, column =1)

check = Checkbutton(root,text = 'keep me logged in')
check.grid(columnspan=2)  #it going to take 2 columns and merge it together and be diaplayed right there
root.mainloop()


#two labesl and 2 entry widgets
# for entry_1:whenever u want user to enter simple number or name or password u have to use entry.
#where on grid u want me to put it so row = 0 n by default column is always 0
#everything is centeraligned,any software application is right aligned
#sticky is to align labels to right i.e. E,left i.e.s,n i.e. top ,si.e bottom
#i want to have checkbox so dat next time if i will login i need not to give my name and password.
