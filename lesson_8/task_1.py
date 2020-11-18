# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

from datetime import datetime


class Date:

    def __init__(self, my_date):
        self.my_date = my_date

    @classmethod
    def date_transform(cls, my_date):
        day, month, year = list(map(int, my_date.split("-")))

        return f"{day:02} {month:02} {year:02}"

    @staticmethod
    def valid_date(my_date):
        try:
            day, month, year = list(map(int, my_date.split("-")))
        except ValueError:
            return "в дате присутствуют буквы или символы"
        try:
            datetime(year, month, day)
            return f"{day:02} {month:02} {year:02}"
        except ValueError:
            return "Дата введена не корректно"

    def __str__(self):
        return f"Ваша дата {self.my_date}"


my_date = "15-09-1988"

dates = Date(my_date)
print(dates)

print(Date.date_transform(my_date))

print(Date.valid_date(my_date))

print(my_date)
