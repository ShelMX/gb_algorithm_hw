__author__ = 'Шелест Леонид Викторович'
"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""
import memory_profiler


def get_data(n: int=None) -> int or None:
    n = n if n else int(input('Введи целое число от 1 до 1000 '))
    return n


def f_n(n: int):
    if n == 1:
        return 1
    else:
        return -f_n(n-1) / 2

@memory_profiler.profile
def main(n: int=None):
    data = get_data(n=n)
    if data:
        return sum([f_n(i) for i in range(1, data + 1)])


if __name__ == '__main__':
    main()
