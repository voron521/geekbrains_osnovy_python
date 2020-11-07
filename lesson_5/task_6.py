# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                        Физика:   30(л)   —   10(лаб)
#                                        Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

name_file = "new_txt_task_6.txt"


def del_simbols(my_list):
    """Очищает лист от символов и букв"""
    delfunc_list = [[] for i in range(len(my_list))]
    k = 0
    for i in my_list:
        for j in i:
            try:
                int(j)
                delfunc_list[k].append(j)
            except:
                continue
        delfunc_list[k] = "".join(delfunc_list[k])
        k += 1
    if delfunc_list:
        return (delfunc_list)


with open(name_file, "r") as my_obj:
    my_list = (my_obj.readlines())

my_keys = []
my_values = []
summ_list = []
my_dict = {}

for i in my_list:
    my_list[my_list.index(i)] = i.split()
    my_keys.append(my_list[my_list.index(i.split())][0])
    my_values.append(my_list[my_list.index(i.split())][1:])

summ_list = [[] for i in range(len(my_values))]
n = 0
for i in my_values:
    i = del_simbols(i)
    for j in i:
        try:
            j = int(j)
            summ_list[n].append(j)
        except:
            continue
    n += 1

for i in range(len(my_keys)):
    my_dict[my_keys[i]] = sum(summ_list[i])
print(my_dict)
