__author__ = 'Шелест Леонид Викторович'
"""
Написать программу, которая будет складывать, вычитать, умножать или делить два числа. 
Числа и знак операции вводятся пользователем. 
После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. 
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. 
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), 
то программа должна сообщать ему об ошибке и снова запрашивать знак операции. 
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
"""


def simple_calc(data: list) -> str:
    if data[0] == '+':
        result = data[1] + data[2]
    
    elif data[0] == '-':
        result = data[1] - data[2]
    
    elif data[0] == '*':
        result = data[1] * data[2]
    
    else:
        result = data[1] / data[2]
    
    return f"{data[1]} {data[0] if data[2] > 0 else '-'} {abs(data[2])} = {result}"

def get_data() -> list or None:
    check = ['0', '+', '-', '*', '/']
    flag = True
    while flag:
        operation = input("Выбери операцию (+, -, /, *) и введи этот знак.\nЕсли хочешь завершить программу введи 0. ")
        if operation == '0':
            return None
        elif operation not in check:
            continue
        else:
            a = input(f"Для операции '{operation}' введи первое число (целое) = ")
            while flag:
                b = input(f"Для операции '{operation}' введи второе число (целое) = ")
                if operation == '/' and b == '0':
                    print('P.S. На 0 делить низя!')
                else:
                    flag = False
    return [operation, int(a), int(b)]


def main():
    data = get_data()
    if data:
        result = simple_calc(data=data)
        print(result)


if __name__ == '__main__':
    main()
