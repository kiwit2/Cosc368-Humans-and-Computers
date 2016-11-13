from tkinter import *
from tkinter.ttk import * 
from tkinter import messagebox
import getpass
import time
import random
import operator

class fittsBoard(object):
    def __init__(self, distances, widths):
        self.master = Tk()
        self.width = 800
        self.height = 600
        self.center = self.width/2
        self.distance = None
        self.distances = distances
        self.widths = widths
        self.green = 1
        self.index = 0
        self.file = open("experiment_fitts_log.txt","w")
        self.start = time.time()
        self.total = None
        self.pairs = {}
        self.reps = 2
        self.limit = None
        
        
    def setUp(self):
        self.c = Canvas(self.master, width=self.width, height=self.height)        
        self.c.pack()        
        self.c.config(background="white")
        distance =  self.distances[self.index]   
        width = self.widths[self.index]  
        self.distances = random.sample(self.distances, len(self.distances))
        self.widths = random.sample(self.widths, len(self.widths))
        new_dist = []
        new_wid = []
        i = 0
        c = len(self.distances)
        self.limit = c * self.reps
        while i < c:
            num = self.reps
            #num = random.randint(2, 6)
            if num%2 == 0:
                new_dist.append([self.distances[i]] * num)
                new_wid.append([self.widths[i]] * num)
                i += 1
        self.distances = [item for sublist in new_dist for item in sublist]      
        self.widths = [item for sublist in new_wid for item in sublist]
        print(self.distances)
        print(self.widths)
            
        leftbottom, lefttop, rightbottom, righttop = self.positions(distance, width)
        self.play(leftbottom, lefttop, rightbottom, righttop)
        
    def current(self):
        if self.index < self.limit:
            distance =  self.distances[self.index]   
            width = self.widths[self.index]
            return self.positions(distance, width)
        else:
            self.file.close()
            popup = messagebox.showinfo('Thank You','You have completed the test')
            self.master.destroy()
            
            
            return popup
        
    def play(self, leftbottom, lefttop, rightbottom, righttop):
        leftRect = self.c.create_rectangle(leftbottom, 0, lefttop, self.height, tag="left", fill="green", outline="green")
        rightRect = self.c.create_rectangle(rightbottom, 0, righttop, self.height, tag="right", fill="blue", outline="blue")
        self.c.tag_bind("left", "<ButtonPress-1>", self.leftClick)
        self.c.tag_bind("right", "<ButtonPress-1>",  self.rightClick)
        
        
    def positions(self, distance, width):
        leftbottom = self.center - distance
        rightbottom = self.center + distance
        lefttop = (self.center - distance) - width
        righttop = (self.center + distance) + width  
        return leftbottom, lefttop, rightbottom, righttop
    
    def leftClick(self, dummy):
        leftbottom, lefttop, rightbottom, righttop = self.current()
        if self.green == 1:
            self.log()
            self.c.itemconfigure("left", fill="blue", outline="blue")
            self.c.itemconfigure("right", fill="green", outline="green")
            self.c.coords("left", leftbottom, 0, lefttop, self.height)
            self.c.coords("right", rightbottom, 0, righttop, self.height)
            self.green = 0
            self.index += 1
            return 
        else:
            return
        
    def rightClick(self, dummy):
        leftbottom, lefttop, rightbottom, righttop = self.current()
        if self.green == 0:
            self.log()
            self.c.itemconfigure("right", fill="blue", outline="blue")
            self.c.itemconfigure("left", fill="green", outline="green")
            self.c.coords("right", rightbottom, 0, righttop, self.height)
            self.c.coords("left", leftbottom, 0, lefttop, self.height)            
            self.green = 1
            self.index += 1
            return 
        else:
            return        
    
    def isPair(self):
        pair = (self.distances[self.index], self.widths[self.index])
        if pair in self.pairs:
            self.pairs[pair] += 1
        if pair not in self.pairs:
            self.pairs[pair] = 0  
        return self.pairs[pair]    
        
    def log(self):
        
        self.total = (time.time() - self.start) * 1000
        self.file.write(str(getpass.getuser())+ " " + str(self.distances[self.index]) + 
                        " " + str(self.widths[self.index])+ " " + str(pairNum) + " " 
                        + str(round(self.total, 1)) + "\n" )   
        self.start = time.time()  
        return
        

if __name__=="__main__":
    distances = [64, 128, 256, 512]
    widths = [4, 8, 16, 32]
    
    go = fittsBoard(distances, widths)
    go.setUp()
    go.master.mainloop()