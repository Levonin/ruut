from tkinter import *
from math import *
from tkinter import messagebox as mb
from turtle import window_height, window_width
import matplotlib.pyplot as plt
import numpy as np

w_open = False
x=450
y=450
bg="#000000"
fg="#3f9f7f"
height=0
roundTo=1
step=4


def solve():
    aa=a.get()
    bb=b.get()
    cc=c.get()
    if not (aa=="" or bb=="" or cc==""):
        D=round((float(bb)**2)-(4*float(aa)*float(cc)),roundTo)
        if D>0:
            x1=round((abs(float(bb))+sqrt(D))/(2*float(aa)),roundTo)
            x2=round((abs(float(bb))-sqrt(D))/(2*float(aa)),roundTo)
            solution.configure(text=f"D={D}\nX₁={x1}\nX₂={x2}")
            graph()
          
        elif D==0:
            x=round(abs(float(bb))/(2*float(aa)),roundTo)
            solution.configure(text=f"D={D}\nX={x}")
            graph()
        else:
            solution.configure(text=f"D={D}\nLahendusi pole")
    else:
        mb.showwarning("Tähelepanu!","On vaja sisestada numbreid!")

def graph():
    if w_open:
        for indeks,i in enumerate(pildid):
            if var.get() == indeks + 1:
                i()

    else:

        aa=float(a.get())
        bb=float(b.get())
        cc=float(c.get())
        x=round(abs(bb)/(2*aa),roundTo)
        x1=numpy.arange(x-step,x+step,float(f"0.{step}"))
        y=aa*x**2+bb*x1+cc
        y1=aa*x1**2+bb*x1+cc
        fig=plt.figure()
        plt.plot(x1,y1,'b-d')
        plt.title('Ruutvõrrand')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()

