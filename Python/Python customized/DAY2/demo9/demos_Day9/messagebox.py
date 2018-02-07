from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo('Window Title','Hi whats up')
answer = tkinter.messagebox.askquestion('Question1', 'Do u like silly faces')

if answer == 'yes':
    print('8===D~~')
