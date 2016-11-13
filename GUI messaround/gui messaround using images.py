from tkinter import *

root = Tk()


photo = PhotoImage(file="canvas.png")
label = Label(root, image=photo)
label.pack()

root.mainloop()