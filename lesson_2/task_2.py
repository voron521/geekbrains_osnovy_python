# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

# Ниже цикл для задания длинны списка и его введению с клавиатуры, я его закоменчу чтобы вам не вводить вручную

# is_long = 11
<<<<<<< HEAD
# my_list=[]
=======
# a=[]
>>>>>>> Lesson_2
# while is_long >= 10:
#     is_long = int(input("Введите длинну списка(не более 10, иначе вводить много элементов): "))
#     if is_long <= 10:
#         for i in range(is_long):
<<<<<<< HEAD
#             my_list.append(input(f"Введите {i+1} элемент списка: "))
#     else:
#         print ("Надол было ввести длинну меньше 10, попробуйте еще раз")

my_list = [1, "andrew", 15, 90, ["moskow"], 23, 67, "Hello", 1]

print(f"Начальный вариант списка: {my_list}")

for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(f"Список после замены местами соседних элементов: {my_list}")
=======
#             a.append(input(f"Введите {i+1} элемент списка: "))
#     else:
#         print ("Надол было ввести длинну меньше 10, попробуйте еще раз")

a = [1, "andrew", 15, 90, ["moskow"], 23, 67, "Hello", 1]

print(f"Начальный вариант списка: {a}")

for i in range(0, len(a) - 1, 2):
    a[i], a[i + 1] = a[i + 1], a[i]

print(f"Список после замены местами соседних элементов: {a}")
>>>>>>> Lesson_2
