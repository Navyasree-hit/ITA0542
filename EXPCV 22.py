import cv2
import numpy as np

# Read image
image = cv2.imread(r"C:\Users\gowri\Desktop\bird.jpeg")

if image is None:
    print("Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Laplacian kernel with positive center coefficient
kernel = np.array([
    [0, -1,  0],
    [-1,  5, -1],
    [0, -1,  0]
], dtype=np.float32)

# Apply sharpening filter
sharpened_image = cv2.filter2D(gray, -1, kernel)

# Display results
cv2.imshow("Original Image", gray)
cv2.imshow("Sharpened Image (Positive Center)", sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
