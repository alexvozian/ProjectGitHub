#Ex1.1:
from my_library.circle import circle
from my_library.rectangle import rectangle
from my_library.square import square

c1 = circle(5)
c2 = circle(8)
print(c1.circle_area())
print(c2.circle_area())
print(c1 == c2)
print(c1 > c2)
print(c1 < c2)
print(c1 >= c2)
print(c1 <= c2)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1.__mul_by__(3))
print(c2.__mul_by__(6))

r1 = rectangle(3, 5)
r2 = rectangle(6, 7)
print(r1.rectangle_area())
print(r2.rectangle_area())
print(r1 == r2)
print(r1 > r2)
print(r1 < r2)
print(r1 >= r2)
print(r1 <= r2)
print(r1 + r2)
print(r2 - r1)
print(r1 * r2)
print(r1.__mul_by__(3))
print(r2.__mul_by__(6))

s1 = square(3)
s2 = square(6)
print(s1.square_area())
print(s2.square_area())
print(s1 == s2)
print(s1 > s2)
print(s1 < s2)
print(s1 >= s2)
print(s1 <= s2)
print(s1 + s2)
print(s2 - s1)
print(s1 * s2)
print(s1.__mul_by__(3))
print(s2.__mul_by__(6))

#Ex1.2:
from my_library.circle import circle
from my_library.rectangle import rectangle
from my_library.square import square

class shape_service:
    default_inner_color = "white"
    default_outer_color = "black"

    def __init__(self, inner_color, outer_color):
        self.default_inner_color = inner_color
        self.default_outer_color = outer_color

    @staticmethod
    def create_default_circle(radius):
        return f"{circle(radius)} with Inner Color {shape_service.default_inner_color} and Outer Color {shape_service.default_outer_color}"

    @staticmethod
    def create_default_rectangle(width, length):
        return f"{rectangle(width, length)} with Inner Color {shape_service.default_inner_color} and Outer Color {shape_service.default_outer_color}"

    @staticmethod
    def create_default_square(side_length):
        return f"{square(side_length)} with Inner Color {shape_service.default_inner_color} and Outer Color {shape_service.default_outer_color}"

    @staticmethod
    def color_shapes(list_of_shapes:list, inner_color, border_color):
        for el in list_of_shapes:
            print(f"{el} with Inner Color {inner_color} and Border Color {border_color}.")

y = shape_service.create_default_circle(5)
print(y)
z = shape_service.color_shapes([circle(5), rectangle(2, 3), square(7)], "red", "green")
print(z)

#Ex2:
