# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Машина {self.name} поехала"

    def stop(self):
        return f"Машина {self.name} остановилась"

    def turn(self, turned):
        return f"Машина {self.name} повернула на {turned}"

    def show_speed(self):
        if 60 > self.speed > 40:
            print(w_car.show_speed())
        elif self.speed > 60:
            print(w_car.show_speed())
            print(t_car.show_speed())
        else:
            print("Скорость в норме")


class TownCar(Car):
    def show_speed(self):
        return f"Городская машина {self.name} превысила скоро свыше 60км/ч "


class SportCar(Car):
    def car_info(self):
        return f"Cпортивная машина {self.name} цвет {self.color}"


class WorkCar(Car):
    def show_speed(self):
        return f"Рабочая машина {self.name} цвет {self.color} первысила скорость 40 км/ч"


class PoliceCar(Car):
    def check_police(self):
        if self.is_police:
            return f"машина является полицейской"
        else:
            return f"машина не является полицейской"


car_speed = 70
car_color = "Черный"
car_name = "Ford_Focus_3"
police = False
direction = "Лево"

car = Car(car_speed, car_color, car_name, police)
t_car = TownCar(car_speed, car_color, car_name, police)
s_car = SportCar(car_speed, car_color, car_name, police)
w_car = WorkCar(car_speed, car_color, car_name, police)
p_car = PoliceCar(car_speed, car_color, car_name, police)

print(car.go())
car.show_speed()
print(car.turn(direction))
print(p_car.check_police())
print(car.stop())
print(s_car.car_info())
