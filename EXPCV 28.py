import cv2
import numpy as np

# Read image in grayscale
image = cv2.imread(
    r"C:\Users\gowri\Desktop\lion.jpg",
    cv2.IMREAD_GRAYSCALE
)

if image is None:
    print("Error: Could not load image")
    exit()

# Apply Sobel convolution kernels
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Calculate gradient magnitude (boundary)
gradient = np.sqrt(sobel_x**2 + sobel_y**2)
gradient = cv2.normalize(gradient, None, 0, 255, cv2.NORM_MINMAX)
gradient = gradient.astype("uint8")

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Boundary Image", gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
