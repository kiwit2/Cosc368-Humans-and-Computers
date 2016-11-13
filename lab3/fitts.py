from tkinter import *
from tkinter.ttk import * 
from tkinter import messagebox
import getpass
import time
import random
import operator

class fitts(object):
    def __init__(self):
        self.index = 0
        self.distances = [64, 128, 256, 212]
        self.widths = [4, 8, 16, 32]        
        self.master = Tk()
        self.file = open("experiment_fitts_log.txt","w")
        self.reps = 2
        self.green = "left"
        self.repdict = {}
        self.start = time.time()
        self.setup()
        
    def setup(self):
        self.c = Canvas(self.master, width=800, height=600)        
        self.c.pack()        
        self.c.config(background="white") 
        leftbottom, lefttop, rightbottom, righttop = self.positions()
        leftRect = self.c.create_rectangle(leftbottom, 0, lefttop, 600,
                                    tag="left", fill="green", outline="green")
        rightRect = self.c.create_rectangle(rightbottom, 0, righttop, 600,
                                    tag="right", fill="blue", outline="blue")
        
        self.c.tag_bind("left", "<ButtonPress-1>", self.leftClick)
        self.c.tag_bind("right", "<ButtonPress-1>",  self.rightClick) 
        
    def leftClick(self, dummy):
        if self.green == "left":
            
            leftbottom, lefttop, rightbottom, righttop = self.positions()
            self.c.itemconfigure("left", fill="blue", outline="blue")
            self.c.itemconfigure("right", fill="green", outline="green")
            self.c.coords("left", leftbottom, 0, lefttop, 600)
            self.c.coords("right", rightbottom, 0, righttop, 600)
            self.green = "right"
            
            return 
        else:
            return
        
    def rightClick(self, dummy):
        if self.green == "right":
            
            leftbottom, lefttop, rightbottom, righttop = self.positions()
            self.c.itemconfigure("right", fill="blue", outline="blue")
            self.c.itemconfigure("left", fill="green", outline="green")
            self.c.coords("right", rightbottom, 0, righttop, 600)
            self.c.coords("left", leftbottom, 0, lefttop, 600)            
            self.green = "left"
            
            return 
        else:
            return            
                  
    def positions(self):
        index = self.index
        if index == len(self.distances):
            self.file.close()
            popup = messagebox.showinfo('Thank You','You have completed the test')
            self.master.destroy()    
            return popup        
        
        pos = (self.distances[index], self.widths[index])
        if pos in self.repdict:
            if self.repdict[pos] == (self.reps - 1):
                self.log()
                self.index += 1
                
                
            else:
                self.repdict[pos] += 1
                self.log()
        else:
            self.repdict[pos] = 0
            self.log()
        center = 400
        leftbottom = center - self.distances[self.index]
        rightbottom = center + self.distances[self.index]
        lefttop = (center - self.distances[self.index]) - self.widths[self.index]
        righttop = (center + self.distances[self.index]) + self.widths[self.index] 
        return leftbottom, lefttop, rightbottom, righttop        
    
    def log(self):
        pos = (self.distances[self.index], self.widths[self.index])   
        self.total = (time.time() - self.start) * 1000
        self.file.write(str(getpass.getuser())+ " " + str(self.distances[self.index]) + 
                        " " + str(self.widths[self.index])+ " " + str(self.repdict[pos]) + " " 
                        + str(round(self.total, 1)) + "\n" )   
        self.start = time.time()  
        return    
    
if __name__ == "__main__":
    go = fitts()
    go.master.mainloop()