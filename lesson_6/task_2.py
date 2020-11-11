# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def calculation(self, weight, centimeter):
        self.weight = weight
        self.centimeter = centimeter
        return self.__width * self.__height * weight * centimeter


asphalt = Road(12, 6)
weight = 25
centimeter = 5

print(f"Нужно: {asphalt.calculation(weight, centimeter)} т асфальта")
