# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

# number = int(input("введите целое положительное число"))

number = "52567518832"

i = 0
max = number[i]

while i < len(number):
    if int(max) < int(number[i]):
        max = number[i]
    i += 1

print(f"Максимально число в строке: {max}")
