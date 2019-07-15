import tkinter as tk
from tkinter import Button
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from tkinter import *
import  pypyodbc


AdminAssingmentGradepage=tk.Tk()
AdminAssingmentGradepage.title("Admin Grade Page")
AdminAssingmentGradepage.geometry("500x500")

Subject=tk.Label(text="Course num:", font=('', 15)).grid(row=2)
EntryForSubject=tk.Entry(bd=5)
EntryForSubject.grid(row=2,column=2)

AssingmentNumber=tk.Label(text="AssingmentNumber:", font=('', 15)).grid(row=3)
EntryForAssingmentNumber=tk.Entry(bd=5)
EntryForAssingmentNumber.grid(row=3,column=2)

StudentId=tk.Label(text="StudentId:", font=('', 15)).grid(row=4)
EntryForStudentId=tk.Entry(bd=5)
EntryForStudentId.grid(row=4,column=2)

Grade=tk.Label(text="Grade:", font=('', 15)).grid(row=5)
EntryForGrades=tk.Entry(bd=5)
EntryForGrades.grid(row=5,column=2)
def postGrades():
    database_subject=EntryForStudentId.get()
    database_AssingmentNumber=EntryForAssingmentNumber.get()
    database_StudentId=EntryForAssingmentNumber.get()
    database_Grades=EntryForGrades.get()



    cnxn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=MSI\SQLEXPRESS;"   
                      "Database=Canvas;"         
                      "Trusted_Connection=yes;")


    cursor = cnxn.cursor()
    mycursor = cnxn.cursor()
    sql = "INSERT INTO Grades(CourseNum,StudentId,AssignmentNumber,Grades) VALUES (?,?,?,?)"
    val = (database_subject, database_AssingmentNumber,database_StudentId,database_Grades )
    mycursor.execute(sql,val)
    cnxn.commit()
    print(mycursor.rowcount, "record inserted.")


Button_Submit=Button(text="Post Assingment Grades",command=postGrades).grid()



AdminAssingmentGradepage.mainloop()

