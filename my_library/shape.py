class shape():
    Inner_Color = None
    Border_Color = None

    def __init__(self, inner_color, border_color):
        self.add_inner_color(inner_color)
        self.add_border_color(border_color)

    def __str__(self):
        return f"Inner Color is {self.Inner_Color}, and Border Color is{self.Border_Color}. "

    def add_inner_color(self, inner_color):
        self.Inner_Color = inner_color
        return self.Inner_Color

    def add_border_color(self, border_color):
        self.Border_Color = border_color
        return self.Border_Color