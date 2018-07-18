__author__ = 'Шелест Леонид Викторович'
"""
Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def get_data() -> list:

    while True:

        result = input('Введи любое натуральное число и нажми интер ')
        check = result
        if not float(check) // 1:
            continue

        return list(map(int, result))


def analize_data(data: list) -> str:

    count_odd = 0
    count_even = 0
    for i in data:
        if i//2:
            count_odd += 1
        else:
            count_even += 1

    return f"В числе {''.join(map(str, data))} " \
           f"\nчётных цифр - {count_even}, " \
           f"\nнечётных цифр - {count_odd}"


def main():
    data  = get_data()
    if data:
        print(analize_data(data=data))


if __name__ == '__main__':
    main()
