from tkinter import *
import time
import random

window = Tk()

class forGlobal(object):
    def __init__(self, code, index):
        self.code = code
        self.index = index   
        self.timer = None
        self.total = 0
        self.mode = None
        self.file = None
        self.start = False

g = forGlobal("abcdef", 0) 
g.timer = time.time()

def keypress(var):
    if g.start == False:
        targetlabel.config(text=g.code[g.index])
        g.start = True
        return
        
    limit = 36
    
    if var == g.code[g.index % 6]:
        g.total += g.timer
        g.file.write("Nicholas " + g.mode + " " + var+ " " + str(round(g.total, 1)) + "\n" )
        g.index += 1
        
        targetlabel.config(text=g.code[g.index % 6])
        if g.index >= limit:
            g.file.close()
            window.destroy()
        return
    
    else:    
        
        return
    
def dynamicBoard():
    a = ['q','w','e','r','t','y','u','i','o','p']
    b = ['a','s','d','f','g','h','j','k','l']
    c = ['z','x','c','v','b','n','m']
    
    random.shuffle(a)
    random.shuffle(b)
    random.shuffle(c)
    
    g.mode = "dynamic"
    board = [a, b, c] 
    g.file = open("experiment_dynamic_log.txt","w")
    return board

def staticBoard():
    board = ["qwertyuiop","asdfghjkl","zxcvbnm"]
    g.mode = "static"
    g.file = open("experiment_static_log.txt","w")
    return board
    
    
fullFrame = Frame(window, height=50, width=350, borderwidth=4)
fullFrame.pack()

display = Frame(fullFrame, height=30, width=350)
display.pack_propagate(0)
display.pack()

targetlabel = Label(display, text="Press any key to start", width=30, font=20)
targetlabel.pack(side=TOP)
targetlabel.config(relief="sunken", background="white")



keyboard = Frame(fullFrame, borderwidth=2, relief=RAISED)
keyboard.pack(side=BOTTOM)

row1 = Frame(keyboard)
row2 = Frame(keyboard)
row3 = Frame(keyboard)

row1.pack()
row2.pack()
row3.pack()

#board = dynamicBoard()
board = staticBoard()


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