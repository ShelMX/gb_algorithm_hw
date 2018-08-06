__author__ = 'Шелест Леонид Викторович'
"""
Module with the functions that are used in each homework.
"""
import random as rnd


def generate_int_array(low: int = -100, up: int = 99, size: int = 100) -> list:
    """
    function generate list of random numbers (int type).
    :param low: type int, lower bound of random numbers, included.
    :param up: type int, upper bound of random numbers, included.
    :param size: type int, qty. of random numbers.
    :return: type list, a list of random numbers, given parameters (largest, smallest random numbers and array size).
    """

    return [rnd.randint(low, up) for _ in range(size)]


def generate_float_array(low: float = 0.0, up: float = 50.0, size: int = 100, rounding: int = None) -> list:
    """
    function generate list of random numbers (float type).
    :param rounding: type int: if the value of the parameter is not specified,
                               then the random number will not be rounded,
                               otherwise rounding occurs with a specified accuracy.
    :param low: type float: lower bound of random numbers, included.
    :param up: type float: upper bound of random numbers. The range [a, b) or [a, b] depending on rounding.
    :param size: type int: qty. of random numbers.
    :return: type list: a list of random numbers, given parameters
                        (largest, smallest random numbers, array size and round).
    """

    if rounding:
        return [round(rnd.uniform(low, up), rounding) for _ in range(size)]

    return [rnd.uniform(low, up) for _ in range(size)]


def pretty_print(arr):
    """
    function print array in line, step = 10.
    :param arr: array to print
    :return: None
    """

    for count, i in enumerate(arr, 1):
        print(f"{i:>5}" if isinstance(i, int) else f"{i:>10}",
              end=' ' if count % 10 else '\n')
