#New Plan: Reorganize all of this to be a one-button, one text entry command-line setup
#step One: Establish one text field, one button, and one text input
#Step Two: Use state machines and global variables to operate the code from within the one button push command
from tkinter import *
  
# import messagebox class from tkinter 
from tkinter import messagebox 
  
# global list is declare for storing all text
text_list = [] 

# global variable is declare for state machine
state = 0

#Default name
default_name = "User"
  
# Function for checking input error when 
# empty input is given in task field 
def inputError() : 
      
    # check for enter task field is empty or not 
    if enterTaskField.get() == "" : 
          
        # show the error message 
        messagebox.showerror("Input Error") 
          
        return 0
      
    return 1
  
# Function for clearing the contents 
# of task number text field 
def clear_taskNumberField() : 
      
    # clear the content of task number text field 
    taskNumberField.delete(0.0, END) 
  
# Function for clearing the contents 
# of task entry field    
def clear_taskField() : 
  
    # clear the content of task field entry box 
    enterTaskField.delete(0, END) 
#Connect to a database of a certain name
def Login(): 
  
    global state
      
    # check for error 
    value = inputError() 
  
    # if error occur then return 
    if value == 0 : 
        return
  
    # get the task string concatenating 
    # with new line character 
    content = enterTaskField.get() + "\n"
    print(content)
    if(state == 0):
        writeLine("5) Exit \n")
        writeLine("4) Remove User \n")
        writeLine("3) Report Break Time \n")
        writeLine("2) Add Task \n")
        writeLine("1) Login \n")
        if(enterTaskField.get() == "1"):
            state = 1
        if(enterTaskField.get() == "2"):
            state = 2
        if(enterTaskField.get() == "3"):
            state = 3
        if(enterTaskField.get() == "4"):
            state = 4
        if(enterTaskField.get() == "5"):
            state = 5
    if(state == 1):
        writeLine("State 1")
        state = 0
    if(state == 2):
        writeLine("State 2")
        state = 0
    if(state == 3):
        writeLine("State 3")
        state = 0
    if(state == 4):
        writeLine("State 4")
        state = 0
    if(state == 5):
        writeLine("State 5")
        state = 0
    
def writeLine(content):
    # store task in the list 
    text_list.append(content) 
  
    # insert content of task entry field to the text area 
    TextArea.insert('1.0', content) 
  
    # function calling for deleting the content of task field 
    clear_taskField()
      
  
# Driver code  
if __name__ == "__main__" : 
  
    # create a GUI window 
    gui = Tk() 
  
    # set the background colour of GUI window  
    gui.configure(background = "light green") 
  
    # set the title of GUI window 
    gui.title("Record Book") 
  
    # set the configuration of GUI window  
    gui.geometry("250x350") 
  
    # create a label : Enter Your Task 
    enterTask = Label(gui, text = "Enter Your Task or Name", bg = "light green") 
  
    # create a text entry box  
    # for typing the task 
    enterTaskField = Entry(gui) 
  
    # create a Submit Button and place into the root window 
    # when user press the button, the command or  
    # function affiliated to that button is executed  
    Login = Button(gui, text = "Enter", fg = "Black", bg = "Red", command = Login)
  
    # create a text area for the root 
    # with lunida 13 font 
    # text area is for writing the content 
    TextArea = Text(gui, height = 10, width = 25, font = "lucida 13") 
  
    # grid method is used for placing  
    # the widgets at respective positions  
    # in table like structure. 
    enterTask.grid(row = 0, column = 2) 
  
    # ipadx attributed set the entry box horizontal size                
    enterTaskField.grid(row = 1, column = 2, ipadx = 50) 
                         
    Login.grid(row = 2, column = 2)
          
    # padx attributed provide x-axis margin  
    # from the root window to the widget. 
    TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)

    line1 = "Welcome to the Record Book!\n"
    line2 = "1) Login\n"
    line3 = "2) Add Task\n"
    line4 = "3) Report Break Time\n"
    line5 = "4) Delete User\n"
    line6 = "5) Exit\n"
    text_list.append(line6)
    TextArea.insert('1.0', line6)
    text_list.append(line5)
    TextArea.insert('1.0', line5)
    text_list.append(line4)
    TextArea.insert('1.0', line4)
    text_list.append(line3)
    TextArea.insert('1.0', line3)
    text_list.append(line2)
    TextArea.insert('1.0', line2)
    text_list.append(line1)
    TextArea.insert('1.0', line1)



    # start the GUI  
    gui.mainloop() 
