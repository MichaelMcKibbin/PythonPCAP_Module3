import math
from Shape import Shape

class Circle(Shape):
    def __init__(self, name, color='green', radius=1):
        super().__init__(name, 'circle', color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Shape: {self.name}"

    def get_type(self):
        return self.shape_type

    def get_color(self):
        return self.color

    def get_area(self):
        return self.area()

    def get_perimeter(self):
        return self.perimeter()

c=Circle("My Circle", "blue", 10)
print(c.get_area())
print(c.get_perimeter())
print(c.get_color())
print(c.get_type())
