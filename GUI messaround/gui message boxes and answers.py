from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('monkey message', 'Monkeys can live up to 200 years.')

answer = tkinter.messagebox.askquestion('Question 1', 'do you like silly faces?')

if answer == 'yes':
    print(" 8===D ")

root.mainloop()