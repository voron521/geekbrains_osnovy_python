# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

name_file = "my_text_task_5.txt"

summa = 0

with open(name_file, "w", encoding = "utf-8") as my_obj:
    for i in (randint(0, 100) for i in range(20)):
        my_obj.write(f"{i} ")

with open(name_file, "r", encoding = "utf-8") as my_obj:
    for i in (my_obj.read().split()):
        summa += int(i)

print(f"Сумма всех элементов равна: {summa}")
