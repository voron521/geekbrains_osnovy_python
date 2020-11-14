# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

from random import randint

wight_matrix = 4  # Задание длинны матрицы
height_matrix = 3  # Задание высоты матрицы


def create_matrix(width, height):
    """ Создает матрицы """
    return [[randint(0, 20) for i in range(width)] for j in range(height)]


matrix = create_matrix(wight_matrix, height_matrix)

my_list_1 = matrix
my_list_2 = matrix
my_list_3 = matrix


class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        new_list = []
        new_str = ""
        for el in self.list:
            new_list.append([str(j) for j in el])
        for el in new_list:
            new_str = f'{new_str}{" ".join(el)}\n'
        return new_str

    def __add__(self, other):

        is_long = len(self.list[0])
        width = len(self.list)
        result = [[] for i in range(width)]
        for i in range(width):
            for j in range(is_long):
                result[i].append(self.list[i][j] + other.list[i][j])

        return Matrix(result)


matr_1 = Matrix(my_list_1)
matr_2 = Matrix(my_list_2)
matr_3 = Matrix(my_list_3)

print(matr_1)
print(matr_2)
print(matr_3)

print(f"Результат сложения двух матриц: \n{matr_1 + matr_2}")
print(f"Результат сложения трех матриц: \n{matr_1 + matr_2 + matr_3}")
