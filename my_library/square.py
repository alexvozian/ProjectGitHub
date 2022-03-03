from my_library.rectangle import rectangle


class square(rectangle):
    Width = None
    Length = None

    def __init__(self, width=None, length=None):
        self.set_width(width)
        self.set_length(length)
        if self.Width != None:
            self.Length = self.Width
        elif self.Length != None:
            self.Width = self.Length
        else:
            print(f"Please set square Width or Length")

    def __str__(self):
        return f"Square with Width and Length both equat {self.Width}"

    def set_width(self, width):
        self.Width = width
        self.Length = width
        return self.Width

    def get_width(self, width):
        return self.Width

    def set_length(self, length):
        self.Length = length
        self.Width = length
        return self.Length

    def get_length(self, length):
        return self.Length



