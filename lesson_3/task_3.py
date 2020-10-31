# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(number_1, number_2, number_3):
    my_list = [number_1, number_2, number_3]
    my_list.remove(min(my_list))
    return sum(my_list)


print("Сумма наибольших двух чисел: ", my_func(1, 4, 12))
