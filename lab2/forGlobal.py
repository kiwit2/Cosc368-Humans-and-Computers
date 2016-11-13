from tkinter import *
import time
import random

class forGlobal(object):
    def __init__(self, code, index):
        self.code = code
        self.index = index   
        self.timer = None
        self.total = 0
        self.mode = None
        self.file = None
        self.start = False
        #======windows-----------------
        self.window = Tk()
        self.fullFrame = None
        self.display = None
        self.keyboard = None
        self.row1 = None 
        self.row2 = None
        self.row3 = None
        self.targetlabel = None
        
    def screen(self):
        self.fullFrame = Frame(self.window, height=50, width=350, borderwidth=4)
        self.fullFrame.pack()
        
        self.display = Frame(self.fullFrame, height=30, width=350)
        self.display.pack_propagate(0)
        self.display.pack()
        
        self.targetlabel = Label(self.display, text="Press any key to start", width=30, font=20)
        self.targetlabel.pack(side=TOP)
        self.targetlabel.config(relief="sunken", background="white")        
        return
    
    def keys(self):
        self.keyboard = Frame(self.fullFrame, borderwidth=2, relief=RAISED)
        self.keyboard.pack(side=BOTTOM)        
        return