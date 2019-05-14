from tkinter import *
from tkinter import ttk
from compile import *
window = Tk()
window.title("Welcome to TutorialsPoint")
window.geometry('400x400')
window.configure(background = "grey");
a1 = Text(window)
a1.grid(row = 0,column = 1, rowspan=10,sticky="nwse")
def check():
  compile = Compile()
  compile.setSrc(a1.get("1.0",END))
btn = ttk.Button(window ,text="Submit", command=check).grid(row=4,column=0)
window.mainloop()
