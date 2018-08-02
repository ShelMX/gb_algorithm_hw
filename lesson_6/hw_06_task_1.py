__author__ = 'Шелест Леонид Викторович'
"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. 
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
P.S. Напишите в комментариях версию Python и разрядность ОС.
Python = 3.6
OC - Windows10 x64
"""
from pympler import tracker

from hw_05_task_1 import main as company
# Filename: C:\Users\L\PycharmProjects\algo\hw_05_task_1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     71     19.1 MiB     19.1 MiB   @memory_profiler.profile
#     72                             def main(data: dict):
#     73                                 """
#     74                                 Function wrapper, to obtain, evaluate data and display the result on the screen.
#     75                                 :return: none
#     76                                 """
#     77
#     78     19.1 MiB      0.0 MiB       data = data if data else get_data()
#     79
#     80     19.1 MiB      0.0 MiB       if data:
#     81     19.1 MiB      0.0 MiB           res_dict = analize_data(data=data)
#     82     19.1 MiB      0.0 MiB           high_str = '\n * '.join(res_dict['company_above_average'])
#     83     19.1 MiB      0.0 MiB           low_str = '\n * '.join(res_dict['company_below_average'])
#     84     19.1 MiB      0.0 MiB           result = {'Выше среднего': high_str, 'Ниже среднего': low_str}
#     85     19.1 MiB      0.0 MiB           if res_dict.get('company_is_average'):
#     86                                         avg_str = '\n * '.join(res_dict['company_below_average'])
#     87                                         result.update({'Средняя прибыль': avg_str})
#     88                                 else:
#     89                                     print('К сожалению данные не подходят для обработки.')
#     90
#     91     19.1 MiB      0.0 MiB       return result
#
#
#                   types |   # objects |   total size
# ======================= | =========== | ============
#            <class 'list |        3017 |    154.88 KB
#             <class 'str |        3067 |    146.79 KB
#             <class 'int |         225 |      3.10 KB
#            <class 'type |           0 |    352     B
#            <class 'dict |           2 |    204     B
#   function (store_info) |           1 |     72     B
#            <class 'cell |           2 |     56     B
#           <class 'float |           1 |     16     B
#          <class 'method |          -1 |    -36     B
#            <class 'code |          -1 |    -84     B
#           <class 'tuple |          -4 |   -372     B

from hw_05_task_2 import main as hex_calc
# Filename: C:\Users\L\PycharmProjects\algo\hw_05_task_2.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     80     19.6 MiB     19.6 MiB   @memory_profiler.profile
#     81                             def main(a: list=['A', '2'], b: list=['C', '4', 'F']) -> dict:
#     82
#     83     19.6 MiB      0.0 MiB       result_add = addition(add_1=a, add_2=b)
#     84     19.6 MiB      0.0 MiB       result_multi = multiplication(multi_1=a, multi_2=b)
#     85
#     86     19.6 MiB      0.0 MiB       return {f"{a} + {b}": result_add, f"{a} x {b}": result_multi}
#
#
#                                    types |   # objects |   total size
# ======================================== | =========== | ============
#                              <class 'str |          67 |      4.68 KB
#                             <class 'list |           1 |    424     B
#                             <class 'code |           1 |     84     B
#                            <class 'tuple |           2 |     80     B
#                    function (store_info) |           1 |     72     B
#                             <class 'cell |           2 |     56     B
#                            <class 'float |           1 |     16     B
#                              <class 'int |           1 |     14     B
#   <class 'pympler.tracker.SummaryTracker |          -1 |    -32     B
#                           <class 'method |          -1 |    -36     B
#                             <class 'dict |          -1 |   -136     B

from task_4 import main as algo_2
# Filename: C:\Users\L\PycharmProjects\algo\task_4.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     20     19.5 MiB     19.5 MiB   @memory_profiler.profile
#     21                             def main(n: int=None):
#     22     19.5 MiB      0.0 MiB       data = get_data(n=n)
#     23     19.5 MiB      0.0 MiB       if data:
#     24     19.5 MiB      0.0 MiB           return sum([f_n(i) for i in range(1, data + 1)])
#
#
#                                    types |   # objects |   total size
# ======================================== | =========== | ============
#                              <class 'str |          23 |      1.56 KB
#                             <class 'list |           1 |    156     B
#                             <class 'code |           1 |     84     B
#                            <class 'tuple |           2 |     80     B
#                    function (store_info) |           1 |     72     B
#                             <class 'cell |           2 |     56     B
#                            <class 'float |           1 |     16     B
#                              <class 'int |           1 |     14     B
#   <class 'pympler.tracker.SummaryTracker |          -1 |    -32     B
#                           <class 'method |          -1 |    -36     B
#                             <class 'dict |          -1 |   -136     B

tr = tracker.SummaryTracker()
test_hw5_1 = {'gogeel': {'quarters': (1000, 15000, 5000, 22000),
                         'mean': 10750},
              'yendax': {'quarters': (2000, 12000, 8000, 20000),
                         'mean': 10500},
              'mial': {'quarters': (1500, 5000, 7000, 12000),
                       'mean': 6375},
              'remblar': {'quarters': (8500, 1500, 75000, 2000),
                          'mean': 21750}}

company(data=test_hw5_1)
tr.print_diff()
print('\n\n')
tr = tracker.SummaryTracker()
hex_calc()
tr.print_diff()
print('\n\n')
tr = tracker.SummaryTracker()
algo_2(100)
tr.print_diff()
