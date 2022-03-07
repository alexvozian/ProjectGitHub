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

# y = shape_service.create_default_circle(5)
# print(y)
# z = shape_service.color_shapes([circle(5), rectangle(2, 3), square(7)], "red", "green")
# print(z)