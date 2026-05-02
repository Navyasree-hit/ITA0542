import cv2

# Read image (raw string avoids path error)
img = cv2.imread(r"C:\Users\gowri\Desktop\bird.jpeg")

# Check image loaded
if img is None:
    print("Error: Image not found")
    exit()

# Show original image
cv2.imshow("Original Image", img)
cv2.waitKey(0)

# Bigger size
bigger = cv2.resize(img, (800, 800))
cv2.imshow("Bigger Image", bigger)
cv2.waitKey(0)

# Smaller size
smaller = cv2.resize(img, (300, 300))
cv2.imshow("Smaller Image", smaller)
cv2.waitKey(0)

cv2.destroyAllWindows()
