__author__ = 'Шелест Леонид Викторович'
"""
Написать программу, доказывающую или проверяющую, 
что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, 
где n – любое натуральное число.
"""


def main(n: int=None):
    n = n if n else int(input('Введи целое число больше 1 '))
    result = 0
    i = 1
    while i <= n:
        result += i
        i += 1
    control = n * (n + 1) / 2
    if control == result:
        print(f"Сумма чисел от 1 до {n} вычисляется по формуле n*(n + 1)/2 и равна {result:,d}")
    else:
        print(f"Сумма чисел от 1 до {n} равна {result:,d}. Формула n*(n + 1)/2 = {control:,.2f}")


if __name__ == '__main__':
    main()
