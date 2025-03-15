class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Ввод ширины и высоты от пользователя
width = int(input("Введите ширину прямоугольника: "))
height = int(input("Введите высоту прямоугольника: "))

# Создание объекта Rectangle
rect = Rectangle(width, height)

# Вычисление площади и периметра
a = rect.area()
p = rect.perimeter()

print(f"Площадь: {a}")
print(f"Периметр: {p}")
