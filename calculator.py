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
root.configure(background='white')

num1 = Entry(root, bg='white')
num1.grid(row=0, column=1)
num2 = Entry(root, bg='white')
num2.grid(row=1, column=1)

result = DoubleVar()
Label(root, text="Result:", bg='white').grid(row=4, column=0)
Label(root, textvariable=result, bg='white').grid(row=4, column=1)

Button(root, text="Add", command=add, bg='white').grid(row=2, column=0)
Button(root, text="Subtract", command=subtract, bg='white').grid(row=2, column=1)
Button(root, text="Multiply", command=multiply, bg='white').grid(row=3, column=0)
Button(root, text="Divide", command=divide, bg='white').grid(row=3, column=1)

root.mainloop()