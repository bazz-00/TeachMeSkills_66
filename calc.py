from math import sin, cos, log
def check():
    if len(expression) < 2:
        result1 = 'enter correct values'
    elif (expression[0] != 'sin' and expression[0] != 'cos' and expression[0] != 'log')\
    and expression[0].replace('-', '', 1).replace('.', '', 1).isdigit() != True:
        result1 = 'enter correct values'
        return result1
    else: return ''

def calc():        # создаем функцию
    if expression[1] == '+':
        expression[0] = float(expression[0])
        expression[2] = float(expression[2])
        result = expression[0] + expression[2]
    elif expression[1] == '-':
        expression[0] = float(expression[0])
        expression[2] = float(expression[2])
        result = expression[0] - expression[2]
    elif expression[1] == '*':
        expression[0] = float(expression[0])
        expression[2] = float(expression[2])
        result = expression[0] * expression[2]
    elif expression[1] == '/' and expression[2] == '0':   # нельзя делить на ноль
        result = "can't divide by zero"
    elif expression[1] == '/':
        expression[0] = float(expression[0])
        expression[2] = float(expression[2])
        result = expression[0] / expression[2]
    elif expression[0] == 'cos':
        degree = float(expression[1])            # преобразуем строку в число
        result = cos(degree)
    elif expression[0] == 'sin':
        degree = float(expression[1])
        result = sin(degree)
    elif expression[0] == 'log':
        degree = float(expression[1])
        result = log(degree)
    return result
while True:            # основная программа
    expression = list(map(str, input('enter values: ').split())) or '0' # ввод одной строкой преобразуем в список
    print(check())
    print(calc())
    question = input('do you want to do another calculation? ')
    if question == 'yes':
        continue
    else:
        break
