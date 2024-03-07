from tkinter import *
import tkinter.messagebox
root = Tk()



root.geometry("700x400")

def getvals():
    window = tkinter.Tk()
    window.wm_withdraw()
    tkinter.messagebox.showinfo(title="Message",message="Data stored successfully!")
    window.destroy()

Label(root, text="Registration form",font="lucida 16 italic",bg="cyan",fg="blue").grid(row=0,column=15)
var = IntVar()

name = Label(root,text="Name:-",font="ar 14 italic",fg="blue")
contact = Label(root,text="Phone:-",font="ar 14 italic",fg="blue")
gender = Label(root,text="Gender:-",font="ar 14 italic",fg="blue")
age = Label(root,text="Age:-",font="ar 14 italic",fg="blue")

name.grid(row=3,column=2)
contact.grid(row=4,column=2)
gender.grid(row=5,column=2)
age.grid(row=6,column=2)

namevalue = StringVar
contactvalue = IntVar
gendervalue = StringVar
agevalue = IntVar

nameentry= Entry(root, textvariable=namevalue)
contactentry= Entry(root, textvariable=contactvalue)
genderentry1= Radiobutton(root,text="male",variable=var,value=1)
genderentry2= Radiobutton(root,text="female",variable=var,value=2)
ageentry= Entry(root, textvariable=agevalue)

nameentry.grid(row=3,column=3)
contactentry.grid(row=4,column=3)
genderentry1.grid(row=5,column=3)
genderentry2.grid(row=5,column=4)
ageentry.grid(row=6,column=3)

Button(text="Submit",bg="green",command=getvals).grid(row=9,column=3)

root.mainloop() 


