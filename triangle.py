import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self._x = float(x)
        self._y = float(y)

    def getx(self):
        return self._x

    def gety(self):
        return self._y

    def distance_from_xy(self, x, y):
        return math.hypot(self._x - x, self._y - y)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self._vertice1 = vertice1
        self._vertice2 = vertice2
        self._vertice3 = vertice3

    def perimeter(self):
        return (self._vertice1.distance_from_point(self._vertice2) +
                self._vertice2.distance_from_point(self._vertice3) +
                self._vertice3.distance_from_point(self._vertice1))

    def area(self):
        a = self._vertice1.distance_from_point(self._vertice2)
        b = self._vertice2.distance_from_point(self._vertice3)
        c = self._vertice3.distance_from_point(self._vertice1)
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
triangle2 = Triangle(Point(0, 0), Point(5, 0), Point(0, 5))
print(triangle2.area())
