import cv2
import numpy as np

# Read image (your path)
image = cv2.imread(r"C:\Users\gowri\Desktop\bird.jpeg")

# Check image
if image is None:
    print("Error: Image not loaded!")
else:
    # Rotation settings
    angle = 45   # rotate 45 degrees
    scale = 1.0

    # Get center and rotation matrix
    h, w = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((w/2, h/2), angle, scale)

    # Apply affine transformation
    output_image = cv2.warpAffine(image, rotation_matrix, (w, h))

    # Show images
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated Image", output_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
