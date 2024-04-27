from canvas import Canvas
from shapes import Square, Rectangle

# Get canvas width and height from the user
canvas_height = int(input("Enter canvas height: "))
canvas_width = int(input("Enter canvas width: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black)")

my_canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What would you like to draw? Enter quit to quit. ")
    # Ask for rectangle data and create rectangle if user enters 'rectangle'
    if shape_type.lower() == 'rectangle':
        rec_x = int(input("Enter x of rectangle: "))
        rec_y = int(input("Enter y of rectangle: "))
        rec_width = int(input("Enter width of rectangle: "))
        rec_height = int(input("Enter height of rectangle: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        # Create rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw(my_canvas)

    # Ask for square data and create square if user enters 'square'
    if shape_type.lower() == 'square':
        sqr_x = int(input("Enter x of square: "))
        sqr_y = int(input("Enter y of square: "))
        sqr_side = int(input("Enter length of side: "))
        red = int(input("How much red should the square have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        # Create square
        s1 = Square(x=sqr_x, y=sqr_y, side_length=sqr_side, color=(red, green, blue))
        s1.draw(my_canvas)

    if shape_type == 'quit':
        break

my_canvas.make('canvas.png')





