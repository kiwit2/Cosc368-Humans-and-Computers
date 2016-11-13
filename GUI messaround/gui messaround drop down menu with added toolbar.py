from tkinter import *

def doNothing():
    print("ok ok I won't...")

root = Tk()

# ******main meny 

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="new project...", command=doNothing)
subMenu.add_command(label="new...", command=doNothing)
subMenu.add_separator()   #adds line between new and exit
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="edit", menu=editMenu)
editMenu.add_command(label="redo", command=doNothing)

# ****** the toolbar

toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)


root.mainloop()