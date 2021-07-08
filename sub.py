from tkinter import *

def MA(x):
    if x == '+':
        plus(a,b)
    elif x == '-':
        minus(a,b)
    elif x == '*':
        mult(a,b)
    elif x == '/':
        try:
            div(a,b)
        except ZeroDivisionError:
            return 0

def inputs(a):
    aa = a
    #return aa
    print(aa)

def plus(a,b):
    return a + b

def minus(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a / b

root = Tk()
root.title("Калькулятор")
root.geometry("600x400")

btn1 = Button(root, text="1", width=3, height=2, command=inputs(1))
btn2 = Button(root, text="2", width=3, height=2, command=inputs(1))
btn3 = Button(root, text="3", width=3, height=2, command=inputs(1))
btn4 = Button(root, text="4", width=3, height=2, command=inputs(1))
btn5 = Button(root, text="5", width=3, height=2, command=inputs(1))
btn6 = Button(root, text="6", width=3, height=2, command=inputs(1))
btn7 = Button(root, text="7", width=3, height=2, command=inputs(1))
btn8 = Button(root, text="8", width=3, height=2, command=inputs(1))
btn9 = Button(root, text="9", width=3, height=2, command=inputs(1))
btn0 = Button(root, text="0", width=3, height=2, command=inputs(1))
btnP = Button(root, text="+", width=3, height=2, command=inputs(1))
btnM = Button(root, text="-", width=3, height=2, command=inputs(1))
btnMult = Button(root, text="*", width=3, height=2, command=inputs(1))
btnDiv = Button(root, text="/", width=3, height=2, command=inputs(1))

btn.pack(side="left")




root.mainloop()