def Kala():
    x1 = np.arange(0, 9.5, 0.5) #min max step
    y1= (2/27)*x1*x1-3
    x2 = np.arange(-10, 0.5, 0.5)#min max step
    y2= 0.04*x2*x2-3
    x3 = np.arange(-9, -2.5, 0.5) #min max step
    np.arange(-9, -2.5, 0.5) #min max step
    y3=(2/9)*(x3+6)**2+1
    x4 = np.arange(-3, 9.5, 0.5) #min max step
    y4=(-1/12)*(x4-3)**2+6
    x5 = np.arange(5, 9, 0.5) #min max step
    y5=(1/9)*(x5-5)**2+2
    x6 = np.arange(5, 8.5, 0.5) #min max step
    y6=(1/8)*(x6-7)**2+1.5
    x7 = np.arange(-13, -8.5, 0.5) #min max step
    y7=(-0.75)*(x7+11)**2+6
    x8 = np.arange(-15, -12.5, 0.5) #min max step
    y8=(-0.5)*(x8+13)**2+3
    x9= np.arange(-15, -10, 0.5)#min max step
    y9=[1]*len(x9)
    x10 = np.arange(3, 4, 0.5)#min max step
    y10=[3]*len(x10)
    plt.figure()
    plt.plot
    (x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title("Kala")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()

def prillid():
    x1 = np.arange(-9, -0.5, 0.5) #min max step
    y1= (-1/16)*(x1+5)**2+2
    x2 = np.arange(1, 9.5, 0.5)#min max step
    y2= (-1/16)*(x2-5)**2+2
    x3 = np.arange(-9, -0.5, 0.5) #min max step
    y3= (1/4)*(x3+5)**2-3
    x4 = np.arange(1, 9.5, 0.5) #min max step
    y4= (1/4)*(x4-5)**2-3
    x5 = np.arange(-9, -5.5, 0.5) #min max step
    y5=-(x5+7)**2 + 5
    x6 = np.arange(6, 9.5, 0.5) #min max step
    y6= -1*(x6-7)**2+5
    x7 = np.arange (-1, 1.5, 0.5)
    y7= -0.5*x7**2+1.5
    plt.figure()
    plt.plot
    (x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title("prillid")
    plt.ylabel("y")
    plt.xlabel("y")
    plt.grid(True)
    plt.show

def zontik():
    x1=np.arange(-12, 12.5,0.5)
    y1=(-1/18)*x1**2+12
    x2=np.arange(-4, 4.5, 0.5)
    y2=(-1/8)*x2**2+6
    x3 = np.arange(-12, -3.5, 0.5)
    y3= (-1/8)*(x3+8)**2+6
    x4 = np.arange(4, 12.5, 0.5)
    y4= (-1/8)*(x4-8)**2+6
    x5 = np.arange(-4, 0.5, 0.5)
    y5= 2*(x5+3)**2-9
    x6 = np.arange(-4, 0.7, 0.5)
    y6= 1.5*(x6+3)**2-10

    plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6)
    plt.title("Vihmavari")
    plt.ylabel("y")
    plt.xlabel("x")
    plt.grid(True)
    plt.show()


pildid=[prillid,zontik,Kala]

def suurenda_ja_vahenda():
    global x, y, w_open
    if not w_open:
        e.grid()
        t.grid()
        k_.grid()
        w_open = True
        x += 100
        y += 100
        window.geometry(f"{x}x{y}")
    else:
        e.grid_forget()
        t.grid_forget()
        k_.grid_forget()
        w_open = False
        x -= 100
        y -= 100
        window.geometry(f"{x}x{y}")
    window.geometry(f'{x}x{y}')







window=Tk()
window.geometry(f"{x}x{y}")
window.title("Ruutvõrrand")
label=Label(window,
            text="Ruutvõrrandi lahendamine",
            bg=bg,
            fg=fg,
            font="Arial 20",
            height=height,
            width=x)
frame=Frame(window)
a=Entry(frame,
            bg=bg,
            fg=fg,
            font="Arial 20",
            width=2,
            justify=CENTER)
first=Label(frame,
            text="x²+",
            bg=bg,
            fg=fg,
            font="Arial 20",
            height=height,
            width=3)
b=Entry(frame,
              bg=bg,
              fg=fg,
              font="Arial 20",
              width=2,
              justify=CENTER)
second=Label(frame,
            text="x+",
            bg=bg,
            fg=fg,
            font="Arial 20",
            height=height,
            width=2)
c=Entry(frame,
              bg=bg,
              fg=fg,
              font="Arial 20",
              width=2,
              justify=CENTER)
third=Label(frame,
            text="=0",
            bg=bg,
            fg=fg,
            font="Arial 20",
            height=height,
            width=2)
solve1=Button(frame,
            text="Lahenda",
            bg=bg,
            fg=fg,
            font="Arial 20",
            height=height,
            width=7,
            command=solve)
Function=Button(frame,
             text="Graafik",
             bg=bg,
             fg=fg,
             font="Arial 20",
             height=height,
             width=7,
             command=graph)
solution=Label(window,
            text="",
            bg=bg,
            fg=fg,
            font="Arial 20",
            height=height,
            width=x)
lahtimine = Button(frame,
            text = "ekraani suurus",
            bg=bg,
            fg=fg,
            font='Arial 20',
            width=7,
            command = suurenda_ja_vahenda)

label.pack(side="top")
frame.pack(side="top")
solution.pack(side="top")

a.grid(row=0,column=1)
first.grid(row=0,column=2)
b.grid(row=0,column=3)
second.grid(row=0,column=4)
c.grid(row=0,column=5)
third.grid(row=0,column=6)
solve1.grid(row=0,column=7)
lahtimine.grid(row=0,column=8)

Function.grid(row=0,column=9)


f=Frame(window)
var=IntVar() #StringVar()
e=Radiobutton(frame,text="prillid",variable=var,value=1,font="Arial 20",bg="#caff70",)
t=Radiobutton(frame,text="zontik",variable=var,value=2,font="Arial 20",bg="#caff70",)
k_=Radiobutton(frame,text="kala",variable=var,value=3,font="Arial 20",bg="#caff70",)





window.mainloop()