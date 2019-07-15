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
        self.Destination = "C:\\Users\\manda\\AppData\\Tkinter\\UploadFile"   # only change this location to any folder on your desktop
        self.y_index = 600

        header_file_frame = LabelFrame(studfileroot, text="Welcome to the University of Bridgeport")\
                .pack(fill="both", expand=False)

        header_file_content = Label(header_file_frame, text="Course Files", font=('arial 40 bold'))\
                .pack(fill="both", expand=False)

        dash = Button(header_file_frame, text="Homepage", command=lambda:self.studHome()).place(x=1700, y=10, height=50, width=100)

        mainframe = LabelFrame(studfileroot, text="Select & Download Files").pack(fill="both", expand="yes")

        """
        MySource = Entry(studfileroot, textvariable=self.Source).place(x=600, y=250,height=30, width=500)
        select = Button(studfileroot, text="Select", command=lambda: self.Source.set(
                fdialog.askopenfilename(filetypes=[("JPEG File", '.jpg'),( "Text File", '.txt')])))\
                .place(x=800, y=300, height=50, width=100)

        # uploadbtn = Button(studfileroot, text="  Upload ", command=self.upload).place(x=800, y=350,height=50, width=100)
        
        header= Label(text="Uploaded Files", font=('arial 12 bold')).place(x=560,y=550)
        refresh = Button(studfileroot, text="  Refresh ", command=self.refreshwin).place(x=550, y=580, height=30, width=130)
        """

        header = Label(text="Uploaded Files", font=('arial 15 bold')).place(x=170, y=80)

        mycursor.execute("select * from uploads")
        mycur=mycursor.fetchall()
        listbox = Listbox(studfileroot, font=('arial 15 bold'), bg='Light Blue', fg='white')
        listbox.place(x=50, y=120, height=850, width=400)
        for item in mycur:
            listbox.insert(END, item)

        Download = Label(text="Download Your File",  font=('arial 15 bold')).place(x=600, y=80)
        search = Entry(bd=4, text="Enter the File Name ", textvariable=self.Source1).place(x=600, y=120, height=30, width=500)
        retrieve = Button(studfileroot, text="  Download ", command=self.download).place(x=600, y=155, height=30, width=100)

        exitb = Button(studfileroot, text="Exit", command=lambda: self.closewindow())
        exitb.place(x=1700, y=120, height=50, width=100)

    def refreshwin(self):
        studfileroot.mainloop()


    """
    def upload(self):
        source_file=self.Source.get()
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
        source ="C:\\Users\\manda\\AppData\\Tkinter\\UploadFile\\"

        destiny = "C:\\Users\\manda\\Downloads\\Destination\\"
        retrieve_name=self.Source1.get()
        source_name = source + retrieve_name
        try:
            shutil.copy(source_name, destiny)
            tkinter.messagebox.showinfo("Download Complete", message="File Downloaded Successfully")
        except:
            tkinter.messagebox.showinfo("Error", message="File Not Found. Enter the correct file name with it's extension")

    def closewindow(self):
        exit()

    def studHome(self):
        studfileroot.destroy()
        import StudDashboard


studfileroot = Tk()
app = MainClass(studfileroot)
screen_width = studfileroot.winfo_screenwidth()
screen_height = studfileroot.winfo_screenheight()
screen_resolution = str(screen_width) + 'x' + str(screen_height)
studfileroot.geometry(screen_resolution)
studfileroot.title("File Management Student")
mainloop()
