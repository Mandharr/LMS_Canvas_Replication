import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3
import pypyodbc
import os
from tkinter import filedialog as fdialog
import shutil

cnxn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=MSI\SQLEXPRESS;"
                      "Database=Canvas;"
                      "Trusted_Connection=yes;")


mycursor = cnxn.cursor()

class Home:

    def __init__(self, master):
        self.parent=master
        self.gui()

    def gui(self):

        self.entryforusername=StringVar()
        self.entryforpassword=StringVar()

        headerframe = LabelFrame(Homeroot, text="Welcome to the University of Bridgeport")
        headerframe.pack(fill="both", expand=True)

        self.img1 = Image.open(r"C:\Users\manda\AppData\Tkinter\logo1.gif")
        self.img1 = self.img1.resize((400, 400), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(self.img1)

        headerimage = Label(headerframe, text="UB LOGO", image=self.img1)
        headerimage.pack(fill="both", expand=False)

        UserName = Label(Homeroot, text="Username:", font=('arial 15 bold'))
        UserName.place(x=800, y=450)

        entryforusername = Entry(Homeroot, textvariable=self.entryforusername).place(x=920, y=450)

        Password = Label(Homeroot, text="Password:", font=('arial 15 bold'))
        Password.place(x=800, y=480)

        entryforpassword = Entry(Homeroot, textvariable=self.entryforpassword, show="**",).place(x=920, y=480)

        enteradmin = Button(headerframe, text="Admin Login", command=lambda: self.btn_select_add())
        enteradmin.place(x=820, y=520, height=50, width=100)

        stud = Button(headerframe, text="Student Login", command=lambda: self.btn_select_stud())
        stud.place(x=1000, y=520, height=50, width=100)

        footer_frame = LabelFrame(Homeroot)
        footer_frame.pack(side="bottom", fill="both", expand=True)

        exitb = Button(footer_frame, text="Close Application", command=lambda: self.closewindow())
        exitb.place(x=850, y=10, height=50, width=200)

    def closewindow(self):
        exit()

    def btn_select_add(self):

        username = self.entryforusername.get()
        password = self.entryforpassword.get()

        sql = "select * from Login where Username=? and Password=? and isAdmin=1"

        val = (username, password)

        mycursor.execute(sql, val)
        print(mycursor.rowcount, "record selected.")
        #if (mycursor.rowcount == -1):
           # print(check)
           # print(username)
           # print(password)

        if username == "admin":
            tkinter.messagebox.showinfo("Welcome to Canvas", message="Logged-In as Admin")
            Homeroot.destroy()
            import AdminDashbaord

        else:
            tkinter.messagebox.showinfo("Error", message="Incorrect Credentials. Check Case type and Login type")

    def btn_select_stud(self):

        username = self.entryforusername.get()
        password = self.entryforpassword.get()

        user = username

        sql = "select * from LoginStudent where studentID=? and password=?"

        val = (username, password)

        mycursor.execute(sql, val)
        print(mycursor.rowcount, "record selected.")

        if (mycursor.rowcount == -1):
            tkinter.messagebox.showinfo("Welcome to Canvas", message="Logged-In as Student")
            Homeroot.destroy()
            import StudDashboard

        else:
            tkinter.messagebox.showinfo("Error", message="Incorrect Credentials. Check Case type and Login type")


Homeroot = Tk()
homeapp = Home(Homeroot)
screen_width = Homeroot.winfo_screenwidth()
screen_height = Homeroot.winfo_screenheight()
screen_resolution = str(screen_width) + 'x' + str(screen_height)
Homeroot.geometry(screen_resolution)
Homeroot.title("CANVAS Login")
mainloop()
