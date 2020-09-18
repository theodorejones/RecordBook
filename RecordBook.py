#Step One: TKInter with functional message line and four buttons
#Step Two: SQL Database w/ name
#Step Three: SQL Inputs
#Step Four: SQL Outputs
#Step Five: Process SQL Outputs to display time worked VS break time
#Step Six: Package for universal install and run
from tkinter import *
root = Tk()
root.title("Record Book")
root.geometry("350x200")
lbl = Label(root, text = "Welcome to the Record Book!")
lbl.grid(column=1, row=1)
def rest():
    lbl.configure(text = "On Break")
def work():
    lbl.configure(text = "At Work")
def sleep():
    lbl.configure(text = "Have a good night!")
def report():
    lbl.configure(text = "Still need to program that part")
brk = Button(root, text = "Break", fg = "red",command = rest)
wrk = Button(root, text = "Work", fg = "red",command = work)
slp = Button(root, text = "Sleep", fg = "red",command = sleep)
rpt = Button(root, text = "Report", fg = "red",command = report)
brk.grid(column=0,row=1)
wrk.grid(column=0,row=2)
slp.grid(column=0,row=3)
rpt.grid(column=0,row=4)
while(1):
    root.mainloop()
