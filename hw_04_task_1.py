from timeit import timeit
import cProfile
import sys
sys.setrecursionlimit(2000)

from task_2 import main as algo_1
"""
функция подсчёта чётных и нечётных в числе на число длинной 1000 знаков
         6 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task_2.py:21(analize_data)
        1    0.000    0.000    0.003    0.003 task_2.py:35(main)
        1    0.002    0.002    0.002    0.002 task_2.py:8(get_data)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
from task_4 import main as algo_2
"""
вычисление суммы убывающей арифметической прогрессии для вычисления прогресии 1000 элементов
0.6666666666666667
         500508 function calls (1008 primitive calls) in 0.348 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.348    0.348 <string>:1(<module>)
500500/1000    0.347    0.000    0.347    0.000 task_4.py:13(f_n)
        1    0.000    0.000    0.348    0.348 task_4.py:20(main)
        1    0.001    0.001    0.348    0.348 task_4.py:23(<listcomp>)
        1    0.000    0.000    0.000    0.000 task_4.py:8(get_data)
        1    0.000    0.000    0.348    0.348 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""
from task_7 import main as algo_3
"""
вычисление суммы возрастающей арифметической прогрессии для 1000 элементов
Сумма чисел от 1 до 1000 вычисляется по формуле n*(n + 1)/2 и равна 500,500
         5 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_7.py:9(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""


n = ''.join(map(str, [i for i in range(1000)]))
# print(timeit('algo_1(n=int(n))', number=100))  # выдает ошибку, при импорте функции из модуля
print('\nфункция подсчёта чётных и нечётных в числе')
cProfile.run('algo_1(n=int(n))')

print('\nвычисление суммы убывающей арифметической прогрессии')
cProfile.run('algo_2(1000)')

print('\nвычисление суммы возрастающей арифметической прогрессии')
cProfile.run('algo_3(1000)')
