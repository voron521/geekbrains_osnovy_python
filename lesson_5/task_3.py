# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

import os

name_file = "my_text_task_3.txt"

my_dict = {
    "Andrew": 45000,
    "John": 35000,
    "Mikle": 70000,
    "Piter": 15000,
    "Nina": 34500,
    "Sike": 14500,
    "Garry": 35600,
    "Sonia": 19800,
    "Leo": 61900,
    "Simlen": 100000
}

average = 0

if os.path.exists(name_file):
    with open(name_file, "w", encoding = "utf-8") as my_obj:
        for i in my_dict:
            my_obj.write(f"{i} {my_dict[i]}\n")
        new_dict = {}
    with open(name_file, "r") as my_obj:
        for i in my_obj.readlines():
            i = i.split()
            new_dict[i[0]] = i[1]
    with open(name_file, "a", encoding = "utf-8") as my_obj:
        for i in new_dict:
            average += int(new_dict[i])
            if int(new_dict[i]) < 20000:
                my_obj.write(f"сотрудник {i} получает оклад меньше 20000\n")
        average = average / len(new_dict)
        my_obj.write(f"Средний оклад сотрудников = {average:.2f}\n")
else:
    print(f"файла с названием {name_file} не существует, вначале создайте его")
