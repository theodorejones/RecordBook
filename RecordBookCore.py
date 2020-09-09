import sys
import time
from datetime import datetime
import os
import sqlite3
from sqlite3 import Error
def sql_connect():
    try:
        con = sqlite3.connect('TimeSheet.db')
        return con
    except Error:
        print(Error)
def Unique(Record):
    l = len(Record)
    for i in range(0, l):
        unique = Record[i][0]#Capture a certain element's name
        count = 0#Number to be appended to make everything unique
        for j in range(i + 1, l):#Loop through everything after the captured element
            if Record[j][0] == unique:
                count = count + 1
                num=str(count)
                Record[j][0] = Record[j][0]+num#Make the entry unique
    return Record
def Sort(Record):
    l = len(Record)
    for i in range(1, l):#Loop through the list, repeat the process for every element
        for j in range(i + 1, l):#For every element, loop through the unsorted sublist
            if Record[j][1] <= Record[j - 1][1] :#Compare, if out of order:
                temp = Record[j]
                Record[j] = Record[j - 1]
                Record[j - 1] = temp#Swap
    return Record
def Time(Record, Name):
    Time = input('Please enter the time in format DD.MM.YYYY HH:MM:SS or press Enter to default to current time: ') or 'Now'
    try:
        if Time != 'Now':#Converts date to Epoch using time.strptime
            Pattern = '%d.%m.%Y %H:%M:%S'#Establishes date format
            Epoch = str(time.mktime(time.strptime(Time, Pattern)))
            confirm = input('Name Of Task: '+Name+'\nEpoch Time: '+Epoch+'\nIs this correct?(Y/N or Enter to default N, will only confirm if Y is entered)\n') or 'N'
            if confirm == 'Y':
                Record.append([Name, Epoch])
        elif Time == 'Now':
            Epoch = str(datetime.now().timestamp())#Current Epoch value
            confirm = input('Name Of Task: '+Name+'\nEpoch Time: '+Epoch+'\nIs this correct?(Y/N or Enter to default N, will only confirm if Y is entered)\n') or 'N'
            if confirm == 'Y':
                Record.append([Name, Epoch])
    except:#Account for bad date formats
        print('Please enter the date in format DD.MM.YYYY HH:MM:SS')
    return Record
def main():
    con = sql_connect()
    cursor = con.cursor()
    name = input("Please provide a database name: ")
    con.execute('create table if not exists name(Name text, StartTime integer, EndTime integer)')
    #Collect Activity Name, Start Time, and End Time
    #Display welcome message and directions for input or output selection
    print('Welcome to your record book! Please select from the list of functions and enter the appropriate integer:')
    Record = [['Name Of Task','Epoch Time']]
    select = 0
    while select != 4:#Loop the system while in use for the day
        try:
            select = int(input('1) Input Info\n2) Create Log File\n3) Read From File\n4) Exit\n'))
            if select == 1:
                Name = input('Please enter the name of your activity: ')#Ask for name
                Record = Time(Record, Name)#Use Time function
            if select == 2:
                Record = Sort(Record)#Sort by Epoch value
                Record = Unique(Record)#Ensure unique records
                name = input('Please name the file with file extension, suggested .csv: ')
                file = open(name,"w")#Open given file name
                for item in Record:#Input Record list
                    Text = item[0]+','+item[1]+'\n'
                    file.writelines([Text])
                file.close()
                Record = [['Name Of Task','Epoch Time']]#Reset Record list to prepare for next day
            if select == 3:
                try:#Account for bad file names
                    location = 'c:/Users/theod/Desktop/Python/Record Book'
                    files_in_dir = []
                    # r=>root, d=>directories, f=>files
                    for r, d, f in os.walk(location):
                        for item in f:
                            if '.py' not in item:
                                files_in_dir.append(os.path.join(r, item))
                    """for item in files_in_dir:
                        print(item.replace('c:/Users/theod/Desktop/Python/Record Book',''))"""
                    count = 0
                    selection = False
                    print('Press Enter to use the displayed file name, or enter symbol ] to cycle through available files')
                    while selection == False:
                        name1 = files_in_dir[count]
                        sys.stdout.write(name1)
                        choice = input() or 'Select'
                        if choice == 'Select':
                            selection = True
                        elif choice == ']':
                            selection = False
                            if count == len(files_in_dir)-1:
                                count = 0
                            else:
                                count = count + 1
                            sys.stdout.write(CURSOR_UP_ONE)
                            sys.stdout.write(ERASE_LINE)
                        else:
                            select = False
                            print('Invalid input')
                    Read = open(name1, 'r')#Open file for reading
                    print(Read.read())#Print file information in the shell
                except:
                    print('Invalid file name')
            if select <= 0 or select >=5:
                print('Please choose an integer between 1 and 4\n')        
        except:
            print('Please choose an integer between 1 and 4\n')#Error handling
    print('Goodbye!')
main()
