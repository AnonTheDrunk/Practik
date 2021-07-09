from tkinter import *




def plus(a,b):
    return a + b


def minus(a,b):
    return a - b


def mult(a,b):
    return a * b


def div(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return 0




def output():
    value = input_field.get()
    all_num = value.split(' ')
    length_all_num = len(all_num)
    x = []
    y = []
    z = []
    x.extend(all_num)
    #i = 0
    for i in range(1, length_all_num-1, 2):
        if all_num[i] == '*':
            a = float(x[i-1])
            b = float(x[i+1])

            x[i+1] = mult(a, b)
            x[i]=' '
            x[i-1]=' '


        elif all_num[i] == '/':
            a = float(x[i-1])
            b = float(x[i+1])

            x[i + 1] = div(a, b)
            x[i] = ' '
            x[i - 1] = ' '

    print(x)



    for i in range(length_all_num):
        if x[i] != ' ':
            y.append(x[i])



    z.extend(y)
    print(z)


    for i in range(1, len(y) - 1, 2):

        if y[i] == '+':
            a = float(z[i - 1])
            b = float(z[i + 1])
            z[i + 1] = plus(a, b)
            z[i] = ' '
            z[i - 1] = ' '
        elif y[i] == '-':
            a = float(z[i - 1])
            b = float(z[i + 1])
            z[i + 1] = minus(a, b)
            z[i] = ' '
            z[i - 1] = ' '

    y = set(z)
    for i in range(len(y)):
        y.discard(' ')

    y = list(y)
    y.sort(key=z.index)
    z.clear()
    if y[0].is_integer():
        z = int(y[0])
    else:
        z = y[0]

    print(z)






root = Tk()
root.title("Калькулятор")
root.geometry("600x400")



frame1 = Frame(root)
frame2 = Frame(root)

input_field = Entry(frame1)

def insert_into_input(new_char):
    value = input_field.get()
    value += new_char
    input_field.delete(0, END)
    input_field.insert(0, value)

def press1():
    insert_into_input('1')

def press2():
    insert_into_input('2')

def press3():
    insert_into_input('3')

def press4():
    insert_into_input('4')


def press5():
    insert_into_input('5')


def press6():
    insert_into_input('6')


def press7():
    insert_into_input('7')


def press8():
    insert_into_input('8')

def press9():
    insert_into_input('9')


def press0():
    insert_into_input('0')

def press_plus():
    insert_into_input(" + ")

def press_minus():
    insert_into_input(" - ")

def press_div():
    insert_into_input(" / ")

def press_multiply():
    insert_into_input(" * ")

def press_equal():

    output()

def press_del():
    input_field.delete(0, END)

btn1 = Button(frame1, text="1", width=10, height=6, command=press1)#, command=inputs(1))
btn2 = Button(frame1, text="2", width=10, height=6, command=press2)#, command=inputs(2))
btn3 = Button(frame1, text="3", width=10, height=6, command=press3)#, command=inputs(3))
btn4 = Button(frame1, text="4", width=10, height=6, command=press4)#, command=inputs(4))
btn5 = Button(frame1, text="5", width=10, height=6, command=press5)#, command=inputs(5))
btn6 = Button(frame1, text="6", width=10, height=6, command=press6)#, command=inputs(6))
btn7 = Button(frame1, text="7", width=10, height=6, command=press7)#, command=inputs(7))
btn8 = Button(frame1, text="8", width=10, height=6, command=press8)#, command=inputs(8))
btn9 = Button(frame1, text="9", width=10, height=6, command=press9)#, command=inputs(9))
btn0 = Button(frame1, text="0", width=10, height=6, command=press0)#, command=inputs(0))
btnP = Button(frame2, text="+", width=10, height=6, command=press_plus)#, command=inputs('+'))
btnM = Button(frame2, text="-", width=10, height=6, command=press_minus)#, command=inputs('-'))
btnMult = Button(frame2, text="*", width=10, height=6, command=press_multiply)#, command=inputs('*'))
btnDiv = Button(frame2, text="/", width=10, height=6, command=press_div)#, command=inputs('/'))
btnE = Button(frame1, text="=", width=10, height=6, command=press_equal)#, command=)
btn_del = Button(frame1, text="C", width=10, height=6, command=press_del)


frame1.pack(side=LEFT, fill="x")
frame2.pack(side=LEFT, fill="x")

btnP.grid(row=0,column=0)
btnM.grid(row=0,column=1)
btnMult.grid(row=1,column=0)
btnDiv.grid(row=1,column=1)

input_field.grid(row=0,column=0, columnspan=2)
btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btn7.grid(row=3,column=0)
btn8.grid(row=3,column=1)
btn9.grid(row=3,column=2)
btn0.grid(row=4,column=1)
btnE.grid(row=4,column=2)
btn_del.grid(row=4, column=0)




root.mainloop()