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

        Courses=Label(header, text="Course ID:           ", font=('', 12)).place(x=100, y=130)
        EntryForCourse=Entry(header, bd=5, textvariable=self.Variable6)
        EntryForCourse.place(x=300, y=130)

        show = Button(header, text="Show Enrollments", command=lambda: self.showenroll()).place(x=800, y=130)
        label = Label(header, text="Student ID      ", font=('', 12)).place(x=800, y=170)


        courselist = Label(header, text="Available Courses", font=('arial 15 bold')).place(x=100, y=200)
        CPSC = Label(header, text="CPSC 422 : Python Programming", font=('arial 15 italic')).place(x=120, y=230)
        TM = Label(header, text="TCMG 645 : Technology New Venture Creation", font=('arial 15 italic')).place(x=120, y=260)

        dash = Button(header, text="Homepage", command=lambda: self.goadminHome()).place(x=1700, y=10, height=50, width=100)



    def goadminHome(self):
        AdminPeoplespage.destroy()
        import AdminDashbaord

    def refresh(self):
        AdminPeoplespage.destroy()
        import AdminAddPeo

    """
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
    """

    def showenroll(self):

        CourseForDatabase = str(self.Variable6.get())
        print(CourseForDatabase)
        sql = "select StudentId from StudentEnrollment where CourseNum = ?"
        val = CourseForDatabase
        mycursor.execute(sql, (val, ))
        print(mycursor.rowcount, "record selected.")
        mycur = mycursor.fetchall()
        print(mycur)
        Libcontect_label = Listbox(font=('arial 15 '))
        Libcontect_label.place(x=800, y=200)

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
AdminPeoplespage.title("Course People")
mainloop()
