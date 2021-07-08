from tkinter import *

'''def MA(x):
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
    aa = [int(a)]
    #return aa
    

def plus(a,b):
    return a + b

def minus(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    return a / b '''

root = Tk()
root.title("Калькулятор")
root.geometry("600x400")

frame1 = Frame(root)
frame2 = Frame(root)


btn1 = Button(frame1, text="1", width=10, height=6)#, command=inputs(1))
btn2 = Button(frame1, text="2", width=10, height=6)#, command=inputs(2))
btn3 = Button(frame1, text="3", width=10, height=6)#, command=inputs(3))
btn4 = Button(frame1, text="4", width=10, height=6)#, command=inputs(4))
btn5 = Button(frame1, text="5", width=10, height=6)#, command=inputs(5))
btn6 = Button(frame1, text="6", width=10, height=6)#, command=inputs(6))
btn7 = Button(frame1, text="7", width=10, height=6)#, command=inputs(7))
btn8 = Button(frame1, text="8", width=10, height=6)#, command=inputs(8))
btn9 = Button(frame1, text="9", width=10, height=6)#, command=inputs(9))
btn0 = Button(frame1, text="0", width=10, height=6)#, command=inputs(0))
btnP = Button(frame2, text="+", width=10, height=6)#, command=MA('+'))
btnM = Button(frame2, text="-", width=10, height=6)#, command=MA('-'))
btnMult = Button(frame2, text="*", width=10, height=6)#, command=MA('*'))
btnDiv = Button(frame2, text="/", width=10, height=6)#, command=MA('/'))
btnE = Button(frame1, text="=", width=21, height=6)

'''btn1.pack(side="center")
btn2.pack(side="center")
btn3.pack(side="center")
btn4.pack(side="center")
btn5.pack(side="center")
btn6.pack(side="center")
btn7.pack(side="center")
btn8.pack(side="center")
btn9.pack(side="center")'''



frame1.pack(side=LEFT, fill="x")
frame2.pack(side=LEFT, fill="x")

btnP.grid(row=0,column=0)
btnM.grid(row=0,column=1)
btnMult.grid(row=1,column=0)
btnDiv.grid(row=1,column=1)

btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)
btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)
btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)
btn0.grid(row=3,column=0)
btnE.grid(row=3,column=1, columnspan=2)




root.mainloop()