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


def mult_div(all_num):
    x = []
    x.extend(all_num)
    y = []

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

    x.clear()
    return y


def plus_minus(zz):
    z = []
    z.extend(zz)
    y = []
    y.extend(z)

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
    return y[0]


def output(value):
    all_num = value.split(' ')
    zz = []
    zz.extend(mult_div(all_num))

    if plus_minus(zz).is_integer():
        z = int(plus_minus(zz))
    else:
        z = plus_minus(zz)

    zz.clear()
    return z
