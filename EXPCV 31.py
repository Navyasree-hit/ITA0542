# 31. Morphological operations based on OpenCV using Opening technique

import cv2
import numpy as np

# Load image
image = cv2.imread(r"C:\Users\gowri\Desktop\lion.jpg", cv2.IMREAD_GRAYSCALE)

if image is not None:

    # Create kernel
    kernel = np.ones((5,5), np.uint8)

    # Opening operation
    opening_result = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Opening Result", opening_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Error: Could not load the image.")
