print("Sinh viên: Ngo Duc Thang")
print("Ma so Sv: 245751030310019")
print("########################")

from tkinter import *

def NewFile():
    print("New File!")
def OpenFile():
    print("Open File!")
def InsertText():
    print("InsertText")
def InsertPicture():
    print("InsertPicture")
def About():
    print("This is a simple example of a menu")
    
root = Tk() 
menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label="File", menu=filemenu) 
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator() 
filemenu.add_command(label="Exit", command=root.quit)

insertmenu = Menu(menu) 
menu.add_cascade(label="Insert", menu=insertmenu) 
insertmenu.add_command(label="Text", command=InsertText)
insertmenu.add_command(label="Picture", command=InsertPicture)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu) 
helpmenu.add_command(label="About...", command=About) 

root.mainloop()
 

