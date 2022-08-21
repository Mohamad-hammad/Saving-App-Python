#Import the required Libraries
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x750")

#Create a canvas object
canvas= Canvas(win, width= 1000, height= 750)

#Add a text in Canvas
canvas.create_text(300, 50, text="Saving App", fill="black", font=('Helvetica 15 bold'))
canvas.create_text(300, 80, text="Add Title", fill="black", font=('Helvetica 10 bold'))
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()
canvas.create_text(300, 180, text="Add Amount", fill="black", font=('Helvetica 10 bold'))



canvas.pack()


win.mainloop()