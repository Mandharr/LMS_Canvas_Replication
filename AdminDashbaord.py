import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog as fdialog
import shutil
from tkinter import messagebox
import sqlite3
import os


class AdDashMain:

    def __init__(self, master):
        self.parent = master
        self.admindashgui()

    def admindashgui(self):

        headerframe = LabelFrame(admindashroot, text="Welcome to the University of Bridgeport")
        headerframe.pack(fill="both", expand=False)

        headercontent = Label(headerframe, text="myUB Canvas : Administrator Login", font=('arial 15 bold'))
        headercontent.pack(fill="both", expand=False)

        self.img = Image.open(r"C:\Users\manda\AppData\Tkinter\cover.gif")
        self.img = self.img.resize((1500, 400), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)

        headerimage = Label(headerframe, text="myUB Canvas", image=self.img)
        headerimage.pack(fill="both", expand=False)

        mainframe = LabelFrame(admindashroot, text="WebAdvisor for Students", bg="light yellow")
        mainframe.pack(fill="both", expand="yes")

        dash = Button(mainframe, text="Logout", command=lambda: self.goLogin())
        dash.place(x=1700, y=30, height=50, width=100)

        files = Button(mainframe, text="Files", command=lambda: self.adminfile())
        files.place(x=15, y=30, height=50, width=100)

        assignment = Button(mainframe, text="Assignment", command=lambda: self.adminassign())
        assignment.place(x=15, y=80, height=50, width=100)

        grades = Button(mainframe, text="Transcripts", command=lambda: self.admingrades())
        grades.place(x=15, y=130, height=50, width=100)

        people = Button(mainframe, text="Add Students", command= lambda: self.addstud())
        people.place(x=15, y=180, height=50, width=100)

        announ = Button(mainframe, text="Announcements", command= lambda: self.goAnnoun())
        announ.place(x=15, y=230, height=50, width=100)

        exitb = Button(mainframe, text="Exit", command= lambda: self.closewindow())
        exitb.place(x=1700, y=180, height=50, width=100)


        courselist = Label(mainframe, text="Available Courses", font=('arial 15 bold'), bg="light yellow").place(x=200, y=30)
        CPSC = Label(mainframe, text="CPSC 422 : Python Programming", font=('arial 15 italic'), bg="light yellow").place(x=220, y=60)
        TM = Label(mainframe, text="TCMG 645 : Technology New Venture Creation", font=('arial 15 italic'),bg="light yellow").place(x=220, y=100)

    def addstud(self):
        admindashroot.destroy()
        import AdminAddPeo

    def admingrades(self):
        admindashroot.destroy()
        import StudentGrade

    def adminfile(self):
        admindashroot.destroy()
        import FileHandlingAdmin

    def adminassign(self):
        admindashroot.destroy()
        import AdminAssign

    def goAnnoun(self):
        admindashroot.destroy()
        import Announcements

    def goLogin(self):
        tkinter.messagebox.showinfo("BYE BYE", message="Logged of Successfully")
        admindashroot.destroy()
        import LoginPage

    def closewindow(self):
        exit()




admindashroot = Tk()
adapp = AdDashMain(admindashroot)
screen_width = admindashroot.winfo_screenwidth()
screen_height = admindashroot.winfo_screenheight()
screen_resolution = str(screen_width) + 'x' + str(screen_height)
admindashroot.geometry(screen_resolution)
admindashroot.title("Admin Dashboard")
mainloop()
