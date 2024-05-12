import customtkinter as tk
import tkinter
from tkinter import ttk
import pyodbc
import datetime
import re

ind=0
hhh=datetime.date
conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-DSUUU82;'
                          'Database=task;'
                          'Trusted_Connection=yes;')
cursor = conn.cursor()
window=tk.CTk()
window.title("dr/hossam")
window.geometry("1000x600")
window.resizable(0,0)


header=tk.CTkFrame(window,height=80,width=1000,fg_color="#175491",corner_radius=0)
header.place(x=0,y=0)

tip=tk.CTkFrame(window,height=30,width=1000,fg_color="#7395B7",corner_radius=0)
tip.place(x=0,y=79)

frameemployee=tk.CTkFrame(window,width=1000,height=500,fg_color="#E0E0E0",corner_radius=0)
    #frameemployee

tree=ttk.Treeview(frameemployee)
tree['column']=('ssn', 'Name', 'salary','Dname','Pname','Dno')
tree.column('#0',width=0,stretch=tkinter.NO)
tree.column('ssn',anchor=tkinter.CENTER,width=140)
tree.column('Name',anchor=tkinter.CENTER,width=140)
tree.column('salary',anchor=tkinter.CENTER,width=140)
tree.column('Dname',anchor=tkinter.CENTER,width=140)
tree.column('Pname',anchor=tkinter.CENTER,width=140)
tree.column('Dno',anchor=tkinter.CENTER,width=140)

tree.heading('#0',text='',anchor=tkinter.CENTER)
tree.heading('ssn',text='ssn',anchor=tkinter.CENTER)
tree.heading('Name',text='Name',anchor=tkinter.CENTER)
tree.heading('salary',text='salary',anchor=tkinter.CENTER)
tree.heading('Dname',text='Dname',anchor=tkinter.CENTER)
tree.heading('Pname',text='Pname',anchor=tkinter.CENTER)
tree.heading('Dno',text='Dno',anchor=tkinter.CENTER)

def solo():

    fname,lname,ss_n,birthy,addres,salar,superss_n,Dno_=getvalue()
    superssn__ = f"SELECT superssn FROM Employees WHERE ssn={ss_n}"
    cursor.execute(superssn__)
    superssn___=str(cursor.fetchall())
    superssn___ = ''.join(char for char in superssn___ if char.isdigit())
    print(superssn___)
    select_query = f"SELECT fname FROM Employees WHERE ssn={ss_n}"
    select_query1 = f"SELECT salary FROM Employees WHERE ssn ={ss_n}"
    select_query2 = f"SELECT dname FROM Department WHERE mgrssn ={superssn___} "
    select_query3 =f"SELECT hours FROM WORKS_ON WHERE essn={ss_n}"
    cursor.execute(select_query)

    rows=cursor.fetchall()
    cursor.execute(select_query1)
    sal=cursor.fetchall()
    cursor.execute(select_query2)
    dep=cursor.fetchall()
    cursor.execute(select_query3)
    ho=cursor.fetchall()



    val=(ss_n,rows,sal,dep,ho)
    global ind
    tree.insert(parent='',index=ind,iid=ind,text='',values=val)
    ind=ind+1



tree.place(x=360,y=100)

buttonsearch=tk.CTkButton(frameemployee,text="search",width=80,height=20,command=lambda :solo()).place(x=600,y=50)
Fname=tk.CTkEntry(frameemployee,width=100,height=20)
Fname.place(x=40,y=50)

Lname = tk.CTkEntry(frameemployee, width=100, height=20)
Lname.place(x=40, y=100)

ssn = tk.CTkEntry(frameemployee, width=100, height=20)
ssn.place(x=40, y=150)

Bdate = tk.CTkEntry(frameemployee, width=100, height=20)
Bdate.place(x=40, y=200)

address = tk.CTkEntry(frameemployee, width=100, height=20)
address.place(x=40, y=250)

salary = tk.CTkEntry(frameemployee, width=100, height=20)
salary.place(x=40, y=300)

superssn = tk.CTkEntry(frameemployee, width=100, height=20)
superssn.place(x=40, y=350)

Dno = tk.CTkEntry(frameemployee, width=100, height=20)
Dno.place(x=40, y=400)
    #***************************************************************
Fnamel = tk.CTkLabel(frameemployee,text="Fname", width=100, height=20)
Fnamel.place(x=150, y=50)

Lnamel = tk.CTkLabel(frameemployee,text="Lname", width=100, height=20)
Lnamel.place(x=150, y=100)

ssnL = tk.CTkLabel(frameemployee,text="ssn", width=100, height=20)
ssnL.place(x=150, y=150)

BdateL = tk.CTkLabel(frameemployee,text="Bdate", width=100, height=20)
BdateL.place(x=150, y=200)

addressl = tk.CTkLabel(frameemployee, width=100, height=20,text="address")
addressl.place(x=150, y=250)

salaryl = tk.CTkLabel(frameemployee, width=100, height=20,text="salary")
salaryl.place(x=150, y=300)

superssnl = tk.CTkLabel(frameemployee, width=100, height=20,text="superssn")
superssnl.place(x=150, y=350)

Dnol = tk.CTkLabel(frameemployee, width=100, height=20,text="Dno")
Dnol.place(x=150, y=400)
    #hhhhhh





    #header element

buttonemployee=tk.CTkButton(header,width=150,height=40,fg_color="#083D72",text="EMPLOYEE",text_color="white",command=lambda :buttonemp())
buttonemployee.place(x=50,y=20)


buttondepr=tk.CTkButton(header,width=150,height=40,fg_color="#083D72",text="DEPARTMENT",text_color="white")
buttondepr.place(x=220,y=20)

buttonproject=tk.CTkButton(header,width=150,height=40,fg_color="#083D72",text="DEPARTMENT",text_color="white")
buttonproject.place(x=390,y=20)




labelheader=tk.CTkLabel(window,text="Hamoksha",width=200,fg_color="#175491",bg_color="#175491",font=("Verdana",36,"bold"),text_color="white")
labelheader.place(x=700,y=25)

#end of header element

#element of tip
#tk.CTkButton(tip,width=100,height=20,fg_color="#224FA8",text="EDIT",corner_radius=5).place(x=30,y=5)
#tk.CTkButton(tip, width=100, height=20, fg_color="#224FA8", text="ADD", corner_radius=5).place(x=150, y=5)
#tk.CTkButton(tip, width=100, height=20, fg_color="#224FA8", text="DELET", corner_radius=5).place(x=270, y=5)
#end of tip
def buttonemp():
    frameemployee.place(x=0, y=108)




def getvalue():
    fname=Fname.get()
    lname=Lname.get()
    ss_n=ssn.get()
    birthy=Bdate.get()
    addres=address.get()
    salar=salary.get()
    superss_n=superssn.get()
    Dno_=Dno.get()
    Fname.delete(0,tk.END)
    Lname.delete(0, tk.END)
    ssn.delete(0, tk.END)
    Bdate.delete(0, tk.END)
    address.delete(0, tk.END)
    salary.delete(0,tk.END)
    superssn.delete(0, tk.END)
    Dno.delete(0,tk.END)
    return  fname,lname,ss_n,birthy,addres,salar,superss_n,Dno_

window.mainloop()