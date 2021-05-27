# LISTBOX
import tkinter
from tkinter import *  

# from tkinter.ttk import *

master = Tk()
canvas = Canvas(master, width=500, height=500, borderwidth=0, highlightthickness=0)
canvas.pack()
cellwidth = 50
cellheight = 50
rect = {}
for column in range(20):
    for row in range(20):
        x1 = column*cellwidth
        y1 = row * cellheight
        x2 = x1 + cellwidth
        y2 = y1 + cellheight
        rect[row,column] = canvas.create_rectangle(x1,y1,x2,y2, fill="white", tags="rect")
master.mainloop()