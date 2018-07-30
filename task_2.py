__author__ = 'Шелест Леонид Викторович'
"""
Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def get_data(n: int=None) -> list:

    while not n:

        result = input('Введи любое натуральное число и нажми интер ')
        check = result
        if not float(check) // 1:
            continue

        return list(map(int, result))
    return list(map(int, str(n)))


def analize_data(data: list) -> str:
    count_odd = 0
    count_even = 0
    for i in data:
        if i//2:
            count_odd += 1
        else:
            count_even += 1
    return count_even, count_odd
    # return f"В числе {''.join(map(str, data))} " \
    #        f"\nчётных цифр - {count_even}, " \
    #        f"\nнечётных цифр - {count_odd}"


def main(n: int=None):
    data = get_data(n=n)
    if data:
        return analize_data(data=data)


if __name__ == '__main__':
    main()
