__author__ = 'Шелест Леонид Викторович'
"""
Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def get_data() -> list:

    while True:

        result = input('Введи любое натуральное число и нажми интер ')
        check = result
        if int(float(check)) != float(check):
            continue

        return list(map(int, result))


def analize_data(data: list) -> str:

    n_1 = 0
    n_2 = 0
    for i in data:
        if i//2:
            n_1 += 1
        else:
            n_2 += 1

    return f"В числе {''.join(map(str, data))} " \
           f"\nчётных цифр - {n_2}, " \
           f"\nнечётных цифр - {n_1}"


def main():
    data  = get_data()
    if data:
        print(analize_data(data=data))


if __name__ == '__main__':
    main()