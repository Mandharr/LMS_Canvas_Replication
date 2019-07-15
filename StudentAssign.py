import tkinter
from tkinter import *
from tkinter import filedialog as fdialog
import shutil
from tkinter import messagebox
import sqlite3
import pypyodbc
import os
import time

"""cnxn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=MSI\SQLEXPRESS;"   
                      "Database=Canvas;"         
                      "Trusted_Connection=yes;")
"""
cnxn = sqlite3.connect(r"C:\Users\manda\AppData\Tkinter\student_db.db")
mycursor = cnxn.cursor()


class MainClass:

    def __init__(self,master):
        self.parent=master
        self.studassign()


    def studassign(self):
        self.Destination = "C:\\Users\\manda\\AppData\\Tkinter\\UploadFile"
        self.Variable=StringVar()
        self.Thetext=StringVar()
        today = time.strftime("%m/%d/%Y")

        header_file_frame = LabelFrame(StudAssignmentpage, text="Welcome to the University of Bridgeport") \
            .pack(fill="both", expand=False)

        header_file_content = Label(header_file_frame, text="ASSIGNMENTS", font=('arial 40 bold')) \
            .pack(fill="both", expand=False)

        homep = Button(header_file_frame, text="Homepage", command=lambda: self.goStudHome()).place(x=1700, y=10,
                                                                                                     height=50,
                                                                                                     width=100)

        mainframe = LabelFrame(StudAssignmentpage, text="MENU").pack(fill="both", expand="yes")
        date = Label(mainframe, text="Todays Date : " + today, font=('arial 12 bold')).place(x=850, y=90)

        """
        MySource = Entry(mainframe, textvariable=self.Variable).place(x=600, y=250, height=30, width=500)
        select = Button(mainframe, text="Select", command=lambda: self.Variable.set(
            fdialog.askopenfilename(filetypes=[("JPEG File", '.jpg'), ("Text File", '.txt')]))) \
            .place(x=800, y=300, height=50, width=100)

        uploadbtn = Button(mainframe, text="  Upload ", command=self.upload).place(x=800, y=350, height=50, width=100)

        header = Label(mainframe, text="Uploaded Files", font=('arial 12 bold')).place(x=230, y=90)
        refresh = Button(mainframe, text="  Refresh ", command=self.refreshwin).place(x=550, y=580, height=30,
                                                                                      width=130)
        """

        header = Label(mainframe, text="Uploaded Assignments", font=('arial 12 bold')).place(x=230, y=90)
        header2 = Label(mainframe, text="Due By", font=('arial 12 bold')).place(x=430, y=90)


        sql = "select file_name from assignments where due_date > ?"
        mycursor.execute(sql, (today, ))
        mycur = mycursor.fetchall()
        listbox = Listbox(StudAssignmentpage, font=('arial 12 '), bg='yellow', fg='black')
        listbox.place(x=230, y=120, height=500, width=300)
        for item in mycur:
            for i in item:
                listbox.insert(END, i)
        print(today)
        sql = "select due_date from assignments where due_date > ?"
        mycursor.execute(sql, (today, ))
        mycur = mycursor.fetchall()
        listbox2 = Listbox(StudAssignmentpage, font=('arial 12' ), bg='light yellow', fg='black')
        listbox2.place(x=430, y=120, height=500, width=200)
        for item in mycur:
            for i in item:
                listbox2.insert(END, i)

        header = Label(mainframe, text="Past Assignments", font=('arial 12 bold')).place(x=230, y=630)
        header2 = Label(mainframe, text="Due By", font=('arial 12 ')).place(x=430, y=630)

        sql = "select file_name from assignments where due_date < ?"
        mycursor.execute(sql, (today,))
        mycur = mycursor.fetchall()
        listbox = Listbox(StudAssignmentpage, font=('arial 12'), bg='yellow', fg='black')
        listbox.place(x=230, y=660, height=100, width=300)
        for item in mycur:
            for i in item:
                listbox.insert(END, i)
        print(today)
        sql = "select due_date from assignments where due_date < ?"
        mycursor.execute(sql, (today,))
        mycur = mycursor.fetchall()
        listbox2 = Listbox(StudAssignmentpage, font=('arial 12 '), bg='light yellow', fg='black')
        listbox2.place(x=430, y=660, height=100, width=200)
        for item in mycur:
            for i in item:
                listbox2.insert(END, i)


        Download = Label(text="Download Assignment Here (add extension)", font=('arial 12 bold')).place(x=800, y=120)
        search = Entry(bd=4, text="Enter the File Name ", textvariable=self.Variable).place(x=800, y=145, height=30,
                                                                                           width=500)
        retrieve = Button(mainframe, text="  Download ", command=self.download).place(x=800, y=175, height=30,
                                                                                      width=100)

        dash = Button(mainframe, text="Logout", command=lambda: self.goLogin())
        dash.place(x=1700, y=130, height=50, width=100)

        files = Button(mainframe, text="Files", command=lambda: self.adminfile())
        files.place(x=15, y=90, height=50, width=100)

        assignment = Button(mainframe, text="Assignment", command=lambda: self.adminassign())
        assignment.place(x=15, y=140, height=50, width=100)

        grades = Button(mainframe, text="Transcripts", command= lambda: self. studgrades())
        grades.place(x=15, y=190, height=50, width=100)

        announ = Button(mainframe, text="Announcements", command=lambda: self.seeannoun())
        announ.place(x=15, y=240, height=50, width=100)

        exitb = Button(mainframe, text="Exit", command=lambda: self.closewindow())
        exitb.place(x=1700, y=340, height=50, width=100)

    def studgrades(self):
        StudAssignmentpage.destroy()
        import StudentseeGrade

    def adminassign(self):
        StudAssignmentpage.mainloop()

    def adminfile(self):
        StudAssignmentpage.destroy()
        import FileHandlingStudent


    """
    def post_assign(self, EntryForAssingment):
        inputValue = str(EntryForAssingment.get("1.0","end-1c"))
        data = inputValue

        textdata = self.Variable.get()

        file_name= "Assignment No_" + textdata
        save_path="C:/Users/manda/AppData/Tkinter/UploadFile/"
        complete_file_name = save_path + file_name + ".txt"

        f = open(complete_file_name, 'w')
        f.write(data)
        f.close()

    def refreshwin(self):
        self.studassign()
    """
    """
    def upload(self):
        source_file=self.Variable.get()
        print(source_file)
        if source_file.endswith(".jpg") or source_file.endswith(".txt"):
            shutil.copy(source_file, self.Destination)
            name =(os.path.basename(source_file))
            tkinter.messagebox.showinfo("Uploaded", message="File Uploaded Successfully")

            sql = "INSERT INTO uploads (File_Name) VALUES (?)"
            mycursor.execute(sql, (name,))
            cnxn.commit()
    """

    def download(self):
        source ="C:\\Users\\manda\\AppData\\Tkinter\\UploadFile\\Assignments\\"

        destiny = "C:\\Users\\manda\\Downloads\\Destination\\"
        retrieve_name=self.Variable.get()
        print(retrieve_name)
        source_name = source + retrieve_name
        print(source_name)
        try:
            shutil.copy(source_name, destiny)
            tkinter.messagebox.showinfo("Download Complete", message="File Downloaded Successfully")
        except:
            tkinter.messagebox.showinfo("Error", message="File Not Found. Enter the correct file with extension")

    def closewindow(self):
        exit()

    def goLogin(self):
        tkinter.messagebox.showinfo("BYE BYE", message="Logged of Successfully")
        StudAssignmentpage.destroy()
        import LoginPage

    def goStudHome(self):
        StudAssignmentpage.destroy()
        import StudDashboard

    def seeannoun(self):
        StudAssignmentpage.destroy()
        import Announcements

StudAssignmentpage = Tk()
app = MainClass(StudAssignmentpage)
screen_width = StudAssignmentpage.winfo_screenwidth()
screen_height = StudAssignmentpage.winfo_screenheight()
screen_resolution = str(screen_width) + 'x' + str(screen_height)
StudAssignmentpage.geometry(screen_resolution)
StudAssignmentpage.title("Student Assignment Page")
mainloop()
