import tkinter as tk
from tkinter import *
top = Tk()
top.title("My Calculator")

sralik= False       #turns on in memo1, turns off in other functions
dalek = False       #turns on in memo0, turns off in other functions
r =0                #main memory of the result
te=DoubleVar()      #saves the number from the upper Entry
tet=DoubleVar()     #saves the number from the lower Entry
v=5                 # position where the results start
def Plus():
    global v, r, dalek, sralik
    if dalek == False:
        c = tet.get()
        a = te.get()
    elif dalek== True:
        if sralik == False:
            c = tet.get()
            a = r
        elif sralik==True:
            a = te.get()
            c=r
    last = Label(top, text="               0                 ").grid(row=7, column=0)
    l0 = Label(top, text="memory is empty   ").grid(row=6, column=0)
    plable=Label(top, text="Adding").grid(row=v, column=1)
    mplable= tk.Label(top, text=a+c)
    mplable.grid(row=v+1, column=1)
    r = a + c
    v = v+2
    if sralik == False:
        memory1 = Button(top, text="m2", command=Memo1).grid(row=3, column=1)
        mEntry = Entry(top, textvariable=te).grid(row=1, column=0)
    elif sralik == True:
        memory0 = Button(top, text="m1", command=Memo0).grid(row=1, column=1)
        mEntry = Entry(top, textvariable=tet).grid(row=3, column=0)
    dalek = False
    sralik = False

def Minus():
    global v, r, dalek, sralik
    if sralik ==False:
        c = tet.get()
        if dalek == False:
            a = te.get()
        elif dalek == True:
            a = r
            last = Label(top, text="               0                 ").grid(row=7, column=0)
            l0 = Label(top, text="memory is empty   ").grid(row=6, column=0)
        r = a - c
        mEntry = Entry(top, textvariable=te).grid(row=1, column=0)
        memory1 = Button(top, text="m2", command=Memo1).grid(row=3, column=1)
    elif sralik ==True:
            c = te.get()
            if dalek == False:
                a = tet.get()
            elif dalek == True:
                a = r
                last = Label(top, text="               0                 ").grid(row=7, column=0)
                l0 = Label(top, text="memory is empty     ").grid(row=6, column=0)
            r = c-a
            mEntry = Entry(top, textvariable=tet).grid(row=3, column=0)
            memory0 = Button(top, text="m1", command=Memo0).grid(row=1, column=1)
    milable = Label(top, text=r).grid(row=v + 1, column=1)
    mlable = Label(top, text="Substracting").grid(row=v, column=1)
    v = v + 2
    dalik = False
    sralik = False
def Divide():
    global v, r, dalek, sralik
    if sralik == False:
        c = tet.get()
        if c == 0:
            pass
        if dalek == False:
            a = te.get()
        elif dalek == True:
            a = r
            last = Label(top, text="               0                 ").grid(row=7, column=0)
            l0 = Label(top, text="memory is empty   ").grid(row=6, column=0)
        r = a / c
        mEntry = Entry(top, textvariable=te).grid(row=1, column=0)
        memory1 = Button(top, text="m2", command=Memo1).grid(row=3, column=1)
    elif sralik == True:
        c = te.get()
        if dalek == False:
            a = tet.get()
        elif dalek == True:
            a = r
            last = Label(top, text="               0                 ").grid(row=7, column=0)
            l0 = Label(top, text="memory is empty     ").grid(row=6, column=0)
        if a == 0:
            pass
        r = c / a
        mEntry = Entry(top, textvariable=tet).grid(row=3, column=0)
        memory0 = Button(top, text="m1", command=Memo0).grid(row=1, column=1)

    dlable=Label(top, text="Dividing").grid(row=v, column=1)
    mdlable= Label(top, text=r).grid(row=v+1, column=1)
    v = v + 2
    dalik = False
    sralik = False
