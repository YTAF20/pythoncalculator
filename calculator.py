from tkinter import *

def add():
    result.set(float(num1.get()) + float(num2.get()))

def subtract():
    result.set(float(num1.get()) - float(num2.get()))

def multiply():
    result.set(float(num1.get()) * float(num2.get()))

def divide():
    result.set(float(num1.get()) / float(num2.get()))

root = Tk()
root.title("Calculator")

num1 = Entry(root)
num1.grid(row=0, column=1)
num2 = Entry(root)
num2.grid(row=1, column=1)

result = DoubleVar()
Label(root, text="Result:").grid(row=4, column=0)
Label(root, textvariable=result).grid(row=4, column=1)

Button(root, text="Add", command=add).grid(row=2, column=0)
Button(root, text="Subtract", command=subtract).grid(row=2, column=1)
Button(root, text="Multiply", command=multiply).grid(row=3, column=0)
Button(root, text="Divide", command=divide).grid(row=3, column=1)

root.mainloop()