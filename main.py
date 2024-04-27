import numpy as np
from PIL import Image


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


class Canvas:
    """An object where all shapes will be drawn"""
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        # Create 3d numpy area of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, image_path):
        img = Image.fromarray(self.data, 'RGB' )
        img.save(image_path)


image_file = 'canvas.png'
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

canvas_height = int(input("Enter canvas height: "))
canvas_width = int(input("Enter canvas width: "))
canvas_color = tuple(input("Enter canvas color: "))

my_canvas = Canvas(height=canvas_height, width=canvas_width, color=canvas_color)

my_square = Square(100, 100, 50, white, )
my_square.draw(my_canvas)

my_rectangle = Rectangle(300, 300, 100, 50, red)
my_rectangle.draw(my_canvas)

my_canvas.make(image_file)




