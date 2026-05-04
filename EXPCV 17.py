import cv2
import numpy as np

# Read image in grayscale
image = cv2.imread(r"C:\Users\gowri\Desktop\bird.jpeg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found")
    exit()

# Sobel X
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)

# Convert to absolute
sobel_x = np.absolute(sobel_x)
sobel_x = np.uint8(sobel_x)

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Sobel X Edge Detection", sobel_x)

cv2.waitKey(0)
cv2.destroyAllWindows()
