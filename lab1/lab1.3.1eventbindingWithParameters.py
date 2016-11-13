from tkinter import *
from tkinter.ttk import * 
def change(the_value, n):
    the_value.set(the_value.get()+n)

window = Tk()
value = IntVar(0)
label = Label(window, textvariable=value)
label.pack()
button = Button(window, text="Left +1, Right -1")
button.bind("<Button-1>", lambda event: change(value, 1))
button.bind("<Button-3>", lambda event: change(value, -1))
button.pack()
window.mainloop()