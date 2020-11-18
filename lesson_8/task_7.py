# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplNumber:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return f'сумма равна: {self.num_1 + other.num_1} + {self.num_2 + other.num_2} * i'

    def __mul__(self, other):
        return f'Произведение = {self.num_1 * other.num_1 - (self.num_2 * other.num_2)} + {self.num_2 * other.num_1} * i'

    def __str__(self):
        return f'{self.num_1} + {self.num_2} * i'


numbers_1 = ComplNumber(3, 5)
numbers_2 = ComplNumber(1, 16)

print(f"Первые комплексные числа: {numbers_1}")
print(f"Вторые комплексные числа: {numbers_2}")

print(numbers_1 + numbers_2)
print(numbers_1 * numbers_2)
