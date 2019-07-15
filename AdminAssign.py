import tkinter
from tkinter import *
from tkinter import filedialog as fdialog
import shutil
from tkinter import messagebox
import sqlite3
import os


cnxn = sqlite3.connect(r"C:\Users\manda\AppData\Tkinter\student_db.db")
mycursor = cnxn.cursor()


class MainClass:

    def __init__(self, master):
        self.parent = master
        self.adminassign()
        self.Destination = "C:\\Users\\manda\\AppData\\Tkinter\\UploadFile"

    def adminassign(self):
        self.Variable = StringVar()
        self.Variable1= StringVar()
        self.Variable2 = StringVar()
        self.Dvariable = StringVar()
        self.Thetext = StringVar()

        header_file_frame = LabelFrame(AdminAssignmentpage, text="Welcome to the University of Bridgeport") \
            .pack(fill="both", expand=False)

        header_file_content = Label(header_file_frame, text="ASSIGNMENT UPLOADS", font=('arial 40 bold')) \
            .pack(fill="both", expand=False)

        dash = Button(header_file_frame, text="Homepage", command=lambda: self.goadminHome()).place(x=1700, y=10, height=50, width=100)

        mainframe = LabelFrame(AdminAssignmentpage, text="Enter the Assignment Details").pack(fill="both", expand="yes")

        Enterassi = Label(mainframe, text="Add new Assignment", font=('', 25)).place(x=1100, y=100)

        courseid = Label(mainframe, text="Course ID : ", font=('', 15)).place(x=950, y=200)

        EntryForid = Entry(mainframe, bd=5, width=50, textvariable=self.Variable1).place(x=1200, y=200)

        AssingmentNumber = Label(mainframe, text="Assignment Name : ", font=('', 15)).place(x=950, y=240)

        entryForAssingmentNumber = Entry(mainframe, bd=5, textvariable=self.Variable, width=50).place(x=1200, y=240)

        DueDate = Label(mainframe, text="Due Date(mm/dd/yyyy)", font=('', 15)).place(x=950, y=280)

        EntryForDueDate = Entry(mainframe, bd=5, width=50,textvariable=self.Variable2).place(x=1200, y=280)

        Assingment = Label(mainframe, text="Assignment:", font=('', 15)).place(x=950, y=320)

        EntryForAssingment = Text(mainframe, width=80, height=20)
        EntryForAssingment.place(x=1200, y=320)

        Button_Submit = Button(mainframe, text="Post Assignment", command= lambda: self.post_assign(EntryForAssingment)).place(x=1200, y=650)

        courselist = Label(mainframe, text="Available Courses", font=('arial 15 bold')).place(x=600, y=350)
        CPSC = Label(mainframe, text="CPSC 422 : Python Programming", font=('arial 15 italic')).place(x=660, y=380)
        TM = Label(mainframe, text="TCMG 645 : Technology New Venture Creation", font=('arial 15 italic')).place(x=660,
                                                                                                                 y=410)

        header = Label(mainframe, text="Uploaded Assignments", font=('arial 12 bold')).place(x=20, y=170)

        mycursor.execute("select file_name from assignments")
        mycur = mycursor.fetchall()
        listbox = Listbox(mainframe, font=('arial 18 bold'), bg='light yellow', fg='black')
        listbox.place(x=20, y=200, height=600, width=500)
        for item in mycur:
            for i in item:
                listbox.insert(END, i)

        Download = Label(text="Download Assignment Here : add extension", font=('arial 12 bold')).place(x=20, y=105)

        search = Entry(bd=4, text="Enter the File Name ", textvariable=self.Dvariable).place(x=20, y=130, height=30,
                                                                                            width=500)
        retrieve = Button(mainframe, text="  Download ", command=self.download).place(x=520, y=130, height=30,
                                                                                      width=100)


    def post_assign(self, EntryForAssingment):
        inputValue = str(EntryForAssingment.get("1.0","end-1c"))
        data = inputValue
        courseid= self.Variable1.get()
        due = self.Variable2.get()
        textdata = self.Variable.get()

        if courseid == '422' or courseid == '645':

            name= "Assignment " + textdata
            save_path="C:/Users/manda/AppData/Tkinter/UploadFile/Assignments/"
            complete_file_name = save_path + name + ".txt"
            try:
                f = open(complete_file_name, 'w')
                f.write(data)
                sql = "INSERT INTO assignments (file_name, course_id, due_date ) VALUES (?,?,?)"
                mycursor.execute(sql, (name, courseid, due, ))
                cnxn.commit()
                tkinter.messagebox.showinfo("File Uploaded", message="Assignment was posted !")
                f.close()
            except:
                tkinter.messagebox.showinfo("Something went wrong", message="Enter the data in the right format")

        else:
            tkinter.messagebox.showinfo("ID Error", message="Course ID did not match")
    def download(self):
        source ="C:\\Users\\manda\\AppData\\Tkinter\\UploadFile\\Assignments\\"

        destiny = "C:\\Users\\manda\\Downloads\\Destination\\"
        retrieve_name=self.Dvariable.get()
        print(retrieve_name)
        source_name = source + retrieve_name
        print(source_name)
        try:
            shutil.copy(source_name, destiny)
            tkinter.messagebox.showinfo("Download Complete", message="Check your Destination folder")
        except:
            tkinter.messagebox.showinfo("Error", message="File Not Found. Enter the correct file with extension")

    def goadminHome(self):
        AdminAssignmentpage.destroy()
        import AdminDashbaord

AdminAssignmentpage = Tk()
app = MainClass(AdminAssignmentpage)
screen_width = AdminAssignmentpage.winfo_screenwidth()
screen_height = AdminAssignmentpage.winfo_screenheight()
screen_resolution = str(screen_width) + 'x' + str(screen_height)
AdminAssignmentpage.geometry(screen_resolution)
AdminAssignmentpage.title("Admin Assignment Page")
mainloop()
