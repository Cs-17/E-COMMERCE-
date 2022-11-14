from tkinter import *
import tkinter
window=Tk()
window.title("Mountain Stores")

x_axis=(window.winfo_screenwidth())
y_axis=(window.winfo_screenheight())

winx=int(x_axis*0.7)
winy=int(y_axis*0.7)

window.geometry("{}x{}".format(winx,winy))
window.resizable(False,False)
window.attributes('-topmost', 1)
#bgimg=tkinter.PhotoImage(file="./EXTRAS/logo.jpg")
#l1=Label(window,i=bgimg)
#l1.pack()
window.configure(bg='yellow')
window.iconbitmap('./EXTRAS/logo.ico')
window.mainloop()











"""
  makeWindow():
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
def makeWindow():
    print()
    global wndw
    wndw=t.Tk()
    wndw.title("Shop Manager")
    global universalBg,universalFont
    universalBg="#8399c9"
    universalFont="Century Gothic"
    wndw.config(bg=universalBg)
    """