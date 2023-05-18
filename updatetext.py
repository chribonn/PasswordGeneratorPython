# https://www.tutorialspoint.com/how-to-change-the-entry-widget-value-with-a-scale-in-tkinter

#Import the Tkinter Library
from tkinter import *
from tkinter import ttk

#Create an instance of Tkinter Frame
win = Tk()

#Set the geometry of window
win.geometry("700x350")

#Create an Integer Variable to set the initial value of Scale
var = IntVar(value=10)

#Create an Entry widget
entry = ttk.Entry(win,width= 45,textvariable=var)
scale = Scale(win, from_=10, to=200, width= 20, orient="horizontal", variable=var)

entry.place(relx= .5, rely= .5, anchor= CENTER)
scale.place(relx= .5, rely= .6, anchor = CENTER)

win.mainloop()