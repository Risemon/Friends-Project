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




b = Button(root, text="hi").grid(row=0, column=0)
#Comand for things to run
def hello():
    print("Hello")
#Defining the main menu
bar = Menu(root)
#defining the first dropdown menu
filebar = Menu(bar, tearoff=0)
clientbar = Menu(bar, tearoff=0)
#Adding an item to the dropdown menu
filebar.add_command(label="Open", command=hello)
filebar.add_command(label="Save", command=hello)
clientbar.add_command(label="New Client", command=newclient)
clientbar.add_command(label="Client Status", command=hello)
clientbar.add_command(label="Edit Client Information", command=hello)
#Adding the new dropdown menu to the full menu bar
bar.add_cascade(label="File", menu=filebar)
bar.add_cascade(label="Client", menu=clientbar)
#Display the menu
root.config(menu=bar)


frame = Frame(width=500, height=250).grid(row=0, column=0, rowspan=20, columnspan=20)
root.mainloop()
