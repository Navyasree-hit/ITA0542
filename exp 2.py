import cv2

# Read image (use normal quotes)
image = cv2.imread("C:/Users/gowri/Desktop/animal.jpeg")

# Check if image loaded
if image is None:
    print("Error: Image not found")
    exit()

# Resize image (make it small for lab)
image_small = cv2.resize(image, (300, 300))

# Gaussian Blur parameters
k_size = (5, 5)
sigma_x = 0

# Apply Gaussian Blur
blurred_image = cv2.GaussianBlur(image_small, k_size, sigma_x)

# Save output image
cv2.imwrite("blurred_image.jpg", blurred_image)

# Display images
cv2.imshow("Original Image", image_small)
cv2.imshow("Blurred Image", blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
