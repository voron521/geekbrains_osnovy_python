# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
#  Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
#  (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”# : “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”:   # “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”:   # “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором # каждый ключ — характеристика товара, например название, а значение —  # список значений-характеристик, например список названий товаров.
# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }

# *********************************
# Ниежа закоментил ручной ввод данных


# my_list = []
# for i in range (3):
#     my_list.append((i+1, {"название": input(f"введите название {i+1}: "), "цена": input(f"введите цену {i+1}-го отовара: "), "кол-во": input3q43w(f"введите кол-во {i+1}-го отовара: "), "ед": input(f"введите ед. #измерения {i+1}-го отовара: ")}))

my_list = [
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."}),
    (4, {"название": "видеокамера", "цена": 15000, "количество": 3, "eд": "шт."})
]
my_dict = {}
my_values = []
rezult = []

my_keys = list(my_list[0][1].keys())  # Получение ключей словаря

[my_values.append(list(i[1].values())) for i in my_list]  # Получение значений словаря

val_list = sum(my_values, [])  # Делаем список всех значений словаря

[rezult.append((val_list[i::len(my_values)])) for i in range(len(my_values))]

for i in range(len(my_values)):
    my_dict[my_keys[i]] = rezult[i]

print(f"Заданный список:\n {my_list} \n")
print("Итоговый словарь:\n", my_dict)
