# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce
from random import randrange

start_list = [randrange(100, 1001, 2) for i in range(10)]


def my_func(param_1, param_2):
    return param_1 * param_2


print(start_list)

print(reduce(my_func, start_list))
