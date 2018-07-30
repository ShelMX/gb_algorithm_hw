__author__ = 'Шелест Леонид Викторович'
"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, элементы которого это цифры числа.
"""
import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s]: %(message)s')
logging.disable(level=logging.DEBUG)

hex_ = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
dec_ = {v: k for k,v in hex_.items()}


def addition(add_1: list, add_2: list) -> list:
    result = []
    a, b = (add_1[::-1], add_2[::-1]) if len(add_1) >= len(add_2) else (add_2[::-1], add_1[::-1])

    logging.debug(f"{a} + {b}")

    for i in range(len(a)):
        temp = []
        if len(a[:i+1]) == len(b[:i+1]):
            t = hex_[a[i]] + hex_[b[i]]
            if t >= 16:
                temp.append(dec_[t-16])
                temp.append(dec_[1])
            else:
                temp.append(dec_[t])
        else:
            temp.append(a[i])

        logging.debug(f"{i}. temp = {temp}, result = {result}")
        logging.debug(f"{i}. {len(result[:i+1])} == {i + 1}")

        if len(result[:i+1]) == i + 1:
            if hex_[result[i]] + hex_[temp[0]] >= 16:
                result[i] = dec_[hex_[result[i]] + hex_[temp[0]] - 16]
                if len(temp) == 2:
                    temp[1] = hex_[dec_[temp[1]] + 1]
                else:
                    temp.append(dec_[1])

                logging.debug(f"{i}. {len(result[:i+2])} == {i + 2}")

                if len(result[:i+2]) == i + 2:
                    result[i+1] = dec_[hex_[result[i]] + hex_[temp[0]]]
                else:
                    result.append(temp[1])
            else:
                result[i] = dec_[hex_[result[i]] + hex_[temp[0]]]
                if len(temp) == 2:
                    result.append(temp[1])

        else:
            for k in temp:
                result.append(k)

        logging.debug(f"{i}. temp = {temp}, result = {result}")

    return result[::-1]


def multiplication(multi_1: list, multi_2: list) -> list:
    result = ['0']
    a = int(''.join(multi_1), 16)
    b = int(''.join(multi_2), 16)
    add_x, lim = (multi_1, b) if a > b else (multi_1, a)
    for i in range(lim):
        result = addition(add_1=result, add_2=add_x)
    return result


def main(a: list, b: list):

    result_add = addition(add_1=a, add_2=b)
    print(f"{''.join(a)} + {''.join(b)} = {''.join(result_add)}")
    print()
    result_multi = multiplication(multi_1=a, multi_2=b)
    print(f"{''.join(a)} x {''.join(b)} = {''.join(result_multi)}")


if __name__ == '__main__':
    main(a=['5', '0', 'F', '1'], b=['F', 'A', 'F'])
