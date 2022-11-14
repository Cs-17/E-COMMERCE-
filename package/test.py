import GUIhandler as g
def task():
    print("hello")
    g.window.after(5000, task())
g.window.after(5000,task())
g.window.mainloop()