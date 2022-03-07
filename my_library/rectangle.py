from my_library.shape import shape

class square:
    Width = None
    Length = None

    def __init__(self, width=None, length=None):
        self.set_width(width) or self.set_length(length)
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

    def square_area(self):
        area = self.Width ** 2 or self.Length ** 2
        return area


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

    def rectangle_area(self):
        area = self.Width * self.Length
        return area

    def __eq__(self, other):
        if type(other) != square or rectangle:
            return False
        if (other.Width == self.Width and other.Length == self.Length) or (self.rectangle_area() == other.rectangle_are()):
            return True
        return False

    def __gt__(self, other):
        if type(other) != square or rectangle:
            return False
        if (self.Width > other.Width and self.Length > other.Length) or (self.rectangle_area() > other.rectangle_area()):
            return True
        return False

    def __lt__(self, other):
        if type(other) != square or rectangle:
            return False
        if (self.Width < other.Width and self.Length < other.Length) or (self.rectangle_area() < other.rectangle_area()):
            return True
        return False

    def __le__(self, other):
        return (self == other or self < other) or (self.rectangle_area() == other.rectangle_area() or self.rectangle_area() < other.rectangle_area())

    def __ge__(self, other):
        return (self == other or self > other) or (self.rectangle_area() == other.rectangle_area() or self.rectangle_area() > other.rectangle_area())

    def __add__(self, other):
        if type(other) is not rectangle and square:
            raise Exception('Addition is only allowed for Square and Rectangle objects')
        return rectangle(self.Width + other.Width, self.Length + other.Length)

    def __sub__(self, other):
        if type(other) is not rectangle and square:
            raise Exception('Addition is only allowed for Square and Rectangle objects')
        if (self.Width >= 0 and other.Width >= 0) and (self.Length >= 0 and other.Length >= 0):
            if self.Width - other.Width <= 0 or self.Length - other.Length <= 0:
                raise Exception("The second object is too BIG")
            else:
                return rectangle(self.Width - other.Width, self.Length - other.Length)
        else:
            raise Exception('self.Width, self.Length and other.Width, other.Length should be not less than 0')

    def __mul__(self, other):
        if type(other) is not rectangle and square:
            raise Exception('Addition is only allowed for Square and Rectangle objects')
        return rectangle(self.Width * other.Width, self.Length * other.Length)

    def __mul_by__(self, by):
        return rectangle(self.Width * by, self.Length * by)

