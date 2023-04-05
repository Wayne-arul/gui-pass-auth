from PIL import Image, ImageDraw
import random


def draw_shapes(shapes_list, num_shapes_list):
    # Set the dimensions of the image
    width = 500
    height = 500

    # Define the color
    color = (128, 128, 128)

    # Define the shapes
    shapes = {
        "triangle": "polygon",
        "circle": "ellipse",
        "square": "rectangle"
    }

    # Create a new image
    img = Image.new("RGB", (width, height), (255, 255, 255))

    # Draw the shapes
    draw = ImageDraw.Draw(img)
    for i, shape in enumerate(shapes_list):
        num_shapes = num_shapes_list[i]
        for j in range(num_shapes):
            # Set the size of the shape to 8% of the frame size
            shape_size = int(width * 0.08)
            x1 = random.randint(0, width - shape_size)
            y1 = random.randint(0, height - shape_size)
            x2 = x1 + shape_size
            y2 = y1 + shape_size
            if shape == "triangle":
                # Choose two random points on the bottom edge of the rectangle
                bx1 = random.randint(x1, x2 - shape_size//2)
                by1 = y2
                bx2 = random.randint(bx1 + shape_size//4, x2)
                by2 = y2
                # Choose one random point at the top of the rectangle
                tx = random.randint(x1 + shape_size//4, x2 - shape_size//4)
                ty = y1
                draw.polygon([(bx1, by1), (bx2, by2), (tx, ty)], fill=color)
            elif shape == "circle":
                draw.ellipse([(x1, y1), (x2, y2)], fill=color)
            elif shape == "square":
                draw.rectangle([(x1, y1), (x2, y2)], fill=color)
                # Draw the diagonal line to make it a square
                draw.line([(x1, y1), (x2, y2)], fill=color)

    # Show the image
    img.show()

    # Save the image
    img.save("output.png")


shapes_list = ["triangle", "circle", "square"]
num_shapes_list = [2, 3, 1]
draw_shapes(shapes_list, num_shapes_list)
