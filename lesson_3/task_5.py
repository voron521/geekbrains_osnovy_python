# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def del_simbols(*args):
    """Очищает лист от символов и букв и завершает работу программы в случае если есть символ выхода"""
    new_list = []
    for i in args:
        if i != symbol:
            try:
                new_list.append(int(i))
            except:
                continue
        else:
            new_list.append(symbol)
    return new_list


def str_list(strings):
    """ преобразует строку в список и пробует сделать все элементы int """
    my_list = list(strings.split(" "))
    try:
        my_list = [int(i) for i in my_list]
    except:
        return del_simbols(*my_list)
    return my_list


summa = 0
my_str = "0"
symbol = "@"

while (str_list(my_str)) != None:
    my_str = input("Введите несколько чисел через пробел, если хотите выйти добавьте в строку символ '@:' ")
    my_list = str_list(my_str)
    if symbol in my_list:
        my_list.remove(symbol)
        summa += sum(my_list)
        print(f"Вы внесли в строку символ @ тем самым завершили программу, результат = {summa}")
        break
    else:
        summa += sum(my_list)
        print(f"Все элементы цифры и их сумма = {summa}")