def Multiply():
    global v, dalek, r, sralik
    if dalek == False:
        c = tet.get()
        a = te.get()
    elif dalek== True:
        if sralik == False:
            c = tet.get()
            a = r
        elif sralik==True:
            a = te.get()
            c=r
    last = Label(top, text="               0                 ").grid(row=7, column=0)
    l0 = Label(top, text="memory is empty   ").grid(row=6, column=0)
    mulable=Label(top, text="Multiplying").grid(row=v, column=1)
    mullable= Label(top, text=a*c).grid(row=v+1, column=1)
    mEntry = Entry(top, textvariable=te).grid(row=1, column=0)
    r=a*c
    v = v+2
    if sralik == False:
        memory1 = Button(top, text="m2", command=Memo1).grid(row=3, column=1)
        mEntry = Entry(top, textvariable=te).grid(row=1, column=0)
    elif sralik == True:
        memory0 = Button(top, text="m1", command=Memo0).grid(row=1, column=1)
        mEntry = Entry(top, textvariable=tet).grid(row=3, column=0)
    dalek = False
    sralik = False
def Memo0():
    global r, dalek
    dalek=True
    if dalek == True:
        memory1 = Button(top, text="m2", state = DISABLED).grid(row=3, column=1)
        mEntry = Entry(top, state = DISABLED).grid(row=1, column=0)
        last = Label(top, text=r).grid(row=7, column=0)
        l0 = Label(top, text="First number              ").grid(row=6, column=0)

def Memo1():
    global r, dalek, sralik
    dalek=True
    sralik =True
    if sralik == True:
        memory0 = Button(top, text="m1", state = DISABLED).grid(row=1, column=1)
        mEntry = Entry(top, state = DISABLED).grid(row=3, column=0)
        last = Label(top, text=r).grid(row=7, column=0)
        l0 = Label(top, text="Second number           ").grid(row=6, column=0)

def erace ():
    global dalek, sralik, r
    r =0
    te.set(0)
    tet.set(0)
    memory0 = Button(top, text="m1", command=Memo0).grid(row=1, column=1)
    memory1 = Button(top, text="m2", command=Memo1).grid(row=3, column=1)
    mEntry = Entry(top, textvariable=tet).grid(row=3, column=0)
    mEntry = Entry(top, textvariable=te).grid(row=1, column=0)
    last = Label(top, text="               0                 ").grid(row=7, column=0)
    l0 = Label(top, text="memory is empty   ").grid(row=6, column=0)
    dalek =False
    sralik=False
def cancel ():
    global dalek, sralik
    memory0 = Button(top, text="m1", command=Memo0).grid(row=1, column=1)
    memory1 = Button(top, text="m2", command=Memo1).grid(row=3, column=1)
    mEntry = Entry(top, textvariable=tet).grid(row=3, column=0)
    mEntry = Entry(top, textvariable=te).grid(row=1, column=0)
    last = Label(top, text="               0                 ").grid(row=7, column=0)
    l0 = Label(top, text="memory is empty   ").grid(row=6, column=0)
    dalek =False
    sralik=False

l1=Label (top, text='First number')
l1.grid(row=0, column=0)
mEntry=Entry(top, textvariable=te).grid(row=1, column=0)
l2=Label (top, text='Second number')
l2.grid(row=2, column=0)
memory0=Button(top, text="m1", command=Memo0).grid(row=1, column=1)
memory1=Button(top, text="m2", command=Memo1).grid(row=3, column=1)
cke=Button(top, text="c", command=erace).grid(row=1, column=2)
mEntry=Entry(top, textvariable=tet).grid(row=3, column=0)
Cancel=Button(top, text="cancel memory", command=cancel).grid(row=4, column=1)
p = Button(top, text="+", command=Plus)
p.grid(row=4, column=2, sticky=W)
m = Button(top, text="-", command=Minus)
m.grid(row=4, column=3, sticky=W)
d = Button(top, text="/", command=Divide)
d.grid(row=4, column=4, sticky=W)
mul = Button(top, text="*", command=Multiply)
mul.grid(row=4, column=5, sticky=W)
top.mainloop()

