import tkinter
from tkinter import *
from tkinter import filedialog as fdialog
import shutil
from tkinter import messagebox
import sqlite3
import os
import time


cnxn = sqlite3.connect(r"C:\Users\manda\AppData\Tkinter\student_db.db")
mycursor = cnxn.cursor()


class MainClass:

    def __init__(self, master):
        self.parent = master
        self.Studannoun()
        self.Destination = "C:\\Users\\manda\\AppData\\Tkinter\\UploadFile"

    def Studannoun(self):
        self.Variable = StringVar()
        self.Variable1= StringVar()
        self.Variable2 = StringVar()
        self.Dvariable = StringVar()
        self.Thetext = StringVar()
        today = time.strftime("%m/%d/%Y")
        vakt = time.strftime('%H:%M:%S')
        self.Variable1.set(today)
        self.Variable2.set(vakt)
        self.thedata=StringVar()

        header_file_frame = LabelFrame(Studannoun, text="Welcome to the University of Bridgeport") \
            .pack(fill="both", expand=False)

        header_file_content = Label(header_file_frame, text="Announcements", font=('arial 40 bold')) \
            .pack(fill="both", expand=False)

        dash = Button(header_file_frame, text="Homepage", command=lambda: self.goadminHome()).place(x=1700, y=10, height=50, width=100)

        refresh = Button(header_file_frame, text="Refresh", command=lambda: self.refresh()).place(x=1600, y=10,
                                                                                                    height=50,
                                                                                                    width=100)

        mainframe = LabelFrame(Studannoun, text="Course Announcements").pack(fill="both", expand="yes")

        Enterassi = Label(mainframe, text="Add New Announcement", font=("arial 20")).place(x=1300, y=100)




        AssingmentNumber = Label(mainframe, text="Announcement Title : ", font=('', 15)).place(x=1100, y=200)

        entryForAssingmentNumber = Entry(mainframe, bd=5, textvariable=self.Variable, width=50).place(x=1350, y=200)

        Time = Label(mainframe, text="Announced at : ", font=('', 15)).place(x=1100, y=240)

        EntryForTime = Entry(mainframe, bd=5, width=50, text=self.Variable2).place(x=1350, y=240)

        Date = Label(mainframe, text="Date :", font=('', 15)).place(x=1100, y=280)

        EntryForDueDate = Entry(mainframe, bd=5, width=50,text=self.Variable1).place(x=1350, y=280)

        Assingment = Label(mainframe, text="Message:", font=('', 15)).place(x=1100, y=320)

        EntryForAssingment = Text(mainframe, width=60, height=29)
        EntryForAssingment.place(x=1350, y=320)


        Button_Submit = Button(mainframe, text="Post Announcement", command= lambda: self.post_announ(EntryForAssingment)).place(x=1350, y=800)


        header = Label(mainframe, text="Announcements", font=('arial 15 bold')).place(x=20, y=170)
        header2 = Label(mainframe, text="View Announcements", font=('arial 15 bold')).place(x=550, y=170)

        mycursor.execute("select annountitle, announdate from announcements")
        mycur = mycursor.fetchall()
        listbox = Listbox(mainframe, font=('arial 18 bold'), selectmode=EXTENDED, listvariable=self.Dvariable, bg='light yellow', fg='black')
        listbox.place(x=20, y=200, height=600, width=500)
        for item in mycur:
            listbox.insert(END, item)
        v = Button(mainframe, text="View", command=lambda : selection()).place(x=450, y=170, width=70, height=30)


        def selection():

            a=listbox.curselection()
            for i in a:
                b= listbox.get(i)
                print(b[0])


            fname = b[0]
            name2 = "Announcement " + fname
            save_path = "C:/Users/manda/AppData/Tkinter/UploadFile/Announcements/"
            complete_file_name = save_path + name2 + ".txt"

            f = open(complete_file_name, 'r')
            textdata=f.read()

            f.close()

            ShowData = Label(mainframe, text=textdata, bg="white", anchor=NW, justify=LEFT).place(x=550, y=200, width=500, height=600)

    def refresh(self):
        Studannoun.destroy()
        import StudAnnoun



    def post_announ(self, EntryForAssingment):
        inputValue = str(EntryForAssingment.get("1.0","end-1c"))
        data = inputValue
        announdate= self.Variable1.get()
        annountime = self.Variable2.get()
        annountitle = self.Variable.get()
        announmsg = str(EntryForAssingment.get("1.0","end-1c"))


        name= "Announcement " + annountitle
        save_path="C:/Users/manda/AppData/Tkinter/UploadFile/Announcements/"
        complete_file_name = save_path + name + ".txt"

        Title = "\t\t\t\tAnnouncement Name : " + annountitle + "\n\n\n"
        announat = "Date : " + announdate + "\n"
        announvakt = "Time : " + annountime + "\n\n\n"
        headerline = "Dear Students, \n"

        content = Title + announat + announvakt + headerline

        f = open(complete_file_name, 'w')
        f.write(content)
        f.write("\t\t" + announmsg)
        sql = "INSERT INTO announcements (annountitle, announdate, annountime, messagedata ) VALUES (?,?,?,?)"
        mycursor.execute(sql, (annountitle, announdate, annountime, announmsg, ))
        cnxn.commit()
        tkinter.messagebox.showinfo("File Uploaded", message="Announcement was posted !")
        f.close()



    """
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
    """

    def goadminHome(self):
        Studannoun.destroy()
        import StudDashboard


Studannoun = Tk()
app = MainClass(Studannoun)
screen_width = Studannoun.winfo_screenwidth()
screen_height = Studannoun.winfo_screenheight()
screen_resolution = str(screen_width) + 'x' + str(screen_height)
Studannoun.geometry(screen_resolution)
Studannoun.title("Student Announcement Page")
mainloop()
