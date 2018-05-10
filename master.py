import tkinter as tk
from tkinter import *

root = tk.Tk()
fields = []
def clearer():
    #Removes all widgets from the screen
    for item in root.grid_slaves():
        item.grid_remove()
    frame = Frame(width=500, height=250).grid(row=0, column=0, rowspan=20, columnspan=20)

def allfill():
    global fields
    print(fields)
    if "" or '' in fields:
        print("missing value")

def newclient():
    clearer()
    #Setup the window to enter the information for a new client
    names = Label(root, text="First name", anchor="w", justify=LEFT).grid(row=0, column=0, sticky="w", padx=5)
    name = StringVar()
    names2 = Entry(root, textvariable=name).grid(row=1, column=0)
    lasts = Label(root, text="Last name").grid(row=0, column=1, sticky="w", padx=5)
    last = StringVar()
    lasts2 = Entry(root, textvariable=last).grid(row=1, column=1)
    adresss = Label(root, text="Adress").grid(row=2, column=0, sticky="w", padx=5)
    adress = StringVar()
    adress2 = StringVar()
    adresss2 = Entry(root, textvariable=adress).grid(row=3, column=0, columnspan=2, sticky="we", padx=5)
    adresss3 = Entry(root, textvariable=adress2).grid(row=4, column=0, columnspan=2, sticky="we", padx=5)
    citys = Label(root, text="City").grid(row=5, column=0, sticky="w", padx=5)
    city = StringVar()
    citys2 = Entry(root, textvariable=city).grid(row=6, column=0, columnspan=2, sticky="we", padx=5)
    states = Label(root, text="State").grid(row=7, column=0, sticky="w", padx=5)
    state = StringVar()
    states2 = Entry(root, textvariable=state).grid(row=8, column=0)
    zips = Label(root, text="Zip Code").grid(row=7, column=1, sticky="w", padx=5)
    zipcode = StringVar()
    zips2 = Entry(root, textvariable=zipcode).grid(row=8, column=1)
    nextb = Button(root, text="next", command=lambda:nextpagenew()).grid(row=0, column=5, sticky="w")
    global fields
    def nextpagenew():
        global fields
        fields = [name.get(), last.get(), adress.get(), adress2.get(), city.get(), state.get(), zipcode.get()]
        print(name.get())
        print(fields)
        allfill()
        clearer()
    
def editclient():
    pass
    #This will be a copy of newclient() but the textvariables will use the get()
    #method to obtain all of the current information

def adminpage():
    clearer()
    AdminL = Label(root, text="Confirm Admin Password").grid(row=5, column=0, columnspan=20, rowspan=5)
    global adminp
    adminp = StringVar()
    PassE = Entry(root, textvariable=adminp).grid(row=7, column=0, columnspan=20, rowspan=5)
    login = Button(root, text="Login", command=lambda:admincheck()).grid(row=10, column=0, columnspan=20, rowspan=5)
    def admincheck():
        x = open("Passwords.txt", "r")
        for line in x:
            y = line
            y = y.split()
            global adminp
            if adminp.get() == y[1]:
                adminpager()
            else:
                false = Label(root, text="Wrong username or password").grid(row=0, column=0, columnspan=20, rowspan=5)
            x.close()
            break
    def adminpager():
        clearer()
        title = Label(root, text="Administrator actions").grid(row=0, column=0, columnspan=20, rowspan=5)
        new_password = Button(root, text="Add a new username and password", command=lambda:create_user()).grid(row=2, column=0, columnspan=10, rowspan=5, sticky="e")
        del_password = Button(root, text="Remove a username and password").grid(row=2, column=10, columnspan=10, rowspan=5, sticky="w")
    def create_user():
        clearer()
        x = open("Passwords.txt", "a")
        usern = StringVar()
        passn = StringVar()
        UserL = Label(root, text="New Username").grid(row=0, column=0, columnspan=20, rowspan=5)
        UserE = Entry(root, textvariable=usern).grid(row=2, column=0, columnspan=20, rowspan=5)
        PassL = Label(root, text="New Password").grid(row=5, column=0, columnspan=20, rowspan=5)
        PassE = Entry(root, textvariable=passn).grid(row=7, column=0, columnspan=20, rowspan=5)
        final = Button(root, text="Create user", command=lambda:creater()).grid(row=9, column=0, columnspan=20, rowspan=5)
        def creater():
            x.write("\n" + usern.get() + " " + passn.get())
            x.close()
            clearer()
            results = Label(root, text="New user created").grid(row=0, column=0, columnspan=20, rowspan=5)

        
def beginmenu():
    def hello():
        print("Hi")
    clearer()
    #Defining the main menu
    bar = Menu(root)
    #defining the first dropdown menu
    filebar = Menu(bar, tearoff=0)
    clientbar = Menu(bar, tearoff=0)
    helpbar = Menu(bar, tearoff=0)
    #Adding an item to the dropdown menu
    filebar.add_command(label="Open", command=hello)
    filebar.add_command(label="Save", command=hello)
    clientbar.add_command(label="New Client", command=newclient)
    clientbar.add_command(label="Client Status", command=hello)
    clientbar.add_command(label="Edit Client Information", command=hello)
    helpbar.add_command(label="Program Instructions", command=hello)#Clear the screen and add a few pages of text that help the user learn how this program works
    helpbar.add_command(label="Admin", command=adminpage)
    #Adding the new dropdown menu to the full menu bar
    bar.add_cascade(label="File", menu=filebar)
    bar.add_cascade(label="Client", menu=clientbar)
    bar.add_cascade(label="Help", menu=helpbar)
    #Display the menu
    root.config(menu=bar)

def login():
    x = open("Passwords.txt", "r")
    def check():
        for line in x:
            y = line
            y = y.split()
            if y[0] == username.get():
                if y[1] == password.get():
                    return True
    if check():
        x.close()
        beginmenu()
    else:
        false = Label(root, text="Wrong username or password").grid(row=0, column=0, columnspan=20, rowspan=5)
    x.close()

frame = Frame(width=500, height=250).grid(row=0, column=0, rowspan=20, columnspan=20)
UserL = Label(root, text="Username").grid(row=2, column=0, columnspan=20, rowspan=5)
username = StringVar()
UserE = Entry(root, textvariable=username).grid(row=4, column=0, columnspan=20, rowspan=5)
PassL = Label(root, text="Password").grid(row=7, column=0, columnspan=20, rowspan=5)
password = StringVar()
PassE = Entry(root, textvariable=password).grid(row=9, column=0, columnspan=20, rowspan=5)
OK = Button(root, text="Log In", command=lambda:login()).grid(row=12, column=0, columnspan=20, rowspan=5)

root.mainloop()
