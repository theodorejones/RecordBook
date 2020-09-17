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
lbl.grid()
def clicked():
    lbl.configure(text = "Button operational")
btn = Button(root, text = "Button", fg = "red",command = clicked)
btn.grid(column=1,row=0)
root.mainloop()
