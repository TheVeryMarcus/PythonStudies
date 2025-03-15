# class Car:
#     def __init__(self, make, max_speed):
#         self.make = make
#         self.max_speed = max_speed
#         self.speed = 0  # Начальная скорость автомобиля
#
#     def display_speed(self):
#         print(f"Текущая скорость: {self.speed} км/ч")
#
#     def accelerate(self):
#         if self.speed + 10 <= self.max_speed:
#             self.speed += 10
#         else:
#             self.speed = self.max_speed
#         self.display_speed()
#
#     def brake(self):
#         if self.speed - 10 >= 0:
#             self.speed -= 10
#         else:
#             self.speed = 0
#         self.display_speed()
#
# # Пример использования:
# my_toyota = Car("Toyota", 180)
# my_toyota.accelerate()  # Увеличивает скорость на 10
# my_toyota.accelerate()  # Увеличивает скорость на 10
# my_toyota.accelerate()  # Увеличивает скорость на 10


class Car:
    def __init__(self, make, max_speed):
        self.make = make
        self.max_speed = max_speed
        self.speed = 0  # Начальная скорость автомобиля

    def display_speed(self):
        print(f"Текущая скорость: {self.speed} км/ч")

    def accelerate(self):
        if self.speed + 10 <= self.max_speed:
            self.speed += 10
        else:
            self.speed = self.max_speed
        self.display_speed()

    def brake(self):
        if self.speed - 10 >= 0:
            self.speed -= 10
        else:
            self.speed = 0
        self.display_speed()

def main():
    print("Выберите модель автомобиля:")
    print("1. Марк I")
    print("2. Марк II")
    print("3. Марк III")

    choice = input("Введите номер модели (1, 2 или 3): ")

    if choice == '1':
        car = Car("Марк I", 160)
    elif choice == '2':
        car = Car("Марк II", 180)
    elif choice == '3':
        car = Car("Марк III", 200)
    else:
        print("Неверный выбор. Создан автомобиль по умолчанию.")
        car = Car("Марк I", 160)

    print(f"Вы выбрали {car.make} с максимальной скоростью {car.max_speed} км/ч.")

    while True:
        action = input("Введите '+' для ускорения, '-' для торможения или 'q' для выхода: ")
        if action == '+':
            car.accelerate()
        elif action == '-':
            car.brake()
        elif action == 'q':
            print("Выход из программы.")
            break
        else:
            print("Неверная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()
