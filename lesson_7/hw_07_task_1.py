__author__ = 'Шелест Леонид Викторович'
"""
Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, 
заданный случайными числами на промежутке [-100; 100). 
Вывести на экран исходный и отсортированный массивы.
"""
import hw_07 as lib


def bubble_sort(nsl: list) -> list:
    """
    classic sorting algorithm - bubble sort.
    :param nsl: type list: non sorted list
    :return: type list: sorted list
    """

    sl = nsl[:]
    n = len(sl)

    if n < 2:
        return sl

    for i in range(len(sl)):
        for j in range(len(sl) - 1, i, -1):
            if sl[j] > sl[j-1]:
                sl[j], sl[j-1] = sl[j-1], sl[j]

    return sl


def main(arr: list = None, is_print: bool = True) -> list:
    """
    main function that combines all the functions of the module.
    :param is_print: type bool: flag, if True, then function will print result, else not print.
    :param arr: type list: non sorted list, if the value of the parameter is not specified,
                           then an array of random numbers is created.
    :return: type list: sorted list
    """

    non_sort_list = arr if arr else lib.generate_int_array()
    sorted_list = bubble_sort(nsl=non_sort_list)

    if is_print:
        print(f"Non sorted list:")
        lib.pretty_print(arr=non_sort_list)
        print(f"\nList after Bubble sort:")
        lib.pretty_print(arr=sorted_list)

    return sorted_list


if __name__ == '__main__':
    main()
