from tkinter import *
from tkinter.ttk import * 

window = Tk()



vertscrollbar = Scrollbar(window, orient=VERTICAL)
vertscrollbar.grid(row=0, column=1, sticky="ns")
horiscrollbar = Scrollbar(window, orient=HORIZONTAL)
horiscrollbar.grid(row=1, column=0, sticky="ew")

t = Text(window, wrap=NONE, height=10, width=24)
t.grid(row=0, column=0, sticky="n")

vertscrollbar.config(command=t.yview)
horiscrollbar.config(command=t.xview)


t.config(yscrollcommand=vertscrollbar.set)
t.config(xscrollcommand=horiscrollbar.set)

paragraph = ""
while len(paragraph) < 3000:
    paragraph += ("This is Nick's sentence for creating \n "
                   "a small 2d scrolling window. ")
    
    
    

t.insert(END, paragraph)    

  

window.mainloop()