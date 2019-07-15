import tkinter
from tkinter import *
import pypyodbc
from tkinter import messagebox


cnxn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=MSI\SQLEXPRESS;"
                      "Database=Canvas;"
                      "Trusted_Connection=yes;")
cursor = cnxn.cursor()
mycursor = cnxn.cursor()


class MainClass:
    def __init__(self, master):
        self.parent=master
        self.gui()

    def gui(self):
        self.Variable=StringVar()
        self.Variable1 = StringVar()
        self.Variable2= StringVar()
        self.Variable3 = StringVar()
        self.Variable4 = StringVar()
        self.Variable5 = StringVar()
        self.Variable6 = StringVar()
        self.Variable7 = StringVar()
        self.Variable8 = StringVar()
        self.yield_y = 100

        header = LabelFrame().pack(fill="both", expand=True)
        submitButton = Button(header, text="Submit", command=lambda: self.addpeopleDatabase()).place(x=300, y=450, width=60)
        ClearButton = Button(header, text="Clear", command="").place(x=370, y=450, width=60)

        EnterPeople=Label(header, text="Add New Student",font=('', 25)).place(x=100, y=100)

        Firstname=Label(header, text="First_Name         ", font=('', 12)).place(x=100, y=210)
        EntryForFirstname=Entry(bd=5, textvariable=self.Variable)
        EntryForFirstname.place(x=300, y=210)

        Lastname=Label(header, text="Last_Name         ", font=('', 12)).place(x=100, y=240)
        EntryForLastname=Entry(header, bd=5, textvariable=self.Variable2)
        EntryForLastname.place(x=300, y=240)


        Email=Label(header, text="Email ID             ", font=('', 12)).place(x=100, y=270)
        EntryForEmail=Entry(header, bd=5, textvariable=self.Variable3)
        EntryForEmail.place(x=300, y=270)


        StudentId=Label(header, text="Student ID          ", font=('', 12)).place(x=100, y=300)
        EntryForStudentId=Entry(header, bd=5, textvariable=self.Variable4)
        EntryForStudentId.place(x=300, y=300)


        SemisterID=Label(header, text="Semester Term   ", font=('', 12)).place(x=100, y=330)
        EntryForSemester=Entry(header, bd=5, textvariable=self.Variable5)
        EntryForSemester.place(x=300, y=330)

        City=Label(header, text="City                    ", font=('', 12)).place(x=100, y=360)
        EntryForCity=Entry(header, bd=5, textvariable=self.Variable7)
        EntryForCity.place(x=300, y=360)

        Courses=Label(header, text="Course               ", font=('', 12)).place(x=100, y=390)
        EntryForCourse=Entry(header, bd=5, textvariable=self.Variable6)
        EntryForCourse.place(x=300, y=390)

        Telephone=Label(header, text="Telephone          ", font=('', 12)).place(x=100, y=420)
        EntryForTelephone=Entry(header, bd=5, textvariable=self.Variable8)
        EntryForTelephone.place(x=300, y=420)

        show = Button(header, text="Show Enrollments", command=lambda: self.showenroll()).place(x=650, y=130)
        label = Label(header, text="Student ID       Semester Term      Course No", font=('', 12)).place(x=550, y=170)


        courselist = Label(header, text="Available Courses", font=('arial 15 bold')).place(x=100, y=500)
        CPSC = Label(header, text="CPSC 422 : Python Programming", font=('arial 15 italic')).place(x=120, y=530)
        TM = Label(header, text="TCMG 645 : Technology New Venture Creation", font=('arial 15 italic')).place(x=120, y=560)

        dash = Button(header, text="Homepage", command=lambda: self.goadminHome()).place(x=1700, y=10, height=50, width=100)



    def goadminHome(self):
        AdminPeoplespage.destroy()
        import AdminDashbaord

    def refresh(self):
        AdminPeoplespage.destroy()
        import AdminAddPeo


    def addpeopleDatabase(self):


         FirstNameForDatabase=self.Variable.get()
         print(FirstNameForDatabase)
         LastnameForDatabase=self.Variable2.get()
         EmailForDatabase=self.Variable3.get()
         StudentIdForDatabase=self.Variable4.get()
         semiseteridforDatabase=self.Variable5.get()
         cityForDatabase=self.Variable7.get()
         TelephoneForDatabase=self.Variable8.get()
         CourseForDatabase=self.Variable6.get()

         if CourseForDatabase == '645' or CourseForDatabase == '554' or CourseForDatabase == '422':
              sql = "INSERT INTO Student1(StudentId,FirstName,LastName,Street,City,State,Email,Telephone) VALUES (?,?,?,?,?,?,?,?)"
              val = (StudentIdForDatabase, FirstNameForDatabase,LastnameForDatabase, "114 rennell",cityForDatabase,"CT",
              EmailForDatabase,TelephoneForDatabase)

              mycursor.execute(sql, val)
              tkinter.messagebox.showinfo("Successful", message="New Student Record created successfully")
              cnxn.commit()
              print(mycursor.rowcount, "record inserted.")
              sql = "INSERT INTO StudentEnrollment(StudentId,SemesterId,CourseNum) VALUES (?,?,?)"
              val = (StudentIdForDatabase, semiseteridforDatabase, CourseForDatabase)
              mycursor.execute(sql, val)
              cnxn.commit()
              print(mycursor.rowcount, "record inserted.")

         else:
              tkinter.messagebox.showinfo("Course ID Error", message="We couldn't find the mentioned course number")


    def showenroll(self):

        sql = "select * from StudentEnrollment"
        mycursor.execute(sql)
        print(mycursor.rowcount, "record selected.")
        mycur = mycursor.fetchall()
        print(mycur)
        Libcontect_label = Listbox(font=('arial 15 '))
        Libcontect_label.place(x=550, y=200)

        for rows in mycur:
            Libcontect_label.insert(END, rows)

    """
    def ClearEntry():
    EntryForFirstname.delete(0,'end')
    EntryForLastname.delete(0,'end')
    EntryForStudentId.delete(0,'end')
    EntryForCity.delete(0,'end')
    EntryForCourse.delete(0,'end')
    EntryForTelephone.delete(0,'end')
    EntryForEmail.delete(0,'end')
    EntryForSemester.delete(0,'end')
    """

AdminPeoplespage = Tk()

app = MainClass(AdminPeoplespage)
screen_width = AdminPeoplespage.winfo_screenwidth()
screen_height = AdminPeoplespage.winfo_screenheight()
screen_resolution = str(screen_width) + 'x' + str(screen_height)
AdminPeoplespage.geometry(screen_resolution)
AdminPeoplespage.title("Add New Students")
mainloop()
