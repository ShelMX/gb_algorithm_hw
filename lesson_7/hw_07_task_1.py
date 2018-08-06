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
    if len(sl) == 1:
        return sl
    elif not sl:
        return []
    else:
        for i in range(len(sl)):
            for j in range(len(sl) - 1, i, -1):
                if sl[j] < sl[j-1]:
                    sl[j], sl[j-1] = sl[j-1], sl[j]

    return sl


def main(mass: list=None, print_: bool=True) -> list:
    """
    main function that combines all the functions of the module.
    :param print_: type bool: flag, if True, then function will print result, else not print.
    :param mass: type list: non sorted list, if the value of the parameter is not specified,
                            then an array of random numbers is created.
    :return: type list: sorted list
    """

    non_sort_list = mass if mass else lib.generate_int_array()
    sorted_list = bubble_sort(nsl=non_sort_list)

    if print_:
        print('Non sorted list:')
        lib.pretty_print(arr=non_sort_list)
        print('\nList after Bubble sort:')
        lib.pretty_print(arr=sorted_list)

    return sorted_list


if __name__ == '__main__':
    main()
