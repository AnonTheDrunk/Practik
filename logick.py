def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return 0


'''def check_double(value):
    all_num = value.split(' ')

    all_num2 = []

    for i in range(1,len(all_num) - 1):

        if all_num[i] == '.':
            if all_num[i + 1] != '*' or all_num[i + 1] != '/' or all_num[i + 1] != '+' or all_num[i + 1] != '-':

                if all_num[i - 1] == '*' or all_num[i - 1] == '/' or all_num[i - 1] == '+' or all_num[i - 1] == '-':
                    all_num2.append(0.)
            else:
                all_num2.append(all_num[i-1]+all_num[i]+all_num[i]+1)
        elif all_num[i] == '0.':
            if all_num[i + 1] != '*' or all_num[i + 1] != '/' or all_num[i + 1] != '+' or all_num[i + 1] != '-':
                all_num2.append(str(all_num[i])+all_num[i+1])
        else:
            all_num2.append(all_num[i])

    print(all_num2)
    return all_num2'''


def mult_div(all_num):
    x = []

    for i in range(1, len(all_num) - 1, 2):
        if all_num[i] == '*':
            a = float(all_num[i - 1])
            b = float(all_num[i + 1])
            x.append(mult(a, b))
            '''x[i + 1] = mult(a, b)
            x[i] = ' '
            x[i - 1] = ' '''

        elif all_num[i] == '/':
            a = float(all_num[i - 1])
            b = float(all_num[i + 1])
            x.append(div(a, b))
            ''''x[i + 1] = div(a, b)
            x[i] = ' '
            x[i - 1] = ' '''''

        else:
            x.append(all_num[i])
    print('x: ', x)
    return x


def plus_minus(zz):
    print(zz)
    z = []
    y = []
    y.extend(zz)

    for i in range(1, len(y) - 1, 2):

        if y[i] == '+':
            a = float(y[i - 1])
            b = float(y[i + 1])
            z.append(plus(a, b))
            '''z[i + 1] = plus(a, b)
            z[i] = ' '
            z[i - 1] = ' '''
        elif y[i] == '-':
            a = float(y[i - 1])
            b = float(y[i + 1])
            z.append(minus(a, b))
            '''z[i + 1] = minus(a, b)
            z[i] = ' '
            z[i - 1] = ' '''

        else:
            z.append(y[i])

    '''y.clear()

    for i in range(len(z)):
        if z[i] != ' ':
            y.append(z[i])
    z.clear()'''
    #print(y)
    #y = y[0]
    print(z)
    return z


def output(value):
    all_num = value.split(' ')
    zz = mult_div(all_num)
    z = plus_minus(zz)

    zz.clear()
    print(z)
    return z or zz
