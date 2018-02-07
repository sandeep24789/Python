#Fitting widgets in your layout

from tkinter import *
root = Tk()
one = Label(root,text = 'one',fg = 'white',bg = 'red' )#fg--color of text
two = Label(root,text = 'two',fg = 'black',bg = 'green' )
three = Label(root,text = 'three',fg = 'white',bg = 'blue' )
 
one.pack(fill = Y) #not going to grow
two.pack(fill = X)  #grow in x direction
three.pack(fill = Y, side = LEFT)  #grow in y direction
root.mainloop()
