# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


class Clothes():

    def __init__(self, *args, **kwargs):
        self._tissue_consumption = None

    def consumption(self):
        return self._tissue_consumption

    def __str__(self):
        return f"{self.consumption():.2f}"

    def __add__(self, other):
        consump = Clothes()
        consump._tissue_consumption = self.consumption() + other.consumption()

        return consump


class Costume(Clothes):

    def __init__(self, H, *args, **kwargs):
        super().__init__()
        self.growth = H

    def consumption(self):
        if self._tissue_consumption is None:
            self._tissue_consumption = 2 * self.growth + 0.3
        return self._tissue_consumption


class Coat(Clothes):

    def __init__(self, V, *args, **kwargs):
        super().__init__()
        self.size = V

    def consumption(self):
        if self._tissue_consumption is None:
            self._tissue_consumption = self.size / 6.5 + 0.5
        return self._tissue_consumption


cost = Costume(6)
coat = Coat(24)

print(f"На костюм нужно ткани: {cost}")
print(f"На пальто нужно ткани: {coat}")
print(f"Суммарный расход ткани {cost + coat} ")
