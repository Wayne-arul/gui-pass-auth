import cv2

# Load the image
img = cv2.imread('output.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find the contours in the image
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Iterate over the contours and detect the shape
num_triangles = 0
num_rectangles = 0
num_circles = 0
for contour in contours:
    # Detect the shape using the number of vertices
    vertices = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True)
    num_vertices = len(vertices)
    if num_vertices == 3:
        num_triangles += 1
    elif num_vertices == 4:
        num_rectangles += 1
    else:
        num_circles += 1

# Count the number of shapes
num_shapes = num_triangles + num_rectangles + num_circles

# Print the results
print("Number of triangles:", num_triangles)
print("Number of rectangles:", num_rectangles)
print("Number of circles:", num_circles)
print("Total number of shapes:", num_shapes)
