# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def naming(self):
        print(self._income)


class Position(Worker):
    def get_full_name(self):
        return f"Имя, Фамилия сотрудника: {self.surname} {self.name}"

    def get_total_income(self):
        return f"Доход сотрудника с учетом премии: {sum(self._income.values())}"


my_dict = {"wage": 1000, "bonus": 500}
employee = Position("Андрей", "Воронов", "Директор", my_dict)

print(employee.get_full_name())
print(employee.get_total_income())
employee.naming()
