from tkinter import *
import time

window = Tk()

class forGlobal(object):
    def __init__(self, code, index):
        self.code = code
        self.index = index   
        self.timer = None
        self.total = 0

g = forGlobal("abcdef", 0) 
g.timer = time.time()

def keypress(var):
     
    limit = 10
    
    if var == g.code[g.index % 6]:
        g.total += g.timer
        timerlabel.config(text="Nicholas " + str(round(g.total, 1)))
        g.index += 1
        txtDisplay.insert(END, var)
        targetlabel.config(text=g.code[g.index % 6])
        if g.index >= 10:
            targetlabel.config(text="You have completed the experiment")
            window.destroy()
        return
    
    else:    
        txtDisplay.insert(END, var)
        return
    

    
    
fullFrame = Frame(window, height=50, width=350, borderwidth=4)
fullFrame.pack()

display = Frame(fullFrame, height=50, width=350)
display.pack_propagate(0)
display.pack()
txtDisplay = Entry(display, bd=2, width=28, font = 30, justify=CENTER) #bd is border
txtDisplay.pack(side=TOP, pady=3)
targetlabel = Label(display, text=g.code[g.index], width=30, font=20)
targetlabel.pack(side=TOP)
timer = Frame(fullFrame, height=50, width=350)
timer.pack(side=TOP, pady=3)
timerlabel = Label(timer, text="Nicholas ")
timerlabel.pack(side=TOP)


keyboard = Frame(fullFrame, borderwidth=2, relief=RAISED)
keyboard.pack(side=BOTTOM)

row1 = Frame(keyboard)
row2 = Frame(keyboard)
row3 = Frame(keyboard)

row1.pack()
row2.pack()
row3.pack()


board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
row = [row1,row2,row3]
rowIndex = 0
for line in board:
    
    for letter in line:
        f = Frame(row[rowIndex], height=32, width=32)
        f.pack_propagate(0)
        f.pack(side=LEFT)
        
        button = Button(f, text=letter, command=lambda x=letter: keypress(x))
        button.pack( fill=BOTH, expand=1)
    rowIndex += 1





window.mainloop()