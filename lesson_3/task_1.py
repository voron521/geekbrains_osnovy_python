# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def division(number_1, number_2):
    try:
        return print("Результат деления: ", number_1 / number_2)
    except ZeroDivisionError:
        return print("Делить на ноль нельзя")


# number_1 = int(input("Введите число 1: "))
# number_2 = int(input("Введите число 2: "))

number_1 = 2
number_2 = 5

division(number_1, number_2)
