

import cv2
import numpy as np

# Load image
image = cv2.imread(r"C:\Users\gowri\Desktop\lion.jpg", cv2.IMREAD_GRAYSCALE)

if image is not None:

    # Create kernel
    kernel = np.ones((5,5), np.uint8)

    # Top Hat operation
    top_hat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Top Hat Result", top_hat)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Error: Could not load the image.")
