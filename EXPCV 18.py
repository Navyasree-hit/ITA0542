import cv2
import numpy as np

# Read image in grayscale
image = cv2.imread(r"C:\Users\gowri\Desktop\bird.jpeg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found")
    exit()

# Sobel Y
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Convert to absolute
sobel_y = np.absolute(sobel_y)
sobel_y = np.uint8(sobel_y)

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Sobel Y Edge Detection", sobel_y)

cv2.waitKey(0)
cv2.destroyAllWindows()
