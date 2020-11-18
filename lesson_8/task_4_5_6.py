# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

from abc import ABC, abstractmethod


class ChekError(Exception):
    pass


class Warehouse:  # склад

    def __init__(self, name, dict, *args, **kwargs):
        self.name = name
        self.dict = dict
        self._dict_sklad = {"1 секция склада": [], "2 секция склада": [], "3 секция склада": []}

    def __str__(self):

        result_txt = f"На складе '{self.name}' сейчас:\n\n"

        for key, val in self._dict_sklad.items():
            interm_str = ""
            for el in val:
                interm_str = f"{interm_str}{el}\n"
            result_txt = f"{result_txt}{key}:\n{interm_str}\n"

        return f"{result_txt}"


class Offequipment(ABC):

    @abstractmethod
    def __init__(self, name, energy_consumption):
        self._name = name
        self.energy_consumption = energy_consumption
        self._result = []

    @property
    def on_sklad(self):
        skl_1._dict_sklad[skl_1.dict[self._name.lower()]].append(self._result)
        try:
            if isinstance((self.quantity), str):
                raise ChekError(f"Вы ввели количество {self._name}-ов строкой")
        except ChekError as ex:
            print(ex)



    def __str__(self):
        return f"{self._result}"


class Printer(Offequipment):  # Класс принтер

    def __init__(self, name, energy_consumption, print_speed, printing_technology, quantity):
        super().__init__(name, energy_consumption)
        self.quantity = quantity
        self.print_speed = print_speed
        self.printing_technology = printing_technology
        self._result = [self._name, self.energy_consumption, self.print_speed, self.printing_technology, self.quantity]


class Scanner(Offequipment):  # Класс сканер
    def __init__(self, name, energy_consumption, scan_speed, resolution, quantity):
        super().__init__(name, energy_consumption)
        self.scan_speed = scan_speed
        self.resolution = resolution
        self.quantity = quantity
        self._result = [self._name, self.energy_consumption, self.scan_speed, self.resolution, self.quantity]


class Xerox(Offequipment):  # Класс ксерокс
    def __init__(self, name, energy_consumption, memory, quantity):
        super().__init__(name, energy_consumption)
        self.memory = memory
        self.quantity = quantity
        self._result = [self._name, self.energy_consumption, self.memory, self.quantity]


dict_sclad = {"принтер": "1 секция склада", "сканер": "2 секция склада", "ксерокс": "3 секция склада"}  # склад

skl_1 = Warehouse("Главный", dict_sclad)  # склад

print_1 = Printer("принтер", "5 ватт", "100", "Лазерный", "100шт")  # Принтер
print_1.on_sklad

scan_1 = Scanner("сканер", "10 ватт", "5", "1000dpi", "50шт")  # Сканер
scan_1.on_sklad

xer_1 = Xerox("ксерокс", "16 ватт", "1гб", "40шт")  # Ксерокс
xer_1.on_sklad

xer_2 = Xerox("ксерокс", "5 ватт", "4гб", "10шт")
xer_2.on_sklad

xer_2 = Xerox("ксерокс", "2 ватт", "0,5гб", "1шт")
xer_2.on_sklad

print_2 = Printer("принтер", "300 ватт", "50", "Струйный", "20шт")
print_2.on_sklad

print(skl_1)
