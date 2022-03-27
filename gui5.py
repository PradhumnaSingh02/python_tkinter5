from tkinter import *

def getvalue():
    print("The name of user is", uservalue.get())
    print("The password of user is", passwordvalue.get())

root = Tk()
root.title('Width and Layout')
root.geometry('655x333')


#frame = Frame(root, borderwidth=5, bg='Black', relief=SUNKEN)
#frame.pack(side=LEFT, anchor='nw')
name = Label(root, text='Name')
password = Label(root, text='Password')
name.grid()
password.grid()
# variable class in tkinter
# BooleanVar,DoubleVar,IntVar,StringVar
uservalue = StringVar()
passwordvalue = StringVar()

userEntry = Entry(root, textvariable=uservalue)
passwordentry = Entry(root, textvariable=passwordvalue)

userEntry.grid(row=0, column=1)
passwordentry.grid(row=1, column=1)

Button(text="Submit", command=getvalue).grid()


root.mainloop()