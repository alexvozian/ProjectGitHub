from my_library.shape import shape


class rectangle(shape):
    Width = None
    Length = None

    def __init__(self, width, length):
        self.add_width(width)
        self.add_length(length)

    def __str__(self):
        return f"Rectangle have Width of {self.Width} and Length of {self.Length}. "

    def add_width(self, width):
        self.Width = width
        return self.Width

    def add_length(self, length):
        self.Length = length
        return self.Length

