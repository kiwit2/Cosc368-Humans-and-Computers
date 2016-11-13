
from tkinter import *

def clear():
    txtDisplay.delete(0, END)
    return


currentTotal = ""

def btn(num):
    
    txtDisplay.insert(1000, num)
    return

      
root = Tk()
frame = Frame(root)
frame.pack()

root.title("Calculator")


num1 = StringVar()

topframe = Frame(root)
topframe.pack(side = TOP)

txtDisplay = Entry(frame, textvariable = num1, bd=20, insertwidth = 1, font = 30) #bd is border
txtDisplay.pack(side = TOP)

button1 = Button(topframe, padx=16, pady=16, bd=8, text="1", fg="black", command=lambda:btn("1"))
button1.pack(side =LEFT)
button2 = Button(topframe, padx=16, pady=16, bd=8, text="2", fg="black", command=lambda:btn("2"))
button2.pack(side =LEFT)
button3 = Button(topframe, padx=16, pady=16, bd=8, text="3", fg="black", command=lambda:btn("3"))
button3.pack(side =LEFT)
button4 = Button(topframe, padx=16, pady=16, bd=8, text="+", fg="black")
button4.pack(side =LEFT)

frame1 = Frame(root)
frame1.pack( side = TOP )

button1 = Button(frame1, padx=16, pady=16, bd=8, text="4", fg="black", command=lambda:btn("4"))
button1.pack(side =LEFT)
button2 = Button(frame1, padx=16, pady=16, bd=8, text="5", fg="black", command=lambda:btn("5"))
button2.pack(side =LEFT)
button3 = Button(frame1, padx=16, pady=16, bd=8, text="6", fg="black", command=lambda:btn("6"))
button3.pack(side =LEFT)
button4 = Button(frame1, padx=16, pady=16, bd=8, text="-", fg="black")
button4.pack(side =LEFT)

frame2 = Frame(root)
frame2.pack(side = TOP)

button1 = Button(frame2, padx=16, pady=16, bd=8, text="7", fg="black", command=lambda:btn("7"))
button1.pack(side =LEFT)
button2 = Button(frame2, padx=16, pady=16, bd=8, text="8", fg="black", command=lambda:btn("8"))
button2.pack(side =LEFT)
button3 = Button(frame2, padx=16, pady=16, bd=8, text="9", fg="black", command=lambda:btn("9"))
button3.pack(side =LEFT)
button4 = Button(frame2, padx=16, pady=16, bd=8, text="=", fg="black")
button4.pack(side =LEFT)

frame3 = Frame(root)
frame3.pack(side=TOP)

button1 = Button(frame3, padx=16, pady=16, bd=8, text="0", fg="black", command=lambda:btn("0"))
button1.pack(side =LEFT)
button2 = Button(frame3, padx=16, pady=16, bd=8, text="/", fg="black")
button2.pack(side =LEFT)
button3 = Button(frame3, padx=16, pady=16, bd=8, text="*", fg="black")
button3.pack(side =LEFT)
button4 = Button(frame3, padx=16, pady=16, bd=8, text="C", fg="black", command=clear)
button4.pack(side =LEFT)





root.mainloop()

