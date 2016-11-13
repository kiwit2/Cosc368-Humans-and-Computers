from tkinter import *
from tkinter.ttk import * 

window = Tk()

for label_num in range(6):
    button = Button(window, text="Button"+str(label_num))
    button.grid(row=label_num // 3, column=label_num % 3)

window.mainloop()