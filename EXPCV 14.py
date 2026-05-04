import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\gowri\Desktop\bird.jpeg")

# Check image loaded or not
if img is None:
    print("Image not found")
    exit()

# Define source points (choose any 4 points from the image)
pts_src = np.array([
    [50, 50],
    [300, 50],
    [300, 300],
    [50, 300]
], dtype=np.float32)

# Define destination points (changed position)
pts_dst = np.array([
    [80, 80],
    [320, 60],
    [340, 340],
    [60, 320]
], dtype=np.float32)

# Find Homography matrix
H, status = cv2.findHomography(pts_src, pts_dst)

# Warp the image
height, width = img.shape[:2]
warped_img = cv2.warpPerspective(img, H, (width, height))

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformed Image", warped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
