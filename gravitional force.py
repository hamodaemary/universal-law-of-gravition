from tkinter import *
from math import sqrt
def calc():
	y = 6.67*10**-11
	z = int(ent1.get())
	c = int(ent2.get())
	g = int and float(ent3.get())
	f = (y*z*c) / g**2
	lbl.config(text=f)
x=Tk()
x.config(bg='black')
x.title('gravitional force')
lbl0 = Label(text='first mass',fg='white',bg='black').pack()
ent1 = Entry(x)
ent1.pack()
lblx = Label(text='second mass',fg='white',bg='black').pack()
ent2 = Entry(x)
ent2.pack()
lbly = Label(text='raduis',fg='white',bg='black').pack()
ent3 = Entry(x)
ent3.pack()
lbl = Label(text='',bg='black',fg='white')
lbl.pack()
but = Button(text='command',command=calc)
but.pack()
x.mainloop()