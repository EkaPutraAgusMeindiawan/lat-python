import tkinter as tk
from tkinter.constants import CENTER

def hasill():
    angka = tb1.get()
    angki = tb2.get()
    angko = tb3.get()
    angke = tb4.get()
    hasel = float(angka)*float(angki)*float(angko)*float(angke)
    text.set(str(hasel))

window = tk.Tk()
window.title("judul")
window.geometry("600x800")

lb1=tk.Label(window,text="harga",font=('helvetica',12,"bold"))
lb1.pack()
tb1 = tk.Entry(window,font=('helvetica',20,"bold"),justify=tk.CENTER)
tb1.pack()

lb2=tk.Label(window,text="hargi",font=('helvetica',12,"bold"))
lb2.pack()
tb2 = tk.Entry(window,font=('helvetica',20,"bold"),justify=tk.CENTER)
tb2.pack()

lb3=tk.Label(window,text="hargo",font=('helvetica',12,"bold"))
lb3.pack()
tb3 = tk.Entry(window,font=('helvetica',20,"bold"),justify=tk.CENTER)
tb3.pack()

lb4=tk.Label(window,text="harge",font=('helvetica',12,"bold"))
lb4.pack()
tb4 = tk.Entry(window,font=('helvetica',20,"bold"),justify=tk.CENTER)
tb4.pack()

btn=tk.Button(window,text="TO",command=hasill)
btn.pack()

text =  tk.StringVar()
text.set("0")
lb5=tk.Label(window,text="anjass",font=('helvetica',12,"bold"),textvariable=text)
lb5.pack()

window.mainloop()