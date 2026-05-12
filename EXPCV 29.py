import cv2
import numpy as np

# Read image in grayscale
image = cv2.imread(
    r"C:\Users\gowri\Desktop\lion.jpg",
    cv2.IMREAD_GRAYSCALE
)

if image is None:
    print("Error: Could not load the image")
    exit()

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Show results
cv2.imshow("Original Image", image)
cv2.imshow("Erosion Result", eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
