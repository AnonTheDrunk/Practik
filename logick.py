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


#def mult_div():



def output(value):
    all_num = value.split(' ')
    x = []
    y = []
    z = []
    x.extend(all_num)

    for i in range(1, len(all_num) - 1, 2):
        if all_num[i] == '*':
            a = float(x[i - 1])
            b = float(x[i + 1])

            x[i + 1] = mult(a, b)
            x[i] = ' '
            x[i - 1] = ' '


        elif all_num[i] == '/':
            a = float(x[i - 1])
            b = float(x[i + 1])

            x[i + 1] = div(a, b)
            x[i] = ' '
            x[i - 1] = ' '

    for i in range(len(all_num)):
        if x[i] != ' ':
            y.append(x[i])

    z.extend(y)

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

    y.clear()

    for i in range(len(z)):
        if z[i] != ' ':
            y.append(z[i])

    z.clear()

    if y[0].is_integer():
        z = int(y[0])
    else:
        z = y[0]

    return z
