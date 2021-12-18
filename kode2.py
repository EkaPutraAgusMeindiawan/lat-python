import tkinter as tk
from tkinter.constants import LEFT

def hasill():
    angki = tb2.get()
    angko = tb3.get()
    angke = tb4.get()
    hasel = float(angki)*float(angko)*float(angke)
    text.set(str(hasel))

def hasill2():
    angki2 = tb8.get()
    angko3 = tb6.get()
    angke4 = tb7.get()
    hasel2 = float(angki2)*float(angko3)*float(angke4)
    text2.set(str(hasel2))

def hasill3():
    if lb5.get() > lb9.get() : tb1.get()
    else : tb2.get()
    hasill3=text3()

window = tk.Tk()
window.title("judul")
window.geometry("600x800")

lb1= tk.Label(window,text="Nama kota",font=('helvetica',12,"bold"))
lb1.pack()
tb1 = tk.Entry(window,font=('helvetica',15,"bold"),justify=tk.CENTER)
tb1.pack()

lb2=tk.Label(window,text="hargi",font=('helvetica',12,"bold"))
lb2.pack()
tb2 = tk.Entry(window,font=('helvetica',10,"bold"),justify=tk.CENTER)
tb2.pack()

lb3=tk.Label(window,text="hargo",font=('helvetica',12,"bold"))
lb3.pack()
tb3 = tk.Entry(window,font=('helvetica',10,"bold"),justify=tk.CENTER)
tb3.pack()

lb4=tk.Label(window,text="harge",font=('helvetica',12,"bold"))
lb4.pack()
tb4 = tk.Entry(window,font=('helvetica',10,"bold"),justify=tk.CENTER)
tb4.pack()

btn=tk.Button(window,text="cek",command=hasill)
btn.pack()

text =  tk.StringVar()
text.set("0")
lb5=tk.Entry(window,text="anjass",font=('helvetica',12,"bold"),textvariable=text)
lb5.pack()

lb10=tk.Label(window,text="Nama kota",font=('helvetica',12,"bold"))
lb10.pack()
tb10 = tk.Entry(window,font=('helvetica',15,"bold"),justify=tk.CENTER)
tb10.pack()

lb6=tk.Label(window,text="hargi",font=('helvetica',12,"bold"))
lb6.pack()
tb6 = tk.Entry(window,font=('helvetica',10,"bold"),justify=tk.CENTER)
tb6.pack()

lb7=tk.Label(window,text="hargo",font=('helvetica',12,"bold"))
lb7.pack()
tb7 = tk.Entry(window,font=('helvetica',10,"bold"),justify=tk.CENTER)
tb7.pack()

lb8=tk.Label(window,text="harge",font=('helvetica',12,"bold"))
lb8.pack()
tb8 = tk.Entry(window,font=('helvetica',10,"bold"),justify=tk.CENTER)
tb8.pack()

btn=tk.Button(window,text="cek",command=hasill2)
btn.pack()

text2 =  tk.StringVar()
text2.set("0")
lb9=tk.Entry(window,text="anjass",font=('helvetica',12,"bold"),textvariable=text2)
lb9.pack()

btn=tk.Button(window,text="hasil perbandingan",command=hasill3)
btn.pack()

text3 = tk.IntVar()
text3.set("a")
lb11=tk.Label(window,text="Perbandingan",font=('helvetica',12,"bold"),textvariable=text3)
lb11.pack




window.mainloop()