from my_library.shape import shape
from math import pi


class circle(shape):
    Radius = None


    def __init__(self, radius):
        self.add_radius(radius)

    def __str__(self):
        return f"Circle have a radius of {self.Radius}. "

    def add_radius(self, radius):
        self.Radius = radius
        return self.Radius

    def circle_area(self):
        area = pi * self.Radius**2
        return area

    def __eq__(self, other):
        if type(other) != circle:
            return False
        if other.Radius == self.Radius:
            return True
        return False

    def __gt__(self, other):
        if type(other) != circle:
            return False
        if self.Radius > other.Radius:
            return True
        return False

    def __lt__(self, other):
        if type(other) != circle:
            return False
        if self.Radius < other.Radius:
            return True
        return False

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other

    def __add__(self, other):
        if type(other) is not circle:
            raise Exception('Addition is only allowed for Circle objects')
        return circle(self.Radius + other.Radius)

    def __sub__(self, other):
        if type(other) is not circle:
            raise Exception('Addition is only allowed for Circle objects')
        if self.Radius >= 0 and other.Radius >= 0:
            return circle(self.Radius - other.Radius)
        else:
            raise Exception('self.Radius and other.Radius should be not less than 0')

    def __mul__(self, other):
        if type(other) is not circle:
            raise Exception('Addition is only allowed for Circle objects')
        return circle(self.Radius * other.Radius)

    def __mul_by__(self, by):
        return circle(self.Radius * by)




