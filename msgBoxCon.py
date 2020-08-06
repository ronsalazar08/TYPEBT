#!/usr/bin/env python3
#import tkMessageBox
from tkinter import *
import subprocess as sp
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()
def closewindow(event=None):
    #sp.Popen(['python','test.py'])
    Messagebox.destroy()
def task():
    keyboard.press(Key.space)
    keyboard.release(Key.space)

Messagebox=Tk()
#Messagebox.attributes('-type', 'splash')
Messagebox.title(" ")
w = 400 # width for the Tk root
h = 220 # height for the Tk root

# get screen width and height
ws = Messagebox.winfo_screenwidth() # width of the screen
hs = Messagebox.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed

msg = '''Reconnected...'''

Messagebox.geometry('%dx%d+%d+%d' % (w, h, x, y))
l3=Label( Messagebox, text=msg)
l3.config(font=("Tahoma", 31, 'bold'), fg='green')
l3.place(relx=.5, rely=.5, anchor="c")
'''
b3=Button(Messagebox, text="Okay", command=closewindow)
b3.place(relx=.5, rely=.8, anchor="c")
b3.bind('<Return>', lambda _: closewindow())
b3.focus_set()
'''

Messagebox.after(2000, closewindow)

Messagebox.mainloop()
