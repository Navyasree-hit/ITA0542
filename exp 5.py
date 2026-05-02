import cv2
import numpy as np

# Read the image (use raw string for Windows path)
image = cv2.imread("C:/Users/gowri/Desktop/bird.jpeg")

# Check if image loaded
if image is None:
    print("Error: Image not found")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Translation values
tx = 50   # move right
ty = 30   # move down

# Create translation matrix
translation_matrix = np.float32([
    [1, 0, tx],
    [0, 1, ty]
])

# Apply translation
moved_image = cv2.warpAffine(image, translation_matrix, (width, height))

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Moved Image", moved_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
