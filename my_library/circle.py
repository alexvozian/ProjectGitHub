from my_library.shape import shape

class circle(shape):
    Radius = None


    def __init__(self, radius):
        self.add_radius(radius)

    def __str__(self):
        return f"Circle have a radius of {self.Radius}. "

    def add_radius(self, radius):
        self.Radius = radius
        return self.Radius

