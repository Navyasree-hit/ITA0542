import cv2
import numpy as np

image = cv2.imread(r"C:\Users\gowri\Desktop\bird.jpeg")

if image is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

gradient = cv2.magnitude(grad_x, grad_y)
gradient = cv2.convertScaleAbs(gradient)

sharp = cv2.addWeighted(gray, 1.5, gradient, -0.5, 0)

cv2.imshow("Original", gray)
cv2.imshow("Gradient Sharpening", sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()
