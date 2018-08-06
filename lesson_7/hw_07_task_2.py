__author__ = 'Шелест Леонид Викторович'
"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50). 
Выведите на экран исходный и отсортированный массивы.
"""
import hw_07 as lib


def merge_sort(nsl: list) -> list:
    """
    function sorts an array by a merge method.
    :param nsl: type list: non sorted list
    :return: type list: list after merge sort
    """
    sl = nsl[:]
    n = len(nsl)
    if n < 2:
        return sl
    else:
        left_arr = merge_sort(nsl=nsl[:n//2])
        right_arr = merge_sort(nsl=nsl[n//2:n])

        sl = []
        i = 0
        j = 0

        while i < len(left_arr) or j < len(right_arr):
            if not (i < len(left_arr)):
                sl.append(right_arr[j])
                j += 1

            elif not (j < len(right_arr)):
                sl.append(left_arr[i])
                i += 1

            elif not (left_arr[i] > right_arr[j]):
                sl.append(left_arr[i])
                i += 1

            else:
                sl.append(right_arr[j])
                j += 1

        return sl


def main(arr: list=None, print_: bool=True) -> list:
    """
    main function that combines all the functions of the module.
    :param print_: type bool: flag, if True, then function will print result, else not print.
    :param mass: type list: non sorted list, if the value of the parameter is not specified,
                            then an array of random numbers is created.
    :return: type list: sorted list
    """

    non_sort_list = arr if arr else lib.generate_float_array(low=0, up=50, rounding=5)
    sorted_list = merge_sort(nsl=non_sort_list)

    if print_:
        print('Non sorted list:')
        lib.pretty_print(arr=non_sort_list)
        print('\nList after Bubble sort:')
        lib.pretty_print(arr=sorted_list)

    return sorted_list


if __name__ == '__main__':
    main()
