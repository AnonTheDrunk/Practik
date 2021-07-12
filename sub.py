from tkinter import *
from logick import *


class Interface:
    def __init__(self):
        root = Tk()
        root.title("Калькулятор")
        root.geometry("600x400")
        self.frame1 = Frame(root)
        self.frame2 = Frame(root)
        self.input_field = Entry(self.frame1, state='disabled')
        self.buttons()
        root.mainloop()

    def answer_output(self, new_char):
        self.input_field.configure(state='normal')
        self.input_field.delete(0, END)
        self.input_field.insert(0, new_char)
        self.input_field.configure(state='disabled')

    def insert_into_input(self, new_char):
        self.input_field.configure(state='normal')
        value = self.input_field.get()
        value += new_char
        self.input_field.delete(0, END)
        self.input_field.insert(0, value)
        self.input_field.configure(state='disabled')

    def press1(self):
        self.insert_into_input('1')

    def press2(self):
        self.insert_into_input('2')

    def press3(self):
        self.insert_into_input('3')

    def press4(self):
        self.insert_into_input('4')

    def press5(self):
        self.insert_into_input('5')

    def press6(self):
        self.insert_into_input('6')

    def press7(self):
        self.insert_into_input('7')

    def press8(self):
        self.insert_into_input('8')

    def press9(self):
        self.insert_into_input('9')

    def press0(self):
        self.insert_into_input('0')

    def press_plus(self):
        self.insert_into_input(" + ")

    def press_minus(self):
        self.insert_into_input(" - ")

    def press_div(self):
        self.insert_into_input(" / ")

    def press_multiply(self):
        self.insert_into_input(" * ")

    def press_equal(self):
        self.answer_output(output(self.input_field.get()))

    def press_del(self):
        self.input_field.configure(state='normal')
        self.input_field.delete(0, END)
        self.input_field.configure(state='disabled')

    def buttons(self):
        btn1 = Button(self.frame1, text="1", width=10, height=6, command=self.press1)
        btn2 = Button(self.frame1, text="2", width=10, height=6, command=self.press2)
        btn3 = Button(self.frame1, text="3", width=10, height=6, command=self.press3)
        btn4 = Button(self.frame1, text="4", width=10, height=6, command=self.press4)
        btn5 = Button(self.frame1, text="5", width=10, height=6, command=self.press5)
        btn6 = Button(self.frame1, text="6", width=10, height=6, command=self.press6)
        btn7 = Button(self.frame1, text="7", width=10, height=6, command=self.press7)
        btn8 = Button(self.frame1, text="8", width=10, height=6, command=self.press8)
        btn9 = Button(self.frame1, text="9", width=10, height=6, command=self.press9)
        btn0 = Button(self.frame1, text="0", width=10, height=6, command=self.press0)
        btnP = Button(self.frame2, text="+", width=10, height=6, command=self.press_plus)
        btnM = Button(self.frame2, text="-", width=10, height=6, command=self.press_minus)
        btnMult = Button(self.frame2, text="*", width=10, height=6, command=self.press_multiply)
        btnDiv = Button(self.frame2, text="/", width=10, height=6, command=self.press_div)
        btnE = Button(self.frame1, text="=", width=10, height=6, command=self.press_equal)
        btn_del = Button(self.frame1, text="C", width=10, height=6, command=self.press_del)
        # btn_

        self.frame1.pack(side=LEFT, fill="x")
        self.frame2.pack(side=LEFT, fill="x")

        btnP.grid(row=0, column=0)
        btnM.grid(row=0, column=1)
        btnMult.grid(row=1, column=0)
        btnDiv.grid(row=1, column=1)

        self.input_field.grid(row=0, column=0, columnspan=2)
        btn1.grid(row=1, column=0)
        btn2.grid(row=1, column=1)
        btn3.grid(row=1, column=2)
        btn4.grid(row=2, column=0)
        btn5.grid(row=2, column=1)
        btn6.grid(row=2, column=2)
        btn7.grid(row=3, column=0)
        btn8.grid(row=3, column=1)
        btn9.grid(row=3, column=2)
        btn0.grid(row=4, column=1)
        btnE.grid(row=4, column=2)
        btn_del.grid(row=4, column=0)
