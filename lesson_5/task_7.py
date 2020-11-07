# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

name_file = "new_txt_task_7.txt"

with open(name_file, "r") as my_obj:
    my_list = (my_obj.readlines())

    my_keys = []
    values = []
    list_profit = []
    list_profit_aver = []
    dict_firms = {}
    dict_average_profit = {}

    for i in my_list:
        my_list[my_list.index(i)] = i.split()
        my_keys.append(my_list[my_list.index(i.split())][0])
        values.append(my_list[my_list.index(i.split())][2:])

    for i in values:
        profit = int(i[0]) - int(i[1])
        if profit > 0:
            list_profit_aver.append(profit)  # без минусов
            list_profit.append(profit)  # с минусами
        else:
            list_profit.append(profit)

    for i in range(len(my_keys)):
        dict_firms[my_keys[i]] = list_profit[i]

    dict_average_profit = {"average_profit": (sum(list_profit_aver)) / len(list_profit_aver)}

    result_list = [dict_firms, dict_average_profit]

    print(result_list)

with open("my_result.json", "w") as write_f:
    json.dump(result_list, write_f)
