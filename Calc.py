import tkinter as tk
from tkinter import messagebox

mainWindow=tk.Tk()
mainWindow.title("Calculater")

heading_label1= tk.Label(mainWindow, text="First Number")
heading_label1.pack()

name_field1=tk.Entry(mainWindow)
name_field1.pack()

heading_label2= tk.Label(mainWindow, text="First Number")
heading_label2.pack()

name_field2=tk.Entry(mainWindow)
name_field2.pack()

def value():
    first=name_field1.get()
    second=name_field2.get()

    try:
        first=int(first)
        second=int(second)

        return first,second

    except ValueError:
        if((len(name_field1.get())==0)or(len(name_field2.get())==0)):
           messagebox.showerror("Error","Please Enter Value")
        else:
            messagebox.showerror("Error", "Please Enter only integer Value")
        quit(0)


def add():
    first,second=value()
    result=first+second
    result_label.config(text="Operation result is:" +str(result))
def subtract():
    first, second = value()
    result = first - second
    result_label.config(text="Operation result is:" + str(result))
def multiply():
    first, second = value()
    result = first * second
    result_label.config(text="Operation result is:" + str(result))
def divide():
    first, second = value()

    if second==0:
        messagebox.showerror("Error","Cannot divide by 0")
    else:
        result = first /second
        result=round(result,2)
        result_label.config(text="Operation result is:" + str(result))


button1= tk.Button(mainWindow, text="+",command=lambda:add())
button1.pack()

button2= tk.Button(mainWindow, text="-",command=lambda:subtract())
button2.pack()

button3= tk.Button(mainWindow, text="*",command=lambda:multiply())
button3.pack()

button4= tk.Button(mainWindow, text="/",command=lambda:divide())
button4.pack()

result_label=tk.Label(mainWindow, text="operation result is:")
result_label.pack()

mainWindow.mainloop()