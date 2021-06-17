#importing library
from tkinter import *
from tkinter import ttk
window = Tk()

#Declaring Window Title
window.title("Registration Screen")

#Declaring Window size
window.geometry('600x400')

#Declaring Window Color
window.configure(background = "sky blue");

#below four fields are declared
Firstname = Label(window ,text = "First Name").grid(row = 0,column = 0)
LastName = Label(window ,text = "Last Name").grid(row = 1,column = 0)
Email = Label(window ,text = "Email Id").grid(row = 2,column = 0)
Mobile = Label(window ,text = "Contact Number").grid(row = 3,column = 0)
Address = Label(window ,text = "Address").grid(row = 4,column = 0)
City = Label(window ,text = "City").grid(row = 5,column = 0)
State = Label(window ,text = "State").grid(row = 6,column = 0)
Country = Label(window ,text = "Country").grid(row = 7,column = 0)
list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];
c=StringVar()
droplist=OptionMenu(window,c, *list1)
droplist.config(width=22)
c.set('SELECT YOUR COUNTRY')
droplist.grid(row = 7,column = 1)
Gender =Label(window ,text = "Gender").grid(row = 10,column = 0)
var = IntVar()
Radiobutton(window, text="Male",padx = 30, variable=var, value=1).grid(row = 10,column = 1)
Radiobutton(window, text="Female",padx = 20, variable=var, value=2).grid(row = 10,column = 3)
label_12 = Label(window, text="Programming")
label_12.grid(row = 14,column = 0)
var1 = IntVar()
Checkbutton(window, text="Java", variable=var1).grid(row = 14,column = 1)
var2 = IntVar()
Checkbutton(window, text="Python", variable=var2).grid(row = 14,column = 3)

Firstname1 = Entry(window).grid(row = 0,column = 1)
Lastname1 = Entry(window).grid(row = 1,column = 1)
Email1 = Entry(window).grid(row = 2,column = 1)
Mobile1 = Entry(window).grid(row = 3,column = 1)
Address1 = Entry(window).grid(row = 4,column = 1)
City1 = Entry(window).grid(row = 5,column = 1)
State1 = Entry(window).grid(row = 6,column = 1)


#fubction declaration
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=15,column=2)
window.mainloop()

