'''from tkinter import *
kalai = Tk()
kalai.title("Arithmetic operation")
kalai.geometry("600x600+600+600")
kalai.state("zoomed")

def Addition():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a+b
    Labeloutput.config(text=c)

def Subtraction():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a-b
    Labeloutput.config(text=c)

def Division():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a/b
    Labeloutput.config(text=c)

def Multiplication():
    a=int(tbEntrya.get())
    b=int(tbEntryb.get())
    c=a*b
    Labeloutput.config(text=c)


Labeltitle  = Label(kalai,text="    Mathematical operation ",font= ("lucida calligraphy",25),fg="green")
Labeltitle.grid(row=0,column=30)

Label1msg=Label(kalai,text="Enter the value 1",font=("lucida calligraphy",14),fg="green")
Label1msg.grid(row=1,column=30,pady=20)
tbEntrya=Entry(kalai,width=60)
tbEntrya.grid(row=1,column=35)

Label2msg=Label(kalai,text= "Enter the value 2",font=("lucida calligraphy",14),fg="green")
Label2msg.grid(row=2,column=30,pady=25)
tbEntryb=Entry(kalai,width=60)
tbEntryb.grid(row=2,column=35)

Labeloutput =Label(kalai,text="output",font=("monotype corsiva",15),fg="white",bg="blue",)
Labeloutput.grid(row=3,column=30,pady=20)
btnadd=Button(kalai,text="Addition",font=("monotype corsiva",15),fg="white",bg="blue",command=Addition)
btnadd.grid(row=5,column=1)
btnsub=Button(kalai,text="Subtraction",font=("monotype corsiva",15),fg="white",bg="blue",command=Subtraction)
btnsub.grid(row=5,column=2)
btndivision=Button(kalai,text="Division",font=("monotype corsiva",15),fg="white",bg="blue",command=Division)
btndivision.grid(row=5,column=3)
btnmultiply=Button(kalai,text="Multiplication",font=("monotype corsiva",15),fg="white",bg="blue",command=Multiplication)
btnmultiply.grid(row=5,column=4)'''


from  tkinter import *
data=Tk()
data.title("Personal Information")
data.geometry("500x500+500+500")
data.state("zoomed")



Labeltitle=Label(data,text="Personal Information",font=("lucida calligraphy",20),fg="green")
Labeltitle.grid(row=0,column=90)

Label1msg=Label(data,text= "NAME",font=("castellar",15 ),fg="Red")
Label1msg.grid(row=1,column=30,pady=25)
tbEntrya=Entry(data,width=60)
tbEntrya.grid(row=1,column=35)
Label2msg=Label(data,text="GENDER",font=("castellar",15),fg="Red")
Label2msg.grid(row=2,column=30,pady=25)
tbEntrya=Entry(data,width=60)
tbEntrya.grid(row=2,column=35)
Label3msg=Label(data,text="D.O.B",font=("castellar",15),fg="Red")
Label3msg.grid(row=3,column=30,pady=25)
tbEntrya=Entry(data,width=60)
tbEntrya.grid(row=3,column=35)
Label4msg=Label(data,text="CITY",font=("castellar",15),fg="Red")
Label4msg.grid(row=4,column=30,pady=25)
tbEntrya=Entry(data,width=60)
tbEntrya.grid(row=4,column=35)
Label5msg=Label(data,text="PH NUM",font=("castellar",15),fg="Red")
Label5msg.grid(row=5,column=30,pady=25)
tbEntrya=Entry(data,width=60)
tbEntrya.grid(row=5,column=35)

Labeloutput=Label(data,text=(" "),font=("castellar",15),fg="RED")
Labeloutput.grid(row=6,column=100)
btnname=Button(data,text="SUBMIT",font=("monotype corsiva",15),fg="white",bg="ORANGE")
btnname.grid(row=7,column=1)
btnname=Button(data,text="CLOSE",font=("monotype corsiva",15),fg="white",bg="orange")
btnname.grid(row=7,column=2)
btnname=Button(data,text="CANCEL",font=("monotype corsiva",15),fg="white",bg="orange")
btnname.grid(row=7,column=3)











data.mainloop()