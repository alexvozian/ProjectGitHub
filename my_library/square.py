from my_library.rectangle import rectangle


class square(rectangle):
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

    def __eq__(self, other):
        if type(other) != square or rectangle:
            return False
        if other.Width == self.Width or other.Length == self.Length:
            return True
        return False

    def __gt__(self, other):
        if type(other) != square or rectangle:
            return False
        if self.Width > other.Width or self.Length > other.Length:
            return True
        return False

    def __lt__(self, other):
        if type(other) != square or rectangle:
            return False
        if self.Width < other.Width or self.Length < other.Length:
            return True
        return False

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other

    def __add__(self, other):
        if type(other) is not square and rectangle:
            raise Exception('Addition is only allowed for Square and Rectangle objects')
        if type(other) is square:
            return square(self.Width + other.Width or self.Length + other.Length)
        else:
            return (square.square_area() + other.rectangle_area()) // 2

    def __sub__(self, other):
        if type(other) is not square and rectangle:
            raise Exception('Addition is only allowed for Square and Rectangle objects')
        if (self.Width >= 0 and other.Width >= 0) and (self.Length >= 0 and other.Length >= 0):
            if type(other) is square:
                return square(self.Width - other.Width or self.Length - other.Length)
            else:
                return (square.square_area() - other.rectangle_area()) // 2
        else:
            raise Exception('self.Width, self.Length and other.Width, other.Length should be not less than 0')

    def __mul__(self, other):
        if type(other) is not square and rectangle:
            raise Exception('Addition is only allowed for Square and Rectangle objects')
        if type(other) is square:
            return square(self.Width * other.Width or self.Length * other.Length)
        else:
            return (square.square_area() * other.rectangle_area()) // 2

    def __mul_by__(self, by):
        return square(self.Width * by or self.Length * by)




