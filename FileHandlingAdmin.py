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
        self.gui()

    def gui(self):

        self.Source = StringVar()
        self.Source1= StringVar()
        #self.Source1.set("Enter the File Name with extension you want to download")
        self.Destination = "C:\\Users\\manda\\AppData\\Tkinter\\UploadFile"   # only change this location to any folder on your desktop
        self.y_index = 600

        header_file_frame = LabelFrame(fileroot, text="Welcome to the University of Bridgeport")\
                .pack(fill="both", expand=False)

        header_file_content = Label(header_file_frame, text="FILE MANAGEMENT", font=('arial 40 bold'))\
                .pack(fill="both", expand=False)

        homep = Button(header_file_frame, text="Homepage", command=lambda: self.goadminHome()).place(x=1700, y=10, height=50, width=100)

        mainframe = LabelFrame(fileroot, text="MENU").pack(fill="both", expand="yes")

        header = Label(mainframe, text="Browse Files to Upload", font=('arial 12 bold')).place(x=800, y=90)
        MySource = Entry(mainframe, textvariable=self.Source, bd=4).place(x=800, y=120,height=30, width=500)
        browse = Button(mainframe, text="Browse", command=lambda: self.Source.set(
                fdialog.askopenfilename(filetypes=[("JPEG File", '.jpg'),( "Text File", '.txt'), ("PDF", '.pdf')])))\
                .place(x=800, y=150, height=30, width=100)

        uploadbtn = Button(mainframe, text="  Upload ", command=self.upload).place(x=900, y=150, height=30, width=100)

        header= Label(mainframe, text="Uploaded Files", font=('arial 12 bold')).place(x=230,y=90)
        refresh = Button(mainframe, text="  Refresh ", command=self.refreshwin).place(x=550, y=580, height=30, width=130)

        mycursor.execute("select * from uploads")
        mycur=mycursor.fetchall()
        listbox = Listbox(fileroot, font=('arial 18 bold'), bg='Light Blue', fg='white')
        listbox.place(x=230, y=120, height= 600, width= 500)
        for item in mycur:
            listbox.insert(END, item)

        newvalue= listbox.get(ACTIVE)
        sel=str(newvalue)
        self.Source1.set(newvalue)
        Download = Label(text="Download Your File",  font=('arial 12 bold')).place(x=800, y=200)
        search = Entry(text="Enter the File Name with extension you want to download", bd=4, textvariable=self.Source1).place(x=800, y=230, height=30, width=500)
        retrieve = Button(mainframe, text="  Download ", command=self.download).place(x=800, y=260, height=30, width=100)

        dash = Button(mainframe, text="Logout", command=lambda: self.goLogin())
        dash.place(x=1700, y=130, height=50, width=100)

        files = Button(mainframe, text="Files", command=lambda: self.adminfile())
        files.place(x=15, y=90, height=50, width=100)

        assignment = Button(mainframe, text="Assignment", command=lambda: self.adminassign())
        assignment.place(x=15, y=140, height=50, width=100)

        grades = Button(mainframe, text="Transcripts", command= lambda : self.admingrades())
        grades.place(x=15, y=190, height=50, width=100)

        people = Button(mainframe, text="Add Students", command= lambda :  self.addstud())
        people.place(x=15, y=240, height=50, width=100)

        announ = Button(mainframe, text="Announcements", command=lambda: self.goAnnoun())
        announ.place(x=15, y=290, height=50, width=100)

        exitb = Button(mainframe, text="Exit", command=lambda: self.closewindow())
        exitb.place(x=1700, y=340, height=50, width=100)

    def refreshwin(self):
        self.gui()

    def upload(self):
        source_file=self.Source.get()
        print(source_file)
        if source_file.endswith(".jpg") or source_file.endswith(".txt") or source_file.endswith(".pdf"):
            shutil.copy(source_file, self.Destination)
            name =(os.path.basename(source_file))
            tkinter.messagebox.showinfo("Uploaded", message="File Uploaded Successfully")

            sql = "INSERT INTO uploads (File_Name) VALUES (?)"
            mycursor.execute(sql, (name,))
            cnxn.commit()

    def download(self):
        source ="C:\\Users\\manda\\AppData\\Tkinter\\UploadFile\\"

        destiny = "C:\\Users\\manda\\Downloads\\Destination\\"
        retrieve_name=self.Source1.get()
        source_name = source + retrieve_name
        try:
            shutil.copy(source_name, destiny)
            tkinter.messagebox.showinfo("Download Complete", message="File Downloaded Successfully. Check your Destination Folder")
        except:
            tkinter.messagebox.showinfo("Error", message="File Not Found. Enter the correct file with extension")

    def closewindow(self):
        exit()

    def goLogin(self):
        tkinter.messagebox.showinfo("BYE BYE", message="Logged of Successfully")
        fileroot.destroy()
        import LoginPage

    def goadminHome(self):
        fileroot.destroy()
        import AdminDashbaord

    def adminfile(self):
        fileroot.destroy()
        import FileHandlingAdmin


    def goAnnoun(self):
        fileroot.destroy()
        import Announcements

    def adminassign(self):
        fileroot.destroy()
        import AdminAssign

    def admingrades(self):
        fileroot.destroy()
        import StudentGrade

    def addstud(self):
        fileroot.destroy()
        import AdminAddPeo



fileroot = Tk()
app = MainClass(fileroot)
screen_width = fileroot.winfo_screenwidth()
screen_height = fileroot.winfo_screenheight()
screen_resolution = str(screen_width) + 'x' + str(screen_height)
fileroot.geometry(screen_resolution)
fileroot.title("File Management Admin")
mainloop()
