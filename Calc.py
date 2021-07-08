class MathC:


    def choise(self,a,b):
        x = input("Select math action (+, -, *, /)\n")

        if x == '+':
            return a + b
        elif x == '-':
            return a - b
        elif x == '*':
            return a * b
        elif x == '/':
            try:
                return a / b
            except ZeroDivisionError:
                return 0
        else:
            print("Please enter one of the math action\n")
            self.calc()


    def calc(self):
        while True:
            a = input("Enter first number\n")
            b = input("Enter second number\n")

            if a.isdigit() == True and b.isdigit() == True:
                a = int(a)
                b = int(b)
                print(int(self.choise(a,b)))

                z = input("Do you want to do it again y/n?\n")
                if z == 'y' or z == 'Y':
                    print("Starting over\n")
                else:
                    print("Bye\n")
                    break
            else:
                print("PLease enter the numbers\n")

            '''self.a = None
            self.b = None
            self.x = None
            self.z = None'''

    #calc()
answer = MathC().calc()
print(answer)