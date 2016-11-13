from tkinter import *
import time
import random
import getpass
import string 

#----------------------------------------------test display and keyboard=====

class forGlobal(object):
    """Creates the test display and keyboard"""
    def __init__(self, index):
        self.code = []
        while len(self.code) < 6:
            letter = random.choice(string.ascii_lowercase)     
            if letter not in self.code:
                self.code.append(letter)
        print(self.code)        
        self.index = index   
        self.total = 0
        self.mode = None
        self.file = None
        self.start = False
        self.charlist = []
        self.chardict = {}
        self.total = None
        #======windows-----------------
        self.window = Tk()
        self.window.wm_title("welcome to the test")
        self.fullFrame = None
        self.display = None
        self.keyboard = None
        self.row1 = None 
        self.row2 = None
        self.row3 = None
        self.targetlabel = None
        
    #-----------creates the screen of the display----------------------------
    
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
    
    #---------------------creates the keys for the keyboard------------------
    
    def keys(self):
        self.keyboard = Frame(self.fullFrame, borderwidth=2, relief=RAISED)
        self.keyboard.pack(side=BOTTOM) 
        
        self.row1 = Frame(self.keyboard)
        self.row2 = Frame(self.keyboard)
        self.row3 = Frame(self.keyboard)
        
        self.row1.pack()
        self.row2.pack()
        self.row3.pack()        
        return
    
    #-----------------shuffles the keys around in a dynamic search-----------
    
    def shuffleKeys(self):
        self.keyboard.destroy()
        self.keys()
        board = dynamicBoard()
        row = [g.row1,g.row2,g.row3]
        rowIndex = 0
        for line in board:
            random.shuffle(line)
            for letter in line:
                f = Frame(row[rowIndex], height=32, width=32)
                f.pack_propagate(0)
                f.pack(side=LEFT)
                button = Button(f, text=letter, command=lambda x=letter: keypress(x))
                button.pack( fill=BOTH, expand=1)
            rowIndex += 1            

    #-----------------creates the overall test (THIS IS THE MAIN FUNCTION)---        

    def test(self):
        self.screen()
        self.keys()
       
        row = [self.row1,self.row2,self.row3]
        rowIndex = 0
        
        for line in self.board:
            for letter in line:
                f = Frame(row[rowIndex], height=32, width=32)
                f.pack_propagate(0)
                f.pack(side=LEFT)
                button = Button(f, text=letter, command=lambda x=letter: keypress(x))
                button.pack( fill=BOTH, expand=1)
            rowIndex += 1        
        
#-------------------------When a key is pressed this function is returned----        

def keypress(var):
    if g.start == False:
        g.targetlabel.config(text=g.code[g.index])
        g.start = time.time()
        return
        
    limit = 36
    if var == g.code[g.index % 6]:
        if g.index % 6 == 0:
            a = list(g.code)
            random.shuffle(a)
            c = "".join(a)
            g.code = c
        if g.mode == "dynamic":
            g.shuffleKeys()
        
        if var in g.charlist:
            g.chardict[var] += 1
        
        if var not in g.charlist:
            g.chardict[var] = 1
            g.charlist.append(var)
        
        g.total = (time.time() - g.start) * 1000
        g.file.write(str(getpass.getuser())+ " " + g.mode + " " + var+ " " + 
                     str(g.chardict[var]) + " " + str(round(g.total, 1)) + "\n" )
        g.start = time.time() 
        g.index += 1
        g.targetlabel.config(text=g.code[g.index % 6])
        if g.index >= limit:
            g.file.close()
            g.window.destroy()
        return
    else:    
        return

#----if a user has chosen a dynamic mode this is the board that will be set--     

def dynamicBoard():
    keys = list("qwertyuiopasdfghjklzxcvbnm")
    random.shuffle(keys)
    a = keys[0:10]
    b = keys[10:19]
    c = keys[19:26]
        
    g.mode = "dynamic"
    board = [a, b, c] 
    if g.file == None:
        g.file = open("experiment_dynamic_log.txt","w")
        return board
    return board

#-----if the user has chosen a static mode this is the keyboard that is set--

def staticBoard():
    board = ["qwertyuiop","asdfghjkl","zxcvbnm"]
    g.mode = "static"
    g.file = open("experiment_static_log.txt","w")
    return board
    
#------------------------------------start the test--------------------------
       
if __name__ == "__main__":
        
    g = forGlobal(0) 
    g.board = dynamicBoard()
    #g.board = staticBoard()    
    g.test()
    g.window.mainloop()     