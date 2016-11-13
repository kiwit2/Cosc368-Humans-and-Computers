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
    target = g.code[g.index]
    if g.start == False:
        txtDisplay.delete(0, END)
        txtDisplay.insert(END, target)  
        g.start = True
        
    if var == target:
        g.index += 1
        txtDisplay.delete(0, END)
        txtDisplay.insert(g.code[g.index])
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

display = Frame(fullFrame, height=50, width=350)
display.pack_propagate(0)
display.pack()
txtDisplay = Entry(display, bd=2, width=28, font = 30, justify=CENTER) #bd is border
txtDisplay.pack(side=TOP, pady=3)
txtDisplay.insert(0, "Click any button to start")




keyboard = Frame(fullFrame, borderwidth=2, relief=RAISED)
keyboard.pack(side=BOTTOM)

row1 = Frame(keyboard)
row2 = Frame(keyboard)
row3 = Frame(keyboard)

row1.pack()
row2.pack()
row3.pack()

board = dynamicBoard()
#board = staticBoard()


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