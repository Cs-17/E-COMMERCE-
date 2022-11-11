import tkinter as t
from tkinter import *
from tkinter import messagebox
from tkinter import Label
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import Frame
global wndw
def makeWindow():
    print()
    wndw=t.Tk()
    wndw.title("Shop Manager")
    global universalBg,universalFont
    universalBg="#8399c9"
    universalFont="Century Gothic"
    wndw.config(bg=universalBg)
    l=Label(wndw,text="Initialisation complete",font=(universalFont,20),bg=universalBg,fg="#8A307F", ).pack(side="top",padx=10,pady=10)
    #wndw.mainloop()
def done():
    messagebox.showinfo("showinfo", "Information")
'''def makeWindow():
    print()
    global wndw
    wndw=t.Tk()
    wndw.title("Shop Manager")
    global universalBg,universalFont
    universalBg="#8399c9"
    universalFont="Century Gothic"
    wndw.config(bg=universalBg)'''