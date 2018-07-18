__author__ = 'Шелест Леонид Викторович'
"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def get_data() -> int or None:
    n = int(input('Введи целое число от 1 до 1000 '))
    return n


def f_n(n: int):
    if n == 1:
        return 1
    else:
        return -f_n(n-1) / 2


def main():
    data = get_data()
    if data:
        print(sum([f_n(i) for i in range(1, data + 1)]))


if __name__ == '__main__':
    main()