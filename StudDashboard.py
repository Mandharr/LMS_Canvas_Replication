import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog as fdialog
import shutil
from tkinter import messagebox
import sqlite3
import os
import time



class StudDashMain:

    def __init__(self, master):
        self.parent = master
        self.studdashgui()

    def studdashgui(self):

        today = time.strftime("%m/%d/%Y")
        headerframe = LabelFrame(studdashroot, text="Welcome to the University of Bridgeport")
        headerframe.pack(fill="both", expand=False)

        headercontent = Label(headerframe, text="myUB Canvas : Student Login", font=('arial 15 bold'))
        headercontent.pack(fill="both", expand=False)

        self.img = Image.open(r"C:\Users\manda\AppData\Tkinter\cover.gif")
        self.img = self.img.resize((1500, 400), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)

        headerimage = Label(headerframe, text="myUB Canvas", image=self.img)
        headerimage.pack(fill="both", expand=False)

        mainframe = LabelFrame(studdashroot, text="WebAdvisor for Students", relief=RIDGE, bg="light yellow")
        mainframe.pack(fill="both", expand="yes")

        date =  Label(mainframe, text= "Todays Date : " + today, font=('arial 15 bold'), bg="light yellow").place(x=800, y = 20)

        dash = Button(mainframe, text="Logout", command=lambda: self.goLogin())
        dash.place(x=1700, y=30, height=50, width=100)

        files = Button(mainframe, text="Files", command=lambda: self.studFile())
        files.place(x=15, y=30, height=50, width=100)

        assignment = Button(mainframe, text="Assignment", command= lambda : self.studassign())
        assignment.place(x=15, y=80, height=50, width=100)

        grades = Button(mainframe, text="Transcripts", command= lambda : self.studgrades())
        grades.place(x=15, y=130, height=50, width=100)

        announ = Button(mainframe, text="Announcements", command= lambda : self.seeannoun())
        announ.place(x=15, y=180, height=50, width=100)

        showpeople = Button(mainframe, text="People", command=lambda: self.seepeople())
        showpeople.place(x=15, y=180, height=50, width=100)

        exitb = Button(mainframe, text="Exit", command= lambda: self.closewindow())
        exitb.place(x=1700, y=180, height=50, width=100)

    def seepeople(self):
        studdashroot.destroy()
        import StudentPeople

    def closewindow(self):
        exit()

    def goLogin(self):
        tkinter.messagebox.showinfo("BYE BYE", message="Logged of Successfully")
        studdashroot.destroy()
        import LoginPage

    def studFile(self):
        studdashroot.destroy()
        import FileHandlingStudent

    def seeannoun(self):
        studdashroot.destroy()
        import StudAnnoun

    def studassign(self):
        studdashroot.destroy()
        import StudentAssign

    def studgrades(self):
        studdashroot.destroy()
        import StudentseeGrade




studdashroot = Tk()
studapp = StudDashMain(studdashroot)
screen_width = studdashroot.winfo_screenwidth()
screen_height = studdashroot.winfo_screenheight()
screen_resolution = str(screen_width) + 'x' + str(screen_height)
studdashroot.geometry(screen_resolution)
studdashroot.title("Student Dashboard")
mainloop()
