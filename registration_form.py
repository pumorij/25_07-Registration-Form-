from mysql import connector
from tkinter import messagebox

def database():
    conn=connector.connect(
        user='root',
        password='pumori2002',
        host='127.0.0.1',
        port='3306',
        database='registrationform')
    mycursor=conn.cursor()
    mycursor.execute("insert into registrationform values(%s,%s,%s,%s,%s,%s)",(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get(),c.get(),var.get()))
    messagebox.showinfo("Info","Submitted")
    conn.commit()

from cProfile import label
from tkinter import *
from tkinter.font import BOLD
ab=Tk()
ab.geometry("200x250")
ab.title("Registration Form")
ab.configure(bg='grey')

label_0=Label(ab,text="Registration Form",font=BOLD,bg='black',fg='white')
label_0.place(x=90,y=53)

label_1 = Label(ab, text="Sr No.",bg='black',fg='white')
label_1.place(x=80,y=130)
entry_1 = Entry(ab)
entry_1.place(x=240,y=130)

label_2= Label(ab, text="Name",bg='black',fg='white')
label_2.place(x=80,y=180)
entry_2 = Entry(ab)
entry_2.place(x=240,y=180)

label_3 = Label(ab, text="Roll no.",bg='black',fg='white')
label_3.place(x=80,y=230)
entry_3=Entry(ab)
entry_3.place(x=240,y=230)

label_4=Label(ab,text="Address",bg='black',fg='white')
label_4.place(x=80,y=280)
entry_4=Entry(ab)
entry_4.place(x=240,y=280)

label_5=Label(ab,text="Branch",bg='black',fg='white')
label_5.place(x=80,y=330)
list_of_branches=['CSE','IT','ECE','EE','CIVIL']
c=StringVar()
droplist=OptionMenu(ab,c,*list_of_branches)
droplist.config(width=15)
c.set('Select your Branch')
droplist.place(x=240,y=330)


label_6= Label(ab, text="Gender",bg='black',fg='white')
label_6.place(x=80,y=380)
var = IntVar()
Radiobutton(ab, text="Male", variable=var, value=1).place(x=235,y=380)
Radiobutton(ab, text="Female", variable=var, value=2).place(x=290,y=380)

Button(ab, text='Submit',command=database).place(x=180,y=430)

ab.mainloop()