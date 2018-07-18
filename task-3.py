__author__ = 'Шелест Леонид Викторович'
"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
Например, если введено число 3486, то надо вывести число 6843.
"""


def get_data() -> list or str:
    return input("\nВведи число и получи его задом наперёд ")


def reverse_data_1(data: list or str) -> str:
    i = len(data)
    result = []
    while i > 0:
        result.append(data[i-1])
        i -= 1
    return f"Число {data} задом наперёд будет {''.join(result)}"


def reverse_data_2(data: list or str) -> str:
    result = []
    for i in data:
        result.insert(0, i)
    return f"Число {data} задом наперёд будет {''.join(result)}"


def reverse_data_3(data: str) -> str:
    result = list(data)
    result.reverse()
    return f"Число {data} задом наперёд будет {''.join(result)}"


def main():
    print(input("Введи число и получи его задом наперёд ")[::-1])

    data = get_data()
    if data:
        print(reverse_data_1(data=data))

    data = get_data()
    if data:
        print(reverse_data_2(data=data))

    data = get_data()
    if data:
        print(reverse_data_3(data=data))


if __name__ == '__main__':
    main()
