import cv2
import numpy as np

# Read image
image = cv2.imread("C:/Users/gowri/Desktop/bird.jpeg", cv2.IMREAD_GRAYSCALE)

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Apply erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Show output
cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
