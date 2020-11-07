# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
import os

name_file = "my_text_task_2.txt"

if os.path.exists(name_file):
    with open(name_file, "r") as my_obj:
        count = 0
        for i in my_obj.readlines():
            count += 1
            print(f"В стрроке №{count}  {len(i.split())} слов(а)")
        print(f"Количество строк в файле: {count}")
else:
    print(f"файла с названием {name_file} не существует, вначале создайте его")
