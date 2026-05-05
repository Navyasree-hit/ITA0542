import cv2
import numpy as np

# Read image
image = cv2.imread(r"C:\Users\gowri\Desktop\bird.jpeg")

if image is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Laplacian kernel with diagonals
laplacian_kernel = np.array([
    [1,  1,  1],
    [1, -8,  1],
    [1,  1,  1]
], dtype=np.float32)

# Apply filter
sharpened = cv2.filter2D(gray, -1, laplacian_kernel)

# Display
cv2.imshow("Original Image", gray)
cv2.imshow("Sharpened Image (Diagonal)", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
