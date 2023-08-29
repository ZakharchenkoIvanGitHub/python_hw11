"""
Задание №5
📌 Дорабатываем класс прямоугольник из прошлого семинара.
📌 Добавьте возможность сложения и вычитания.
📌 При этом должен создаваться новый экземпляр
прямоугольника.
📌 Складываем и вычитаем периметры, а не длинну и ширину.
📌 При вычитании не допускайте отрицательных значений.
"""


class Rectangle:
    """
    Класс прямоугольник.
    Имеется возможность сложения и вычитания периметра.
    """

    def __init__(self, side_a, side_b=0):
        self.side_a = side_a
        if side_b == 0:
            side_b = side_a
        self.side_b = side_b

    def get_perimeter(self):
        """
        метод возвращает периметр
        """
        return 2 * (self.side_a + self.side_b)

    def get_area(self):
        """
        метод возвращает площадь
        """
        return self.side_a * self.side_b

    def __add__(self, other):
        # (self.side_a + other.side_a, self.side_b + other.side_b)
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)

    def __sub__(self, other):
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)

    def __str__(self):
        return f'Периметр 1 прямоугольника = {self.get_perimeter():.2f}'


rectangle1 = Rectangle(7.3)
rectangle2 = Rectangle(5.6, 10.2)
rectangle3 = rectangle1 + rectangle2
rectangle4 = rectangle3 - rectangle2

print(rectangle1)
print(rectangle2)

print(rectangle3)
print(rectangle4)
