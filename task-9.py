__author__ = 'Шелест Леонид Викторович'
"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. 
Вывести на экран это число и сумму его цифр.
"""


def get_data() -> str:
    data = input('Введи любую последовательность чисел через пробел - ')
    return data


def get_answer(data: str) -> str:
    data = data.split()
    max_ = 0
    num = ''

    for numb in data:
        temp = list(map(int, numb))
        temp_sum = sum(temp)
        if temp_sum > max_:
            max_ = temp_sum
            num = numb

    return f"Из всей последовательности чисел, у числа {num} наибольшая сумма всех цифр = {max_}"


def main():
    data = get_data()
    if data:
        print(get_answer(data=data))


if __name__ == '__main__':
    main()