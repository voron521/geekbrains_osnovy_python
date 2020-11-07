# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

import os

name_file = "my_text_task_4.txt"
name_file_result = "my_text_task_4_result.txt"

my_dict = {
    "one": "Один",
    "two": "Два",
    "three": "Три",
    "four": "Четыре",
}

my_list = []

if os.path.exists(name_file):
    with open(name_file, "r") as my_obj:
        for i in my_obj.readlines():
            i = i.split(" — ")
            i[0] = my_dict[i[0].lower()]
            my_list.append(" — ".join(i))
    with open(name_file_result, "w") as my_obj:
        for i in my_list:
            my_obj.write(i)
