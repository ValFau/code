from tkinter import *
from bazooka import *
from roquette import*


def create_roquette1():
    roquette=roquette(can,b1.x2,ba,y2,'red2')

# Code pour tester sommairement la classe Bazouka :
f = Tk()
can = Canvas(f,width =500, height =250, bg ='ivory')
can.pack(padx =10, pady =10)
b1 = Bazooka(can, 50, 200)
roquette1=Roquette(can,250,125,'green')
b2 = Bazooka (can,150,50)

s1 =Scale(f, label='hausse', from_=90, to=-90, command=b1.orienter)
s1.pack(side=LEFT, pady =5, padx =20)
s1.set(25)
s2 =Scale(f, label='hausse', from_=90, to=-90, command=b2.orienter)
s2.pack(side=RIGHT, pady =5, padx =20)
s2.set(25)
#button feu 
bouton=Button(f, text="tir",command=create_roquette1 )
bouton.pack(side=LEFT ) 
bouton=Button(f, text="tir", command=create_roquette1)
bouton.pack(side=RIGHT )



# angle de tir initial
f.mainloop()
#a
