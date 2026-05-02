import cv2
import numpy as np

# Read image (use raw string for Windows path)
image = cv2.imread(r"C:\Users\gowri\Desktop\bird.jpeg")

# Check if image loaded
if image is None:
    print("Error: Image not found")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Center of image
center = (width // 2, height // 2)

# Rotation angle
angle = 45

# Clockwise rotation (-angle)
clockwise_matrix = cv2.getRotationMatrix2D(center, -angle, 1.0)
rotated_clockwise = cv2.warpAffine(image, clockwise_matrix, (width, height))

# Counter-clockwise rotation (+angle)
counterclockwise_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated_counterclockwise = cv2.warpAffine(
    image, counterclockwise_matrix, (width, height)
)

# Show results
cv2.imshow("Original Image", image)
cv2.imshow("Clockwise Rotation", rotated_clockwise)
cv2.imshow("Counter-Clockwise Rotation", rotated_counterclockwise)

cv2.waitKey(0)
cv2.destroyAllWindows()
