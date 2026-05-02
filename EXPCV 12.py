import cv2
import numpy as np

# Read image (use raw string r"" to avoid path errors)
image = cv2.imread(r"C:\Users\gowri\Desktop\bird.jpeg")

# Check if image is loaded
if image is None:
    print("Error: Image not found")
    exit()

# Get image size
h, w = image.shape[:2]

# Source points (corners of original image)
pts1 = np.float32([
    [0, 0],
    [w - 1, 0],
    [0, h - 1],
    [w - 1, h - 1]
])

# Destination points (changed for perspective effect)
pts2 = np.float32([
    [50, 50],
    [w - 100, 30],
    [80, h - 50],
    [w - 50, h - 80]
])

# Perspective transform matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply transformation
result = cv2.warpPerspective(image, matrix, (w, h))

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
