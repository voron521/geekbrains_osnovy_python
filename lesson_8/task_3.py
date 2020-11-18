# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.


class SearchError(Exception):
    def __init__(self, text_error):
        self.my_except = text_error


result_list = []

stop_word = "stop"

while True:
    try:
        print(f"для завершения программы введите '{stop_word}'")
        el = input("Введите число: ")
        if el == stop_word:
            break
        if not el.isdigit():
            raise SearchError(f"вы ввели '{el}' и это не цифра")
        result_list.append(int(el))
    except SearchError as err:
        print(err)

print(result_list)
