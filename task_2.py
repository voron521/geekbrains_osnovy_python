# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

# sec = int(input("Введите количество секунд"))
enter_sec = "45650"

enter_sec = int(enter_sec)

hour = enter_sec // (60 * 60)
minut = (enter_sec - (hour * 60 * 60)) // 60
sec = (enter_sec - (hour * 60 * 60)) % 60

print(f'Время: {hour:02}:{minut:02}:{sec:02}')
