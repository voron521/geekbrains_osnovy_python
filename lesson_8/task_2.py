# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class SearchError(Exception):
    pass


try:
    inp_namber = int(input("введите делимое число: "))
    inp_div = int(input("введите делитель: "))
    if inp_div == 0:
        raise SearchError("На ноль делить нельзя!")
    result = inp_namber / inp_div
except ValueError:
    print(SearchError("вы ввели не число!"))
except SearchError as ex:
    print(ex)

else:
    print(f"Все хорошо. Ваше число: {result:.2f}")
