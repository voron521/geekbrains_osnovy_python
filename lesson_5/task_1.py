# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

name_file = "my_text_task_1.txt"

with open(name_file, "w", encoding="utf-8") as my_obj:
    my_string = True
    while my_string:
        my_string = input("Введите строку: ")
        my_obj.write(f"{my_string}\n")
