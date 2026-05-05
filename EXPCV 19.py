import cv2
import numpy as np

# Read image in grayscale
image = cv2.imread(r"C:\Users\gowri\Desktop\bird.jpeg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Image not found")
    exit()

# Sobel X
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_x = np.absolute(sobel_x)

# Sobel Y
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_y = np.absolute(sobel_y)

# Combine X and Y
edge_image = cv2.add(sobel_x, sobel_y)
edge_image = np.uint8(edge_image)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Sobel XY Edge Detection", edge_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
