__author__ = 'Шелест Леонид Викторович'
"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. 
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def get_data() -> tuple:
    check = input('Введи любую цифру, которую необходимо посчитать в последовательности ')
    data = input('Введи любую последовательность чисел ')
    return data, check


def get_answer(numbers: str, check: str) -> str:
    answer = numbers.count(check)
    return f"Цифра {check} встречается {answer} раз, в последовательности '{numbers}'"


def main():
    numbers, check = get_data()
    if numbers and check:
        print(get_answer(numbers=numbers, check=check))


if __name__ == '__main__':
    main()
