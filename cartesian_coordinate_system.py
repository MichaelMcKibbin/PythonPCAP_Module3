import math

# Each point located on the plane can be described as a pair of coordinates called x and y.
# Store both coordinates as float numbers.
# All the properties should be private
# The objects of the Point class should evaluate the distances between any two points situated on the plane.
# The math.hypot() function can be used to calculate the distance between two points.


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


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
