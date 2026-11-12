import math
from Shape import Shape

class Square(Shape):
    def __init__(self, name, color='blue', side_length=1):
        super().__init__(name, 'square', color)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

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

s=Square("My Square", "red", 5)
print(s.get_area())
print(s.get_perimeter())
print(s.get_color())
print(s.get_type())