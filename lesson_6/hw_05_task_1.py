__author__ = 'Шелест Леонид Викторович'
"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия. 
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, 
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""
import memory_profiler


def get_data() -> dict or None:
    """
    The function is ready for keyboard input.
    When using any ready-made data, a function update is required.
    :return: type dict {name_company_1: {'quarters': tuple, 'mean': float}, ...}
             If user input wrong data, then function return None.
    """
    try:
        corp_count = int(input("Введи количество компаний для оценки - "))

        if corp_count:
            result = {}
            print("Введи через пробел Название компании и прибыль за каждый квартал "
                  "(пример - 'Гугель 10000 1556,8 258900,4 20580'): ")

            for i in range(corp_count):
                company_data = input(f"{i+1}. Компания : ").split()

                while len(company_data) != 5:
                    print("Через пробел должны быть перечислены: Название компании, Прибыль за 1, 2, 3 и 4 кварталы")
                    company_data = input(f"{i+1}. Компания: ").split()
                profit = tuple(map(float, company_data[1:]))
                result[company_data[0]] = {'quarters': profit, 'mean': sum(profit) / len(profit)}

            return result

        else:
            return None

    except:
        return None


def analize_data(data: dict) -> dict:
    """
    The function divides the dictionary with companies into two dictionaries:
    comparing the average profit for the quarter with the company's average profit for the quarter for all companies.
    :param data: type dict,
    :return: type dict {'company_above_average': {}, 'company_below_average': {}, 'total_mean': float}
    """

    result = {'company_above_average': {},
              'company_below_average': {},
              'total_mean': 0.0}

    total_sum = sum([sum(data[comp_data]['quarters']) for comp_data in data])
    quarters_count = max([len(data[comp_data]['quarters']) for comp_data in data])
    result['total_mean'] = total_sum / len(data) / quarters_count

    for company in data:
        if data[company]['mean'] > result['total_mean']:
            result['company_above_average'].update({company: data[company]})

        elif data[company]['mean'] < result['total_mean']:
            result['company_below_average'].update({company: data[company]})

        elif data[company]['mean'] == result['total_mean']:
            result['company_is_average'].update({company: data[company]})

    return result

@memory_profiler.profile
def main(data: dict):
    """
    Function wrapper, to obtain, evaluate data and display the result on the screen.
    :return: none
    """

    data = data if data else get_data()

    if data:
        res_dict = analize_data(data=data)
        high_str = '\n * '.join(res_dict['company_above_average'])
        low_str = '\n * '.join(res_dict['company_below_average'])
        result = {'Выше среднего': high_str, 'Ниже среднего': low_str}
        if res_dict.get('company_is_average'):
            avg_str = '\n * '.join(res_dict['company_below_average'])
            result.update({'Средняя прибыль': avg_str})
    else:
        print('К сожалению данные не подходят для обработки.')

    return result


if __name__ == '__main__':
    main()
