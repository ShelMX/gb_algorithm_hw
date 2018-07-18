__author__ = 'Шелест Леонид Викторович'
"""
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. 
Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
"""


def main() -> list:
    result = []
    i = 32
    n = 127
    j = 0
    temp = []
    for s in range(i, n+1):
        temp.append((s, chr(s)))
        j += 1
        if j < 10:
            continue
        else:
            print(temp)
            result.append(temp)
            temp = []
            j = 0
    if temp:
        print(temp)
        result.append(temp)

    return result


if __name__ == '__main__':
    main()
