import time
import os
import sys
from tkinter import *
from PIL import Image, ImageTk
from itertools import count

def move_window(event):
    root.geometry(f'+{event.x_root}+{event.y_root}')

# creating Tk window
root = Tk()


root.overrideredirect(1) # Remove shadow & drag bar. Note: Must be used before wm calls otherwise these will be removed.

root.call("wm", "attributes", ".", "-topmost", "true") # Always keep window on top of others
root.configure(cursor="fleur")
root.geometry("261x195+55+666") # Set offset from top-left corner of screen as well as size

# setting geometry of tk window

# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
root.title("Bard-Diet")
  
# Declaration of variables
minute=StringVar()
second=StringVar()

# setting the default value as 0
minute.set("00")
second.set("01")

# Use of Entry class to take input from the user
minuteEntry= Entry(root, width=2, font=("calibri",15,""), justify='center', textvariable=minute, bd='0', cursor="left_ptr")
minuteEntry.grid(row = 0, column = 2, padx =  2, pady = 2, sticky='nesw')

secondEntry= Entry(root, width=2, font=("calibri",15,""), justify='center', textvariable=second, bd='0', cursor="left_ptr")
secondEntry.grid(row = 1, column = 2, padx =  2, pady = 2, sticky='nesw')
  
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


frames = [PhotoImage(file='2.gif',format = 'gif -index %i' %(i)) for i in range(14)]
img = Button(root, bd='-2', cursor="left_ptr", command = restart_program)

def update(ind):
    frame = frames[ind]
    ind += 1
    time.sleep(0.1)
    print(ind)
    if ind>14: #With this condition it will play gif infinitely
        ind = 0
    img.configure(image=frame)
    root.after(14, update, ind)

def playani():
    root.after(0, update, 0)

def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60) 
  
        # Converting the input entered in mins or secs,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)         
        # using format () method to store the value up to 
        # two decimal places
        minute.set("{0:0>2}".format(mins))
        second.set("{0:0>2}".format(secs))
        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            #root.configure(background='red')
            playani()

        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1

Label(root, text="Minute", font=("calibri",9,""), justify=LEFT, bd='-2').grid(row=0, rowspan = 1, padx =  4, pady = 8, sticky='nesw')
Label(root, text="Second", font=("calibri",9,""), justify=LEFT, bd='-2').grid(row=1, rowspan = 1, padx =  4, pady = 8, sticky='nesw')

#icon1 = ImageTk.PhotoImage(Image.open('1.gif'))
icon1 = ImageTk.PhotoImage(Image.open('2.gif'))
img = Label(root, image = icon1, bd='-2', cursor="left_ptr")
# command = restart_program)
img.grid(row = 0, column = 3, rowspan = 2)

# button widget
btn = Button(root, text='[Start]', font=("calibri",9,""), bd='-2', cursor="left_ptr", command = submit)
btn.grid(row = 2, column = 0, padx =  22, pady = 4, sticky='nesw')
# Reset 
btn1 = Button(root, text = '[Reset]', font=("calibri",9,""), bd='-2', cursor="left_ptr", command = restart_program)
btn1.grid(row = 2, column = 2, padx =  1, pady = 1, sticky='nesw')
# Quit 
btn2 = Button(root, text = '[Quit]', font=("calibri",9,""), bd='-2', cursor="X_cursor", command = root.destroy) 
btn2.grid(row = 2, column = 3, padx =  33, pady = 4, sticky='nesw')

root.bind("<B1-Motion>", move_window)

# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()