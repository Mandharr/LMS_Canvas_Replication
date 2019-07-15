import tkinter
from tkinter import messagebox
import tkinter as tk
from tkinter import Button
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from tkinter import *
import pypyodbc

cnxn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=MSI\SQLEXPRESS;"
                        "Database=Canvas;"
                        "Trusted_Connection=yes;")


class MainClass:

    def __init__(self, master):
        self.parent = master
        self.gradegui()

    def gradegui(self):
        self.Variable=StringVar()
        self.Variable2=StringVar()
        self.Variable3=StringVar()
        self.Variable4=StringVar()

        header = LabelFrame(graderoot, text="See Students Scores").pack(fill="both", expand=True)

        dash = Button(graderoot, text="Logout", command=lambda: self.goLogin())
        dash.place(x=1700, y=20, height=50, width=100)

        exitb = Button(header, text="Exit", command=lambda: self.closewindow())
        exitb.place(x=1800, y=20, height=50, width=100)

        Subject = Label(header, text="Course # :", font=('', 15)).place(x=10, y=20)

        EntryForSubject = Entry(header, bd=5, textvariable=self.Variable).place(x=300, y=20, width=250)

        AssingmentNumber = Label(header, text="Assignment #:", font=('', 15)).place(x=10,y=60)

        EntryForAssingmentNumber = Entry(header, bd=5, textvariable=self.Variable2).place(x=300, y=60, width=250)

        StudentId = Label(header, text="Student ID:", font=('', 15)).place(x=10, y=100)

        EntryForStudentId = Entry(header, bd=5, textvariable=self.Variable3).place(x=300, y=100, width=250)

        Button_Submit = Button(header, text="See Assignment Grades", command= lambda : self.SeeassingmentGrades())\
            .place(x=300, y=140, height=40, width=250)

        """
        header2 = LabelFrame(graderoot, text="Post Assignment Grades").pack(fill="both", expand=True)

        Subject = Label(header2, text="Course #:", font=('', 15)).place(x=10, y=550)

        EntryForSubject = Entry(header2, bd=5, textvariable=self.Variable).place(x=300, y=550, width=250)

        AssingmentNumber = Label(header2, text="Assignment #:", font=('', 15)).place(x=10, y=590)

        EntryForAssingmentNumber = Entry(header2, bd=5, textvariable=self.Variable2).place(x=300, y=590, width=250)

        StudentId = Label(header2, text="Student ID:", font=('', 15)).place(x=10, y=630)

        EntryForStudentId = Entry(header2, bd=5, textvariable=self.Variable3).place(x=300, y=630, width=250)

        Grade = Label(header2, text="Grades:", font=('', 15)).place(x=10, y=670)

        EntryForGrades = Entry(header2, bd=5, textvariable=self.Variable4).place(x=300, y=670, width=250)
        """

        # Button_Submit = Button(header2, text="Post Assignment Grades", command= lambda: self.postGrades())\
        #    .place(x=300, y=710, width=250)

        courselist = Label(header, text="Available Courses", font=('arial 15 bold'), bg="light yellow").place(x=200,
                                                                                                                 y=280)
        CPSC = Label(header, text="CPSC 422 : Python Programming", font=('arial 15 italic'),
                     bg="light yellow").place(x=220, y=320)
        TM = Label(header, text="TCMG 645 : Technology New Venture Creation", font=('arial 15 italic'),
                   bg="light yellow").place(x=220, y=360)


    def SeeassingmentGrades(self):

        database_subjectId = self.Variable.get()
        database_AssingmentNumber = self.Variable2.get()
        database_studentid = self.Variable3.get()

        mycursor = cnxn.cursor()
        sql = "select AssignmentNumber,Grades from Grades where CourseNum=? and StudentId=? and AssignmentNumber=?"
        val = (database_subjectId, database_studentid, database_AssingmentNumber)
        mycursor.execute(sql, val)
        print(mycursor.rowcount, "record selected.")

        if mycursor.rowcount == 0:
            tkinter.messagebox.showinfo("Error", message="The Professor might not have filled in your grades yet.")
        # AdminDashboard=tk.Tk()
        # AdminDashboard.title("Admin Dashboard Page")
        # AdminDashboard.geometry("500x500")
        mycur = mycursor.fetchall()

        for rows in mycur:
            for i in rows:

                Libcontect_label = Label(text="Assignment " + database_AssingmentNumber + " received " + i + " points", font=('arial 15 italic'))
                Libcontect_label.place(x=250, y=190)
                print(i)


    """
    def postGrades(self):
        database_subject = self.Variable.get()
        database_AssingmentNumber = self.Variable2.get()
        database_StudentId = self.Variable3.get()
        database_Grades = self.Variable4.get()

        cnxn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                "Server=MSI\SQLEXPRESS;"
                                "Database=Canvas;"
                                "Trusted_Connection=yes;")

        cursor = cnxn.cursor()
        mycursor = cnxn.cursor()
        sql = "INSERT INTO Grades(CourseNum,AssignmentNumber,StudentId,Grades) VALUES (?,?,?,?)"
        val = (database_subject, database_AssingmentNumber, database_StudentId, database_Grades)
        mycursor.execute(sql, val)
        cnxn.commit()
        tkinter.messagebox.showinfo("Success", message="Grades Posted Successfully")
        print(mycursor.rowcount, "record inserted.")
    """

    def goLogin(self):
        tkinter.messagebox.showinfo("BYE BYE", message="Logged of Successfully")
        graderoot.destroy()
        import LoginPage

    def closewindow(self):
        exit()


graderoot = Tk()
app = MainClass(graderoot)
screen_width = graderoot.winfo_screenwidth()
screen_height = graderoot.winfo_screenheight()
screen_resolution = str(screen_width) + 'x' + str(screen_height)
graderoot.geometry(screen_resolution)
graderoot.title("Student GradeBook")
mainloop()
