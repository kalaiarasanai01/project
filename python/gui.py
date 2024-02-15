'''from tkinter import *
master = Tk()
w=Canvas(master,width=60,height=80)
w.pack()
Canvas_height=20
Canvas_width=200
y=int(Canvas_height/2)
w.create_line(0,y,Canvas_width,y)
mainloop()'''


'''from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='kalai', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='surya', variable=var2).grid(row=1, sticky=W)
var3 = IntVar
Checkbutton(master,text='Rooban', variable=var3).grid(row=2, sticky=W)
var4 = IntVar
Checkbutton(master,text='hari',variable=var4).grid(row=3, sticky = W)
mainloop()
'''


from tkinter import *
kalai = Tk()
LB = Listbox(kalai)
LB.insert(1, 'python')
LB.insert(2, 'Java')
LB.insert(3, 'C++')
LB.insert(4, 'SQL')
LB.pack()
kalai.mainloop()
