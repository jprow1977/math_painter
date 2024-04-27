class Square:
    """A square shape that can be drawn onto a canvas"""
    def __init__(self, x, y, side_length, color):
        self.x = x
        self.y = y
        self.side_length = side_length
        self.color = color

    def draw(self, canvas):
        """Draws itself into canvas"""
        canvas.data[self.x: self.x + self.side_length, self.y: self.y + self.side_length] = self.color


class Rectangle:
    """A Rectangle shape that can be drawn onto a canvas"""
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        """Draws itself into canvas"""
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color
