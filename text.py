import tkinter as tk
from tkinter import *
import sys
import os
from tkinter import filedialog

root=Tk("Texteditor")
text=Text(root)
text.grid()
def saveas():
    global text
    t=text.get("1.0","end-1c")
    savelocation=filedialog.asksaveasfilename()
    file1=open(savelocation,"wt")
    file1.write(t)
    file1.close()

button=Button(root,text="save",command=saveas)
button.grid()
def fonthelvetica():
    global text
    text.config(font="Helvetica")
def fontcourier():
    global text
    text.config(font="courier")
font=Menubutton(root,text="Font").grid()
font.Menu=Menu(font,tearoff=0)
font["menu"]=font.menu
helvetica=IntVar()
courier=IntVar()
font.menu.add_checkbutton(label="courier",variable=courier,command=fontcourier)
font.menu.add_checkbutton(label="Helvetica",variable=helvetica,command=fonthelvetica)
root.mainloop()
